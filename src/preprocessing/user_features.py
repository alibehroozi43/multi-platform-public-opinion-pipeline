"""Compute cross-video automation-risk features for YouTube authors.

This post-ingestion stage can detect repeated behavior across videos that the
per-video collector cannot. YouTube represents replies as a flat
comment-to-reply structure. Parent-author features such as ``self_reply_ratio``
and ``unique_parent_authors`` may be unavailable for older records without
parent linkage.

Older records may use raw ``author_channel_id`` when ``author_hash`` is absent;
that fallback is legacy compatibility data and must be handled as identifiable
information. Risk weights are heuristics, not estimates trained on labeled bot
ground truth, and require calibration and cautious interpretation.

This module was originally developed by Parmida Mohamadzade as part of the
collaborative pipeline.
"""

import statistics
import sys
from collections import defaultdict
from pathlib import Path
from typing import Iterable

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "ingestion"))
# Keep text, timestamp, and URL semantics consistent with content-level scoring.
from automation_risk import _normalize_text, _parse_ts, _URL_RE  # noqa: E402

# Initial heuristic weights; calibrate before treating scores as decision thresholds.
_WEIGHT_EXACT_DUPLICATE = 0.35
_WEIGHT_RAPID_ACTIVITY = 0.25
_WEIGHT_URL_RATIO = 0.15
_WEIGHT_HOUR_COVERAGE = 0.10
_WEIGHT_COMMENT_LEVEL_MEAN = 0.15  # bridges in Tier A's per-comment score, when available

_RAPID_ACTIVITY_WINDOW_SECONDS = 60

FLAG_THRESHOLD = 0.7  # suggested review threshold, not an auto-exclude rule


def _user_key(record: dict) -> str | None:
    meta = record.get("author_metadata") or {}
    return meta.get("author_hash") or meta.get("author_channel_id")


def build_user_table(records: Iterable[dict]) -> list[dict]:
    """Group records by author and compute cross-video risk features.

    Returns a plain list of dicts so this module
    stays importable without a hard pandas dependency."""
    by_user: dict[str, list[dict]] = defaultdict(list)
    for r in records:
        key = _user_key(r)
        if key:
            by_user[key].append(r)
    return [_features_for_user(key, items) for key, items in by_user.items()]


def _features_for_user(user_key: str, items: list[dict]) -> dict:
    n = len(items)

    texts_norm = [_normalize_text(r["text"]) for r in items if r.get("text")]
    text_counts: dict[str, int] = defaultdict(int)
    for t in texts_norm:
        text_counts[t] += 1
    duplicate_count = sum(1 for t in texts_norm if text_counts[t] > 1)
    exact_duplicate_ratio = duplicate_count / len(texts_norm) if texts_norm else 0.0
    unique_text_ratio = len(text_counts) / len(texts_norm) if texts_norm else 0.0

    post_ids = {r["post_id"] for r in items if r.get("post_id")}
    replies = sum(1 for r in items if r.get("is_reply"))
    reply_ratio = replies / n if n else 0.0

    word_counts = [len((r.get("text") or "").split()) for r in items]
    mean_word_count = statistics.fmean(word_counts) if word_counts else 0.0
    median_word_count = statistics.median(word_counts) if word_counts else 0

    like_counts = [(r.get("author_metadata") or {}).get("like_count") or 0 for r in items]
    mean_like_count = statistics.fmean(like_counts) if like_counts else 0.0

    url_flags = [bool(_URL_RE.search(r.get("text") or "")) for r in items]
    url_interaction_ratio = sum(url_flags) / n if n else 0.0

    timestamps = sorted(ts for ts in (_parse_ts(r.get("date", "")) for r in items) if ts)
    interarrivals = [(b - a).total_seconds() for a, b in zip(timestamps, timestamps[1:])]
    median_interarrival_seconds = statistics.median(interarrivals) if interarrivals else None
    rapid_activity_ratio = (
        sum(1 for gap in interarrivals if gap <= _RAPID_ACTIVITY_WINDOW_SECONDS) / len(interarrivals)
        if interarrivals
        else 0.0
    )
    active_utc_hours = len({ts.hour for ts in timestamps})
    hour_coverage_ratio = active_utc_hours / 24 if timestamps else 0.0

    # Tier A's per-comment automation_risk_score, when the collector already
    # wrote one (v2/v3 data only) - folded in as one more signal, optional.
    comment_scores = [
        r["automation_risk_score"] for r in items if r.get("automation_risk_score") is not None
    ]
    mean_comment_level_score = statistics.fmean(comment_scores) if comment_scores else None

    return {
        "user_key": user_key,
        "total_interactions": n,
        "posts_participated": len(post_ids),
        "replies": replies,
        "reply_ratio": round(reply_ratio, 4),
        "mean_word_count": round(mean_word_count, 2),
        "median_word_count": median_word_count,
        "mean_like_count": round(mean_like_count, 2),
        "url_interaction_ratio": round(url_interaction_ratio, 4),
        "exact_duplicate_ratio": round(exact_duplicate_ratio, 4),
        "unique_text_ratio": round(unique_text_ratio, 4),
        "median_interarrival_seconds": median_interarrival_seconds,
        "rapid_activity_ratio_60s": round(rapid_activity_ratio, 4),
        "active_utc_hours": active_utc_hours,
        "hour_coverage_ratio": round(hour_coverage_ratio, 4),
        "mean_comment_level_automation_risk": (
            round(mean_comment_level_score, 4) if mean_comment_level_score is not None else None
        ),
        "first_activity_utc": timestamps[0].isoformat() if timestamps else None,
        "last_activity_utc": timestamps[-1].isoformat() if timestamps else None,
    }


def score_users(user_rows: list[dict]) -> list[dict]:
    """Adds automation_risk_score_user ([0,1]) and is_flagged_bot_suspect to
    each row, in place, and returns the same list. Heuristic risk score,
    NOT a bot verdict - see docs/cross_platform_alignment_guide_fa.md §4;
    filtering on it is a separate, team-reviewed downstream decision, never
    automatic here."""
    for row in user_rows:
        comment_level = row["mean_comment_level_automation_risk"] or 0.0
        score = (
            _WEIGHT_EXACT_DUPLICATE * row["exact_duplicate_ratio"]
            + _WEIGHT_RAPID_ACTIVITY * row["rapid_activity_ratio_60s"]
            + _WEIGHT_URL_RATIO * row["url_interaction_ratio"]
            + _WEIGHT_HOUR_COVERAGE * row["hour_coverage_ratio"]
            + _WEIGHT_COMMENT_LEVEL_MEAN * comment_level
        )
        row["automation_risk_score_user"] = round(min(1.0, score), 4)
        row["is_flagged_bot_suspect"] = row["automation_risk_score_user"] >= FLAG_THRESHOLD
    return user_rows

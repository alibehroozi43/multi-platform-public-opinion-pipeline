# Pipeline Roadmap

This roadmap records the remaining engineering work for the current Reddit, X, and YouTube pipeline. Methodological requirements are maintained in `docs/`; this file does not replace those contracts.

## Current Architecture

```text
platform collectors
    -> shared raw schema and provenance
    -> intake profiling and eligibility
    -> relevance audit and annotation
    -> validated analytical dataset
    -> temporal, event, and financial analysis
    -> reports and monitoring
```

Each stage writes a versioned artifact or checkpoint so failed and incremental runs can resume without repeating completed collection.

## Completed Foundations

- Configurable topic, source, and query registries
- Reddit two-stage collection and raw-schema conversion
- X browser-based collection with checkpointing
- YouTube video/comment collection and incremental state
- Cross-platform schema harmonization and eligibility rules
- Author hashing and automation-risk features
- Manual labeling samples, LLM route evaluation, and annotation assembly
- Descriptive, temporal, comparative, sensitivity, and event analysis
- Financial-market preparation and social-outcome alignment
- Control Center, VictoriaMetrics collection, and Grafana dashboards

## Remaining Priorities

### Validation

- Expand automated tests for schema transformations, checkpoints, and eligibility edge cases.
- Re-run annotation accuracy and agreement checks when reviewed labels change.
- Record collection coverage and query-execution audit artifacts for each production run.

### Reproducible Execution

- Add a thin orchestrator that calls existing stages without duplicating their logic.
- Validate stage inputs before starting expensive collection or annotation work.
- Persist run identifiers and configuration versions through every downstream artifact.

### Operational Reliability

- Add health checks for browser dependencies and external APIs.
- Keep retry policies bounded and distinguish transient failures from exhausted quotas or invalid credentials.
- Extend monitoring alerts for stale checkpoints, incomplete handoffs, and missing metrics.

### Analysis and Reporting

- Execute notebooks against the final reviewed analytical dataset.
- Export figures and tables with run metadata and data-status labels.
- Keep causal limitations, low-sample weeks, annotation failures, and coverage gaps visible in published results.

## Acceptance Criteria

A portfolio release is ready when:

- tracked configuration contains no credentials or machine-specific paths;
- all Python modules compile and notebooks parse without stored error output;
- documentation references only files present in the snapshot or clearly identifies runtime artifacts;
- collector and analysis behavior remains covered by smoke or targeted tests;
- generated reports identify their source run and whether the data are synthetic or real;
- collaboration credit remains available in `ATTRIBUTION.md`.

# Git Workflow

This portfolio repository uses short-lived branches and pull requests for reviewable changes.

## Repository

```bash
git clone https://github.com/alibehroozi43/multi-platform-public-opinion-pipeline.git
cd multi-platform-public-opinion-pipeline
```

Use `origin` for this repository. Do not add remotes for private or legacy project repositories.

## Branches and Changes

Create a focused branch from the current `main` branch:

```bash
git switch main
git pull --ff-only origin main
git switch -c <name>/<short-description>
```

Keep commits limited to one coherent change. Before committing, review `git status` and the staged diff. Open a pull request to `main`; do not force-push or rewrite shared history.

## Repository Hygiene

- Read credentials from environment variables and keep `.env` untracked.
- Do not commit raw datasets, browser profiles, local databases, logs, or generated outputs.
- Coordinate changes to shared schemas and query contracts because every collector and downstream analysis depends on them.
- Preserve attribution when moving or consolidating collaborative work.
- Resolve conflicts by reviewing both versions and testing the affected workflow; do not discard changes with destructive Git commands.

The tracked `.env.example` documents supported settings without containing working credentials.

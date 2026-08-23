# Multi-Platform Public Opinion Pipeline

An end-to-end pipeline for collecting, harmonizing, annotating, and analyzing public discourse from Reddit, X, and YouTube. It combines reproducible research workflows with operational monitoring through a web Control Center, Grafana, VictoriaMetrics, and Docker Compose.

This repository is a portfolio snapshot of a collaborative academic project. Team attribution and the limits of individual ownership are documented in [ATTRIBUTION.md](ATTRIBUTION.md).

## Pipeline

```text
Reddit / X / YouTube
        |
        v
Ingestion and incremental collection
        |
        v
Schema harmonization and quality checks
        |
        +-- relevance and eligibility
        +-- author privacy and geographic context
        +-- bot / automation-risk signals
        |
        v
Sentiment, stance, emotion, and content-type annotation
        |
        v
Temporal, statistical, event, and financial analysis
        |
        v
Reports, dashboards, and runtime monitoring
```

The ingestion layer handles platform-specific APIs and Selenium-based browser automation while producing shared records. Checkpoints, query registries, provenance fields, and duplicate controls support repeatable incremental runs.

The analytical workflow includes:

- relevance screening and manual audit samples;
- LLM-assisted annotation with route comparison, caching, cost tracking, and evaluation against reviewed samples;
- sentiment, stance, emotion, and content-type analysis;
- descriptive statistics, weekly trends, group comparisons, and sensitivity checks;
- rule-based automation-risk analysis at content and account level;
- registered-event studies and financial/economic time-series alignment.

Automation-risk scores are review signals, not definitive bot classifications. Event and financial results are treated as temporal associations rather than causal effects.

## Data Sources and External Services

- **YouTube:** collection uses the **YouTube Data API v3**. The project API key is provisioned through **Google Cloud Console** and supplied at runtime through the `YOUTUBE_API_KEY` environment variable; credentials are never committed to the repository.
- **Global financial markets:** global market series are collected primarily from **Yahoo Finance** through the `yfinance` workflow. The financial registry covers foreign exchange, crude oil, gold, equity indices, volatility measures, Treasury yields, shipping-related equities, ETFs, and crypto assets. Selected series are also cross-checked against the FRED REST API as an external verification source.

## Pipeline Architecture Map

A detailed map of the end-to-end workflow—from raw data ingestion and harmonization through eligibility, normalization, annotation, statistical analysis, event studies, financial alignment, and final outputs—is shown below.

[![End-to-end pipeline architecture](docs/images/pipeline_architecture.jpg)](https://claude.ai/code/artifact/2257fb34-8166-4fa0-836b-24873bbcd56c)

[**Open the interactive pipeline architecture map**](https://claude.ai/code/artifact/2257fb34-8166-4fa0-836b-24873bbcd56c)

The map also distinguishes optional execution paths such as live ingestion, profiling, financial-data preparation, notebook execution, and the human-reviewed Gold Sample workflow.

## Monitoring and Control Center

The `monitoring/` application provides process controls, live logs, read-only data summaries, runtime metrics, and pipeline-integrity checks. Platform-specific Grafana dashboards cover Reddit, X, YouTube, finance, and overall status. VictoriaMetrics stores scraped metrics, and Docker Compose provisions the monitoring services.

The Control Center applies runtime settings without rewriting the core pipeline configuration where isolation is required. Reddit's two-stage collector is kept sequential because its stages share browser state and handoff files.

## Repository Layout

```text
config/                 Topic, query, calendar, and schema configuration
docs/                   Research design, contracts, and operating guidance
monitoring/             Control Center, dashboards, metrics, and Docker services
notebooks/              Reproducible analytical workflows
scripts/                Supporting execution and synthetic-data utilities
src/annotation/         Annotation, model routing, evaluation, and dataset assembly
src/cost_tracking/      API usage and run-cost accounting
src/event_analysis/     Registered-event analysis
src/ingestion/          Reddit, X, YouTube, and financial ingestion
src/intake/             Input profiling and quality grading
src/preprocessing/      Cleaning, eligibility, deduplication, and relevance audit
src/reporting/          Static analytical dashboard generation
src/temporal_analysis/  Descriptive, temporal, comparative, and sensitivity analysis
src/validation/         Agreement and annotation-accuracy evaluation
```

Runtime data, local databases, logs, credentials, and generated reports are intentionally excluded from version control.

## Setup

Requirements vary by collector. Start with the shared environment:

```bash
git clone https://github.com/alibehroozi43/multi-platform-public-opinion-pipeline.git
cd multi-platform-public-opinion-pipeline
python -m venv .venv
```

Activate the environment and install dependencies:

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
```

Provide credentials only in the local `.env` file. Do not commit API keys, salts, browser profiles, or raw data. Platform-specific configuration is defined in `config/config.yaml`, `config/query_registry.yaml`, and the environment template.

## Running Monitoring

From `monitoring/`:

```bash
docker compose up -d
```

Windows launchers are available at the repository root and under `monitoring/`. The Control Center and collectors also require their platform dependencies, such as Firefox/GeckoDriver for browser-driven workflows.

## Research and Data Constraints

- Collection covers Reddit, X, and YouTube; schemas retain platform provenance and parent relationships.
- Stable author identifiers are salted and hashed where available. Raw salts and unnecessary personally identifiable information are not stored in tracked files.
- Low-sample and partial weeks remain visible in temporal outputs rather than being silently dropped.
- Annotation failures and missing coverage are reported explicitly.
- Raw and interim datasets are local artifacts and are not included in this portfolio snapshot.

Detailed schema, eligibility, sampling, and analysis decisions are in [docs/README.md](docs/README.md).

## Contributions

The project was developed collaboratively. My work focused primarily on financial and economic integration; statistical, temporal, and comparative analysis; analytical validation and reproducibility; and integration and operational testing of the monitoring stack.

Other modules and design decisions were collaborative, and responsibility changed during development. See [ATTRIBUTION.md](ATTRIBUTION.md) for contributor credit without inferring module ownership from this snapshot's clean Git history.

## Portfolio

Ali Behroozi — data science, transportation and mobility analytics, machine learning, simulation, and data engineering. GitHub: [@alibehroozi43](https://github.com/alibehroozi43)

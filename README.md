# Multi-Platform Public Opinion & Sentiment Analysis Pipeline

An end-to-end data engineering, analytics, and observability pipeline for collecting and analysing public discourse across **Reddit, X (Twitter), and YouTube**.

The project combines multi-platform data acquisition, browser automation, data validation, sentiment and relevance analysis, statistical analysis, bot/automation-risk signals, and a monitoring layer with **Grafana, VictoriaMetrics, Docker, and a web-based Control Center**.

> **Portfolio note:** This repository originates from a collaborative academic/team project. This portfolio branch is organised to demonstrate the system architecture, analytical workflow, monitoring stack, and my contributions while preserving team attribution.

---

## Project Overview

The pipeline was designed to study large-scale public opinion around a configurable geopolitical topic while maintaining a reproducible workflow from raw collection to analytical outputs.

At a high level, the system covers:

```text
Reddit / X / YouTube
        │
        ▼
Data Acquisition & Scraping
        │
        ▼
Schema Harmonisation
        │
        ▼
Data Quality & Validation
        │
        ├── Relevance Filtering
        ├── Bot / Automation-Risk Signals
        └── Geographic / Contextual Enrichment
        │
        ▼
Sentiment / Stance / Emotion Analysis
        │
        ▼
Statistical & Temporal Analysis
        │
        ▼
Monitoring / Control Center
        │
        ├── Grafana
        ├── VictoriaMetrics
        └── Live Runtime Metrics
```

---

## Key Capabilities

### Multi-Platform Data Acquisition

The ingestion layer supports multiple public-data sources:

* **Reddit** — post and comment collection
* **X / Twitter** — browser-based scraping and query execution
* **YouTube** — video and comment collection
* Configurable topic and query registries
* Incremental collection and duplicate control
* Shared output schemas across platforms

### Browser Automation & Scraping

The project includes automated collection workflows using tools such as:

* Python
* Selenium
* Firefox / GeckoDriver
* REST APIs where available
* Configurable queries and source registries
* Retry and error-handling logic
* Runtime collection controls

---

## Sentiment & Public Opinion Analysis

The analytical layer supports structured annotation and comparison of public discourse.

Analytical dimensions include:

* Sentiment
* Stance
* Emotion
* Content type
* Relevance
* Confidence scores
* Group comparison
* Sensitivity analysis
* Temporal analysis

The repository also contains evaluation workflows for comparing model-generated labels against manually reviewed samples.

---

## Bot & Automation-Risk Analysis

The pipeline contains mechanisms for identifying suspicious or automated behaviour using account/activity characteristics and rule-based risk signals.

Rather than treating bot detection as a single binary classifier, the workflow supports **automation-risk scoring** and downstream analysis of potentially non-organic activity.

---

## Statistical & Analytical Workflow

The project includes reproducible analytical workflows covering:

* Descriptive statistics
* Group comparisons
* Hypothesis testing
* Sensitivity analysis
* Temporal aggregation
* Financial/economic data integration
* Claim validation and analytical audit outputs

Statistical procedures used across the project include methods such as:

* Chi-square tests
* Fisher's exact test
* Mann-Whitney tests
* Welch's t-tests

---

## Monitoring & Observability

A dedicated monitoring layer provides visibility into collectors and pipeline execution.

The monitoring architecture includes:

* **Grafana** dashboards
* **VictoriaMetrics** metrics storage
* Docker-based monitoring services
* Runtime collector metrics
* Live logs
* Platform-specific dashboards
* Pipeline integrity checks
* Process status and execution controls

Dedicated Grafana dashboards are available for:

* Reddit
* X
* YouTube
* Finance
* Overall pipeline status

---

## Control Center

The repository includes a web-based operational Control Center for managing and observing the pipeline.

The interface provides:

* Collector status
* Read-only data summaries
* Reddit scraper configuration
* YouTube collection controls
* X scraper controls
* Financial-data controls
* Live logs
* Pipeline-integrity validation

Runtime configuration is isolated from the core pipeline logic where possible, allowing the monitoring layer to control execution without rewriting the original source configuration.

---

## Docker Monitoring Stack

The monitoring environment is containerised using Docker Compose.

Core services include:

```text
Grafana
   │
   ▼
VictoriaMetrics
   ▲
   │
Pipeline Metrics
```

The Docker stack also includes Grafana image rendering for dashboard export and reporting.

---

## Technology Stack

### Programming & Data

* Python
* Pandas
* NumPy
* SQL
* JSON / JSONL
* YAML

### Data Collection

* Selenium
* Firefox / GeckoDriver
* REST APIs
* Web scraping

### Analytics & Machine Learning

* Statistical inference
* Sentiment analysis
* Stance analysis
* LLM-assisted annotation
* Relevance classification
* Bot / automation-risk analysis
* Temporal analysis

### Monitoring & Backend

* Grafana
* VictoriaMetrics
* Docker
* Docker Compose
* Python-based web control layer
* Runtime metrics and logging

### Engineering

* Git / GitHub
* Modular pipeline architecture
* Environment-based configuration
* Data validation
* Reproducible analytical workflows

---

## Repository Structure

```text
multi-platform-public-opinion-pipeline/
|-- config/                  # Topic, schema, and pipeline configuration
|-- docs/                    # Methodology and technical documentation
|-- monitoring/              # Control Center, dashboards, and Docker services
|   |-- grafana/             # Dashboards and provisioning
|   |-- static/              # Control Center frontend assets
|   |-- templates/           # Web interface templates
|   `-- victoriametrics/     # Metrics scraping configuration
|-- notebooks/               # Analytical notebooks
|-- reports/                 # Report directory placeholder
|-- scripts/                 # Utility and execution scripts
|-- src/
|   |-- annotation/          # Annotation and model evaluation
|   |-- common/              # Shared JSONL utilities
|   |-- cost_tracking/       # Model/API usage analysis
|   |-- event_analysis/      # Event-study workflows
|   |-- ingestion/           # Reddit, X, YouTube, and financial ingestion
|   |-- intake/              # Input validation and profiling
|   |-- preprocessing/       # Cleaning, eligibility, and relevance workflows
|   |-- reporting/           # Dashboard-report generation
|   |-- temporal_analysis/   # Time-based analytical workflows
|   `-- validation/          # Quality and evaluation procedures
|-- .env.example             # Safe environment-variable template
|-- ATTRIBUTION.md           # Team collaboration credit
|-- README.md
`-- requirements.txt
```

---

## My Contributions

This project was developed collaboratively.

My work focused primarily on:

* Financial and economic data integration
* Statistical analysis and hypothesis testing
* Temporal and comparative analysis
* Analytical workflow validation
* Data-quality and reproducibility checks
* Integration and testing of pipeline monitoring and observability workflows
* Technical debugging and operational testing across the end-to-end pipeline

I also worked with the broader system architecture, including the interaction between data ingestion, analytical outputs, monitoring, Docker-based services, and dashboard components.

Other modules in this repository were developed collaboratively by members of the project team. Detailed team attribution is documented in [`ATTRIBUTION.md`](ATTRIBUTION.md). This portfolio snapshot intentionally uses a clean Git history and preserves collaboration credit separately from the original repository history.

---

## Running the Project

### 1. Clone the repository

```bash
git clone https://github.com/alibehroozi43/multi-platform-public-opinion-pipeline.git
cd multi-platform-public-opinion-pipeline
```

### 2. Create a Python environment

```bash
python -m venv .venv
```

Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Copy the provided template:

```bash
cp .env.example .env
```

On Windows:

```powershell
Copy-Item .env.example .env
```

Add your own API credentials locally.

**Never commit `.env` or API credentials to Git.**

---

## Running the Monitoring Layer

The monitoring environment is located under:

```text
monitoring/
```

From that directory:

```bash
docker compose up -d
```

This starts the containerised monitoring services, including Grafana and VictoriaMetrics.

The repository also includes Windows launcher scripts for the Control Center and Grafana environment.

---

## Data & Security Notes

Runtime artifacts are intentionally excluded from the portfolio repository, including:

* Local `.env` files
* API credentials
* Runtime logs
* Local monitoring databases
* Python cache files

The portfolio repository should therefore contain source code and reproducible configuration templates rather than local execution state.

---

## Project Context

The original project investigates public opinion using multi-platform social-media data and was built as a collaborative analytical pipeline.

The architecture was intentionally designed to be reusable: topics, search terms, source registries, and collection parameters can be changed without redesigning the complete pipeline.

---

## Author / Portfolio

**Ali Behroozi**

Data Scientist | Transportation & Mobility Analytics | Machine Learning | Simulation | Data Engineering

* GitHub: `@alibehroozi43`
* LinkedIn: Ali Behroozi
* Research interests: Machine Learning, Graph Neural Networks, Reinforcement Learning, Transportation Analytics, Data Engineering, Simulation

---

## Attribution

This repository represents collaborative project work.

Detailed collaboration credit is documented in [`ATTRIBUTION.md`](ATTRIBUTION.md). This clean portfolio snapshot is intended to demonstrate my technical contributions and experience working within a larger data-science and software-engineering workflow without reproducing the original repository history.

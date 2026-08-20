# Documentation Index

The documents in this directory define the research design, data contracts, collection scope, and analysis rules used by the pipeline.

## Start Here

- [Project execution order](PROJECT_EXECUTION_ORDER_v1.md) — dependencies between collection, annotation, and analysis stages.
- [Project definition and research design](Chapter_1_Project_Definition_and_Research_Design_v5.md) — research questions, study period, and inference scope.
- [Statistical population and sampling](Chapter_2_Statistical_Population_and_Sampling_Design_v5.md) — population and sampling design.
- [Platform selection](Chapter_3_Platform_Selection_and_Source_Justification_v3.md) — rationale for Reddit, X, and YouTube.

## Data and Collection Contracts

- [Raw schema v0.5](raw_schema_v05.md) and [v0.3 compatibility contract](raw_schema_v03.md)
- [Schema migration notes](schema_migration_v03_to_v05_diff.md)
- [Source registry](source_registry_v4.md) and [query registry](query_registry_v5.md)
- [Eligibility rules](eligibility_rules_v03.md)
- [Legacy-data harmonization](legacy_data_intake_and_harmonization_plan_v1.md)
- [Pipeline B input contract](pipeline_b_input_contract.md)

Intake templates are provided for the data handoff manifest, schema mapping, query-execution audit, and collection coverage. They describe expected structure; populated runtime records are not included in this portfolio snapshot.

## Annotation and Analysis

- [Manual labeling guide](manual_labeling_guide_fa.md)
- [Pre-analysis decision table](pre_analysis_decision_table_v1.md)
- [Event registry](event_registry_v3.md)
- [Cross-platform alignment guide](cross_platform_alignment_guide_fa.md)
- [Data and feature dictionary](data_and_features_dictionary_fa.md)
- [Financial workflow](financial/README_FINANCIAL_WORKFLOW_FA.md)

Documents with explicit version numbers remain available where they record a contract still consumed by code or explain a migration boundary. For current repository structure and setup, see the root [README](../README.md).

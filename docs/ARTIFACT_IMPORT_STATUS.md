# Artifact import inventory (2026-10-19)

This repository was initialized through a GitHub connector that can write UTF-8 text files but **cannot ingest binary artifacts from the local container**. The following files have NOT been imported to GitHub. They remain in the project's ChatGPT ZIP package until uploaded through Git or the GitHub website.

## Available local project artifacts
- Growing_Up_with_Christ_Complete_Reference_Matrix.xlsx
- Growing_Up_with_Christ_Reference_Matrix_v2.xlsx
- Growing_Up_with_Christ_Knowledge_Base_v0_1.zip
- Growing_Up_with_Christ_Phase_0_Baseline.zip
- Growing_Up_with_Christ_Phase_0_Baseline_v1_1.zip
- Growing_Up_with_Christ_Phase_0_Baseline_v1_2.zip
- Growing_Up_with_Christ_Phase_1_Knowledge_Architecture_v1_0.zip
- Growing_Up_with_Christ_Phase_2_Source_Collection_Batch_1.zip
- Growing_Up_with_Christ_Phase_2_Source_Collection_Batch_2A.zip through Batch_2F.zip
- Growing_Up_with_Christ_Phase_2_Consolidation_v0_8.zip
- Growing_Up_with_Christ_Phase_3_Pilot_v0_1.zip
- Growing_Up_with_Christ_Phase_3_Batch_3B_v0_2.zip
- Growing_Up_with_Christ_Phase_3_Batch_3C_v0_3.zip
- Growing_Up_with_Christ_Phase_4_Workflow_v1_0.zip
- growing-up-with-christ-github-ready.zip

## Current GitHub content
- README.md, .gitignore, initial docs
- writing_system/workflow.py and writing_system/test_workflow.py
- The SQLite DB, large research/CSV assets, older versioned archive bundles and Excel reference matrices are **not yet present**.

## Import guidance
1. Extract `growing-up-with-christ-github-ready.zip` locally.
2. Compare its contents with the GitHub checkout and add missing files without replacing newer changes.
3. Store historical release ZIPs in `artifacts/history/` or GitHub Releases (with rights review).
4. Review each included text for copyright, confidential information, and personally identifiable data before sharing.
5. Run `python -m unittest discover -s writing_system -p 'test_*.py'` once inputs are installed.

Do not call the workflow complete until its SQLite input and coverage matrix are present.

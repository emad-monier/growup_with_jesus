# Phase 4 prototype

The runnable reference implementation, source database, chapter CSVs and sample briefs are in the prepared ZIP linked from the project handoff. This GitHub repository is being populated incrementally.

The intended commands are:

```bash
cd writing_system
python workflow.py prepare B04
python workflow.py prepare G05
python -m unittest discover -p 'test_*.py'
```

The prototype **does not integrate an LLM** and its citation checks are structural only. Missing input files must be imported from the reviewed project package before running the CLI.

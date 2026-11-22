# KB-1 — Knowledge-base schema upgrade

The migration is **non-destructive**: input file remains untouched and a separate output database is created.

```bash
python knowledge_base/migrations/kb1_upgrade.py --source knowledge_base/knowledge_base_phase3c.sqlite --output /tmp/knowledge_base_kb1.sqlite
python knowledge_base/migrations/kb1_readiness.py /tmp/knowledge_base_kb1.sqlite --output /tmp/kb1_readiness.json
python -m unittest discover -s knowledge_base/migrations/tests -v
```

New tables: `kb_schema_migrations`, `kb_source_versions`, `kb_claim_revisions`, `kb_passage_provenance`, `kb_review_decisions`, `kb_chapter_requirements`.

The migration does not invent verification approvals, fill missing source text, or change any existing claim states. Reviewer signatures and rights clearances must be supplied by qualified humans. A successful migration is NOT expert review or publication approval.

Note: the readiness script calculates conservative structural indicators and does not grade medical accuracy. Approval must not be inferred from source_checked links.

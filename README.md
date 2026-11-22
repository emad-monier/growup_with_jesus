# Growing Up with Christ

Coptic Orthodox growing-up guides for teenage boys and girls, planned in **English, German and Arabic**.

## Current status

- **49 planned chapters** across two companion guides.
- **Phases 0–2:** editorial structure and source discovery, with unresolved gaps tracked.
- **Phase 3:** pilot evidence extraction for B04 (boys' puberty) and G05 (girls' menstruation).
- **Phase 4:** Python command-line evidence retrieval and citation-ID checking prototype. **No LLM API has been connected and no draft has expert approval.**

## Editorial safeguards

Use source-grounded Coptic Orthodox teaching and medically reliable references. Separate historical/pastoral guidance from medical advice. All health, safeguarding, theological and translation claims require appropriate review before publication. Do not import protected full source texts, credentials, or private individuals' data.

## Repo layout

- `docs/` — editorial policy, outline and project roadmap
- `research/` — source register, permissions, evidence coverage and open questions
- `writing_system/` — Phase 4 prototype code and tests
- `data/` — chapter and source metadata
- `knowledge_base/` — pilot evidence database (to be added after initial code import)

## Next engineering work

1. Import remaining audited project files and SQLite database from the prepared project ZIP.
2. Connect an LLM through an explicit, configurable provider adapter.
3. Add semantic citation checks and review states.
4. Draft B04 and G05 in three languages; seek human review.

The project is **not publication-ready**.
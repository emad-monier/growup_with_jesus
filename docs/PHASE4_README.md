# Growing Up with Christ — Phase 4 writing workflow v1.0

## Scope
A **runnable, offline, evidence-first writing preparation and citation-linting prototype**, built directly on the Phase 3C SQLite database. It does not invoke an LLM or generate completed prose automatically. AI drafting remains a manual step using the generated evidence briefs and prompts, or a future explicitly connected LLM adapter.

## Commands
```bash
python workflow.py prepare B04
python workflow.py prepare G05
python workflow.py check B04 path/to/your_draft.md
python -m unittest -v test_workflow.py
```

## Workflow
1. `prepare` loads chapter-linked claims and source passage metadata, excludes unverified leads from citable material, and produces a JSON brief, Markdown brief, prompt, and skeleton chapter.
2. A writer/model uses the brief and prompt to author original text, preserving citation tokens of form `[CLM:P3C001]` and identifying open decisions using `[REVIEW-NEEDED: ...]`.
3. `check` catches unknown claim IDs, missing tags, and missing required sections. It does **not** prove that a cited source supports the statement in the manuscript: this requires human review of the corresponding source passage.
4. English and Arabic are drafted in coordination; German is adapted from approved content. Every edition needs independent language, doctrine, health, safeguarding, and rights review.

## Safety and provenance
- `grounded_claims` means a source passage record is marked checked and its evidence relationship is marked reviewed, **not** that the claim has passed expert review.
- Do not reproduce source passages or Bible translations as direct quotations without checking permissions.
- No chapter may be marked publication-approved automatically.
- In G05, menstruation and Communion remain a **pastoral review hold**, not a universal Church pronouncement.
- `input/` contains the unchanged Phase 3C pilot database and its exported materials.
- The available record is a curated evidence registry; most entries contain pointers and paraphrases, not original full text.

## Future iteration
Add a separately configured LLM writer and sentence-level entailment evaluator, immutable review decisions, human sign-off UI, multilingual glossary validation, and automated evidence coverage gates. Do not switch on unattended manuscript publication.

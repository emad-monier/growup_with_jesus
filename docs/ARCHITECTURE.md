# Evidence-first authoring architecture

1. **Sources:** Maintain identifiable theological, clinical, liturgical and safeguarding references with provenance and edition data.
2. **Passages:** Record precise locations, reviewed text status and quotation permissions separately.
3. **Claims:** Link each claim to supporting or conflicting passages and chapter objectives; keep unverified leads out of draft evidence.
4. **Research briefs:** Retrieve B04/G05 claims with checked source passages; mark specialist approval as pending.
5. **Writing:** Produce original paraphrased drafts grounded in `CLM` identifiers; never invent exact quotations or Church-wide rulings.
6. **Validation:** Check citation identifiers mechanically, then evaluate semantic support and current guidance through human review.
7. **Editions:** Translate/adapt English -> Arabic and German with separate expert language and ecclesiastical checks.
8. **Publication gate:** No edition ships until theological, medical, safeguarding, editorial and rights gates pass.

## CLI contract

`python workflow.py prepare B04` and `python workflow.py check B04 path/to/draft.md`

The Phase 4 CLI assumes `writing_system/input/knowledge_base_phase3c.sqlite` and `writing_system/input/COVERAGE_MATRIX_3C.csv` exist. Both are supplied in the offline ZIP; the database is not automatically recreated from the present GitHub text files.

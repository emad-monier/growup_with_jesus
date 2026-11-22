# Repository Recovery and Consistency Audit

**Project:** Growing Up with Christ  
**Audit date:** 2026-11-07  
**Scope:** Current working tree only. This audit did not draft chapters, change any existing status, edit research data, or retrieve protected source text.

## Executive finding

The checkout contains a usable Phase 2/3 research subset, a structurally sound
Phase 3 SQLite knowledge base, and a tested Phase 4 evidence-to-draft *prototype*.
It does **not** contain the claimed Phase 0 archive files under their documented
names, their reconciliation CSV, any manuscript, any completed human review, or a
Git repository/history. The project can be recovered into a controlled pilot
preparation state, but it is not ready to begin drafting B04 or G05 without first
resolving the blocking evidence, review, and provenance conditions below.

Terms used in this report:

- **Verified fact**: observed in this checkout or produced by a documented local
  check during this audit.
- **Documented claim**: asserted by a project file but not independently proved by
  the checkout.
- **Not assessed**: requires a qualified human, an unavailable archive, or source
  text/rights access beyond this audit.

## Method and limits

The audit read all project documentation and enumerated tracked and hidden working
tree content (excluding no directory; there is no `.git` directory). It inspected
the SQLite schema and contents, ran its integrity and foreign-key checks, ran the
available Python tests using `python3`, checked the current HTTP response for each
distinct URL recorded in the evidence-passages table, and searched the project and
its nearby parent directories for Git metadata and named archive bundles.

There is no Git repository at or above this checkout, no local branch/ref/log/object
database, and no remote URL to inspect. Therefore Git recovery, branch comparison,
and remote-ref recovery were **not available**. This is a limitation, not evidence
that no upstream repository or archive exists elsewhere.

The documented commands use `python`; the local shell has no `python` executable,
but has Python 3.12.3 as `python3`. The tests below passed with `python3`. The test
run created only ignored cache files; they are not project deliverables.

## Available artifact inventory

| Area | Verified available artifacts | Assessment |
|---|---|---|
| Project control | `README.md`; 13 files in `docs/` before this audit | Present, but portions are stale or contradictory. |
| Editorial baseline | `EDITORIAL_GUIDELINES.md`, `BOYS_OUTLINE.md`, `GIRLS_OUTLINE.md`, `DECISION_LOG.md`, `REVIEW_POLICY.md` | Working archival reconstructions are present. They are not present under the exact controlled filenames claimed by the closure documents. |
| Registries | `data/chapters.csv` (49 rows), `orthodox_sources.csv` (19), `medical_sources.csv` (16) | Present. This matches the ID cardinalities stated in the master plan, but does not independently verify each source. |
| Phase 2 research | source manifest (69 rows), 12-gap register, 8-row rights register, 10-row patristic inventory, policy and consolidation audit | Present; it is discovery/collection metadata, not a cleared source corpus. |
| Phase 3 research | B04/G05 evidence briefs, 10-row coverage matrix, 11 evidence additions | Present. Both pilot scopes remain incomplete/conditionally usable only. |
| Knowledge base | `knowledge_base_phase3c.sqlite`, duplicated byte-for-byte in `writing_system/input/` | Present and integrity-checked. SHA-256 for both copies: `4ca8996ce39a5bc82fef05ae6637b9d609f76817acf2b3fbfdfe6fdc322f9dff`. |
| Writing prototype | `writing_system/workflow.py`, tests, and two supplied input files | Present and tested; it has no LLM/provider integration. |
| Migration/CI | non-destructive KB-1 migration/readiness scripts, tests, GitHub Actions workflow | Present. No migrated KB-1 output database is checked in. |
| Examples | B04/G05 draft templates and evidence briefs | Present; templates are not chapter drafts or approvals. |
| Binary reference matrix | `research/Reference_Matrix_v2.xlsx` | Present. It cannot be assumed identical to either differently named matrix claimed in the import inventory. |
| Manuscripts/reviews/permissions | No manuscript files, signed reviews, or cleared licenses found | Not started/not supplied. |
| Repository history | No `.git`, refs, remotes, releases, or archive bundles found locally | Unavailable for recovery. |

## Missing referenced files and locations

The following are explicitly named in project documentation but absent from this
checkout. “Possible counterpart” identifies related material only; it must not be
silently treated as the missing controlled artifact.

| Referenced item | Referenced by | Finding | Possible counterpart / recovery source |
|---|---|---|---|
| `EDITORIAL_GUIDELINES_FULL_v1_0.md` | master plan, issue plan, Phase 0 closure | **Missing.** | `docs/EDITORIAL_GUIDELINES.md` contains a controlled reconstruction and similar scope, but filename and claimed 1–19 archive provenance differ. Recover from Phase 0 v1.2 ZIP or original approved conversation. |
| `BOYS_FULL_ORIGINAL_OUTLINE.md` | master plan, issue plan, Phase 0 closure | **Missing.** | `docs/BOYS_OUTLINE.md` is a controlled reconstruction of 23 chapters. Recover/compare against Phase 0 v1.2 ZIP or original conversation. |
| `GIRLS_FULL_ORIGINAL_OUTLINE.md` | master plan, issue plan, Phase 0 closure | **Missing.** | `docs/GIRLS_OUTLINE.md` is a controlled reconstruction of 26 chapters. Recover/compare against Phase 0 v1.2 ZIP or original conversation. |
| `OUTLINE_REGISTRY_RECONCILIATION.csv` | master plan, issue plan, Phase 0 closure | **Missing.** | No equivalent reconciliation file found. This is needed to substantiate the stated 49/49 alignment and 36 title variants. |
| `test_results.txt` | Phase 4 validation | **Missing.** | No prior test artifact found. Current tests pass, but that does not recreate the historical result. |
| `Growing_Up_with_Christ_Complete_Reference_Matrix.xlsx` | artifact-import status | **Missing.** | No exact filename found. |
| `Growing_Up_with_Christ_Reference_Matrix_v2.xlsx` | artifact-import status | **Missing under this name.** | `research/Reference_Matrix_v2.xlsx` is present; identity is unverified. |
| `Growing_Up_with_Christ_Knowledge_Base_v0_1.zip` and all listed Phase 0–4 ZIP bundles | artifact-import status | **Missing.** | No archive bundle found locally. Recover from the stated ChatGPT ZIP package, original workstation, release storage, or a source repository if one is supplied. |
| `growing-up-with-christ-github-ready.zip` | artifact-import status | **Missing.** | No local copy found. |
| `artifacts/history/` | artifact-import status | **Missing.** | No historical-artifact directory exists. |
| Controlled production files named in editorial guideline §16: manuscripts, `THEOLOGICAL_REFERENCE_LIBRARY`, `CHAPTER_SOURCE_MAPPING`, `TRILINGUAL_GLOSSARY`, `FACT_CHECK_AND_REVIEW_LOG`, `COPYRIGHT_AND_PERMISSIONS_REGISTER` | editorial guideline | **Missing as controlled project artifacts.** | Phase 2 registers partially cover source/rights work only; no general review log, glossary, or manuscript exists. |

Items such as `workflow.py`, the two writing-system inputs, and `ISSUE_RESOLUTION_PLAN.md`
are present. Paths such as `/tmp/...`, `path/to/draft.md`, and generated
`*_DRAFT_PROMPT.md` names are examples/runtime outputs rather than missing project
deliverables.

## Documentation inconsistencies

1. `PROJECT_MASTER_PLAN.md`, `ISSUE_RESOLUTION_PLAN.md`, and
   `PHASE0_CLOSURE_REPORT.md` say ISS-007 and ISS-008 are resolved by four exact
   archive/reconciliation files. All four exact files are absent. Related outline
   and guideline documents exist under different names, but the reconciliation is
   absent; therefore the claimed closures cannot be verified from this checkout.
2. `ARTIFACT_IMPORT_STATUS.md` says the SQLite database, large CSV assets, and
   reference matrix are not present in the current GitHub content. This checkout
   does contain the SQLite database, research CSVs, and `Reference_Matrix_v2.xlsx`.
   The note is stale or describes another checkout.
3. `README.md` says the pilot database is “to be added after initial code import,”
   while both required copies are present and identical.
4. `PHASE4_VALIDATION.md` claims local test results in `test_results.txt`; that
   artifact is absent. Current test success confirms present behavior only.
5. Phase 4 documentation calls the workflow retrieval-assisted, but the code
   supports only B04/G05, reads a prebuilt local database, and does no semantic
   entailment check, web retrieval, LLM call, or multilingual consistency check.
   Its own validation document correctly identifies these exclusions.
6. The master plan says Phase 1’s gate requires traceable source and immutable IDs.
   IDs and a schema exist, but the checked-in Phase 3 database does not include the
   KB-1 provenance/revision/review tables; those are only applied by an optional
   migration to a new output database.
7. Project status says Phase 1 is completed and Phase 2 has 77 discovery records.
   The database does have 77 `phase2_source_discovery` rows; the standalone manifest
   has 69 rows. The difference is not explained in the documentation.

## Phase-by-phase verified completion matrix

| Phase / requirement | Classification | Evidence and limitation |
|---|---|---|
| 0 — editorial decisions and working outlines | **PARTIALLY COMPLETE** | Guidelines, decisions, and 23/26 chapter outlines exist. The exact closure archives/reconciliation used to mark ISS-007/008 resolved are not found. |
| 1 — schema, traceability, immutable IDs | **PARTIALLY COMPLETE** | CSV IDs, Phase 3 schema, and a non-destructive KB-1 upgrade exist. The baseline DB has valid foreign keys, but no applied KB-1 provenance/revision/review tables and no immutable-version workflow evidence. |
| 2 — lawful source acquisition and precise anchors | **PARTIALLY COMPLETE** | 77 discovery rows in DB; 69 manifest rows; 24 checked passages; policy/registers exist. All 12 gap-register rows are open, rights register contains 5 `uncleared`, 1 `contact_required`, 1 `edition_check`, and 1 `review_needed`; no source corpus or permissions are supplied. |
| 3 — B04/G05 claim evidence | **PARTIALLY COMPLETE** | DB passes `integrity_check` and has 51 chapter-claim mappings. B04: 20 mapped / 7 source-checked; G05: 31 / 11. All 40 claims are `partially_verified` or `unverified`; none are `verified`; zero review records exist. |
| 4 — evidence-first drafting/check prototype | **VERIFIED COMPLETE** *(prototype scope only)* | The CLI, inputs, migration tooling, and CI config exist. Six local unit tests passed (3 workflow + 3 migration). It mechanically rejects unknown citation IDs. It is not an LLM agent, semantic verifier, or approval system. |
| 5 — pilot chapter production in EN/AR/DE | **NOT STARTED** | Templates and briefs exist; no pilot prose or three-language editions exist. |
| 6 — English/Arabic manuscript batches | **NOT STARTED** | No manuscript files found. |
| 7 — German adaptation/terminology review | **NOT STARTED** | No translations or glossary found; the German Bible decision remains provisional. |
| 8 — qualified human reviews/sign-off | **NEEDS HUMAN REVIEW** | No review rows/signatures or approved decisions in the database; documentation explicitly says review is pending. |
| 9 — design, rights, and publication | **NOT STARTED** | No design assets, permissions, print/e-book artifacts, or approvals found. |

### Issue-plan status audit

| Issue | Classification | Audit finding |
|---|---|---|
| ISS-001 source full text | **PARTIALLY COMPLETE** | Exact locators/URLs exist for 24 passages, but full source text is intentionally not stored and claims are not fully verified. |
| ISS-002 medical claims | **NEEDS HUMAN REVIEW** | Clinical sources are linked, but no specialist review or approved claim exists. |
| ISS-003 patristic quotations | **PARTIALLY COMPLETE** | Inventory/metadata exists; no evidence of primary-work/translation verification for all quotations. |
| ISS-004 rights | **NEEDS HUMAN REVIEW** | Permission register is open/uncleared; no licenses found. |
| ISS-005 German Bible | **NEEDS HUMAN REVIEW** | Decision remains provisional; no qualified pastoral confirmation found. |
| ISS-006 human review | **NEEDS HUMAN REVIEW** | No reviewer decisions/signatures found. |
| ISS-007 guidelines archive | **DOCUMENTED BUT NOT FOUND** | Marked resolved, exact stated archive absent; related guideline exists. |
| ISS-008 outlines/reconciliation | **DOCUMENTED BUT NOT FOUND** | Marked resolved, exact archives and reconciliation absent; related outlines exist. |
| ISS-009 live URLs | **PARTIALLY COMPLETE** | Current check reached 18 of 20 distinct passage URLs with HTTP 200. CDC and NHS Inform returned HTTP 403 to the audit client, which is inconclusive. The wider source inventory was not fully rechecked. |
| ISS-010 concept depth | **NOT STARTED** | Coverage matrix exists, but no manual learning-objective coverage audit was found. |
| ISS-011 age disaggregation | **PARTIALLY COMPLETE** | Ages 12–18 are documented; no maturity-band tagging or pilot feedback is recorded. |
| ISS-012 menstrual guidance currency | **NEEDS HUMAN REVIEW** | Current-access ACOG FAQ links and an explicitly older 2015 opinion are recorded, but formal current-guideline evaluation and specialist confirmation are absent. |

## Evidence and source-traceability assessment

### Verified structural facts

- SQLite `PRAGMA integrity_check` returned `ok`; `foreign_key_check` returned zero
  errors.
- It contains 49 chapters, 55 sources/works, 24 passages, 40 claims, 36
  claim-evidence links, 51 chapter-claim mappings, and zero review rows.
- All 24 passages are marked `checked`. All evidence links have a source URL and
  locator; 11 links are marked `reviewed` and 25 `unreviewed`.
- The readiness script reports 7 source-checked claims for B04 and 11 for G05, with
  zero claims marked verified and zero approved review entries in both cases.
- The current reachability check returned HTTP 200 for 18/20 distinct passage URLs.
  The CDC and NHS Inform URLs returned HTTP 403 to this automated client; no
  conclusion about their content or permanence follows from that response.

### Interpretation

The research artifacts are genuine *traceability metadata*, not placeholders: they
contain claim IDs, source URLs, passage locators, classifications, checked-read
statuses, and explicit review holds. They do **not** establish that every summary is
an accurate paraphrase, that a current source remains clinically suitable, that an
ecclesiastical interpretation is correct, or that a quotation/reuse is permitted.
The project correctly labels the available material `source_checked_not_expert_approved`.
That label must be retained.

## AI-agent/workflow architecture

No repository-local agent definitions, skills, prompt library, provider adapter,
or LLM client were found. The reusable project components are:

| Component | Reusable next-phase role | Boundary |
|---|---|---|
| `writing_system/workflow.py` | Produce B04/G05 evidence briefs and reject unregistered citation tokens | Supports only B04/G05 and structural checks; it does not establish semantic support or approval. |
| Phase 3 SQLite DB | Source/claim/passage lookup for the two pilots | All claims remain partial/unverified; duplicate DB copies need an ownership rule before edits. |
| `kb1_upgrade.py` and `kb1_readiness.py` | Create a non-destructive upgraded copy and report conservative readiness | Upgrade is not presently applied and cannot create evidence/reviews. |
| `test_workflow.py`, migration tests, GitHub Actions workflow | Regression checks and future CI | Current workflow does not run writing-system tests and assumes `python`, which Actions supplies but this local shell does not. |
| CSV registries and Phase 2/3 reports | Controlled research and gap tracking | They require reconciliation with DB and human review. |

Before any AI writing integration, introduce an explicit provider interface, immutable
input/version manifest, output quarantine, semantic-review queue, language-review
states, and audit logging. This is a recovery recommendation, not a change made by
this audit.

## Pilot-production blockers

The following block the start of controlled pilot drafting, not merely publication:

1. Recover or formally supersede the missing Phase 0 archive/reconciliation
   artifacts, then correct the ISS-007/008 evidence trail without silently changing
   their status.
2. Reconcile the 77 DB discovery records with the 69-row manifest and identify the
   authoritative data source/version for each duplicate input file.
3. Complete a learning-objective/claim coverage audit for B04 and G05, including
   the 13 B04 and 20 G05 leads excluded by the readiness tool.
4. Have a qualified clinician confirm the currency, scope, and adolescent-safe
   phrasing of B04/G05 medical claims; specifically resolve ISS-012 before G05.
5. Obtain qualified Coptic Orthodox clergy/theological review of B04 sources and a
   current pastoral ruling for menstruation and Communion before wording that topic.
6. Complete safeguarding review and age/maturity-band decisions for the pilots.
7. Decide permissions/quotation approach: retain original paraphrase only until
   rights clearance, and do not use protected direct quotations.
8. Establish a controlled reviewer/sign-off log. The current database has zero
   reviews, and a source link is not an approval.

The following block publication but need not prevent a clearly labeled, quarantined
internal pilot after the preceding gates: all-edition language review, German Bible
approval, full permissions, signed publication gate, and design/production work.

## Recovery options and prioritized plan

1. **Preserve and acquire (highest priority).** Obtain the original ChatGPT ZIP
   package or another authoritative archive. Recover the four Phase 0 controlled
   files, versioned ZIPs, and historical matrix; calculate checksums and record
   source, acquisition date, and rights constraints before copying anything in.
2. **Reconcile, do not overwrite.** Compare recovered files against the present
   guideline/outlines and registries. Produce a new reconciliation record showing
   identity, differences, and authority. Only then amend status evidence through a
   deliberate decision-log update.
3. **Restore repository provenance.** Obtain the intended Git remote/clone or
   initialize a new repository only after an authorized preservation snapshot. Until
   then, no Git-history recovery claim can be made. Store binary release bundles in
   controlled artifact storage with checksums rather than treating the working tree
   as complete history.
4. **Make Phase 1 operational.** Create a non-destructive KB-1 upgraded database,
   preserve the Phase 3 baseline checksum, designate canonical DB/CSV locations,
   and resolve the duplicated input ownership. Do not edit claims during migration.
5. **Close pilot evidence gates.** Revalidate the selected source editions and
   passages, update medical currency, perform the B04/G05 coverage audit, and add
   qualified decisions to a review log.
6. **Only then authorize an internal pilot.** Generate English pilot drafts from
   evidence briefs with visible review flags; hold Arabic/German adaptations until
   core wording and terminology are reviewed. No publication or chapter-generation
   action was taken in this audit.

## Local verification record

Executed successfully with Python 3.12.3:

```text
python3 -m unittest discover -s writing_system -p 'test_*.py' -v
# 3 tests passed
python3 -m unittest discover -s knowledge_base/migrations/tests -p 'test_*.py' -v
# 3 tests passed
python3 knowledge_base/migrations/kb1_readiness.py knowledge_base/knowledge_base_phase3c.sqlite
# integrity ok; zero foreign-key errors; B04 7, G05 11 source-checked claims
```

These checks verify code/database behavior at audit time only. They do not verify
theology, clinical accuracy, safeguarding, copyright, translation quality, or
publication readiness.

## Recovery import addendum — 2026-11-07

After this audit, the user supplied `Christ_Recovery.zip`. Its SHA-256 is
`d9171edf70796c635b5fbea58e4bd24e9da6fcd791adb61d65acd8afff114e61`; ZIP
integrity passed. The archive contains the four Phase 0 artifacts listed as missing
above, all historical Phase 0–4 bundles, a GitHub-ready bundle, and the historical
Phase 4 `test_results.txt`.

Non-destructive import was performed with no overwrite permitted. The reconciliation
CSV is now restored at `docs/OUTLINE_REGISTRY_RECONCILIATION.csv`; it has 49 rows,
49 unique IDs, and 36 title variants, with every row reporting an ID/order match.
The three controlled Phase 0 originals are preserved under
`artifacts/recovery/phase0/`; each is byte-identical to its existing document under
`docs/`. Eighteen historical ZIPs are preserved under `artifacts/history/`, and the
historical Phase 4 test output is at `artifacts/recovery/phase4/test_results.txt`.

See `artifacts/recovery/RECOVERY_IMPORT_MANIFEST.md` for destination paths,
checksums, verification method, and status boundary. This resolves the audit's
artifact-availability finding only; no issue status, evidence status, or completion
claim was changed by the import. The archive does not contain Git metadata, so the
Git-history limitation remains.

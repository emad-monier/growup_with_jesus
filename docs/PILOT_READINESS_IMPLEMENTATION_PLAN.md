# Phase 5 Pilot Readiness — Detailed Implementation Plan

**Scope:** B04 (*Puberty — What’s Happening to My Body?*) and G05
(*Understanding My Period*).  
**Objective:** Make an evidence-bounded internal pilot package and test the
evidence-to-draft workflow before qualified human review. This plan does not
authorize publication, status inflation, or use of unlicensed quotations.

## Working rules

- Execute one numbered step at a time and obtain user confirmation before starting
  the next step.
- Do not overwrite research, database, archive, or documentation artifacts.
- Record evidence facts, reviewer decisions, and unresolved questions separately.
- Treat a checked URL/locator as traceability metadata, not expert approval.
- Keep direct quotations out of draft-ready material until rights and wording are
  explicitly cleared.
- Preserve the current status vocabulary: source checked, partially verified,
  review pending, and approved are not interchangeable.
- Use Arabic as the primary working language for pilot review and correction. Record
  substantive correction decisions first against the Arabic draft, then reconcile
  English and German adaptations without changing source meaning.

## Gate sequence

| Step | Deliverable | What it establishes | Completion test | User checkpoint |
|---|---|---|---|---|
| 1 | `CANONICAL_INPUTS_MANIFEST.md` | Which existing files are authoritative baselines, working copies, archives, and duplicates | Hashes, row counts, and DB integrity recorded; no files changed | Required before Step 2 |
| 2 | `PILOT_COVERAGE_GATE.md` | B04/G05 learning objectives mapped to supported claims, excluded leads, and gaps | Every objective classified as covered, partial, or gap; no claim upgraded | Required before Step 3 |
| 3 | `PILOT_SOURCE_CURRENCY_REGISTER.md` | Source version/date/reachability review and current-guideline follow-up list | Each pilot medical/pastoral source has a recorded current-state result or explicit limitation | Required before Step 4 |
| 4 | Internal English pilot drafts | A non-public pipeline test with explicit holds and registered citation markers | Structural citation check passes; no review claim added | User-authorized on 2026-11-07 |
| 5 | Internal Arabic/German adaptations | A multilingual pipeline test derived from the held English drafts | Structural/source-marker checks pass; all holds survive in each language | User confirmation required |
| 6 | `PILOT_REVIEW_PACKETS.md` | Focused questions, evidence references, and acceptance criteria for clergy, clinician, safeguarding, and language review | Each reviewer domain has a bounded packet and decision field | Deferred until after internal multilingual drafts |
| 7 | `PILOT_REVIEW_LOG_TEMPLATE.md` | A controlled place to record named reviewer decisions without treating them as approvals in advance | Fields support decision, date, scope, rationale, and unresolved items | Deferred until reviewer engagement |
| 8 | `PILOT_DRAFTING_GATE.md` | Whether reviewed drafts may be reader-facing | All critical blockers have explicit decisions and revisions | Required before any reader-facing use |

## Step detail

### Step 1 — Canonical inputs and provenance

Inventory the current Phase 0–4 working inputs and recovered historical sources.
Use SHA-256 checksums and simple integrity/row-count checks. Designate roles only:
baseline, runtime copy, registry, reconciliation, or historical artifact. Do not
merge duplicate files, alter workflow code, or infer approval from a checksum.

### Step 2 — Coverage and claim boundary audit

For B04 and G05, compare each coverage-matrix objective with its chapter-claim
links and the workflow’s eligible evidence set. List source-checked claims, leads
that must be excluded, and objectives with insufficient support. Explicitly isolate
the G05 Communion issue and any claims needing clinical/safeguarding review.

### Step 3 — Source currency and retrievability review

Review the selected pilot URLs and recorded publication/version metadata. Record
the access date, response or access limitation, publisher/institution, locator,
and whether a more current guideline needs specialist confirmation. Do not copy
protected source text or make a clinical conclusion from availability alone.

### Step 4 — Internal English pipeline drafts

Create original English working drafts for B04 and G05 using registered citation
markers only. Exclude or visibly flag material outside the eligible evidence set.
Run the existing structural citation check. The drafts are not a substitute for
review and cannot be distributed, translated, or represented as approved.

### Step 5 — Internal Arabic/German adaptations

Create non-public Arabic and German adaptations from the held English drafts to
test multilingual handling. Preserve citation markers and every review hold; do not
claim theological equivalence, native-language quality, or publication suitability.

### Step 6 — Human-review packets

Prepare decision-focused packets, not manuscripts. The theological packet must ask
about doctrinal/pastoral accuracy and the current practice question concerning
menstruation and Communion. The clinical packet must cover age-appropriate health
claims and red flags; the safeguarding packet boundaries, autonomy, abuse language,
and age bands; language packets terminology and meaning parity; the rights packet
quotation/paraphrase constraints.

### Step 7 — Controlled review logging

Create a review record format with reviewer role, credential/identity reference,
scope, evidence version/checksum, decision, date, rationale, required revisions,
and approval limits. No reviewer field may be pre-populated as approved.

### Step 8 — Reader-facing gate decision

Evaluate Step 1–5 evidence against the project’s acceptance criteria. The output
must say one of: `HOLD`, `INTERNAL DRAFT WITH SPECIFIC HOLDS`, or `READY FOR
QUALIFIED REVIEW`. It cannot say publication-ready. If drafting is later allowed,
it begins with original English prose only and carries the agreed review flags.

## Current blocking conditions

1. B04/G05 claims are not expert-approved; the current database has zero review
   decisions.
2. G05’s menstruation/Communion wording needs qualified current Coptic pastoral
   review before categorical guidance.
3. Medical and safeguarding specialist review is required for pilot content.
4. Rights and direct-quotation permissions remain unresolved.
5. German Bible choice and multilingual language review remain pending; they are
   publication blockers and will constrain later adaptation.

## Status at plan creation

**Step 1: COMPLETE.** Its manifest is `docs/CANONICAL_INPUTS_MANIFEST.md`.  
**Step 2: COMPLETE.** Its coverage decision is `docs/PILOT_COVERAGE_GATE.md`.  
**Step 3: COMPLETE.** Its currency register is `docs/PILOT_SOURCE_CURRENCY_REGISTER.md`.  
**Step 4: COMPLETE.** The drafts and structural check are recorded in
`drafts/internal/` and `docs/PILOT_DRAFT_PIPELINE_CHECK.md`.  
**Step 5: COMPLETE.** Internal Arabic and German adaptations passed the same
structural citation check as the English drafts. The trilingual review copy is at
`review/pilot_drafts_trilingual.html`. Qualified reviews remain deferred until the
user authorizes Step 6.
**Step 6: NOT STARTED.** Await explicit user confirmation.

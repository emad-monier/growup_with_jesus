# Pilot Coverage Gate — Step 2

**Scope:** B04 and G05 against the canonical Phase 3 baseline recorded in
`CANONICAL_INPUTS_MANIFEST.md`.  
**Method:** Compared the 10 objectives in `research/phase3/COVERAGE_MATRIX_3C.csv`
with chapter-claim mappings in `knowledge_base/knowledge_base_phase3c.sqlite` and
the eligibility rule in `writing_system/workflow.py`.

## Boundary rules used

- **Eligible** means the current CLI exposes a claim because it has a supporting,
  checked passage and `reviewed` evidence status. It does not mean clinically,
  theologically, or editorially approved.
- **Lead only** means a mapped claim is currently excluded by the CLI. It cannot be
  cited in an internal draft unless its evidence status is deliberately reviewed in
  a later controlled step.
- **Covered with holds** means relevant eligible claims exist but qualified review
  is still mandatory.
- **Partial/gap** means the stated objective needs content that is missing from the
  eligible claim set, is overly broad, or remains dependent on excluded leads.

## Baseline counts

| Chapter | Mapped claims | CLI-eligible claims | Excluded leads | Claim status / approvals |
|---|---:|---:|---:|---|
| B04 | 20 | 7 | 13 | All mapped claims are `partially_verified`; zero human review decisions. |
| G05 | 31 | 11 | 20 | All mapped claims are `partially_verified`; zero human review decisions. |

## B04 objective audit

| Objective | Relevant eligible claim IDs | Lead-only / excluded material | Gate assessment | Required action |
|---|---|---|---|---|
| Puberty and developmental variation | `P3C004`, `P3C005` | `CLM-3B005`–`CLM-3B007` provide more specific boys’ development material but are excluded. | **Covered with clinical hold.** The eligible claims support a general puberty explanation and timing variation, not a full account of erections, wet dreams, or voice changes. | Clinician must confirm scope/wording; assess eligible evidence for the omitted boys-specific topics before any use. |
| Gentle hygiene, skin, hair and genital care | None | `CLM-3C001`–`CLM-3C003` are the mapped hygiene/skin claims; all are excluded. | **GAP.** The coverage matrix labels this source-supported, but no relevant hygiene claim is eligible in the present CLI. | Review the existing hygiene evidence, record source/clinical decision, then add only approved claims to a later controlled evidence set. |
| Body dignity / church tradition | `P3C001`, `P3C002`, `P3C003` | `CLM-3B001`–`CLM-3B004` provide additional pastoral framing but are excluded. | **Covered with clergy hold.** Eligible material supports dignity, care, and non-shaming language. | Clergy/theological reviewer must confirm interpretation, age suitability, and any doctrine/pastoral distinction. |
| Urgent safety and support | `P3C011` | `CLM-3B013`, `CLM-3B014` are excluded; the latter is the specific child-abuse/reporting lead. | **PARTIAL.** Eligible material supports age-appropriate health education broadly, but not localized reporting routes or specific safety guidance. | Safeguarding reviewer must define age-band wording, reporting language, and country/localization handling. |

### B04 mapping anomaly

The CLI exposes `P3C006` for B04, but its claim concerns menstruation. It is not
relevant evidence for a boys’ puberty chapter and must not be used merely because
the chapter-claim mapping permits it. This is a mapping-quality finding, not a
claim-status change.

## G05 objective audit

| Objective | Relevant eligible claim IDs | Lead-only / excluded material | Gate assessment | Required action |
|---|---|---|---|---|
| Menstrual basics and early-cycle variability | `P3C004`–`P3C008` | `CLM-3B007`–`CLM-3B009`, `CLM-3C007`–`CLM-3C009` add specific ranges/thresholds but are excluded. | **Covered with clinical hold.** General naturalness, timing variation, first-period timing, and assessment triggers have eligible support. | Confirm current guideline version and the age-appropriate presentation of numerical thresholds. |
| Period products and practical hygiene | None | `CLM-3C004`–`CLM-3C006` cover products, disposal, hygiene, and TSS precautions; all are excluded. | **GAP.** The objective has no eligible claim in the current workflow. | Clinical reviewer must validate product/hygiene language and decide which claims can enter a reviewed evidence set. |
| Period pain/heavy-flow warning signs | `P3C009`, `P3C010` | `CLM-3B010`–`CLM-3B012`, `CLM-3C008`–`CLM-3C009` add detailed thresholds and irregularity guidance but are excluded. | **PARTIAL.** Eligible claims support seeking help for pain/heavy flow affecting life, but not the full warning-sign detail. | Confirm safety-net wording and current thresholds with an adolescent-health clinician. |
| Bodily dignity and spiritual support | `P3C001`, `P3C002`, `P3C003` | `CLM-3B001`–`CLM-3B003` are excluded supporting pastoral material. | **Covered with clergy hold.** Eligible material supports non-shaming dignity and support. | Clergy/theological reviewer must confirm pastoral framing and distinguish spiritual guidance from medical guidance. |
| Menstruation and Communion / church practice | None | `CLM-3C010`, `CLM-3C011` are excluded and describe an attributed historical pastoral position. | **HOLD.** The coverage matrix already marks current applicability unconfirmed. | Obtain qualified current Coptic Orthodox pastoral guidance before any categorical statement. Do not use this as a general Church-wide rule. |
| Age-appropriate safeguarding | `P3C011` | `CLM-3B013`, `CLM-3B014` are excluded; specific reporting/safety content is not eligible. | **PARTIAL.** General age-appropriate education is supported; actionable safeguarding details are not. | Safeguarding reviewer must approve age bands, boundaries, reporting language, and localization. |

## Claim-boundary findings

1. The coverage matrix is an objective-level planning record, not proof that every
   subtopic has a currently eligible claim.
2. The current CLI filters to reviewed evidence links, yielding a deliberately
   smaller citable set than the chapter mappings. This is functioning as a safety
   boundary, not a data error.
3. Both pilots have material designated `draft_with_review` in the coverage matrix,
   but neither meets an expert-review or publication gate.
4. Hygiene/product guidance is the clearest evidence-to-workflow gap: it is mapped
   for B04/G05 but currently excluded from the citable set.
5. B04 has an overbroad chapter-claim association (`P3C006`); later work should
   correct mapping scope in a versioned output rather than edit the baseline.

## Step 2 gate decision

**Result: HOLD FOR REVIEW-PACKAGE PREPARATION; NOT READY FOR CHAPTER DRAFTING.**

The pilot has enough traceability to prepare review packets, but lacks eligible
coverage for hygiene/product guidance, localized safety detail, and the G05
Communion question. No claim status was changed, no evidence was added, and no
chapter content was generated.

## Next step boundary

Step 3 may review current source metadata and retrievability for the claims above.
It must record access/version limitations and required clinical/clergy review; it
must not promote any claim, copy protected text, or create chapter prose.

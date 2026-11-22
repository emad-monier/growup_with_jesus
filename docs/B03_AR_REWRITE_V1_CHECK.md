# B03 Arabic Reader Draft v1 — Draft Check

**Reader draft:** `drafts/internal/B03_AR_READER_DRAFT_v1.md`  
**Authoring brief:** `drafts/internal/B03_AR_AUTHORING_BRIEF.md`  
**Editorial layer:** `drafts/internal/B03_AR_EDITORIAL_NOTES_v1.md`  
**Reviewer copy:** `review/B03_AR_READER_DRAFT_v1.html`  
**Status:** Internal first draft only; not approved, not publishable, not for distribution.

## What v1 is

B03 — «شخصيتي ومشاعري: لستُ مجرد مزاج عابر» — is the first Arabic reader
draft for the chapter *Personality and Feelings*. It follows the accepted
Arabic-first house workflow: the reader question, scene, spiritual thread, and
voice were authored in Arabic first, with the editorial notes kept as a separate
non-reader layer. No prior version was overwritten.

The chapter moves from a fictional school scene (anger after a teasing remark)
through honest naming of feelings, the difference between feeling and action,
calm speech, loneliness and longing, and when to seek help. Two chapter-mapped
verses and two short Christ-life scenes — Gethsemane (مر 14: 32–34) and the tomb
of Lazarus (يو 11: 33–35) — carry the spiritual thread, with a brief phrase from
رو 12: 15. Two named Coptic pastoral voices and the Coptic Encyclopedia
commentaries on متى 26 and يوحنا 11 are attributed paraphrases; the WHO fact sheet
supplies only general public-health framing. The closing prayer is original and
not a quotation.

## Source boundaries held

| Material | Form in reader copy | Boundary |
|---|---|---|
| أم 15: 1 (Smith–Van Dyke) | Short quotation, marked in the HTML | Chapter-mapped; not a rule to stay silent when harmed |
| مز 42: 1 (Smith–Van Dyke) | Short quotation, marked in the HTML | Chapter-mapped; longing neither diagnosed nor shamed |
| مر 14: 32–34 (Smith–Van Dyke) | Short narrative quotation, marked in the HTML | In context before the arrest; no invented dialogue or emotion |
| تفسير متى 26 (الموسوعة الكنسية) | Attributed paraphrase, marked in the HTML | «ساعة واحدة» = a short period; facing distress alone is hard; page not in the source manifest and not rights-cleared |
| يو 11: 33–35 (Smith–Van Dyke) | Short narrative quotations, marked in the HTML | In context at the tomb before the raising; no added feelings |
| تفسير يوحنا 11 (الموسوعة الكنسية) | Attributed paraphrase, marked in the HTML | Christ's tender humanity and sharing in sorrow; page not in the source manifest and not rights-cleared |
| رو 12: 15 | Short phrase «بكاء مع الباكين», marked in the HTML | Not chapter-mapped; same edition/permissions check as the other quotations |
| يع 1: 19 | Checked but **not quoted** | Kept in reserve to avoid stacking three chapter-mapped verses |
| البابا شنودة الثالث، *الهدوء* | Attributed paraphrase, marked in the HTML | No quotation; online edition/headings still need a stable house locator |
| الأب تادرس يعقوب ملطي، *دعوني أنمو!* | Attributed paraphrase, marked in the HTML | No quotation; hosted text not cleared for republication |
| WHO, *Mental health of adolescents* (2025-09-01) | General framing only | No diagnosis, no statistic, no clinical rule |
| Bishop Moussa, *مكونات الشخصية الإنسانية* | **Excluded** | `catalog_verified_pdf_not_examined` (P2C-003); no content claim taken |
| St John Chrysostom, *On Divine Providence* | **Excluded** | `intro_verified` only (P2D-010); no doctrinal or psychological claim taken |
| St Poemen saying | **Excluded** | Pending ISS-003 verification; no saying attributed from memory |

Full locators, verification dates, and permitted-use notes are in
`drafts/internal/B03_AR_EDITORIAL_NOTES_v1.md`.

## Verification results

Run 2026-11-22 with `b03_verify3.py` (letters-only Arabic token counts, so
diacritics and punctuation do not distort comparison). This run includes the two
Christ-life scenes added during the pre-review drafting pass.

### Structure and length

| Section | Tokens | House target | Result |
|---|---:|---:|---|
| قصة في البداية | 280 | 250–350 | OK |
| لنتحدث بصراحة | 217 | 180–250 | OK |
| ما ينبغي أن تعرفه | 714 | 600–800 | OK |
| أنت أكبر من مزاجك | 430 | 300–450 | OK |
| أسئلة قد تخجل من طرحها | 454 | 450–600 | OK |
| خطوة عملية | 181 | 180–250 | OK |
| فكّر في الأمر | 96 | 90–125 | OK |
| صلاة من القلب | 94 | 90–125 | OK |
| **Total** | **2466** | **2000–2500** | **OK** |

Q&A blocks: 5. Hidden English section comments retained for the legacy
checker: all 3 present.

### Markdown ↔ HTML synchronization

- Arabic tokens in Markdown: **2466**; in the HTML `<main>` body: **2466**.
- **Exact synchronized text match: True.**
- The HTML contains 7 `sacred-text` and 4 `tradition-text` spans (bold/purple),
  applied at the HTML layer only; the Markdown reader copy carries no spans.

### Reader-layer cleanliness

Zero occurrences in the Markdown of: `[CLM:`, `[REVIEW-NEEDED:`,
«تشير مجموعة الأدلة», «من المهم أن», «لا داعي للخجل», «هذا الأسبوع», the
feminine-form slips carried over from B01 v5 («قولي», «اكتبي», «لستِ»,
«تستطيعين»), or any HTML tags. Masculine forms used consistently throughout
the boys' chapter. Both Christ-life scenes name their references, invent no
dialogue or feelings, and use the modest bridge «قد يضيء لنا هذا الموقف…».

### Encoding

All four B03 files decode as valid UTF-8 with no BOM, matching the rest of the
Arabic drafts.

## Legacy structural-check caveat

`writing_system/workflow.py check` still accepts only `{B04, G05}` and requires
`[CLM:<claim-id>]` citation tokens in the reader text. Replicating its logic
against the clean B03 reader copy gives:

- `citation_tokens: 0`
- `invalid_citations: []`
- `missing_sections: []`
- `structurally_valid: False` — solely because zero citation tokens are present
- `publication_approved: False` (always)

This `False` is an intentional consequence of the accepted decision to keep
evidence IDs, claim tokens, and review flags **out of the reader layer**. It is
not a content failure. The mismatch is left documented rather than fixed here;
adapting the checker to accept clean Arabic reader drafts is a separate tooling
decision for the project owner. «Source checked» never equals expert-approved
or publication-ready.

## Open review gates

Human review remains open; no chapter is approved and the `reviews` table has
zero rows. Before B03 can advance:

1. Deacon/pastoral review of attributed paraphrases, theological tone, and terminology.
2. Confirm the approved Arabic Bible edition and quotation rights for all five Scripture
   uses now present (أم 15: 1، مز 42: 1، مر 14: 32–34، يو 11: 33–35، رو 12: 15), plus the
   reserved يع 1: 19.
3. Choose a stable house edition/locator for *الهدوء* and resolve the online-heading caveat.
4. Youth/language review for age suitability and local Arabic register.
5. Mental-health clinician and safeguarding review of the escalation section and WHO framing.
6. Rights clearance for any hosted pastoral text, including the two Coptic Encyclopedia
   commentary summaries; adapt local emergency routes before publication.
7. Register the newly consulted narrative passages and commentary pages in the source
   manifest if the project requires every consulted source to be listed.
8. Confirm the in-place v1 revision. The house rule says a substantive change requires a
   new version; the two scenes were added to the still-unreviewed v1 during drafting, so
   a formal v2 should be cut if that rule is enforced at review time.
9. English/German adaptation only after the Arabic text is reviewed and frozen.

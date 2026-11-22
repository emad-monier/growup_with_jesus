# Internal Pilot Draft Pipeline Check — Step 4

**Run date:** 2026-11-07  
**Draft status:** Internal only; not reviewed, not approved, not distributable.

| Draft | Path | Citation tokens | Invalid citation IDs | Required sections missing | Structural result | Publication result |
|---|---|---:|---:|---:|---|---|
| B04 | `drafts/internal/B04_EN_INTERNAL_DRAFT.md` | 8 | 0 | 0 | Pass | Not approved |
| G05 | `drafts/internal/G05_EN_INTERNAL_DRAFT.md` | 12 | 0 | 0 | Pass | Not approved |
| B04 (Arabic) | `drafts/internal/B04_AR_INTERNAL_DRAFT.md` | 8 | 0 | 0 | Pass | Not approved |
| G05 (Arabic) | `drafts/internal/G05_AR_INTERNAL_DRAFT.md` | 12 | 0 | 0 | Pass | Not approved |
| B04 (German) | `drafts/internal/B04_DE_INTERNAL_DRAFT.md` | 8 | 0 | 0 | Pass | Not approved |
| G05 (German) | `drafts/internal/G05_DE_INTERNAL_DRAFT.md` | 12 | 0 | 0 | Pass | Not approved |

## Commands executed

```text
cd writing_system
python3 workflow.py prepare B04
python3 workflow.py prepare G05
python3 workflow.py check B04 ../drafts/internal/B04_EN_INTERNAL_DRAFT.md
python3 workflow.py check G05 ../drafts/internal/G05_EN_INTERNAL_DRAFT.md
```

The preparation commands produced the existing prototype’s evidence briefs/prompts.
The check commands accepted only registered claim IDs and found all required
structural headings. They do not verify semantic support, clinical accuracy,
theological accuracy, safeguarding suitability, rights, language quality, or
publication readiness.

The current checker recognizes English heading strings only. The Arabic drafts
therefore contain non-rendered HTML comments with those structural anchors; their
reader-visible headings remain Arabic. This is a temporary pipeline compatibility
workaround, not Arabic language validation.

## Trilingual review copy

`review/pilot_drafts_trilingual.html` provides a chapter and language selector for
the English, Arabic, and German internal drafts. It renders Arabic right-to-left,
highlights registered citation markers and review holds, and supports printing the
selected draft. It loads the Markdown source drafts at runtime; serve the repository
with `python3 -m http.server` rather than opening the HTML directly as `file://`.
The embedded JavaScript passed a Node syntax check. The viewer is a reading aid, not
a review, translation, or approval tool.

## Holds retained in both drafts

- B04: hygiene/skin care, specific boys’ puberty content, local safeguarding and
  reporting guidance require qualified review.
- G05: period products/hygiene, detailed thresholds, pain/safety-net wording, and
  localized safeguarding guidance require qualified review.
- G05: no universal/current statement about menstruation and Communion is included;
  qualified Coptic Orthodox pastoral review remains required.
- Both: direct quotations are excluded; all review domains remain pending.

## Step 4 decision

**PASS — internal pipeline operation demonstrated.** This is not an approval gate.
The next planned step is to prepare review packets for the deferred review stage.

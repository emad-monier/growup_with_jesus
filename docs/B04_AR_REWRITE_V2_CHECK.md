# B04 Arabic Reader Draft v2 — Implementation Check

**Reader draft:** `drafts/internal/B04_AR_READER_DRAFT_v2.md`  
**Editorial layer:** `drafts/internal/B04_AR_EDITORIAL_NOTES_v2.md`  
**Reviewer copy:** `review/B04_AR_READER_DRAFT_v2.html`  
**Status:** Internal draft only; not approved for publication or distribution.

## Change made

The original citation-marked pipeline draft is preserved. Version 2 rewrites the
reader layer in Arabic-first, youth-facing prose and adds short, chapter-mapped
Scripture moments from Psalm 139:13 and 1 Corinthians 6:19.

## Boundary checks

- No internal citation IDs, review flags, database language, or placeholder sources
  appear in the reader layer.
- Scripture supports dignity and wise care; it is not used as medical advice or as
  a substitute for a clinician, safeguarding action, or formal Church guidance.
- The text avoids detailed male-puberty and hygiene claims that remain outside the
  current eligible evidence set.
- The original B04 source and approval holds remain unchanged.

## Legacy pipeline result

The existing `writing_system/workflow.py check B04` validator is designed for
the older internal-draft format: it requires visible `[CLM:...]` tokens in the
Markdown source. This clean reader draft deliberately keeps those identifiers in
the separate editorial-notes file, so the legacy checker reports **no invalid
citations and no missing sections**, but `structurally_valid: false` because its
token count is zero. This is a tooling-format limitation, not a claim that the
reader copy passed or failed expert review. The prior B04 pipeline draft remains
the citation-marked structural test artifact.

## Still required before external use

Pediatric, safeguarding, pastoral/theological, language, rights, and publication
reviews remain required. The existing B04 v1 was not overwritten.

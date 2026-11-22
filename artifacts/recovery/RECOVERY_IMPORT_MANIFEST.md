# Recovery Import Manifest

**Imported:** 2026-11-07  
**Source archive:** `Christ_Recovery.zip` (retained at repository root)  
**Source archive SHA-256:** `d9171edf70796c635b5fbea58e4bd24e9da6fcd791adb61d65acd8afff114e61`  
**Archive integrity:** verified with Python `zipfile.testzip()` before import.

## Import rules

- Every destination was required to be absent before extraction; no existing file was overwritten.
- Top-level member bytes and SHA-256 values were verified against `RECOVERY_MANIFEST.csv` inside the source archive.
- The import does not change any project or issue status. It restores provenance artifacts only.
- The historical bundles are preserved as ZIP files, not expanded into working inputs.

## Restored controlled artifacts

| Archive member | Destination | SHA-256 | Verification |
|---|---|---|---|
| `EDITORIAL_GUIDELINES_FULL_v1_0.md` | `artifacts/recovery/phase0/EDITORIAL_GUIDELINES_FULL_v1_0.md` | `2dcf1365dfd2d14157b2648f6b910e49143861a49f7a2c2ef6700b0fc6245d40` | Byte-identical to `docs/EDITORIAL_GUIDELINES.md`. |
| `BOYS_FULL_ORIGINAL_OUTLINE.md` | `artifacts/recovery/phase0/BOYS_FULL_ORIGINAL_OUTLINE.md` | `33fe9fb1288cd2547e2c7a06f03525d88cdd0365fd8edf3f968f86570c918a64` | Byte-identical to `docs/BOYS_OUTLINE.md`. |
| `GIRLS_FULL_ORIGINAL_OUTLINE.md` | `artifacts/recovery/phase0/GIRLS_FULL_ORIGINAL_OUTLINE.md` | `30e8cd6924696398c0d8b3c889fe26e0f3235da4be03de2cbaf77c218ebceced` | Byte-identical to `docs/GIRLS_OUTLINE.md`. |
| `OUTLINE_REGISTRY_RECONCILIATION.csv` | `docs/OUTLINE_REGISTRY_RECONCILIATION.csv` | `ad86364db19fa69ff595abdc29bc54adb1be1627dcfd71ff749ddf068865d4f4` | 49 rows / 49 unique chapter IDs; 36 title variants; all rows report ID/order match. |
| Nested Phase 4 `test_results.txt` | `artifacts/recovery/phase4/test_results.txt` | `cf9f51e31ceacbe63aea92a2a40ab3a8f4d5f00ca66eef64a5a77bbf3db6afd6` | Historical output only; records three passing tests. |

## Preserved historical bundles

Eighteen verified ZIP members were copied unchanged to `artifacts/history/`: the
knowledge-base v0.1 bundle; Phase 0 baseline, v1.1, and v1.2; Phase 1 architecture;
Phase 2 Batch 1, Batches 2A–2F, and consolidation; Phase 3 pilot, Batch 3B, and
Batch 3C; Phase 4 workflow; and the GitHub-ready bundle. Their expected checksums
are recorded in the source archive's `RECOVERY_MANIFEST.csv` and were verified on
import.

## Status note

This import resolves the *artifact-availability* finding recorded in the recovery
audit. It does not constitute source verification, rights clearance, clinical or
theological approval, Git-history recovery, or authorization to change ISS status.

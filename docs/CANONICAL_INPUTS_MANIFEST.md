# Canonical Inputs Manifest — Pilot Readiness Step 1

**Created:** 2026-11-07  
**Purpose:** Establish file roles and reproducible baselines for B04/G05 pilot
readiness. This is a provenance record, not an evidence or approval decision.

## Designations

| Role | Path | SHA-256 | Verification |
|---|---|---|---|
| Canonical Phase 3 evidence baseline | `knowledge_base/knowledge_base_phase3c.sqlite` | `4ca8996ce39a5bc82fef05ae6637b9d609f76817acf2b3fbfdfe6fdc322f9dff` | SQLite integrity check: `ok`; 49 chapter rows. Do not edit in place. |
| Runtime copy for existing Phase 4 CLI | `writing_system/input/knowledge_base_phase3c.sqlite` | `4ca8996ce39a5bc82fef05ae6637b9d609f76817acf2b3fbfdfe6fdc322f9dff` | Byte-identical to canonical Phase 3 evidence baseline. It is a workflow input, not an independent source of truth. |
| Canonical Phase 3 coverage matrix | `research/phase3/COVERAGE_MATRIX_3C.csv` | `1c6b031f810c5eaff28c26670a14de2dbe55b8ab8f86dc3f499a8eca838cd92c` | 10 data rows. |
| Runtime copy for existing Phase 4 CLI | `writing_system/input/COVERAGE_MATRIX_3C.csv` | `1c6b031f810c5eaff28c26670a14de2dbe55b8ab8f86dc3f499a8eca838cd92c` | Byte-identical to canonical Phase 3 coverage matrix. |
| Chapter registry | `data/chapters.csv` | `bf5cd52fe0cc723b917dfec5c74f7d7ef721e215d1f4b13d6fa46c0fd2b42290` | 49 data rows. |
| Orthodox source registry | `data/orthodox_sources.csv` | `e262f6ff1326adaa2f15dc435b91cfdc3acb648f41af932195ac35e25e39412f` | 19 data rows. |
| Medical source registry | `data/medical_sources.csv` | `b9813fd1510b3fe8d23583dc6fa84d716a3444c07bd80e434e4392387d1718bc` | 16 data rows. |
| Outline/registry reconciliation | `docs/OUTLINE_REGISTRY_RECONCILIATION.csv` | `ad86364db19fa69ff595abdc29bc54adb1be1627dcfd71ff749ddf068865d4f4` | 49 data rows / 49 unique chapter IDs; recovered from verified archive. |
| Historical provenance bundles | `artifacts/history/*.zip` | See `artifacts/recovery/RECOVERY_IMPORT_MANIFEST.md` | 18 checksum-verified archives. Not working inputs. |
| Recovery source archive | `Christ_Recovery.zip` | `d9171edf70796c635b5fbea58e4bd24e9da6fcd791adb61d65acd8afff114e61` | ZIP integrity verified; retain unchanged. |

## Operating rules

1. Use `knowledge_base/knowledge_base_phase3c.sqlite` and
   `research/phase3/COVERAGE_MATRIX_3C.csv` when auditing evidence. Treat the
   matching `writing_system/input/` files as derived runtime copies.
2. Any later database change must create a new, separately named output; preserve
   the baseline checksum above and never overwrite it.
3. Any later CSV change must be versioned and must state whether the runtime copy
   must be regenerated. Do not edit one duplicate silently.
4. Historical ZIPs may be inspected and compared, but are not to be merged into
   pilot inputs without a separate reconciliation decision.
5. Checksums prove file identity, not factual accuracy, rights clearance, or human
   approval.

## Step 1 result

The pilot has identified canonical baseline inputs and duplicate roles without
modifying the evidence database, source registries, workflow, or project statuses.
Step 2 may now audit B04/G05 objective coverage against this fixed baseline.

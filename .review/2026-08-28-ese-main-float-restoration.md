# ESE main-paper float restoration

Date: 2026-08-28

Status: completed.

## Scope

Starting HEAD was `b82c1828f270b9b68249bcc5a545c7edaac53a5f`. Commit `07a81e58d0eb8abf1a6d4ef7e5286c59d08f2fa7` had removed four visual elements from the main article and placed stand-alone versions in Online Resource 1. At the user's request, this change restores all four to the main article while retaining the supplement copies:

1. `fig:implicitColumnsRepresentations`: paired SQL and jOOQ Implicit Columns representations.
2. `tab:detectionApproaches`: detection representations and output units.
3. `tab:trainingTestValidationSplit`: occurrence and repository support by project-disjoint partition.
4. `tab:iouSensitivity`: complete line-span IoU-threshold sensitivity grid.

The restoration uses the pre-`07a81e5` structures and values rather than newly inventing replacement material. Captions, references, and adjacent interpretations were reconciled with the current article.

## Reconciliation and evidence checks

- The paired listing uses `select(DSL.asterisk())` and describes the SQL and jOOQ forms as equivalent Implicit Columns representations. The caption does not claim that `fetchOne()` has identical result-cardinality behaviour.
- The detection-comparison table retains the current bounded wording. It does not restore the uncited claim that no prior baseline exists or claim that one representation is inherently superior.
- Every split-table cell was checked against the frozen partition data. The caption states that partition cells contain occurrences and repository counts, while the Total column contains occurrences only.
- The IoU rows reproduce the frozen localisation analysis for 536 predictions and 523 original reference spans: 462/74/61 at 0.25, 460/76/63 at 0.50, and 457/79/66 at 0.75 and 1.00.
- Each restored visual element has a main-text reference and adjacent interpretation. Duplicate label names in the main article and supplement are safe because they compile as separate document roots.
- Online Resource 1 now describes its versions as stand-alone copies rather than material moved exclusively out of the article.

## Float-restoration measurements

Canonical TeXCount used `texcount -inc -sum main.tex` in the repository's TeX Live container.

| Section | Step 9 count | Current count | Change |
|---|---:|---:|---:|
| Introduction | 452 | 452 | 0 |
| Background and Related Work | 1,345 | 1,607 | +262 |
| Study Design | 3,623 | 3,677 | +54 |
| Results | 1,789 | 1,825 | +36 |
| Discussion | 1,044 | 1,038 | -6 |
| Threats to Validity | 926 | 926 | 0 |
| Conclusion | 163 | 163 | 0 |
| **Main paper, including front matter** | **9,777** | **10,123** | **+346** |

Relative to the 6,985-word restoration baseline, the float-restoration TeXCount increase was 3,138 words, inside the planned 2,850--3,150 range. At this audit point, the compiled main PDF contained 12,878 layout-extracted words across 32 A4 pages. The supplement contained 1,954 layout-extracted words across seven A4 pages.

The article has two figures and nine labelled tables. Two tables use `longtable`, so TeXCount reports nine floats for 11 labelled visual elements.

## Build and layout verification

`make clean && make paper` rebuilt both document roots after the restoration.

- Main PDF SHA-256: `40761cd5a97f486f89d81a2709df7dfa3e18e7a567aab4002eef709042180a87`.
- Supplement PDF SHA-256: `839b8ad7f8fa13b8d7cab2280cfe5976120232cd22f5ef3f643af73442b82307`.
- Main log: no LaTeX errors, unresolved citations or references, overfull boxes, float-size warnings, duplicate labels, or rerun warnings; 20 accepted underfull notices.
- Supplement log: the same checks pass; one accepted underfull notice.
- Both BibTeX logs contain no warnings.
- Visual inspection of the restored elements on main-paper pages 5, 7, 13, and 20 found no clipping, margin overflow, float-only pages, excessive whitespace, or adverse displacement. The detection table uses ragged-right fixed-width columns to keep the dense comparison readable.
- `git diff --check` passes.

## Post-audit declaration update

The four declaration placeholders were subsequently replaced with `Not applicable.` The clean build remains 32 pages and now contains 10,131 TeXCount words and 12,836 layout-extracted words. The current main PDF SHA-256 is `45ea50aa5032973a771664c79e2048c213ec1dc7c5c951503bf83428213865c5`; the supplement SHA-256 is `86ea60c3baa96fb440a8e0c3fb93e7d150cc9cfc095ef4ef6412cbd16f23a651`. The current main log has 21 accepted underfull notices and no errors, unresolved citations or references, overfull boxes, or rerun warnings.

The DOI-backed deposit and remaining author-metadata blockers recorded in Step 13 are unchanged.

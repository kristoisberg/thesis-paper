# ESE word restoration: Step 9 final audit

Date: 2026-08-28

Status: completed with a documented TeXCount deviation. This report records the historical Step 9 state; `2026-08-28-ese-main-float-restoration.md` supersedes its final counts, hashes, page count, and float inventory.

## Starting state

- Starting HEAD: `a8c9f790fc0f4bf75a84439f192291f7c4f10123`.
- Restoration baseline: `098d195c58c72705ff5263af466f92561afa032f`.
- Step 8 main-paper TeXCount: 9,771.
- Step 8 layout-extracted PDF words: 12,393.
- Step 8 main PDF pages: 31.

## Final manuscript changes

The final consistency audit found two caption-level defects in `paper/sections/04_results.tex`. The occurrence-agreement caption used TP, FP, and FN without expanding them. The RQ3 table used `manifestation category` where the RQ and analysis use `source-fragment category`. Step 9 expanded the abbreviations and aligned the category label. No claim, result, paragraph, float placement, citation, bibliography entry, Abstract text, or Conclusion text changed.

## Reuse ledger

Every restored unit retains its Step 1 legacy source. Step 8 reconciled the units in place, and Step 9 changed captions only.

| ID | Destination | Legacy source | Final state |
|---|---|---|---|
| I01 | Introduction motivation | `paper/chapters/01_introduction.tex:5-6`; `02_background.tex:25-27` | Retained and reconciled |
| B01 | Antipattern and code-smell distinction | `paper/chapters/02_background.tex:5,7` | Retained and reconciled |
| B02 | Implicit Columns mechanism | `paper/chapters/02_background.tex:11-13` | Retained and reconciled |
| B03 | jOOQ representation | `paper/chapters/02_background.tex:85` | Retained and reconciled |
| B04 | Detection progression | `paper/chapters/02_background.tex:104-112` | Retained and reconciled |
| B05 | SQL-detector comparison | `paper/chapters/02_background.tex:135-145` | Retained and reconciled |
| S01 | Generated-class mining rationale | `paper/chapters/03_dataset_creation.tex:11-15` | Retained and reconciled |
| S02 | Filtering and duplicate review | `paper/chapters/03_dataset_creation.tex:21-27` | Retained and reconciled |
| S03 | Relevant files and size strata | `paper/chapters/03_dataset_creation.tex:64-71,89-113` | Retained and reconciled |
| S04 | Operational-scope examples | `paper/chapters/03_dataset_creation.tex:117-131` | Retained and reconciled |
| S05 | Annotation records and repeatability | `paper/chapters/03_dataset_creation.tex:137-160` | Retained and reconciled |
| S06 | Project-disjoint partitioning | `paper/chapters/03_dataset_creation.tex:203-217,235-239` | Retained and reconciled |
| S07 | Model-selection criteria | `paper/chapters/04_evaluation.tex:5-21` | Retained and reconciled |
| S08 | Prompt construction and refinement | `paper/chapters/04_evaluation.tex:33-58` | Retained and reconciled |
| R01 | Held-out disagreement examples | `paper/chapters/08_analysis.tex:31-35,38-40,45-49,52-58,61,71,74-81` | Retained and reconciled |
| R02 | Repository-denominator context | `paper/chapters/07_results.tex:390-400` | Retained and reconciled |
| R03 | Lower-frequency fragment categories | `paper/chapters/07_results.tex:408-410,442-444` | Retained and reconciled |
| D01 | Single-run configuration trade-off | `paper/chapters/07_results.tex:61,87,91,115,123,147,155-157` | Retained and reconciled |
| D02 | Bounded follow-up studies | `paper/chapters/08_analysis.tex:187,193,197,199` | Retained and reconciled |

## Final counts

Canonical TeXCount used `texcount -inc -sum main.tex` in the repository's TeX Live container.

| Section | Baseline | Pre-reconciliation addition | Final addition | Final count | Movement from pre-reconciliation addition |
|---|---:|---:|---:|---:|---:|
| Introduction | 384 | 68 | 68 | 452 | 0.0% |
| Background and Related Work | 789 | 599 | 556 | 1,345 | -7.2% |
| Study Design | 2,287 | 1,388 | 1,336 | 3,623 | -3.7% |
| Results | 1,224 | 550 | 565 | 1,789 | +2.7% |
| Discussion | 777 | 340 | 267 | 1,044 | -21.5% |
| Threats to Validity | 926 | 0 | 0 | 926 | 0 words |
| Conclusion | 163 | 0 | 0 | 163 | 0 words |
| **Main paper** | **6,985** | **2,945** | **2,792** | **9,777** | **-5.2%** |

Discussion is the only section whose restored allocation moved by more than 10%. Step 8 removed repeated configuration-table narration, two one-sentence bridges, and a mechanical inventory of missing measurements. The retained D01 and D02 blocks still interpret the single-run trade-off and define bounded follow-up studies.

| Compiled measure | Final value | Target | Result |
|---|---:|---:|---|
| TeXCount net addition | 2,792 | 2,850--3,150 | 58 below lower tolerance |
| Main PDF layout-extracted words | 12,399 | at least 12,000 | Pass |
| Main PDF pages | 31 | at least 30 | Pass |
| Supplement layout-extracted words | 1,954 | informational | Recorded |
| Supplement pages | 7 | informational | Recorded |

The TeXCount shortfall is accepted. Filling 58 words solely to cross the threshold would conflict with the source-reuse and no-padding rules, while the submission-facing word and page targets already pass.

## Build and layout audit

`make clean && make paper` rebuilt the final main paper and supplement after the two caption corrections.

- Main PDF: 31 A4 pages, SHA-256 `deffe8ae7bf81000369368d62c92654cfc2b4b0624a5b0cc7e983a7a45c6cd7e`.
- Supplement: 7 A4 pages, SHA-256 `330bf55a6e02f2212901e0fb8b9a998e8eaa3b1ba912703796e01703bbde8389`.
- Main log: no LaTeX errors, unresolved citations or references, overfull boxes, duplicate labels, or rerun warnings. It contains 24 accepted underfull notices.
- Supplement log: the same checks pass, with one accepted underfull notice.
- Both BibTeX logs report `warning$ -- 0`.
- The PDFs contain no unresolved `??` or `[?]` markers.

Visual inspection of all 31 main-paper pages found no clipping, overlap, widows, orphan headings, displaced floats, excessive whitespace, float-only pages, or illegible tables. All six tables and Figure 1 are referenced and interpreted. The bibliography's unused lower space on its final page is normal.

## Repository-local verification

Both frozen analysis commands completed successfully:

```text
python3 analysis/localisation_robustness.py /home/kristoi/masters-thesis
python3 analysis/corpus_concentration.py /home/kristoi/masters-thesis/datasets/analysis-results.csv --verify-frozen
```

They reproduce 536 predictions, 523 references, the 460/76/63 primary totals, micro precision/recall/F1 of 0.858/0.880/0.869, the four-threshold IoU grid, all 10,000 bootstrap replicates, 15,931 corpus flags, 601 flagged repositories, every class total, and the 59.1% overall top-decile share. The frozen corpus SHA-256 is `76e900ef1ccb2442c9721587bcb96440c564befc608bcd0c1754cca40c64c8b6`.

The three RQs remain text-identical between Introduction and Results. Title, Abstract, direct answers, Discussion, Threats to Validity, and Conclusion retain consistent values and evidence boundaries. Searches found no duplicate labels, unsupported ground-truth or prevalence wording, model-reasoning claims, novelty or superiority language, conspicuous generated-prose markers, or negation-contrast patterns.

All Step 13 repository-local checks pass. This report's historical blocker list included author-confirmed declarations; those four fields were later confirmed as not applicable. The remaining blockers are the DOI-backed package deposit, author metadata and approval, and the unavailable exact validation-run outputs already disclosed in the paper and supplement.

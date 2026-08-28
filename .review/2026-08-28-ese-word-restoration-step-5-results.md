# ESE word restoration: Step 5 report

Date: 2026-08-28

Status: completed.

## Starting state

- Step 5 starting HEAD: `d121a0373bb259c9bd2f83e741dcdf91488afef2`.
- Results TeXCount: 1,224.
- Main-paper TeXCount after Step 4: 9,040.
- PDF-extracted words after Step 4: 11,626.
- Main PDF pages after Step 4: 29.
- Manuscript sections already restored: Introduction, Background and Related Work, and Study Design.

## Source ledger

The row deltas are standalone TeXCount counts of the new blocks. They sum to the canonical Results-section delta.

| ID | Legacy source | Restored job | Net words |
|---|---|---|---:|
| R01 | `paper/chapters/08_analysis.tex:31-35,38-40,45-49,52-58,61,71,74-81` | Restore concrete code forms and detector/reference judgments for the seven class-specific disagreement groups. | +368 |
| R02 | `paper/chapters/07_results.tex:390-400` and frozen `datasets/analysis-results.csv` | Restore flags per repository and per flagged repository for selected corpus comparisons. | +87 |
| R03 | `paper/chapters/07_results.tex:408-410,442-444` | Restore the lower-frequency source-fragment categories hidden by the compact catch-all rows. | +95 |
|  |  | **Total** | **+550** |

The frozen corpus CSV at `/home/kristoi/masters-thesis/datasets/analysis-results.csv` matched the recorded SHA-256 `76e900ef1ccb2442c9721587bcb96440c564befc608bcd0c1754cca40c64c8b6`. The repository counts, class totals, and top-decile shares reproduced with `analysis/corpus_concentration.py --verify-frozen`. Direct division reproduced every retained per-repository average to two decimals.

## Exclusions and adaptations

- Class-specific paragraphs retain the thesis's class order, examples, and viable sentence structure, but report observed forms and judgments rather than inferred model reasoning.
- Reference additions, removals, and range changes are identified as detector-informed. They are not presented as an independent audit or corrected ground truth.
- The numeric `CHECK` example is described in prose; the old figure and its prompt-causality explanation remain excluded.
- RQ2 uses detector flags and repository denominators. Corpus cost, runtime, old RQ numbering, prevalence wording, and repository-size-adjusted interpretations remain excluded.
- RQ3 expands only the two aggregate catch-all rows. The labels remain precedence-ordered source-fragment matches without resolved call targets or API-use denominators.
- The existing RQ wording, tables, labels, direct answers, sensitivity analyses, and bibliography are unchanged.

## Counts and budget

Canonical TeXCount was run from `paper/main.tex` with `-inc -sum`.

| Measure | Before Step 5 | After Step 5 | Change |
|---|---:|---:|---:|
| Results TeXCount | 1,224 | 1,774 | +550 |
| Main-paper TeXCount | 9,040 | 9,590 | +550 |
| PDF-extracted words, including references | 11,626 | 11,988 | +362 |
| Main PDF pages | 29 | 30 | +1 |

Step 5 finished 14 words below its 564-word allocation and within the 508--620 completion range. The overall execution budget is now 2,925 words, still within the 2,850--3,150 target range. The PDF-extracted count is 12 words below the 12,000-word practical threshold; the planned Step 6 Discussion restoration remains source-backed and should carry the paper over that boundary without padding Results.

## Verification

- `make paper` completed successfully.
- The main log contains no LaTeX errors, undefined citations or references, or overfull boxes.
- BibTeX reports no warnings.
- The main PDF is 30 pages.
- The frozen corpus CSV hash and all retained RQ2 averages were independently reproduced.
- The fixed RQ headings, detector totals, reference totals, class totals, source-fragment totals, floats, and direct answers remain unchanged.
- No citation, bibliography entry, model-causality claim, unqualified prevalence claim, or resolved-API claim was added.

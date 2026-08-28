# ESE word restoration: Step 6 report

Date: 2026-08-28

Status: completed.

## Starting state

- Step 6 starting HEAD: `f3ca3268bb17b331435e3fdecbe1afa3a0923cbc`.
- Discussion TeXCount: 777.
- Main-paper TeXCount after Step 5: 9,590.
- PDF-extracted words after Step 5: 11,988.
- Main PDF pages after Step 5: 30.
- Manuscript sections already restored: Introduction, Background and Related Work, Study Design, and Results.

## Source ledger

The row deltas are standalone TeXCount counts of the new blocks. They sum to the canonical Discussion-section delta.

| ID | Legacy source | Restored job | Net words |
|---|---|---|---:|
| D01 | `paper/chapters/07_results.tex:61,87,91,115,123,147,155-157` | Interpret the originally reported single-run prompt-configuration trade-off. | +153 |
| D02 | `paper/chapters/08_analysis.tex:187,193,197,199` | Define measurable follow-up studies for scope, model, representation, and preserved-flag boundaries. | +187 |
|  |  | **Total** | **+340** |

Both blocks retain the thesis's comparison and future-work sequence. Adaptation is limited to the current three-RQ article terminology, the surviving evidence boundary, citations at first Discussion mention, and short links to the surrounding analytical chain.

## Exclusions and adaptations

- D01 uses only the four originally reported Claude Opus 4.5 rows in `tab:configurationSelection`. Zero-Shot had the lowest cost, was faster than both reasoning-oriented prompts, and was 15 seconds slower than Few-Shot.
- The displayed F1, cost, and runtime values are described as single reported runs. The exact underlying outputs are unavailable, and run-to-run uncertainty was not measured.
- No prompt effect, causal model explanation, general superiority, or statistical difference is claimed.
- D02 converts broader taxonomies, smaller or self-hosted models, another query builder, and further preserved-flag analysis into experiments with explicit measurements.
- Speculative RAG and preprocessing benefits, model-release commentary, interface features, work-process reflection, cross-study rankings, and developer-benefit claims remain excluded.
- Existing bibliography entries support the restored model, prompt-design, and taxonomy references; no bibliography entry was added or changed.

## Counts and budget

Canonical TeXCount was run from `paper/main.tex` with `-inc -sum`.

| Measure | Before Step 6 | After Step 6 | Change |
|---|---:|---:|---:|
| Discussion TeXCount | 777 | 1,117 | +340 |
| Main-paper TeXCount | 9,590 | 9,930 | +340 |
| PDF-extracted words, including references | 11,988 | 12,352 | +364 |
| Main PDF pages | 30 | 31 | +1 |

Step 6 finished 20 words above its 320-word allocation and within the 288--352 completion range. The overall execution budget is now 2,945 words, inside the 2,850--3,150 target range. The main PDF now exceeds the 12,000-word and 30-page lower targets. Remaining plan steps verify threats, source reuse, and final counts; they do not require more prose.

## Verification

- `make paper` completed successfully.
- The main log contains no LaTeX errors, undefined citations or references, or overfull boxes.
- BibTeX reports no warnings.
- The main PDF contains 12,352 extracted words across 31 pages.
- The four Opus cost and runtime comparisons reproduce `tab:configurationSelection`, including the 15-second Few-Shot difference.
- All new model, prompt-design, and taxonomy mentions use existing citations at their first Discussion mention.
- No result, RQ, float, direct answer, conclusion, threat, bibliography entry, or reproducibility disclosure changed.

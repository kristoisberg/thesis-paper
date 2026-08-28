# ESE word restoration: Step 4 report

Date: 2026-08-28

Status: completed.

## Starting state

- Step 4 starting HEAD: `08d8c306de415c5637b2e8bccc9ef85ab356e400`.
- Study Design TeXCount: 2,287.
- Main-paper TeXCount after Step 3: 7,652.
- PDF-extracted words after Step 3: 10,184.
- Main PDF pages after Step 3: 26.
- Manuscript sections already restored: Introduction and Background and Related Work.

## Source ledger

The row deltas below are standalone TeXCount differences between each restored block and the block it replaced. They sum to the canonical section delta.

| ID | Legacy source | Restored job | Net words |
|---|---|---|---:|
| S01 | `paper/chapters/03_dataset_creation.tex:11-15` | Explain the checked-in generated-class requirement, rebuilding decision, manifest search, and GitHub result cap. | +254 |
| S02 | `paper/chapters/03_dataset_creation.tex:21-27` | Explain the non-generated Java filter and human-reviewed duplicate removal. | +63 |
| S03 | `paper/chapters/03_dataset_creation.tex:64-71,89-113` | Define relevant files and explain the skewed size distribution, recursive mean splits, proportional sampling, and fixed seed. | +227 |
| S04 | `paper/chapters/03_dataset_creation.tex:117-131` | Give the Index Shotgun runtime-evidence exclusion and Implicit Columns blind-projection inclusion examples. | +60 |
| S05 | `paper/chapters/03_dataset_creation.tex:137-160` | Explain annotation records, iterative flowchart revision and re-review, washout sampling, and exact-span repeatability. | +214 |
| S06 | `paper/chapters/03_dataset_creation.tex:203-217,235-239` | Explain split roles, whole-project assignment, support filtering, exhaustive seed selection, and label-informed status. | +135 |
| S07 | `paper/chapters/04_evaluation.tex:5-21` | Explain model-diversity, stable-identifier, and structured-output preferences used at the time. | +156 |
| S08 | `paper/chapters/04_evaluation.tex:33-58` | Explain one-request scope, shared prompts, two prompt types, key context, preprocessing, decision rules, and synthetic examples. | +279 |
|  |  | **Total** | **+1,388** |

Every restored paragraph begins from a named thesis paragraph or the current article's compressed version of it. New synthesis is limited to connecting the restored rationale to the article's occurrence-level units and evidence boundaries.

## Exclusions and adaptations

- Rebuilding difficulty is described as the study's decision rationale; it is not presented as universal build failure.
- Manifest queries are described as intended to reduce duplicate saturation. No import-search comparison was measured.
- The sample includes each observed size stratum but is not claimed to be statistically representative.
- The full codebook, split equations, support table, prompts, model inventory, and implementation architecture remain outside the main paper.
- The scope examples omit claims about jOOQ mitigating organisational antipatterns and about typical framework exception handling.
- Annotation revision is described as intended to improve within-annotator consistency. The report retains the distinction between temporal repeatability and correctness.
- Model criteria are stated as preferences used at the time. Performance rankings, repeatability guarantees, and omitted-model inventories remain excluded.
- Prompt refinement is described through operational and localisation rules. No unpreserved metric improvement or hallucination cause is claimed.
- The matching equation and all later evaluation, corpus, and reproducibility paragraphs are unchanged.

## Counts and budget

Canonical TeXCount was run from `paper/main.tex` with `-inc -sum`.

| Measure | Before Step 4 | After Step 4 | Change |
|---|---:|---:|---:|
| Study Design TeXCount | 2,287 | 3,675 | +1,388 |
| Main-paper TeXCount | 7,652 | 9,040 | +1,388 |
| PDF-extracted words, including references | 10,184 | 11,626 | +1,442 |
| Main PDF pages | 26 | 29 | +3 |

The section finished nine words below the provisional 1,397-word lower bound. Adding text solely to cross that boundary would conflict with the source-reuse protocol. The unused 164 words from the original 1,552-word allocation moved to R01 in Step 5, where the thesis contains concrete class-error narratives. The overall execution budget remains 2,939 words.

## Verification

- `make paper` completed successfully.
- The main log contains no LaTeX errors, undefined citations or references, or overfull boxes.
- BibTeX reports no warnings.
- The main PDF is 29 pages.
- The fixed repository, annotation, split, model, validation, held-out, and corpus values remain unchanged.
- Every selected model is cited at first mention in the restored model-selection paragraph.
- No float, equation, research question, result, corpus claim, or reproducibility disclosure was changed.

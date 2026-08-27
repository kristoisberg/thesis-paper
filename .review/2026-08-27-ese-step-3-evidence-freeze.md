# ESE Step 3: evidence freeze

Date: 2026-08-27

Status: completed. Two robustness analyses were performed, four unavailable upgrades were converted into claim limits, and the Step 2 identity was narrowed accordingly. No manuscript source changed.

## Decision rule

This step selects only analyses that can reconstruct the original held-out run from preserved artefacts. It excludes studies that need a new annotator, missing source snapshots, a changed model service, or new paid inference. The excluded studies remain limitations rather than implied evidence.

## Upgrade decisions

| Proposed upgrade | Decision | Reason | Consequence for the paper |
|---|---|---|---|
| IoU-threshold sensitivity | Selected and completed | The original 523 reference spans and all 536 predictions survive in the executed evaluation notebook. | Report the IoU 0.50 result as primary and the 0.25, 0.75, and exact-span results as boundary sensitivity. |
| Project-level bootstrap | Selected and completed | Every held-out reference and prediction retains its project identifier. | Report the aggregate interval as conditional project-composition sensitivity, not as a population confidence interval. |
| Independent annotation audit | Not selected | No second qualified annotator or adjudication exists. The exact source revisions were not recorded. | RQ1 reports agreement with original single-annotator reference spans. It does not establish annotation correctness. |
| Corpus transfer audit | Not selected | Corpus files preserve positive flags but omit the complete 17,450-file analysis frame and files with no flags. Source revisions were not recorded. | RQ2 and RQ3 remain descriptions of detector flags. They do not estimate transfer accuracy, recall, or true prevalence. |
| Deterministic API or AST baseline | Not selected | No antipattern baseline exists, and the original test-source revisions cannot be reconstructed. | Remove claims that the LLM outperforms, replaces, simplifies, or bypasses static analysis. |
| Repeated selected-model runs | Not selected | Repetition needs the source snapshots, API credentials, new spend, and a provider state that may differ from the original run. | Identify RQ1 as one run and leave stochastic stability unmeasured. |

## Frozen inputs

The analyses use the public `masters-thesis` repository at commit [`d9b35e398a6deb544f913bdbc0b211ab38474a44`](https://github.com/kristoisberg/masters-thesis/tree/d9b35e398a6deb544f913bdbc0b211ab38474a44).

| Input | Preserved content | SHA-256 |
|---|---|---|
| `datasets/test-set.csv` | 523 original single-annotator reference spans from 20 test projects | `f2be1176e5f655dbb2f5ec4d5fd4630298cb6ac2cc161362f0f138ee7366af7c` |
| `scripts/14-evaluate-tool-localisation.ipynb` | Executed notebook whose stored HTML table contains all 536 selected-detector predictions | `8efd33f04e88a878bc3389a5bbc05e9ef2982e4b3b98fc1e6af953812de96cb5` |
| `datasets/analysis-results.csv` | 15,931 positive corpus flags from 602 repositories | `76e900ef1ccb2442c9721587bcb96440c564befc608bcd0c1754cca40c64c8b6` |

The detector source is available at commit [`cf82fe56acb728f076df67279ff4a78a138996f3`](https://github.com/kristoisberg/jooq-antipattern-detector/tree/cf82fe56acb728f076df67279ff4a78a138996f3). The original experiment did not record the detector commit, analysed repository commits, raw API responses, request identifiers, retry histories, or complete provider metadata. These commits therefore freeze the surviving artefacts; they do not recover the original missing metadata.

The reconstruction canonicalises `Beware of the Unknown` to `Fear of the Unknown`, straightens the apostrophe in `Poor Man's Search Engine`, and changes project `/` separators to `_` to match the prediction output.

## Performed analysis 1: IoU sensitivity

The new script [`analysis/localisation_robustness.py`](../analysis/localisation_robustness.py) performs maximum-cardinality, one-to-one matching within each project, file, and class. Candidate edges are ordered by descending IoU and then by prediction span. The primary IoU 0.50 result reproduces the manuscript totals exactly.

| IoU threshold | TP | FP | FN | Micro precision | Micro recall | Micro F1 |
|---:|---:|---:|---:|---:|---:|---:|
| 0.25 | 462 | 74 | 61 | 0.862 | 0.883 | 0.873 |
| 0.50 | 460 | 76 | 63 | 0.858 | 0.880 | 0.869 |
| 0.75 | 457 | 79 | 66 | 0.853 | 0.874 | 0.863 |
| 1.00 | 457 | 79 | 66 | 0.853 | 0.874 | 0.863 |

Only Implicit Columns and Poor Man's Search Engine change across these thresholds. The largest micro-F1 difference is 0.010. The aggregate held-out result is therefore insensitive to the tested span-overlap boundary.

The archived notebook does not implement the one-to-one Non-Maximum Suppression described in the manuscript. It separately counts every reference and prediction with any qualifying overlap. At IoU 0.50, no ambiguous qualifying overlaps occur, so both methods yield 460 TP, 76 FP, and 63 FN. At IoU 0.25, one prediction can overlap three references, so the original any-overlap method is unsuitable for sensitivity analysis. Step 4 must replace the method description and derived analysis with the explicit one-to-one rule.

## Performed analysis 2: project-cluster bootstrap

The script resamples the 20 test projects with replacement for 10,000 iterations using seed `20260827`. Each draw retains every reference and prediction from the sampled project. The analysis uses the original reference spans, one-to-one matching, and IoU 0.50.

| Aggregate metric | Point estimate | 2.5th percentile | 97.5th percentile |
|---|---:|---:|---:|
| Micro precision | 0.858 | 0.799 | 0.933 |
| Micro recall | 0.880 | 0.817 | 0.913 |
| Micro F1 | 0.869 | 0.819 | 0.913 |

These percentiles measure sensitivity to the composition of the 20 held-out projects. The split was selected from 1,000,000 label-informed seeds numbered 0 through 999,999, so the interval is conditional on the study design. It does not quantify population sampling uncertainty or run-to-run model variation.

Class-level bootstrap intervals are too unstable for headline use. Reference support occurs in one test project for 31 Flavors, two for Rounding Errors, three each for Keyless Entry and Poor Man's Search Engine, and five for Fear of the Unknown. Many bootstrap samples omit all support for these classes. The script emits the class-level diagnostics and the number of defined replicates, but the planned manuscript will report only the aggregate interval and the observed per-class point estimates.

## Final evidence set

Later restructuring and results writing may use the following quantitative evidence:

1. Per-class TP, FP, FN, precision, recall, and F1 from one selected-detector run against the original reference spans at IoU 0.50, with 460 TP, 76 FP, 63 FN, and micro F1 0.869 overall.
2. The IoU sensitivity table above, which bounds micro F1 between 0.863 and 0.873 for thresholds 0.25 through exact matching.
3. The aggregate project-composition sensitivity above, with a 95% percentile interval of 0.819 to 0.913 for micro F1.
4. Corrected-reference totals only as an optimistic sensitivity analysis. The archive preserves manually entered corrected counts rather than corrected row-level spans, so no IoU or bootstrap extension can be run for them.
5. The 15,931 corpus flags across 17,450 relevant Java files and 602 repositories, interpreted by class and described only as detector output.
6. API or source-pattern distributions among flags for Implicit Columns and Poor Man's Search Engine, subject to the coverage correction in Step 4.

This evidence does not establish independent annotation correctness, corpus-wide accuracy, true prevalence, stochastic stability, or superiority over deterministic analysis.

## Required later corrections

- Replace accuracy language in RQ1 with agreement against the original single-annotator reference spans.
- State that RQ1 evaluates one selected-detector run.
- Replace the archived any-overlap matching implementation with the one-to-one rule when Step 4 recalculates tables.
- Reassess the reported Cohen's kappa. The notebook omits files with no annotations in either pass and treats shifted spans as separate background disagreements, so the current statistic does not establish independent correctness.
- Limit the availability statement to preserved artefacts. The archive lacks raw responses, request metadata, source-project commits, and a complete corpus file manifest.
- Archive the surviving artefacts and the robustness script under a DOI before submission.

## Review method

Three independent passes informed the evidence freeze:

- a technical review checked matching validity, sensitivity design, bootstrap interpretation, annotation reliability, and reproducibility;
- a consistency review traced every proposed upgrade to exact archived inputs and missing units;
- a logic review mapped each unavailable upgrade to the claims that must be narrowed.

The repository's methodology-rigor skill set the rule that unavailable raw outputs or human checks cannot be simulated. The results-synthesis skill kept the analysis tied to the three locked RQs. Its older four-RQ structure was not used because Step 2 supersedes it. The acceptance check requires the unavailable studies to remain visible as limitations rather than implied work.

## Completion check

- Every proposed evidence upgrade has a decision.
- Both selected analyses have executable code and reproduced primary counts.
- Every unavailable upgrade has a corresponding claim limit.
- The final quantitative evidence set is fixed for later restructuring.
- No manuscript source changed.

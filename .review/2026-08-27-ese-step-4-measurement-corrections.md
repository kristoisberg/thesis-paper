# ESE Step 4: measurement and statistical corrections

Date: 2026-08-27

Status: completed. The manuscript compiles with the corrected units, matching rule, aggregates, corpus terminology, and API-category coverage.

## Decisions applied

- The primary detector result is occurrence-level agreement from one selected run against the original single-annotator reference spans.
- Original annotations are primary. Detector-informed revised annotations are an optimistic sensitivity analysis, not corrected truth.
- Localisation uses maximum-cardinality one-to-one matching within repository, file, and class at IoU 0.50. Candidate lists use descending IoU, prediction span, and source order for deterministic tie handling.
- Localisation counts are event-matching counts, not confusion matrices. The negative-event universe and true negatives are undefined.
- Micro, macro, and reference-support-weighted aggregates are named and reported separately.
- Corpus measurements are detector flags. They are not prevalence estimates because no corpus transfer audit, repository-size adjustment, API-exposure denominator, or class-specific error correction is available.
- The plain-SQL density comparison was removed because detector flags and static execution-method references do not form a compatible statement-level rate.
- Co-detection was removed from the main results, discussion, summary, and compiled appendices. The source matrices remain in the repository as archived exploratory material.
- API results are post hoc manifestation categories among detector flags. They do not estimate API risk or support API-design claims.

## Corrected primary results

At IoU 0.50, the original-reference event totals are 460 TP, 76 FP, and 63 FN.

| Aggregate | Precision | Recall | F1 |
|---|---:|---:|---:|
| Micro | 0.858 | 0.880 | 0.869 |
| Macro | 0.797 | 0.813 | 0.793 |
| Reference-support weighted | 0.885 | 0.880 | 0.877 |

The revised-reference sensitivity totals are 512 TP, 24 FP, and 51 FN.

| Aggregate | Precision | Recall | F1 |
|---|---:|---:|---:|
| Micro | 0.955 | 0.909 | 0.932 |
| Macro | 0.922 | 0.857 | 0.881 |
| Reference-support weighted | 0.962 | 0.909 | 0.931 |

The manuscript now also reports IoU sensitivity from 0.25 through 1.00 and the conditional project-composition bootstrap ranges from Step 3. A malformed Keyless Entry reference span, lines 61 through 51, is treated as invalid and unmatched rather than silently repaired.

## Split and annotation corrections

- The split search is described as an exhaustive, label-informed search over 1,000,000 seeds numbered 0 through 999,999.
- The 21/20/20 project allocation and per-class project support are reported beside occurrence support.
- The class support rule and split objective are disclosed as using annotations from the complete 61-project sample.
- The nonstandard 0.834 kappa claim was removed. Repeat annotation is reported directly as 142 exact matches from 158 original-pass and 149 repeated-pass events, giving precision 0.953, recall 0.899, and F1 0.925 when the original pass is treated as reference.

## Corpus and API corrections

- The corpus table reports 15,931 flags, projects with at least one flag, flags per project, and flags per flagged project.
- Implicit Columns categories cover 6,860 of 7,289 flags, or 94.1%; 429 flags, or 5.9%, are other or uncategorised.
- Poor Man's Search Engine categories cover 546 of 583 flags, or 93.7%; 37 flags, or 6.3%, are other or uncategorised.
- The two largest Implicit Columns categories contain 5,227 flags, or 71.7%.
- `Field.like` contains 273 Poor Man's Search Engine flags, or 46.8%; the four largest categories contain 517 flags, or 88.7%.

## Verification

- Manuscript tables, captions, abstract, results, discussion, limitations, and summary use the corrected units.
- Localisation and file-classification appendices were consolidated into count tables.
- Unsupported uses of statistical significance and margin of error were removed from the results.
- The robustness script now treats reversed spans as invalid and includes a direct self-check.

## Remaining scope

Step 4 corrects the existing analysis. Step 5 still performs the structural article conversion. The independent annotation audit, corpus transfer audit, deterministic baseline, and repeated model runs remain unavailable and are not implied by the manuscript.

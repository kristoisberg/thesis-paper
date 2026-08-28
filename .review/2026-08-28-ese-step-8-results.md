# ESE Step 8: RQ-centred results

Date: 2026-08-28

Status: completed.

## Applied changes

- Moved the validation comparison and detector-selection outcome before RQ1 while leaving the comparison procedure in Study Design.
- Rebuilt RQ1 around one held-out occurrence-localisation run, class-specific disagreements, IoU sensitivity, project-composition sensitivity, and the detector-informed reference sensitivity analysis.
- Rebuilt RQ2 around flag counts, repository coverage, class concentration, and top-decile repository concentration.
- Rebuilt RQ3 around recurring source-fragment patterns for Implicit Columns and Poor Man's Search Engine flags.
- Removed classification-only results, the isolated CHECK-constraint example, redundant RQ1 tables, and the incompatible classification comparison in Discussion.
- Added a direct answer at the end of each RQ and used flag/detection language for every corpus result.

## New reproducible measure

`analysis/corpus_concentration.py` calculates the share of each class's flags contained in the highest-count 10 percent of flagged repositories. Its verification mode checks the frozen CSV SHA-256 and reproduces the reported class and overall shares.

## Completion check

- Every retained result answers an RQ or is labelled detector configuration selection.
- All counts and agreement metrics match the frozen evidence and measurement-correction reports.
- The three Results headings match the RQs in the Introduction, and each subsection ends with a short answer.
- A `make paper` rebuild succeeds with no undefined citations or references and no overfull boxes in Results.
- Specialist findings and their disposition are recorded in `2026-08-28-ese-step-8-review.md`.

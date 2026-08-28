# ESE Step 8: results review

Date: 2026-08-28

## Synthesis

The original Results section contained the required evidence but obscured the three research questions with configuration detail, four overlapping RQ1 tables, a classification-only detour, and a seven-part error inventory. The repository table also omitted project percentages and did not quantify concentration across repositories.

## Critical findings addressed

- Moved the model and prompt comparison from Study Design to a labelled detector-selection subsection before RQ1.
- Removed the classification-only analysis and the single CHECK-constraint figure because neither answers a retained research question.
- Combined primary occurrence counts and agreement metrics into one class-level table.
- Kept detector-informed revised references as an aggregate optimistic sensitivity analysis rather than corrected truth.
- Replaced API-qualified category names with the source-fragment patterns that the preserved coding procedure actually matches.
- Added a direct answer at the end of each RQ subsection.

## Important findings addressed

- Added the percentage of all 602 repositories flagged for every class.
- Calculated top-decile repository concentration directly from the frozen positive-flag CSV and documented the exact rule in `analysis/corpus_concentration.py`.
- Reduced the error analysis to the dominant observed mechanism for each class without inferring internal model reasoning.
- Preserved IoU sensitivity and project-composition bootstrap ranges with their claim limits.
- Reported all corpus quantities as detector flags rather than antipattern prevalence.

## Verification criteria

- Every quantitative result answers RQ1, RQ2, or RQ3, apart from the explicitly labelled detector-selection comparison.
- Every retained table is referenced and interpreted.
- Configuration, held-out, corpus, and manifestation counts match the frozen evidence reports.
- The concentration script verifies the frozen CSV SHA-256 and reproduces all reported shares.
- The compiled Results section has no overfull boxes or unresolved references.

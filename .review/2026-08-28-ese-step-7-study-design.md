# ESE Step 7: study-design consolidation

Date: 2026-08-28

Status: completed.

## Applied changes

- Reordered Study Design around the empirical pipeline: population, scope, annotation, partitioning, detector selection, held-out evaluation, corpus analysis, and reproducibility.
- Reduced the section from 10,025 to 2,517 words by removing thesis-scale implementation detail, prompt histories, duplicate results, and classification-only analysis.
- Preserved the exact repository funnel, sampling frame, annotation process, support rule, project-disjoint split, selected detector configuration, held-out matching, robustness checks, corpus measures, and API-pattern coding rule.
- Distinguished original references from the detector-informed sensitivity analysis and detector flags from independently verified occurrences.
- Added the substantive AI-use disclosure and the frozen-artefact boundary, including the evidence that was not retained.

## Completion check

- The resulting section lets a reader reconstruct the study population, reference data, detector selection, held-out evaluation, and corpus analysis without an appendix.
- A forced `make paper` rebuild succeeds and produces a 32-page PDF with no undefined citations or references.
- The consolidated section introduces no overfull boxes.
- Specialist review findings and their disposition are recorded in `2026-08-28-ese-step-7-review.md`.

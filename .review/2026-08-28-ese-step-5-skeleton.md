# ESE Step 5: paper skeleton

Date: 2026-08-28

Status: completed.

## Applied structure

1. Introduction
2. Background and Related Work
3. Study Design
4. Results
5. Discussion
6. Threats to Validity
7. Conclusion
8. Statements and Declarations

The article now uses native `svjour3` section commands. The thesis heading compatibility layer and compiled thesis appendices were removed from `paper/main.tex`.

## Block routing

- The Introduction retains the opening, objectives, and contributions. Its five thesis research questions were replaced with the three questions locked in Step 2.
- Background and Related Work contains the preserved background blocks.
- Study Design follows the evidence pipeline: repository mining, operational scope, reference annotations, project-disjoint split, detector configuration, detector pipeline, corpus measures, API-pattern coding, and the AI-use and reproducibility disclosure.
- Results contains occurrence-level agreement as RQ1, corpus detector flags as RQ2, and API manifestations as RQ3. Detector model and prompt comparisons now appear as configuration evidence in Study Design.
- Discussion contains the preserved interpretation, comparison, API-manifestation, and future-work blocks.
- Threats to Validity contains repository-search limitations and the preserved limitations block.
- Conclusion contains the preserved summary and calibrated final takeaway.
- The thesis outline, work-process reflection, repeated repository-links paragraph, thesis navigation paragraphs, and compiled appendices were omitted according to the Step 1 routing map.

Temporary `% Source:` comments identify the original chapter and section of each relocated block.

## Mechanical repairs

- Applied the title locked in Step 2.
- Remapped the former RQ3, RQ4, and RQ5 labels to RQ1, RQ2, and RQ3.
- Reframed the former RQ1 and RQ2 result labels as detector-configuration labels.
- Replaced compiled-appendix references with Online Resources references.
- Retained the Springer bibliography style and bibliography after Statements and Declarations.

## Completion check

- `make paper` succeeds.
- The generated `paper/main.pdf` has 61 pages.
- The final LaTeX log contains no undefined references or citations.
- The PDF presents the eight target sections in the intended order.

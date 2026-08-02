# EMSE Style Calibration

Status: initial calibration from `examples/`

## Structural Pattern

Use a compact empirical-study structure:

1. Introduction: problem, gap, contribution, RQs.
2. Background and Related Work: only the concepts needed to position SQL antipattern detection, jOOQ, static analysis, LLM code analysis, and localisation.
3. Study Design: repository mining, sampling, annotation, detector setup, metrics.
4. Results: detector validity first, then large-scale prevalence, co-occurrence, and API associations.
5. Discussion: implications for jOOQ users, tool builders, and empirical software engineering.
6. Threats to Validity.
7. Conclusion and artifact availability.

## Example-Derived Guidance

- Follow the LLM-evaluation density of `Macedo_et_al_2026`: state the evaluation problem, model set, dataset size, metrics, and why output/evaluation reliability matters.
- Follow the localisation framing of `Yang_et_al_2024`: make line-level/localised prediction a first-class task rather than an implementation detail.
- Follow the large-scale static-analysis framing of `Trautsch_et_al_2023`: define the analysis unit, density metric, comparison baseline, and practical relevance.
- Follow the human-vs-automated framing of `Morales_et_al_2020`: be explicit about what the automated tool is compared against and what human judgement provides.
- Use `Patel_et_al_2024` as the MSR-style model for transparent data collection, practical implications, and threats.

## Abstract Pattern

Use 150 to 250 words with five moves:

1. Context: SQL antipatterns and dynamic jOOQ code challenge traditional static analysis.
2. Objective: evaluate LLM-based localisation and study real-world prevalence.
3. Method: annotated dataset, IoU/F1 evaluation, 602-project mining study.
4. Results: detector performance, 15,931 detections, dominant antipatterns, co-occurrence/API associations.
5. Conclusion: implications and limits.

## Tone

- Write as a journal article, never as a thesis report.
- Prefer "we study", "we evaluate", "we find" over process-heavy narration.
- Keep result claims quantitative and bounded to the observed population.
- Put limitations in the main text, not only at the end.


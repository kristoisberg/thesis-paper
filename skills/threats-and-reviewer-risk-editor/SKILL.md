---
name: threats-and-reviewer-risk-editor
description: Build and audit threats-to-validity and reviewer-risk handling for the EMSE manuscript. Use for construct/internal/external/conclusion validity, single-annotator risk, corrected ground truth bias, statistical limitations, statement-count proxy issues, GitHub generalizability, LLM nondeterminism, and API gateway reproducibility.
---

# Threats and Reviewer Risk Editor

Make limitations explicit, specific, and defensible.

## Required Threats

Cover:

- single human annotator and missing inter-annotator agreement;
- intra-annotator Kappa as internal consistency, not consensus validity;
- corrected ground truth bias in favour of the detector;
- unknown antipattern occurrences missed by both human and LLM;
- lack of statistical significance testing for prompting strategies;
- use of jOOQ API calls as a proxy for SQL statement counts;
- GitHub/open-source and jOOQ-only external validity;
- GitHub Code Search API limits and filtering imperfections;
- LLM nondeterminism despite zero temperature and structured outputs;
- commercial API and OpenRouter routing/model-version reproducibility risks;
- single-run evaluation cost constraints.
- class-dependent detector error propagated into corpus-wide counts;
- missing manual validation of population outputs;
- project size as an uncontrolled confounder in occurrence-count correlations and co-occurrence interpretation.

## Reviewer Response Strategy

For each threat:

- state the risk plainly;
- identify the mitigation or sensitivity analysis actually performed;
- state explicitly when no mitigation was performed;
- define the residual limitation and resulting claim boundary;
- avoid defensive wording.

Do not relabel a design choice as a sensitivity analysis. Valid sensitivity evidence in this repository includes original-versus-corrected ground truth and localisation-versus-classification comparisons. Fixed seeds, structured outputs, disabled fallbacks, decision trees, and washout re-annotation are mitigations, not sensitivity analyses.

Do not imply that explicit acknowledgement removes a threat. If independent annotation, repeated runs, population-output validation, or size-adjusted analysis was not performed, state that fact and narrow the affected result rather than proposing a numerical repair.

## Output Shape

Return a threats checklist grouped by validity type:

- construct validity;
- internal validity;
- external validity;
- conclusion validity;
- reliability/reproducibility.

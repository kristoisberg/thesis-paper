---
name: methodology-rigor-reviewer
description: Review and strengthen empirical methodology for an EMSE manuscript converted from the thesis. Use for repository mining design, sampling, annotation protocol, localisation metrics, IoU/NMS reporting, model and prompt evaluation, corrected ground truth handling, statistical claims, reproducibility, and methodological caveats.
---

# Methodology Rigor Reviewer

Audit whether the manuscript reports enough detail for EMSE reviewers to trust and replicate the study.

## Required Method Elements

Check that the paper reports:

- repository mining source, queries, filtering, and exclusions;
- project counts at each filtering stage;
- train/validation/test or development/evaluation split logic;
- annotation protocol, decision rules, and validation method;
- single-annotator limitation and intra-annotator agreement;
- model list, settings, prompting strategies, and selection rationale;
- localisation metric definition, including line-range matching and IoU threshold;
- post-processing such as NMS if used;
- classification vs localisation evaluation distinction;
- corrected vs uncorrected ground truth handling;
- cost/runtime reporting where used to justify model choice;
- artifact availability.

Require these explicit Study Design subsections:

- `Operational Definitions`;
- `Annotation and Adjudication`;
- `Model and Prompt Selection`;
- `Evaluation Protocol`.

Use “adjudication” accurately: if no independent adjudicator existed, say so and describe the actual disagreement-review and correction procedure.

Require the main text to report test support per antipattern, the project-level data split, all fixed seeds, model parameters, schema/query prompt separation, structured-output validation, retry policy, IoU threshold, NMS assignment, averaging rule, and analysis units.

## Statistical Discipline

Require careful language:

- descriptive differences are not statistical significance;
- corrected ground truth scores are optimistic;
- jOOQ API call counts are a proxy, not exact SQL statement counts;
- single-run LLM evaluations do not establish output variance.
- sensitivity results discovered through model disagreements are optimistic and do not estimate errors missed by both human and model;
- do not invent confidence intervals or significance tests when project-level raw outputs or repeated runs are unavailable.

## Output Shape

Return:

- missing method details;
- overclaims to weaken;
- reproducibility gaps;
- concrete text-level requirements for the later manuscript.
- performed mitigations and sensitivity analyses, separated from future work.

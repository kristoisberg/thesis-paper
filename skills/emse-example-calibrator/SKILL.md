---
name: emse-example-calibrator
description: Calibrate manuscript structure and style against provided Empirical Software Engineering example papers. Use when deriving EMSE-style article organization, abstract density, research question framing, methodology reporting, result presentation, and threats-to-validity conventions from PDFs in examples/.
---

# EMSE Example Calibrator

Use the PDFs in `examples/` as style and structure exemplars. Do not copy phrasing.

## Example Roles

- `Macedo_et_al_2026...`: LLM evaluation in code tasks; output format bias; empirical model comparison.
- `Yang_et_al_2024_LineFlowDP...`: line-level localisation and defect-prediction framing.
- `Trautsch_et_al_2023...`: static-analysis tool validation over open-source projects.
- `Morales_et_al_2020_RePOR...`: human-vs-automated comparison and anti-pattern/refactoring evaluation.
- `Patel_et_al_2024...`: MSR-style methodology and threats from a strong empirical software engineering group.
- `Alomari_et_al_2026...`: current LLM code-smell comparison and RQ-labelled result subsections.
- `Su_McMillan_2026...`: LLM static-analysis capabilities, task design, and RQ-labelled methods/results.

## Calibration Targets

Extract patterns for:

- abstract structure and density;
- how the introduction moves from problem to gap to contribution;
- whether RQs are stated explicitly and where;
- methodology section granularity;
- result table density;
- discussion vs results separation;
- threats-to-validity taxonomy;
- data/artifact availability wording;
- length and placement of related work.
- whether complete RQs appear as result headings and how each section closes with an answer;
- approximate full-paper length as calibration evidence, never as a formal journal limit.

## Output Shape

Produce a short style guide:

- recommended section order;
- abstract pattern;
- RQ presentation pattern;
- table/figure conventions;
- threats style;
- citation and related-work positioning.

Keep the guide descriptive and avoid importing example-paper claims into the manuscript.

For this repository, record that the supplied examples contain roughly 10,000--23,000 PDF-extracted words and commonly use RQ-labelled result headings. Use this observation to justify deeper reporting, not filler.

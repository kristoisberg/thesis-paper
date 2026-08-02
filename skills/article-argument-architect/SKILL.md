---
name: article-argument-architect
description: Design the EMSE article argument from thesis evidence. Use when choosing the manuscript angle, title, contribution claims, research questions, section outline, abstract structure, novelty framing, and what to exclude so the output is a targeted journal article rather than a thesis condensation.
---

# Article Argument Architect

Build the article argument around a narrow EMSE contribution.

## Default Angle

Use this default unless the user changes it:

> An empirical study of LLM-based detection and localisation of SQL antipatterns in jOOQ-based database access code.

The empirical contribution is primary. The detector and LLM prompt evaluation support the credibility of the mined findings.

## RQ Mapping

Map thesis RQs into article logic:

- Thesis RQ1/RQ2: model and prompt-selection rationale.
- Thesis RQ3: validity of the LLM detector and localisation methodology.
- Thesis RQ4: core prevalence and co-occurrence findings.
- Thesis RQ5: API usage patterns associated with query antipatterns.

Avoid giving every thesis RQ equal weight.

## Contribution Claims

Prefer 3 to 4 claims:

- a manually annotated jOOQ SQL-antipattern dataset and localisation evaluation setup;
- an LLM-based localisation method for antipatterns in dynamic jOOQ database access code;
- large-scale empirical evidence of SQL antipattern prevalence and co-occurrence in 602 projects;
- API-level evidence that jOOQ convenience methods are associated with common query antipatterns.

## Default Outline

1. Introduction
2. Background and Related Work
3. Study Design
4. LLM-Based Antipattern Localisation
5. Large-Scale Empirical Results
6. Discussion
7. Threats to Validity
8. Conclusion

## Exclusion Rules

Exclude:

- thesis process reflection;
- broad tutorial-style background;
- implementation architecture unless required to reproduce the study;
- exhaustive appendix content from the main paper.


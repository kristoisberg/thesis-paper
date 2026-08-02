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

## Novelty and Prior Dissemination

Require an introduction comparison that distinguishes the combined contribution from:

- SQL extraction followed by rule-based detection;
- dedicated API- or AST-based rules;
- LLM code-smell classification;
- LLM static-analysis and line-level localisation studies.

Frame novelty around the validated instrument plus the 602-project empirical analysis. Avoid unverified first-ever claims.

State explicitly that the article is based on Kristo Isberg's master's thesis and identify reused data, software, experiments, and results. Put this disclosure in a prior-dissemination declaration and the cover letter, not in the scientific motivation. Do not present reorganisation or rewriting as a scientific contribution and do not imply new experiments where none were performed.

Prefer titles that name both the validated measurement protocol and its bounded repository use. Avoid titles that imply a general SQL-antipattern detector or broader novelty than the evaluated jOOQ setting supports.

## Default Outline

1. Introduction
2. Background and Related Work
3. Study Design
4. Results, with RQ1--RQ4 as subsections
5. Discussion
6. Threats to Validity
7. Conclusion

Use each full research question as a heading inside the corresponding results section. End each RQ subsection with a short, evidence-bounded answer.

## Exclusion Rules

Exclude:

- thesis process reflection;
- broad tutorial-style background;
- implementation architecture unless required to reproduce the study;
- exhaustive appendix content from the main paper.

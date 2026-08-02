# Article Blueprint

Status: initial conversion blueprint

Revision target: feedback-remediated journal draft of approximately 12,000 words (normally 11,000--13,000), excluding references and supplementary material. This is a project target calibrated from the supplied examples, not an EMSE rule.

## Working Title Options

1. An Empirical Study of LLM-Based Localisation of SQL Antipatterns in jOOQ Database Access Code
2. Detecting and Localising SQL Antipatterns in jOOQ Projects with Large Language Models: An Empirical Study
3. SQL Antipatterns in the Wild: LLM-Based Localisation and Large-Scale Evidence from jOOQ Projects

Recommended: option 1. It foregrounds EMSE fit, LLM localisation, SQL antipatterns, and jOOQ without sounding like a tool paper.

## Core Claim

This paper presents an empirical software engineering study showing how LLM-based localisation can support the detection and large-scale analysis of SQL antipatterns in dynamic jOOQ database access code.

## Proposed Research Questions

- RQ1: How accurately can LLMs localise SQL antipattern occurrences in jOOQ-based Java code?
- RQ2: How prevalent are SQL antipatterns in open-source jOOQ projects?
- RQ3: Which SQL antipatterns co-occur across projects and files?
- RQ4: Which jOOQ API methods are most frequently associated with query antipattern occurrences?

Thesis RQ1/RQ2 should appear as method-selection evidence under RQ1, not as separate headline contributions.

## Contributions

- A manually annotated dataset of SQL antipattern occurrences in jOOQ-based Java projects, with line-level localisation labels.
- An evaluation of LLM-based antipattern detection as a multi-label, multi-occurrence localisation task using IoU, NMS, precision, recall, and F1.
- A large-scale empirical analysis of seven SQL antipatterns across 602 open-source jOOQ projects.
- Evidence of co-occurrence patterns and jOOQ API method associations that suggest practical documentation and tool-design targets.

## Proposed Section Plan

1. Introduction
   - Problem: SQL antipatterns matter, but dynamic jOOQ code resists conventional SQL extraction and AST-based detection.
   - Gap: little evidence on SQL antipattern prevalence in jOOQ projects and limited localisation-oriented LLM evaluation.
   - Sharp novelty comparison against extraction-based, API/AST-rule, LLM smell-classification, and LLM localisation studies.
   - Explicit relationship to Kristo Isberg's master's thesis.
   - Contributions and RQs.
2. Background and Related Work
   - SQL antipattern detection and static analysis.
   - jOOQ as dynamic SQL DSL.
   - LLMs for code analysis and line-level/localisation tasks.
3. Study Design
   - Repository mining and filtering.
   - Operational Definitions.
   - Annotation and Adjudication.
   - Model and Prompt Selection.
   - Evaluation Protocol.
   - Large-scale statistical analysis.
4. Detector Evaluation
   - Model/prompt selection compressed.
   - Localisation and classification performance.
   - Corrected vs uncorrected ground truth.
5. Large-Scale Results
   - Prevalence.
   - Co-occurrence.
   - API method associations.
6. Discussion
   - SQL decay patterns in jOOQ projects.
   - Implications for jOOQ API use, documentation, and static-analysis tooling.
   - Comparison to prior SQLInspect/plain-SQL results with proxy caveat.
7. Threats to Validity
8. Conclusion

Use the full RQ wording as result subsection headings and close each with a concise answer.

## Section Word Budget

| Section | Target words |
|---|---:|
| Introduction | 650--800 |
| Background and Related Work | 1,600--2,000 |
| Study Design | 3,000--3,400 |
| Detector Evaluation | 1,200--1,500 |
| Large-Scale Results | 1,600--2,000 |
| Discussion | 1,300--1,600 |
| Threats to Validity | 700--900 |
| Conclusion | 250--350 |

## Main Tables and Figures

- Data funnel figure adapted from thesis Figure `data_funnel_diagram.png`.
- Compact detector-performance table with localisation/classification, corrected/uncorrected scores.
- Prevalence table for seven antipatterns.
- Co-occurrence figure/table with main Jaccard/Spearman findings.
- API association table for Implicit Columns and Poor Man's Search Engine.

## Non-Goals

- Do not describe the CLI architecture as a central contribution.
- Do not preserve the thesis chapter sequence.
- Do not include reflection on work process.
- Do not make the article a survey of SQL antipatterns or prompt engineering.

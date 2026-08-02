# Article Blueprint

Status: revised after adversarial EMSE screening feedback

Revision target: feedback-remediated journal draft of approximately 12,000 words (normally 11,000--13,000), excluding references and supplementary material. This is a project target calibrated from the supplied examples, not an EMSE rule.

## Working Title

Validating LLM-Based Localisation for Mining SQL Antipatterns in jOOQ Repositories

The title foregrounds the validated measurement protocol and its bounded repository use without implying a general detector.

## Core Claim

This paper evaluates occurrence-localised LLM detection on a project-disjoint held-out set and uses that fallible instrument for bounded analysis of detector outputs in 602 jOOQ repositories.

## Proposed Research Questions

- RQ1: How accurately can LLMs localise SQL antipattern occurrences in jOOQ-based Java code?
- RQ2: How prevalent are SQL antipatterns in open-source jOOQ projects?
- RQ3: Which SQL antipatterns co-occur across projects and files?
- RQ4: Which jOOQ API methods are most frequently associated with query antipattern occurrences?

Thesis RQ1/RQ2 should appear as method-selection evidence under RQ1, not as separate headline contributions.

## Contributions

- A manually annotated dataset of SQL antipattern occurrences in jOOQ-based Java projects, with line-level localisation labels.
- An evaluation of LLM-based antipattern detection as a multi-label, multi-occurrence localisation task using IoU, NMS, precision, recall, and F1.
- Bounded detector-output measurements for seven SQL antipatterns across 602 open-source jOOQ projects.
- Exploratory, size-unadjusted co-detection and jOOQ API-association evidence for future validation and tool design.

## Proposed Section Plan

1. Introduction
   - Problem: SQL antipatterns matter, but dynamic jOOQ code resists conventional SQL extraction and AST-based detection.
   - Gap: little evidence on SQL antipattern prevalence in jOOQ projects and limited localisation-oriented LLM evaluation.
   - Sharp novelty comparison against extraction-based, API/AST-rule, LLM smell-classification, and LLM localisation studies.
   - No thesis-conversion or editorial-provenance argument.
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
4. Results
   - RQ1 detector evaluation and ground-truth sensitivity.
   - RQ2 confidence-tiered detector-output prevalence.
   - RQ3 exploratory co-detection with project-size confounding explicit.
   - RQ4 API method associations.
5. Discussion
   - SQL decay patterns in jOOQ projects.
   - Implications for jOOQ API use, documentation, and static-analysis tooling.
   - Comparison to prior SQLInspect/plain-SQL results with proxy caveat.
6. Threats to Validity
7. Conclusion
8. Prior-dissemination and other declarations

Use the full RQ wording as result subsection headings and close each with a concise answer.

## Section Word Budget

| Section | Target words |
|---|---:|
| Introduction | 650--800 |
| Background and Related Work | 1,600--2,000 |
| Study Design | 3,000--3,400 |
| Results | 2,800--3,500 |
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

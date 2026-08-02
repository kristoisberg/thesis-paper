# EMSE Conversion Workflow

Status: launched

Launched from the skill-forging workflow. This file starts the conversion workflow without drafting manuscript prose.

## Validated Inputs

- `thesis/`: TalTech master's thesis source, including LaTeX and PDF.
- `template/`: Springer SVJour3 template files.
- `examples/`: five related Empirical Software Engineering example papers.
- `paper/`: output workspace.
- `skills/`: project-local Codex-style skill packages for this workflow.

## Article Angle

An empirical study of LLM-based detection and localisation of SQL antipatterns in jOOQ-based database access code.

The main EMSE contribution should be the empirical evidence from the annotated dataset and 602-project mining study, with the LLM detector presented as the validated instrument that enables the study.

## Skill Sequence

1. `emse-journal-fit-auditor`
2. `emse-example-calibrator`
3. `thesis-evidence-extractor`
4. `emse-novelty-positioner`
5. `article-argument-architect`
6. `methodology-rigor-reviewer`
7. `results-synthesis-specialist`
8. `threats-and-reviewer-risk-editor`
9. `evidence-grounded-paper-expander`
10. `springer-latex-packager`
11. `acceptance-checker`

## Current Phase

Phase 2: feedback-driven journal expansion.

Initial conversion artifacts have been created:

- `paper/evidence-inventory.md`
- `paper/emse-style-guide.md`
- `paper/article-blueprint.md`
- `paper/reviewer-risk-checklist.md`
- `paper/main.tex`
- `paper/drafting-notes.md`
- `paper/feedback-remediation-matrix.md`

The first manuscript draft is being expanded from approximately 4,753 words to an evidence-backed target of approximately 12,000 words.

## Defaults Chosen

- Target venue: Springer's Empirical Software Engineering.
- Target format: SVJour3 LaTeX.
- Primary contribution: empirical software engineering study, not thesis condensation.
- RQ emphasis: thesis RQ4/RQ5 as primary findings; RQ1/RQ2 as method selection; RQ3 as detector validity.
- Supplementary material: use for full prompts, decision trees, confusion matrices, and large correlation matrices.
- Use full RQ text in result subsection headings.
- Use 0.88 as the primary detector result; treat 0.93 only as optimistic sensitivity analysis.
- Preserve explicit author-confirmation placeholders until the authors approve contribution roles and archival identifiers.

## Required User Data Before Submission-Ready Drafting

- final author list and order;
- affiliations and corresponding author email;
- ORCID values, if available;
- competing interests statement;
- funding statement;
- data availability wording;
- whether supplementary information is allowed/preferred;
- target manuscript length preference, if any.

## First Conversion Tasks

- Build an evidence inventory from the thesis LaTeX.
- Calibrate article structure from the five EMSE examples.
- Draft a paper blueprint with title options, RQs, contribution claims, section outline, and table/figure plan.
- Run methodology, results, and threats review passes before writing manuscript prose.

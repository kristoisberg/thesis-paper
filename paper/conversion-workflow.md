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
4. `article-argument-architect`
5. `methodology-rigor-reviewer`
6. `results-synthesis-specialist`
7. `threats-and-reviewer-risk-editor`
8. `springer-latex-packager`
9. `acceptance-checker`

## Current Phase

Phase 1: conversion blueprinting.

Initial conversion artifacts have been created:

- `paper/evidence-inventory.md`
- `paper/emse-style-guide.md`
- `paper/article-blueprint.md`
- `paper/reviewer-risk-checklist.md`
- `paper/main.tex`
- `paper/drafting-notes.md`

The first manuscript draft has started in `paper/main.tex`.

## Defaults Chosen

- Target venue: Springer's Empirical Software Engineering.
- Target format: SVJour3 LaTeX.
- Primary contribution: empirical software engineering study, not thesis condensation.
- RQ emphasis: thesis RQ4/RQ5 as primary findings; RQ1/RQ2 as method selection; RQ3 as detector validity.
- Supplementary material: use for full prompts, decision trees, confusion matrices, and large correlation matrices.

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

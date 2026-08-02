---
name: emse-orchestrator
description: Orchestrate a Tallinn University of Technology master's thesis to Springer's Empirical Software Engineering journal paper workflow. Use when coordinating the EMSE skill suite, validating source directories, launching conversion after skill forging, tracking workflow state, or deciding which thesis-to-paper specialist skill should run next.
---

# EMSE Orchestrator

Coordinate the skill suite for converting the thesis in `thesis/` into an EMSE-targeted Springer manuscript in `paper/`.

## Start Conditions

Expected repository layout:

- `thesis/`: source thesis PDF and LaTeX.
- `template/`: Springer SVJour3 LaTeX template files.
- `examples/`: EMSE example papers for style calibration.
- `paper/`: output workspace for the conversion.

If any directory is missing, stop and report the blocker.

## Workflow

1. Run `emse-journal-fit-auditor` to load current EMSE/Springer constraints.
2. Run `emse-example-calibrator` to derive style and structure patterns from `examples/`.
3. Run `thesis-evidence-extractor` to inventory reusable thesis evidence.
4. Run `article-argument-architect` to define the article angle, RQs, outline, and novelty claims.
5. Run `methodology-rigor-reviewer`, `results-synthesis-specialist`, and `threats-and-reviewer-risk-editor` as independent review passes.
6. Run `springer-latex-packager` to map accepted content to SVJour3 outputs.
7. Run `acceptance-checker` for desk-reject and reviewer-risk gates.

## Conversion Launch

After skill forging and validation, launch conversion by creating or updating a workflow state artifact in `paper/` before drafting manuscript text.

Minimum kickoff artifact:

- chosen article angle
- source directories validated
- skill sequence
- current phase
- blocking user-supplied data still needed
- first conversion tasks

Do not draft manuscript prose until required author/declaration data and the article blueprint are available.

## Defaults

- Target journal: Empirical Software Engineering.
- Publisher/template path: Springer SVJour3 LaTeX.
- Main angle: empirical study of LLM-based detection and localisation of SQL antipatterns in jOOQ projects.
- RQ emphasis: thesis RQ4/RQ5 as the primary EMSE empirical contribution; RQ1/RQ2 as method-selection evidence; RQ3 as detector validity.
- Supplementary material: use for large confusion matrices, full prompt listings, decision trees, and oversized appendix tables unless the user says otherwise.

## Hard Stop Conditions

Stop the workflow if:

- author list, affiliations, corresponding author, or competing-interest statement is needed for submission-ready outputs and missing;
- source evidence is unavailable or internally contradictory;
- requested edits would fabricate or strengthen unsupported empirical claims;
- Springer/EMSE guidance has changed and cannot be verified.


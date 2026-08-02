# EMSE Conversion Workflow

Status: feedback-remediation pass implemented; submission blockers remain

Launched from the skill-forging workflow. This file starts the conversion workflow without drafting manuscript prose.

## Validated Inputs

- `thesis/`: TalTech master's thesis source, including LaTeX and PDF.
- `template/`: Springer SVJour3 template files.
- `examples/`: five related Empirical Software Engineering example papers.
- `paper/`: output workspace.
- `skills/`: project-local Codex-style skill packages for this workflow.

## Article Angle

Validation of occurrence-localised LLM detection followed by bounded mining of detector outputs in jOOQ repositories.

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

Phase 3: adversarial-feedback remediation and readiness gating.

Initial conversion artifacts have been created:

- `paper/evidence-inventory.md`
- `paper/emse-style-guide.md`
- `paper/article-blueprint.md`
- `paper/reviewer-risk-checklist.md`
- `paper/main.tex`
- `paper/drafting-notes.md`
- `paper/feedback-remediation-matrix.md`

The manuscript has been restructured around one Results section, class-calibrated population claims, and explicit limits on unadjusted co-detection.

## Defaults Chosen

- Target venue: Springer's Empirical Software Engineering.
- Target format: SVJour3 LaTeX.
- Primary contribution: empirical software engineering study, not thesis condensation.
- RQ emphasis: thesis RQ4/RQ5 as primary findings; RQ1/RQ2 as method selection; RQ3 as detector validity.
- Supplementary material: use for full prompts, decision trees, confusion matrices, and large correlation matrices.
- Move split optimisation, provider configuration, retry, cost, and runtime detail to Online Resource 1.
- Use full RQ text in result subsection headings.
- Disclose thesis provenance in declarations and the cover letter, not the Introduction.
- Use 0.88 as the primary detector result; treat 0.93 only as optimistic sensitivity analysis.
- Preserve explicit author-confirmation placeholders until the authors approve contribution roles and archival identifiers.

No new study data were available for this pass. Population-output validation, repeated LLM runs, independent annotation, and project-size-controlled co-occurrence remain unperformed and must not be implied.

## Required User Data Before Submission-Ready Drafting

- final author list and order;
- affiliations and corresponding author email;
- ORCID values, if available;
- competing interests statement;
- funding statement;
- data availability wording;
- whether supplementary information is allowed/preferred;
- target manuscript length preference, if any.

## Remaining Tasks

- Confirm author contributions and corresponding author.
- Deposit and cite an immutable artifact snapshot and record exact commits/model/prompt identifiers.
- Compile the final flat submission package and re-run the acceptance gate.

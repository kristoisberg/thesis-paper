---
name: acceptance-checker
description: Perform final EMSE acceptance-readiness checks for a Springer manuscript. Use to simulate desk-reject and reviewer-reject risks, verify journal fit, novelty, empirical rigor, Springer formatting, abstract and keyword limits, declarations, AI-use disclosure, reproducibility statements, and removal of thesis-specific language.
---

# Acceptance Checker

Run this before considering the manuscript ready for submission.

## Desk-Reject Gate

Fail if the manuscript:

- reads as a condensed thesis;
- lacks a clear EMSE empirical contribution;
- hides the LLM detector validation behind tool-building narrative;
- has excessive textbook background;
- misses declarations or AI-use documentation;
- remains below the agreed journal-depth target without an explicit author decision;
- violates obvious Springer formatting requirements;
- makes unsupported novelty or generalizability claims.

## Reviewer-Reject Gate

Fail if the manuscript:

- does not confront the single-annotator limitation;
- presents corrected ground truth metrics as unbiased;
- implies statistical significance without tests;
- compares jOOQ proxy density directly to SQL-statement density;
- underreports repository mining and filtering;
- omits artifact availability or reproducibility constraints;
- does not explain localisation metrics clearly;
- reports performance ratios without TP, FP, FN, and test support;
- presents result sections without RQ-labelled headings and direct answers;
- leaves novelty as “an LLM applied to jOOQ”;
- omits or obscures the manuscript's relationship to the master's thesis.

## Mechanical Checks

Check:

- abstract: 150 to 250 words;
- keywords: 4 to 6;
- figures and tables cited in order;
- references cited and formatted consistently;
- no remaining `this thesis`, `Chapter`, or thesis-outline phrasing;
- all abbreviations defined at first use;
- main-manuscript length: normally 11,000 to 13,000 words for this project, treated as a project target rather than an EMSE rule;
- primary detector result is 0.88 and corrected 0.93 is labelled only as optimistic sensitivity analysis;
- every validity threat names an actual mitigation/sensitivity analysis and a residual claim boundary;
- Author Contributions, Code and Materials Availability, Data Availability, Ethics Approval, and Consent statements are present;
- no `[AUTHOR CONFIRMATION REQUIRED` or other unresolved submission placeholder remains;
- source compiles if LaTeX files exist.

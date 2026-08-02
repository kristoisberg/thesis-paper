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
- does not explain localisation metrics clearly.

## Mechanical Checks

Check:

- abstract: 150 to 250 words;
- keywords: 4 to 6;
- figures and tables cited in order;
- references cited and formatted consistently;
- no remaining `this thesis`, `Chapter`, or thesis-outline phrasing;
- all abbreviations defined at first use;
- source compiles if LaTeX files exist.


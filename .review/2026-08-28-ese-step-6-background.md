# ESE Step 6: background refocus

Date: 2026-08-28

Status: completed in commit `741ebae85192d318aca70dc5003d0f39d0767199`.

## Applied changes

- Reduced Background and Related Work to the SQL-antipattern definitions, jOOQ source representation, detection approaches, and occurrence localisation needed by the study.
- Replaced the broad antipattern catalogue with operational definitions of the seven evaluated classes.
- Condensed the four prompting configurations to one paragraph in Study Design and directed full prompts and decision rules to the Online Resources.
- Added a comparison of SQL extraction, API/AST rules, LLM source analysis, and this study's occurrence-level output.
- Identified the gap in occurrence-level localisation evidence for the seven retained classes in jOOQ code.

## Completion check

- Each background subsection supports an operational definition, detector input choice, or later interpretation.
- All seven evaluated classes and the occurrence-localisation unit are defined.
- The full taxonomy, prompt instructions, localisation rules, and examples remain outside the compiled main paper and are referenced as online materials.
- A forced `make paper` rebuild succeeds and produces a 55-page PDF with no undefined citations or references.
- The working tree matched the recorded commit before this metadata update.

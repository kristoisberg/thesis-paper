---
name: thesis-evidence-extractor
description: Extract and classify reusable scientific evidence from the TalTech thesis source for an EMSE journal paper. Use when mining thesis LaTeX/PDF for research questions, dataset facts, methodology, metrics, results, figures, tables, citations, limitations, and material to keep, compress, move to supplementary information, or discard.
---

# Thesis Evidence Extractor

Extract evidence from `thesis/` without treating the paper as a condensed thesis.

## Inputs

Start with:

- `thesis/main.tex`
- `thesis/chapters/chapters_main.tex`
- `thesis/misc/abstract-english.tex`
- `thesis/chapters/01_introduction.tex`
- `thesis/chapters/03_dataset_creation.tex`
- `thesis/chapters/04_evaluation.tex`
- `thesis/chapters/06_project_analysis.tex`
- `thesis/chapters/07_results.tex`
- `thesis/chapters/08_analysis.tex`
- `thesis/references.bib`

Use appendices only when main text points to a needed table, prompt, decision tree, or validation artifact.

## Classification Labels

Classify extracted material as:

- `main paper`: central to EMSE argument.
- `supplementary`: necessary for transparency but too large for the manuscript.
- `discard`: thesis-only, redundant, or not journal-relevant.
- `needs author decision`: requires non-discoverable information.

## Main Paper Priority

Prioritize:

- 1,562 human-annotated antipattern occurrences;
- 61 manually annotated open-source projects;
- 602-project large-scale analysis;
- 15,931 detected occurrences;
- seven detected SQL antipatterns;
- corrected and uncorrected tool evaluation;
- localisation framing using IoU and boundary matching;
- prevalence, co-occurrence, Jaccard, Spearman, and conditional probabilities;
- jOOQ API associations such as `selectFrom`, `select().from`, `Field.like`, and `containsIgnoreCase`;
- limitations and threats.

## Default Discards

Discard or heavily compress:

- thesis outline;
- generic SQL, jOOQ, LLM, or prompt-engineering background;
- implementation details of TypeScript, Bun, CLI architecture, or internal workflow unless needed for reproducibility;
- personal reflection and work-process narrative;
- exhaustive appendix tables in the main manuscript.

## Output Shape

Produce an evidence inventory with:

- claim or artifact;
- thesis source location;
- classification label;
- proposed article section;
- reviewer-risk note if any.


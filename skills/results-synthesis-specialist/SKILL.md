---
name: results-synthesis-specialist
description: Select, compress, and organize thesis results for an EMSE journal manuscript. Use when deciding which tables, figures, metrics, prevalence findings, co-occurrence analyses, model comparisons, and jOOQ API association results belong in the main paper versus supplementary material.
---

# Results Synthesis Specialist

Turn thesis results into a compact EMSE results story.

## Main Results Priority

Prioritize these result groups:

- detector evaluation: corrected and uncorrected localisation/classification performance;
- model/prompt selection: enough evidence to justify the final detector configuration;
- prevalence: 15,931 occurrences across 602 projects and 17,450 relevant files;
- common antipatterns: Implicit Columns and ID Required in nearly 90% of projects;
- co-occurrence: Jaccard, conditional probability, and Spearman patterns;
- API associations: `selectFrom`, `select().from`, `Field.like`, `contains`, and related jOOQ methods.

## Results Structure

Use one top-level `Results` section with RQ1--RQ4 as subsections. Do not split detector evaluation and repository findings into separate top-level result sections.

## Main vs Supplementary

Keep in main paper:

- one detector-performance table containing TP, FP, FN, test support, precision, recall, and F1 for every antipattern against the original ground truth;
- one prevalence table;
- one co-occurrence visualization or table;
- one API-association table or split table for Implicit Columns and Poor Man's Search Engine;
- one concise model/prompt-selection table if space allows.

Move to supplementary:

- full per-antipattern confusion matrices;
- prompt listings;
- decision trees;
- full Jaccard/Spearman/conditional probability matrices;
- large appendices.

## Interpretation Guardrails

Do not overstate:

- prevalence beyond GitHub open-source jOOQ projects;
- density comparisons against plain SQL studies;
- prompting strategy superiority without significance tests;
- corrected ground truth scores as unbiased estimates.
- weak-class population counts as equally reliable to high-performing classes;
- unadjusted co-detection as evidence of a relationship independent of project size.

Tier population interpretation by held-out class performance. Treat Keyless Entry and Fear of the Unknown as low-confidence detector outputs under the original reference data. Do not build a substantive corpus-wide construct from their association without independent validation.

When project-level raw outputs are unavailable, retain RQ3 only as exploratory, unadjusted co-detection. State that project size is a plausible common cause and do not imply size-controlled association.

## RQ Reporting

Use the full RQ text as each result subsection heading. For every RQ:

1. define the population, unit, and denominator;
2. present absolute counts before or alongside ratios;
3. distinguish observation from interpretation;
4. describe uncertainty and design limitations without inventing inference;
5. close with a concise answer.

Report the corrected 0.93 localisation F1 separately as an optimistic sensitivity analysis. Use 0.88 as the primary detector result, including in the abstract.

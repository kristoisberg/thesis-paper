# Focused density audit: worst offenders

Date: 2026-10-19

Scope: fresh read of the current sections 1, 2, 3, 4, and 6. The user explicitly requested a repeat audit with a stricter threshold: readability for capable readers while preserving scientific depth. No manuscript files changed.

Reviewers: writing-reviewer and logic-reviewer independently reread all five sections; parent synthesized the priorities. This focused list supersedes the earlier broad audit's editing priorities. Ordinary technical vocabulary, necessary operational definitions, and detailed but coherent procedures were not treated as defects.

## Findings to prioritise

### 1. Results: duplicate-file sensitivity

Location: `paper/sections/04_results.tex:138`.

This is the clearest offender. The paragraph moves through physical file occurrences, duplicate groups, excess copies, unique contents, class-and-span event unions, inconsistent event sets, representative selection, class distributions, and repository concentration. Readers repeatedly change counting units while retaining intermediate totals and following two robustness conclusions.

Minimal remedy: separate duplicate extent, counting procedure and alternative-count sensitivity, and the substantive robustness findings. A compact table could carry intermediate accounting and alternative totals, allowing the prose to explain the conclusions. Keep all technical information available, including the eight inconsistent groups, union versus representative procedures, and their different totals. Preserve numerical evidence for repository concentration as well as the breadth/repetition interpretation.

The purpose is to make the units and comparisons easy to follow, not to replace the analysis with a generic claim that the results were robust.

### 2. Study Design: corpus metrics and aggregation

Location: `paper/sections/03_study_design.tex:140`, continuing into the concentration rules at line 142.

The paragraph defines three quantities and three formulas, then introduces a second level of calculation through pooled and repository-equal density, eligibility rules, and the all-class denominator. The next paragraph adds size strata, top-group selection, rounding, and cutoff ties. Readers must retain the basic definitions while decoding several later operations.

Minimal remedy: keep the three basic measures and formulas together, explain cross-repository aggregation in a separate paragraph, and then introduce concentration analysis with its purpose. Place zero-flag inclusion and no-eligible-file exclusion beside the aggregation definitions. Preserve the notation, formulas, source-role distinctions, broad denominator, and exact selection/tie rules.

These are appropriate scientific concepts. Their grouping and order create the difficulty.

### 3. Threats to Validity: sampling defects, corrections, and selection

Location: `paper/sections/06_threats_to_validity.tex:19`.

The paragraph says sampling conditions remain in the sample and partitions, then says later analyses corrected counts, then introduces a file exclusion that still affects test coverage. Readers have to reconstruct what was corrected and what remained affected. The last sentence changes subject to model/prompt selection.

Minimal remedy: explain, in order, what affected the original sampling frame, which original sample/partition decisions remained fixed, and what later analyses corrected. Keep the test-exclusion disclosure explicit. Move the model/prompt selection limitation to its own paragraph or its existing conclusion-validity discussion, consolidating duplicate statements without removing the limitation.

No new causal explanation or assumption about how the counts were corrected should be added without checking the study records.

## Deliberately excluded from this priority list

- Introduction's gap and contribution wording.
- Background's jOOQ explanation, generic detection overview, and operational-definition cells.
- Study Design's model settings, provider choices, execution dates, and retry policies.
- Threats' bootstrap, corpus-denominator, and archive paragraphs.
- Minor repetition of values between Results prose and tables.

These passages may admit stylistic improvements, but that does not make them serious comprehension obstacles. The strict audit does not justify general simplification or a target percentage reduction.

The logic reviewer also nominated Results lines 134–136, which contain several repository-density summaries and comparisons. The parent considers these a lower priority: the prose is detailed, but the argument is more explicit than in the three selected passages. Preserve the distinction between size strata and highest-flag repositories if that material is edited later.

Both reviewers identified the duplicate-file paragraph and corpus-metric definitions as the strongest priorities. The parent selected the unclear correction chronology as the third because it obstructs understanding of the methodological limitation, rather than merely asking readers to follow technical results.

## Application and verification

Applied all three changes at the user's request. Results now separates the duplicate-file accounting into a referenced table and explains the two counting procedures before interpreting class distributions and union-weighted concentration. Study Design displays the unchanged metric formulas and gives aggregation its own paragraph. Threats explains the original sampling frame, later count corrections, unchanged sample/partitions, and remaining exclusion, with configuration selection in a separate paragraph.

All previously reported formatted numerical values in the three edited files are retained. A read-only reviewer verified the formulas, aggregation/eligibility rules, duplicate accounting, union versus representative interpretations, and sampling chronology against the prior text and local analysis records. No actionable issues were found.

`make paper` and `git diff --check` passed. No unresolved references or citations were reported. The new table and displayed formulas were visually checked in the compiled PDF. No overfull boxes occur in the revised passages; an existing 1.11-point warning remains in the Study Design overview. The rebuilt artifact is `paper/main.pdf`.

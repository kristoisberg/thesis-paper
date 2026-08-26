# Writing review: `paper/main.tex`

Date: 2026-08-26

## Overview

The manuscript is technically careful and generally clear. Its main prose weakness is repeated defensive qualification. Scope boundaries recur in the introduction, related work, methods, results, discussion, threats, and conclusion, which obscures the central contribution. The prose also overuses negation-contrast, long single-line paragraphs, and the word "bounded".

## Critical issues

1. Submission placeholders remain at lines 526, 529, 538, and 541.
   - They require author decisions, archive identifiers, and exact repository revisions.
   - Do not invent replacements or polish around them.

## Important issues

1. Rewrite the abstract at line 40.
   - State the task, held-out result, corpus result, and hybrid-design implication directly.
   - Remove the closing "complement, but not replace" construction.
   - Preserve every number and empirical qualification.

2. Lead the contribution paragraph at line 53 positively.
   - Replace the cluster of "rather than", "instead", and "do not claim" frames.
   - State that the contribution is a linked measurement design that validates the detector at the same granularity used for repository counting.

3. Reduce caveat saturation in related work, especially lines 89-125.
   - Keep one representation-comparison paragraph, one localisation-gap paragraph, and one positive contribution paragraph.
   - Move no technical claims or citations. Remove only repeated framing.

4. Remove the repeated operational-definition opening at lines 179-181.
   - Combine the 19-antipattern scope, 1,562 annotated occurrences, exclusions, and seven-class retention rule without weakening inclusion or exclusion criteria.

5. Merge the duplicate statement-proxy limitation at lines 244-246.
   - Keep the exact measurements.
   - State once that static API references support within-corpus comparison and do not estimate runtime or plain-SQL density.

6. Merge the repeated localisation rationale at lines 449-451.
   - Focus the discussion on inspectable warning regions, IoU boundary tolerance, duplicate penalties, and the remaining need for developer studies.

7. Reorganise the implications section at lines 465-475 around two findings.
   - Stable syntactic cases support deterministic rules.
   - Contextual cases require project evidence.
   - Avoid a role-by-role report and merge the two "The study also" paragraphs.

8. Rewrite systemic negation-contrast at representative lines 40, 51, 53, 89, 93, 174, 320, 445, 455, 461, 469, 498, 502, and 512.
   - State the supported claim first, then its exact boundary.

9. Split dense paragraphs at lines 40, 53, 117, 119, 170, 207, 304, and 483 where they combine method, interpretation, qualification, and implication.

10. Replace vague uses of "bounded" at lines 40, 73, 121, 459, 467, 491, 510, 514, and 523 with the actual limit, such as detector-output measurement, analysed corpus, or class-specific uncertainty.

## Minor issues

1. Line 153: repair parallelism in the project inclusion sentence.
2. Line 196: use "Cohen's kappa".
3. Line 207: change "had score 0.52" to "had a score of 0.52".
4. Line 266: change "different amount" to "different amounts" or "varying amount".
5. Line 350: add the second "has" in the comparison.
6. Use British `artefact(s)` consistently unless the journal mandates `artifact(s)`.

## Constraints for polishing

- Preserve all numerical results, equations, table contents, citations, antipattern names, model names, API identifiers, and LaTeX commands.
- Preserve the technical detail of the operational definitions beyond removing the duplicated opening.
- Preserve the substance of Threats to Validity. Remove repeated caveats elsewhere first.
- Leave unresolved submission placeholders intact.
- Keep British spelling and the established deductive, first-person-plural voice.

# Discussion readability review

Date: 2026-10-19

Scope: `paper/sections/05_discussion.tex`, with Results, Study Design, and Threats to Validity as context.

User constraint: preserve the existing structure and suggest improvements. No manuscript edits were requested or made in this review.

Reviewers: writing-reviewer and logic-reviewer, synthesized by the parent agent.

## Assessment

The three-subsection structure works. Density comes mainly from abstract wording, repeated qualifications, numerical recaps, and detailed proposals for future studies. A reduction of roughly 20–30% is a reasonable editing target, subject to preserving the substantive distinctions below. The source currently contains approximately 1,364 whitespace-delimited words, including LaTeX commands; this is a rough size measure, not TeXCount.

The earlier August review also identified repeated qualifications, but the Discussion was rewritten in October. These recommendations concern the current text rather than carrying forward old line-specific findings.

## Important recommendations

1. **State the practical insight in the opening.** Line 3 introduces class-specific validation, agreement, breadth, repetition, and density before explaining what the reader should do with them. State that antipattern classes require different review decisions and that their distributions suggest where to inspect code. Avoid implying that agreement scores alone identify the semantic decisions; the class definitions and error analysis supply that evidence.

2. **Remove the competing comparisons at line 7.** The paragraph introduces the combined corpus share of Implicit Columns and ID Required, then compares precision for Implicit Columns and Keyless Entry. Delete the 68.3% recap here. Open with the differing review questions and retain the precision comparison only as supporting evidence. The breadth/repetition contrast between Implicit Columns and ID Required belongs in subsection two.

3. **Give each class example one interpretive purpose.** At line 9, retain the audit-log disagreement and the need to decide whether a foreign key suits the application; shorten the repeated explanation about inferred relationships. At line 11, explicitly distinguish detector misses from omissions in the human reference. At line 13, retain the grouping example and its review implication; the pooled IoU sensitivity recap adds little and does not isolate grouping effects. Preserve these examples because they explain why a low agreement score can have different causes.

4. **Consolidate qualifications.** Lines 11 and 15 both call for independent validation, which subsection three then develops. Shorten the line-15 recap to a transition, or remove it if the adjacent paragraphs connect naturally. At line 23, two consecutive sentences warn that repeated expressions may not share a cause; one cautious recommendation is sufficient. At line 27, the exact-content sensitivity recap can remain in Results and Threats. Keep local qualifications that change a claim's meaning, especially the naming-based ID Required definition at line 21. Retain the distinction between inspection priorities and demonstrated harm, without repeating it after every recommendation.

5. **Keep the useful distribution contrast; compress the additional recap.** Line 19's approximate coverage and repetition figures directly support the schema/query review contrast and are worth retaining. Line 25's high-count share, relative density, and large-stratum comparison repeat Results. Explain the practical distinction directly: total counts show how many flags there are to inspect, while density shows their concentration relative to eligible-file count. Neither metric establishes actual remediation effort or severity.

6. **Introduce the audit's governing principle first.** Move the substance of line 37 to the beginning of subsection three: sample code from the corpus, include flagged and unflagged uses, and obtain independent annotations. Then use common projection forms, missed returning clauses, and search expressions as targeted examples. Preserve that fragment-category shares describe detector output and that eligible API uses are needed as denominators. The writing reviewer favored keeping the principle at the end as a consolidated protocol; the parent recommends introducing it first because it explains the purpose of all subsequent examples. Implementation details such as precedence-ordered pattern matching can stay in Study Design.

7. **Reduce future-work protocol detail.** At line 35, retain the need to distinguish search semantics, record uncertainty, and count consecutive expressions separately; shorten the exhaustive case list. At line 39, compress the deterministic-baseline proposal to two or three sentences explaining the fair comparison and the question it would answer. Retain the distinction between explicit syntactic conditions and contextual judgments. Do not imply that a rule-based baseline has already been implemented or evaluated.

## Example replacements

Opening at line 3:

> The results suggest that review should depend on the antipattern class and the distribution of its flags. We discuss what reviewers need to check, where to focus their attention, and how an independent audit could test the corpus findings.

Keyless Entry topic sentence at line 9:

> Keyless Entry flags require a decision about whether the application needs a foreign-key constraint.

Reference-error explanation at line 11:

> The low F1 reflects both detector misses and omissions in the reference annotations.

Audit principle from line 37:

> An independent audit should sample code directly from the repositories, including expressions the detector did not flag. Reviewing flagged expressions can identify false positives, while reviewing unflagged expressions can reveal missed occurrences.

These are illustrative prose suggestions, not replacements applied to the manuscript. The sampling design and eligible-expression inventory still need to support any precision/recall estimates.

## Editing priorities

First remove duplicated qualifications and result recaps. Then rewrite abstract topic sentences around concrete review decisions. Finally shorten the future-study protocols. Preserve the three headings and their order, the substantive class-specific examples, and the distinction between observed findings and proposed uses. Aim for one main claim per paragraph, only the evidence needed to support it, and a clear implication.

## Application

Applied at the user's request after the review. The discussion now contains approximately 910 whitespace-delimited words, down from 1,364, a 33.3% reduction using the same rough measure. The three subsection headings, their order, section label, and supporting bibliography citation are preserved. The parent checked the rewritten claims against the reported class errors, corpus distributions, and operational definitions.

`make paper` and `git diff --check` passed. The final LaTeX log reports no unresolved references or citations and no overfull boxes in the Discussion. Two overfull-box warnings remain in unchanged passages of Study Design and Threats to Validity. The rebuilt PDF is `paper/main.pdf`.

# Density audit of sections 1, 2, 3, 4, and 6

Date: 2026-10-19

Scope: current Introduction, Background and Related Work, Study Design, Results, and Threats to Validity. Read-only manuscript audit. No manuscript files changed.

Reviewers: writing-reviewer for sections 1, 2, and 6; logic-reviewer for sections 3 and 4; parent synthesis across all five sections. Earlier August reviews predate the rewritten material and were not treated as a substitute for reading the current text.

## Overall assessment

Study Design and Results contain the most sustained density. Threats to Validity has several overloaded paragraphs. Background needs a focused reduction in repetition. The Introduction is comparatively lean and needs selective simplification, especially its contribution list.

The common problem is the number of jobs assigned to a paragraph: conceptual explanation, numerical evidence, implementation rules, exceptions, and limitations compete for attention. Shortening individual sentences alone would leave much of this problem intact. Preserve the existing overall structure; improve the ordering and separation of material inside it.

No critical scientific defect was established by this prose audit. The recommendations below concern reading effort and the clarity of the evidence, not a re-evaluation of external sources or the underlying analyses.

## Highest-priority passages

### 1. Results: duplicate-file sensitivity, line 138

This is the strongest single hotspot. It combines the scale of duplication, duplicate groups, extra physical copies, unique file contents, event unions, inconsistent event sets, representative selection, class breadth/repetition, and repository concentration. The paragraph asks readers to reconstruct two counting procedures while tracking two robustness conclusions.

Lead with the substantive conclusion and give its supporting figures next. Separate the class-distribution result from repository concentration. Place the full accounting of duplicate groups and alternative counting totals in a compact sensitivity table or supplement, with an explicit main-text reference. Preserve the eight inconsistent groups and the distinction between union and representative-based results in that destination; those procedures yield different totals.

Possible lead:

> Accounting for byte-identical files preserved the main corpus patterns. ID Required remained broader across eligible files with almost no repetition within flagged files. Implicit Columns remained narrower and more repetitive.

Then give the concentration result and a reference to the detailed accounting. This is a proposed reorganisation, not permission to omit the alternative counting results.

### 2. Study Design: corpus measures and concentration rules, lines 140–142

Line 140 introduces three symbols and formulas, two aggregation methods, zero and undefined-denominator rules, and an all-class measure. Line 142 immediately adds size strata, selection of the highest-count tenth, rounding, tie-breaking, shares, density ratios, and tie bounds.

Explain the questions first. Then present the three metric definitions together, followed by pooled versus repository-equal density and their eligibility rules. Introduce repository concentration separately before describing its selection machinery.

Possible conceptual lead:

> We distinguish how broadly flags occur across eligible files from how often they repeat within a flagged file. File breadth is the percentage of eligible files with at least one flag. Repetition is the mean number of flags per flagged file. Density is the number of flags per 100 eligible files.

Keep formulas available, ideally in a compact definition table or displayed separately with their names. Preserve zero-flag inclusion, omission of repositories with no eligible files, role-specific denominators, and the all-class denominator. Exact rounding and tie rules can follow the purpose of the concentration analysis rather than precede understanding of it.

### 3. Study Design: configuration and execution, lines 112–118

These paragraphs alternate among compared configurations, gateway and SDK, model-specific settings, an exceptional temperature choice, implementation assistance, detector behaviour, held-out counts/cost/runtime, execution dates, provider instability, revision identifiers, and retry policies.

Organise them as configuration comparison, detector operation, and execution records, without requiring a new top-level structure. A model-settings table could carry the settings. A compact execution record or the replication documentation could carry exact dates, revisions, and retry policies. Keep the routing change and temperature exception available because they affect reproducibility. Retain a clear disclosure and link in the main text if details move.

Held-out prediction count, cost, and runtime at line 114 are results. Place them with the held-out results, or use a short cross-reference from Methods, so the description of detector operation has one purpose.

### 4. Results: repository density and concentration, lines 134–136

The passage moves through pooled density, repository-equal mean, median, interquartile interval, count–size correlation, file and flag shares, three size-stratum densities, and top-group estimates with cutoff-tie ranges. Readers receive the arithmetic before the comparison is fully established.

State the observation first: flag totals reflect both file volume and flag density. Separate size-stratum evidence from the highest-count group. Let a table carry the full descriptive distribution and keep only the values needed for the main comparison in prose. Preserve the distinction between the largest repositories by file count and the repositories with the most flags. Tie bounds should remain beside the estimates they qualify.

### 5. Threats: corpus-measure limitations, line 9

One paragraph covers eligible-file denominators, absence of relevant opportunities, detector error, unresolved call targets, interpretation of four corpus measures, and the requirements for prevalence or API-risk estimates. Terms such as “role-eligible files,” “class-specific opportunities,” and “API-opportunity denominators” arrive in rapid succession.

Keep the concrete application-file example. Explain denominator limitations in one paragraph and fragment-classification limitations in another. Replace abstract denominator language with the actual counting distinction: eligible files versus eligible projections, search predicates, or other class-specific uses. Preserve that corpus statistics describe detector output and that prevalence estimation needs independent validation and suitable opportunity counts.

### 6. Threats: conclusion validity, line 33

The first five sentences now give a reasonably clear explanation of the bootstrap. The paragraph becomes dense when it appends configuration comparisons, IoU sensitivity, and a general conclusion boundary.

End the bootstrap paragraph after the sparse-class resampling limitation. Consolidate the descriptive configuration-comparison limitation with the single-validation-partition/single-run statement at line 19. The IoU limitation already appears at line 7. Remove the final general disclaimer if the specific qualifications remain clear. Preserve the conditional nature of the bootstrap and the absence of a run-to-run uncertainty estimate.

## Other section-specific improvements

### Introduction

- **Lines 21–23, contributions:** each bullet is a compressed methods inventory. Keep the dataset, evaluation, and corpus-analysis contributions, but reduce the technical qualifiers that will be defined later. “File-normalised characterisation,” “exact-content sensitivity,” and “source-fragment patterns” make the reader learn the analysis vocabulary before seeing its purpose. For example, the third contribution could begin “an analysis of how detector flags are distributed across files and repositories in a 602-repository corpus.” Preserve the important scope details in Methods.
- **Line 7, gap paragraph:** explain the jOOQ representation, then the localisation gap. The full three-way catalogue of prior detection approaches is already developed in Background. “Source units” could be replaced with a concrete term or explained where used. Retain the citations and the distinction between recognition and localisation.
- The rest of the Introduction does not warrant general shortening.

### Background and Related Work

- **Line 53, jOOQ representation:** the paragraph teaches the DSL, code generation, schema classes, analysed inputs, and JDBC/plain SQL in one block. Explain query calls and generated classes first. Put the plain-SQL alternative in its own short paragraph so the following SQL/jOOQ example has a clear role.
- **Lines 78–92, detection overview:** generic metrics/rules/learning descriptions delay the SQL-specific literature, and repeated paragraph endings state that representation or output units matter. The comparison table and closing paragraph repeat the same point. Shorten the generic taxonomy; retain the specific evidence from DbDeo, SQLInspect, SQLCheck, and the LLM studies. Let the table carry the compact representation/output comparison and state the localisation gap once at the end.
- **Lines 30–48, definition table:** some density is necessary. The Keyless Entry row combines its condition, view exclusion, and referenced-key requirement in one sentence. Split those into short sentences within the cell. Preserve every inclusion and exclusion. Apply the same treatment to Fear of the Unknown's inclusion cases and Java-related exclusions. Check layout after edits because extra sentences can change table height.

Possible jOOQ explanation, retaining the existing supporting citations in an implementation:

> jOOQ constructs SQL through typed Java calls. Its code generator produces Java classes for tables, columns, keys, and constraints from a database schema. Queries refer to these generated objects, so analysing DSL code requires examining both query calls and schema classes.

Then describe the JDBC/plain-SQL alternative separately.

### Study Design

- **Line 54, annotation records:** the spreadsheet-to-CSV conversion interrupts the explanation of what constitutes an annotation. Keep the actual annotation fields and matching unit together; put storage-format history with data-release information if retained.
- **Lines 66–72 and 94, partitions:** reduce repeated explanations of whole-project assignment, but protect the substantive disclosures. All annotations informed the support rule and seed search, the detector configuration was fixed before test execution, and occurrence balance does not guarantee broad project support. The support threshold and label-informed split must remain explicit.
- **Line 148, fragment coding:** “precedence-ordered list” can be explained directly as assigning each fragment to the first matching pattern. Preserve what is categorised, how unmatched fragments are handled, and where the ordered patterns are recorded.

### Results

- **Line 5, selection:** the catalogue of models and prompting methods repeats Methods and the adjacent table. Keep the selected configuration, the tied displayed F1, the shortest runtime among Zero-Shot configurations, and the higher-F1/more-expensive prompting tradeoff. Avoid implying it was the cheapest or fastest configuration overall.
- **Lines 29–31, agreement:** lead with micro F1 and class variation. Keep prediction/reference/event counts with the main agreement table. Put macro and support-weighted precision/recall values alongside tabulated results, retaining a useful F1 comparison in the prose. Do not silently drop metrics.
- **Lines 56 and 78, class errors:** the lead and closing paragraph both summarise the error table. Keep one organising statement and the informative table.
- **Lines 80–103:** revised-reference, overlap-threshold, and project-composition sensitivity currently sit under “Class-specific errors.” A short “Sensitivity analyses” subheading would signal their different purpose while preserving the main structure. Use the same sequence as Methods.
- **Lines 82, 87, and 101:** the overlap-sensitivity range is repeated in prose, caption, and prose. State the finding once; keep the caption self-contained enough to define the analysis.
- **Lines 142–144:** retain summaries that combine categories, such as the leading forms' combined share. Let the adjacent table carry individual category totals and percentages already visible there.
- Preserve caption definitions needed to interpret the tables independently, especially source roles, denominators, and aggregation methods.

### Threats to Validity

- **Line 19, internal validity:** separate sampling/exclusion history from model selection. Explain what was wrong, what was corrected later, and what remained in the original sample/partitions in that order. Keep the skipped annotated table disclosure. Consolidate the one-partition/one-run model comparison here or in Conclusion Validity, choosing one home rather than repeating it.
- **Line 41, reproducibility:** separate what can be recomputed from what prevents exact replay. Keep the replication and manifest links, but reduce the archive inventory in prose if those records already provide it. Preserve the distinction between recalculating analyses from stored outputs and repeating hosted-model requests.

## Editing order and boundaries

Start with Results line 138, Methods lines 140–142 and 112–118, then Results lines 134–136. Next separate the mixed validity paragraphs. Background's generic overview and the Introduction's contribution bullets are smaller, lower-risk edits.

Do not apply a uniform percentage cut across sections. The Introduction is already short, and operational definitions and reproducibility rules carry necessary complexity. The goal is to keep exact information accessible while reducing the number of concepts readers must track at once. This audit does not authorise manuscript edits; implementation remains a separate user decision.

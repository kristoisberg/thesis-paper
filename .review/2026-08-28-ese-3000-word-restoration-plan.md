# ESE 3,000-word restoration plan

Date: 2026-08-28

Status: in progress. Steps 1--8 were completed on 2026-08-28; see the corresponding reports in `.review/`.

Baseline: commit `098d195c58c72705ff5263af466f92561afa032f`.

Scope: increase the main article by about 3,000 words while preserving the corrected three-RQ ESE structure. The expansion should reuse the original thesis in `paper/chapters/` as its prose source. Newly generated prose is limited to transitions, factual corrections, and short synthesis sentences.

## Target and counting rule

The current main article is 25 pages. TeXCount reports 6,985 words when text, headings, captions, and the front matter are included. Text extracted from the compiled PDF contains 9,332 whitespace-delimited words, including the references. The latter is the measure comparable to the proposal's practical 12,000--18,000-word target, which explicitly includes references.

The implementation target is a **net addition of 3,000 TeXCount-visible manuscript words**, with an acceptable range of 2,850--3,150. That should produce approximately 9,985 TeXCount words and 12,300 PDF-extracted words, subject to LaTeX tokenisation. The expected page range is 30--32 pages, which reaches the lower end of the 30--40-page practical target.

| Section | Baseline TeXCount | Planned net addition | Approximate target |
|---|---:|---:|---:|
| Introduction | 384 | 68 | 452 |
| Background and Related Work | 789 | 556 | 1,345 |
| Study Design | 2,287 | 1,336 | 3,623 |
| Results | 1,224 | 559 | 1,783 |
| Discussion | 777 | 267 | 1,044 |
| Threats to Validity | 926 | 0 | 926 |
| Conclusion | 163 | 0 | 163 |
| **Net change** |  | **2,786** |  |

The section figures are planning controls, not quotas to fill with weak material. Step 8 removed 159 TeXCount words of duplicated definitions, repeated table narration, thesis navigation, and mechanical summary while retaining the thesis-derived methodological and quantitative detail needed for the argument. The reconciled net addition is 2,786 words, 64 below the plan's tolerance. No material was added merely to cross that threshold: the compiled paper already exceeds the practical targets at 12,393 layout-extracted words and 31 pages. Step 9 will record this deviation in the final audit.

## Source-reuse protocol

1. Start each new paragraph from a named paragraph or paragraph sequence in `paper/chapters/`; do not draft from a blank prompt.
2. Preserve the original paragraph's argumentative job, sentence order, and viable sentence structure. Change only what is needed to fit the article's terminology, evidence boundary, and surrounding text.
3. Record the source file and line range in the step report or working ledger. Do not leave provenance comments in the submitted TeX.
4. Limit new connective prose to about 15% of the net addition. If a legacy passage cannot be made accurate through local edits, omit it instead of replacing it with a newly generated paragraph.
5. Recheck every retained number, model setting, denominator, citation, and cross-reference against the current article and frozen analysis. The current article wins whenever it conflicts with the thesis.
6. Keep the article's evidential vocabulary: *reference annotations*, *agreement*, *detector flags*, *source-fragment patterns*, and *optimistic sensitivity analysis*. Do not restore *ground truth*, unqualified *prevalence*, cross-study superiority, causal model explanations, or practical-utility claims.
7. Use tables as evidence and restored prose for rationale or interpretation. Do not turn table rows into repetitive sentences merely to increase the count.

## Incremental execution plan

Each step should leave the main article compilable and should receive its own short report with the source ledger, net word change, and verification results.

### Step 1: Freeze the expansion baseline and create the reuse ledger

Status: completed on 2026-08-28. See `2026-08-28-ese-word-restoration-step-1-baseline-ledger.md`.

Actions:

- Record the current commit, TeXCount total, PDF-extracted count, page count, and per-section counts shown above.
- Create a source ledger containing one row for each restored paragraph: legacy location, current destination, intended argumentative job, expected net addition, and required factual changes.
- Treat the present title, central claim, three RQs, reported measurements, retained floats, online-resource boundary, and Step 13 evidence limitations as fixed.
- Save the manuscript diff before each subsequent section so that source-led edits can be reviewed independently.

Completion check: the baseline reproduces 6,985 TeXCount words, 9,332 PDF-extracted words, and 25 pages; every planned paragraph has a legacy source before prose editing starts.

### Step 2: Restore the Introduction's problem progression (+68 words)

Status: completed on 2026-08-28. See `2026-08-28-ese-word-restoration-step-2-introduction.md`.

Primary sources:

- `paper/chapters/01_introduction.tex:5-6`
- `paper/chapters/02_background.tex:25-27`

Actions:

- Expand the opening around attributed prior evidence that SQL antipatterns persist and may receive little remediation priority.
- Preserve the current movement from SQL-antipattern motivation to jOOQ representation, then to the occurrence-localisation evidence gap.
- Keep the current RQs and contribution list unchanged except for mechanical transitions.

Do not restore the old five RQs, thesis outline, broad Design Science Research framing, first-of-its-kind claim, claims that tool scarcity causes antipattern persistence, or claims that deterministic analysis is inherently infeasible.

Completion check: the Introduction gained 68 words and reaches the measurement problem by its third conceptual move. The original 180-word allocation could not be supported without duplicating existing motivation or adding connective filler, so the remaining 112 words were reassigned to Step 4's source-rich repository-mining material.

### Step 3: Restore the related-work argument (+599 words)

Status: completed on 2026-08-28. See `2026-08-28-ese-word-restoration-step-3-background.md`.

Primary sources:

- `paper/chapters/02_background.tex:5,7,11-13`
- `paper/chapters/02_background.tex:85`
- `paper/chapters/02_background.tex:104-112`
- `paper/chapters/02_background.tex:135-145`

Actions:

- Add the original distinction between SQL antipatterns and neighbouring code-smell concepts, followed by the Implicit Columns maintenance mechanism.
- Expand the jOOQ subsection with the original DSL, code-generation, generated-schema, and JDBC sequence, retaining only details needed to understand the analysed representation.
- Restore the progression from metric-based analysis to AST/rule-based analysis, learned detectors, and LLM-based detection.
- Expand the existing SQL-specific comparison with only the representation and output-unit details needed to support the localisation gap. Let the existing localisation-gap paragraph provide the synthesis.

Do not restore the full 19-class taxonomy, prompt-engineering tutorial, promotional jOOQ adoption claims, CodeRabbit claims, the statement that only two SQL tools exist, or numerical cross-study rankings. Use "coverage has not been established" rather than "incapable."

Completion check: Background gained 599 words, within the planned 594--726 range. Its final paragraph still identifies the output-unit gap; every restored tool description has a citation and is used by the synthesis.

### Step 4: Restore procedural depth in Study Design (+1,388 words)

Status: completed on 2026-08-28. See `2026-08-28-ese-word-restoration-step-4-study-design.md`.

Primary sources and sub-budgets:

| Topic | Legacy source | Actual net addition |
|---|---|---:|
| Generated-class requirement and manifest-search rationale | `paper/chapters/03_dataset_creation.tex:11-15` | 254 |
| Filtering and duplicate-review rationale | `paper/chapters/03_dataset_creation.tex:21-27` | 63 |
| Relevant-file definition and size-stratum rationale | `paper/chapters/03_dataset_creation.tex:64-71,89-113` | 227 |
| Selected operational-scope examples | `paper/chapters/03_dataset_creation.tex:117-131` | 60 |
| Annotation records, iterative codebook, and washout procedure | `paper/chapters/03_dataset_creation.tex:137-160` | 214 |
| Project-disjoint split roles and label-informed selection | `paper/chapters/03_dataset_creation.tex:203-217,235-239` | 135 |
| Model-selection criteria | `paper/chapters/04_evaluation.tex:5-21` | 156 |
| Prompt construction and refinement | `paper/chapters/04_evaluation.tex:33-58` | 279 |

Actions:

- Preserve the empirical-pipeline order already used in the article; expand within existing subsections rather than adding new top-level structure.
- Restore why generated classes were required, why manifest queries were used, how irrelevant files and duplicate repositories were handled, and what the search cannot cover.
- Restore the sampling rationale without calling the sample statistically representative or adding an uncited Head--Tail Breaks label.
- Explain the annotation record, iterative guideline revision, washout sampling, and exact-span repeatability using the thesis's paragraph sequence. Retain the distinction between repeatability and correctness.
- Explain the separate roles of training, validation, and test projects, whole-project assignment, support filtering, and the label-informed seed search. Keep equations and the full support table online.
- Restore the two-prompt division, supplied key context, line numbering, and decision-rule refinement. Do not reproduce full prompts.
- Leave the current matching equation and aggregate definitions unchanged; they already provide the necessary detail.

Do not restore implementation architecture, CLI options, complete prompts, the complete 19-class codebook, the full split table, obsolete model parameters, or unpreserved validation-run details. The Step 13 disclosure about missing exact validation outputs remains unchanged.

Completion check: Study Design gained 1,388 words, nine below the provisional tolerance. Padding and disallowed legacy detail remained excluded. The unused 164-word allocation moved to R01 in Step 5, whose legacy class-error narratives contain concrete source examples.

### Step 5: Restore concrete result detail (+550 words)

Status: completed on 2026-08-28. See `2026-08-28-ese-word-restoration-step-5-results.md`.

Primary sources:

- `paper/chapters/08_analysis.tex:31-35,38-40,45-49,52-58,61,71,74-81`
- `paper/chapters/07_results.tex:390-400,408-410,442-444`

Actual net additions were 368 words for R01, 87 words for R02, and 95 words for R03. R01 used the source-rich allocation carried forward from Step 4 without padding to its full provisional budget.

Actions:

- After the class-error summary table, restore a compact class-by-class factual narrative for the most informative disagreements. Preserve the original order of the seven classes but combine classes whose only contribution would repeat a table cell.
- Describe the observed code forms and detector/reference judgments, not inferred model reasoning. Identify all revised-reference judgments as detector-informed.
- Restore flags-per-repository and flags-per-flagged-repository context where it helps interpret RQ2.
- Restore the lower-frequency RQ3 manifestation categories in prose only when they complete the distribution rather than restate every row.
- Verify all retained counts and percentages against the current tables and frozen analysis, not the old thesis text.

Do not restore classification-only results, the old RQ numbering, the IoU grid already assigned online, the large per-class tables, or unqualified occurrence/prevalence language.

Completion check: Results gained 550 words, within the planned 508--620 range. Every restored sentence reports an observation, comparison, or direct answer; inferred model reasoning and prompt causality remain excluded.

### Step 6: Restore the Discussion's analytical chain (+340 words)

Status: completed on 2026-08-28. See `2026-08-28-ese-word-restoration-step-6-discussion.md`.

Primary sources:

- configuration-comparison paragraphs from `paper/chapters/07_results.tex:61,87,91,115,123,147,155-157`
- selected future-work sentences from `paper/chapters/08_analysis.tex:187,193,197,199`

Actual net additions were 153 words for D01 and 187 words for D02.

Actions:

- Add a compact interpretation of the configuration results. Zero-Shot was the simpler and lower-cost choice. In the reported Opus comparison it was faster than Chain-of-Thought and Tree-of-Thought, but 15 seconds slower than Few-Shot. Preserve the original comparison sequence while stating that the results came from single runs whose exact outputs are unavailable.
- Restore bounded follow-up directions for broader taxonomies, smaller or self-hosted models, other query builders, and further analysis of the preserved flags. State them as experiments to run, not improvements that will occur.

Do not restore the work-process reflection, schedule narrative, model-release commentary, direct cross-study F1 ranking, claims about developer benefit, or unsupported claims that RAG, preprocessing, or a particular model will improve accuracy or cost.

Completion check: Discussion gained 340 words, within the planned 288--352 range. Each restored paragraph begins from a current result or a scoped design difference, and the new analysis does not repeat a Results paragraph. The main PDF now contains 12,352 extracted words across 31 pages, so subsequent steps are verification-only work rather than further expansion.

### Step 7: Confirm that Threats to Validity needs no expansion (+0 words)

Status: completed on 2026-08-28. See `2026-08-28-ese-word-restoration-step-7-threats-audit.md`.

Actions:

- Verify that the existing construct, internal, external, conclusion, and reliability subsections still cover the effects of the restored method detail.
- Keep the existing manifest-search, GitHub API-cap, single-run, bounded gateway/provider, missing-metadata, and replay limitations. The earlier reference to an existing caching limitation was stale: the section contains no cache-effect claim, and the surviving evidence does not show that caching affected the single-pass runs.
- Add no prose unless a later restoration step creates a genuinely new threat.

Do not claim that the omitted population is small, that the chosen mining approach was best, or that gateway routing affected runs for which routing evidence is unavailable.

Completion check: Threats remained at its 926-word baseline. Parallel consistency and logic reviews found complete, non-duplicative coverage. A technical review proposed explicit codebook and future-caching sentences, but the existing construct and reliability paragraphs already cover the codebook consequence, while a caching sentence would introduce an unevidenced provider mechanism. No manuscript change was required.

### Step 8: Reconcile the restored prose

Status: completed on 2026-08-28. See `2026-08-28-ese-word-restoration-step-8-reconciliation.md`.

Actions:

- Read the article linearly from Introduction through Conclusion, comparing every added paragraph with the paragraphs immediately before and after it.
- Remove duplicate definitions, table narration, thesis-navigation language, and conclusions stated before their evidence.
- Merge abrupt one-sentence bridge paragraphs into adjacent source-led paragraphs where possible.
- Run terminology, number, citation, label, and RQ wording searches used in Step 13.
- Apply a restrained language pass: remove generic throat-clearing, stacked signposting, false causal connectors, inflated novelty, repetitive three-item summaries, and claims about what an LLM "understands." Preserve the original author's viable wording instead of synonymising it.
- Keep the current Abstract and Conclusion unchanged unless a restored passage exposes a factual inconsistency. Word-count pressure alone is not a reason to lengthen them.

Completion check: all 19 restored paragraph units remain mapped to the legacy source ledger, and Step 8 introduced no new freestanding paragraph. The reconciliation removed 159 TeXCount words rather than adding padding to retain the numerical budget. The title, unchanged abstract, RQs, direct answers, Discussion, and unchanged Conclusion remain claim-consistent.

### Step 9: Build, inspect, and measure the final article

Actions:

- Run `make clean && make paper`.
- Check both logs for LaTeX errors, undefined references or citations, overfull boxes, and BibTeX warnings.
- Inspect the main PDF for new widows, orphan headings, table displacement, excessive white space, and pages consisting mostly of floats.
- Re-run TeXCount inside the repository's TeX Live container with `-inc -sum`.
- Run `pdftotext -layout paper/main.pdf - | wc -w` and `pdfinfo paper/main.pdf`.
- Compare section deltas against the budget table and explain any movement greater than 10%.
- Produce a final report containing the reuse ledger, exact net count, final PDF-extracted count, page count, build status, and any deviations from this plan.

Completion check: the net TeXCount increase is 2,850--3,150 words, the compiled main PDF contains at least 12,000 extracted words and at least 30 pages, and all Step 13 repository-local checks still pass. If the article reaches the word target before all planned passages are restored, stop; do not add the remaining passages as padding.

## Material that remains excluded

- the old five-RQ framing and thesis outline;
- the complete SQL-antipattern catalogue and decision trees;
- full prompt listings and configuration-option catalogues;
- implementation architecture, CLI detail, and development diary;
- classification-only evaluation and cross-domain ranking tables;
- work-process reflection, AI-writing reflection, and personal/supervisor narrative;
- unsupported novelty, superiority, causality, prevalence, API-risk, and developer-utility claims;
- exact validation settings or outputs that the surviving artefacts cannot establish;
- tables and appendices already assigned to Online Resource 1.

These exclusions are structural and evidential safeguards, not a reserve to draw from if the target is missed.

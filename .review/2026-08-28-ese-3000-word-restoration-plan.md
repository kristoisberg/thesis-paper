# ESE 3,000-word restoration plan

Date: 2026-08-28

Status: proposed; no manuscript text has been changed.

Baseline: commit `098d195c58c72705ff5263af466f92561afa032f`.

Scope: increase the main article by about 3,000 words while preserving the corrected three-RQ ESE structure. The expansion should reuse the original thesis in `paper/chapters/` as its prose source. Newly generated prose is limited to transitions, factual corrections, and short synthesis sentences.

## Target and counting rule

The current main article is 25 pages. TeXCount reports 6,985 words when text, headings, captions, and the front matter are included. Text extracted from the compiled PDF contains 9,332 whitespace-delimited words, including the references. The latter is the measure comparable to the proposal's practical 12,000--18,000-word target, which explicitly includes references.

The implementation target is a **net addition of 3,000 TeXCount-visible manuscript words**, with an acceptable range of 2,850--3,150. That should produce approximately 9,985 TeXCount words and 12,300 PDF-extracted words, subject to LaTeX tokenisation. The expected page range is 30--32 pages, which reaches the lower end of the 30--40-page practical target.

| Section | Current TeXCount | Planned net addition | Approximate target |
|---|---:|---:|---:|
| Introduction | 384 | 250 | 634 |
| Background and Related Work | 789 | 650 | 1,439 |
| Study Design | 2,299 | 950 | 3,249 |
| Results | 1,224 | 400 | 1,624 |
| Discussion | 777 | 600 | 1,377 |
| Threats to Validity | 926 | 150 | 1,076 |
| Conclusion | 163 | 0 | 163 |
| **Net change** |  | **3,000** |  |

The section figures are planning controls, not quotas to fill with weak material. A section may finish up to roughly 10% above or below its allocation if the overall net addition remains within range.

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

Actions:

- Record the current commit, TeXCount total, PDF-extracted count, page count, and per-section counts shown above.
- Create a source ledger containing one row for each restored paragraph: legacy location, current destination, intended argumentative job, expected net addition, and required factual changes.
- Treat the present title, central claim, three RQs, reported measurements, retained floats, online-resource boundary, and Step 13 evidence limitations as fixed.
- Save the manuscript diff before each subsequent section so that source-led edits can be reviewed independently.

Completion check: the baseline reproduces 6,985 TeXCount words, 9,332 PDF-extracted words, and 25 pages; every planned paragraph has a legacy source before prose editing starts.

### Step 2: Restore the Introduction's problem progression (+250 words)

Primary sources:

- `paper/chapters/01_introduction.tex:1-8`
- selected context clauses from `paper/chapters/01_introduction.tex:14`

Actions:

- Expand the opening around the original progression from database use, recurring SQL mistakes, reported persistence, and detection motivation.
- Preserve the current movement from SQL-antipattern motivation to jOOQ representation, then to the occurrence-localisation evidence gap.
- Reuse only the original context-specific and cross-file observations needed to explain why a jOOQ occurrence can depend on generated schema code.
- Keep the current RQs and contribution list unchanged except for mechanical transitions.

Do not restore the old five RQs, thesis outline, broad Design Science Research framing, first-of-its-kind claim, claims that tool scarcity causes antipattern persistence, or claims that deterministic analysis is inherently infeasible.

Completion check: the Introduction gains 225--275 words, reaches the measurement problem by its third conceptual move, and introduces no claim absent from Background or Study Design.

### Step 3: Restore the related-work argument (+650 words)

Primary sources:

- `paper/chapters/02_background.tex:5,11-13,25-27`
- `paper/chapters/02_background.tex:85-100`
- `paper/chapters/02_background.tex:104-114`
- `paper/chapters/02_background.tex:133-145`
- the localisation distinction in `paper/chapters/04_evaluation.tex:155`

Actions:

- Add the original distinction between SQL antipatterns and neighbouring code-smell concepts, followed by the Implicit Columns maintenance mechanism and carefully attributed prior evidence.
- Expand the jOOQ subsection with the original DSL, code-generation, generated-schema, and JDBC sequence, retaining only details needed to understand the analysed representation.
- Restore the progression from metric-based analysis to AST/rule-based analysis, learned detectors, and LLM-based detection.
- Restore separate, compact paragraphs for DbDeo, SQLInspect, SQLCheck, and PL/SQL smell classification. Keep their original tool-by-tool order, then let the existing localisation-gap paragraph synthesise the comparison.
- Add a short distinction between multi-label file classification and multi-occurrence localisation immediately before the existing gap statement.

Do not restore the full 19-class taxonomy, prompt-engineering tutorial, promotional jOOQ adoption claims, CodeRabbit claims, the statement that only two SQL tools exist, or numerical cross-study rankings. Use “coverage has not been established” rather than “incapable.”

Completion check: Background gains 585--715 words; its final paragraph still identifies the output-unit gap; every restored tool description has a citation and is used by the synthesis.

### Step 4: Restore procedural depth in Study Design (+950 words)

Primary sources and sub-budgets:

| Topic | Legacy source | Net addition |
|---|---|---:|
| Repository search and filtering rationale | `paper/chapters/03_dataset_creation.tex:11-17,21-27` | 150 |
| Size stratification and operational-scope decisions | `paper/chapters/03_dataset_creation.tex:89-133` | 175 |
| Annotation records, iterative codebook, and washout procedure | `paper/chapters/03_dataset_creation.tex:137-160` | 225 |
| Project-disjoint split roles and label-informed seed search | `paper/chapters/03_dataset_creation.tex:203-239` | 150 |
| Model/prompt selection and prompt construction | `paper/chapters/04_evaluation.tex:5-21,33-60` | 150 |
| Multi-occurrence matching and metric interpretation | `paper/chapters/04_evaluation.tex:155-191` | 100 |

Actions:

- Preserve the empirical-pipeline order already used in the article; expand within existing subsections rather than adding new top-level structure.
- Restore why generated classes were required, why manifest queries were used, how irrelevant files and duplicate repositories were handled, and what the search cannot cover.
- Restore the sampling rationale without calling the sample statistically representative or adding an uncited Head--Tail Breaks label.
- Explain the annotation record, iterative guideline revision, washout sampling, and exact-span repeatability using the thesis's paragraph sequence. Retain the distinction between repeatability and correctness.
- Explain the separate roles of training, validation, and test projects, whole-project assignment, support filtering, and the label-informed seed search. Keep equations and the full support table online.
- Restore the two-prompt division, supplied key context, line numbering, and decision-rule refinement. Do not reproduce full prompts.
- Expand the matching explanation only enough to make multi-label, multi-occurrence evaluation, inclusive spans, one-to-one assignment, and the three aggregate types readable without the supplement.

Do not restore implementation architecture, CLI options, complete prompts, the complete 19-class codebook, the full split table, obsolete model parameters, or unpreserved validation-run details. The Step 13 disclosure about missing exact validation outputs remains unchanged.

Completion check: Study Design gains 855--1,045 words; each addition lets a reader reconstruct or evaluate a decision; no detail is restored solely because it existed in the thesis.

### Step 5: Restore concrete result detail (+400 words)

Primary sources:

- `paper/chapters/08_analysis.tex:30-81`
- `paper/chapters/07_results.tex:370-400,408-444`

Actions:

- After the class-error summary table, restore a compact class-by-class factual narrative for the most informative disagreements. Preserve the original order of the seven classes but combine classes whose only contribution would repeat a table cell.
- Describe the observed code forms and detector/reference judgments, not inferred model reasoning. Identify all revised-reference judgments as detector-informed.
- Restore flags-per-repository and flags-per-flagged-repository context where it helps interpret RQ2.
- Restore the lower-frequency RQ3 manifestation categories in prose only when they complete the distribution rather than restate every row.
- Verify all retained counts and percentages against the current tables and frozen analysis, not the old thesis text.

Do not restore classification-only results, the old RQ numbering, the IoU grid already assigned online, the large per-class tables, or unqualified occurrence/prevalence language.

Completion check: Results gains 360--440 words; every sentence reports an observation, comparison, or direct answer; no discussion-level causal explanation appears in Results.

### Step 6: Restore the Discussion's analytical chain (+600 words)

Primary sources:

- configuration-comparison paragraphs from `paper/chapters/07_results.tex:61,85-87,91,115-119,123,147-157`
- `paper/chapters/08_analysis.tex:83-90`
- selected future-work sentences from `paper/chapters/08_analysis.tex:187,193,197,199`

Actions:

- Add a compact interpretation of the configuration results: the selected Zero-Shot configuration was simpler and faster in the reported comparison, while the alternative prompting results came from single runs whose exact outputs are unavailable. Preserve the original comparison sequence but remove explanations attributed to model architecture, reasoning behaviour, or overfitting.
- Expand the comparison with DbDeo, SQLInspect, SQLCheck, and PL/SQL classification only around representation, supported classes, output unit, and the requirements of a fair same-task baseline. Refer back to Background instead of redescribing each tool.
- Connect the observed class-specific disagreement mechanisms to the article's principal measurement point: pooled agreement does not transfer uniformly across classes.
- Restore bounded follow-up directions for broader taxonomies, smaller or self-hosted models, other query builders, and further analysis of the preserved flags. State them as experiments to run, not improvements that will occur.

Do not restore the work-process reflection, schedule narrative, model-release commentary, direct cross-study F1 ranking, claims about developer benefit, or unsupported claims that RAG, preprocessing, or a particular model will improve accuracy or cost.

Completion check: Discussion gains 540--660 words; each interpretive paragraph begins from a current result or a cited difference in study design; none repeats the Results section paragraph for paragraph.

### Step 7: Add only the missing validity detail (+150 words)

Primary sources:

- `paper/chapters/03_dataset_creation.tex:38-54`
- `paper/chapters/08_analysis.tex:181-183`

Actions:

- Expand external validity with the concrete coverage consequences of dependency-manifest search, the GitHub Code Search result cap, and omitted project types.
- If space remains, distinguish model version, backend routing, caching, and unavailable request metadata as separate replay concerns, but keep the current evidence-specific qualification that only GLM-5 has a preserved fixed backend.
- Add consequences, not another description of the method.

Do not claim that the omitted population is small, that the chosen mining approach was best, or that gateway routing affected runs for which routing evidence is unavailable.

Completion check: Threats gains 135--165 words and adds a limitation not already stated at equivalent detail.

### Step 8: Reconcile the restored prose

Actions:

- Read the article linearly from Introduction through Conclusion, comparing every added paragraph with the paragraphs immediately before and after it.
- Remove duplicate definitions, table narration, thesis-navigation language, and conclusions stated before their evidence.
- Merge abrupt one-sentence bridge paragraphs into adjacent source-led paragraphs where possible.
- Run terminology, number, citation, label, and RQ wording searches used in Step 13.
- Apply a restrained language pass: remove generic throat-clearing, stacked signposting, false causal connectors, inflated novelty, repetitive three-item summaries, and claims about what an LLM “understands.” Preserve the original author's viable wording instead of synonymising it.
- Keep the current Abstract and Conclusion unchanged unless a restored passage exposes a factual inconsistency. Word-count pressure alone is not a reason to lengthen them.

Completion check: at least 85% of the net addition is traceable to the legacy source ledger; no paragraph exists only to satisfy the numerical target; the title, abstract, RQs, direct answers, discussion, and conclusion remain claim-consistent.

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

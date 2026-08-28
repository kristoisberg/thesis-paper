# ESE word restoration Step 1: baseline and reuse ledger

Date: 2026-08-28

Status: completed. This step changed review metadata only. No manuscript, supplement, bibliography, analysis, or figure file changed.

## Baseline identity

- Last manuscript commit: `098d195c58c72705ff5263af466f92561afa032f` (`complete submission-readiness pass and disclose evidence limits`).
- Execution-plan commit: `e6a3ac70a9430361281b7797c55acb5f5fff5c93` (`add ESE 3,000-word restoration plan`). The only change between these commits is the plan in `.review/`.
- Branch at measurement: `main`, aligned with `origin/main`.
- Manuscript diff at the start of Step 1: empty.
- Main PDF SHA-256 after a clean build: `5be6fcbcde06b316ad84d4904cfba3fa396d14b620f3f96ecbe4cda27fc733bc`.
- Supplement PDF SHA-256 after a clean build: `5d2f661787c359e8f03244ea5eb1231c5aea2c69fa98a51735c8b9700cd9f493`.

The commit boundary is the pre-expansion snapshot. A separate copy of the manuscript would duplicate Git's job. Before each later step, the step report must record the starting commit or diff, the section count, and the manuscript files already modified by earlier restoration steps.

## Reproduced counts and build state

The baseline was rebuilt with `make clean && make paper`. TeXCount ran in the same TeX Live container used by the Makefile, using `texcount -inc -sum main.tex`.

| Measure | Baseline |
|---|---:|
| TeXCount total | 6,985 |
| Words in text | 6,478 |
| Words in headings | 211 |
| Words outside text, chiefly captions | 293 |
| PDF-extracted words, including references | 9,332 |
| Supplement PDF-extracted words | 1,954 |
| Main PDF pages | 25 |
| Supplement pages | 7 |
| Main-paper floats | 6 |

The per-section planning counts are the included-file values from the canonical `texcount -inc -sum main.tex` run. Counting Study Design alone produces 2,299 because TeXCount parses 12 words differently without the inclusion context. Later deltas must use the included-file values.

| Section | Included-file TeXCount | Planned net addition | Target |
|---|---:|---:|---:|
| Introduction | 384 | 68 | 452 |
| Background and Related Work | 789 | 599 | 1,388 |
| Study Design | 2,287 | 1,388 | 3,675 |
| Results | 1,224 | 550 | 1,774 |
| Discussion | 777 | 340 | 1,117 |
| Threats to Validity | 926 | 0 | 926 |
| Conclusion | 163 | 0 | 163 |
| **Current execution budget** |  | **2,945** |  |

The paragraph audit moved 490 words into Study Design and removed the planned Threats expansion. The current Threats section covers manifest-search coverage, the GitHub result cap, single-run uncertainty, bounded gateway/provider change, missing metadata, and replay limits. It does not assert a caching effect because the evidence does not show that caching affected the single-pass runs. The audit also reduced Discussion because its tool comparison already follows Background. This allocation gives the largest share to procedural material whose original sentence structure remains usable.

The clean final logs contain zero LaTeX errors, undefined citations, undefined references, overfull boxes, or BibTeX warnings. The main log contains 19 underfull-box notices and the supplement contains one. These are the harmless table-cell, URL, and page-breaking notices accepted in Step 13. Both frozen analysis scripts also reran successfully. They reproduced the 536 predictions, 523 references, 460/76/63 primary totals, IoU grid, 10,000-replicate bootstrap ranges, 15,931 corpus flags, 601 flagged repositories, all class totals, and the 59.1% overall top-decile concentration.

## Protected article identity

The restoration may explain the study in more detail. It may not alter the following identity.

### Title

*LLM-Based SQL Antipattern Detection in jOOQ Code: An Occurrence-Level Evaluation and Repository Study*

### Central claim

Project-disjoint evaluation measures agreement for the class-labelled span outputs later counted as corpus flags. Per-class held-out agreement bounds how those flags can be interpreted. The corpus findings describe detector output; true antipattern prevalence and risk associated with particular APIs remain unmeasured.

### Research questions

1. **RQ1:** What occurrence-level agreement does one run of the selected LLM-based detector achieve against the original single-annotator reference spans for seven operationalised SQL antipatterns in the 20-repository, project-disjoint test partition?
2. **RQ2:** How frequently does the selected detector flag each of the seven SQL antipatterns in the 602-repository corpus, and how are those flags distributed across repositories?
3. **RQ3:** Which recurring source-fragment patterns are most frequent among detector flags for Implicit Columns and Poor Man's Search Engine in the 602-repository corpus?

The same wording must remain in the Introduction and Results headings. The short answers may gain explanatory sentences, but their units and conclusions may not change.

### Contribution boundary

- A single-annotator reference dataset contains 1,562 class-labelled spans across 19 operationalised classes from 61 sampled repositories. Seven classes were retained for detector analysis.
- The held-out contribution is one project-disjoint detector run evaluated through class-labelled, one-to-one span matching. The study does not measure repeated-run stability.
- The repository contribution is a bounded description of detector flags across the identified 602-repository corpus, including concentration and source-fragment patterns for two classes. It is not a prevalence or API-risk study.

## Fixed evidence ledger

Current manuscript values and the frozen analysis take precedence over legacy prose.

| Evidence area | Fixed values or boundary |
|---|---|
| Repository funnel | Search date 10 January 2026; 3,829 search results; 802 repositories with generated classes; 645 after the non-generated Java-file filter; 603 in the preliminary sampling corpus; 602 in the final analysis corpus. |
| Sampling and annotation | Size groups 467/100/36 with breakpoints 31 and 94 files; sampled groups 47/10/4; seed 123456; 61 repositories; 1,562 spans across 19 classes; 1,436 spans in the seven retained classes. |
| Repeat annotation | 128 files after a 30-day washout; 158 original events, 149 repeated events, and 142 exact matches; precision 0.953, recall 0.899, F1 0.925. These measure temporal repeatability, not correctness. |
| Partitioning | Whole-project allocation of 21/20/20 projects; support rule of at least 25 occurrences in at least three projects; seven retained classes; one million seeds evaluated; selected seed 767573 with score 0.52. Both class retention and seed selection were label-informed. |
| Configuration comparison | The displayed validation table is an originally reported, one-run comparison. Its exact run outputs, reported file count, costs, and runtimes cannot be reconstructed from the surviving notebooks. Do not add precision beyond the table or infer run-to-run differences. |
| Held-out execution | 20 test repositories; 502 relevant files; one Claude Opus 4.5 Zero-Shot run; cost USD 14.34; runtime 386 seconds; 536 predictions; 523 original reference spans. Exact prompt identity and the executed detector revision are unavailable. |
| Primary matching | IoU 0.50; one-to-one maximum-cardinality matching; 460 TP, 76 FP, 63 FN; micro P/R/F1 0.858/0.880/0.869; macro P/R/F1 0.797/0.813/0.793; reference-support-weighted P/R/F1 0.885/0.880/0.877. |
| Per-class agreement | F1 spans 0.481 for Fear of the Unknown to 0.974 for 31 Flavors. All per-class counts and metrics in `tab:toolDetections` are fixed. |
| Detector-informed revision | 563 reference spans; 512 TP, 24 FP, 51 FN; micro P/R/F1 0.955/0.909/0.932. This is an optimistic sensitivity analysis, not corrected ground truth. Row-level revised spans were not archived. |
| Robustness | Micro F1 0.863--0.873 across IoU 0.25 through exact matching; 10,000 project-cluster bootstrap replicates; micro P 0.799--0.933, R 0.817--0.913, and F1 0.819--0.913. These are project-composition sensitivity ranges, not population confidence intervals. |
| Corpus execution | 602 repositories; 17,450 relevant files; 15,931 positive flags; 601 repositories with at least one retained-class flag; 59.1% of all flags in the highest-count 10% of flagged repositories. No independently labelled corpus frame or complete negative-file frame exists. |
| Leading corpus classes | Implicit Columns 7,289 flags in 535 repositories; ID Required 3,597 flags in 523 repositories; together 10,886 flags, or 68.3% of the corpus output. All class rows in `tab:corpusFlags` are fixed. |
| Source-fragment coding | Implicit Columns leading pair 5,227/7,289, or 71.7%; recurring categories cover 94.1%. Poor Man's Search Engine `like(` 273/583, or 46.8%; leading four categories 517/583, or 88.7%; recurring categories cover 93.7%. Categories are precedence-ordered fragment matches without resolved call targets or API-use denominators. |
| Reproducibility | Study artefacts: `d9b35e3`; released detector: `cf82fe5`; article analysis: `96dc91b`. Missing items include source-repository revisions, executed detector revision, raw API responses, complete request and provider metadata, retry histories, and the full corpus frame. |

## Protected float inventory

The main paper contains one figure and six labelled tables. Restoration prose may introduce and interpret them, but it may not add, replace, or move their detailed counterparts back from Online Resource 1.

| Label | Role |
|---|---|
| `tab:evaluatedAntipatterns` | Operational definitions for the seven evaluated classes. |
| `fig:dataFunnel` | Repository-selection boundaries. |
| `tab:configurationSelection` | Originally reported validation configuration comparison. |
| `tab:toolDetections` | Held-out per-class and pooled occurrence agreement. |
| `tab:detectionErrors` | Compact index of observed disagreement mechanisms. |
| `tab:corpusFlags` | Corpus flag totals, repository coverage, and concentration. |
| `tab:apiManifestations` | Post hoc source-fragment categories for two flag classes. |

`tab:evaluatedAntipatterns` is a `longtable` that TeXCount does not classify as a float, which explains why TeXCount reports six floats although seven labelled visual elements appear above.

## Online-resource boundary

Online Resource 1 remains the home of the following material:

- the resource index and preservation warnings;
- immutable snapshots, preserved outputs, model dates, settings, retries, dependencies, and script invocations;
- the paired SQL and jOOQ source-representation listing;
- the detailed detection-representation and output-unit comparison;
- class occurrence and project support for the project-disjoint split;
- the complete IoU-threshold grid;
- exact search terms and the omitted-project list;
- the full 19-class catalogue, codebook, exclusions, and decision trees;
- complete prompt templates, localisation rules, and ordered source-pattern rules.

Full prompt listings, the full taxonomy, detailed model and prompt tables, classification-only results, implementation architecture, CLI documentation, matching diagnostics, matrices, and co-flagging analyses remain outside the main paper. Restoration prose may summarise why these materials matter, but may not reproduce them.

## Paragraph-level reuse ledger

Each row defines one candidate restored paragraph. The destination names an existing subsection or a stable neighbouring paragraph so the ledger remains usable after line numbers shift. The budget is a net addition after deleting duplicated or invalid legacy material.

| ID | Destination in current article | Legacy source | Paragraph job | Budget | Required factual adaptation |
|---|---|---|---|---:|---|
| I01 | Introduction, after the opening paragraph | `paper/chapters/01_introduction.tex:5-6`; `paper/chapters/02_background.tex:25-27` | Add attributed evidence about persistence and remediation priority. | 68 | Completed in Step 2. Omitted duplicated prevalence and impact figures, developer-education claims, tooling causality, and a redundant representation bridge; preserved the current move into jOOQ. |
| B01 | Background, after the opening definition | `paper/chapters/02_background.tex:5,7` | Distinguish antipatterns from code smells. | 78 | Completed in Step 3. Kept the cited definitions and removed unused history. |
| B02 | Background, before the operational-definition table | `paper/chapters/02_background.tex:11-13` | Explain the Implicit Columns maintenance mechanism. | 82 | Completed in Step 3. Kept the existing 27%/29% result once and omitted the unevaluated `INSERT` form. |
| B03 | Background, after the opening jOOQ paragraph | `paper/chapters/02_background.tex:85` | Explain DSL, code-generation, generated-schema, and JDBC roles. | 92 | Completed in Step 3. Omitted adoption, ORM-superiority, GitHub-star, customer, and IDE-support claims, and left the runtime consequence to the existing synthesis paragraph. |
| B04 | Background, expand the first detection-approaches paragraph | `paper/chapters/02_background.tex:104-112` | Restore the metric-, rule-, and learned-analysis progression. | 228 | Completed in Step 3. Removed product inventories, extended smell examples, universal rigidity claims, and uncited adoption statements. |
| B05 | Background, expand the existing SQL-detector comparison | `paper/chapters/02_background.tex:135-145` | Compare representations, analysis methods, class scope, and output units. | 119 | Completed in Step 3. Removed "only two," "incapable," database-catalogue inventory, and cross-tool rankings; retained the existing gap synthesis. |
| S01 | Study Design, repository mining after the dated-search paragraph | `paper/chapters/03_dataset_creation.tex:11-15` | Explain the generated-class requirement and manifest-search rationale. | 254 | Completed in Step 4. Preserved target-population limits and stated manifest search as a rationale, not measured saturation. |
| S02 | Study Design, repository mining before the funnel figure | `paper/chapters/03_dataset_creation.tex:21-27` | Explain content filtering and human-reviewed duplicate removal. | 63 | Completed in Step 4. Omitted speculation, model praise, and named duplicate anecdotes; preserved 645/603/602. |
| S03 | Study Design, sampling around the current count paragraph | `paper/chapters/03_dataset_creation.tex:64-71,89-113` | Define relevant files and explain the skewed size distribution and stratum sampling. | 227 | Completed in Step 4. Omitted representativeness claims, the method name, equations, and corrected-distribution detours. |
| S04 | Study Design, operational scope after the current codebook paragraph | `paper/chapters/03_dataset_creation.tex:117-131` | Give at most two concrete examples of evidence-based inclusion or exclusion decisions. | 60 | Completed in Step 4 with Index Shotgun and Implicit Columns examples; kept the full codebook online. |
| S05 | Study Design, sampling and annotation after the one-annotator paragraph | `paper/chapters/03_dataset_creation.tex:137-160` | Explain record fields, iterative rule revision, re-review, and washout comparison. | 214 | Completed in Step 4. Preserved the repeatability-versus-correctness boundary and fixed counts. |
| S06 | Study Design, project-disjoint partitioning after its opening paragraph | `paper/chapters/03_dataset_creation.tex:203-217,235-239` | Explain split roles, whole-project assignment, support filtering, and label-informed selection. | 135 | Completed in Step 4. Omitted equations, the support table, the rejected-seed claim, and sample-size history. |
| S07 | Study Design, detector configuration before the current model paragraph | `paper/chapters/04_evaluation.tex:5-21` | Explain the model-inclusion criteria used at the time. | 156 | Completed in Step 4. Retained diversity, stable-identifier, and structured-output preferences; omitted rankings and guarantees. |
| S08 | Study Design, expand prompt construction | `paper/chapters/04_evaluation.tex:33-58` | Explain one-request scope, training-set development, query/schema prompts, key context, preprocessing, and explicit rules. | 279 | Completed in Step 4. Omitted claimed metric improvements, hallucination causes, and full prompts; identified synthetic examples. |
| R01 | Results RQ1, after `tab:detectionErrors` | `paper/chapters/08_analysis.tex:31-35,38-40,45-49,52-58,61,71,74-81` | Add concrete code forms and examples absent from the compact table. | 368 | Completed in Step 5. Preserved the class order and concrete source forms; identified reference changes as detector-informed; removed inferred reasoning, prompt causality, and the old figure. |
| R02 | Results RQ2, after `tab:corpusFlags` | `paper/chapters/07_results.tex:390-400` | Add flags-per-repository and flags-per-flagged-repository context. | 87 | Completed in Step 5 from the SHA-256-verified frozen CSV. Omitted corpus cost, runtime, and old RQ numbering; used flags throughout. |
| R03 | Results RQ3, after `tab:apiManifestations` | `paper/chapters/07_results.tex:408-410,442-444` | Add selected lower-frequency source-fragment categories. | 95 | Completed in Step 5 with current fragment labels and precedence; made no resolved-call or API-risk claim. |
| D01 | Discussion, before "Relation to existing detectors" | `paper/chapters/07_results.tex:61,87,91,115,123,147,155-157` | Interpret the single-run configuration trade-off. | 153 | Completed in Step 6. Preserved the reported Opus comparison sequence, cited the model and prompt designs, and retained the missing-output and single-run limits. |
| D02 | Discussion, end of the implications subsection | `paper/chapters/08_analysis.tex:187,193,197,199` | Define bounded follow-up studies. | 187 | Completed in Step 6. Framed broader taxonomies, smaller or self-hosted models, other query builders, and preserved-flag analysis as experiments with specified measurements and no predicted gain. |
|  |  |  | **Current execution budget** | **2,945** |  |

## Fixed exclusions

The following sources are not candidates for later restoration:

- `paper/chapters/01_introduction.tex:1-4,7-68`: popularity and developer-education claims, old objectives, five RQs, broad DSR and novelty framing, AI/reproducibility claims, and thesis outline;
- `paper/chapters/02_background.tex:31-82,116-130`: full taxonomy and prompt tutorial;
- complete prompt listings and configuration tables from `paper/chapters/04_evaluation.tex` and the appendices;
- `paper/chapters/05_development.tex`: implementation architecture, CLI behaviour, and development detail;
- `paper/chapters/07_results.tex:288-368`: classification-only evaluation;
- `paper/chapters/08_analysis.tex:7-24,89-117,129-157,179,189-195`: unsupported model-behaviour explanations, cross-study ranking, work reflection, schedule and collaboration narrative, practical utility, speculative RAG claims, and interface features;
- `paper/chapters/03_dataset_creation.tex:38-54` and `paper/chapters/08_analysis.tex:181-183`: mining and reliability limitations already covered at equivalent detail in the current Threats to Validity section;
- the old five-RQ answer structure and all thesis-navigation prose;
- any number or setting contradicted by the fixed evidence ledger;
- material already assigned to Online Resource 1.

## Step 1 completion check

- Baseline reproduced: **yes**. TeXCount 6,985; PDF-extracted count 9,332; main PDF 25 pages.
- Clean build verified: **yes**. Both PDFs built; final logs have no errors, unresolved references or citations, overfull boxes, or BibTeX warnings.
- Article identity frozen: **yes**. Title, central claim, RQs, contribution boundary, numerical evidence, floats, and online-resource boundary are recorded above.
- Paragraph-level source ledger complete: **yes**. Nineteen candidate paragraph units have legacy sources, stable destinations, argumentative jobs, budgets, and factual adaptations. They totalled 3,000 words when Step 1 was completed; the executed rows and current budget are recorded above.
- Manuscript changed: **no**.

Step 2 completed row I01 at 68 words. Its unsupported 112-word remainder moved to S01 rather than being replaced with generated filler; the ledger still totalled 3,000 words at that point.

Step 3 completed rows B01--B05 at a combined 599 words, 61 below their provisional allocation and within the step's tolerance. The difference was not reassigned because the resulting 2,939-word execution budget remains inside the overall target range.

Step 4 completed rows S01--S08 at a combined 1,388 words. Its 164-word remainder moved to R01, whose legacy source contains concrete class-error examples; the execution budget remains 2,939 words.

Step 5 completed rows R01--R03 at a combined 550 words, 14 below their provisional allocation and within the step tolerance. The resulting execution budget is 2,925 words, still inside the overall target range.

Step 6 completed rows D01--D02 at a combined 340 words, 20 above their provisional allocation and within the step tolerance. The resulting execution budget is 2,945 words. The main PDF reached 12,352 extracted words and 31 pages, so no further length restoration is planned.

Step 7 audited every restored consequence against the five Threats to Validity categories. The section remained unchanged at 926 words; its SHA-256 remained `67b021d1d1f30133924d4b6f21828c63083a25810bdf1ff501e225080b4c48c7`. The stale metadata reference to an existing caching limitation was corrected without adding an unsupported cache-effect claim to the manuscript.

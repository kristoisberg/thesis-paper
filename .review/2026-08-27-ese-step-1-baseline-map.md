# ESE Step 1 baseline and routing map

Date: 2026-08-27

Status: complete

Scope: read-only audit of `paper/`. No manuscript source was changed.

## Completion assessment

Step 1 is complete. This record provides:

- the current compiled baseline;
- the current section and page order;
- a destination for every source section and paragraph group;
- a destination for all 33 main-paper floats;
- a destination for all 20 appendices and their 73 floats;
- the structural lessons retained from the earlier paper attempt;
- the cross-reference and layout risks that later steps must preserve or repair.

The four routing statuses are:

- **KEEP MAIN**: move the existing paragraph or float block intact.
- **CONDENSE LATER**: move it intact during restructuring, then shorten it in a later step.
- **MOVE ONLINE**: preserve it in an Online Resource or the replication package.
- **REMOVE**: omit it because it is thesis-specific, redundant, or unsupported by the study design.

## Reproducible baseline

| Item | Recorded state |
|---|---|
| Git commit | `3e2bd14831173e6bb27461af73a5db0ce302390b` |
| Compiled manuscript | `paper/main.pdf` |
| PDF hash | `57f51c5ab6c0199ebb81832685f2b7875713d442c690f0b2ebe1acbb71cf373c` |
| PDF size | 3,003,793 bytes |
| PDF format | 147 A4 pages, PDF 1.7, untagged |
| Pages 1-68 | 27,581 extracted words, including front matter and declarations |
| References, pages 69-74 | 3,010 extracted words |
| Appendices, pages 75-147 | 30,621 extracted words |
| Full PDF | 61,212 extracted words |
| Chapter source files | 9 |
| Appendix source files | 20 |
| Main-paper figures | 13 numbered figures, consisting of 10 figure environments and 3 listing-based figures |
| Main-paper tables | 20 |
| Appendix figures | 35 numbered figures |
| Appendix tables | 53 |
| Bibliography | 113 resolved entries |
| Undefined citations or references | 0 |
| Multiply defined labels | 0 |

The PDF metadata has blank title, subject, keywords, and author fields. This is a later submission-readiness task.

## Current page outline

| Current content | PDF pages |
|---|---:|
| Title and abstract | 1 |
| 1 Introduction | 2-4 |
| 2 Background and Related Work | 5-13 |
| 3 Dataset Creation | 14-24 |
| 4 Evaluation of Prompting Strategies | 25-32 |
| 5 Development of Antipattern Detector | 33-39 |
| 6 Project Analysis | 40-41 |
| 7 Results | 42-54 |
| 8 Analysis | 54-67 |
| 9 Summary | 68 |
| Statements and Declarations | 68-69 |
| References | 69-74 |
| Appendices 2-21 | 75-147 |

The appendices occupy 73 pages, exactly half of the compiled PDF.

## Existing build warnings

The paper builds without LaTeX errors or unresolved references. The current log records:

| Warning | Count |
|---|---:|
| LaTeX warnings | 13 |
| Package warnings | 2 |
| Overfull horizontal boxes | 323 |
| Underfull horizontal boxes | 43 |
| Overfull vertical boxes | 1 |
| Underfull vertical boxes | 34 |
| Floats too large for a page | 7 |
| Float placement changes from `h` to `ht` | 5 |

The largest visible problems are wide tables on pages 23-24, 31, 43-47, 52-54, and 59. Figure 10 on page 36 exceeds the page height. Several appendix decision trees also exceed the page height. These problems largely disappear when the routed online material leaves the main PDF.

## Structural comparator

`.review/paper-old.pdf` was re-added after the initial audit and has now been inspected directly. Its extracted text exactly matches the cached copy used to prepare the original structural comparison.

Recorded earlier baseline:

| Item | Earlier paper attempt |
|---|---:|
| Pages | 30 A4 pages |
| Extracted words | 12,017 |
| Main figures | 1 |
| Main tables | 5 |
| PDF size | 454,597 bytes |
| PDF hash | `bebd6a144a8503eef37c1491389781169ded2c66165fca3c7eec3bf98202eacd` |

Its useful structural sequence was:

1. Introduction
2. Background and Related Work
3. Study Design
4. Results organised by RQ
5. Discussion
6. Threats to Validity
7. Conclusion
8. Declarations and references

The current plan reuses this section sequence and the RQ-oriented result grouping. It does not reuse prose, authorship, or claims from the earlier attempt. The earlier attempt included a standalone co-occurrence RQ. The current plan demotes that analysis unless it is recomputed with suitable exposure controls.

## Source routing map

### Front matter and declarations

| Current source block | Status | Destination |
|---|---|---|
| `main.tex:67-90`, title, abstract, and keywords | **CONDENSE LATER** | Final title, abstract, and keywords. Write the abstract after the RQ answers stabilise. |
| `main.tex:94-118`, Statements and Declarations | **KEEP MAIN** | Statements and Declarations. Complete the placeholders in Step 12. |
| `main.tex:123-124`, thesis appendix inclusion | **REMOVE** | Replace with citations to Online Resources. |

### Introduction

| Current source block | Status | Destination |
|---|---|---|
| `01_introduction.tex:1-8`, adoption, recurring mistakes, prevalence, persistence, and missing jOOQ support | **KEEP MAIN** | Introduction, problem and practical setting. Preserve the four paragraph blocks. |
| `01_introduction.tex:10-12`, tool-development objective | **CONDENSE LATER** | Introduction, evidence gap and central claim. |
| `01_introduction.tex:14`, contextual and dynamic jOOQ difficulty | **KEEP MAIN** | Introduction, why jOOQ complicates extraction and localisation. |
| `01_introduction.tex:16`, prevalence and API objective | **CONDENSE LATER** | Introduction, empirical scope. Remove unevaluated developer-benefit claims. |
| `01_introduction.tex:18-26`, five existing RQs | **CONDENSE LATER** | Introduction, three revised RQs. Model and prompt comparison become instrument configuration. |
| `01_introduction.tex:28-30`, Design Science framing | **REMOVE** | No destination in the empirical measurement framing. |
| `01_introduction.tex:32-37`, model, prompt, dataset, corpus, and localisation contributions | **CONDENSE LATER** | Introduction, contributions ordered as dataset, occurrence validation, and corpus study. |
| `01_introduction.tex:38-48`, detailed AI-use inventory | **CONDENSE LATER** | Study Design, AI-use disclosure. Preserve the distinctions among research, coding, drafting, and editing. |
| `01_introduction.tex:50-52`, Jupyter and open artefacts | **KEEP MAIN** | Study Design, reproducibility, and the availability declarations. |
| `01_introduction.tex:54-68`, thesis outline | **REMOVE** | No journal-paper destination. |

### Background and related work

| Current source block | Status | Destination |
|---|---|---|
| `02_background.tex:1`, thesis chapter preview | **REMOVE** | Replace later with a one-sentence section claim. |
| `02_background.tex:3-29`, definition, history, effects, example, and prior prevalence | **CONDENSE LATER** | Background, SQL antipatterns and units of analysis. Preserve the current paragraph order during relocation. |
| `02_background.tex:9`, scope limited to Karwin | **KEEP MAIN** | Study Design, operational definitions. |
| `02_background.tex:31-82`, full four-category catalogue | **MOVE ONLINE** | Online Resource, full taxonomy. Extract the seven evaluated definitions into the main operational-definition table. |
| `02_background.tex:83-101`, jOOQ description and dynamic DSL example | **KEEP MAIN** | Background, jOOQ and dynamic query representation. |
| `02_background.tex:102-115`, static, rule-based, ML, and LLM detection | **CONDENSE LATER** | Background, static, API/AST, and LLM approaches. |
| `02_background.tex:116-130`, prompt-engineering tutorial | **MOVE ONLINE** | Online Resource, detector-configuration background. Retain only definitions needed to understand configuration selection. |
| `02_background.tex:131-145`, existing SQL detectors and the jOOQ extraction gap | **KEEP MAIN** | Background, related work and measurement gap. |

### Repository mining and reference dataset

| Current source block | Status | Destination |
|---|---|---|
| `03_dataset_creation.tex:1`, thesis chapter preview | **REMOVE** | Replace later with the Study Design overview. |
| `03_dataset_creation.tex:3-18`, repository criteria, generated-schema rationale, search method, and dated retrieval | **KEEP MAIN** | Study Design, repository mining and target population. |
| `03_dataset_creation.tex:19`, observation that 21 percent of projects commit generated classes | **REMOVE** | Tangential observation. |
| `03_dataset_creation.tex:21-35`, filtering, duplicate removal, final corpus, and funnel | **KEEP MAIN** | Study Design, repository mining and target population. |
| `03_dataset_creation.tex:36-47`, GitHub search limitations | **CONDENSE LATER** | Threats to Validity, external validity. |
| `03_dataset_creation.tex:48-55`, GH Archive, RepoReaper, and GHTorrent comparison | **MOVE ONLINE** | Online Resource, repository-search alternatives. |
| `03_dataset_creation.tex:56-61`, need for annotated data | **KEEP MAIN** | Study Design, reference annotations. Rename "ground truth" later. |
| `03_dataset_creation.tex:62-90`, relevant-file definition, sampling frame, and final 61-project sample | **KEEP MAIN** | Study Design, sampling. |
| `03_dataset_creation.tex:91-114`, Head-Tail Breaks derivation | **MOVE ONLINE** | Online Resource, sampling procedure. Keep the breakpoints and class counts in the paper. |
| `03_dataset_creation.tex:115-134`, antipattern inclusion and exclusion | **CONDENSE LATER** | Study Design, seven operational definitions. Move the detailed exclusions online. |
| `03_dataset_creation.tex:135-149`, annotation procedure and fields | **KEEP MAIN** | Study Design, reference annotation. |
| `03_dataset_creation.tex:150-155`, codebook development | **KEEP MAIN** | Study Design, annotation and reliability. Move the decision trees online. |
| `03_dataset_creation.tex:156-161`, reannotation design | **KEEP MAIN** | Study Design, annotation and reliability. |
| `03_dataset_creation.tex:162-197`, Kappa derivation and full calculation | **MOVE ONLINE** | Online Resource, annotation-reliability calculation. Retain the result and limitation in the paper. |
| `03_dataset_creation.tex:198-238`, annotation totals and nineteen-class sample table | **CONDENSE LATER** | Study Design, reference dataset profile. Move the full nineteen-class table online. |
| `03_dataset_creation.tex:239-254`, project-disjoint split roles, data-dependent seed search, and eligibility filtering | **KEEP MAIN** | Study Design, project-disjoint partitioning. |
| `03_dataset_creation.tex:255-276`, split optimisation equations | **MOVE ONLINE** | Online Resource, split optimisation. |
| `03_dataset_creation.tex:277-301`, seven-class split table and explanation | **KEEP MAIN** | Study Design, project-disjoint partitioning. |
| `03_dataset_creation.tex:302-309`, dataset-use diagram | **CONDENSE LATER** | Study Design, one combined study-pipeline figure. |

### Detector configuration and evaluation

| Current source block | Status | Destination |
|---|---|---|
| `04_evaluation.tex:1`, chapter preview | **REMOVE** | No standalone prompting chapter. |
| `04_evaluation.tex:3-22`, model criteria and selected candidates | **CONDENSE LATER** | Study Design, detector configuration. |
| `04_evaluation.tex:23-30`, omitted models | **MOVE ONLINE** | Online Resource, candidate-model selection. |
| `04_evaluation.tex:31-117`, prompt development, preprocessing, context, and localisation rules | **CONDENSE LATER** | Study Design, detector configuration. Move the iteration history and full prompts online. |
| `04_evaluation.tex:118-154`, validation execution and provider parameters | **KEEP MAIN** | Study Design, detector configuration and execution. |
| `04_evaluation.tex:155-187`, event localisation, IoU, one-to-one matching, precision, recall, and F1 | **KEEP MAIN** | Study Design, localisation matching and evaluation measures. |
| `04_evaluation.tex:188-191`, detailed cost and runtime collection | **MOVE ONLINE** | Online Resource, configuration experiment execution. |
| `04_evaluation.tex:192-193`, old-RQ navigation | **REMOVE** | Superseded by the revised RQs. |
| `04_evaluation.tex:194-198`, qualitative inspection procedure | **KEEP MAIN** | Study Design, error analysis. |

### Detector implementation and corpus analysis

| Current source block | Status | Destination |
|---|---|---|
| `05_development.tex:1`, chapter preview | **REMOVE** | Tool construction is no longer a paper-level section. |
| `05_development.tex:3`, Codex-assisted implementation disclosure | **CONDENSE LATER** | Study Design, AI-use disclosure. |
| `05_development.tex:5-19`, architecture | **MOVE ONLINE** | Online Resource, detector implementation. |
| `05_development.tex:20-40`, workflow | **CONDENSE LATER** | Study Design, detector pipeline. Merge it with the study overview. |
| `05_development.tex:41-102`, result representation and example output | **MOVE ONLINE** | Online Resource, CLI output. |
| `05_development.tex:103-117`, implementation technologies | **REMOVE** | Tool repository documentation already covers this material. |
| `05_development.tex:118-125`, configuration interface | **MOVE ONLINE** | Online Resource, CLI configuration. |
| `05_development.tex:126-129`, held-out localisation protocol | **KEEP MAIN** | Study Design, held-out evaluation. |
| `05_development.tex:130-135`, classification-only comparison | **MOVE ONLINE** | Online Resource, classification-only sensitivity analysis. |
| `05_development.tex:136-139`, error inspection | **KEEP MAIN** | Study Design, error analysis. |
| `06_project_analysis.tex:1`, chapter preview | **REMOVE** | Replace later with a claim-first corpus-measures subsection. |
| `06_project_analysis.tex:3-14`, counts, project coverage, and concentration | **KEEP MAIN** | Study Design, corpus measures. |
| `06_project_analysis.tex:15-18`, jOOQ-statement proxy and cross-study rate | **REMOVE** | The proposed RQ2 does not use this incompatible rate. |
| `06_project_analysis.tex:19-52`, Jaccard, conditional probability, and Spearman methods | **MOVE ONLINE** | Online Resource, exploratory co-detection, after correction. |
| `06_project_analysis.tex:54-60`, API-pattern coding | **KEEP MAIN** | Study Design, API-manifestation coding. |
| `06_project_analysis.tex:62-66`, qualitative-analysis navigation | **REMOVE** | Later discussion paragraphs will cite results directly. |

### Results

| Current source block | Status | Destination |
|---|---|---|
| `07_results.tex:1`, five-RQ preview | **REMOVE** | Replace with a three-RQ results introduction. |
| `07_results.tex:3-54`, current RQ1 model comparison | **CONDENSE LATER** | Study Design, detector-configuration selection. |
| `07_results.tex:55-152`, current RQ2 prompt comparisons | **MOVE ONLINE** | Online Resource, prompt-configuration experiments. |
| `07_results.tex:153-158`, prompt-comparison summary and selected configuration | **KEEP MAIN** | Study Design, configuration outcome. |
| `07_results.tex:159-191`, held-out setup, original annotations, and per-class event counts | **KEEP MAIN** | Results, revised RQ1 occurrence localisation. |
| `07_results.tex:192-228`, aggregate tables framed as confusion matrices | **REMOVE** | Redundant with the per-class event counts and technically misnamed. |
| `07_results.tex:229-256`, primary per-class precision, recall, and F1 | **KEEP MAIN** | Results, revised RQ1 against the original reference annotations. |
| `07_results.tex:257-282`, corrected-label performance | **MOVE ONLINE** | Online Resource, optimistic corrected-label sensitivity analysis. |
| `07_results.tex:283-376`, classification-only evaluation | **MOVE ONLINE** | Online Resource, classification-only evaluation. |
| `07_results.tex:377-380`, held-out interpretation | **CONDENSE LATER** | Results, revised RQ1 direct answer. |
| `07_results.tex:381-412`, prevalence and project distribution | **KEEP MAIN** | Results, revised RQ2. Remove the per-100-jOOQ-statements column later. |
| `07_results.tex:413-422`, co-occurrence findings | **MOVE ONLINE** | Online Resource, exploratory co-detection. |
| `07_results.tex:423-490`, API manifestations | **KEEP MAIN** | Results, revised RQ3. Combine the two API tables later. |

### Discussion, threats, and conclusion

| Current source block | Status | Destination |
|---|---|---|
| `08_analysis.tex:1-6`, chapter and interpretation previews | **REMOVE** | Replace later with a Discussion claim tied to the central result. |
| `08_analysis.tex:7-15`, common and context-dependent class performance | **KEEP MAIN** | Discussion, what occurrence-level validation adds. |
| `08_analysis.tex:16-25`, prompt-strategy interpretation | **MOVE ONLINE** | Online Resource, configuration interpretation. |
| `08_analysis.tex:26-82`, seven class-specific error blocks | **CONDENSE LATER** | Results, revised RQ1 error mechanisms. Preserve the blocks during relocation, then combine recurrent mechanisms. |
| `08_analysis.tex:83-90`, directly related SQL detection comparisons | **CONDENSE LATER** | Discussion, relationship to existing approaches. |
| `08_analysis.tex:91-118`, cross-domain performance league table | **REMOVE** | The tasks and output granularities are incompatible. |
| `08_analysis.tex:119-126`, plain-SQL density comparison | **REMOVE** | The numerator and denominator do not match the present study. |
| `08_analysis.tex:127-136`, co-occurrence interpretation | **MOVE ONLINE** | Online Resource, exploratory co-detection interpretation. |
| `08_analysis.tex:137-144`, API-design implications | **KEEP MAIN** | Discussion, implications for hybrid detection and jOOQ guidance. |
| `08_analysis.tex:145-174`, work-process reflection | **REMOVE** | No journal-paper destination. |
| `08_analysis.tex:175-180`, single annotator and corrected-label bias | **KEEP MAIN** | Threats, reliability and construct validity. |
| `08_analysis.tex:181-182`, statement-count proxy limitation | **REMOVE** | Obsolete after removing the proxy. |
| `08_analysis.tex:183-188`, open-source generalisability, search limits, and sampling imperfections | **KEEP MAIN** | Threats, external and internal validity. |
| `08_analysis.tex:189-194`, prompt overfitting, lack of inference, and restricted prompt set | **CONDENSE LATER** | Threats, conclusion validity of configuration selection. |
| `08_analysis.tex:195-200`, lack of naturalistic evaluation, nondeterminism, and OpenRouter reproducibility | **KEEP MAIN** | Threats, construct, conclusion, and reliability validity. |
| `08_analysis.tex:201-215`, future work | **CONDENSE LATER** | Discussion and conclusion, restricted to limitations-driven extensions. Remove the UI product roadmap and elaborate prompting digression. |
| `09_summary.tex:1-5`, tool-first recap and corpus findings | **CONDENSE LATER** | Conclusion, direct answers to revised RQ1, RQ2, and RQ3. |
| `09_summary.tex:7`, repeated repository links | **REMOVE** | Already covered by declarations. |
| `09_summary.tex:9`, broad actionability claim | **CONDENSE LATER** | Conclusion, calibrated central takeaway. |

## Main-paper float routing

This table accounts for all 13 numbered main figures and 20 main tables.

| Float | Current location | Status | Destination |
|---|---|---|---|
| `fig:implicitColumnsSql` | `02_background.tex:17-23` | **CONDENSE LATER** | One paired SQL and jOOQ example in Background. |
| `fig:implicitColumnsJooq` | `02_background.tex:89-98` | **CONDENSE LATER** | One paired SQL and jOOQ example in Background. |
| `fig:dataFunnel` | `03_dataset_creation.tex:29-34` | **KEEP MAIN** | Study Design, repository funnel. |
| `fig:distribution` | `03_dataset_creation.tex:73-78` | **MOVE ONLINE** | Sampling diagnostics. |
| `fig:distributionCorrected` | `03_dataset_creation.tex:82-87` | **MOVE ONLINE** | Sampling diagnostics. |
| `tab:prevalenceInSample` | `03_dataset_creation.tex:202-238` | **CONDENSE LATER** | Seven-class reference dataset summary. |
| `tab:trainingTestValidationSplit` | `03_dataset_creation.tex:277-301` | **KEEP MAIN** | Project-disjoint partitioning. |
| `fig:dataSets` | `03_dataset_creation.tex:304-309` | **CONDENSE LATER** | Merge into one study-pipeline figure. |
| `fig:ddlInstructions` | `04_evaluation.tex:62-67` | **MOVE ONLINE** | Full prompts and instructions. |
| `fig:dmlDqlInstructions` | `04_evaluation.tex:92-97` | **MOVE ONLINE** | Full prompts and instructions. |
| `tab:modelParameters` | `04_evaluation.tex:131-151` | **CONDENSE LATER** | Compact detector-configuration table. |
| `fig:toolComponents` | `05_development.tex:13-18` | **MOVE ONLINE** | Detector implementation. |
| `fig:toolWorkflow` | `05_development.tex:34-39` | **CONDENSE LATER** | Extract study-relevant stages into the study-pipeline figure. |
| `fig:toolResults` | `05_development.tex:47-101` | **MOVE ONLINE** | CLI output documentation. |
| `tab:zeroShotBev` | `07_results.tex:7-27` | **CONDENSE LATER** | Compact detector-selection table. |
| `fig:gptOssAnomaly` | `07_results.tex:41-53` | **MOVE ONLINE** | Model-selection diagnostics. |
| `tab:fewShotBev` | `07_results.tex:63-83` | **CONDENSE LATER** | Compact detector-selection table. |
| `tab:chainOfThoughtBev` | `07_results.tex:93-113` | **CONDENSE LATER** | Compact detector-selection table. |
| `tab:treeOfThoughtBev` | `07_results.tex:125-145` | **CONDENSE LATER** | Compact detector-selection table. |
| `tab:toolDetections` | `07_results.tex:167-190` | **KEEP MAIN** | Revised RQ1 event-count evidence. |
| `tab:toolConfusion` | `07_results.tex:194-210` | **MOVE ONLINE** | Event-matching diagnostics, renamed later. |
| `tab:toolConfusionCorrected` | `07_results.tex:212-227` | **MOVE ONLINE** | Corrected-label sensitivity analysis. |
| `tab:toolBevUncorrected` | `07_results.tex:231-255` | **KEEP MAIN** | Revised RQ1 primary per-class results. |
| `tab:toolBevCorrected` | `07_results.tex:257-281` | **MOVE ONLINE** | Corrected-label sensitivity analysis. |
| `tab:toolClassificationConfusion` | `07_results.tex:289-303` | **MOVE ONLINE** | Classification-only evaluation. |
| `tab:toolClassificationConfusionCorrected` | `07_results.tex:306-320` | **MOVE ONLINE** | Classification-only evaluation. |
| `tab:toolClassificationBevUncorrected` | `07_results.tex:325-349` | **MOVE ONLINE** | Classification-only evaluation. |
| `tab:toolClassificationBevCorrected` | `07_results.tex:351-375` | **MOVE ONLINE** | Classification-only evaluation. |
| `tab:prevalenceInTotal` | `07_results.tex:385-409` | **KEEP MAIN** | Revised RQ2 after revising its columns. |
| `tab:implicitColumnsCauses` | `07_results.tex:433-459` | **CONDENSE LATER** | Combined revised RQ3 API table. |
| `tab:poorMansSearchEngineCauses` | `07_results.tex:467-490` | **CONDENSE LATER** | Combined revised RQ3 API table. |
| `fig:checkConstraint` | `08_analysis.tex:63-69` | **MOVE ONLINE** | Error example. Summarise its mechanism in the main error table. |
| `tab:toolComparison` | `08_analysis.tex:93-117` | **REMOVE** | Incompatible cross-task comparison. |

## Appendix routing

No current appendix remains in the journal PDF. The main paper will extract only compact evidence from selected appendices.

| Current appendix | Contents | Status | Online destination |
|---|---|---|---|
| Appendix 2 | GitHub search terms, one listing figure | **MOVE ONLINE** | Repository mining. |
| Appendix 3 | Omitted projects | **MOVE ONLINE** | Repository cleaning. |
| Appendix 4 | Nineteen-class table | **MOVE ONLINE** | Full taxonomy. Extract seven operational rows for the main paper. |
| Appendix 5 | Nineteen decision-tree figures | **MOVE ONLINE** | Annotation codebook. |
| Appendix 6 | Intra-annotator matrix | **MOVE ONLINE** | Annotation reliability. Retain Kappa in the main paper. |
| Appendix 7 | Candidate-model table | **MOVE ONLINE** | Detector configuration. Extract the selected configuration. |
| Appendix 8 | Eight full prompt figures | **MOVE ONLINE** | Prompt artefacts. |
| Appendix 9 | CLI configuration table | **MOVE ONLINE** | Implementation documentation. |
| Appendix 10 | Seven zero-shot metric tables | **MOVE ONLINE** | Configuration results. |
| Appendix 11 | Seven few-shot metric tables | **MOVE ONLINE** | Configuration results. |
| Appendix 12 | Seven Chain-of-Thought metric tables | **MOVE ONLINE** | Configuration results. |
| Appendix 13 | Seven ToT-inspired metric tables | **MOVE ONLINE** | Configuration results. |
| Appendix 14 | Eleven localisation tables | **MOVE ONLINE** | Event-matching diagnostics, renamed later. |
| Appendix 15 | Eleven classification tables | **MOVE ONLINE** | Classification-only evaluation. |
| Appendix 16 | Project-level Jaccard heatmap | **MOVE ONLINE** | Exploratory co-detection after correction. |
| Appendix 17 | File-level Jaccard heatmap | **MOVE ONLINE** | Exploratory co-detection after correction. |
| Appendix 18 | Project-level conditional-frequency heatmap | **MOVE ONLINE** | Exploratory co-detection after correction. |
| Appendix 19 | File-level conditional-frequency heatmap | **MOVE ONLINE** | Exploratory co-detection after correction. |
| Appendix 20 | Project-level Spearman heatmap | **MOVE ONLINE** | Exploratory co-detection after correction. |
| Appendix 21 | File-level Spearman heatmap | **MOVE ONLINE** | Exploratory co-detection after correction. |

## Cross-reference and structure hazards

### Critical

1. The wrapper in `main.tex:39-56` maps thesis headings down one level. A source `subsubsection` becomes a fourth-level paragraph heading. The target ESE structure must remove this compatibility layer after the source files are reorganised.
2. The appendix sequence starts at Appendix 2. Appendix 1 is absent.
3. Appendix labels are anchored one section early. Numeric references work, but hyperlink targets and label metadata are unreliable.
4. The current RQ labels and navigation references assume five RQs. Step 5 must replace them as one coordinated change.
5. The terms "ground truth," "confusion matrix," and "Total" are embedded in section, table, and appendix labels. Step 4 must correct the measurement terminology before the new skeleton relies on it.

### Important

1. Main float numbering follows first-mention order, and every labelled main float is referenced. Preserve that property when relocating blocks.
2. Most appendix floats have no individual label. Eleven labelled localisation tables are never referenced individually.
3. The `fig:dataSets` diagram mixes dataset construction, configuration evaluation, detector development, and test evaluation. It should become one simpler study-pipeline figure.
4. The `fig:toolWorkflow` diagram describes implementation rather than the empirical study and is too dense at article scale.
5. The original and corrected distribution figures describe 603-project and 602-project populations. Only the final population belongs in the main argument.
6. The annotation heatmap image says "Beware of the Unknown," whereas the paper uses "Fear of the Unknown."
7. DDL, DML, and DQL appear in captions without manuscript definitions.
8. Most captions name their float but do not define encodings or tell the reader what result to inspect.

### Minor

1. The abstract uses "LLM" before expansion.
2. Several defined section labels are unused. They are relocation hazards rather than current build errors.
3. Raw repository URLs in the abstract create two large overfull lines.
4. The declarations contain unresolved confirmation placeholders for competing interests, funding, ethics approval, and consent.

## Disposition summary

The route preserves the study's empirical core:

- repository mining and the target population;
- reference annotation and project-disjoint partitioning;
- detector configuration and occurrence-level evaluation;
- detected corpus prevalence;
- API manifestations;
- evidence-based discussion and validity threats.

The route moves thesis-scale detail online:

- the full taxonomy and decision trees;
- search alternatives and search strings;
- full prompts and configuration options;
- detailed model and prompt tables;
- classification-only analysis;
- corrected-label diagnostics;
- co-detection matrices and heatmaps;
- implementation and CLI documentation.

The route removes material with no defensible journal-paper role:

- the thesis outline;
- Design Science framing;
- the work-process reflection;
- implementation-technology inventory;
- the incompatible plain-SQL rate comparison;
- the cross-domain F1 league table;
- the product-interface roadmap.

## Step 1 completion check

- [x] Current page, section, figure, table, appendix, and warning baseline recorded.
- [x] Every current section and paragraph group assigned a destination.
- [x] All 33 main-paper floats assigned a destination.
- [x] All 20 appendices and their 73 floats assigned an online destination.
- [x] Earlier paper inspected directly and used only for its section order and RQ grouping.
- [x] No manuscript source changed.

Step 2 can now lock the paper's claim, scope, title, contribution list, and three research questions against this route.

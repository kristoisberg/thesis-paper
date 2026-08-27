# ESE Step 2: locked paper identity

Date: 2026-08-27

Status: completed and narrowed by the Step 3 evidence freeze. These decisions govern the later restructuring steps; no manuscript source was changed in this step.

## One-page decision sheet

### Title

*LLM-Based SQL Antipattern Detection in jOOQ Code: An Occurrence-Level Evaluation and Repository Study*

### Central claim

Project-disjoint occurrence-level evaluation shows how closely one selected-detector run agrees with the original single-annotator reference spans at the same granularity used for repository counting, so the 602-repository corpus supports class-specific claims about detector flags rather than estimates of true antipattern prevalence.

### Target population and scope

The study population comprises the 602 public GitHub repositories identified on 10 January 2026 through the study's Maven and Gradle manifest searches that declare a jOOQ dependency, store generated jOOQ schema classes in version control, and contain non-generated Java files referring to jOOQ or those generated classes, after the documented exclusions and duplicate removal. Empirical claims are restricted to this identified corpus.

The corpus is not presented as representative of all jOOQ, GitHub, open-source, industrial, or proprietary projects. The study does not cover repositories that generate jOOQ classes only at build time, use unsearched build arrangements, or do not expose the required Java sources through the search procedure.

### Research questions

1. **RQ1:** What occurrence-level agreement does one run of the selected LLM-based detector achieve against the original single-annotator reference spans for seven operationalised SQL antipatterns in the 20-repository, project-disjoint test partition?
2. **RQ2:** How frequently does the selected detector flag each of the seven SQL antipatterns in the 602-repository corpus, and how are those flags distributed across repositories?
3. **RQ3:** Which recurring jOOQ API or source-code patterns are most frequently associated with detector flags for Implicit Columns and Poor Man's Search Engine in the 602-repository corpus?

The four-model, four-prompt comparison configures the detector before RQ1; it is not a standalone research question. Co-detection remains exploratory and outside the three RQs unless it is recomputed over all analysis units with repository-size or exposure controls.

### Contributions

1. A source-level operationalisation and single-annotator reference dataset containing 1,562 line-localised occurrences of 19 SQL antipatterns in a stratified sample of 61 jOOQ repositories, with seven classes retained under explicit support criteria for detector experiments.
2. A project-disjoint, occurrence-level agreement evaluation of one selected-detector run for multi-label, multi-occurrence line-span localisation, with class-specific event counts, precision, recall, F1, and error mechanisms against the original single-annotator reference spans.
3. Detector-output measurements for seven SQL antipatterns across the identified corpus of 602 public GitHub repositories, comprising 15,931 flags in 17,450 relevant Java files and reporting class-level counts and repository coverage.
4. An empirical characterisation of recurring jOOQ API and source-code patterns associated with detected Implicit Columns and Poor Man's Search Engine occurrences.

The detector implementation and replication package are supporting artefacts rather than separate empirical contributions.

## Locked units and evidence chain

| Stage | Population or data | Unit of analysis | Permitted conclusion |
|---|---|---|---|
| Reference annotation | 61 repositories sampled from the preliminary 603-repository corpus | Line-span occurrence in a Java file | The reference dataset contains 1,562 occurrences across 19 classes; seven classes satisfy the support criteria. |
| Detector configuration | Validation partition from the project-disjoint split | Same-file, same-class occurrence match | The model and prompt results justify selecting one configuration for held-out evaluation within this experiment. |
| RQ1 evaluation | 20 test repositories, 502 relevant Java files, and 523 original-reference occurrences in the seven retained classes | One-to-one same-file, same-class line-span match at IoU >= 0.5 | Agreement with the original reference and observed errors differ by class; aggregate performance does not apply uniformly to every class. |
| RQ2 corpus study | 602 repositories and 17,450 relevant Java files | Detector flag, aggregated by class and repository | The selected detector produced 15,931 flags in 601 repositories; these are detector outputs, not verified population prevalence. |
| RQ3 pattern study | Detector flags for Implicit Columns and Poor Man's Search Engine in the 602-repository corpus | Detector flag assigned post hoc to an API or source-code pattern | The reported patterns describe how these two classes appear among detector flags; they do not estimate API risk or causality. |

The project split contains 21 training, 20 validation, and 20 test repositories. Class selection used the complete annotated sample, and the split seed was selected to balance class support. The 602-repository corpus analysis includes repositories used during detector configuration and evaluation, so it is not an independent external-transfer test.

## Reporting rules fixed by this step

- Use **reference annotations**, not **ground truth**.
- Use **evaluated detector**, not **validated detector**.
- Describe corpus results as **flags**, **detections**, or **detector outputs**, not true prevalence, incidence, or rates.
- Use the original reference annotations for the primary RQ1 result. Present corrected annotations only as an optimistic sensitivity analysis because detector disagreements initiated the corrections.
- Identify all RQ1 metrics as results from one selected-detector run.
- Treat the project bootstrap as conditional project-composition sensitivity, not as a population confidence interval.
- Report class-specific results alongside aggregates. Under the original reference, the per-class F1 range is 0.48 to 0.97.
- Distinguish micro, macro, and weighted measures. The primary original-reference event totals are 460 TP, 76 FP, and 63 FN, which yield micro precision 0.858, micro recall 0.880, and micro F1 0.869.
- Do not infer developer benefit, production readiness, CI suitability, improved code quality, or superiority over static analysis.
- Do not infer that an API construct causes or increases antipattern risk because the analysis lacks API-use denominators.
- Restrict RQ3 claims to Implicit Columns and Poor Man's Search Engine.
- Do not retain the claimed 98% API-pattern coverage until it is reconciled with the 5.9% and 6.3% uncategorised shares.
- Do not describe co-detection frequencies as dependency, prediction, or causal clustering.

## Terminology to preserve

Use these seven class names consistently:

1. Implicit Columns
2. ID Required
3. Keyless Entry
4. Fear of the Unknown
5. 31 Flavors
6. Poor Man's Search Engine
7. Rounding Errors

The annotation heatmap label "Beware of the Unknown" is inconsistent and must not propagate into the paper.

## Review method

The lock sheet synthesises three independent passes required by the academic review workflow:

- a research-positioning pass tested the title, central claim, target population, RQs, and contribution boundary against an ESE-style empirical paper;
- a logic pass traced each RQ from population and unit through method, result, and permitted conclusion;
- a consistency pass audited corpus sizes, split sizes, occurrence counts, class names, aggregate metrics, and forbidden generalisations.

## Completion check

- One title and one central claim are fixed.
- Three RQs use occurrence, detector-flag, repository, and pattern units consistently.
- The target population is dated and bounded by the actual repository-search procedure.
- Detector configuration and exploratory co-detection have explicit roles outside the RQs.
- The contribution list matches the available evidence.
- No manuscript source changed.

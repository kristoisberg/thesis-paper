**

HIGH LEVEL SUMMARY

---

Summary

This manuscript presents an empirical evaluation of a large language model (LLM)-based detector for identifying and localizing SQL antipatterns in Java applications using the jOOQ fluent query-builder domain-specific language (DSL) and its reverse-engineered schema classes. The authors construct a manually annotated, occurrence-level reference dataset of 1,562 source-line spans across 19 SQL antipatterns from 61 size-stratified open-source repositories, retaining seven antipattern classes for project-disjoint evaluation. Evaluating a selected Zero-Shot configuration (Claude Opus 4.5) via one-to-one bipartite line-span matching ($\text{IoU} \ge 0.50$) on 20 held-out test repositories yields a pooled micro F1-score of 0.869 (ranging from 0.481 to 0.974 across classes), and applying the detector to a 602-repository corpus produces 15,931 flags whose file-normalized breadth, within-file repetition, repository concentration, and exploratory source-fragment patterns are systematically characterized.

Strengths

- Novel Representation and Occurrence-Level Benchmark Dataset: The study addresses an important representation gap in database-access code quality research by targeting type-safe fluent query-builder DSLs (jOOQ) and generated Java schema classes that traditional SQL string-extraction and parsing pipelines cannot observe, contributing a valuable dataset of 1,562 class-labelled source-line spans across 61 stratified repositories.
    
- Fine-Grained Line-Span Localisation and Qualitative Error Analysis: Rather than framing LLM code smell detection as coarse file- or snippet-level binary classification, the authors formulate the task as multi-span, line-level localisation evaluated via Intersection over Union ($\text{IoU}$) on project-disjoint splits, uncovering nuanced failure modes such as missed returning() clauses, unexempted audit-log tables, and grouped search predicates.
    
- Rigorous Repository-Scale Structural Characterization: The 602-repository corpus study thoughtfully decomposes raw detector flag counts by source role (generated schema vs. application/query code), separating flagged-file breadth from within-file repetition, controlling for repository-size skew and SHA-256 byte-identical file duplicates, and providing actionable insights into how schema-level versus query-level warnings distribute in practice.
    

Weaknesses

- Absence of a Deterministic Static Analysis Baseline: Over two-thirds of the corpus flags and held-out reference spans come from Implicit Columns and ID Required, where occurrences are largely governed by straightforward syntactic or lexical patterns (e.g., selectFrom, select(), DSL.asterisk(), or primary keys named id). Please consider implementing a lightweight AST- or regex-based baseline on the held-out test set to empirically quantify where LLM semantic inference adds value relative to deterministic rules.
    
- Severe Project-Level Sparsity in Evaluation Partitions: Because the partitioning seed search optimized for raw occurrence counts without constraining the number of distinct projects per class within each split, several retained antipatterns appear in only 1 to 3 test repositories (e.g., all 39 test instances of 31 Flavors reside in a single repository, and Rounding Errors in two). The authors might consider enforcing a minimum project-support constraint per split or more prominently framing the per-class metrics for these sparse classes as descriptive case-study observations rather than generalizable cross-project estimates.
    
- Single-Annotator Reference Standard and Pre-Partitioning Codebook Refinement: The ground-truth dataset relies on a single annotator who iteratively refined the decision-flowchart codebook across all 61 repositories prior to partitioning, and post-hoc inspection revealed substantial human omissions in classes like Fear of the Unknown (where 23 of 24 apparent false positives were unannotated occurrences). Please consider clarifying whether any prompt exclusions were derived from validation/test edge cases during codebook creation and reporting class-specific revised-reference bounds alongside the pooled sensitivity metrics.
    
- Confounded Model Selection Factors and Missing Replication Package Links: In the validation comparison, runtime and cost comparisons across models are confounded by asymmetric reasoning configurations (disabling reasoning only for Claude Opus 4.5 while enabling high/fixed reasoning for others), and the Data and Code Availability declarations provide bare Git commit hashes (d9b35e3, bb3bf60, cf82fe5, 4a3b4d5) without a repository URL or archival DOI. Please consider providing explicit repository URLs/DOIs for Empirical Software Engineering compliance and clarifying the two-stage validation screening protocol and reasoning trade-offs.
    

Potential Issues And Suggestions

[Introduction, SQL Antipattern Operational Definitions, and Related Work] (Pages: 1-7)

Potential Mistakes and Improvements

1. Potential Concern Regarding Over-Inclusive Operationalisation of ID Required and Conflation of Naming Conventions with Schema Antipatterns (Section 2.1, Table 1, Page 3) In Section 2.1 (Table 1, p. 3), the operational definition for ID Required states: "A generated table class, excluding views, defines a primary key named exactly id, ignoring case, or defines a synthetic primary key despite a suitable natural or compound unique key (Karwin 2023, Ch. 4)." In Karwin's conceptual definition, the antipattern occurs when a synthetic/pseudokey (often named id) is added superfluously when a natural or compound key is already suitable, or when naming a key id obscures domain meaning and causes join ambiguity; however, a surrogate key named id is widely used in relational design when no stable, concise natural key exists. Because the first disjunct of the operational definition treats name.equalsIgnoreCase("id") as a standalone sufficient condition via a purely lexical check—whereas the second disjunct requires semantic evaluation of candidate keys—this creates a potential construct validity concern by conflating a ubiquitous ORM/migration naming convention with a structural schema-design flaw. Given that ID Required accounts for 3,597 flags across 49.7% of all generated-schema files in the corpus (and is one of the two dominant classes highlighted in the Abstract and RQ2), readers of Empirical Software Engineering may question what proportion of ID Required occurrences in both the reference dataset and corpus flags were triggered solely by the lexical id rule versus the presence of a competing natural/unique key. While Section 5.2 briefly notes later that a primary key named id is sufficient for a flag, Section 2.1 should explicitly justify why this disjunction was chosen over requiring evidence of a redundant surrogate key, clarify early on that this operational boundary represents an over-approximation of Karwin's conceptual antipattern, and, if feasible, note whether the reference annotations or prompt rules distinguish between the two sub-conditions.
    
2. Potential Concern Regarding Ambiguity Between Reference Annotation Rules and Detector Rules in Poor Man's Search Engine (Section 2.1, Table 1, Page 4) In Table 1 (p. 4), the operational definition of Poor Man's Search Engine states: "A jOOQ condition uses LIKE, ILIKE, or a regular expression for full-text matching. Prefix searches are excluded. Calls whose parameters do not reveal whether full-text wildcards are present are included by the detector rule (Karwin 2023, Ch. 17)." Phrasing the last sentence specifically as "included by the detector rule" leaves it ambiguous whether the human reference annotator also followed this exact conservative inclusion rule during ground-truth creation (e.g., for dynamically passed variables in like(param) or likeIgnoreCase(param) where wildcard placement is not statically visible in the file), or whether this heuristic applied only to the single-file LLM prompt. If the annotator and detector used asymmetric inclusion criteria for unresolved parameters, that would introduce systematic bias into the RQ1 agreement metrics; if both used the exact same conservative rule, the phrasing "by the detector rule" is potentially confusing in a table defining the study's ground-truth operational classes. Furthermore, jOOQ substring-matching convenience methods such as contains() and containsIgnoreCase() (which constitute 27.0% of the corpus flags for this class in Table 10) generate LIKE '%...%' predicates under the hood without using the literal method name like or ilike in the Java DSL. Clarifying in Table 1 and Section 2.1 that both the reference codebook and the detector prompt shared the exact same conservative rule for unresolved parameters, explaining why unresolved parameters were included rather than excluded, and explicitly mentioning substring convenience methods (contains / containsIgnoreCase) in Table 1 would improve methodological clarity and reproducibility.
    
3. Potential Concern Regarding Underspecified Static Evidence and jOOQ Code-Generation Artefacts for 31 Flavors and Fear of the Unknown (Section 2.1–2.2, Pages 3–4) In Section 2.2 (p. 4), the manuscript states: "The generator reverse-engineers an existing database schema into Java classes that model objects such as tables, columns, keys, and constraints (jOOQ 2025a)." However, two of the retained database-design classes in Table 1 rely on schema properties and semantic qualifiers whose static representation in jOOQ-generated Java code is not fully specified:
    

- 31 Flavors (Page 4): Defined as "A column encodes a fixed allowed-value list with a CHECK constraint or ENUM instead of a lookup table." In jOOQ code generation, whether CHECK constraint expressions are emitted into generated table or key classes depends on the underlying SQL dialect and generator configuration, and generated Java classes for ENUM types (which implement org.jooq.EnumType) are separate artefacts that could potentially interact with the path-exclusion filters described in Section 3.3.
    
- Fear of the Unknown (Page 4): Defined in part as a schema that "uses a semantically meaningless sentinel for missing data, [or] marks a practically non-null column as nullable". While column nullability (DataType.nullable(...)) and default values (DataType.defaultValue(...)) are encoded in generated TableImpl column declarations, determining from a generated table class alone whether a column marked .nullable(true) is "practically non-null" requires specific static indicators (such as column-naming heuristics) that are not described in the text. Briefly expanding Section 2.1 or Section 2.2 to specify which exact jOOQ-generated artefacts and AST constructs (TableImpl DataType chains, Keys.java, Check metadata, or EnumType declarations) survive reverse-engineering into the analysed files—and what static indicators operationalise a "practically non-null" column—would help readers understand what schema evidence is genuinely observable by both the annotator and the detector.
    

5. Potential Concern Regarding the Framing of Deterministic AST/API Rule Baselines Across Syntactic vs. Semantic Antipatterns (Section 2.3, Pages 5–7; Table 2, Page 7) In Section 2.3 and Table 2 (p. 7), the manuscript characterises the "API or AST rules" approach as: "Can localise encoded patterns but requires explicit coverage of jOOQ idioms and cross-file relationships." While this limitation holds for classes requiring semantic interpretation of identifier names or cross-file schema context (such as inferring foreign-key relationships in Keyless Entry, where the LLM prompt is explicitly supplied the closest Keys class, or judging whether a FLOAT/DOUBLE column stores monetary quantities in Rounding Errors), several of the dominant operational rules in Table 1 are local syntactic patterns within a single file. Specifically, matching primary keys named id in a generated table class (ID Required) or matching selectFrom(...), select(), and DSL.asterisk() outside fetchCount/fetchExists (Implicit Columns) does not require cross-file relationships and can be localised deterministically via standard Java AST analysis. Explicitly distinguishing in Section 2.3 and Table 2 between (a) antipattern classes whose operational definitions are largely syntactic/structural within a single file and (b) classes whose definitions require cross-file key context or natural-language domain interpretation of identifier names would provide a more balanced comparison with rule-based static analysis and better motivate why an LLM is evaluated across all seven classes (as well as the deterministic baseline discussion in Section 5.3).
    
6. Potential Concern Regarding the Breadth of Related Work on Host-Language ORM Analysis and Peer-Reviewed LLM Code-Smell Detection (Section 2.3, Pages 6–7; Table 2, Page 7) In Section 2.3 and Table 2, prior database-access detectors are grouped strictly under "SQL extraction and parsing" (DbDeo, SQLInspect, SQLCheck), while prior LLM-based code-smell detection is represented solely by an undergraduate bachelor's thesis (Blaauwendraad 2025) and a regional conference paper on PL/SQL (Sousa et al. 2025). For a submission to Empirical Software Engineering, this literature framing has two notable gaps:
    

- First, prior software engineering research has investigated static and hybrid detection of database-access and ORM performance/query antipatterns directly in host-language Java ASTs and call graphs without relying on regex SQL string extraction—for example, empirical studies by Chen et al. on detecting redundant data retrieval / unnecessary column fetching in ORM code (which directly parallels Implicit Columns) and rule/metric-based ORM antipattern detection, as well as static localisation of SQL queries in Java source.
    
- Second, relying on a bachelor's thesis (Blaauwendraad 2025) as the sole citation for LLM-based code-smell detection in general programming languages under-represents the peer-reviewed software engineering literature investigating prompt-based and hybrid LLM code-smell detection in Java. Incorporating peer-reviewed studies on host-language ORM antipattern analysis and LLM-based code-smell detection into Section 2.3 and Table 2 would more rigorously situate the paper within the Empirical Software Engineering literature.
    

Minor Corrections and Typos

- Page 4, Table 1 (Implicit Columns row): The citation (Karwin 2023; jOOQ 2025f, Ch. 19) attaches Ch. 19 to jOOQ 2025f rather than Karwin 2023. It should read (Karwin 2023, Ch. 19; jOOQ 2025f).
    

[Study Design, Dataset Construction, Partitioning, and Evaluation Methodology] (Pages: 7-16)

Potential Mistakes and Improvements

Verification Summary: The repository mining filtering sequence ($3,829 \rightarrow 802 \rightarrow 645 \rightarrow 603 \rightarrow 602$), size stratification counts ($467 + 100 + 36 = 603$, with a $10\%$ sample yielding $47 + 10 + 4 = 61$ repositories), 30-day washout intra-annotator reliability calculations ($P = 142/149 = 0.953$, $R = 142/158 = 0.899$, $F_1 = 0.925$), and all row and column sums in Table 3 (totaling $1,436$ retained occurrences across the seven classes) were verified as mathematically accurate.

1. Underspecified Partitioning Objective Function and Single-Repository Class Concentration (Section 3.5, Page 12, Table 3): In Section 3.5, the authors retain classes with at least $25$ occurrences across at least three projects globally, and then evaluate $1,000,000$ integer seeds (Seed 767 573) to partition the $61$ repositories into training ($21$), validation ($20$), and test ($20$) sets: "For each candidate, the objective measured variation in each class's occurrence counts across the splits and summed the squared values over the seven classes. Seed 767 573 achieved the lowest score, 0.52." This raises two methodological concerns:
    

- Omission of the exact mathematical objective function: A potential concern for reproducibility is that the mathematical formula producing the dimensionless score of 0.52 is not written out in the text. Because raw occurrence counts in Table 3 span more than an order of magnitude across classes (from $39$ for Rounding Errors to $795$ for Implicit Columns) and differ substantially across splits (e.g., Implicit Columns has $175$, $350$, and $270$ occurrences in Training, Validation, and Test; 31 Flavors has $17$, $15$, and $39$), an unnormalized sum of squared deviations or raw variances would be orders of magnitude larger than $0.52$. Explicitly stating the equation (e.g., whether variation is computed as the squared coefficient of variation across the three splits or squared relative deviation from target split proportions) is necessary to verify the 0.52 score.
    
- Single-repository clustering and bootstrap degeneracy: Because the prerequisite support rule ("at least 25 occurrences in at least three projects") was applied globally across all $61$ repositories and the seed-search objective optimized exclusively for occurrence counts without constraining repository counts per class within each split, several classes in Table 3 collapse into a single repository in the validation or test sets. Specifically, Keyless Entry has all $56$ validation occurrences in $1$ repository (56 (1)), Rounding Errors has all $10$ validation occurrences in $1$ repository (10 (1)), and 31 Flavors has all $39$ test occurrences in $1$ repository (39 (1)). When all occurrences of a class in an evaluation partition come from a single repository, class-level metrics reflect conformance to a single project's schema and naming conventions rather than cross-project generalization. Furthermore, in the $10,000$-iteration project-cluster bootstrap on the $20$ test repositories (Section 3.7, Page 15), resampling $20$ projects with replacement omits the sole test project containing 31 Flavors in approximately $(19/20)^{20} \approx 35.8\%$ of bootstrap replicates (and omits both test projects containing Rounding Errors in $(18/20)^{20} \approx 12.2\%$ of replicates), leaving recall and $F_1$ undefined for that class in those draws. Explaining in Section 3.5 why a minimum per-partition repository constraint (e.g., requiring $\ge 1$ or $\ge 2$ repositories per split for every retained class) was not enforced alongside occurrence balance, and specifying in Section 3.7 how zero-occurrence bootstrap replicates are handled mathematically, would strengthen the evaluation methodology.
    

3. Ambiguity in the Bipartite Span-Matching Algorithm Specification (Section 3.7, Page 14): Section 3.7 describes the one-to-one occurrence matching procedure as follows: "At the primary threshold of 0.50, maximum-cardinality bipartite matching assigns each prediction and reference to at most one pair. Candidate lists are ordered by descending IoU, predicted span, and source order for deterministic tie handling."
    

- Potential concern for algorithmic reproducibility: In combinatorial optimization, an unweighted maximum-cardinality bipartite matching (e.g., Hopcroft–Karp) on a thresholded graph ($\text{IoU}(S_p, S_r) \ge 0.50$) maximizes the total number of matched edges $|\mathcal{M}|$ without optimizing edge weights, whereas iterating sequentially over candidate pairs sorted by descending IoU describes a greedy matching heuristic (or, if cardinality is maximized first and edge weights second, a maximum-cardinality, maximum-weight bipartite matching). When multiple overlapping or consecutive predictions and references compete within the same file and class (such as when consecutive occurrences are grouped into one span), greedy assignment by descending IoU is not guaranteed to yield a maximum-cardinality matching and can produce different true-positive counts than exact maximum-cardinality matching. Clarifying in Section 3.7 whether the evaluation script executes (a) a greedy one-to-one assignment over the sorted candidate list, (b) an unweighted maximum-cardinality algorithm relying on adjacency-list ordering, or (c) an exact lexicographic maximum-cardinality, maximum-weight bipartite matching solver would make the evaluation protocol unambiguous.
    

5. Retry-Limit Discrepancy and Unreported File-Failure Rates in the Corpus Run (Section 3.6, Page 14 & Section 3.8, Page 15): Section 3.6 (Page 14) notes a substantial difference in retry budgets between the held-out evaluation and the full corpus run: "The held-out command allowed up to 1000 retries per file. The corpus command allowed two retries per file." Section 3.8 (Page 15) then defines the corpus denominators ($F_{rc}$, totaling $17,988$ relevant Java files: $7,226$ generated-schema and $10,762$ application/query files) over all files selected by recursive file discovery (**/*.java) and the detector's file filters.
    

- Potential concern for denominator validity: Because LLM API requests routed through gateways can encounter transient network, rate-limit, or JSON Schema validation errors, reducing the retry cap from $1,000$ on the test set ($502$ files) to $2$ on the corpus ($17,988$ files) raises the question of whether all $17,988$ corpus files succeeded within the two-retry budget. Neither Section 3.6 nor Section 3.8 states whether any files exhausted their retries and failed to return a valid structured response. If any file requests failed permanently after two retries and were retained in the eligible file denominators ($F{rc}$) with zero flags ($Y{rc} = 0$), API execution failures would be conflated with negative detections, downward-biasing flagged-file breadth and flag density. Explicitly reporting the file-level failure rate (or confirming a $100\%$ completion rate across all $17,988$ files) in Section 3.6 or Section 3.8 would resolve this concern.
    

7. Pre-Partitioning Codebook Iteration Loop and Washout Check Scope (Sections 3.4–3.6, Pages 11–13): Two boundary conditions connecting annotation, partitioning, and prompt construction across Sections 3.4–3.6 would benefit from explicit clarification in situ:
    

- Whole-sample codebook revision loop prior to partitioning (Sections 3.4–3.6): Section 3.4 (Page 11) states that a single annotator iteratively developed and revised the decision-flowchart codebook while reviewing the entire $61$-repository sample ("When a previously unseen variant or a non-occurrence edge case exposed a missing rule, the annotator revised the corresponding flowchart and reviewed earlier files that the change could affect"). Project-disjoint partitioning (Section 3.5, Page 12) occurred after the entire $61$-repository sample was annotated, and Section 3.6 (Page 13) notes that detector prompt development translated those codebook rules directly into the prompts ("the resulting instructions stated the intended decision boundary in the same terms as the annotation codebook"). Although iterative prompt refinement and Few-Shot example selection only inspected the $21$ training repositories, adapting the underlying codebook rules to edge cases encountered across all $61$ repositories prior to partitioning creates a potential pathway for validation- and test-set edge cases to influence the operational definitions and exclusions encoded in the prompts. Clarifying in Sections 3.4 and 3.6 whether every variant and exclusion rule in the final prompts was independently attested in the $21$-repository training partition—or whether any codebook exclusions derived from test-set edge cases were carried over into the universal prompts—would help readers assess the strictness of the held-out boundary.
    
- Washout repeatability check scope (Section 3.4, Page 11): For the 30-day washout repeatability check across $128$ files ($64$ positively annotated and $64$ unannotated files, yielding $158$ original and $149$ repeated events with $142$ exact matches), the text does not specify whether those event counts span all $19$ initially annotated classes or only the $7$ retained classes, nor how many of the $64$ previously unannotated files remained negative in the second pass.
    

9. Missing Operational Specifications for File Filtering, Source-Role Classification, Context Attachment, and Exact-Content Weighting (Sections 3.3, 3.6, and 3.8; Pages 10, 13–16): A potential concern for independent reimplementation is that several static pre-processing, context-selection, and aggregation heuristics in Section 3 are referenced without summarizing their exact operational criteria in the text:
    

- File exclusions and generated-table indicators (Sections 3.3 and 3.8, Pages 10 and 15): Section 3.3 notes that a "manually maintained path list" removed irrelevant generated files (records, plain data objects, system schemas, and database extensions), and Section 3.8 states that "Files containing the detector's generated-table indicators form the generated schema role, which contains 7226 files." Summarizing the specific lexical, AST, or path patterns used to classify a file into the generated-schema role (e.g., extends TableImpl or @Generated annotations) and to filter out irrelevant generated artefacts would make the source-frame definition self-contained.
    
- Attaching the "closest" key-definition class and context-window handling (Section 3.6, Page 13): Section 3.6 states that "The request for generated source also received the closest generated key-definition class." In multi-module or multi-schema repositories containing multiple Keys.java files, the exact directory-tree or package-hierarchy heuristic used to select the "closest" key-definition class is not specified, nor is it stated whether any of the $17,988$ source files (plus attached Keys.java classes) exceeded model context or output token limits.
    
- Exact-content deduplication weighting (Section 3.8, Page 16): Section 3.8 states: "We weight each unique content and event once across its physical copies when calculating repository concentration." When a file with a given SHA-256 hash appears $k > 1$ times across repositories, it is ambiguous whether each physical copy receives a fractional weight of $1/k$ or whether full weight ($1$) is assigned to a single canonical copy and $0$ to the remaining $k - 1$ copies. Providing the explicit formula for how repository-level flag counts ($Y{rc}$) and eligible-file counts ($F{rc}$) are adjusted under exact-content weighting would remove this ambiguity.
    

Minor Corrections and Typos

- Page 14, Section 3.6, Paragraph 2 & Page 16, Section 3.8, Paragraph 3: The passive phrasing "The corpus execution was recorded as using the same model, settings, and Zero-Shot prompt family" is slightly ambiguous regarding execution provenance; stating directly that the corpus execution used the same model, settings, and Zero-Shot prompt templates (while keeping any logging limitations in the replication note) would improve clarity.
    
- Page 15, Section 3.8 (Formulas for corpus measures): In the displayed equation $\text{Within-file repetition}{rc} = Y{rc}/A{rc}$, the ratio is undefined ($0/0$) when a repository has eligible files ($F{rc} > 0$) but zero flagged files ($A{rc} = 0$). While the paragraph below explicitly notes when $\text{Flag density}{rc}$ is undefined ($F{rc} = 0$), adding the condition $A{rc} > 0$ alongside the repetition formula would make the mathematical definitions complete.
    
- Page 16, Section 3.8, Paragraph 1: The text states "we select the ceiling of 10 % of flagged repositories by flag count, with repository name breaking cutoff ties" and in the next sentence states that the authors "report bounds over every possible cutoff-tie selection." Clarifying that bounds over all cutoff-tie selections are reported in the analysis while alphabetical repository name breaks ties when a single deterministic selection is needed would remove the apparent contradiction between the two sentences.
    

[Empirical Results: Validation Selection, Held-Out Localisation (RQ1), and Corpus Study (RQ2)] (Pages: 16-21)

Potential Mistakes and Improvements

- Quantitative Verification Summary: All numerical metrics, event counts, and derived percentages reported across Section 4 (Tables 4–10) were cross-checked and verified for internal mathematical consistency:
    

- Section 4.2 & Table 5: For every antipattern class, TP + FN matches the held-out Test count in Table 3 (summing to 523 reference spans), TP + FP sums to the 536 reported predictions, and all per-class, micro (P = 0.858, R = 0.880, F1 = 0.869), macro (P = 0.797, R = 0.813, F1 = 0.793), and reference-support-weighted (P = 0.885, R = 0.880, F1 = 0.877) precision, recall, and F1 scores are exact to three decimal places.
    
- Section 4.2.1 & Tables 6–7: The detector-informed revised-reference sensitivity metrics (512 TP, 24 FP, 51 FN $\rightarrow$ P = 0.955, R = 0.909, F1 = 0.932) and all IoU threshold sensitivity calculations in Table 7 (0.25 to 1.00, preserving TP + FP = 536 and TP + FN = 523) are mathematically exact.
    
- Section 4.3 & Tables 8–10: In Table 8, class flag counts sum to 15,931, and all repository coverage percentages (out of 602), file breadth percentages (out of 7,226 G files, 10,762 A files, and 17,988 All files), within-file repetition ratios (Flags / File breadth), and pooled densities (100 * Flags / Eligible files) are exact. In Table 9, the SHA-256 deduplication counts (17,988 - 621 = 17,367 unique file contents; 488 + 621 = 1,109 file occurrences in duplicate groups, or 6.17%; 1,080 / 15,931 = 6.78% raw flags) are exact, as are the source-fragment category counts and shares in Table 10.
    

- Confounded Reasoning Configurations, Incomplete Factor Grid, and Trade-Off Criteria in Model Selection (Section 3.6, Page 14 & Section 4.1, Pages 16–17, Table 4):
    

- Potential Concern: In Section 3.6, Section 4.1, and Table 4, three aspects of the validation comparison and configuration selection affect evaluation parity and reproducibility:
    

1. Confounded Reasoning Modes and Latency: In the first four rows of Table 4, the candidate models are evaluated under asymmetric reasoning regimes: Claude Opus 4.5 is run with reasoning disabled (temperature = 0.0), whereas GPT-5.2 (xhigh reasoning), gpt-oss-120B (high reasoning at temperature = 1.0), and GLM-5 (fixed reasoning effort) generate internal reasoning tokens (as noted in Section 3.6). Because internal reasoning token generation substantially increases output token volume and wall-clock latency, justifying the selection of Claude Opus 4.5 Zero-Shot (367 s) over GLM-5 (5,774 s) and GPT-5.2 (2,423 s) primarily by its shorter runtime conflates intrinsic model/provider throughput (e.g., Friendli for GLM-5) with the decision to disable reasoning on only one candidate.
    
2. Incomplete Model $\times$ Prompt Grid and Metric Granularity: While Section 4.1 states "We compared these four models and four prompting configurations on the 20-repository validation set" (and Section 3.6 on Page 14 mentions running "each model-prompt pair once", which reads as a full $4 \times 4$ factorial evaluation of 16 runs), Table 4 reports only 7 of the 16 possible combinations in a two-stage screening design (evaluating all four models under Zero-Shot prompts first, and then evaluating Few-Shot, Chain-of-Thought, and Tree-of-Thought exclusively with Claude Opus 4.5). In addition, Table 4 reports only reference-support-weighted metrics to two decimal places (0.88), which are heavily dominated by Implicit Columns ($350 / 581 = 60.2\%$ of validation occurrences in Table 3), leaving unclear whether the three tied models (0.88 F1) differed at the third decimal place or in macro F1 across the sparser database-design classes.
    
3. Cost–Latency–Accuracy Decision Rule and Corpus Execution Cost: GLM-5 (Zero-Shot) achieved the exact same displayed precision (0.88), recall (0.89), and F1 (0.88) as Claude Opus 4.5 (Zero-Shot) at nearly one-third of the cost ($11.76 vs. $31.39), and gpt-oss-120B achieved 0.83 F1 at ~21$\times$ lower cost ($1.49). Conversely, Claude Opus 4.5 (Chain-of-Thought) improved validation precision from 0.88 to 0.92 and F1 from 0.88 to 0.90 for a $1.30\times$ cost increase ($40.86 vs. $31.39) and a 10-minute runtime increase (956 s vs. 367 s). No explicit decision rule explains why a $2.67\times$ cost increase ($31.39 vs. $11.76) was preferred to reduce batch runtime, whereas a $1.30\times$ cost increase and 10 additional minutes for +0.02 F1 (+0.04 precision) were rejected. Moreover, unlike the validation and held-out test runs, Section 4.3 does not report the total cost or runtime of the 602-repository corpus execution.
    

- Suggestion: In Sections 3.6 and 4.1, explicitly state the two-stage validation screening design (or reference the remaining 9 model–prompt combinations in the replication package), note that runtime and cost differences in Table 4 reflect both provider routing and enabled versus disabled reasoning modes, report three decimal places and validation macro F1 in Table 4, and state the weighting criteria governing the trade-off among F1, cost, and batch latency. In Section 4.3, report the total cost and wall-clock runtime of the 602-repository corpus run.
    

- Unexplained Mechanism Behind Inconsistent Detector Events Across Byte-Identical Files and Connection to Reliability Validity (Section 4.3, Page 20, Table 9 & Section 6.5, Pages 25–26):
    

- Potential Concern: Table 9 and the accompanying text on page 20 report that "Eight groups of byte-identical files have inconsistent sets of detector events" during the corpus run, even though the selected detector configuration (Claude Opus 4.5, Zero-Shot) was executed at temperature = 0.0 with reasoning disabled (Section 4.1, page 16). Later, Section 6.5 ("Reliability validity", p. 25) states that "The selected detector was run once on the held-out partition and once on the corpus, leaving run-to-run variance unmeasured" without connecting back to the 8 inconsistent duplicate groups observed in Table 9. Within the study's architecture, two distinct mechanisms can cause byte-identical Java files (having identical SHA-256 content hashes) to yield different detector events:
    

1. Differing attached schema context: For generated-schema (G) files, the detector attaches the closest generated key-definition class (Keys.java) from the repository to the prompt (Section 3.6, page 13). Consequently, two byte-identical generated table files located in different repositories or modules could be paired with different key-definition classes, producing different prompt payloads and legitimately different detector outputs.
    
2. Provider/API inference non-determinism: Conversely, if the full prompt payloads (including any attached context, or in application/query A files that receive no external schema context) were also identical, the divergence reflects residual floating-point or dynamic-batching non-determinism in the hosted LLM API despite temperature = 0.0.
    

- Suggestion: Clarify in Section 4.3 how many of the 8 inconsistent duplicate groups occurred in generated-schema files paired with differing attached key-definition contexts versus identical full prompt payloads exhibiting API-level non-determinism, and cross-reference this observation in Section 6.5 as concrete empirical evidence bounding within-run variance on identical file contents at temperature = 0.0.
    

- Incomplete Breakdown of Disagreement Counts and Pooled-Only Sensitivity Reporting (Section 4.2.1, Pages 18–19, Tables 5–6):
    

- Potential Concern: While Section 4.2 highlights that the pooled micro F1 (0.869) is dominated by Implicit Columns (270 of 523 reference spans) and masks wide per-class variation (0.481 to 0.974), both the qualitative error summary in Table 6 and the sensitivity analyses in Section 4.2.1 obscure class-level distinctions:
    

1. Unquantified Residual Disagreements in Table 6: Unlike Fear of the Unknown and 31 Flavors (where every FP and FN from Table 5 is explicitly accounted for), ID Required (13 FP, 16 FN in Table 5) specifies only 6 of the 16 FNs ("primary-key columns named id") and 1 of the 13 FPs ("unsuitable natural key"), attributing the remaining 10 FNs and 12 FPs generically to "other disagreements exposed reference errors." Similarly, for Keyless Entry (30 FP, 1 FN), Table 6 accounts for 15 FPs (audit-log tables) and 1 FP (ambiguous column name), grouping the remaining 14 FPs as "missing or disputed reference annotations" and omitting the cause of the 1 FN; for Implicit Columns (4 FP, 17 FN), 14 FNs are attributed to returning()/returningResult(), leaving 4 FPs and 3 FNs combined as "span boundaries and reference errors."
    
2. Pooled-Only Revised Reference and Bootstrap Intervals: Both the detector-informed reference revision (512 TP, 24 FP, 51 FN, micro F1 0.932) and the 10,000-replicate project-cluster bootstrap (0.820–0.912 micro F1) are reported solely as pooled micro aggregates. Because reference omissions were heavily concentrated in Fear of the Unknown (23 of 24 FPs) and Keyless Entry (up to 14 of 30 FPs), and because sparse classes occur in only 1–3 test projects (Table 3), pooled micro numbers do not show how the revised reference alters per-class F1 for the lower-scoring classes or how macro/per-class F1 behaves across bootstrap resamples.
    

- Suggestion: In Table 6, provide the exact counts of reference annotation omissions/errors versus genuine detector semantic or span-boundary errors for ID Required, Keyless Entry (including the 1 FN), and Implicit Columns. In Section 4.2.1, report the revised-reference F1 for the classes substantially affected by reference omissions (Fear of the Unknown, Keyless Entry, and ID Required), and report the project-cluster bootstrap intervals for macro or support-weighted F1 (or for the high-support classes Implicit Columns and ID Required) alongside the pooled micro interval.
    

- Unseparated Inclusion of Annotated Sample Repositories in Corpus Aggregate Counts (Section 4.3, Pages 19–21, Tables 8 and 10 & Section 6.3, Page 25):
    

- Potential Concern: The corpus distribution analysis in Section 4.3 (Table 8) and the exploratory source-fragment coding in Section 4.3.1 (Table 10) aggregate all 602 repositories together, including the 61 sampled repositories (2,170 relevant files, or ~12.1% of the 17,988 corpus files) used for prompt development (21 training), configuration selection (20 validation), and held-out evaluation (20 test), as noted in Section 6.3 (p. 25). Because the detector's operational definitions, exclusions, and localisation rules were iteratively tailored to variants observed in the sampled repositories, pooling the 61 sampled projects with the 541 unsampled projects leaves open whether detector flag densities, repetition, or fragment shares differ between the annotated sample and the 541 out-of-sample repositories.
    
- Suggestion: Briefly note in Section 4.3 (or Section 6.3) whether the primary flag density, file breadth (49.7% for ID Required), within-file repetition (2.80 for Implicit Columns), top-decile concentration, and dominant fragment shares in Tables 8 and 10 remain consistent when computed exclusively across the 541 truly unseen repositories.
    

---

Minor Corrections and Typos

- Page 17, Table 4 (Claude Opus 4.5 | Few-Shot row): The reported runtime for Few-Shot (352 s at $45.00) is slightly shorter than for Zero-Shot (367 s at $31.39), while page 16 notes that Claude Opus 4.5 Zero-Shot had "the shortest runtime among the Zero-Shot configurations." A brief note acknowledging transient API/network throughput variance would clarify why the longer Few-Shot prompt completed in slightly less wall-clock time than the Zero-Shot prompt.
    
- Page 18, Section 4.2.1, paragraph 5: In "within the 0.863-0.873 range", a hyphen (-) is used for the numeric range instead of an en-dash (0.863–0.873) as used elsewhere in the manuscript.
    
- Pages 20–21, Section 4.3.1 and Table 10 (Implicit Columns shares): In Table 10, the six rounded category percentages (46.9% + 24.8% + 9.1% + 3.8% + 9.4% + 5.9%) sum to 99.9% due to rounding. Similarly, the text on page 20 notes that fields() (665) and asterisk() (280) "contributed a further 945 flags, or 13.0 %" (945 / 7289 = 12.965%) and that "Named recurring categories accounted for 94.1 %" (6860 / 7289 = 94.114%), whereas summing the corresponding rounded table entries yields 12.9% (9.1% + 3.8%) and 94.0% (46.9% + 24.8% + 9.1% + 3.8% + 9.4%). Adding a brief note to the Table 10 caption stating that percentages are computed from unrounded counts and may not sum to subgroup totals or 100.0% due to rounding would prevent reader confusion.
    

[Discussion, Audit Priorities, and Threats to Validity] (Pages: 21-26)

Potential Mistakes and Improvements

1. Deferred Comparison Against a Deterministic Rule-Based Baseline (Section 5.3, p. 23; Section 7, p. 26):
    

- Observation: Throughout Sections 5.1–5.3 and 6.1–6.3, the manuscript carefully distinguishes between unverified detector flags in the 602-repository corpus and confirmed antipattern prevalence, explicitly noting that the corpus lacks an independent human audit, retains the 61 annotated repositories, and uses role-eligible files rather than API-opportunity denominators. However, in Section 5.3 ("Priorities for independent corpus validation", p. 23) and Section 7 (p. 26), comparing the LLM detector against a deterministic jOOQ baseline (using AST or regular-expression rules) is deferred entirely to future work.
    
- Potential Concern (Comparative Baseline Gap): The study's own empirical findings indicate that the two dominant antipattern classes—which together account for 71.7% (375 of 523) of held-out reference spans in Table 3 and 68.3% (10,886 of 15,931) of corpus flags in Table 8—are heavily driven by deterministic lexical or syntactic patterns:
    

- For Implicit Columns, Table 10 (p. 21) and Section 5.3 (p. 23) show that selectFrom, select(), fields(), and asterisk() fragments account for 84.6% of all class flags (71.7% from selectFrom and select() alone) and were already categorized using a fixed, precedence-ordered list of string and regular-expression patterns (Section 3.8, p. 16). Furthermore, 14 of the 17 held-out false negatives came from returning() or returningResult() calls.
    
- For ID Required, Section 5.2 (p. 22) and Section 5.3 (p. 23) note that under the operational definition in Table 1, a primary key named id (ignoring case) in a generated table class is sufficient by itself to trigger a flag.
    
- For 31 Flavors and Rounding Errors, the operational definitions check for CHECK/ENUM and FLOAT/REAL declarations in generated schema classes.
    

- Because the held-out test set of 502 files and 523 reference spans is already fully annotated, deferring a deterministic baseline entirely to a future corpus audit leaves an important empirical question unanswered: how much of the reported 0.869 micro F1-score (and the associated $14.34 API cost and 386-second runtime) could be achieved by lightweight syntactic rules on the existing 20-project test set, versus where LLM semantic reasoning genuinely adds value (e.g., inferring Keyless Entry relationships, identifying natural keys, or interpreting Fear of the Unknown sentinels).
    
- Actionable Suggestion: Implementing and evaluating a lightweight regular-expression or AST-based baseline on the 20 held-out test repositories for the syntactically regular conditions—or providing a quantitative breakdown in Section 5 of the exact proportion of held-out reference instances that require semantic inference beyond syntactic matching—would substantially strengthen the comparative validity of the evaluation.
    

3. Unquantified Pipeline Anomalies Disclosed in Internal Validity (Sections 3.2–3.5, 3.8, and Section 6.2, p. 24):
    

- Observation: Section 6.2 ("Internal validity", p. 24) candidly discloses three pipeline anomalies in a single paragraph:
    

"The sampling frame used for annotation and partitioning contained one duplicate repository and an incomplete exclusion list for irrelevant generated files. Later analyses corrected the file counts and retained all 15 931 detector flags, but did not revise the original sample or project partitions. An over-broad file-exclusion rule also skips an annotated application table in the test partition."

- Potential Concern (Clarity and Accounting Consistency): While this transparency is commendable, introducing these pipeline discrepancies in Section 6.2 without quantitatively reconciling them with the numbers presented in Sections 3 and 4 leaves three ambiguities that affect traceability and reproducibility:
    

1. Skipped annotated application table in the test partition: It is unclear how the skipped annotated application table affected the held-out evaluation in Section 4.2 (Tables 5–7, pp. 17–19) and the reported partition file counts in Section 3.5 ($509$ training, $1,159$ validation, and $502$ test files). Specifically, the text does not state how many reference annotations resided in that skipped table, which antipattern class(es) they belonged to, or whether those annotations are included among the 523 test-set reference spans and 63 false negatives reported in Table 5 (counted as automatic misses because the detector skipped the file) or excluded from the 523-span denominator prior to evaluation.
    
2. Retained 15,931 detector flags after correcting file counts: Stating that later analyses "corrected the file counts and retained all 15 931 detector flags" implies that the denominator of relevant files ($F{rc}$, totaling 17,988 relevant files in Section 3.8) was updated to exclude irrelevant generated files without clarifying whether any of the 15,931 retained flags originated from files subsequently deemed irrelevant. If the denominator was reduced while retaining flags from excluded files in the numerator, the reported flagged-file breadth ($100 A{rc}/F{rc}$) and flag density ($100 Y{rc}/F_{rc}$) in Table 8 (p. 19) could be inflated. Conversely, if the detector only processed the 17,988 relevant files so that all 15,931 flags reside strictly within those files, the phrasing in Section 6.2 is ambiguous and could be misread.
    
3. Duplicate repository in the 603-repository sampling frame: Section 3.2 (p. 9, Fig. 2) notes that a late-stage duplicate removal reduced the preliminary 603-repository corpus (used for stratified sampling in Section 3.4) to 602 repositories, while Section 3.8 (p. 15) notes that the 602-repository corpus included the 61 sampled repositories. Neither Section 3.2 nor Section 6.2 specifies whether the duplicate pair discovered after sampling involved one of the 61 sampled repositories (and, if so, which partition and size stratum were affected and whether duplicate copies crossed between training, validation, and test partitions).
    

- Actionable Suggestion: Expand Section 6.2 (and cross-reference Sections 3.2–3.5, 4.2, and 4.3 where appropriate) to provide the exact counts for these three anomalies: (a) specify the number and class of reference annotations in the skipped test-partition table and state whether they were counted among the 63 false negatives in Table 5 (along with the test-set F1-score if that file is included or excluded), (b) verify whether all 15,931 corpus flags reside strictly within the 17,988 retained relevant files, and (c) confirm whether the removed duplicate repository was part of the 61-repository annotated sample.
    

2. Distinction Between Corpus Flags and Class-Specific Precision in Table 8 Discussion (Section 5.2, p. 22):
    

- Potential Concern: Section 5.2 (p. 22) focuses almost exclusively on how the two highest-agreement classes (Implicit Columns at 0.984 precision and ID Required at 0.873 precision) are distributed across repositories and files. It does not explicitly caution readers that for lower-precision classes—specifically Keyless Entry (precision 0.538; 30 FPs vs. 35 TPs) and Fear of the Unknown (precision 0.442 against the original reference)—the 2,153 and 1,256 corpus flags (and 33.2% and 32.7% repository coverage) reported in Table 8 may contain a substantial proportion of false positives (such as unexempted audit-log tables) or reference-boundary edge cases.
    
- Actionable Suggestion: Briefly note in Section 5.2 that the repository coverage and density figures for Keyless Entry and Fear of the Unknown in Table 8 should be interpreted alongside their lower held-out precision and the specific disagreement mechanisms identified in RQ1.
    

Minor Corrections and Typos

- Page 24, Section 6.2, paragraph 3: "An over-broad file-exclusion rule also skips an annotated application table in the test partition." Notice the shift to present tense ("skips") whereas the preceding sentences use past tense ("contained", "corrected", "retained", "did not revise"). Consider changing "skips" to "skipped" for tense consistency.
    

[Conclusion, Declarations, Replication Package, and References] (Pages: 26-30)

Potential Mistakes and Improvements

1. Missing Repository URLs and Persistent Identifiers in Data and Code Availability Statements (Page 27): In the "Data availability" and "Code and materials availability" subsections under Statements and Declarations (Page 27), the manuscript cites bare Git commit hashes (d9b35e3, bb3bf60, cf82fe5, and 4a3b4d5) to reference the annotated dataset, experimental outputs, prompts, detector source code, and replication README. However, no repository URL (e.g., a GitHub link) or persistent archival identifier (such as a Zenodo or Figshare DOI) is provided anywhere in the manuscript or reference list. Without a base URL or DOI, a reader or reviewer cannot locate or access the replication package from the commit hashes alone. For a submission to Empirical Software Engineering, which emphasizes open science and verifiable replication packages, this is a substantive reproducibility concern that can be resolved by providing the explicit repository URL(s) and, ideally, a permanent archival DOI.
    
2. Incomplete Bibliographic Details for the Referenced Master's Thesis (Page 26): In the "Prior dissemination and relationship to the master's thesis" subsection (Page 26), the text notes that the article is based on Kristo Isberg's master's thesis, Detecting SQL Antipatterns in jOOQ Database Access Code Using Large Language Models. Because earlier methodology sections (e.g., Section 3.3, Page 10) explicitly direct readers to the original thesis's dataset-creation chapter for detailed explanations of class exclusions and interpretational boundaries, the thesis serves as a supporting methodological reference. However, it is not listed in the References section (Pages 28–30), nor are the granting institution (Tallinn University of Technology), publication year, or persistent URI/handle included in the declaration. Adding a complete bibliographic entry or institutional repository link would ensure that readers can locate the referenced dataset-creation documentation.
    

Minor Corrections and Typos

1. Ambiguous OpenAI (2025) Reference Entries and In-Text Citations (Page 13, Page 16, and Page 30): In the References section (Page 30, lines 1–6), two distinct bibliography entries share the identical author-year label OpenAI (2025):
    

- OpenAI (2025) gpt-oss-120b & gpt-oss-20b model card...
    
- OpenAI (2025) Update to GPT-5 system card: GPT-5.2... Unlike the OpenAI (2026a), OpenAI (2026b), and OpenAI (2026c) entries immediately following them, these two 2025 entries lack a and b suffixes, making in-text citations to OpenAI 2025 (such as on Page 13, Section 3.6, Paragraph 6, and Page 16, Section 4.1, Paragraph 1, where (OpenAI 2025; GLM-5 Team 2026; OpenAI 2025) repeats OpenAI 2025 twice) ambiguous. These entries should be disambiguated as OpenAI (2025a) and OpenAI (2025b) in both the reference list and the corresponding in-text citations.
    

3. Inconsistent Access Date in Reference Factor P (2014) (Page 28): In the reference entry for Factor P (2014) 119 SQL code smells (Page 28), the URL access date is recorded as accessed 28 August 2026, whereas all experimental runs, repository mining, and other URL access dates in the manuscript are dated on or before May 2026 (or late 2025). This appears to be a typographical error for 28 August 2025.
    

CITATION & REFERENCE VERIFICATION

---

Citation Checker V2 Report

Summary

- Paper References Checked: 43
    
- Verified: 40
    
- Flagged (Likely Hallucinated): 3
    
- Unresolved: 0
    
- Skipped (Non-Paper): 6
    

References Details

❌ Reference 19: gradle2026gradle

- Final Verdict: Likely Hallucinated
    
- Lookup Verdict: Not Found
    
- Search Verdict: Hallucinated
    

Search Rationale:

There is no academic paper or formal publication titled 'Gradle build tool' authored by 'Gradle' in 2026. While Gradle Build Tool is a well-known open-source build automation tool, this citation appears to be a fabricated entry.

---

❌ Reference 25: jooq2025sql

- Final Verdict: Likely Hallucinated
    
- Lookup Verdict: Not Found
    
- Search Verdict: Hallucinated
    

Search Rationale:

The citation refers to 'SQL building' with the author given as 'jOOQ' (2025). No academic paper, report, or formal publication with the title 'SQL building' exists by this author; 'SQL building' is merely a section title within the official documentation/user manual of the jOOQ software library developed by Data Geekery GmbH.

---

❌ Reference 44: openrouter2026openrouter

- Final Verdict: Likely Hallucinated
    
- Lookup Verdict: Not Found
    
- Search Verdict: Hallucinated
    

Search Rationale:

No academic paper titled 'OpenRouter' exists. OpenRouter is an LLM routing service and API gateway platform (openrouter.ai), not an academic publication.

  
**
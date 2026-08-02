# Evidence Inventory

Status: initial extraction

This inventory records thesis material for the EMSE manuscript. It is intentionally selective: the target article is not a compressed thesis.

## Main Paper Evidence

| Evidence | Thesis source | Article role | Risk note |
|---|---|---|---|
| No public jOOQ SQL-antipattern dataset was available, motivating a new ground truth. | `thesis/chapters/03_dataset_creation.tex` | Study motivation and dataset contribution | Phrase as "to the best of our knowledge" unless a fresh literature check confirms stronger wording. |
| GitHub Code Search mining found 3,829 jOOQ dependency candidates on 10 January 2026; filtering yielded 802 projects with generated classes, 645 with non-generated jOOQ Java code, 603 after duplicate cleanup, and 602 for final analysis. | `thesis/chapters/03_dataset_creation.tex` | Repository mining method and data funnel | Explain GitHub API 1,000-result limit as a threat. |
| Stratified sampling used head-tail breaks over relevant database access files, with 47 small, 10 medium, and 4 large projects selected for annotation. | `thesis/chapters/03_dataset_creation.tex` | Sampling method | Use fixed seed and class thresholds for reproducibility. |
| Manual annotation produced 1,562 SQL-antipattern occurrences across 61 sampled projects. | `thesis/chapters/03_dataset_creation.tex` | Dataset contribution and ground truth | Single annotator must be acknowledged prominently. |
| Intra-annotator agreement after a 30-day washout yielded Cohen's Kappa 0.834 over 128 re-annotated files. | `thesis/chapters/03_dataset_creation.tex`; `thesis/chapters/08_analysis.tex` | Annotation consistency evidence | Do not present as inter-annotator agreement. |
| Seven qualifying antipatterns were retained for experiments after filtering out sparse classes. | `thesis/chapters/03_dataset_creation.tex` | Scope definition | Explain why the article covers 7 of 19 annotated antipatterns. |
| LLM evaluation is a multi-label, multi-occurrence localisation task using line-span IoU and F1-score. | `thesis/chapters/04_evaluation.tex` | Method novelty | Define IoU threshold clearly. |
| A prediction is a TP when IoU >= 0.5; NMS assigns only the highest-overlap prediction to each ground truth span. | `thesis/chapters/04_evaluation.tex` | Evaluation method | Useful differentiator from pure file-level classification. |
| Zero-shot prompting was selected for the final tool because complex prompts did not reliably improve performance and increased cost/runtime. | `thesis/chapters/07_results.tex` | Detector configuration rationale | Avoid claiming statistical superiority without tests. |
| Final localised detector using Claude Opus 4.5 achieved weighted F1 0.88 uncorrected and 0.93 corrected. | `thesis/chapters/07_results.tex` | Instrument validity | Corrected score is optimistic because corrections were tool-triggered. |
| Classification mode achieved weighted F1 0.88 uncorrected and 0.94 corrected. | `thesis/chapters/07_results.tex` | Comparison to localisation | Keep secondary; localisation is the article's methodological hook. |
| Large-scale run analysed 602 projects and 17,450 relevant files, costing USD 1,036.32 and taking 3h31m. | `thesis/chapters/07_results.tex` | Study scale and feasibility | Cost/runtime can support practical discussion. |
| The tool flagged 15,931 occurrences of seven antipatterns. | `thesis/chapters/07_results.tex` | Main empirical result | State as "flagged" or "detected" with detector limitations. |
| Implicit Columns and ID Required occurred in 535 and 523 projects, respectively, nearly 90% and 87% of projects. | `thesis/chapters/07_results.tex` | Main prevalence finding | Avoid extrapolating beyond open-source GitHub jOOQ projects. |
| Co-occurrence analysis used Jaccard, conditional probabilities, and Spearman at project and file levels. | `thesis/chapters/06_project_analysis.tex`; `thesis/chapters/07_results.tex` | Empirical analysis method/results | Large matrices likely supplementary. |
| Implicit Columns and ID Required form a high-prevalence pair with Jaccard 0.81 and Spearman 0.43. | `thesis/chapters/07_results.tex`; `thesis/chapters/08_analysis.tex` | Co-occurrence result | Clarify prevalence inflates Jaccard. |
| Keyless Entry and Fear of the Unknown form a lower-prevalence constraint-neglect cluster with Spearman 0.32. | `thesis/chapters/07_results.tex`; `thesis/chapters/08_analysis.tex` | Co-occurrence result | Keep interpretation cautious. |
| `selectFrom(TABLE)` and `select().from(TABLE)` account for nearly three quarters of Implicit Columns occurrences. | `thesis/chapters/07_results.tex`; `thesis/chapters/08_analysis.tex` | API association result | Frame as association, not causal proof. |
| `Field.like`, `likeIgnoreCase`, `containsIgnoreCase`, and `contains` dominate Poor Man's Search Engine occurrences. | `thesis/chapters/07_results.tex`; `thesis/chapters/08_analysis.tex` | API association result | Frame as developer/API usage pattern. |

## Supplementary Candidates

- Full prompt listings from `thesis/appendices/appendix-final-prompts.tex`.
- Full per-antipattern confusion matrices from classification and localisation appendices.
- Annotation decision trees from `thesis/figures/decision_tree_*.png`.
- Full Jaccard, Spearman, and conditional probability matrices.
- GitHub search terms and omitted-project details.
- Complete annotated-antipattern list and sparse antipattern classes.

## Discard or Heavily Compress

- Thesis outline and degree-program structure.
- Broad SQL, jOOQ, and LLM background that EMSE readers can be expected to know.
- Tool implementation architecture, TypeScript/Bun details, component diagrams, and workflow diagrams unless needed for artifact reproducibility.
- Reflection on work process and supervisor collaboration.
- Personal learning narrative.


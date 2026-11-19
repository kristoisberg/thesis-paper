# Replication materials

This directory contains the reconstruction scripts and generated tables for *LLM-Based SQL Antipattern Detection in jOOQ Code: An Occurrence-Level Evaluation and Repository Study*. This README indexes the frozen study materials and records the inputs, commands, and preservation limits needed to recompute the article's analyses.

Recomputation uses preserved reference annotations, parsed predictions, corpus flags, and retained source files. The detector revisions for the held-out and corpus runs preserve the source and embedded prompt templates. Exact replay remains limited by incomplete request and provider records and possible changes to the hosted model. The execution records below document surviving evidence and its limits.

## Resource index

The linked resources include the annotated class list, decision rules, prompts, and original experimental records. This README provides an entry point to those materials.

| Material | Frozen location |
|---|---|
| Repository mining | [GitHub search strings](https://github.com/kristoisberg/masters-thesis/blob/9913a7670fce52b135651f95ff18cd505c61b142/thesis/appendices/appendix-github-search-terms.tex), [omitted-project list](https://github.com/kristoisberg/masters-thesis/blob/9913a7670fce52b135651f95ff18cd505c61b142/thesis/appendices/appendix-omitted-projects.tex), and [mining notebooks](https://github.com/kristoisberg/masters-thesis/tree/9913a7670fce52b135651f95ff18cd505c61b142/scripts). |
| Annotation materials | [List of the 19 annotated antipatterns](https://github.com/kristoisberg/masters-thesis/blob/9913a7670fce52b135651f95ff18cd505c61b142/thesis/appendices/appendix-annotated-antipatterns.tex), [codebook decision trees](https://github.com/kristoisberg/masters-thesis/tree/9913a7670fce52b135651f95ff18cd505c61b142/diagrams/decision), and [reference datasets](https://github.com/kristoisberg/masters-thesis/tree/9913a7670fce52b135651f95ff18cd505c61b142/datasets). |
| Detector configuration | [Query and schema prompts](https://github.com/kristoisberg/masters-thesis/tree/9913a7670fce52b135651f95ff18cd505c61b142/prompts), [original thesis](https://github.com/kristoisberg/masters-thesis/tree/9913a7670fce52b135651f95ff18cd505c61b142/thesis), and [notebooks](https://github.com/kristoisberg/masters-thesis/tree/9913a7670fce52b135651f95ff18cd505c61b142/scripts) containing model-selection detail, per-class configuration results, and configuration options. |
| Evaluation and exploratory corpus analysis | [Frozen notebooks](https://github.com/kristoisberg/masters-thesis/tree/9913a7670fce52b135651f95ff18cd505c61b142/scripts) contain localisation and classification diagnostics, detector-informed sensitivity analysis, and co-detection matrices and heatmaps. [21-find-frequent-offenders.ipynb](https://github.com/kristoisberg/masters-thesis/blob/9913a7670fce52b135651f95ff18cd505c61b142/scripts/21-find-frequent-offenders.ipynb) contains the ordered source-fragment categorisation procedure and stored counts. |
| Article corpus analysis | [Corpus-normalisation script](https://github.com/kristoisberg/thesis-paper/blob/bb3bf6056cc7bbda29bb0fb5f0b720e7f9d06028/analysis/corpus_normalization.py), [class-level breadth and repetition](https://github.com/kristoisberg/thesis-paper/blob/bb3bf6056cc7bbda29bb0fb5f0b720e7f9d06028/analysis/corpus_phase2_class_summary.csv), [repository density](https://github.com/kristoisberg/thesis-paper/blob/bb3bf6056cc7bbda29bb0fb5f0b720e7f9d06028/analysis/corpus_phase3_density_summary.csv), [concentration decomposition](https://github.com/kristoisberg/thesis-paper/blob/bb3bf6056cc7bbda29bb0fb5f0b720e7f9d06028/analysis/corpus_phase3_concentration.csv), and [exact-content sensitivity](https://github.com/kristoisberg/thesis-paper/blob/bb3bf6056cc7bbda29bb0fb5f0b720e7f9d06028/analysis/corpus_phase4_exact_duplicate_sensitivity.csv). |
| Implementation | Architecture, workflow, output, and command-line configuration details accompany the [released detector source](https://github.com/kristoisberg/jooq-antipattern-detector/tree/cf82fe56acb728f076df67279ff4a78a138996f3) and [original thesis appendices](https://github.com/kristoisberg/masters-thesis/tree/9913a7670fce52b135651f95ff18cd505c61b142/thesis/appendices). |

## Frozen snapshots and preserved outputs

Immutable commits identify the preserved study, the detector revisions for the held-out and corpus runs, the later released implementation, and the article analyses. Their dates distinguish run-specific source revisions from later archive snapshots.

| Resource | Full revision and archive date | Preserved evidence and boundary |
|---|---|---|
| Study artefacts | [`9913a7670fce52b135651f95ff18cd505c61b142`](https://github.com/kristoisberg/masters-thesis/tree/9913a7670fce52b135651f95ff18cd505c61b142), 4 October 2026 | [`datasets/test-set.csv`](https://github.com/kristoisberg/masters-thesis/blob/9913a7670fce52b135651f95ff18cd505c61b142/datasets/test-set.csv) contains 523 original test references. The executed [`scripts/14-evaluate-tool-localisation.ipynb`](https://github.com/kristoisberg/masters-thesis/blob/9913a7670fce52b135651f95ff18cd505c61b142/scripts/14-evaluate-tool-localisation.ipynb) contains all 536 held-out predictions. [`datasets/analysis-results.csv`](https://github.com/kristoisberg/masters-thesis/blob/9913a7670fce52b135651f95ff18cd505c61b142/datasets/analysis-results.csv) contains all 15,931 positive corpus flags; [per-project positive outputs](https://github.com/kristoisberg/masters-thesis/tree/9913a7670fce52b135651f95ff18cd505c61b142/datasets/projects) also survive. |
| Held-out detector | [`80f3ff4eeabdc3fec860bc35bb9a4566fe130763`](https://github.com/kristoisberg/jooq-antipattern-detector/tree/80f3ff4eeabdc3fec860bc35bb9a4566fe130763), 4 April 2026 | Source, embedded prompts in [`src/prompts.ts`](https://github.com/kristoisberg/jooq-antipattern-detector/blob/80f3ff4eeabdc3fec860bc35bb9a4566fe130763/src/prompts.ts), prompt construction, and dependency lock file for the held-out run. |
| Corpus detector | [`245b50aa381d9917e5febf9f4ab0cd13d1b9d944`](https://github.com/kristoisberg/jooq-antipattern-detector/tree/245b50aa381d9917e5febf9f4ab0cd13d1b9d944), 14 April 2026 | Source and dependencies for the 15 April corpus run. The embedded prompt templates and prompt-construction code are identical to the held-out revision. |
| Released detector | [`cf82fe56acb728f076df67279ff4a78a138996f3`](https://github.com/kristoisberg/jooq-antipattern-detector/tree/cf82fe56acb728f076df67279ff4a78a138996f3), 26 May 2026 | Source, tests, [`package.json`](https://github.com/kristoisberg/jooq-antipattern-detector/blob/cf82fe56acb728f076df67279ff4a78a138996f3/package.json), and [`bun.lock`](https://github.com/kristoisberg/jooq-antipattern-detector/blob/cf82fe56acb728f076df67279ff4a78a138996f3/bun.lock). This later release is separate from the run-specific revisions listed above. |
| Article analyses | [`bb3bf6056cc7bbda29bb0fb5f0b720e7f9d06028`](https://github.com/kristoisberg/thesis-paper/tree/bb3bf6056cc7bbda29bb0fb5f0b720e7f9d06028/analysis), 12 September 2026 | [`localisation_robustness.py`](https://github.com/kristoisberg/thesis-paper/blob/bb3bf6056cc7bbda29bb0fb5f0b720e7f9d06028/analysis/localisation_robustness.py), [`corpus_concentration.py`](https://github.com/kristoisberg/thesis-paper/blob/bb3bf6056cc7bbda29bb0fb5f0b720e7f9d06028/analysis/corpus_concentration.py), [`corpus_normalization.py`](https://github.com/kristoisberg/thesis-paper/blob/bb3bf6056cc7bbda29bb0fb5f0b720e7f9d06028/analysis/corpus_normalization.py), and [`requirements.txt`](https://github.com/kristoisberg/thesis-paper/blob/bb3bf6056cc7bbda29bb0fb5f0b720e7f9d06028/analysis/requirements.txt) reproduce localisation robustness, source-frame reconstruction, normalised corpus measures, and exact-content sensitivity from the frozen study artefacts and retained source snapshot. |

The study-artefact revision restores the original Opus Zero-Shot validation notebook after a later rerun had replaced its stored outputs. The restored notebook is byte-identical to its version at `112f3a4eac5fcdb27f380102c1b296d946128ada`. All other tracked study files are unchanged from the earlier study archive at `d9b35e398a6deb544f913bdbc0b211ab38474a44`.

The preserved prediction tables contain the parsed class, file, span, code fragment, and explanation fields used in the analyses. Raw API response envelopes, request identifiers, negative-file outputs, failed responses, and complete request metadata were not archived. The source snapshot for the 602 analysed repositories survives without Git history. The [corpus source manifest](https://github.com/kristoisberg/thesis-paper/blob/bb3bf6056cc7bbda29bb0fb5f0b720e7f9d06028/analysis/corpus_source_manifest.csv) records a repository-relative path and SHA-256 content hash for each of the 17,988 selected files. It does not contain the Java source files, so source-based recomputation requires the retained source snapshot separately.

## Original model executions

The validation notebooks called [OpenRouter](https://openrouter.ai/) through the [OpenAI Python SDK](https://github.com/openai/openai-python). They preserve the following model slugs and settings.

| Model | Preserved slug | Generation settings and routing evidence |
|---|---|---|
| [GPT-5.2](https://deploymentsafety.openai.com/gpt-5-2/introduction) | `openai/gpt-5.2` | xhigh reasoning. Temperature adjustment was unsupported with this setting. Archived notebook requests nevertheless submitted temperature 0.0 to the gateway; its handling of that unsupported field was not recorded. |
| [GLM-5](https://doi.org/10.48550/ARXIV.2602.15763) | `z-ai/glm-5` | Temperature 0.0, with no reasoning-effort parameter because the effort level was not configurable. DeepInfra, which OpenRouter initially selected for GLM-5, had stability problems during the analysis. We therefore routed GLM-5 requests to Friendli and disabled provider fallbacks. |
| [Claude Opus 4.5](https://www-cdn.anthropic.com/bf10f64990cfda0ba858290be7b8cc6317685f47.pdf) | `anthropic/claude-opus-4.5` | Temperature 0.0 with reasoning disabled. |
| [gpt-oss-120B](https://doi.org/10.48550/ARXIV.2508.10925) | `openai/gpt-oss-120b` | High reasoning, with the temperature parameter omitted. The default temperature 1.0 was retained because near-zero temperatures caused repeated-token loops. Preserved response metadata reports temperature 1.0. |

Each combination of model and prompt ran once. The following dashboard records give the execution date in 2026 and aggregate retry count as date/retries. ZS denotes Zero-Shot, FS Few-Shot, CoT Chain-of-Thought, and ToT Tree-of-Thought. Retry totals count empty or failed responses repeated by the notebooks. Dashboard time-zone information was not saved.

| Prompt | GPT-5.2 | GLM-5 | Opus 4.5 | gpt-oss-120B |
|---|---|---|---|---|
| ZS | 6 Mar/1 | 6 Mar/175 | 7 Mar/0 | 7 Mar/0 |
| FS | 7 Mar/0 | 7 Mar/9 | 7 Mar/0 | 6 Mar/1 |
| CoT | 6 Mar/1 | 6 Mar/234 | 7 Mar/0 | 6 Mar/3 |
| ToT | 27 Mar/2 | 27 Mar/14 | 27 Mar/9 | 27 Mar/58 |

The [split-file inventory analysis](split_file_inventory.py) identifies 1,159 distinct relevant files in the validation partition. All 16 archived validation configurations record the same completed-file inventory.

Printed agreement, runtime, and cost summaries also survive. Agreement and runtime summaries reproduce the displayed configuration-selection values after rounding. The original [Opus Zero-Shot notebook](https://github.com/kristoisberg/masters-thesis/blob/9913a7670fce52b135651f95ff18cd505c61b142/scripts/backups/09-evaluate-prompting-strategy-opus-zs.ipynb), restored from revision `112f3a4eac5fcdb27f380102c1b296d946128ada`, records runtime 366.72 seconds, weighted precision/recall/F1 of 0.8836/0.8898/0.8839, and API cost $31.392120. These round to the article's 367 seconds, 0.88/0.89/0.88, and $31.39. The validation table uses charges reported by OpenRouter in US dollars. The reported costs are $31.39 for Opus Zero-Shot, $26.16 for GPT-5.2 Zero-Shot, $81.43 for Opus Tree-of-Thought, and $11.76 for GLM-5 Zero-Shot.

The held-out and corpus runs used `openrouter:anthropic/claude-opus-4.5`, temperature 0.0, reasoning disabled, and the Zero-Shot prompt family. The study author identified detector revisions [`80f3ff4`](https://github.com/kristoisberg/jooq-antipattern-detector/tree/80f3ff4eeabdc3fec860bc35bb9a4566fe130763) and [`245b50a`](https://github.com/kristoisberg/jooq-antipattern-detector/tree/245b50aa381d9917e5febf9f4ab0cd13d1b9d944) for these runs, respectively. Their commit dates are consistent with the recorded execution dates. Both revisions contain identical `src/prompts.ts` and `src/prompt-builder.ts` files.

| Execution | Dashboard record in 2026 | Requests and retry handling |
|---|---|---|
| Held-out test | 4 April, 15:00 | 502 requests for 502 files. The command allowed up to 1,000 retries per file. Equal request and file counts show no additional attempts in the dashboard total. |
| Corpus | 15 April, 08:00 through 12:00 | 18,051 requests. The command allowed two retries per file. This total exceeds the reconstructed 17,988-file frame by 63 requests, consistent with up to 63 repeated attempts. |

Per-request retry histories, final failure records, backend provider identifiers, and model snapshot identifiers are unavailable. The aggregate records cannot reconstruct each request's execution history.

The eight query and schema prompt files survive in [`prompts/zero-shot/`](https://github.com/kristoisberg/masters-thesis/tree/9913a7670fce52b135651f95ff18cd505c61b142/prompts/zero-shot), [`prompts/few-shot/`](https://github.com/kristoisberg/masters-thesis/tree/9913a7670fce52b135651f95ff18cd505c61b142/prompts/few-shot), [`prompts/chain-of-thought/`](https://github.com/kristoisberg/masters-thesis/tree/9913a7670fce52b135651f95ff18cd505c61b142/prompts/chain-of-thought), and [`prompts/tree-of-thought/`](https://github.com/kristoisberg/masters-thesis/tree/9913a7670fce52b135651f95ff18cd505c61b142/prompts/tree-of-thought). The validation notebooks load these files directly. The held-out and corpus prompt templates are preserved in [`src/prompts.ts`](https://github.com/kristoisberg/jooq-antipattern-detector/blob/80f3ff4eeabdc3fec860bc35bb9a4566fe130763/src/prompts.ts) at the run-specific detector revisions. These source templates and the prompt-construction code are byte-identical between the two revisions. The original compiled binaries and complete per-request payloads were not archived.

### Annotation and detector boundaries

The annotation codebook was refined across the 61 repositories before project partitioning. Later prompt iteration used training projects and configuration selection used validation projects. Test projects were excluded from those later stages, but the inherited operational definitions were sample-informed.

ID Required includes the standalone condition that a primary-key **column** is named `id`, ignoring case. It does not refer to the key constraint's name and does not require a visible alternative key for that branch. This broad screening condition is not itself proof of an unsuitable key design.

The annotation decision trees documented variants encountered in the sample; the prompts also covered relevant variants absent from it. In particular, regex search was included in the prompts although no such occurrence was found in the annotated sample. The following table distinguishes the written rules; broader prompt coverage alone does not establish an inconsistency in annotation:

| Class | Annotation decision tree | Detector instruction |
|---|---|---|
| Poor Man's Search Engine | LIKE/ILIKE and substring convenience methods, including negative variants, in SELECT/WHERE conditions. | Also includes regex and has no explicit SELECT/WHERE restriction. Both include unresolved wildcard behaviour conservatively and exclude prefix search. |
| Keyless Entry | Accepts a suitable referenced primary or unique key, considering names and types. | Imprecisely names only a primary key in the attached Keys context, omitting the intended unique-key variants. |
| 31 Flavors | Includes ranges encoding discrete business categories; excludes ordinary validity ranges and emptiness checks. CHECK occurrences are located at constraint-definition lines. | Its blanket range exclusion is overly broad. Its column-definition span instruction also omits the intended CHECK-constraint span. |
| Query-level Fear of the Unknown | Enumerates `notIn` and column self-equality. The author confirmed that annotation also checked nullability, although that requirement was implicit in the flowchart. | Also requires evidence that the affected column is nullable and excludes Java-only null handling. |

The author confirmed that validation contained neither Keyless Entry cases requiring a non-primary unique key nor category-encoding range cases for 31 Flavors, so validation did not expose those prompt imprecisions. For CHECK-based 31 Flavors occurrences, the intended span was the constraint definition, and the inspected model responses returned those spans despite the generic column-definition instruction. No frequency or class-specific performance effect is inferred from these qualitative observations.

For schema-level Fear of the Unknown, a nullable column with a non-NULL default is sufficient screening evidence; business logic may also establish practical non-nullability. A default does not prevent explicit NULL values, and business-logic context may be absent from the detector's single-file request. Table classes can expose ENUM evidence through `asEnumDataType` and CHECK expressions through `getChecks`, even though standalone EnumType implementations are excluded as target files.

These rules are directly inspectable in the versioned [decision trees](https://github.com/kristoisberg/masters-thesis/tree/9913a7670fce52b135651f95ff18cd505c61b142/diagrams/decision), [study prompt files](https://github.com/kristoisberg/masters-thesis/tree/9913a7670fce52b135651f95ff18cd505c61b142/prompts), and [embedded detector prompts](https://github.com/kristoisberg/jooq-antipattern-detector/blob/245b50aa381d9917e5febf9f4ab0cd13d1b9d944/src/prompts.ts). The embedded prompts match each other between held-out and corpus revisions. They are not byte-identical to the study Markdown templates: they use the label “Beware of the Unknown” and add user-facing explanation/fix instructions. The localisation analysis normalises that label to “Fear of the Unknown.”

### File selection and prompt construction

Both run-specific implementations use case-sensitive literal path/content tests, not Java parsing. Their 22 excluded path fragments, three inclusion terms (`org.jooq`, `Tables`, `tables`), and 22 excluded content signatures match the arrays in [corpus_normalization.py](corpus_normalization.py). A selected file receives the schema prompt and generated-schema role if it contains any of `This class is generated by jOOQ`, `extends TableImpl`, or `extends org.jooq.impl.TableImpl`; other selected files receive the query prompt and application/query role.

The implemented detector collects Keys candidates before target filtering from all loaded Java files containing the literal signature `public class Keys `, including its trailing space. It sorts relative paths and chooses the longest character-level common prefix with the target's repository-relative path. The first candidate resolves ties, with no minimum proximity threshold. No candidate yields empty key context. Only schema prompts attach this context. The exact rules are in [held-out file discovery](https://github.com/kristoisberg/jooq-antipattern-detector/blob/80f3ff4eeabdc3fec860bc35bb9a4566fe130763/src/file-discovery.ts) and [corpus file discovery](https://github.com/kristoisberg/jooq-antipattern-detector/blob/245b50aa381d9917e5febf9f4ab0cd13d1b9d944/src/file-discovery.ts).

The shared [budget resolver](https://github.com/kristoisberg/jooq-antipattern-detector/blob/245b50aa381d9917e5febf9f4ab0cd13d1b9d944/src/model.ts) gives the matched Claude model a default 240,000-character prompt budget, unless overridden. [Prompt construction](https://github.com/kristoisberg/jooq-antipattern-detector/blob/245b50aa381d9917e5febf9f4ab0cd13d1b9d944/src/prompt-builder.ts) subtracts template size, prioritises trimmed/numbered target source, and uses remaining space for trimmed Keys content. Oversized target content is shortened to head/tail lines with an omission marker where possible, otherwise to a prefix. Keys shortening preserves a prefix and appends an ellipsis. This is character-based capacity estimation, not exact token accounting. The source establishes the policy, not the number of affected requests or whether a runtime override was supplied.

Validation notebooks use a separate Python path: Keys candidates come from unsorted glob output, proximity uses `os.path.commonprefix` on full paths, and the prompt-loading code opens the chosen Keys file directly. They do not implement this detector's character budget or empty-context fallback. The held-out implementation decodes Latin-1; the corpus implementation tries strict UTF-8 and falls back to Latin-1. Thus identical embedded prompt templates do not establish identical preprocessing or complete request payloads. The older corpus counting notebook also searches under `src`, whereas detector execution and the article's file-normalised analysis discover Java files recursively throughout each repository.

### Validation evidence map

All 16 combinations of model and prompt were executed. The article displays seven rows: the four Zero-Shot configurations and the three other Claude Opus 4.5 prompts. The mapping below links each run to its preserved notebook. Each notebook records the same 1,159 completed files and 581 reference occurrences. These summaries are archived observations, not new model executions.

P, R, and F1 below are the printed reference-support-weighted scores. For precision, each validation prediction counts as covered if it overlaps any reference of the same class in the same file at line-span IoU 0.50 or higher. Recall applies the same rule to each reference span. These separate counts can reuse a span across matches. The held-out evaluation uses one-to-one matching. The article rounds the printed scores to two decimals and the batch runtime to whole seconds.

| Archived run | Article table row | P | R | F1 | Runtime (s) |
|---|---|---:|---:|---:|---:|
| [GPT-5.2 / Zero-Shot](https://github.com/kristoisberg/masters-thesis/blob/9913a7670fce52b135651f95ff18cd505c61b142/scripts/backups/09-evaluate-prompting-strategy-gpt5-zs.ipynb) | 1 | 0.8537 | 0.9225 | 0.8801 | 2423.31 |
| [GPT-5.2 / Few-Shot](https://github.com/kristoisberg/masters-thesis/blob/9913a7670fce52b135651f95ff18cd505c61b142/scripts/backups/09-evaluate-prompting-strategy-gpt5-fs.ipynb) | Not displayed | 0.8593 | 0.9243 | 0.8830 | 2506.91 |
| [GPT-5.2 / Chain-of-Thought](https://github.com/kristoisberg/masters-thesis/blob/9913a7670fce52b135651f95ff18cd505c61b142/scripts/backups/09-evaluate-prompting-strategy-gpt5-cot.ipynb) | Not displayed | 0.8462 | 0.9139 | 0.8730 | 2896.33 |
| [GPT-5.2 / Tree-of-Thought-inspired](https://github.com/kristoisberg/masters-thesis/blob/9913a7670fce52b135651f95ff18cd505c61b142/scripts/backups/09-evaluate-prompting-strategy-gpt5-tot.ipynb) | Not displayed | 0.8706 | 0.9139 | 0.8873 | 4701.55 |
| [GLM-5 / Zero-Shot](https://github.com/kristoisberg/masters-thesis/blob/9913a7670fce52b135651f95ff18cd505c61b142/scripts/backups/09-evaluate-prompting-strategy-glm5-zs.ipynb) | 2 | 0.8837 | 0.8933 | 0.8768 | 5774.14 |
| [GLM-5 / Few-Shot](https://github.com/kristoisberg/masters-thesis/blob/9913a7670fce52b135651f95ff18cd505c61b142/scripts/backups/09-evaluate-prompting-strategy-glm5-fs.ipynb) | Not displayed | 0.8938 | 0.9002 | 0.8882 | 4280.87 |
| [GLM-5 / Chain-of-Thought](https://github.com/kristoisberg/masters-thesis/blob/9913a7670fce52b135651f95ff18cd505c61b142/scripts/backups/09-evaluate-prompting-strategy-glm5-cot.ipynb) | Not displayed | 0.8709 | 0.8847 | 0.8654 | 9628.06 |
| [GLM-5 / Tree-of-Thought-inspired](https://github.com/kristoisberg/masters-thesis/blob/9913a7670fce52b135651f95ff18cd505c61b142/scripts/backups/09-evaluate-prompting-strategy-glm5-tot.ipynb) | Not displayed | 0.9150 | 0.8812 | 0.8730 | 5358.76 |
| [Claude Opus 4.5 / Zero-Shot](https://github.com/kristoisberg/masters-thesis/blob/9913a7670fce52b135651f95ff18cd505c61b142/scripts/backups/09-evaluate-prompting-strategy-opus-zs.ipynb) | 3 | 0.8836 | 0.8898 | 0.8839 | 366.72 |
| [Claude Opus 4.5 / Few-Shot](https://github.com/kristoisberg/masters-thesis/blob/9913a7670fce52b135651f95ff18cd505c61b142/scripts/backups/09-evaluate-prompting-strategy-opus-fs.ipynb) | 5 | 0.8800 | 0.8881 | 0.8803 | 351.81 |
| [Claude Opus 4.5 / Chain-of-Thought](https://github.com/kristoisberg/masters-thesis/blob/9913a7670fce52b135651f95ff18cd505c61b142/scripts/backups/09-evaluate-prompting-strategy-opus-cot.ipynb) | 6 | 0.9248 | 0.9002 | 0.9030 | 955.93 |
| [Claude Opus 4.5 / Tree-of-Thought-inspired](https://github.com/kristoisberg/masters-thesis/blob/9913a7670fce52b135651f95ff18cd505c61b142/scripts/backups/09-evaluate-prompting-strategy-opus-tot.ipynb) | 7 | 0.9199 | 0.8967 | 0.9007 | 4700.71 |
| [gpt-oss-120B / Zero-Shot](https://github.com/kristoisberg/masters-thesis/blob/9913a7670fce52b135651f95ff18cd505c61b142/scripts/backups/09-evaluate-prompting-strategy-oss-zs.ipynb) | 4 | 0.8262 | 0.8692 | 0.8339 | 2808.35 |
| [gpt-oss-120B / Few-Shot](https://github.com/kristoisberg/masters-thesis/blob/9913a7670fce52b135651f95ff18cd505c61b142/scripts/backups/09-evaluate-prompting-strategy-oss-fs.ipynb) | Not displayed | 0.8264 | 0.8675 | 0.8396 | 543.45 |
| [gpt-oss-120B / Chain-of-Thought](https://github.com/kristoisberg/masters-thesis/blob/9913a7670fce52b135651f95ff18cd505c61b142/scripts/backups/09-evaluate-prompting-strategy-oss-cot.ipynb) | Not displayed | 0.8059 | 0.8520 | 0.8207 | 894.59 |
| [gpt-oss-120B / Tree-of-Thought-inspired](https://github.com/kristoisberg/masters-thesis/blob/9913a7670fce52b135651f95ff18cd505c61b142/scripts/backups/09-evaluate-prompting-strategy-oss-tot.ipynb) | Not displayed | 0.8101 | 0.8262 | 0.8134 | 2138.84 |

The article cost column uses OpenRouter-reported charges confirmed by the study author during the October archive restoration. Notebook-summed response costs are a separate record and do not always equal those charges. The following mapping preserves both sources without replacing the article costs. The author confirmation and restoration checks are recorded in [the October restoration report](../.review/2026-10-04-opus-original-run-restoration.md).

| Article table row | Configuration | OpenRouter charge used in article (USD) | Printed notebook cost (USD) |
|---|---|---:|---:|
| 1 | GPT-5.2 / Zero-Shot | 26.16 | 26.077763 |
| 2 | GLM-5 / Zero-Shot | 11.76 | 10.950958 |
| 3 | Claude Opus 4.5 / Zero-Shot | 31.39 | 31.392120 |
| 4 | gpt-oss-120B / Zero-Shot | 1.49 | 1.493565 |
| 5 | Claude Opus 4.5 / Few-Shot | 45.00 | 44.999000 |
| 6 | Claude Opus 4.5 / Chain-of-Thought | 40.86 | 40.862095 |
| 7 | Claude Opus 4.5 / Tree-of-Thought-inspired | 81.43 | 80.850875 |

## Dependencies and recomputation

The original data processing and evaluations used [Jupyter notebooks](https://jupyter.org/). The archive contains 26 top-level notebooks and 16 backups for combinations of model and prompt. Notebook metadata records Python 3.14.3 in 38 notebooks and Python 3.13.5 in four backups. The notebooks import NumPy, pandas, scikit-learn, matplotlib, seaborn, the OpenAI Python SDK, Pydantic, and `requests_async`. The original environment has no requirements or lock file, so its exact package versions are unavailable.

Both run-specific detector revisions record Bun 1.2.21 in `package.json` and preserve the same JavaScript dependency lock file, `bun.lock`. These files document the intended dependencies; the installed runtime environment was not archived. The article's reconstruction scripts were verified separately with Python 3.14.7. Their direct third-party dependencies are pinned in [requirements.txt](requirements.txt). The corpus-normalisation script uses the Python standard library.

Run the commands below from the article repository root. Replace `/path/to/masters-thesis` with a checkout of the frozen study-artefact revision and `/path/to/repositories` with the retained repository-source snapshot. Keep the frozen study directory structure intact because the corpus-normalisation script locates notebooks and per-project outputs relative to the dataset paths.

### Localisation robustness

This command requires `datasets/test-set.csv` and the executed `scripts/14-evaluate-tool-localisation.ipynb` with its stored HTML prediction table. Install the pinned dependencies in `analysis/requirements.txt` before running it.

```bash
python analysis/localisation_robustness.py /path/to/masters-thesis \
  --bootstrap 10000 --seed 123456
```

It reconstructs all 536 held-out predictions, reproduces the primary 460 true positives, 76 false positives, and 63 false negatives, evaluates four intersection-over-union thresholds, and runs the 10,000-iteration project bootstrap with seed 123456. The output reports defined-replicate counts for each metric separately, both pooled and by class. Percentiles use only replicates with a defined value for the corresponding metric.

### Repeat-annotation recount

The repeat-annotation exercise used the original 19-class codebook across 128 files; 15 classes occur in the union of both passes. Of the 64 originally unannotated files, 63 remained unannotated. Recompute the exact labelled-event comparison without model requests or new annotations:

```bash
python analysis/repeat_annotation_check.py /path/to/masters-thesis \
  > analysis/repeat_annotation_summary.json
```

The standard-library script reads `datasets/files-to-reannotate.csv`, `datasets/ground-truth.csv`, and `datasets/reannotated-ground-truth.csv`. The [summary](repeat_annotation_summary.json) records input hashes and the full recount. Multiset intersection by project, file, class, and inclusive span yields 144 matches among 158 original and 149 repeated events: precision 0.966, recall 0.911, and F1 0.938.

The script also replays the archived notebook's span-first procedure, reproducing its historical 142 same-class pairs. At line 99 of `boogiespook/waltz-test`'s `EntityStatisticDefinition.java`, both passes contain Keyless Entry and Naive Trees, but the row order reverses. The span-first procedure cross-pairs these labels and creates two artificial disagreements. The article corrects this calculation without changing the frozen annotation files. This correction concerns repeat-annotation reliability; held-out detector counts remain 460 TP, 76 FP, and 63 FN.

### Detector-informed revised counts

The frozen `scripts/15-calculate-tool-localisation-corrected.ipynb` stores revised class-level TP/FP/FN aggregates supplied to its metric function. The seven rows sum to 512 TP, 24 FP, and 51 FN, implying reference support of 563 and pooled micro F1 0.931756. The reference-support-weighted F1 is a distinct value, 0.930902. The event-level revised reference and a record of individual changes were not retained, so the aggregates cannot establish which specific annotation was added, removed, or remapped. They support an optimistic, detector-informed count sensitivity rather than a reconstructable replacement dataset.

### Corpus sensitivity by annotation-sample membership

The [subset comparison](corpus_sample_sensitivity.csv) joins the existing per-repository corpus counts to the 61 annotated repositories listed in the split inventory. It pools eligible files, flagged files, and flags separately over the annotated subset, the other 541 repositories, and the full corpus. Rates use the pooled counts and are blank when their denominator is zero. The all-class rows also give flag counts by source role, which can be divided by the corresponding eligible-file counts in the ID Required and Implicit Columns rows to compare density within each role.

```bash
python analysis/corpus_sample_sensitivity.py > analysis/corpus_sample_sensitivity.csv
```

### Original repository concentration

This command requires the frozen `datasets/analysis-results.csv` containing the 15,931 corpus flags.

```bash
python analysis/corpus_concentration.py \
  /path/to/masters-thesis/datasets/analysis-results.csv \
  --verify-frozen
```

It verifies the frozen CSV hash and reproduces the original class-level repository-concentration results.

### Corpus normalisation and exact-content sensitivity

This command requires the retained source snapshot, the frozen allowlist `datasets/final-repositories-corrected.csv`, the frozen corpus flags `datasets/analysis-results.csv`, and per-project positive outputs under `datasets/projects/`. Source directories must retain the original layout, with `owner/repository` names represented as `owner_repository`. The script checks that all 602 allowlisted directories and the original 43 excluded directories are present, and verifies its selection rules against the frozen study notebooks under `scripts/`.

The public source manifest provides file identities and hashes; it cannot substitute for the retained Java source snapshot.

```bash
python analysis/corpus_normalization.py /path/to/repositories \
  /path/to/masters-thesis/datasets/final-repositories-corrected.csv \
  /path/to/masters-thesis/datasets/analysis-results.csv \
  --output-dir analysis
```

It scans the retained source snapshot, verifies the allowlist and frozen flags, reconstructs the 17,988-file frame, and writes all normalisation artefacts for Phases 1 through 4. Every phase has assertion-based acceptance checks and a JSON summary recording methods and checksums. These commands recompute analyses from preserved evidence without making model calls.

### Training, validation, and test file counts

The [split-file inventory analysis](split_file_inventory.py) applies recursive `**/*.java` discovery and the corpus path/content filters to the projects in the three frozen split CSVs. It counts each repository-relative path once. Byte-identical files at different paths remain distinct file occurrences; their collapsed counts are reported separately.

```bash
python analysis/split_file_inventory.py /path/to/repositories \
  /path/to/masters-thesis --output-dir analysis
```

This standard-library script requires the retained source snapshot, `datasets/training-set.csv`, `datasets/validation-set.csv`, `datasets/test-set.csv`, the frozen allowlist, the frozen study notebooks under `scripts/`, all 16 validation backups, and the frozen `analysis/corpus_source_manifest.csv`. It verifies project membership, selection rules, every selected file's content hash and metadata against that manifest, and equality of all 16 archived completed-file inventories with the selected validation files. It makes no model requests.

| Partition | Repositories | Distinct relevant paths | Unique file contents |
|---|---:|---:|---:|
| Training | 21 | 509 | 476 |
| Validation | 20 | 1,159 | 1,141 |
| Test | 20 | 502 | 502 |

Training has 33 groups of byte-identical files containing 66 paths; validation has 13 groups containing 31 paths; test has none. No byte-identical file group crosses partitions. This check does not detect modified clones.

The annotation frame is distinct from the selected source frame. The split CSVs contain 332, 581, and 523 retained-class reference events across 145, 276, and 195 annotated paths, respectively. All training and validation annotated paths belong to the selected frame. Two test-reference paths do not, each carrying one reference event. In `jOOQ/jOOQ-mcve`, the overbroad `mysql/tables` blacklist excludes an annotated application table. In `therepanic/trustwin-casino-project`, an extra annotation uses the wrong module path, `game-overgo-service`; the original reference already contains the corresponding ID Required event at line 56 under the correct `game-miner-service` path. The thesis reports removing invalid reference occurrences in its corrected analysis, but the corrected notebook preserves aggregate counts rather than an event-level revision, so removal of this particular extra annotation cannot be verified from that notebook. This audit does not alter the frozen annotations, selection rules, or matching results.

Both out-of-frame references are unmatched and remain among the 63 primary false negatives. The two SQLite-module paths ending in `h2/tables/Test.java` and `sqlite/tables/Test.java` are separate files in the frozen manifest with different hashes; both have exact matching predictions. Their unusual names do not establish an annotation error. Full-source semantic reinspection was unavailable during the November reconciliation. The late removal of `Davincii254/Stroom` from the 603-project list did not affect any of the 61 annotated repositories or their partitions.

The outputs are [split-level counts](split_file_counts.csv), [per-repository counts](split_file_counts_by_repository.csv), the [2,170-path source manifest](split_source_manifest.csv), [duplicate glob matches](split_duplicate_glob_matches.csv), [cross-partition exact duplicates](split_cross_partition_exact_duplicates.csv), and [annotation-frame exceptions](split_annotation_frame_exceptions.csv). The two duplicate tables contain headers only because no matches were found. The [JSON summary](split_file_inventory_summary.json) records checks, input hashes, and output hashes. Its `all_annotations_in_source_frame` check is false because the two test exceptions are retained explicitly.

## Corpus-normalisation artefacts and checksums

The following SHA-256 values identify the generated CSV files at article-analysis commit `bb3bf6056cc7bbda29bb0fb5f0b720e7f9d06028`. The [frozen analysis directory](https://github.com/kristoisberg/thesis-paper/tree/bb3bf6056cc7bbda29bb0fb5f0b720e7f9d06028/analysis) also contains JSON summaries for Phases 1 through 4, input hashes, the selection-rule digest, methods, and acceptance checks.

| Artefact | SHA-256 |
|---|---|
| [corpus_source_manifest.csv](https://github.com/kristoisberg/thesis-paper/blob/bb3bf6056cc7bbda29bb0fb5f0b720e7f9d06028/analysis/corpus_source_manifest.csv) | `8200f8990215912efba90a4f5ed431d52c79d7b20e11ce496457f34829c8a214` |
| [corpus_flag_alignment.csv](https://github.com/kristoisberg/thesis-paper/blob/bb3bf6056cc7bbda29bb0fb5f0b720e7f9d06028/analysis/corpus_flag_alignment.csv) | `b035fd06e7c829da8f995770e769c7d3491d0d32794837ddc2191f960f78c728` |
| [corpus_phase2_by_repository.csv](https://github.com/kristoisberg/thesis-paper/blob/bb3bf6056cc7bbda29bb0fb5f0b720e7f9d06028/analysis/corpus_phase2_by_repository.csv) | `a88de1ee4719d1f8290d1418940a11151fb7cbe443023895002141493e4352a2` |
| [corpus_phase2_class_summary.csv](https://github.com/kristoisberg/thesis-paper/blob/bb3bf6056cc7bbda29bb0fb5f0b720e7f9d06028/analysis/corpus_phase2_class_summary.csv) | `7a91098968dc2b20afd86edf3cc505c2cd21fcd220818e5888a7c144639e451b` |
| [corpus_phase3_density_summary.csv](https://github.com/kristoisberg/thesis-paper/blob/bb3bf6056cc7bbda29bb0fb5f0b720e7f9d06028/analysis/corpus_phase3_density_summary.csv) | `598681f34f558054c2b6cb9f92daac656e8dfb2f76a5e85069ad2a9866236334` |
| [corpus_phase3_concentration.csv](https://github.com/kristoisberg/thesis-paper/blob/bb3bf6056cc7bbda29bb0fb5f0b720e7f9d06028/analysis/corpus_phase3_concentration.csv) | `7a5c900e7d22e3e638a7d12960203ee239902e175345f1d0a3d5a41ecb1fd2c9` |
| [corpus_phase4_exact_duplicate_sensitivity.csv](https://github.com/kristoisberg/thesis-paper/blob/bb3bf6056cc7bbda29bb0fb5f0b720e7f9d06028/analysis/corpus_phase4_exact_duplicate_sensitivity.csv) | `15c16d4e23a18faa68dbe3fe9c5f931d7620f0194650f04c226e351fb985355d` |

# Replication materials

This directory contains the reconstruction scripts and generated tables for *LLM-Based SQL Antipattern Detection in jOOQ Code: An Occurrence-Level Evaluation and Repository Study*. This README indexes the frozen study materials and records the inputs, commands, and preservation limits needed to recompute the article's analyses.

Recomputation uses preserved reference annotations, parsed predictions, corpus flags, and retained source files. Replay of the original model executions remains unavailable because the archive lacks the detector revision used, complete request records, and the prompts embedded in the original run binary. The execution records below document surviving evidence and its limits.

## Resource index

The linked resources include the annotated class list, decision rules, prompts, and original experimental records. This README provides an entry point to those materials.

| Material | Frozen location |
|---|---|
| Repository mining | [GitHub search strings](https://github.com/kristoisberg/masters-thesis/blob/d9b35e398a6deb544f913bdbc0b211ab38474a44/thesis/appendices/appendix-github-search-terms.tex), [omitted-project list](https://github.com/kristoisberg/masters-thesis/blob/d9b35e398a6deb544f913bdbc0b211ab38474a44/thesis/appendices/appendix-omitted-projects.tex), and [mining notebooks](https://github.com/kristoisberg/masters-thesis/tree/d9b35e398a6deb544f913bdbc0b211ab38474a44/scripts). |
| Annotation materials | [List of the 19 annotated antipatterns](https://github.com/kristoisberg/masters-thesis/blob/d9b35e398a6deb544f913bdbc0b211ab38474a44/thesis/appendices/appendix-annotated-antipatterns.tex), [codebook decision trees](https://github.com/kristoisberg/masters-thesis/tree/d9b35e398a6deb544f913bdbc0b211ab38474a44/diagrams/decision), and [reference datasets](https://github.com/kristoisberg/masters-thesis/tree/d9b35e398a6deb544f913bdbc0b211ab38474a44/datasets). |
| Detector configuration | [Query and schema prompts](https://github.com/kristoisberg/masters-thesis/tree/d9b35e398a6deb544f913bdbc0b211ab38474a44/prompts), [original thesis](https://github.com/kristoisberg/masters-thesis/tree/d9b35e398a6deb544f913bdbc0b211ab38474a44/thesis), and [notebooks](https://github.com/kristoisberg/masters-thesis/tree/d9b35e398a6deb544f913bdbc0b211ab38474a44/scripts) containing model-selection detail, per-class configuration results, and configuration options. |
| Evaluation and exploratory corpus analysis | [Frozen notebooks](https://github.com/kristoisberg/masters-thesis/tree/d9b35e398a6deb544f913bdbc0b211ab38474a44/scripts) contain localisation and classification diagnostics, detector-informed sensitivity analysis, and co-detection matrices and heatmaps. [21-find-frequent-offenders.ipynb](https://github.com/kristoisberg/masters-thesis/blob/d9b35e398a6deb544f913bdbc0b211ab38474a44/scripts/21-find-frequent-offenders.ipynb) contains the ordered source-fragment categorisation procedure and stored counts. |
| Article corpus analysis | [Corpus-normalisation script](https://github.com/kristoisberg/thesis-paper/blob/bb3bf6056cc7bbda29bb0fb5f0b720e7f9d06028/analysis/corpus_normalization.py), [class-level breadth and repetition](https://github.com/kristoisberg/thesis-paper/blob/bb3bf6056cc7bbda29bb0fb5f0b720e7f9d06028/analysis/corpus_phase2_class_summary.csv), [repository density](https://github.com/kristoisberg/thesis-paper/blob/bb3bf6056cc7bbda29bb0fb5f0b720e7f9d06028/analysis/corpus_phase3_density_summary.csv), [concentration decomposition](https://github.com/kristoisberg/thesis-paper/blob/bb3bf6056cc7bbda29bb0fb5f0b720e7f9d06028/analysis/corpus_phase3_concentration.csv), and [exact-content sensitivity](https://github.com/kristoisberg/thesis-paper/blob/bb3bf6056cc7bbda29bb0fb5f0b720e7f9d06028/analysis/corpus_phase4_exact_duplicate_sensitivity.csv). |
| Implementation | Architecture, workflow, output, and command-line configuration details accompany the [released detector source](https://github.com/kristoisberg/jooq-antipattern-detector/tree/cf82fe56acb728f076df67279ff4a78a138996f3) and [original thesis appendices](https://github.com/kristoisberg/masters-thesis/tree/d9b35e398a6deb544f913bdbc0b211ab38474a44/thesis/appendices). |

## Frozen snapshots and preserved outputs

Three immutable commits identify the preserved study, released implementation, and article analyses. Their dates distinguish when each snapshot was archived from when the experiments ran.

| Resource | Full revision and archive date | Preserved evidence and boundary |
|---|---|---|
| Study artefacts | [`d9b35e398a6deb544f913bdbc0b211ab38474a44`](https://github.com/kristoisberg/masters-thesis/tree/d9b35e398a6deb544f913bdbc0b211ab38474a44), 24 May 2026 | [`datasets/test-set.csv`](https://github.com/kristoisberg/masters-thesis/blob/d9b35e398a6deb544f913bdbc0b211ab38474a44/datasets/test-set.csv) contains 523 original test references. The executed [`scripts/14-evaluate-tool-localisation.ipynb`](https://github.com/kristoisberg/masters-thesis/blob/d9b35e398a6deb544f913bdbc0b211ab38474a44/scripts/14-evaluate-tool-localisation.ipynb) contains all 536 held-out predictions. [`datasets/analysis-results.csv`](https://github.com/kristoisberg/masters-thesis/blob/d9b35e398a6deb544f913bdbc0b211ab38474a44/datasets/analysis-results.csv) contains all 15,931 positive corpus flags; [per-project positive outputs](https://github.com/kristoisberg/masters-thesis/tree/d9b35e398a6deb544f913bdbc0b211ab38474a44/datasets/projects) also survive. |
| Released detector | [`cf82fe56acb728f076df67279ff4a78a138996f3`](https://github.com/kristoisberg/jooq-antipattern-detector/tree/cf82fe56acb728f076df67279ff4a78a138996f3), 26 May 2026 | Source, tests, [`package.json`](https://github.com/kristoisberg/jooq-antipattern-detector/blob/cf82fe56acb728f076df67279ff4a78a138996f3/package.json), and [`bun.lock`](https://github.com/kristoisberg/jooq-antipattern-detector/blob/cf82fe56acb728f076df67279ff4a78a138996f3/bun.lock). This release postdates the April executions and does not identify the binary used for those runs. |
| Article analyses | [`bb3bf6056cc7bbda29bb0fb5f0b720e7f9d06028`](https://github.com/kristoisberg/thesis-paper/tree/bb3bf6056cc7bbda29bb0fb5f0b720e7f9d06028/analysis), 12 September 2026 | [`localisation_robustness.py`](https://github.com/kristoisberg/thesis-paper/blob/bb3bf6056cc7bbda29bb0fb5f0b720e7f9d06028/analysis/localisation_robustness.py), [`corpus_concentration.py`](https://github.com/kristoisberg/thesis-paper/blob/bb3bf6056cc7bbda29bb0fb5f0b720e7f9d06028/analysis/corpus_concentration.py), [`corpus_normalization.py`](https://github.com/kristoisberg/thesis-paper/blob/bb3bf6056cc7bbda29bb0fb5f0b720e7f9d06028/analysis/corpus_normalization.py), and [`requirements.txt`](https://github.com/kristoisberg/thesis-paper/blob/bb3bf6056cc7bbda29bb0fb5f0b720e7f9d06028/analysis/requirements.txt) reproduce localisation robustness, source-frame reconstruction, normalised corpus measures, and exact-content sensitivity from the frozen study artefacts and retained source snapshot. |

The article-analysis commit predates this README. Its links identify the previously frozen scripts and tables; they do not identify a public version of this new documentation.

The preserved prediction tables contain the parsed class, file, span, code fragment, and explanation fields used in the analyses. Raw API response envelopes, request identifiers, negative-file outputs, failed responses, and complete request metadata were not archived. The source snapshot for the 602 analysed repositories survives without Git history. The [corpus source manifest](https://github.com/kristoisberg/thesis-paper/blob/bb3bf6056cc7bbda29bb0fb5f0b720e7f9d06028/analysis/corpus_source_manifest.csv) records a repository-relative path and SHA-256 content hash for each of the 17,988 selected files. It does not contain the Java source files, so source-based recomputation requires the retained source snapshot separately.

## Original model executions

The validation notebooks called [OpenRouter](https://openrouter.ai/) through the [OpenAI Python SDK](https://github.com/openai/openai-python). They preserve the following model slugs and settings.

| Model | Preserved slug | Generation settings and routing evidence |
|---|---|---|
| [GPT-5.2](https://deploymentsafety.openai.com/gpt-5-2/introduction) | `openai/gpt-5.2` | xhigh reasoning. Temperature adjustment was unsupported with this setting. Archived notebook requests nevertheless submitted temperature 0.0 to the gateway; its handling of that unsupported field was not recorded. |
| [GLM-5](https://doi.org/10.48550/ARXIV.2602.15763) | `z-ai/glm-5` | Temperature 0.0, with no reasoning-effort parameter because the effort level was not configurable. Requests fixed Friendli as the backend and disabled fallbacks. |
| [Claude Opus 4.5](https://www-cdn.anthropic.com/bf10f64990cfda0ba858290be7b8cc6317685f47.pdf) | `anthropic/claude-opus-4.5` | Temperature 0.0 with reasoning disabled. |
| [gpt-oss-120B](https://doi.org/10.48550/ARXIV.2508.10925) | `openai/gpt-oss-120b` | High reasoning, with the temperature parameter omitted. The default temperature 1.0 was retained because near-zero temperatures caused repeated-token loops. Preserved response metadata reports temperature 1.0. |

Each combination of model and prompt ran once. The following dashboard records give the execution date in 2026 and aggregate retry count as date/retries. ZS denotes Zero-Shot, FS Few-Shot, CoT Chain-of-Thought, and ToT Tree-of-Thought. Retry totals count empty or failed responses repeated by the notebooks. Dashboard time-zone information was not saved.

| Prompt | GPT-5.2 | GLM-5 | Opus 4.5 | gpt-oss-120B |
|---|---|---|---|---|
| ZS | 6 Mar/1 | 6 Mar/175 | 7 Mar/0 | 7 Mar/0 |
| FS | 7 Mar/0 | 7 Mar/9 | 7 Mar/0 | 6 Mar/1 |
| CoT | 6 Mar/1 | 6 Mar/234 | 7 Mar/0 | 6 Mar/3 |
| ToT | 27 Mar/2 | 27 Mar/14 | 27 Mar/9 | 27 Mar/58 |

The surviving validation notebook copies process 1,159 files. The article's originally reported validation table uses 823 files, and its exact underlying run outputs are unavailable. The surviving copies do not reproduce that table's file count, costs, or runtimes. The dates and retry totals above therefore do not establish that the archived copies produced the reported validation results.

The held-out and corpus runs used `openrouter:anthropic/claude-opus-4.5`, temperature 0.0, reasoning disabled, and the Zero-Shot prompt family.

| Execution | Dashboard record in 2026 | Requests and retry handling |
|---|---|---|
| Held-out test | 4 April, 15:00 | 502 requests for 502 files. The command allowed up to 1,000 retries per file. Equal request and file counts show no additional attempts in the dashboard total. |
| Corpus | 15 April, 08:00 through 12:00 | 18,051 requests. The command allowed two retries per file. This total exceeds the reconstructed 17,988-file frame by 63 requests, consistent with up to 63 repeated attempts. |

Per-request retry histories, final failure records, backend provider identifiers, and model snapshot identifiers are unavailable. The aggregate records cannot reconstruct each request's execution history.

The eight query and schema prompt files survive in [`prompts/zero-shot/`](https://github.com/kristoisberg/masters-thesis/tree/d9b35e398a6deb544f913bdbc0b211ab38474a44/prompts/zero-shot), [`prompts/few-shot/`](https://github.com/kristoisberg/masters-thesis/tree/d9b35e398a6deb544f913bdbc0b211ab38474a44/prompts/few-shot), [`prompts/chain-of-thought/`](https://github.com/kristoisberg/masters-thesis/tree/d9b35e398a6deb544f913bdbc0b211ab38474a44/prompts/chain-of-thought), and [`prompts/tree-of-thought/`](https://github.com/kristoisberg/masters-thesis/tree/d9b35e398a6deb544f913bdbc0b211ab38474a44/prompts/tree-of-thought). The validation notebooks load these files directly. The held-out and corpus runs used prompts embedded in an unarchived binary, so byte identity with the preserved Zero-Shot files cannot be established.

## Dependencies and recomputation

The original data processing and evaluations used [Jupyter notebooks](https://jupyter.org/). The archive contains 26 top-level notebooks and 16 backups for combinations of model and prompt. Notebook metadata records Python 3.14.3 in 38 notebooks and Python 3.13.5 in four backups. The notebooks import NumPy, pandas, scikit-learn, matplotlib, seaborn, the OpenAI Python SDK, Pydantic, and `requests_async`. The original environment has no requirements or lock file, so its exact package versions are unavailable.

The released detector records Bun 1.2.21 and pins its JavaScript dependency graph in `bun.lock`. That later release cannot establish the original run environment. The article's reconstruction scripts were verified separately with Python 3.14.7. Their direct third-party dependencies are pinned in [requirements.txt](requirements.txt). The corpus-normalisation script uses the Python standard library.

Run the commands below from the article repository root. Replace `/path/to/masters-thesis` with a checkout of the frozen study-artefact revision and `/path/to/repositories` with the retained repository-source snapshot. Keep the frozen study directory structure intact because the corpus-normalisation script locates notebooks and per-project outputs relative to the dataset paths.

### Localisation robustness

This command requires `datasets/test-set.csv` and the executed `scripts/14-evaluate-tool-localisation.ipynb` with its stored HTML prediction table. Install the pinned dependencies in `analysis/requirements.txt` before running it.

```bash
python analysis/localisation_robustness.py /path/to/masters-thesis \
  --bootstrap 10000 --seed 123456
```

It reconstructs all 536 held-out predictions, reproduces the primary 460 true positives, 76 false positives, and 63 false negatives, evaluates four intersection-over-union thresholds, and runs the 10,000-iteration project bootstrap with seed 123456.

### Original repository concentration

This command requires the frozen `datasets/analysis-results.csv` containing the 15,931 corpus flags.

```bash
python analysis/corpus_concentration.py \
  /path/to/masters-thesis/datasets/analysis-results.csv \
  --verify-frozen
```

It verifies the frozen CSV hash and reproduces the original class-level repository-concentration results.

### Corpus normalisation and exact-content sensitivity

This command requires the retained source snapshot, the frozen allowlist `datasets/final-repositories-corrected.csv`, the frozen corpus flags `datasets/analysis-results.csv`, and per-project positive outputs under `datasets/projects/`. Source directories must retain the original layout, with `owner/repository` names represented as `owner_repository`. The script checks that all 602 allowlisted directories and the original 43 excluded directories are present. It also reads these frozen notebooks under `scripts/`:

- `25-count-relevant-files-in-full-set.ipynb`
- `051-select-sample-projects-corrected.ipynb`
- `09-evaluate-prompting-strategy.ipynb`
- `11-select-files-for-reannotation.ipynb`
- `23-count-relevant-files-in-validation-set.ipynb`
- `24-count-relevant-files-in-test-set.ipynb`

The public source manifest provides file identities and hashes; it cannot substitute for the retained Java source snapshot.

```bash
python analysis/corpus_normalization.py /path/to/repositories \
  /path/to/masters-thesis/datasets/final-repositories-corrected.csv \
  /path/to/masters-thesis/datasets/analysis-results.csv \
  --output-dir analysis
```

It scans the retained source snapshot, verifies the allowlist and frozen flags, reconstructs the 17,988-file frame, and writes all normalisation artefacts for Phases 1 through 4. Every phase has assertion-based acceptance checks and a JSON summary recording methods and checksums. These commands recompute analyses from preserved evidence without making model calls.

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

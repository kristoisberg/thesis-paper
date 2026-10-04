# Training, validation, and test source-file recount

Date: 2026-10-04

## Scope and outcome

Recount the three frozen project partitions from `/run/media/kristoi/9327-3833/repositories`, using the selection and path-deduplication rules established in `.review/2026-09-12-corpus-normalization-plan.md`. Review the two conflicting notebook globs without executing notebooks or issuing model requests.

The corrected file-occurrence counts are **509 training, 1,159 validation, and 502 test files**. All freshly selected paths, source roles, sizes, nonblank line counts, and SHA-256 hashes match the corresponding subset of the frozen 17,988-file corpus manifest. No frozen annotation, prediction, or corpus-output rows were changed.

## Counting rules and provenance

1. Take project membership from the frozen `datasets/training-set.csv`, `validation-set.csv`, and `test-set.csv`, not from manually assembled repository lists. They contain 21, 20, and 20 distinct projects, are mutually disjoint, and all belong to the final 602-repository allowlist.
2. Reuse `analysis/corpus_normalization.py` for the original path exclusions, inclusion phrases, content exclusions, decoding, source-role assignment, and file hashing. Discover Java files recursively with `**/*.java` and count each repository-relative path once. Snapshot directories encode `owner/repository` as `owner_repository`.
3. Separately reproduce the narrower `**/src/**/*.java` discovery. Count raw matches and distinct paths independently to expose repeated matches from nested `src` components.
4. Separately group selected files by SHA-256 to measure exact-content duplication. Different paths containing identical bytes remain separate file occurrences in the primary count, as in the earlier corpus reconstruction.
5. Compare all selected files against the frozen corpus manifest, and compare the validation inventory with completed-file log records from every archived model/prompt configuration.

The source-selection rule digest remains `0e76695e8ff0705d6b8db74c500539d707926cbc8cb4df658ad4507d9d261b7b`. The unchanged corpus-manifest SHA-256 is `8200f8990215912efba90a4f5ed431d52c79d7b20e11ce496457f34829c8a214`.

All 26 study input files were independently checked against Git objects at study revision `d9b35e398a6deb544f913bdbc0b211ab38474a44`: the allowlist, three split CSVs, six original notebooks used by the corpus reconstruction, and 16 validation backups. Their local bytes match that frozen revision. The generated JSON summary records their individual hashes and all generated CSV hashes.

## Results

| Partition | Projects | Recursive raw matches | Distinct relevant paths | `src` raw matches | Distinct `src` paths | Duplicate `src` matches | Outside `src` |
|---|---:|---:|---:|---:|---:|---:|---:|
| Training | 21 | 509 | 509 | 496 | 496 | 0 | 13 |
| Validation | 20 | 1,159 | 1,159 | 823 | 823 | 0 | 336 |
| Test | 20 | 502 | 502 | 502 | 502 | 0 | 0 |

Unlike the full corpus, none of these 61 projects emits repeated selected paths under either glob. The narrower glob omits relevant paths outside `src`; it does not inflate these three counts through duplicate matches.

| Partition | Generated schema | Application/query | Unique file contents | Exact-duplicate groups | Paths in those groups | Extra exact copies |
|---|---:|---:|---:|---:|---:|---:|
| Training | 176 | 333 | 476 | 33 | 66 | 33 |
| Validation | 175 | 984 | 1,141 | 13 | 31 | 18 |
| Test | 146 | 356 | 502 | 0 | 0 | 0 |

No byte-identical group crosses the three partitions. This finding does not establish the absence of modified clones. The collapsed-content counts are sensitivity counts, not replacements for the primary source-file frame.

## Resolution of the validation discrepancy

The base evaluation notebook and all 16 backups use `**/*.java`. `23-count-relevant-files-in-validation-set.ipynb` uses `**/src/**/*.java` and retains the scalar output 823. `24-count-relevant-files-in-test-set.ipynb` uses the same narrow glob and retains 502.

Every validation backup preserves 1,159 successful completed-file records, without duplicate paths. All 16 inventories are identical and match the freshly reconstructed validation inventory. Of those files, 823 have a `src` path component and 336 do not. The latter comprise 299 files under `target/generated-sources` and 37 in other locations. The validation discrepancy therefore follows from discovery scope. It is no longer evidence that the archived validation file inventory is missing or inconsistent.

The test glob scopes happen to yield the same 502-file frame. The reconstructed 509-file training frame is the set of relevant files in the assigned training repositories, not evidence that every such file was inserted into a prompt or processed in a particular development run.

## Annotation-frame exceptions

The retained-class split CSVs have 332 training, 581 validation, and 523 test reference events across 145, 276, and 195 distinct annotated paths. All training and validation paths belong to their reconstructed frames. Two test paths do not, each carrying one event:

| Project | Recorded reference path | Finding |
|---|---|---|
| `jOOQ/jOOQ-mcve` | `jOOQ-mcve-java-mysql/src/main/java/org/jooq/mcve/java/mysql/tables/Test.java` | The source exists, but its path matches the original `mysql/tables` exclusion. The annotated event is ID Required at line 55. |
| `therepanic/trustwin-casino-project` | `game-overgo-service/src/main/java/eu/panic/gameminerservice/generatedClasses/tables/NotificationsTable.java` | The recorded path is absent. A file with the same trailing package/file path exists under `game-miner-service`, suggesting a module-path transcription error. The frozen annotation has not been remapped. |

The script records these exceptions rather than silently treating all annotated paths as selected files. The summary's `all_annotations_in_source_frame` is consequently false. The primary 523-reference evaluation remains unchanged, including these events; this audit does not recompute occurrence matching under repaired paths or altered filters.

## Remaining configuration-summary discrepancies

The runtime and recall findings below describe the later-rerun notebook archived before restoration. They are superseded by `2026-10-04-opus-original-run-restoration.md`: the original run now preserves 366.72 seconds and recall 0.8898, matching the manuscript after rounding. The restoration was committed and published as `9913a7670fce52b135651f95ff18cd505c61b142`; the current input hashes match that revision. The author subsequently corrected the Opus Zero-Shot manuscript cost from $29.97 to the restored run's API cost, $31.39. The author then confirmed that the table uses OpenRouter-reported charges and corrected GLM-5 Zero-Shot to $11.76. The cost caveats based on comparing those charges with notebook sums were removed; the details below record the earlier comparison.

A technical-reviewer audit checked the seven displayed configuration rows against preserved notebook summaries. Weighted metrics are in cell 10; runtime and accumulated API-cost summaries are in cell 8.

| Configuration | Archived weighted P/R/F1 | Archived runtime, seconds | Archived API cost, USD | Comparison with the originally reported table |
|---|---|---:|---:|---|
| GPT-5.2 Zero-Shot | .8537/.9225/.8801 | 2423.31 | 26.077763 | Metrics and runtime match displayed rounding; reported cost is 26.16. |
| GLM-5 Zero-Shot | .8837/.8933/.8768 | 5774.14 | 10.950958 | Metrics and runtime match; reported cost is 11.77. |
| Opus Zero-Shot | .8839/.8830/.8796 | 618.29 | 31.396420 | Reported recall .89, runtime 367, and cost 29.97 differ. |
| gpt-oss Zero-Shot | .8262/.8692/.8339 | 2808.35 | 1.493565 | Matches displayed rounding. |
| Opus Few-Shot | .8800/.8881/.8803 | 351.81 | 44.999000 | Matches displayed rounding. |
| Opus Chain-of-Thought | .9248/.9002/.9030 | 955.93 | 40.862095 | Matches displayed rounding. |
| Opus Tree-of-Thought | .9199/.8967/.9007 | 4700.71 | 80.850875 | Metrics and runtime match; reported cost is 81.43. |

The article's cost caption includes VAT, whereas the notebook values are accumulated API costs. Numerical differences alone do not establish their cause. The Opus Zero-Shot recall and runtime differences remain independent of this billing distinction. The original table is retained as originally reported; statements that all exact validation outputs are unavailable were corrected to describe the surviving records and remaining discrepancies. Resolving file counts does not establish full reconstruction of the original executions or configuration table.

## Reproduction and outputs

From the article repository root:

```bash
PYTHONDONTWRITEBYTECODE=1 python analysis/split_file_inventory.py \
  /run/media/kristoi/9327-3833/repositories /home/kristoi/masters-thesis
```

The standard-library script reuses the unchanged corpus helper and produces:

- `analysis/split_file_counts.csv`, split counts and exact-copy summaries;
- `analysis/split_file_counts_by_repository.csv`, 61 repository records;
- `analysis/split_source_manifest.csv`, 2,170 distinct selected paths and hashes;
- `analysis/split_duplicate_glob_matches.csv`, header only;
- `analysis/split_cross_partition_exact_duplicates.csv`, header only;
- `analysis/split_annotation_frame_exceptions.csv`, the two test exceptions;
- `analysis/split_file_inventory_summary.json`, methods, acceptance checks, 16 archived-inventory comparisons, and checksums.

## Applied changes and verification

- Updated Study Design with all three path counts, the verified cause of the validation discrepancy, and the exact narrow glob used for the earlier corpus count.
- Updated the replication README with the recount command, outputs, counting boundaries, duplicate results, reference exceptions, and corrected archive description.
- Updated threats to validity with the two test-reference exceptions and the specific remaining configuration-summary discrepancies.
- Qualified the Results description of the originally reported 367-second runtime and corrected its scope to Zero-Shot configurations.
- Completed fresh source reconstruction and equality checks against the frozen manifest. Independently checked all generated CSV hashes, all 26 frozen study-input hashes, and uniqueness of the 2,170 output keys.
- Built `paper/main.pdf` successfully, now 29 pages. No undefined references, citation warnings, or overfull boxes were reported; the pre-existing document-class name warning remains. Checked changed pages and retained table order.
- Left external snapshots, study notebooks, annotations, predictions, the original configuration table, and all earlier corpus-normalisation artefacts unchanged.

The new audit and updated README are local changes. The article's existing frozen documentation link at `4a3b4d55073adbb38325ca43872852d2a75649c9` predates this audit. Freeze and publish the revised artefacts, then update the documentation revision before submission; no immutable link to a not-yet-published revision has been invented.

## Manuscript wording refinement

At the author's request, the main manuscript now states the final partition sizes directly. The validation passage gives 20 repositories and 1,159 relevant files without the old 823-file count, glob comparison, archived-inventory explanation, or reconstruction wording. The split paragraph also gives its three final file counts directly. The counting history and verification remain in this audit and the replication README. The PDF rebuilt successfully, and its extracted text confirms the simplified validation statement and absence of the old validation count.

The corpus passage was also simplified at the author's request. It now reports the final 17,988-file frame, recursive discovery, relevance filters, and counting each repository-relative path once. The historical 17,450 count, duplicate/omission reconciliation, source-location breakdown, and reconstruction narrative were removed from that passage. The Results opening also refers directly to the corpus source frame. The earlier corpus audit retains the counting history. Source-role denominators and all analysis results remain unchanged. The PDF rebuilt successfully; extracted text confirms the final count and absence of the historical count.

## Classification of the two reference-frame exceptions

Following the author's clarification, the two cases are described separately. The `jOOQ/jOOQ-mcve` case is an overbroad blacklist rule excluding an annotated application table. The casino-project case is an annotation error. The original `test-set.csv` contains both the incorrect `game-overgo-service` path and the correct `game-miner-service` path for ID Required at line 56, so the incorrect row is an extra annotation rather than an occurrence requiring a new annotation at the correct path.

The original thesis, `thesis/chapters/08_analysis.tex`, attributes ID Required disagreements to five incorrect reference line ranges, four invalid reference occurrences, and seven missing reference occurrences. `scripts/15-calculate-tool-localisation-corrected.ipynb`, cell 2, records corrected ID Required totals of TP 101, FP 1, FN 7 as manually supplied aggregate counts. It does not preserve an event-level corrected reference or a removal log. `datasets/reannotated-ground-truth.csv` is a separate repeat-annotation dataset and contains neither of these file names. Removal of the wrong-path row is consistent with the corrected analysis, but cannot be verified individually from the retained aggregate records. No claim is made that the revised-reference analysis repaired the blacklist.

Updated the README and threats paragraph to distinguish file-selection error from reference error. The frozen counts, rules, reference rows, and primary and sensitivity metrics remain unchanged.

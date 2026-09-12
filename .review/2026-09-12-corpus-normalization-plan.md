# Corpus normalization plan

Date: 2026-09-12

Status: Phases 1 and 2 complete; ready to continue.

Scope: the 602-repository corpus, its exact source snapshot at `/run/media/kristoi/9327-3833/repositories/`, and the frozen detector flags in `/home/kristoi/masters-thesis/datasets/analysis-results.csv`.

## Objective

Replace the raw-count account of corpus flags with a reproducible analysis of detector-output density, breadth, repetition, and repository-size effects. The main analysis must use the existing detector outputs and local source snapshot. It must not issue new model requests.

The intended paper-level result is:

> Large repositories contribute much of the total detector output, yet repository size does not fully explain its composition. Some classes occur across many files, whereas others recur several times within flagged files.

These results remain measurements of detector output. Estimates of true antipattern prevalence require an independent corpus audit, and API-specific risk requires denominators for all eligible API uses.

## Confirmed inputs

- The external directory contains 645 repository directories.
- All 602 names in `final-repositories-corrected.csv` map to source directories.
- No included repository is missing.
- The other 43 directories are excluded from every denominator and result.
- The source directories are the exact snapshot used for the original corpus analysis.
- Git history was excluded from the original archive. Reproducibility therefore uses repository-relative paths and SHA-256 content hashes.
- The frozen output contains 15,931 flags in 601 repositories.
- The positive output contains 7,653 distinct `(Project, File)` pairs.
- Six event keys occur twice, producing six extra rows. The analysis must retain the published row count and report a canonical-event sensitivity result.

## Phase 1: reconstruct and freeze the source frame

Create one deterministic script that reads the 602-repository allowlist and ports the original relevant-file selection rules verbatim.

### Authoritative selection logic

Use the detector's `src/file-discovery.ts` at commit `cf82fe56acb728f076df67279ff4a78a138996f3` as the authoritative source for the full-corpus frame. It specifies:

- recursive `**/*.java` discovery across every source location;
- ordinary files only, with hidden paths and symbolic-link traversal disabled;
- 22 `excluded_path_fragments` entries;
- 3 `included_phrases` entries;
- 22 `excluded_phrases` entries;
- UTF-8 decoding with the detector's `TextDecoder("latin1")` fallback;
- three DDL indicator phrases used to select the source role.

The three filter lists are identical in `25-count-relevant-files-in-full-set.ipynb`, `051-select-sample-projects-corrected.ipynb`, `09-evaluate-prompting-strategy.ipynb`, `11-select-files-for-reannotation.ipynb`, `23-count-relevant-files-in-validation-set.ipynb`, and `24-count-relevant-files-in-test-set.ipynb`. Preserve this equality as a self-check. The counting notebooks' `src/**/*.java` restriction is not part of the detector's discovery rule and must not define the result frame. Do not use the older lists in `05-select-sample-projects.ipynb`, which contain only 21 path exclusions and 18 content exclusions.

The new script should keep one literal copy of the authoritative lists and assert a stable digest over their ordered values. It should not combine rules from multiple notebooks or infer new exclusions from the current source tree.

For every selected file, record:

- repository name;
- repository-relative path;
- source role, either generated schema or application/query source;
- byte size;
- nonblank lines of code;
- SHA-256 content hash.

Produce a source manifest and an alignment report that joins every archived flag to its source file and line span.

### Acceptance checks

- [x] The allowlist contains 602 unique repository names.
- [x] All 602 names resolve to distinct directories.
- [x] None of the 43 excluded directories enters the source frame.
- [x] The detector-matched scan contains 17,988 unique relevant files.
- [x] The location breakdown contains 17,314 `src` files, 360 `target/generated-sources` files, and 314 files in other source locations.
- [x] The ordered selection-list digest matches the authoritative rule set.
- [x] The authoritative lists still match the corrected sampling, evaluation, reannotation, validation-count, and test-count notebooks.
- [x] Every archived flag resolves to an allowlisted repository and file.
- [x] Every archived flag belongs to the reconstructed source frame.
- [x] Every reported line span lies within its source file.
- [x] Each reported line span is treated as authoritative; stored code fragments are retained as best-effort diagnostics.
- [x] The merged per-project outputs reproduce `analysis-results.csv` if those files survive.
- [x] Input CSVs and generated manifests receive SHA-256 checksums.

Any missing path, out-of-bounds span, repository-name collision, or unexplained difference from 17,988 stops the source-based analysis until reconciled. Fragment differences and the historical 17,450 count are not acceptance gates.

### Phase 1 execution results

The detector-matched scan contains 17,988 unique files: 17,314 under a path component named `src`, 360 under `target/generated-sources`, and 314 in other source locations such as `build/generated-src`, `src-generated`, and project-specific generated directories. It classifies 7,226 files as generated-schema sources and 10,762 as application/query sources. The manifest SHA-256 is `8200f8990215912efba90a4f5ed431d52c79d7b20e11ce496457f34829c8a214`; the flag-alignment report SHA-256 is `b035fd06e7c829da8f995770e769c7d3491d0d32794837ddc2191f960f78c728`.

The earlier 17,450 count came from `src/**/*.java`. That glob produced 17,314 unique paths and 136 duplicate matches, while omitting 674 detector-selected files outside `src`. The errors partly cancel, leaving the reported value 538 below the corrected total. The 674 added files include all 308 previously out-of-frame flagged files. Consequently, all 15,931 flags and 7,653 distinct flagged files now belong to the reconstructed frame.

All 15,931 archived paths exist in the allowlisted snapshot, and all reported spans are within file bounds. The reported spans are the source of truth. After trimming outer whitespace and collapsing whitespace runs, 15,729 stored fragments equal or occur within their reported spans. The remaining 202 are diagnostic discrepancies: 177 occur elsewhere in the same source file, while 25 do not occur verbatim after normalization. They remain identified in `analysis/corpus_flag_alignment.csv` and do not block source-span analyses. Phase 1 is complete, so the workflow can continue with Phase 2.

## Phase 2: measure breadth and repetition

For repository \(r\) and class \(c\), define:

- \(Y_{rc}\): detector flags;
- \(F_{rc}\): eligible files;
- \(A_{rc}\): eligible files containing at least one flag.

Decompose detector-output density as:

\[
\frac{Y_{rc}}{F_{rc}}
=
\frac{A_{rc}}{F_{rc}}
\times
\frac{Y_{rc}}{A_{rc}}.
\]

This separates breadth, the share of eligible files flagged, from repetition, the number of flags within a flagged file.

For each class, report:

- total flags;
- eligible files;
- unique flagged files;
- percentage of eligible files flagged;
- flags per 100 eligible files;
- flags per flagged file;
- median and interquartile range across repositories.

Use generated-schema files as the file frame for database-design classes and application/query files for query classes. Split Fear of the Unknown by source role because its operational definition spans both representations. Also provide an all-relevant-file measure as a common descriptive denominator, clearly labelled as broad detector-output density.

### Expected checks from the frozen positive output

- [x] Any retained class has 7,653 distinct flagged files.
- [x] `7,653 / 17,988` gives a pooled flagged-file yield of 42.5%.
- [x] Flagged files contain 2.08 flags on average.
- [x] ID Required has 3,591 flagged files and approximately 1.00 flag per flagged file.
- [x] Implicit Columns has 2,607 flagged files and approximately 2.80 flags per flagged file.

### Phase 2 execution results

Across all relevant files, 7,653 of 17,988 files contain at least one retained flag (42.5%). These files contain 15,931 flags, or 2.08 flags per flagged file. The role-specific results separate two different patterns. ID Required affects 3,591 of 7,226 generated-schema files (49.7%) and almost never repeats within a file (1.00 flags per flagged file). Implicit Columns affects 2,607 of 10,762 application/query files (24.2%) but repeats within them (2.80 flags per flagged file).

Fear of the Unknown is mainly a schema-side detector output. It affects 675 generated-schema files (9.34%) and 11 application/query files (0.10%), with 1.84 and 1.45 flags per flagged file, respectively. `analysis/corpus_phase2_class_summary.csv` reports pooled breadth, density, repetition, repository quartiles, and broad flags per 100 all-relevant files for every class-role frame. `analysis/corpus_phase2_by_repository.csv` retains all 602 repositories for later size analysis. Rates are blank when a repository has no eligible files; repetition quartiles include only repositories with at least one flagged file. The output SHA-256 values are recorded in `analysis/corpus_phase2_summary.json`.

## Phase 3: separate repository size from flag density

Calculate every class measure within each repository before aggregation. Include all 602 repositories in repository-equal summaries, including the repository with no flags.

Report:

- pooled flag density;
- repository-equal mean and median density;
- interquartile and 10th--90th percentile ranges;
- results within the existing small, medium, and large strata using the 31-file and 94-file boundaries;
- correlation between raw flags and eligible-file count;
- the top-decile repositories' shares of both flags and eligible files;
- results after excluding the highest-count decile.

The concentration analysis should answer whether the reported 59.1% top-decile flag share reflects repository size, excess flag density, or both.

The 602 repositories form the complete identified corpus. Report their distributions directly. A project bootstrap may measure sensitivity to repository composition, but it must not be described as population uncertainty.

### Decision gate

- [ ] Compare the pooled and repository-equal class rankings.
- [ ] Compare raw-count and file-normalized concentration.
- [ ] Keep a new headline result only when it adds information beyond the published repository-coverage and top-decile measures.

If normalization yields the same interpretation as the raw analysis, report it as a concise robustness result rather than expanding the paper around it.

## Phase 4: exact-duplicate sensitivity

Group byte-identical relevant files by SHA-256. Recalculate the headline results with one contribution per unique file content and occurrence span.

Report:

- the number and share of duplicated relevant files;
- the share of flags in duplicated files;
- class totals after exact-content weighting;
- whether class ordering, breadth, or concentration changes.

Approximate clone detection is out of scope unless exact duplicates materially affect the conclusions.

### Decision gate

- [ ] Raw-row and canonical-event analyses preserve the same substantive ordering.
- [ ] Exact-content weighting does not reverse a headline result.

Any reversal becomes a main robustness finding rather than a footnote.

## Phase 5: optional class-specific exposure denominators

Begin with the two query classes already analysed by source-fragment form.

### Implicit Columns

Count all eligible projection or result-producing forms covered by the operational definition, including `selectFrom`, `select().from`, `asterisk`, `fields`, applicable `returning` forms, and covered generated-DAO operations. Preserve the source-fragment category for every exposure.

### Poor Man's Search Engine

Count all eligible text-search predicates, including `like`, `likeIgnoreCase`, `contains`, `containsIgnoreCase`, and other patterns named in the codebook. Separate recognizable prefix searches and non-wildcard uses where the operational definition requires it.

For form \(a\), calculate:

\[
\operatorname{yield}_a=
\frac{\text{uses associated with a detector flag}}
{\text{all detected eligible uses}}.
\]

Call this quantity lexical flag yield. It does not measure causal API risk.

Use a lexical scan first. Add a Java parser only if a validation sample shows that lexical matching cannot separate eligible calls and near-misses. Keep unresolved calls as a separate count.

### Validation and stop rule

- [ ] Review every rare syntax form.
- [ ] Review a random sample of common candidates and near-misses.
- [ ] Confirm that archived flags map to an eligible exposure.
- [ ] Define extractor acceptance thresholds before comparing API yields.

Omit an exposure-normalized class result if its denominator cannot be extracted reliably. Keyless Entry and query-side Fear of the Unknown are likely to require semantic analysis and should remain file-normalized unless a simple validated method emerges.

## Phase 6: optional corpus transfer audit

This phase adds human annotation and is required before estimating true corpus prevalence.

1. Stratify repositories by size and detector-output composition.
2. Sample complete files from flagged and unflagged groups.
3. Hide detector decisions from annotators.
4. Annotate every eligible occurrence in each sampled file so false negatives are observable.
5. Use independent annotation and adjudication.
6. Preserve selection probabilities and project membership.
7. Estimate class-specific precision and recall with project-clustered uncertainty.

Existing held-out precision and recall may support a supplementary transfer-assumption sensitivity calculation,

\[
\widetilde{Y}_c=Y_c\frac{p_c}{q_c},
\]

where \(p_c\) and \(q_c\) are held-out precision and recall. Sparse project support prevents this calculation from becoming a headline prevalence estimate.

## Analyses to reject

- Per-statement rates from `project-statement-counts.csv`. The heuristic counter gives zero statements for ten repositories that contain 57 flags, and schema-level flag numerators do not match a query-statement denominator.
- Rates per all Java files. Unrelated source files dilute the denominator.
- LOC as the primary denominator. Generated formatting makes LOC hard to interpret; retain it only as a sensitivity check.
- Stars, age, activity, or history-based analyses. Git history is unavailable, and these measures do not answer the normalization question.
- Inclusion of the 43 excluded repositories. They are outside the final corpus and lack corresponding frozen detector outputs.
- Direct prevalence or API-risk claims from held-out precision and recall correction.
- Complex regressions or new dependencies before the descriptive decomposition has been evaluated.

## Planned implementation

Prefer one standard-library Python script with assertion-based self-checks. Reuse existing selection rules and source-fragment categories. Add a parser only if the Phase 5 validation gate requires it.

Planned artefacts:

- `analysis/corpus_normalization.py`;
- a hashed 17,988-file detector-matched source manifest, with location counts for `src`, `target/generated-sources`, and other paths;
- a flag-to-source alignment report;
- machine-readable summary tables;
- exact-duplicate and canonical-event sensitivity outputs;
- an explicit reproduction command in Online Resource 1.

The script must read the external repository snapshot without changing it. Generated files belong in the article repository or a temporary output directory, never under the external source tree.

## Planned paper changes

If Phases 1--4 pass their gates:

- **Study Design:** define the source manifest, file roles, normalization measures, repository weighting, and duplicate-content sensitivity.
- **Results:** replace the raw-count-only account with one compact table covering flag count, repository coverage, flagged-file breadth, and within-file repetition. Interpret pooled and repository-equal results together.
- **Discussion:** explain whether class differences arise from breadth, repetition, repository size, or copied content.
- **Threats to Validity:** retain the detector-output boundary and state that file eligibility is broader than class-specific opportunity.
- **Online Resource 1:** provide the manifest checksum, analysis command, complete normalized tables, and sensitivity results.

Use one table in the main paper. Add a figure only if the repository-rate distribution reveals a pattern that the table cannot express clearly.

## Recommended stopping point

Complete Phases 1--4 first. They require only local deterministic scans, directly address repository-size confounding, and may provide enough evidence for a stronger paper. Begin Phase 5 only if exposure-specific results would materially strengthen RQ3. Reserve Phase 6 for a later study unless prevalence estimation becomes a submission requirement.

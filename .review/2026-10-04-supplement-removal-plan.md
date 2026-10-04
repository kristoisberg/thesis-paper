# Supplement removal plan

Date: 2026-10-04

Status: Steps 1 and 2 completed. Steps 3 through 8 remain planned.

Baseline: `df785ba27c9ff38eaae79af6f5677cbb621290b0`.

## Objective

Remove the separate supplementary PDF. Keep the scientific argument self-contained in the article, preserve unique replication documentation in `analysis/README.md`, and replace references to Online Resource 1 with accurate links to the relevant materials.

At the planning baseline, the supplement was seven pages. Its final four sections repeated material already in the article. Step 1 removed those copies and reduced the supplement to five pages. Most of its remaining content describes preserved files, original executions, dependencies, and reconstruction commands.

## Content destinations

| Current supplementary content | Destination and action |
|---|---|
| Resource index | Move to `analysis/README.md`, with direct links to the frozen files and directories. |
| Snapshot and preserved-output inventory | Move to the README. Keep original study, released detector, and article-analysis revisions distinct. |
| Execution dates, model settings, routing, and retries | Preserve the complete record in the README. Add a concise execution summary to Study Design. |
| Validation date/retry table | Move to the README. Explain that these are archival records whose relationship to the originally reported validation results has limits. |
| Missing records and replay limitations | Preserve the detailed account in the README and the concise account under Reliability validity. |
| Dependencies and reconstruction commands | Move to the README beside links to the scripts and `requirements.txt`. |
| Corpus file inventory and SHA-256 values | Preserve in the README or link to existing machine-readable records that contain the same information. |
| Equivalent SQL and jOOQ example | Remove the supplementary copy. Keep the existing main-paper figure. |
| Detection representations and output units | Remove the supplementary copy. Keep the existing Background and Related Work table. |
| Project-disjoint split support | Remove the supplementary copy. Keep the existing Study Design table. |
| IoU sensitivity | Remove the supplementary copy. Keep the existing Results table. |

## Step 1. Establish the baseline and remove duplicated supplementary sections

- [x] Record the working-tree state and the current main-paper page count before implementation.
- [x] Check the four duplicated sections against their main-paper counterparts. Identify any unique explanatory sentence before removing a copy.
- [x] Transfer any unique explanatory sentence identified during comparison to its main-paper counterpart before deleting the supplementary copy. No transfer was needed.
- [x] Remove these four sections from `paper/supplementary.tex`: Equivalent SQL and jOOQ source representations; Detection representations and output units; Project-disjoint split support; Intersection-over-union sensitivity. Keep their existing main-paper counterparts.
- [x] Remove the resource-index sentence referring to the supplementary split-support and IoU sections, along with any other references to the deleted sections or labels.
- [x] Inventory all live references to `Online Resource`, `ESM_1`, `supplementary.tex`, and supplement build targets. Exclude historical `.review` reports from the migration.
- [x] Verify the frozen repository targets for search strings, omitted repositories, annotation records, decision trees, prompts, source-fragment categorisation, scripts, and generated tables.
- [x] Distinguish material contained in a document from material linked through an index. In particular, the catalogue is not contained in the supplementary PDF.

Completion condition: the four duplicated sections and their supplementary cross-references are removed before Step 2 begins, every unique item has a named destination, and every replacement resource claim has a verified target.

### Step 1 execution record

Implementation began at commit `8daecfefba8c9107805aba08b712fe4245649eec` with a clean working tree. The compiled main paper contained 29 pages and the supplement contained seven.

Removed the four duplicated supplementary sections and the resource-index sentence pointing to their split-support and IoU labels. The SQL/jOOQ listings and both numerical tables match the main paper. Differences in the detector-comparison wording repeat explanations already present in Background and Related Work. No unique scientific content required transfer, and no main-paper source changed.

The remaining resource index and reproducibility record have the destinations listed above for Step 2. The catalogue, decision trees, prompts, search terms, and notebooks are externally linked resources; they are not embedded in the supplementary PDF.

The following frozen paths were verified before any replacement links were written:

| Snapshot | Verification and available targets |
|---|---|
| `masters-thesis` at `d9b35e3` | GitHub's recursive Git tree returned a complete listing. Verified `thesis/appendices/appendix-github-search-terms.tex`, `appendix-omitted-projects.tex`, and `appendix-annotated-antipatterns.tex` in that directory; `diagrams/decision/`, `prompts/`, and `scripts/`; `datasets/test-set.csv`, `analysis-results.csv`, and `final-repositories-corrected.csv` in that directory; and `scripts/14-evaluate-tool-localisation.ipynb` and `scripts/21-find-frequent-offenders.ipynb`. |
| Released detector at `cf82fe5` | GitHub's complete recursive Git tree verified `package.json` and `bun.lock` at the frozen revision. |
| Article analyses at `bb3bf60` | The local Git object verified all three reconstruction scripts, `analysis/requirements.txt`, and all seven manifest/alignment/generated-table files listed in the supplementary checksum table. |

Live references awaiting later steps are inventoried as follows:

| Location | Remaining migration work |
|---|---|
| `paper/sections/02_background_related_work.tex` | One Online Resource reference for taxonomy and annotation rules. |
| `paper/sections/03_study_design.tex` | Four references for mining resources, codebook, prompts, and source-fragment patterns. |
| `paper/sections/06_threats_to_validity.tex` | One reference for preservation limits and the source manifest. |
| `paper/main.tex` | Data-availability reference and the Supplementary information declaration/caption. |
| `paper/supplementary.tex` | Remaining title, metadata, resource index, and reproducibility record, retained until Step 2 transfers the documentation. |
| `Makefile` | Supplement dependency, target, and cleanup recipe. |
| `.github/workflows/paper.yml` | Builds through `make paper`; upload and preview already use only `paper/main.pdf`. |
| Local packaging/checking skills | `springer-latex-packager` expects the supplementary source and Online Resource captions; `acceptance-checker` expects an Online Resource citation. These assumptions are scheduled for Step 6. |

Verification: `git diff --check` and `make paper` passed. Neither PDF log contains undefined citations/references, LaTeX errors, or overfull boxes; the bibliography logs contain no warnings. Searches confirmed that the deleted section labels have no references left in the supplement. The main paper remains 29 pages; the supplement is now five pages. At the completion of Step 1, Steps 2 through 8 had not been applied.

## Step 2. Create the replication README

- [x] Create `analysis/README.md` as the entry point for the article's replication materials.
- [x] Transfer the resource index, snapshot inventory, detailed preservation limits, execution date/retry table, dependencies, reconstruction commands, and checksum information.
- [x] Preserve the existing immutable identifiers: study artefacts at `d9b35e3`, released detector at `cf82fe5`, and the previously frozen article analyses at `bb3bf60`. Use the full revisions in links.
- [x] Explain that the released detector postdates the original executions and does not identify the binary used for them.
- [x] Separate recomputation from preserved outputs from replay of the original model executions. Document what the released scripts can reproduce and which inputs they require.
- [x] Keep the distinction between original notebook environments and the environment used to verify the reconstruction scripts.
- [x] Preserve original model slugs, settings, provider constraints, recorded retry totals, and missing metadata. Retain the GPT-5.2 gateway-field caveat and the explanation for gpt-oss-120B's default temperature.
- [x] Preserve the discrepancy between the 1,159-file archived notebook copies and the originally reported 823-file validation set. Do not present archived dates or retries as proof that those copies produced the published configuration table.
- [x] Remove the publication-workflow statement "A repository DOI remains required" from the transferred narrative. Describe the actual archival identifiers available. Track any future deposit separately.

Completion condition: all unique supplementary documentation is readable and accessible from the README without requiring the supplementary PDF.

### Step 2 execution record

Implementation began at commit `5cc427f88a9dec03de156fbe03bae1c4911db55c` with a clean working tree. Created `analysis/README.md` and transferred the remaining unique resource index and replication documentation. The README distinguishes the three frozen snapshots, original execution records, reconstruction environment, and limits on replay. It preserves the validation-file-count discrepancy and all recorded settings, dates, retries, and missing metadata.

Inspection of the frozen `appendix-annotated-antipatterns.tex` showed that it lists the 19 annotated classes without supplying their definitions. The README therefore labels that link "List of the 19 annotated antipatterns" rather than claiming a full catalogue or operational definitions. Later manuscript link updates must respect this distinction.

Documented the required inputs beside each reconstruction command. Corpus normalisation requires the retained source snapshot with all 602 allowlisted and 43 excluded repository directories, six specified notebooks, and per-project outputs; the public source manifest cannot substitute for the Java source files.

Verification: all three command blocks match the supplement; all seven SHA-256 values match the supplement, local files, and frozen analysis revision. All 44 immutable GitHub links resolve to paths in the frozen repository trees, and the relative requirements link exists. Markdown whitespace checks and `git diff --check` passed. No analyses or model executions were rerun, and no PDF build was needed for this documentation-only step.

Files changed: `analysis/README.md` and this plan. The README explicitly notes that `bb3bf60` predates it; an immutable public documentation revision remains work for Step 5. The supplementary source remains intact until Step 6. Steps 3 through 8 remain planned.

## Step 3. Add the useful execution context to Study Design

Edit `paper/sections/03_study_design.tex`, under Detector configuration and execution.

- [ ] Add the validation execution dates recorded in the archive: 6–7 March 2026 for Zero-Shot, Few-Shot, and Chain-of-Thought, and 27 March for Tree-of-Thought-inspired runs.
- [ ] Add the recorded held-out and corpus execution dates, 4 April and 15 April 2026.
- [ ] Summarise retry handling and the available routing evidence. GLM-5 requests fixed Friendli and disabled fallbacks; comparable routing records for the other models are unavailable.
- [ ] Keep the detailed per-configuration retry table, dashboard clock times, model slugs, and dependency inventory in the README.
- [ ] Make the validation-output preservation limitation clear where the originally reported comparison is introduced. If needed, add one concise sentence explaining the archived-file-count discrepancy, with a link to the detailed record.
- [ ] Keep the existing corrected model settings and distinguish parameters submitted to the gateway from settings supported by the model.

Aim for one short execution-context paragraph plus any essential clarification. Do not add the full archival inventory to Methods or change reported experimental results.

Completion condition: readers can assess the timing, execution controls, and provenance limitations from the article, with detailed records available through a specific link.

## Step 4. Replace Online Resource references throughout the article

| File and passage | Replacement destination |
|---|---|
| `02_background_related_work.tex`, taxonomy and annotation rules | Verified catalogue and decision-rule resources in the frozen study repository. |
| `03_study_design.tex`, repository mining | Search-string and omitted-repository files. |
| `03_study_design.tex`, operational scope | Annotation codebook and decision trees. |
| `03_study_design.tex`, prompt development | Preserved prompt directories and documented localisation rules. |
| `03_study_design.tex`, source-fragment coding | Ordered categorisation procedure in the archived notebook. |
| `06_threats_to_validity.tex`, reliability limits | Replication README and source-file manifest. |
| `main.tex`, data/code availability | Frozen data, scripts, and the new documentation revision. |

- [ ] Use meaningful linked text and avoid repeating full repository URLs in the prose.
- [ ] Retain the existing concise reliability account, including missing detector revision, request/provider records, prompt identity, and validation outputs.
- [ ] Remove the Supplementary information declaration and its `ESM_1.pdf` caption from `paper/main.tex`.
- [ ] Preserve the data and code availability declarations.
- [ ] Keep the user's recent removals: the NotebookLM paragraph and the language-revision sentence remain removed.

Completion condition: the article contains no live reference to the retired Online Resource and makes no claim that an index contains externally linked materials.

## Step 5. Make the documentation version explicit

- [ ] Record the revision that contains the new README when it exists. The old `bb3bf60` revision cannot be used as a link to a newly created file.
- [ ] Keep the frozen analysis revision identifiable even if a newer documentation revision is cited separately.
- [ ] Include a link to the replication README in Code and materials availability. Use an actual immutable documentation link before submission.
- [ ] Verify that linked resource paths resolve and that the README points to the intended versions of the data and scripts.

Completion condition: manuscript links distinguish the existing evidence snapshots from the new documentation version. Creating the local README does not by itself make a public link to it available.

## Step 6. Remove the supplement source and build dependency

Perform this step after the content transfer and reference updates are complete.

- [ ] Delete `paper/supplementary.tex`.
- [ ] Update `Makefile` so `paper` builds the main article only, and remove the `supplement` target and its phony entry.
- [ ] Remove the clean recipe that invokes LaTeX on the deleted source. Keep explicit cleanup for obsolete generated supplement files if useful.
- [ ] Remove obsolete local `ESM_1` and legacy `supplementary` build products by their exact paths so they cannot be mistaken for current submission files.
- [ ] Inspect `.github/workflows/paper.yml`. It already uploads only `paper/main.pdf`; preserve that behavior. Change the plural build-step labels if appropriate.
- [ ] Update the supplement assumptions in `skills/springer-latex-packager/SKILL.md` and `skills/acceptance-checker/SKILL.md`: supplement naming and caption rules apply when a supplement is supplied. The current article's expected outputs should no longer include `paper/supplementary.tex`.
- [ ] Preserve unrelated checklist rules and historical review reports.

Completion condition: the active build and packaging guidance work without a supplementary source or PDF.

## Step 7. Verify the migration

- [ ] Run `git diff --check`.
- [ ] Run the updated `make paper` and inspect the log for compilation errors, undefined citations/references, and overfull boxes.
- [ ] Inspect the changed PDF pages for paragraph flow, table placement, clickable resource links, and a coherent transition out of Study Design.
- [ ] Search active manuscript, build, workflow, and packaging files for obsolete Online Resource and supplement references. Historical `.review` entries and deliberate legacy cleanup paths may remain.
- [ ] Confirm that the four scientific examples/tables remain in the article and their existing labels and references resolve.
- [ ] Check all transferred checksum values and command lines against the previous supplement and existing records. Run deterministic reconstruction commands only if their required source inputs are available and a new change or discrepancy warrants execution.
- [ ] Confirm that no reported counts, metrics, model-selection results, prompts, or raw data changed during the documentation migration.
- [ ] Compare page counts and bibliography changes. Citations used only in the retired supplement may leave the compiled article bibliography; do not delete shared bibliography entries automatically.

Completion condition: the article builds cleanly, resources remain findable, unique documentation survives, and the scientific results are unchanged.

## Step 8. Record the completed outcome

- [ ] Update this plan with the files changed, the final content destinations, and verification results.
- [ ] Record the actual replication-documentation revision or any remaining publication-link work separately from completed local changes.
- [ ] Report the new main-paper page count and whether any unresolved resource paths remain.

## Journal guidance

The journal accepts supplementary files and specifies Online Resource naming when such files are supplied. It also encourages research data to be deposited in repositories and requires a data availability statement. These provisions support a main article with a linked replication package; they do not establish a requirement for a separate supplementary PDF.

Source checked during the preceding review: [Empirical Software Engineering submission guidelines](https://link.springer.com/journal/10664/submission-guidelines), sections Supplementary Information and Research Data Policy and Data Availability Statements.

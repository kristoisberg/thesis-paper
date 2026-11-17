# Step 2: annotation and file-frame reconciliation

Date: 17 November 2026.

Status: complete within the approved existing-evidence scope. The historical source snapshot is not currently mounted, so this step establishes archived event identities, file-frame membership, and matching status. It does not provide a new semantic annotation of the Java source.

## Applied changes

- Named the late-removed repository, `Davincii254/Stroom`, and stated that it belonged to none of the annotated partitions.
- Specified the repeat-annotation exercise's original 19-class scope, its 15 observed classes, and the outcome for originally unannotated files.
- Corrected a newly verified repeat-annotation counting error and documented the historical calculation alongside the recount.
- Replaced claims implying a preserved revised event-level dataset with the actual evidence: archived class-level TP/FP/FN aggregates without an event-level revision/change log.
- Made the error-mechanism table explicitly illustrative and supplied residual FP/FN counts for Implicit Columns, ID Required, and Keyless Entry without inventing causes.
- Distinguished corpus flag/frame reconciliation from verified successful detector responses.
- Accounted for both out-of-frame test references and their contribution to the original false-negative count.
- Added replication-guide instructions, a small standard-library recount script, and its generated summary. The expanded error table now uses `[H]` placement to avoid an overflowing page containing three floats.

## Newly confirmed repeat-annotation calculation error

The frozen CSVs contain 158 original and 149 repeated events in the 128 selected files. Matching complete event identities, including class, yields 144 exact pairs. The correct precision, recall, and F1 are 0.966443, 0.911392, and 0.938111.

The archived `scripts/12-calculate-cohens-kappa.ipynb`, cell 5, pairs records by exact span before inspecting their classes. At `boogiespook/waltz-test/waltz-schema/target/generated-sources/jooq/com/khartec/waltz/schema/tables/EntityStatisticDefinition.java:99`, both passes contain Keyless Entry and Naive Trees. Their row order reverses between `ground-truth.csv:478–479` and `reannotated-ground-truth.csv:69–70`. The archived procedure cross-pairs the labels and records two artificial disagreements. Replaying it reproduces the historical 142 same-class pairs and F1 0.925.

The manuscript now reports the correctly labelled-event recount and explains the discrepancy. This is a correction to the repeatability calculation, not a new annotation round or a change to the held-out matching algorithm. The frozen thesis and notebooks remain unchanged historical artefacts.

Reproduce with:

```bash
python analysis/repeat_annotation_check.py /home/kristoi/masters-thesis \
  > analysis/repeat_annotation_summary.json
```

The script uses multiset intersection, so each record contributes at most once and duplicate records cannot create extra matches. It also replays the historical span-first method and asserts the expected frozen-sample counts. The generated summary records input hashes and both cross-paired labels.

The same recount verifies 15 observed classes under the original 19-class annotation scope. Of 64 originally unannotated files, 63 remained unannotated and one acquired an annotation. The reliability result must not be presented as an independent validation of the later seven-class reference.

## Source/path/span exception audit

Matching used the preserved 523 test references, 536 predictions, and existing maximum-cardinality matching helper. Full-source semantics were not inferred from path names or detector-returned fragments.

| Repository and reference | Archived evidence | Primary status |
|---|---|---|
| `jOOQ/jOOQ-mcve`: MySQL `Test.java:55` | `test-set.csv:49`; exception ledger records historical source existence and exclusion by `mysql/tables`. No selected-manifest row or prediction. | One FN, retained among the 523 references. |
| Same repository: seven other dialect `Test.java:55` references | All seven have selected-manifest entries and exact matching predictions. | Seven TPs. |
| Same repository: SQLite-module path ending `/h2/tables/Test.java:55` | Present in selected manifest, SHA-256 `2a97b231c118a4758ff73f710349d1d74930080de5c99a2ec81b46f209be566b`. | Exact TP; unusual spelling alone is not an annotation-path error. |
| Same repository: SQLite-module path ending `/sqlite/tables/Test.java:55` | Separate manifest file, SHA-256 `b37824861d181afc39f9d6b740a19c6245fafc6ecc53036c596f971c0e413916`. | Exact TP, included in the seven above. |
| `therepanic/trustwin-casino-project`: miner-module `NotificationsTable.java:56` | Correct `game-miner-service` path in reference and manifest; exact prediction. | TP. |
| Same repository: overgo-module `NotificationsTable.java:56` | Extra reference under `game-overgo-service`; historical source absent, no manifest entry or prediction. The correct miner reference already exists. | One FN. This is distinct from the MySQL filtering exception. |
| Same repository: tower-module `NotificationsTable.java:56` | Separate `game-tower-service` file in reference and manifest with exact prediction. | TP. |

The two SQLite details are subsets of the seven selected dialect cases, not additional reference events. In total, the targeted ledger contains 11 references: nine exact matches and two unmatched events. Machine-readable identities, spans, memberships, and matching checks are in `2026-11-17-step-2-accounting.json`.

The original held-out result remains 460 TP, 76 FP, and 63 FN. Omitting either exceptional reference mechanically changes only FN to 62; omitting both changes FN to 61. Those arithmetic sensitivities do not establish corrected truth or what the detector would have returned for the filtered MySQL file. They are not substituted into the manuscript's primary results.

Merely remapping the extra overgo path to the miner path would create two identical reference events competing for one prediction. Under one-to-one matching it would leave the original total unchanged. An actual reference repair must distinguish remapping from removing an extra record and requires its own auditable revision.

## Corpus and sample reconciliation

Independently joined all 15,931 frozen corpus flags, in order, to `analysis/corpus_flag_alignment.csv` and the 17,988-file source manifest. Project/path identities agree, every flag has manifest membership, and every archived source hash agrees with its manifest row. This checks archived membership rather than rereading physical Java source. It confirms the Phase 1 acceptance checks; it does not establish a successful response for every file or distinguish terminal failures from negative detections.

The set difference between `final-repositories.csv` and `final-repositories-corrected.csv` is exactly `Davincii254/Stroom`. It is absent from the union of the 61 annotated projects in the training, validation, and test CSVs. Its removal therefore did not alter those partitions. No broader clone-free claim follows.

## Revised aggregate counts

Extracted these literal records from cell 2 of `scripts/15-calculate-tool-localisation-corrected.ipynb` without executing the notebook:

| Class | TP | FP | FN | F1 from counts |
|---|---:|---:|---:|---:|
| Implicit Columns | 256 | 1 | 15 | 0.969697 |
| ID Required | 101 | 1 | 7 | 0.961905 |
| Keyless Entry | 49 | 16 | 0 | 0.859649 |
| Fear of the Unknown | 42 | 1 | 17 | 0.823529 |
| 31 Flavors | 38 | 1 | 1 | 0.974359 |
| Poor Man's Search Engine | 13 | 4 | 8 | 0.684211 |
| Rounding Errors | 13 | 0 | 3 | 0.896552 |

Totals are 512 TP, 24 FP, and 51 FN, implying support of 563. Micro F1 is 0.931756; reference-support-weighted F1 is 0.930902. These are different aggregates. The manuscript retains the pooled micro result as an optimistic, detector-informed count sensitivity. The compact class-level manuscript table remains scheduled for step 5.

No event-level revised reference or correction log survives, so these counts cannot establish whether a particular reference was added, removed, or remapped. The new reporting avoids implying a released replacement dataset.

## Verification and limits

- Two reviewers independently established the repeat-annotation pairing error. The source semantic inspection is not needed to establish that counting bug.
- The recount script checks the actual frozen sample counts and reproduces the historical row-order effect. Its output reproduces the stored JSON summary.
- Existing localisation helpers reproduce the unchanged primary 460/76/63 counts. Targeted path checks and revised-count arithmetic are recorded in the accounting JSON with input hashes.
- `make paper` succeeds. The affected error table and sensitivity/corpus tables fit their pages after the local placement change. The final PDF has no unresolved citations or references and no new overfull boxes. Two small pre-existing line-overflow warnings remain in Introduction lines 22–23 and Study Design lines 5–6.
- `git diff --check` passes. No frozen study datasets, archived notebooks, corpus flags, or primary result tables were changed. No model calls, new annotations, commits, pushes, or external publications were made.
- The source mount `/run/media/kristoi/9327-3833/repositories` is unavailable. Current remote source was not substituted for historical bytes. Source-level semantic reinspection remains an explicit limitation, not an unfinished reason to invent a causal label.
- The added local script, summary, and guide changes will need inclusion in the final published analysis/documentation revision before the manuscript's reproducibility links can expose this new recount. Existing pinned archives continue to identify the unchanged historical inputs.

# Original Opus Zero-Shot validation run restored

Date: 2026-10-04

## Resolution

The author identified the archived Opus Zero-Shot notebook as a later rerun rather than the run used in the reported comparison. At the author's request, restored `/home/kristoi/masters-thesis/scripts/backups/09-evaluate-prompting-strategy-opus-zs.ipynb` exactly from revision `112f3a4eac5fcdb27f380102c1b296d946128ada`.

Committed the restoration as `9913a7670fce52b135651f95ff18cd505c61b142`, **Restore original Opus zero-shot validation run**, and pushed `main` to `origin`. The remote branch was independently checked with `git ls-remote` and points to that full revision. Only the notebook is included in the commit; unrelated untracked files were left untouched.

## Preserved evidence

| Quantity | Restored notebook | Displayed article value |
|---|---:|---:|
| Runtime, seconds | 366.72 | 367 |
| Weighted precision | 0.8836 | 0.88 |
| Weighted recall | 0.8898 | 0.89 |
| Weighted F1 | 0.8839 | 0.88 |
| Completed files | 1,159 | 1,159 |
| Failed files | 0 | No change |
| Retries | 0 | 0 |
| Printed API cost, USD | 31.392120 | 31.39 |

The runtime and agreement metrics now match the reported values after rounding. The old 618.29-second runtime and 0.8830 recall belonged to the later rerun. The author also identified the published $29.97 cost as a manuscript error and requested the correct API cost, $31.39. The Opus Zero-Shot cost now matches the restored notebook after rounding.

The restored notebook's SHA-256 is `684337d2de7f9bee3096cbe6c2030d981928f6d670c4050e3935aa12f691f995`. Its bytes exactly match the specified historical revision, its JSON is valid, and every source cell is unchanged relative to the later-rerun notebook. Only stored execution evidence changed.

All 16 validation configurations still record 1,159 distinct completed files and exactly match the reconstructed validation inventory. No selected source paths, reference annotations, corpus flags, or generated CSV outputs changed.

## Applied documentation changes

- Removed the Opus runtime and recall discrepancy caveats from the manuscript and replication README.
- Restored the direct statement that Opus Zero-Shot completed in 367 seconds. Kept the accurate restriction of its runtime comparison to Zero-Shot configurations.
- Removed the Results cross-reference concerning discrepant archived summaries and the "Originally reported" qualifier from the configuration-table caption.
- Corrected the Opus Zero-Shot cost to $31.39 and GLM-5 Zero-Shot to $11.76. The author confirmed that the table uses OpenRouter-reported charges, including $26.16 for GPT-5.2 Zero-Shot and $81.43 for Opus Tree-of-Thought. Removed the notebook-cost comparison caveat and replaced the blanket VAT claim with the correct OpenRouter cost provenance. The existing limits on exact replay of original executions remain.
- Updated frozen study links throughout the manuscript and README to the published restoration revision. Its archive date is 4 October 2026. Every other tracked study file is unchanged from `d9b35e398a6deb544f913bdbc0b211ab38474a44`.
- Updated the Opus notebook input hash in `analysis/split_file_inventory_summary.json`. Checked every study input against the new frozen revision and every generated CSV against its previously recorded hash. The source recount was not repeated because code, file inventory, and source evidence are unchanged.

## Verification

The notebook restoration is byte-for-byte exact and the pushed branch is verified. All 26 study-input hashes match the new published revision, all 16 completed-file inventories match the 1,159-file frame, and every generated CSV hash is unchanged.

`make paper` succeeds and produces a 29-page PDF. Extracted PDF text confirms the direct 367-second statement, the revised table caption, and removal of the superseded discrepancy wording. The build has no undefined references or overfull boxes; only the pre-existing document-class name warning remains. `git diff --check` passes.

This report supersedes the Opus Zero-Shot runtime, recall, and cost findings in the earlier split-file audit's configuration-summary section. That section records the evidence observed before restoration and correction of the manuscript cost. The author clarified that OpenRouter-reported charges are authoritative for the table. Numerical differences from notebook-summed cost metadata do not indicate errors in those reported charges. The GLM-5 manuscript value was corrected from $11.77 to $11.76, and the cost-discrepancy caveats were removed.

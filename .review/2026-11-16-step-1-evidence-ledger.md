# Step 1: evidence and revision ledger

Date: 16 November 2026.

Status: complete. This step implements items 17, 21, and 35 only to the extent assigned to the evidence/revision reconciliation. Later wording, interpretation, and presentation work remains in the revision plan.

## Changes

- Corrected the displayed study-archive hash from `d9b35e3` to `9913a76`, preserving its existing destination and the October restoration.
- Replaced all four stale manuscript README targets at `4a3b4d5` with published documentation revision `09dd6965b4e95b92a132f3a3c866a6cd897811cd`. The visible documentation label now agrees with its target.
- Made the full 16-combination validation design explicit in Methods and linked its frozen notebook directory. No two-stage screening procedure was introduced.
- Added a linked 16-run evidence map to `analysis/README.md`, identifying each of the seven displayed table rows and its printed weighted precision, recall, F1, and runtime. A separate seven-row table distinguishes the article's OpenRouter charges from notebook-summed response costs.
- Preserved the separate historical analysis revision `bb3bf60`, held-out detector revision `80f3ff4`, corpus detector revision `245b50a`, and later released detector revision `cf82fe5`.

The new local README evidence map is not yet published. The manuscript pin resolves to an already published README containing the recovered-run documentation; it does not promise that the new local table exists at that older revision. The manuscript's separate validation-notebook link already exposes the complete frozen comparison. This step creates no commits, pushes, or external archive releases.

## Verification

1. Retrieved the published README at `09dd696` and compared it byte-for-byte with the corresponding Git object. It matches the README that was current before this step's additions. SHA-256: `78fcb5a60fb67b063913fef5c9f49b925c0fc306201838fb1d4752a5833180cc`.
2. Retrieved the published original Opus Zero-Shot notebook at study revision `9913a76` and compared its bytes with the local frozen study checkout. SHA-256: `684337d2de7f9bee3096cbe6c2030d981928f6d670c4050e3935aa12f691f995`, matching the October restoration record.
3. Checked all 27 recorded input hashes in `analysis/split_file_inventory_summary.json`. All match; the source snapshot was not re-enumerated because this step concerns archived evidence, not a new source recount.
4. Parsed the success logs from all 16 preserved validation notebooks using the existing inventory helper. Each records exactly 1,159 completed paths, and its set equals the validation subset of `analysis/split_source_manifest.csv`.
5. Extracted the stored weighted metric summaries and batch runtimes. Every notebook's weighted row has support 581. All seven displayed precision/recall/F1 values and runtimes match the article after its existing rounding. No notebook code or model requests were executed.
6. Preserved author-confirmed OpenRouter table charges from the October restoration. The new ledger records distinct notebook cost summaries without substituting them for billed charges. No new billing records were inferred.
7. Retrieved `package.json` at all three detector revisions to confirm public resolution. Retrieved the historical `src/prompts.ts` and `src/prompt-builder.ts` at both execution revisions and confirmed byte equality. Their respective SHA-256 values are `08fd0d14121d17dac9c8ab50915af9cf0e57b85ced9929c270d549b212b6b369` and `0c039411b4a01b330f7a4f1e563d48f2a479a8ef24396f1ea80b8060ff721d92`.
8. `make paper` succeeded, producing a 30-page PDF. Extracted text confirms the 16-combination statement and corrected visible hashes. PDF URL annotations confirm the updated README and study targets. The final build has no unresolved citations/references. Two small overfull boxes remain in unchanged passages: Introduction lines 22–23 and Study Design lines 5–6. No overfull box is reported in an edited paragraph.
9. `git diff --check` passed. Dataset, prediction, result-table, and analysis-code files were not modified.

## Evidence boundaries retained

The recovered sources establish the validation inventory and printed summaries; they do not reconstruct every original hosted-model request. Complete held-out/corpus payloads, backend snapshot identifiers, negative-response ledgers, and final-failure histories remain unavailable. Identical prompt-template source is distinct from verified identical complete submitted requests.

The primary results and seven-row validation table remain unchanged. Steps 2–8, including the approved 61/541 sensitivity analysis, have not been implemented in this step.

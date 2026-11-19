# Step 8 revision closure

19 November 2026

The revision plan is complete within the agreed scope of existing runs, annotations, and targeted reanalysis. The primary held-out and full-corpus result tables match their pre-revision values.

| Review items | Change and verification |
|---|---|
| 1–3, 13–15 | Clarified the ID Required naming rule, search variants and clause scope, schema evidence, file selection, key context, and truncation. Checked the boundary descriptions against the annotation flowcharts and detector prompts using the [Step 3 record](2026-11-17-step-3-operational-boundaries.md). |
| 4–5 | Added focused ORM and LLM comparisons. Checked that the paper credits prior PL/SQL localisation, describes its own one-to-one evaluation in jOOQ source, and explains what a deterministic comparison could measure. |
| 6, 30–31, 36–37 | Verified the compiled Karwin Chapter 19 postnote, IoU interval with an en dash, fragment rounding note, thesis section and appendix citations, and distinct OpenAI 2025a and 2025b labels. |
| 7–8, 12 | Verified split counts and class support from the frozen annotations. The partition objective is 0.5167739250 and all seven classes satisfy the split minima. Methods distinguishes sample-informed codebook development from later configuration selection. Results identifies the one-project and two-project support for 31 Flavors and Rounding Errors. |
| 9–10, 27 | Recomputed the four IoU rows and the 10,000-replicate project bootstrap. At IoU 0.50, confirmed 460 TP, 76 FP, 63 FN, and micro F1 0.869. The micro F1 percentile range is 0.820–0.912. Methods specifies how each metric handles undefined replicates. |
| 11, 17, 35 | Distinguished the study archive, run-specific source revisions, later detector release, and replication guide. Verified that the published guide at `80a9898` matches its Git object and includes the new checks. The PDF links to that release of the guide and analysis materials. The older exact-content and localisation pins still identify the historical analyses. |
| 16, 18–19, 24 | Clarified file and event weighting, rate domains, cutoff ties, and what identical source files establish. Joined all 15,931 flags to the 17,988-file manifest. Recomputed 15,355 exact-content union events, eight groups with differing event sets, and the representative-copy bounds of 15,340–15,349. Verified the seven frozen output checksums. |
| 20–23 | Confirmed all 16 validation notebooks used the same 1,159 paths and assessed precision and recall with separate overlap passes at IoU 0.50. The text now describes that rule alongside the distinct held-out procedure. Checked the seven-row comparison against the [validation evidence map](../analysis/README.md#validation-evidence-map). Summing all 602 per-repository analysis times gives 12,390.941 seconds, reported as 12,391. |
| 25–26, 32, 34 | Checked the [exception accounting](2026-11-17-step-2-annotation-reconciliation.md) and reproduced the repeat-annotation summary with 144 exact labelled matches and F1 0.938. Verified the four revised class rows against the notebook and confirmed unchanged prediction totals for each class. The revised aggregates give 512 TP, 24 FP, 51 FN, and micro F1 0.932. |
| 28, 33 | Recomputed the stored [sample sensitivity CSV](../analysis/corpus_sample_sensitivity.csv) byte for byte and checked all nine manuscript rows. The 61 and 541 subsets reconcile to the full frame. The broader ID Required and more repetitive Implicit Columns pattern persists outside the sample. The discussion identifies class-specific priorities for an independent audit. |

The [triage plan](2026-11-16-review-triage-and-fix-plan.md#disposition-of-all-follow-up-items) records why items 29 and 38–41 require no change.

## Build and layout

`make paper` produced a 33-page PDF. The build log has no unresolved citations, unresolved references, or overfull boxes. The template's existing document-class naming warning remains. PDF inspection confirmed table order, caption and figure agreement, working citation locators, and matching research-question wording in the Introduction and Results. Table 7 now precedes Table 8. The two narrow line overflows from earlier builds were removed. The published replication links expose the repeat-annotation and subset scripts and outputs. The local guide now also explains the validation overlap rule.

## Evidence limits

- The historical Java source mount was unavailable. File and span checks used the preserved manifests and outputs. The two out-of-frame test references remain in the primary false-negative count. Their source semantics would require the historical files.
- Complete request payloads, provider snapshots, negative responses, final failure records, and the effective frequency of truncation remain unknown. The records support recomputation from preserved outputs. End-to-end replay and completion-rate estimates require additional evidence.
- The detector-informed sensitivity retains aggregate counts. Verification of individual changes would require an event-level revision log. The available timing measure is the sum of per-repository analysis times. Total wall time and corpus charges remain unverified.
- Comparative advantage over a deterministic baseline, independent annotation validity, detector run-to-run variability, and corpus prevalence remain open empirical questions.

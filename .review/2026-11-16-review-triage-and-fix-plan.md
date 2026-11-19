# Review triage and revision plan

Date: 16 November 2026.

Status: all eight steps are complete. The [closure ledger](2026-11-19-step-8-closure.md) records the final checks and remaining evidence limits. The primary held-out and full-corpus results are unchanged. See also the [Step 1 evidence ledger](2026-11-16-step-1-evidence-ledger.md), [Step 2 reconciliation](2026-11-17-step-2-annotation-reconciliation.md), and [Step 3 operational-boundary checks](2026-11-17-step-3-operational-boundaries.md).

## Scope and decisions

Inputs:

- `reviews/Deep_review_2026_11_06.md`: original agentic review.
- `reviews/Deep_review_2026_11_06_analuus_2026_11_08.md`: follow-up analysis, whose item numbers are used below.
- Current manuscript and local analysis artefacts, checked against relevant October review records and the preserved study checkout at `/home/kristoi/masters-thesis`.
- The original thesis in `thesis/chapters/02_background.tex` and `thesis/references.bib`, added as a source for the related-work revision following the author's confirmation.

Three specialists independently assessed methods/statistics, execution provenance, and research positioning. This report consolidates their findings and checks the follow-up analysis against the current evidence rather than adopting its recommendations wholesale.

Decisions confirmed by the author during this session:

1. Use existing detector runs and annotations, with targeted reanalysis. Keep new experiments behind a separate decision gate.
2. Add a compact sensitivity comparison between the 61 annotated repositories and the 541 outside that sample, retaining all 602 as the primary RQ2 population. Compare breadth, repetition, and density; repeating every concentration and fragment table is outside the agreed addition.

Implementation should preserve the current RQs, historical operational definitions, and primary results. A discovered reproducible error must be reported explicitly with its consequences; preservation of the primary analysis must never be used to conceal a demonstrated error. No silent relabelling, resplitting, denominator substitution, or replacement of the original reference is permitted.

## Main assessment

The original review identifies genuine weaknesses in operational definitions, annotation independence, method specification, and reporting. Several are already disclosed but need a precise explanation where readers encounter the corresponding result. Others are optional improvements rather than defects.

The follow-up analysis correctly rejects several false alarms, but it has two important limitations. It relies partly on an outdated replication README, and it repeatedly treats deferring additional analyses as if it were scientifically required. The current records resolve some provenance concerns, while modest existing-data additions are feasible.

The strongest remaining scientific limitation is the absence of a deterministic baseline. Clarifying the text can establish an honest agreement-and-distribution study. It cannot establish an LLM advantage in accuracy, cost, or runtime. A baseline remains a separate research decision, not a defect that wording repairs erase.

## Corrections to the supplied analyses

### Preserve recovered evidence

The original Opus Zero-Shot validation notebook was restored at study revision `9913a7670fce52b135651f95ff18cd505c61b142`. The October restoration record documents the author's identification of the original run and confirmation of the cost source. All 16 validation configurations match the reconstructed 1,159-file inventory. The original Opus run records 366.72 seconds, weighted F1 0.8839, and API cost $31.392120.

Evidence: `.review/2026-10-04-opus-original-run-restoration.md`, `analysis/README.md:32`, `analysis/README.md:56`.

The paper still displays `d9b35e3` while linking to `9913a76` in `paper/main.tex:90`, and it points readers to the stale README revision `4a3b4d5`. Correct the labels and documentation pin. Do not revert the study archive to `d9b35e3` or restore the follow-up analysis's obsolete uncertainty about the validation frame and Opus runtime.

Validation-table costs use author-confirmed OpenRouter charges. Some notebook-summed metadata costs differ; the October record already resolves which source is authoritative. Preserve that distinction rather than reopening the author's settled decision.

### Describe revised counts accurately

The corrected-localisation notebook contains manually supplied class-level TP/FP/FN counts. It does not preserve a revised event-level dataset that can be rematched. Current descriptions of a revised “set” of 563 reference events/spans imply stronger artefacts than survive.

Evidence: `/home/kristoi/masters-thesis/scripts/15-calculate-tool-localisation-corrected.ipynb`, `.review/2026-10-04-split-file-recount.md:119`, `paper/sections/03_study_design.tex:132`, `paper/sections/04_results.tex:80`.

Report detector-informed revised counts and the limited audit trail. A compact class-level table is feasible, but it must not imply an independently validated or reconstructable replacement dataset.

### Correct the localisation comparison

The PL/SQL paper by Sousa et al. asks for smell identifiers and line locations. The introduction has been corrected, but `paper/sections/02_background_related_work.tex:92`, `:117`, and `:125` still risk contrasting prior classification with this study's localisation.

Frame the contribution around jOOQ DSL/generated-schema source, the seven operationalised classes, and occurrence-level span matching. Do not imply that source-location output itself is absent from prior LLM studies.

### Keep the source-exception audit open

An excluded MySQL `Test.java` reference mechanically contributes an unmatched event, and a `NotificationsTable.java` reference uses a different module path from the prediction/manifest. Other dialect/path variants also need inspection. Counting these rows is insufficient to establish that each annotation is semantically valid or that filtering alone explains each mismatch.

Evidence: `analysis/split_annotation_frame_exceptions.csv`, `/home/kristoi/masters-thesis/datasets/test-set.csv`, `.review/2026-10-04-split-file-recount.md`.

The retained source snapshot at the historical media path was unavailable during this check. Locate and inspect the evidence before adding a causal error explanation or a counterfactual score. If it remains unavailable, state exactly which mechanical facts are verified and which source-level conclusions cannot be checked.

## Step-by-step implementation plan

### 1. Establish a consistent evidence and revision ledger

Items: 17, 21, 35; prerequisites for 15, 20–23, and 36.

Files: `paper/main.tex`, `paper/sections/03_study_design.tex`, `paper/sections/06_threats_to_validity.tex`, `analysis/README.md`; a compact verification record under `.review/`.

- Retain study revision `9913a76`; correct every displayed hash to match its actual target.
- Identify a published documentation commit containing the recovered-run information and update all stale README links consistently. Keep historical analysis/code pins separate from the documentation pin.
- Map the seven displayed validation rows to the full 16-run archive. Record metric/runtime sources and the distinct dashboard cost source.
- Distinguish run-specific detector revisions `80f3ff4` and `245b50a` from the later release `cf82fe5`.
- Preserve the genuine limits: complete payloads, final-failure records, and negative-response ledgers were not retained.

Done when every revision label resolves to the intended object, the full matrix is traceable, and no new prose resurrects a resolved provenance discrepancy. Updating remote archives or pushing a documentation commit requires a later explicitly authorised implementation action; this plan does not publish anything.

### 2. Reconcile annotation and file-frame exceptions

Items: 13, 25–26, 32, 34; additional revised-count provenance issue.

Files: `analysis/split_annotation_frame_exceptions.csv`, existing summary artefacts, `paper/sections/03_study_design.tex`, `04_results.tex`, `06_threats_to_validity.tex`.

- Inspect existing source/path/span evidence for the skipped MySQL table, NotificationsTable module mismatch, and suspicious dialect/path variants. Record whether each reference was included in the primary denominator, whether it matched, and which causal interpretation is actually supported.
- Reconfirm the existing reconciliation: all 15,931 corpus flags fall inside the reconstructed 17,988-file frame. State that this answers numerator/frame membership, not request-completion success.
- State that late removal of `Davincii254/Stroom` did not change the 61-project annotation sample or its split; do not generalise this to clone-free partitions.
- Make the repeat-annotation scope explicit: original 19-class scope, 15 observed classes across the two passes, and 63 of 64 originally unannotated files remaining unannotated.
- Replace revised-dataset implications with revised-count wording. Extract and verify the four affected classes' archived aggregates; distinguish pooled micro F1 from weighted F1.
- Keep disagreement mechanisms illustrative. Add useful residual FP/FN counts without inventing an exhaustive causal taxonomy.

Done when the exception ledger distinguishes verified counting facts from source-level interpretations, all revised values have a source, and the primary/reference-sensitivity distinction is explicit. If an actual input error is established, present its impact separately and transparently before deciding whether a corrected analysis should supplement the primary result.

### 3. Repair operational definitions and the independence claim

Items: 1–3, 8, 12, 14–15.

Files: `paper/sections/02_background_related_work.tex`, `03_study_design.tex`, `06_threats_to_validity.tex`.

- Explain near ID Required's definition that the standalone `id` naming condition is deliberately broad and does not establish an unsuitable surrogate key.
- Include substring convenience methods in Poor Man's Search Engine. Describe the shared unresolved-input convention and any material differences between the archived decision tree and prompts; do not claim complete equivalence.
- Describe the verified 31 Flavors range/span and Keyless Entry key-kind prompt imprecisions. Distinguish deliberate broader prompt coverage from those omissions, and preserve the shared query-nullability requirement confirmed by the author despite its implicit flowchart representation.
- Explain which schema evidence is present in retained table source and attached Keys context. Standalone EnumType implementations are excluded. A non-NULL default does not prevent an explicit NULL.
- Clarify that codebook refinement used the full annotation sample before partitioning. Later prompt iteration and model selection excluded test projects, but inherited operational rules were sample-informed.
- Describe lexical file/source-role selection, Keys selection by longest character-level relative-path prefix, and tie handling.
- Describe the historical corpus revision's character-budget truncation policy. Its default Claude heuristic is 240,000 characters unless overridden; target source has priority over Keys context. Distinguish implemented policy from unknown effective truncation frequency.

Done when definitions, supplied context, historical prompts, and claims about held-out independence agree. Preserve the historical definitions rather than narrowing them retrospectively to improve apparent validity. Use compact definitions plus links for full implementation details.

### 4. Specify the existing quantitative methods precisely

Items: 7, 9–10, 16, 18–19, 24, 27.

Files: `paper/sections/03_study_design.tex`, `04_results.tex`, `06_threats_to_validity.tex`; existing analysis code as the authority.

- Give the partition objective as the sum across classes of squared coefficients of variation over the three split occurrence counts, using population standard deviation. Include the candidate constraints: at least eight training occurrences and at least one validation and one test occurrence per retained class. Verify the displayed score against stored output/table counts.
- Identify the matching algorithm as maximum-cardinality matching using augmenting paths. Sorted adjacency lists determine traversal; they do not make it greedy or optimise total matched IoU.
- Define precision, recall, and F1 denominator failures separately. Explain metric-specific exclusion of undefined bootstrap values and point to defined-replicate counts already produced by the script.
- Specify inverse file-copy weights and inverse event-reporting-copy weights separately. These denominators differ when identical source files have inconsistent outputs.
- State the domains of breadth/density and repetition; zero flagged files makes repetition undefined.
- Clarify deterministic cutoff membership versus bounds over all cutoff-tie selections.
- Explain that eight inconsistent source-content groups are not verified identical complete requests and cannot identify causes or estimate run-to-run variance.

Done when the text matches existing algorithms without unnecessary algorithm changes. Do not add macro bootstrap intervals or rare-class interval tables by default; existing class-level outputs can be linked. No resampling method supplies additional independent project support.

Verification: the seven partition-table rows satisfy the per-class minima and give a score of 0.5167739250, which rounds to the notebook’s 0.5168. The localisation script reproduced the primary counts and all three pooled bootstrap intervals. The corpus summary confirms eight groups with inconsistent event sets. The paper built with the two existing line-overflow warnings.

### 5. Add the agreed existing-data results and improve selection reporting

Items: 8, 20–23, 26–28, 33.

Files: a small extension to existing corpus analysis or a focused script under `analysis/`, reproducible outputs, `analysis/README.md`, `paper/sections/04_results.tex` and `05_discussion.tex`.

- Build explicit 61/541 membership from the annotated partitions, checking disjointness and union with the 602-project corpus.
- Reaggregate eligible-file counts, flagged-file counts, and flag counts from `analysis/corpus_phase2_by_repository.csv`. Compare the two dominant class/role patterns and pooled all-class density; retain the underlying counts, not only percentages. Preserve existing role eligibility and zero/undefined rules. Do not average repository percentages to obtain pooled breadth.
- Produce a compact comparison of breadth, repetition, and density for the annotated subset, the remaining subset, and the full corpus. Include the class/role denominators so different schema/application composition remains visible. Inspect whether any difference is driven by source-role composition before interpreting it.
- Retain 602 as primary. Report whether the main breadth/repetition pattern persists outside the sample; a change is a result, not something to normalise away. This remains sensitivity of detector output, not independently validated transfer performance.
- Add the compact four-class detector-informed revised-count sensitivity table, with a caption stating the unchanged predictions and limited revision audit trail.
- Add a short result-level explanation of one-project 31 Flavors and two-project Rounding Errors support.
- State that all 16 model/prompt combinations ran and seven are displayed. Describe observed model/configuration/service combinations and the pragmatic selection tradeoff, without inventing a prespecified weighted rule or a two-stage protocol.
- Retain the seven-row main validation table and link the full archive. Use more precision only from preserved original summaries when it resolves an actual ambiguity; do not create unwarranted equality from rounded ties.
- Report the preserved 12,391 seconds, if included, as summed per-repository analysis time. No verified corpus-dollar total or exact end-to-end wall time has been identified; do not extrapolate from test cost.

Done when the new aggregation is reproducible, subset counts reconcile to full-corpus counts, weighting/denominators are explicit, and the prose reflects the actual sensitivity result. Limit the added analysis to the agreed metrics; a full new set of decile and fragment tables is unnecessary.

Verification for step 5: the subset script reproduces the saved CSV and verifies that the 61 and 541 repository counts sum to the full corpus for all three analysis rows. The nine manuscript rows match the CSV and the four revised class rows match the notebook counts. The paper builds with the two existing line-overflow warnings.

### 6. Correct scientific positioning and integrate related work

Items: 4–5, 20, 28, 33; additional PL/SQL-localisation correction.

Files: `paper/sections/01_introduction.tex`, `02_background_related_work.tex`, `05_discussion.tex`, `06_threats_to_validity.tex`, `07_conclusion.tex`, and abstract as needed.

- Repair the recognition-versus-localisation comparison throughout the background/table. Claim the jOOQ representation and explicit occurrence-matching evaluation, with the actual seven-class scope.
- Balance the AST/API-rules comparison: local naming/projection conditions are feasible deterministic targets; some other decisions require contextual interpretation. Dominant-class or fragment shares do not establish the percentage of cases that a baseline would detect.
- State that no deterministic baseline was evaluated, so current results do not quantify an LLM advantage. Keep the separate research gate visible in the plan, not as a long defensive passage in every manuscript section.
- Add two focused related-work connections after checking primary sources: Chen et al.'s hybrid ORM redundant-access analysis and Silva et al.'s Java smell study. Reuse the existing Silva bibliography entry. Do not describe Chen as a source-only jOOQ detector or imply an exhaustive survey.
- First inspect the original thesis's literature discussion and existing bibliography for further directly relevant work, including Sadik and Govind, Gomes et al.'s Attentionsmelling, and the PL/SQL prevalence study by Almeida Filho et al. Verify the primary sources and select only those that add a distinct comparison; their presence in the thesis or bibliography alone does not justify adding them all. Use the thesis's Hibernate/jOOQ distinction where helpful, while retaining the need for empirical ORM-analysis literature.
- Link lower-agreement corpus classes to the existing disagreement discussion with at most a concise bridge. Do not transfer held-out precision to corpus false-positive fractions.
- Consolidate overlapping limitations across Methods, Results, Discussion, and Threats. Preserve the October readability improvements and the user's accepted introduction/contribution wording except where evidence requires a substantive correction.

Done when no claim implies intrinsic model superiority, independently developed operational definitions, corpus prevalence, or classification-only prior work without evidence. Necessary qualifications should be near the claims they change; implementation minutiae can remain in the replication guide.

Step 6 integrates Chen’s hybrid ORM analysis, Silva’s prompt comparison, and Gomes’s investigation of code metrics and prompt context. Sadik and Govind and the earlier PL/SQL prevalence study were considered. The retained sources keep the comparison focused on representation, output, and evaluation. The discussion states the need for a deterministic comparison to measure any LLM advantage.

### 7. Fix bibliography, labels, and small presentation issues

Items: 6, 30–31, 34–37.

Files: `paper/references.bib`, `paper/main.tex`, relevant section citations/captions.

- Attach Karwin Chapter 19 only to the Karwin citation, not to the grouped jOOQ reference.
- Add a complete thesis bibliography entry and cite it where methods rely on its dataset-creation chapter. Preserve the existing institutional link.
- Normalise corporate OpenAI authors and let BibTeX generate distinct 2025a/2025b labels; do not hardcode suffixes.
- Add a short rounding note to the fragment table without changing correct counts or percentages.
- Fold “skips” to “skipped” into the substantive exception rewrite. The numeric-range source already uses `--`; verify rendering but do not duplicate a completed fix.
- Make resource links readable as repository plus revision, while retaining clickability and distinct source/documentation revisions.

Done when compiled citation labels are unambiguous, citation postnotes attach to the intended source, and all visible resource identities match their links.

Verification for step 7: the compiled paper shows OpenAI 2025a and 2025b, assigns Chapter 19 to Karwin, and renders the IoU interval with an en dash. The thesis citations give the relevant dataset-creation sections and appendices. The visible resource descriptions and short revisions correspond to their PDF link targets. The existing wording already describes the MySQL table as excluded by the path filter.

### 8. Rebuild and audit the complete revision

Dependencies: steps 1–7.

- Run the focused analysis checks and assert subset/full reconciliation, original-metric preservation, and correct revised-count arithmetic.
- Build with `make paper`; check unresolved citations/references, bibliography suffixes, table placement, and overfull boxes introduced by the changes.
- Review the PDF passages/tables affected by longer definitions, equations, and links. Confirm source/figure/caption agreement.
- Search for stale independence/provenance/localisation claims and repeated defensive qualifications. Keep RQ wording consistent across introduction and results headings.
- Produce a short closure ledger mapping each accepted finding to the change and validation evidence. Record unresolved historical limitations explicitly. Do not claim that editorial fixes resolve missing baseline or independent-annotation evidence.

Done when the analysis artefacts, paper, replication instructions, and closure ledger agree and the final PDF is readable.

Verification for Step 8 is in the [closure ledger](2026-11-19-step-8-closure.md). The final PDF builds without unresolved references, unresolved citations, or overfull boxes.

## Disposition of all follow-up items

| Items | Decision | Planned destination |
|---|---|---|
| 1–3 | Accept definition/evidence clarifications; preserve historical boundaries. | Step 3 |
| 4 | Accept balanced positioning and explicit absence of baseline; new baseline remains separately gated. | Step 6 |
| 5 | Accept focused primary-source related-work additions. | Step 6 |
| 6 | Accept citation-postnote fix. | Step 7 |
| 7 | Accept exact objective and constraints. | Step 4 |
| 8 | Existing disclosure is partial; add concise support context near results. | Steps 3, 5 |
| 9–10 | Clarify actual bootstrap/matching rules; no algorithm bug established. | Step 4 |
| 11 | Disclose genuine historical logging limit; do not infer full success. | Steps 1–2 |
| 12 | Accept high-priority independence correction. | Step 3 |
| 13–16 | Accept scope/filter/context/weighting details with historical version distinctions. | Steps 2–4 |
| 17 | Revise using recovered provenance; consolidate repetition and retain real payload limits. | Steps 1, 3 |
| 18–19 | Accept concise mathematical/tie-rule clarification. | Step 4 |
| 20 | Clarify observed configuration comparison; matched-budget reruns are separately gated. | Steps 5–6 |
| 21 | Full 16-run grid exists; reject invented two-stage design and obsolete reconstruction caveat. | Steps 1, 5 |
| 22 | Explain pragmatic tradeoff; no invented prior weights. Original precision is available where useful. | Step 5 |
| 23 | Preserved summed runtime is usable with correct label; no invented corpus cost. | Step 5 |
| 24 | Clarify source-content equality versus whole-request equality; no causal/variance allocation. | Step 4 |
| 25 | Keep illustrative mechanisms; audit residual facts without inventing exhaustive causes. | Step 2 |
| 26 | Add archived class aggregates with revised-count provenance, not a replacement-dataset claim. | Steps 2, 5 |
| 27 | Existing class bootstrap outputs can be linked. No new macro-interval table by default. | Step 4 |
| 28 | Corpus overlap is legitimate for RQ2; author approved compact 61/541 sensitivity. | Step 5 |
| 29 | Reject alleged runtime contradiction; no invented network-cause explanation. | No special fix |
| 30 | Already corrected in LaTeX source. | Final rendering check |
| 31 | Accept short rounding note; figures are already correct. | Step 7 |
| 32 | Accept reconciliation; source-level explanation of exceptions remains conditional on verification. | Step 2 |
| 33 | Existing discussion covers much of it; add only a useful bridge. | Step 6 |
| 34 | Accept tense correction within substantive rewrite. | Steps 2, 7 |
| 35 | Reject missing-links claim; fix genuine label/pin problems without reverting restored archive. | Steps 1, 7 |
| 36–37 | Add thesis citation and repair automatic corporate-author/year disambiguation. | Step 7 |
| 38 | Reject unsupported access-date change. | No fix |
| 39–41 | Reject hallucination verdicts: these are real software/documentation/service sources. | No fix required |

## Thesis literature addendum

The thesis inspection confirms that a small addition is useful, rather than restoring a general LLM overview. Most of its static-analysis and prompting background already appears in the article.

| Source | Decision and role in step 6 |
|---|---|
| Gomes et al., *Attentionsmelling* (`DBLP:conf/sbes/GomesSMP25`) | Strongest additional candidate. Already in both bibliographies, although unused in their prose. The publisher abstract describes GPT-4 evaluation for Long Method, God Class, and Feature Envy under four setups varying supplied definitions, context/metrics, and hyperparameters. Add a concise connection beside Silva to contextualised/prompt-sensitive smell detection; distinguish its task and evaluation from jOOQ occurrence matching. |
| Sadik and Govind (`sadik2025benchmarking`) | Directly cited in the thesis's LLM overview and analysis. The primary paper benchmarks smell detection across models and languages using constructed application implementations. Include selectively if it adds a distinct comparison, without comparing its F1 directly with this study. Its existing arXiv-only bibliography entry needs publication-metadata verification: the EASE 2025 record lists pages 969–975 and DOI `10.1145/3756681.3756993`. |
| Almeida Filho et al., PL/SQL smell prevalence (`DBLP:conf/iwpc/FilhoMVMSMR19`) | Optional predecessor to the PL/SQL LLM work. Verify the full paper before describing Manduka's implementation or outputs. Do not inherit the thesis's assertion about present tool availability. |
| Meincke et al., reasoning-prompt report (`DBLP:journals/corr/abs-2506-07142`) | Optional support for distinguishing explicit CoT prompts from internal reasoning modes. It does not explain the causes of the current timing/agreement differences. No additional prompting subsection is needed. |
| Chen et al. 2021 code synthesis and RepoBench | Do not reuse as evidence of smell detection or localisation. Their tasks are program synthesis and repository-level code completion. |
| Generic prompting surveys and Hibernate/jOOQ explanation | Most are already covered. Reuse only a short representation distinction where it helps introduce the separate empirical ORM study by Chen et al. The thesis ORM passage does not itself fill that empirical related-work gap. |

Primary sources checked for the strongest additions: [Gomes publisher abstract](https://sol.sbc.org.br/index.php/sbes/article/view/37005), [Sadik and Govind paper](https://arxiv.org/html/2504.16027v1). Their BibTeX entries are already present in `paper/references.bib:896` and `:1038`. Planned Chen/Silva coverage remains; prioritise Gomes over padding the paragraph with every candidate.

Do not carry over the thesis's speculative prediction that newer models would improve the earlier results, blanket claims that deterministic methods lack context, or cross-study F1 comparisons as evidence of superiority. The article already states the single-request prompting scope and that developer review utility was not evaluated, so no additional paragraphs are needed for those points.

## Separate research gates

These are not authorised as part of the main revision:

- **Deterministic baseline:** needed to measure comparative LLM value. Before implementation, decide covered classes/rules, development evidence, span granularity, and fairness. Designing rules after inspecting test errors must be disclosed; it is not equivalent to a baseline developed independently of the test set.
- **Independent annotation or new evaluation data:** needed for stronger reference validity or genuinely independent operational-definition testing. Existing-data reaggregation cannot supply this evidence.
- **New split or repeated/matched-budget model runs:** needed only for corresponding stronger generalisation, variance, or controlled-comparison claims. They would change the study and cannot repair missing historical execution logs.
- **Permanent archival publication/DOI:** potentially useful, but publishing a new archive is a separate external action. No DOI should be invented and no archive should be published as a side effect of editorial repairs.

The current scope intentionally leaves these evidence gaps visible. Whether the resulting paper is sufficient for a particular venue remains a separate judgment; the plan makes no acceptance guarantee.

# ESE restructuring proposal

Date: 2026-08-27

Scope: `paper/`, with `.review/paper-old.pdf` used only as a structural reference.

## Recommended paper identity

Reframe the manuscript from a thesis about building a tool into an empirical study in which an occurrence-validated LLM detector is the measurement instrument for mining SQL antipatterns in jOOQ repositories.

Candidate title: *Detecting SQL Antipatterns in jOOQ Code: An Occurrence-Level Evaluation and Repository Study*.

Central claim: occurrence-level validation can make an LLM detector a defensible repository-mining instrument, but corpus findings must be reported as detector outputs and interpreted according to class-specific measurement quality.

## Recommended research questions

1. How accurately does the selected LLM-based detector localise seven operationalised SQL antipatterns in held-out, project-disjoint jOOQ-based Java code?
2. How frequently does the validated detector identify each SQL antipattern across the analysed open-source jOOQ corpus, and how are the detections distributed across projects?
3. Through which recurring jOOQ API patterns do the detected query antipatterns manifest?

Treat model and prompt comparisons as instrument-configuration steps, not contribution-level research questions. Remove co-occurrence as a primary research question unless it is recomputed over all analysis units with project-size or exposure controls. Otherwise retain it only as exploratory analysis or an online resource.

## Target structure

1. Introduction
   - Problem and practical setting
   - Why dynamic jOOQ query construction complicates extraction and localisation
   - Evidence gap and central claim
   - Three research questions and contributions
2. Background and related work
   - SQL antipattern detection and relevant units of analysis
   - jOOQ and dynamic query representation
   - Static, API/AST, and LLM-based code analysis and localisation
   - Short comparison table that makes the gap explicit
3. Study design
   - Study overview and pipeline
   - Repository mining and target population
   - Operational definitions of the seven antipatterns
   - Sampling, reference annotation, and reliability
   - Project-disjoint data partitioning
   - Detector configuration, including model and prompt selection
   - Localisation matching and evaluation measures
   - Corpus measures and API-pattern coding
   - Reproducibility and AI-use disclosure
4. Results
   - RQ1: held-out localisation validity and class-specific errors
   - RQ2: detected prevalence and project distribution
   - RQ3: jOOQ API manifestations
   - Optional exploratory co-detection analysis outside the RQs
5. Discussion
   - What occurrence-level validation adds
   - Relationship to existing extraction, rule-based, and LLM approaches
   - Implications for hybrid detectors and jOOQ guidance, clearly marked as implications
6. Threats to validity
   - Construct, internal, external, conclusion, and reliability validity
7. Conclusion
8. Statements and declarations

The previous paper's Introduction / Background / Study Design / RQ-organised Results / Discussion / Threats / Conclusion sequence is a useful routing map. Do not reuse its prose, authorship, or unsupported claims.

## Structural changes

- Merge the current dataset, prompting, tool-development, and project-analysis chapters into one Study Design section ordered by the empirical pipeline.
- Replace the broad antipattern catalogue with a compact table covering only the seven evaluated classes. Move the full taxonomy, decision rules, and examples to the replication package or an online resource.
- Reduce the prompt-engineering tutorial and model comparison to a compact detector-configuration subsection and one selection table.
- Make the held-out occurrence-level evaluation the evidential hinge of the paper. Report original reference annotations as primary and any corrected-label analysis as an optimistic sensitivity analysis.
- Report absolute TP, FP, and FN counts and distinguish micro, macro, and weighted averages. Present occurrence matching as event matching rather than a confusion matrix because true negatives are undefined there.
- State the matching rule completely: repository/file, class agreement, IoU threshold, one-to-one assignment, and tie handling. Add IoU-threshold sensitivity if archived predictions permit it.
- Report corpus findings as detections or flags, not as the true prevalence of antipatterns. Preserve the target-population qualifiers for the mined GitHub projects.
- Replace the current prevalence headline with counts, projects flagged, percentage of projects, and concentration. Do not use occurrences per 100 jOOQ references as a statement-level rate.
- Describe API tables as manifestation distributions, not risk or causal estimates, because API-use denominators are absent.
- Remove the thesis reflection chapter, thesis-navigation language, and most uses of “this thesis.” Convert the summary chapter into a short conclusion.
- Move the inventory of LLM use into a compact Methods disclosure that distinguishes research use, coding assistance, drafting, and copy editing.
- Restrict new prose to the abstract, introduction framing, transitions, short RQ answers, discussion synthesis, conclusion, captions, and declarations. Relocate existing method and results paragraphs as intact blocks wherever feasible.

## Evidence changes with the highest value

1. Add an independent, class-stratified second-annotator audit and adjudication if feasible. The current 30-day self-reannotation measures temporal self-consistency, not independent correctness. Call the labels “reference annotations,” not “ground truth.”
2. Audit a stratified sample of positive detections and negatives from the 602-project corpus. Without this transfer check, the corpus section should make claims only about detector outputs.
3. Add a small deterministic API/AST baseline for the stable, rule-friendly patterns if feasible. If no baseline is added, avoid claims that the LLM outperforms or bypasses static analysis.
4. Add IoU-threshold sensitivity and, if budget permits, repeated selected-model runs or project-level bootstrap intervals. Otherwise describe prompt/model comparisons as descriptive.
5. Recompute co-detection over all projects or files with size/exposure adjustment, or demote it from the main research questions.
6. Freeze the replication package in a DOI-backed archive with repository commits, raw predictions, retries, model/provider identifiers and dates, parameters, prompts, dependency locks, and analysis scripts.

## Technical corrections before submission

- Treat conditional probabilities as descriptive frequencies, not evidence of dependency or prediction.
- Recompute Spearman associations over all analysis units rather than only units containing either antipattern.
- Correct the aggregate localisation labels: the current “Total” appears to be a weighted mean, not a micro average.
- Resolve the apparent conflict between the claimed 98% API-label coverage and the reported 5.9%/6.3% uncategorised shares.
- Remove the plain-SQL density comparison unless numerator and denominator measure compatible quantities.
- Avoid “significant” and “margin of error” unless supported by inferential analysis.
- Disclose that the split was selected from many seeds to balance class support, including the final 21/20/20 project allocation.
- Call the single-prompt strategy “ToT-inspired” unless it performs an actual iterative tree search.
- Remove practical-utility, CI-actionability, and developer-benefit claims that were not evaluated.
- Avoid first-of-its-kind claims without a systematic literature search.

## Main paper versus online resource

Keep in the paper: one study-pipeline figure, one operational-definition table, one configuration-selection table, one held-out per-class table, one prevalence table, one combined API-pattern table, and a concise error-mechanism table. A practical editorial target is about 12,000–18,000 words or 30–40 pages including references; this is not an ESE limit.

Move online: search strings and omissions, full codebook and decision trees, all prompts, complete model/prompt results, classification-only evaluation, matching diagnostics, full co-detection matrices and heatmaps, CLI configuration, and implementation details.

## Journal-compliance checklist

- Write a 150–250-word abstract and retain 4–6 keywords.
- Use no more than three heading levels.
- Complete all applicable Statements and Declarations, including the mandatory data-availability statement.
- Document substantive LLM use in Methods.
- Ensure cited supplementary files are labelled as online resources and submitted in publication-ready form.
- Keep corresponding-author contact details and affiliations complete.

## Suggested implementation order

1. Lock the paper's claim, three RQs, and target outline.
2. Create the new section skeleton and move existing paragraphs without rewriting them.
3. Build the compact evidence tables and move detailed material online.
4. Correct the measurement and statistical claims.
5. Decide which additional validation work is feasible.
6. Write only the new connective and framing prose.
7. Complete declarations, reproducibility material, and a final ESE compliance pass.

## Incremental execution plan

Each step below should leave a compilable paper and can be reviewed or committed separately. Do not rewrite relocated prose during the structural steps.

### Step 1: Record the baseline and map the source material

Status: completed on 2026-08-27. See `2026-08-27-ese-step-1-baseline-map.md`.

Actions:

- Record the current page count, section order, figures, tables, appendices, and unresolved LaTeX warnings.
- Create a paragraph-level routing map from the current chapters to the proposed sections.
- Mark each block as keep in main paper, move online, condense later, or remove.
- Use `.review/paper-old.pdf` only to check the proposed order and RQ grouping.

Completion check: every current section, figure, and table has a destination. No manuscript text has changed.

### Step 2: Lock the paper's claim, scope, and research questions

Status: completed on 2026-08-27. See `2026-08-27-ese-step-2-paper-identity.md`.

Actions:

- Adopt one title and the one-sentence central claim.
- Replace the five thesis RQs with the three paper RQs.
- Define the target population precisely.
- Decide that model and prompt comparisons configure the detector rather than answer standalone RQs.
- Demote co-detection to exploratory analysis unless a corrected analysis will be performed.

Completion check: the title, claim, contribution list, and RQs fit on one page and use the same units of analysis.

### Step 3: Decide and perform the feasible evidence upgrades

Status: completed on 2026-08-27. See `2026-08-27-ese-step-3-evidence-freeze.md` and `../analysis/localisation_robustness.py`.

Actions:

- Decide whether an independent annotation audit, corpus transfer audit, deterministic baseline, repeated model runs, and project bootstrap are feasible.
- Run the selected additions before rewriting results.
- At minimum, add IoU-threshold sensitivity if the archived predictions support it.
- Record unavailable improvements as limitations rather than implied evidence.

Completion check: the final evidence set is fixed, and every planned quantitative claim has a corresponding analysis.

### Step 4: Correct the existing measurement and statistical analysis

Status: completed on 2026-08-27. See `2026-08-27-ese-step-4-measurement-corrections.md`.

Actions:

- Rename annotations, event-matching tables, and aggregate measures correctly.
- Recalculate micro, macro, and weighted results.
- Specify matching, tie handling, split selection, and class support.
- Resolve API coverage inconsistencies.
- Remove or repair the plain-SQL density comparison.
- Recompute co-detection with all analysis units and exposure controls, or remove it from the main analysis.

Completion check: tables, captions, and prose report the same quantities, and every statistical term has the meaning used in the analysis.

### Step 5: Create the new paper skeleton

Actions:

- Create the target section order: Introduction, Background and Related Work, Study Design, Results, Discussion, Threats to Validity, Conclusion, and Statements and Declarations.
- Move existing paragraphs into the new files as intact blocks according to the routing map.
- Keep temporary source comments showing each block's original chapter and section.
- Repair labels, references, bibliography inclusion, and compilation only.

Completion check: the paper compiles in the new order and contains the original prose, apart from mechanical reference fixes.

### Step 6: Reduce and refocus the background

Status: completed on 2026-08-28. See `2026-08-28-ese-step-6-background.md`.

Actions:

- Retain material needed to understand SQL antipatterns, jOOQ representation, detection methods, and localisation.
- Replace the broad catalogue with a compact table for the seven evaluated classes.
- Reduce the prompt-engineering tutorial to the concepts needed to understand detector configuration.
- Add a short comparison of static, API/AST, and LLM approaches that identifies the measurement gap.
- Move the full taxonomy and decision rules online.

Completion check: every background subsection supports a method choice or later interpretation, and no evaluated concept appears without definition.

### Step 7: Consolidate the study design

Status: completed on 2026-08-28. See `2026-08-28-ese-step-7-study-design.md`.

Actions:

- Order the preserved methods paragraphs by the empirical pipeline.
- Describe repository selection, operational definitions, sampling, annotation, partitioning, configuration selection, localisation matching, corpus measures, and API coding.
- Move implementation detail out of the main narrative unless another researcher needs it to reproduce a result.
- Add the substantive AI-use disclosure.

Completion check: a reader can reconstruct the study population, reference data, detector selection, evaluation, and corpus analysis without reading an appendix.

### Step 8: Rebuild the results around the three RQs

Status: completed on 2026-08-28. See `2026-08-28-ese-step-8-results.md`.

Actions:

- Present held-out occurrence localisation and class-specific errors under RQ1.
- Present detected counts, projects flagged, project percentages, and concentration under RQ2.
- Present recurring jOOQ API manifestations under RQ3.
- Put model and prompt comparisons before RQ1 as detector selection, not as a main result.
- Add a short, direct answer at the end of each RQ subsection.
- Report all repository findings as detections or flags.

Completion check: every result answers one RQ or is explicitly labelled configuration or exploratory analysis.

### Step 9: Write the discussion and threats to validity

Status: completed on 2026-08-28. See `2026-08-28-ese-step-9-discussion-validity.md`.

Actions:

- Organise the discussion around what occurrence-level validation adds, how the findings relate to existing detectors, and what the observed API patterns imply.
- Separate measured findings from proposed hybrid-detector and documentation implications.
- Organise threats under construct, internal, external, conclusion, and reliability validity.
- Cover annotation independence, transfer validity, class imbalance, model stochasticity, target-population limits, and commercial-model reproducibility.
- Remove the thesis work-process reflection.

Completion check: every interpretation points to a reported result, and every material unsupported inference is hedged, removed, or reframed as future work.

### Step 10: Rewrite only the framing and connective prose

Status: completed on 2026-08-28. See `2026-08-28-ese-step-10-framing.md`.

Actions:

- Rewrite the introduction around the problem, gap, central claim, RQs, and contributions.
- Add only the transitions needed to connect relocated paragraphs.
- Replace thesis-navigation language and remove remaining references to “this thesis,” except when describing prior dissemination.
- Write the conclusion from the direct RQ answers.
- Write the abstract last, after the claims and numbers have stabilised.

Completion check: the introduction, abstract, results answers, discussion, and conclusion state the same central claim without changing the substance of preserved paragraphs.

### Step 11: Reduce the main-paper tables, figures, and appendices

Status: completed on 2026-08-28. See `2026-08-28-ese-step-11-floats-online-resources.md`.

Actions:

- Keep the pipeline, operational definitions, configuration selection, held-out results, prevalence, API manifestations, and error mechanisms in the paper.
- Move full prompts, codebook, detailed comparisons, diagnostics, matrices, heatmaps, CLI material, and implementation detail online.
- Ensure every retained float is cited, interpreted, and placed after its first textual introduction.
- Cite submitted supplementary files as online resources.

Completion check: each retained float supports one claim, and the main PDF no longer contains thesis-scale appendices.

### Step 12: Complete reproducibility and journal declarations

Actions:

- Freeze the replication package with a DOI and record repository commits, raw predictions, model/provider identifiers and dates, parameters, prompts, retries, dependencies, and analysis scripts.
- Complete funding, competing interests, ethics, consent, author contributions, and data-availability statements as applicable.
- Verify the corresponding author, affiliations, abstract length, keyword count, and heading depth.

Completion check: all ESE submission fields can be completed from the manuscript and archived materials without placeholders.

### Step 13: Run the submission-readiness pass

Actions:

- Build the paper from a clean state and inspect the PDF.
- Audit terminology, RQ-to-result correspondence, cross-references, captions, citations, bibliography entries, and LaTeX warnings.
- Check that the abstract and conclusion use the final numbers.
- Search for residual thesis framing, causal overclaims, unsupported novelty claims, AI-writing patterns, and inconsistent labels.

Completion check: the paper compiles cleanly, all RQs are answered, all claims trace to evidence, and the ESE checklist passes.

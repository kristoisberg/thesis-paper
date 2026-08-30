# Audit of excessively careful wording

Date: 2026-08-30

Scope: `paper/main.tex` and `paper/sections/01_introduction.tex` through `07_conclusion.tex`

Status: report only. No manuscript files were changed.

## Verdict

The paper is overqualified. The main problem is not ordinary hedging such as “may” or “suggests.” It is repeated qualification. A boundary is defined in Study Design, repeated beside the result, added again at the end of a Discussion paragraph, and then explained once more in Threats to Validity. Many paragraphs therefore end by weakening the point they just made.

Four warnings account for most of the drag:

1. Corpus flags are not prevalence or API-risk estimates.
2. The reference came from one annotator, and its revision was detector-informed.
3. Each detector configuration was run once.
4. Missing artefacts prevent exact replay.

All four matter. None needs to appear throughout the paper. The clean placement rule is simple: define the unit or procedure once in Study Design, add a short qualifier at the first affected result, and explain the consequence in Threats to Validity. Discussion and Conclusion should then state what the evidence shows.

A focused edit should be able to remove roughly 700 to 1,000 words without weakening a claim. Most of the cut would come from duplicated cautions, repeated result summaries, and hypothetical study protocols.

## Highest-priority findings

### 1. The flags-versus-prevalence warning appears almost everywhere

Locations:

- `paper/main.tex:69`
- `paper/sections/01_introduction.tex:9,24`
- `paper/sections/03_study_design.tex:7,132,134`
- `paper/sections/04_results.tex:126,144,146,159,182,184`
- `paper/sections/05_discussion.tex:25,27,29`
- `paper/sections/06_threats_to_validity.tex:9`
- `paper/sections/07_conclusion.tex:7`

The warning appears as “detector outputs rather than prevalence estimates,” “true antipattern prevalence remains unmeasured,” “rather than API-specific risk,” and several close variants. The terminology already calls the observations “flags,” so most reminders add no new protection.

Keep one short sentence in the Abstract, define the measurement boundary at `03_study_design.tex:132–134`, and retain the full validity consequence at `06_threats_to_validity.tex:9`. Remove the other versions. A sufficient short form is:

> These unadjusted counts describe detector flags, not antipattern prevalence or API risk.

The current Conclusion is the worst placement. The paper ends by repeating what it did not measure instead of stating why the measured class differences and source-fragment patterns matter.

### 2. “One run” has become a ritual qualifier

Locations include:

- `paper/main.tex:69`
- `paper/sections/01_introduction.tex:9,14,23`
- `paper/sections/03_study_design.tex:5,112,114,126,132`
- `paper/sections/04_results.tex:3,7,12,29,31,38,113,115`
- `paper/sections/05_discussion.tex:11,13`
- `paper/sections/06_threats_to_validity.tex:17,31,33,39`
- `paper/sections/07_conclusion.tex:3,7`

The execution count should remain where the run is introduced. The stochastic limitation belongs at `06_threats_to_validity.tex:39`. Repeating “one selected-detector run” in the Abstract, Introduction, RQ, Results heading, result paragraph, caption, answer block, Discussion, and Conclusion makes a valid experiment sound perpetually provisional.

Remove “one run” from the RQ wording, captions, explicit RQ answers, Discussion recap, and Conclusion. Keep it in the method and at the first result.

### 3. The reference limitation is explained too many times

Single-annotator wording recurs in `paper/main.tex:69`, `01_introduction.tex:9,14`, `03_study_design.tex:52–60,118`, `04_results.tex:29,31,38`, `05_discussion.tex:11`, `06_threats_to_validity.tex:5,37`, and `07_conclusion.tex:3,7`.

The detector-informed revision is qualified at `03_study_design.tex:128`, `04_results.tex:58,63,80,82,84,86,90`, `05_discussion.tex:11`, and `06_threats_to_validity.tex:13`.

Keep the annotation procedure in Study Design. Keep one direct limitation in Threats. In Results, introduce the revised score as an “optimistic sensitivity analysis” and stop there. The four class-error paragraphs do not need to repeat “detector-informed review,” and the table caption does not need a second defense of the original reference.

A single methods sentence covers the revision:

> Because detector disagreements guided the revision, we treat the revised-reference result as an optimistic sensitivity analysis.

### 4. The output unit is defined long after the reader understands it

The distinction among file classification, class-labelled spans, occurrence matching, and corpus flags is developed at:

- `paper/main.tex:69`
- `paper/sections/01_introduction.tex:7,9,14,22–23`
- `paper/sections/02_background_related_work.tex:3,92,95,108–125`
- `paper/sections/03_study_design.tex:5,7,118–124,136`
- `paper/sections/04_results.tex:3,29,31,38,115`
- `paper/sections/05_discussion.tex:5,17–19`
- `paper/sections/06_threats_to_validity.tex:7`
- `paper/sections/07_conclusion.tex:7`

The formal definition at `03_study_design.tex:118–124` is necessary. The motivation at `02_background_related_work.tex:125` is useful. After that, “span-level agreement” is enough. The phrase “class-labelled span outputs later counted as corpus flags” can disappear.

### 5. Reproducibility disclosure interrupts the method repeatedly

Locations:

- `paper/sections/03_study_design.tex:110,112,114,132,140–142`
- `paper/sections/04_results.tex:12`
- `paper/sections/05_discussion.tex:13`
- `paper/sections/06_threats_to_validity.tex:39,41`

The dedicated reproducibility subsection at `03_study_design.tex:138–142` is the right home for the artefact inventory. The full list should appear there or in Online Resource 1, not in the model list, detector-execution paragraph, Results caption, Discussion, and Reliability Validity.

`03_study_design.tex:112` is the most painful paragraph in the paper. It mixes routing constraints, reasoning settings, temperature uncertainty, run count, selection criteria, notebook mismatches, and missing outputs. Reduce the article body to the design decision and preserved settings. Move provider-specific archival forensics to the supplement.

`03_study_design.tex:114` has the same problem. It mixes detector behaviour, differences in the released revision, missing binary identity, held-out execution, corpus execution, and missing prompt identity. Split procedure from preservation, then move preservation to the dedicated subsection.

### 6. Results are repeatedly reported before Discussion begins

The Results section states each result in prose, gives a table, adds a bold “Answer to RQ” block, repeats the result in Discussion, and states it again in Conclusion.

The easiest cuts are:

- delete `paper/sections/04_results.tex:115`
- delete `paper/sections/04_results.tex:148`
- delete `paper/sections/04_results.tex:186`

These answer blocks repeat the preceding subsection almost verbatim. If the journal requires explicit answers, invert the choice: keep each answer block and shorten the preceding recap. Do not keep both.

Discussion should cite the results and start with the interpretation. For example, `05_discussion.tex:5–7` can open with the actual insight: agreement varied more across classes than across tested span thresholds. It does not need to restate all pooled counts first.

## Section-by-section findings

### Abstract

`paper/main.tex:69` ends with two dense scope sentences after already defining the detector, reference, partition, and corpus results. Merge the final two sentences into one:

> Agreement varied substantially by class, so the corpus counts should be read as detector flags rather than prevalence estimates.

That preserves the important boundary and gives the Abstract a readable ending.

### Introduction

- `01_introduction.tex:5`: Delete “These are proposed explanations from the prior study rather than causal findings.” The preceding “suggested” and “may reflect” already calibrate the attribution.
- `01_introduction.tex:9`: The contribution paragraph reaches the study objective and immediately retreats into non-claims. State the objective positively and leave the full measurement boundary to Study Design and Threats.
- `01_introduction.tex:14`: RQ1 contains the run count, detector status, reference provenance, class count, and partition design. Shorten it to “What occurrence-level agreement does the detector achieve on held-out projects?”
- `01_introduction.tex:24`: Delete “bounded.” “Detector flags in 602 repositories” already states the scope.

### Background and related work

- `02_background_related_work.tex:9`: The antipattern versus code-smell distinction takes five sentences. Keep the definition only if the distinction drives later analysis. Otherwise reduce it to one or two sentences.
- `02_background_related_work.tex:92–125`: The representation and output-unit comparison is useful, but the prose, table caption, every table row, and closing paragraph all restate it. Keep the table and shorten the surrounding prose.
- `02_background_related_work.tex:29–48`: Do not simplify the operational definitions. These exclusions determine the labels and earn their precision.

### Study design

- `03_study_design.tex:5–7`: Cut the two closing meta-comments about why the sequence and units are valid. The workflow already demonstrates the separation.
- `03_study_design.tex:11–17`: Three consecutive paragraphs define the population and defend its exclusions. Define it once, describe the search, and move generalisability to External Validity.
- `03_study_design.tex:36`: The build and execution rationale repeats `03_study_design.tex:11–13`. Keep it in one place.
- `03_study_design.tex:50`: Retain allocation, seed, and sample counts. Remove the repeated defenses about stratum coverage and representativeness.
- `03_study_design.tex:54,60`: Two nearby paragraphs end with the same single-annotator limitation. Keep one short distinction here and the full treatment in Threats.
- `03_study_design.tex:92–94`: Keep the observation that project support is sparse. Delete the separate paragraph defending project-disjoint assignment.
- `03_study_design.tex:108`: State the three selection criteria once: model variation, identifiable revisions, and structured output. The explanation of why JSON Schema avoids free-form parsing is obvious.
- `03_study_design.tex:112–114`: Move provider settings and preservation gaps to a compact table or Online Resource 1. Keep only facts needed to understand selection and execution.
- `03_study_design.tex:126`: Define what the bootstrap range measures here. Do not also list every quantity it does not measure when Threats covers the consequence.
- `03_study_design.tex:132–136`: Explain what was counted. Do not spend equal space listing what was not counted. Line 136 is another RQ-to-unit roadmap and can be cut.
- `03_study_design.tex:142`: Compress the missing-artefact inventory in the paper. Preserve the full list in Online Resource 1.
- `03_study_design.tex:144`: Keep the AI-use disclosure. Its detail serves a reporting requirement rather than defensive prose.

### Results

- `04_results.tex:3`: Delete the sentence explaining why the section has its current order.
- `04_results.tex:7,12`: Let the selection paragraph end on the reason for choosing Zero-Shot. Put the replay note in the reproducibility section and stochastic uncertainty in Threats.
- `04_results.tex:29`: Replace the full RQ with a short heading such as “RQ1: Held-out occurrence-level agreement.”
- `04_results.tex:58,63`: Keep the original-reference qualification either in prose or in the caption, not both.
- `04_results.tex:80–88`: Five paragraphs replay nearly every row in the disagreement table and add line-range minutiae. Keep the main semantic and localisation mechanisms with one example each. Move the case inventory to Online Resource 1.
- `04_results.tex:90`: “Optimistic sensitivity analysis” is enough here. The mechanism is already in Study Design and Threats.
- `04_results.tex:111–113`: Report the robustness result and its main interpretation. The full confidence-interval taxonomy belongs in Threats.
- `04_results.tex:126,144,146`: Three warnings surround the RQ2 table. Keep one short caption note and the repository-size point. Remove the standalone prevalence paragraph.
- `04_results.tex:144`: The difference between 26.46 flags per repository and 26.51 per flagged repository adds no insight because 601 of 602 repositories were flagged. Keep the Keyless Entry contrast if distribution across flagged repositories matters; cut the rest of this precision unless a reviewer requested it.
- `04_results.tex:159,182,184`: Keep one API-denominator warning, not three.
- `04_results.tex:182`: The exhaustive inventory of low-frequency categories does not answer “which patterns are most frequent.” The table or supplement can carry these counts.
- `04_results.tex:115,148,186`: Remove the repeated answer blocks, or use them to replace earlier summaries.

### Discussion

This section needs the strongest rewrite. It currently behaves like a second Results section followed by a miniature grant proposal.

- `05_discussion.tex:5–7`: Lead with the class-versus-threshold insight. Remove the full metric recap.
- `05_discussion.tex:9`: Delete “They provide no evidence about model reasoning or training data.” The paper is not making that inference, so denying it adds noise.
- `05_discussion.tex:11–13`: Reduce to two claims. The detector-informed revision raises the estimate, and the validation data do not establish a stable prompt ranking. Do not repeat every F1-score, cost, runtime, and preservation gap.
- `05_discussion.tex:19–21`: Four negative formulations defend why prior approaches cannot be ranked. State the positive requirement once: a direct comparison needs the same files, labels, and matching rule.
- `05_discussion.tex:25`: Move straight from the recurring patterns to their value as audit strata. Do not repeat all RQ3 percentages and the API-risk warning.
- `05_discussion.tex:27–33`: Four paragraphs specify independent audits, deterministic and hybrid baselines, ablations, developer studies, taxonomy expansion, model comparison, query-builder transfer, and new categories. Keep the two highest-value next steps: an independent corpus audit and a same-task baseline. One short transfer sentence is enough if needed.
- `05_discussion.tex:29`: Delete “These are proposed studies.” The modal verbs already make that clear. Delete the following non-evidence sentence as well.

### Threats to validity

This is the correct home for caution. The goal is not to strip the section, but to stop it from repeating full method inventories.

- `06_threats_to_validity.tex:9`: Keep the prevalence and API-risk boundary. Drop the catalogue of unmeasured developer comprehension, trust, action, and utility unless the paper makes a user-impact claim.
- `06_threats_to_validity.tex:17`: Separate sampling-frame defects from one-run configuration selection, or compress each to one sentence.
- `06_threats_to_validity.tex:21`: Summarise the GitHub coverage limit instead of repeating every inclusion rule from Study Design.
- `06_threats_to_validity.tex:29`: Cite the split table and say that several class estimates rest on few projects. The exact project counts need not be repeated.
- `06_threats_to_validity.tex:31–33`: Merge the overlapping non-claims about the bootstrap, threshold analysis, and model comparison around one point: uncertainty is conditional on the observed partition and executions.
- `06_threats_to_validity.tex:41`: Refer to the reproducibility subsection and state the consequence in one sentence. Do not repeat the full missing-artefact list.

### Conclusion

`07_conclusion.tex:7` nearly restates the Introduction and Abstract boundary, then closes with four requirements for stronger claims. Replace it with the paper's central takeaway and one forward-looking sentence. For example:

> Occurrence-level validation reveals class differences hidden by the pooled score and turns recurring corpus flags into concrete targets for audit. Independent annotation and repeated runs should be the next validation step.

## Precision that should remain

Do not apply a blanket shortening pass. Keep these parts precise:

- `02_background_related_work.tex:29–48`: operational class definitions and exclusions
- `03_study_design.tex:118–124`: matching candidates, intersection over union, one-to-one assignment, and aggregate definitions
- `04_results.tex:31–33`: primary held-out counts and class differences
- one explanation of why the detector-informed revision is optimistic
- one complete account of the single-annotator, sparse-class, and run-to-run limitations in Threats to Validity
- required declarations and the AI-use disclosure

These passages define the construct or report evidence. The painful wording comes from repeating their boundaries elsewhere.

## Recommended edit order

1. Remove or consolidate the four recurring disclaimer clusters.
2. Delete the three repeated “Answer to RQ” blocks or use them to replace earlier summaries.
3. Rewrite Discussion around findings, retaining only two priority follow-up studies.
4. Move provider-specific preservation detail and disagreement case inventories to Online Resource 1.
5. Shorten RQ headings, paragraph-closing meta-comments, and the final Conclusion paragraph.
6. Run a final search for paragraphs ending in “unmeasured,” “unknown,” “unavailable,” “cannot,” or “do not.” Keep such endings only when the paragraph's purpose is explicitly to state a limitation.

The paper can stay exact without sounding afraid of its own results. State each boundary once, then let the findings carry the argument.

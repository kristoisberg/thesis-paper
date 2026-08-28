# ESE word restoration: Step 8 reconciliation

Date: 2026-08-28

Status: completed.

## Starting state

- Step 8 starting HEAD: `b1e667a4d702a6e1a6946b086268d3fc3c7df257`.
- Main-paper TeXCount after Step 7: 9,930.
- Net restoration after Step 7: 2,945 words over the 6,985-word baseline.
- PDF-extracted words after Step 7: 12,352.
- Main PDF pages after Step 7: 31.

## Review and reconciliation

Three independent read-only reviews examined the restored article from Introduction through Conclusion. The consistency review checked terminology, figures, citations, labels, RQ wording, and claim alignment. The logic review checked paragraph order, transitions, and the evidence-to-conclusion sequence. The writing review checked concision, repetition, signposting, causal language, novelty language, and common generated-prose patterns.

The reconciled manuscript:

- moves the Introduction's detection sentence after the persistence evidence, preserving the problem progression;
- removes the repeated Implicit Columns definition and compresses repeated representation wording in Background;
- changes `API-pattern coding` to `source-fragment coding`, tightens model and prompt criteria, and removes thesis-navigation language in Study Design;
- adds section-local citations for the configuration comparison while removing prose that merely restated disagreement-table cells in Results;
- clarifies the full-corpus and flagged-repository denominators in RQ2;
- removes two one-sentence Discussion bridges and a mechanical closing inventory while preserving the original single-run cost/runtime comparison and bounded follow-up studies.

The review did not add proposed Discussion subsections, because they would split the article's established three-part analytical chain. It also did not remove the compact RQ map at the end of Study Design, which closes the analysis-frame subsection rather than previewing the thesis structure. No Abstract or Conclusion text changed.

## Provenance and claim checks

All 19 restored paragraph units remain mapped to rows I01 through D02 in the Step 1 legacy-source ledger. Step 8 edited those units and their immediate transitions in place and introduced no new freestanding paragraph. Thus every restored paragraph block remains source-led, exceeding the plan's 85% traceability requirement without estimating unsupported word-level provenance.

The following checks passed:

- the Introduction and Results retain identical wording for all three RQs;
- title, abstract, direct answers, Discussion, Threats to Validity, and Conclusion retain the same evidence boundary;
- 460/76/63 sums to 523 references and 536 predictions, and the reported pooled metrics remain 0.858/0.880/0.869;
- the corpus totals remain 15,931 flags in 602 repositories, with 601 flagged repositories, 68.3% for the two leading classes, 71.7% for the leading Implicit Columns pair, and 46.8% for `like(`;
- no duplicate labels, unresolved references or citations, overfull boxes, prohibited `ground truth` or prevalence wording, model-reasoning claims, novelty claims, or common generated-prose markers were found.

## Counts and verification

Canonical TeXCount was run from `paper/main.tex` with `-inc -sum`.

| Section | Baseline | After Step 8 | Net change |
|---|---:|---:|---:|
| Introduction | 384 | 452 | +68 |
| Background and Related Work | 789 | 1,345 | +556 |
| Study Design | 2,287 | 3,623 | +1,336 |
| Results | 1,224 | 1,783 | +559 |
| Discussion | 777 | 1,044 | +267 |
| Threats to Validity | 926 | 926 | 0 |
| Conclusion | 163 | 163 | 0 |
| **Main paper** | **6,985** | **9,771** | **+2,786** |

Step 8 removed 159 words from the Step 7 manuscript. The final net addition is 64 words below the plan's 2,850-word lower tolerance. Adding replacement prose solely to meet that control would contradict the reconciliation and source-reuse rules. The practical target is nevertheless met: `pdftotext -layout` reports 12,393 words and `pdfinfo` reports 31 pages.

`make paper` completed successfully. The final main log contains no LaTeX errors, unresolved references or citations, or overfull boxes, and BibTeX reports no warnings. The remaining notices are the previously accepted underfull boxes. Full clean-build and visual-layout inspection remain assigned to Step 9.

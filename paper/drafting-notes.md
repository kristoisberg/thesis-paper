# Drafting Notes

Status: feedback-remediated journal-depth draft

## Created Draft Files

- `paper/main.tex`: first SVJour3 manuscript draft.
- `paper/figures/data_funnel_diagram.png`: draft Figure 1 asset copied from the thesis figures.
- `paper/supplementary.tex`: supplementary material scaffold.
- `paper/supplementary-figures/`: supplementary figure assets copied from the thesis figures.

## Remaining Pre-Submission Confirmations

- Kristo Isberg is currently assumed to be the corresponding author.
- Confirm the Author Contributions statement with both authors.
- Replace or remove the archival-identifier marker after deciding whether to create a DOI-backed snapshot.
- Compile and package the manuscript in an environment with a compatible LaTeX engine.

## Validation

- Static check found no remaining `this thesis` or `Chapter` phrasing in `paper/main.tex`.
- Citation keys used in the draft exist in `thesis/references.bib`.
- Abstract length remains within Springer's 150-250 word requirement and reports 0.88 as the primary detector estimate.
- Keyword count is 6, within Springer's 4-6 keyword requirement.
- Lightweight LaTeX environment check found matching `\begin{...}` and `\end{...}` counts.
- All `\ref{...}` keys used in `paper/main.tex` have matching labels.
- All `\ref{...}` keys used in `paper/supplementary.tex` have matching labels.
- All figures referenced from `paper/supplementary.tex` exist under `paper/supplementary-figures/`.
- Static check found no thesis-specific phrasing in `paper/supplementary.tex`.
- Author metadata is filled in both `paper/main.tex` and `paper/supplementary.tex`.
- Competing interests, funding, data availability, code/materials availability, ethics, consent, and AI-use declarations are present in `paper/main.tex`.
- Author Contributions and an optional archival identifier remain explicit author-confirmation items.
- The draft is approximately 11,456 whitespace-delimited LaTeX words, excluding the bibliography and supplementary material.
- Each RQ appears as a result subsection heading and ends with a direct answer.
- Study Design includes Operational Definitions, Annotation and Adjudication, Model and Prompt Selection, and Evaluation Protocol.
- The detector table reports TP, FP, FN, test support, precision, recall, and F1 for every antipattern.
- `paper/references.bib` is self-contained and includes the added 2026 EMSE novelty comparators and the source thesis.
- The supplementary material is approximately 1,409 words, excluding figure content.
- Local PDF compilation was not possible because `pdflatex` is not installed in this environment.
- The draft currently references `../template/svjour3.cls`, `../template/spbasic.bst`, and `../thesis/references.bib`; the final submission package should be flattened later.

## Next Drafting Tasks

- Compile in an environment with `pdflatex` or another compatible LaTeX engine.
- Obtain both authors' approval for the contribution statement.
- Create a DOI-backed archive if desired and resolve the archival-identifier marker.
- Re-run the submission-readiness gate after all confirmation markers are removed.

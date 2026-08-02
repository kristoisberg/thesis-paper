# Drafting Notes

Status: adversarial-feedback revisions implemented; not submission-ready

## Created Draft Files

- `paper/main.tex`: first SVJour3 manuscript draft.
- `paper/figures/data_funnel_diagram.png`: draft Figure 1 asset copied from the thesis figures.
- `paper/supplementary.tex`: supplementary material scaffold.
- `paper/supplementary-figures/`: supplementary figure assets copied from the thesis figures.
- `paper/cover-letter.md`: journal-fit and prior-dissemination cover-letter draft.

## Remaining Pre-Submission Confirmations

- Confirm the corresponding author; Kristo Isberg is only a drafting assumption.
- Confirm the Author Contributions statement with both authors.
- Deposit and cite a DOI-backed immutable artifact snapshot.
- Record exact provider model identifiers, prompt/artifact version, repository commits, and collection snapshot.
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
- Author names and affiliations are filled in both LaTeX files; corresponding-author approval remains blocked.
- Competing interests, funding, data availability, code/materials availability, ethics, consent, and AI-use declarations are present in `paper/main.tex`.
- Author Contributions, corresponding author, reproducibility identifiers, and archival DOI remain explicit blockers.
- The draft remains approximately 11,500 whitespace-delimited LaTeX words, excluding the bibliography and supplementary material.
- Each RQ appears as a result subsection heading and ends with a direct answer.
- Study Design includes Operational Definitions, Annotation and Adjudication, Model and Prompt Selection, and Evaluation Protocol.
- The detector table reports TP, FP, FN, test support, precision, recall, and F1 for every antipattern.
- `paper/references.bib` is self-contained and includes the added 2026 EMSE novelty comparators and the source thesis.
- The supplement is cited as Online Resource 1 and now contains split and operational configuration details moved from the main manuscript.
- Both `main.tex` and `supplementary.tex` compile successfully with the exact TeX Live 2026 Docker image used by CI.
- The draft currently references `../template/svjour3.cls`, `../template/spbasic.bst`, and `../thesis/references.bib`; the final submission package should be flattened later.

## Next Drafting Tasks

- Run `make` from the repository root to compile both PDFs using the same
  Dockerized TeX Live environment as CI. Use `make main`,
  `make supplementary`, or `make clean` for individual builds and cleanup.
- Obtain both authors' approval for the contribution statement.
- Create a DOI-backed archive if desired and resolve the archival-identifier marker.
- Re-run the submission-readiness gate after all confirmation markers are removed.

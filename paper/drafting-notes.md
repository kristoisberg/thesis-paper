# Drafting Notes

Status: declarations completed

## Created Draft Files

- `paper/main.tex`: first SVJour3 manuscript draft.
- `paper/figures/data_funnel_diagram.png`: draft Figure 1 asset copied from the thesis figures.
- `paper/supplementary.tex`: supplementary material scaffold.
- `paper/supplementary-figures/`: supplementary figure assets copied from the thesis figures.

## Remaining Pre-Submission Confirmations

- Kristo Isberg is currently assumed to be the corresponding author.
- Add a DOI-backed archival copy to the data availability statement if one is created before submission.
- Compile and package the manuscript in an environment with a compatible LaTeX engine.

## Validation

- Static check found no remaining `this thesis` or `Chapter` phrasing in `paper/main.tex`.
- Citation keys used in the draft exist in `thesis/references.bib`.
- Abstract length is 207 words, within Springer's 150-250 word requirement.
- Keyword count is 6, within Springer's 4-6 keyword requirement.
- Lightweight LaTeX environment check found matching `\begin{...}` and `\end{...}` counts.
- All `\ref{...}` keys used in `paper/main.tex` have matching labels.
- All `\ref{...}` keys used in `paper/supplementary.tex` have matching labels.
- All figures referenced from `paper/supplementary.tex` exist under `paper/supplementary-figures/`.
- Static check found no thesis-specific phrasing in `paper/supplementary.tex`.
- Author metadata is filled in both `paper/main.tex` and `paper/supplementary.tex`.
- Competing interests, funding, data availability, and AI-use declarations are filled in `paper/main.tex`.
- The draft is approximately 4,753 words.
- The supplementary material is approximately 1,409 words, excluding figure content.
- Local PDF compilation was not possible because `pdflatex` is not installed in this environment.
- The draft currently references `../template/svjour3.cls`, `../template/spbasic.bst`, and `../thesis/references.bib`; the final submission package should be flattened later.

## Next Drafting Tasks

- Compile in an environment with `pdflatex` or another compatible LaTeX engine.
- Create a DOI-backed archive for artifacts if desired before submission.

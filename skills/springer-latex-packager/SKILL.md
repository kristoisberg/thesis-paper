---
name: springer-latex-packager
description: Prepare or plan the Springer SVJour3 LaTeX manuscript package for the EMSE paper. Use for mapping manuscript structure to template/svjour3.cls, bibliography style, figure/table assets, supplementary files, declarations, cover letter, and final flat upload packaging constraints.
---

# Springer LaTeX Packager

Prepare `paper/` for a Springer SVJour3 manuscript.

## Source Template

Use:

- `template/svjour3.cls`
- `template/spbasic.bst`
- `template/template.tex`

Default document class:

```tex
\documentclass[smallextended]{svjour3}
```

Default bibliography style:

```tex
\bibliographystyle{spbasic}
```

## Planned Paper Outputs

Use these names unless the repo establishes another convention:

- `paper/main.tex`
- `paper/references.bib`
- `paper/cover-letter.md`
- `paper/statements-and-declarations.tex`
- `paper/supplementary.tex`
- `paper/figures/` during drafting
- `paper/submission-flat/` for final flattened upload

## Packaging Rules

During drafting, subfolders are allowed for maintainability. Before submission, create a flat upload package if required by Springer's LaTeX upload guidance.

Check:

- all figures are cited in order;
- tables use Springer-compatible captions;
- abstract is 150 to 250 words;
- keywords count is 4 to 6;
- declarations are present;
- declarations include Author Contributions, Funding, Competing Interests, Data Availability, Code and Materials Availability, Ethics Approval, and Consent to Participate;
- thesis-derived-work disclosure is visible in the manuscript;
- prior thesis dissemination is disclosed in a declaration and cover letter rather than used as scientific motivation;
- the corresponding author is explicitly marked and approved;
- model identifiers, prompt version, collection snapshot, and repository commits are recorded where available;
- supplementary files are cited as numbered Online Resources with concise captions;
- the data and code statements cite an immutable archived version and persistent identifier before submission readiness;
- source files compile;
- no thesis-specific package assumptions leak into the article.

Keep the paper bibliography self-contained. Do not modify the completed thesis bibliography to add article-only related work.

Do not replace unknown author roles, correspondence details, commits, or archival identifiers with guesses. Preserve them as hard blockers and fail submission readiness until the authors resolve them.

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
- source files compile;
- no thesis-specific package assumptions leak into the article.


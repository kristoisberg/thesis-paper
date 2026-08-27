# ESE citation-style audit

## Scope

Reviewed all citation commands in `paper/main.tex`, `paper/chapters`, and
`paper/appendices`, plus cited entries in `paper/references.bib`, against the
current Empirical Software Engineering author guidelines and the local
`svjour3`/`spbasic` configuration.

## Findings and resolutions

- Replaced comma-separated runs of individual parenthetical citations with
  single ESE-style clusters separated by semicolons.
- Preserved source-specific page locators with `\citetext` and `\citealp`.
- Made parenthetical and narrative intent explicit through `\citep` and
  `\citet`, and removed non-wrapping `\mbox` citation wrappers.
- Removed duplicated authors and years in narrative prose and the comparison
  table.
- Moved citations outside bold list labels and removed nested citation
  parentheses.
- Converted unsupported `@online` entries to `@misc`, added personal or
  organizational authors, and expressed access dates in supported notes.
- Corrected plural page-range locators, the Kimi Team corporate author, and
  missing thesis institutions.

## Verification

- `make paper`: passed; `paper/main.pdf` generated successfully.
- BibTeX warnings: 0 (previously 100).
- Undefined citations or references: 0.
- PDF text audit: no malformed abbreviated web labels and no comma-separated
  `), (` citation clusters remain.

## Source

- ESE submission guidelines:
  https://link.springer.com/journal/10664/submission-guidelines

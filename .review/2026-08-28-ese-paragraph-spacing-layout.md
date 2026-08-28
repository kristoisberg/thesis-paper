# ESE paragraph-spacing layout audit

Date: 2026-08-28

Status: completed; no manuscript override retained.

## Diagnosis

The source defines ordinary paragraphs with indentation and no fixed vertical skip. The Springer `svjour3` class sets `\parskip` to `0pt plus 1pt` and explicitly ends with `\flushbottom`. On pages with a float or another vertical constraint, TeX can stretch that glue to align the bottom of the text block with other pages. Page 10 shows this effect below Figure 2. The apparent empty lines are generated during page layout; the section source contains no `\vspace`, manual line breaks, or paragraph-spacing package.

## Decision

Retained the class default. A proposed global `\raggedbottom` override was removed because it exchanges the journal template's aligned page bottoms for uneven ones. No paragraph source, float spacing, or class file was changed. If the publisher flags one exceptional page, the class already provides `\thisbottomragged` as a local escape.

## Verification

- Page 10's larger paragraph gaps are layout-generated and consistent within that page.
- A separate `svjour3` Empirical Software Engineering manuscript exhibits the same variable paragraph-start spacing, including gaps of approximately 18--29 pt against an unstretched baseline of approximately 12 pt.
- The main paper remains 32 A4 pages. Float order and page placement are unchanged.
- `make clean && make paper` passes with no LaTeX errors, unresolved citations or references, overfull boxes, float-size warnings, or rerun warnings.
- The class-default build has 21 accepted underfull notices in the main log; the supplement retains one.
- `git diff --check` passes.

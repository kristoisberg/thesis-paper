# ESE word restoration: Step 3 report

Date: 2026-08-28

Status: completed.

## Starting state

- Manuscript baseline: `098d195c58c72705ff5263af466f92561afa032f`.
- Step 3 starting HEAD: `b260fa87f42f2bd64764600985ea34d414b1b570`.
- Background and Related Work TeXCount: 789.
- Main-paper TeXCount after Step 2: 7,053.
- PDF-extracted words after Step 2: 9,420.
- Manuscript files already modified: `paper/sections/01_introduction.tex`.

## Source ledger

The row deltas below are standalone TeXCount differences between each restored block and the block it replaced. They sum to the canonical section delta.

| ID | Legacy source | Restored job | Net words |
|---|---|---|---:|
| B01 | `paper/chapters/02_background.tex:5,7` | Distinguish an antipattern from a code smell before introducing the evaluated classes. | +78 |
| B02 | `paper/chapters/02_background.tex:11-13` | Restore the Implicit Columns ordinal-position and unused-column mechanisms. | +82 |
| B03 | `paper/chapters/02_background.tex:85` | Restore the DSL, code-generation, generated-schema, and JDBC sequence needed to explain the analysed source. | +92 |
| B04 | `paper/chapters/02_background.tex:104-112` | Restore the progression from metric thresholds to AST rules, learned detection, and LLM source analysis. | +228 |
| B05 | `paper/chapters/02_background.tex:135-145` | Compare DbDeo, SQLInspect, SQLCheck, and LLM work by representation and output unit. | +119 |
|  |  | **Total** | **+599** |

The paragraph order and most sentence structures follow the named thesis passages. Short synthesis sentences connect those passages to the article's existing occurrence-localisation argument and to the representation/output-unit comparison already preserved in Online Resource 1.

## Exclusions and adaptations

- The full SQL-antipattern taxonomy, prompt tutorial, product inventories, and extended smell examples remain excluded.
- The existing 27% runtime and 29% energy result remains stated once; the unevaluated `INSERT` form was not restored.
- The jOOQ passage omits adoption, ORM-superiority, GitHub-star, customer, and IDE-support claims.
- The detector comparison omits the claim that only two tools exist, claims of incapability, database-catalogue inventories, and numerical cross-study rankings.
- DbDeo's extraction and parsing errors remain explicitly attributed to its authors.
- The final localisation-gap paragraph is unchanged.

## Counts and budget

Canonical TeXCount was run from `paper/main.tex` with `-inc -sum`.

| Measure | Before Step 3 | After Step 3 | Change |
|---|---:|---:|---:|
| Background and Related Work TeXCount | 789 | 1,388 | +599 |
| Main-paper TeXCount | 7,053 | 7,652 | +599 |
| PDF-extracted words, including references | 9,420 | 10,184 | +764 |
| Main PDF pages | 25 | 26 | +1 |

The TeXCount change is within the planned 594--726 range. The PDF-extracted increase is larger because the restored citations add bibliography entries to the compiled paper. The 61-word difference from the provisional 660-word allocation was not reassigned: the current 2,939-word execution budget remains inside the overall 2,850--3,150 target range.

## Verification

- `make paper` completed successfully.
- The main log contains no LaTeX errors, undefined citations or references, or overfull boxes.
- BibTeX reports no warnings.
- The main PDF is 26 pages.
- Every named approach has a citation in the Background section.
- The final paragraph still states the occurrence-localisation gap and remains the subsection synthesis.
- No new float, label, research question, contribution, result, or corpus claim was introduced.

# ESE word restoration: Step 2 report

Date: 2026-08-28

Status: completed.

## Starting state

- Manuscript baseline: `098d195c58c72705ff5263af466f92561afa032f`.
- Planning HEAD: `e6a3ac70a9430361281b7797c55acb5f5fff5c93`.
- Introduction TeXCount: 384.
- Manuscript files modified by earlier restoration steps: none. Step 1 had changed only review metadata.

## Change

One paragraph was restored after the Introduction's opening paragraph in `paper/sections/01_introduction.tex`. It adds prior evidence that SQL antipattern occurrences can persist and may receive comparatively low remediation priority. The article's existing next paragraph then makes the move into jOOQ.

The paragraph follows the claim order and viable sentence structure of:

- `paper/chapters/01_introduction.tex:6` for persistence and the two proposed explanations;
- `paper/chapters/02_background.tex:27` for the comparison with traditional code smells and lifetime persistence.

The old prevalence figures, tooling-causality claim, developer-education framing, five-RQ structure, novelty claims, and broad thesis framing remain excluded. One short qualification distinguishes the cited study's proposed explanations from causal findings. A newly drafted representation bridge was removed because it repeated the opening paragraph and was not needed to connect the legacy passage to the existing jOOQ paragraph.

## Counts and budget

Canonical TeXCount was run from `paper/main.tex` with `-inc -sum`.

| Measure | Before Step 2 | After Step 2 | Change |
|---|---:|---:|---:|
| Introduction TeXCount | 384 | 452 | +68 |
| Main-paper TeXCount | 6,985 | 7,053 | +68 |
| PDF-extracted words, including references | 9,332 | 9,420 | +88 |
| Main PDF pages | 25 | 25 | 0 |

The source supported 68 accurate words, below the provisional 180-word allocation. Adding another 112 words would have duplicated the opening paragraph or replaced the source with newly generated connective prose. The 112-word remainder was therefore moved to ledger row S01 in Study Design, raising that source-led budget from 180 to 292 words. The overall restoration budget remains 3,000 words.

## Verification

- `make paper` completed successfully.
- The main log contains no LaTeX errors, undefined citations or references, overfull boxes, or BibTeX warnings.
- The main PDF remains 25 pages.
- The three research questions and contribution list are unchanged.
- The Introduction still progresses from SQL-antipattern motivation, through the jOOQ representation problem, to the occurrence-localisation evidence gap.
- The restored paragraph does not claim that the cited explanations are causal findings or that detection changes remediation priorities.

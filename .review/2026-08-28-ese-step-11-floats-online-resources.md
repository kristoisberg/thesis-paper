# ESE Step 11: main-paper floats and online resources

Date: 2026-08-28

Status: completed.

## Applied changes

- Reduced the main paper from 11 to seven floats: the operational definitions, repository-selection pipeline, configuration selection, held-out occurrence agreement, error mechanisms, corpus flag distribution, and source-fragment manifestations.
- Moved the paired SQL/jOOQ example, detector-representation comparison, split-support matrix, and intersection-over-union diagnostic to `paper/supplementary.tex`.
- Added a buildable, numbered `Online Resource 1` that indexes the frozen search materials, codebook and decision trees, prompts, detailed configuration outputs, diagnostics, matrices and heatmaps, detector implementation, and command-line material.
- Replaced vague references to online resources with explicit citations to Online Resource 1 and aligned data availability with the pinned study commit.
- Removed unused float aliases and main-document packages left behind by the moved material.
- Updated the build so `make paper` compiles both the article and the supplement.

## Completion check

- Every retained float follows its first textual introduction, is interpreted in adjacent prose, and supports one reported claim.
- The article contains no compiled appendix and no thesis-scale prompt, codebook, diagnostic, matrix, heatmap, command-line, or implementation inventory.
- The article is 24 A4 pages with seven floats; Online Resource 1 is three A4 pages.
- Both PDFs compile without undefined citations, references, duplicate labels, float-size warnings, or overfull boxes in retained floats or supplementary material.
- The only remaining overfull box is in the author-contributions declaration, outside Step 11 and scheduled for the declarations pass in Step 12.

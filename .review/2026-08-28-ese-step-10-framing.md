# ESE Step 10: framing and connective prose

Date: 2026-08-28

Status: completed.

## Applied changes

- Rewrote the Introduction around the practical problem, jOOQ representation gap, bounded central claim, three research questions, and three empirical contributions.
- Removed tool-building thesis framing, unsupported causal motivation, the unsupported first-of-its-kind claim, and methodology chronology from the Introduction.
- Narrowed RQ3 to the measured source-fragment patterns and aligned its direct answer with that unit.
- Added only the short transitions needed between the occurrence-level, prior-detector, and source-fragment arguments.
- Rewrote the Conclusion directly from the three RQ answers and their claim limits.
- Rewrote the Abstract last using the final counts and agreement measures; repository links remain in the data-availability declarations.
- Retained the reference to the master's thesis only in the prior-dissemination declaration.

## Completion check

- The Abstract, Introduction, direct RQ answers, Discussion, and Conclusion state the same evidence chain: project-disjoint agreement for class-labelled spans bounds interpretation of the corpus flags.
- All framing uses the final values: micro precision 0.858, recall 0.880, F1-score 0.869, per-class F1 0.481--0.974, 15,931 flags, and source-fragment shares of 71.7% and 46.8%.
- Corpus findings are described as detector outputs; prevalence and API-associated risk remain unmeasured.
- The abstract contains 150--250 words and six keywords.
- `make paper` succeeds with no undefined citations or references and no overfull boxes in the rewritten Abstract, Introduction, Discussion transitions, or Conclusion.

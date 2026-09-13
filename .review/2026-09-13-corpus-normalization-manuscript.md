# Corpus-normalization manuscript review

Date: 2026-09-13

Scope: integration of corpus-normalization Phases 1 through 4 into the article manuscript and Online Resource 1.

## Overview

Phases 1 through 4 support a stronger account of detector output without changing the paper into a prevalence study. The manuscript should replace its raw-count-only RQ2 account with role-specific file normalization, repository-size decomposition, and exact-content sensitivity. Phase 5 remains out of scope.

## Critical issues

1. `paper/sections/06_threats_to_validity.tex` says the corpus analysis has no repository-size correction. Phase 3 now provides file-normalized and repository-equal results.
2. `paper/supplementary.tex` says the corpus source revisions are unavailable. The source snapshot survives without Git history, and Phase 1 records repository-relative paths and SHA-256 hashes.
3. RQ2, its methods, and its results currently omit detector-output density, flagged-file breadth, within-file repetition, and the decomposition of top-decile concentration.
4. The article-analysis links point to commit `96dc91b`, which predates the normalization script and outputs. Commit `bb3bf6056cc7bbda29bb0fb5f0b720e7f9d06028` contains Phases 1 through 4.

## Important issues

1. Define generated-schema and application/query source roles, their 7,226- and 10,762-file frames, and the separate Fear of the Unknown rows.
2. Distinguish pooled density from repository-equal density. Eligible zero-flag repositories contribute zero to repository summaries.
3. Report that the 61 highest-count repositories contain 59.1% of flags, 48.1--49.6% of relevant files across cutoff ties, and 1.47--1.56 times the remaining density.
4. Report the breadth--repetition contrast: ID Required flags 49.7% of generated-schema files with 1.00 flag per flagged file, while Implicit Columns flags 24.2% of application/query files with 2.80 flags per flagged file.
5. State that exact-content weighting preserves both headline conclusions. Keep detailed Phase 2--4 outputs in Online Resource 1.

## Minor issues

1. Use "relevant file occurrence" or "distinct repository-relative file path" for the 17,988-file frame and reserve "unique file content" for the 17,367 SHA-256 values.
2. State that exact-content sensitivity covers byte-identical files, not modified clones.
3. Replace the stale statement that later corrections improved the corpus run. The reconstruction corrected file accounting without changing the 15,931 frozen output rows.

## Recommendations

1. Replace the existing RQ2 table with one compact table containing flags, repository coverage, flagged-file breadth, within-file repetition, and pooled/repository-equal density.
2. Add short interpretation paragraphs for repository size and exact-content sensitivity.
3. Update the abstract, contribution statement, discussion, conclusion, threats, and reproducibility record to match the normalized results.
4. Preserve the detector-output boundary. Role-eligible files are broader than class-specific API opportunities, so the results remain neither prevalence nor API-risk estimates.

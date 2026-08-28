# ESE Step 13: submission readiness

Date: 2026-08-28

Status: partially completed. All repository-local manuscript checks pass. The package still requires a DOI-backed deposit and author-confirmed declarations. The exact validation-run outputs underlying the originally reported configuration table are unavailable and are now disclosed as a preservation limitation.

## Applied changes

- Replaced forced placement for the repository funnel and configuration table with normal top/page placement, removing the large gaps previously visible in the main PDF.
- Added references, interpretation, labels, and self-contained captions for every supplementary table and removed orphan supplementary headings.
- Updated the article-analysis snapshot from `07a81e5` to `96dc91b`, which contains both reconstruction scripts and `analysis/requirements.txt`.
- Disclosed that the surviving validation notebooks do not reproduce the reported validation file count, costs, or runtimes; described the table as originally reported rather than exactly reconstructed.
- Qualified prompt identity, detector revision, retry, and corpus-file coverage claims to match the preserved evidence.
- Corrected the RQ3 category labels and catch-all description to match the frozen substring rules in `scripts/21-find-frequent-offenders.ipynb`.
- Corrected the combined Implicit Columns percentage from 12.9% to 13.0%, notebook counts and Python metadata, and per-file retry wording.
- Removed residual causal wording, internal restructuring comments, undefined abstract terminology, and inconsistent domain-specific-language spelling.
- Completed cited bibliography metadata, protected product-name capitalization, and added standalone citations to Online Resource 1.
- Extended `make clean` to remove the obsolete `paper/supplementary.pdf` build products, leaving `paper/ESM_1.pdf` as the single supplement submission file.

## Verification

- `make clean && make paper` built `paper/main.pdf` at 25 A4 pages during Step 13 and `paper/ESM_1.pdf` at 7 A4 pages. Word-restoration Step 9 later superseded the main-paper count at 31 pages, and the subsequent four-float restoration supersedes it again at 32 pages; the supplement remains 7 pages.
- Both final logs contain no overfull boxes, undefined references, undefined citations, or LaTeX errors. Both BibTeX logs report `warning$ -- 0`. Remaining underfull boxes are harmless table-cell and URL wrapping.
- PDF inspection found no clipped content, orphan headings, isolated floats, or margin violations. PDF title, author, subject, and keyword metadata are populated in both files.
- All three research questions retain matching wording between the Introduction and Results, have direct answers, and use the same final values in the Abstract and Conclusion.
- `analysis/localisation_robustness.py` reconstructs 536 predictions and 523 references, the 460/76/63 primary totals, micro precision/recall/F1 of 0.858/0.880/0.869, the IoU grid, and the 10,000-replicate bootstrap ranges.
- `analysis/corpus_concentration.py --verify-frozen` verifies the frozen CSV and reproduces 15,931 flags, 601 flagged repositories, every class total, and the 59.1% overall top-decile share.
- All 46 cited bibliography keys resolve. The compiled PDFs contain no unresolved markers. The two cited arXiv model cards have no identified canonical published replacements.
- Searches found no residual compiled thesis navigation, unsupported novelty or superiority claims, conspicuous AI-writing patterns, or material causal overclaims.

## Remaining submission blockers

1. Deposit the replication package in a DOI-issuing repository, cite the dataset, and replace the supplement's DOI warning.
2. Replace the competing-interests, funding, ethics-approval, and consent placeholders with author-confirmed statements.
3. Confirm author order, affiliations, corresponding email, contribution roles, and both authors' approval of the submitted manuscript.
4. The exact outputs behind the originally reported validation configuration table cannot be recovered from the surviving notebooks. The manuscript and supplement now state this limitation; recovering those outputs would require an external copy of the original run artefacts.

The first three items are the same external and author-confirmation blockers recorded in Step 12. Until they are resolved, the ESE checklist and Step 13 completion check remain partial.

Guideline basis: Empirical Software Engineering submission guidelines, checked 28 August 2026: https://link.springer.com/journal/10664/submission-guidelines

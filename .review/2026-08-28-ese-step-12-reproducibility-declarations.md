# Step 12: Reproducibility and declarations

## Status

Step 12 is partially complete. The repository records every reproducibility field supported by the surviving evidence. The author has confirmed that competing interests, funding, ethics approval, and consent to participate are not applicable. Completion still requires a DOI deposit and confirmation of the remaining author metadata and final approval.

## Applied

- Added PDF title, author, subject, and keyword metadata to the manuscript and Online Resource 1.
- Added the exact article title, journal, affiliations, and corresponding-author contact to Online Resource 1.
- Changed the supplementary build output to `paper/ESM_1.pdf` and added its manuscript caption.
- Pinned the study artefacts at `d9b35e3`, released detector at `cf82fe5`, and article reconstruction scripts with their dependencies at `96dc91b` (corrected during Step 13).
- Recorded preserved prediction locations, model slugs, execution dates, parameters, validation retry totals, held-out and corpus request totals, prompts, dependencies, missing raw metadata, and analysis commands.
- Added `analysis/requirements.txt` for the current reconstruction scripts.
- Corrected the validation-method account to match the archived notebooks: GPT-5.2 requests include temperature `0.0`; gpt-oss-120B omits the parameter and preserved responses report `1.0`; only the GLM-5 notebooks record a fixed backend and disabled fallbacks.
- Converted declaration headings from run-in paragraphs to unnumbered subsections, keeping the manuscript within three decimal heading levels and removing the declaration overflow.
- Preserved the existing contribution roles without adding unsupported roles.
- Replaced the competing-interests, funding, ethics-approval, and consent placeholders with the author-confirmed statement `Not applicable.`

## Verified

- Kristo Isberg is marked as corresponding author and has an institutional email.
- Both authors have institution, city, and country affiliations.
- The abstract is within the required 150--250 words.
- The manuscript has six keywords, meeting the required 4--6.
- Numbered body headings stop at `subsubsection`, the third decimal level.
- The TalTech Digital Collection identifies Kristo Isberg as author, Erki Eessaar as supervisor, Tallinn University of Technology and the School of Information Technologies as the institution and faculty, and 25 May 2026 as the thesis defence date.

## Remaining external and author-confirmation blockers

1. Deposit the final replication package in a repository that issues a DOI. Include the frozen study artefacts, both article reconstruction scripts, dependency file, and this reproducibility record. Add the DOI to the data-availability statement and cite the dataset in `paper/references.bib`.
2. Confirm author order, current affiliations, corresponding email, contribution roles, and both authors' approval of the submitted manuscript.

The original source-repository revisions, detector run revision, raw API responses, request identifiers, full request metadata, per-request retry histories, complete provider routing metadata, negative-file outputs, and the full no-flag corpus frame cannot be reconstructed. The manuscript and supplement state these limits.

## Guideline source

Checked against the Empirical Software Engineering submission guidelines on 28 August 2026: https://link.springer.com/journal/10664/submission-guidelines

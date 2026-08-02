---
name: emse-journal-fit-auditor
description: Audit a manuscript or conversion plan against Springer's Empirical Software Engineering aims, scope, and submission guidelines. Use for EMSE fit, Springer formatting constraints, title page requirements, abstract and keyword checks, declarations, AI-use disclosure, citation style, and desk-reject risk.
---

# EMSE Journal Fit Auditor

Use this skill to enforce journal fit and Springer submission constraints for Empirical Software Engineering.

## Primary Sources

Verify current requirements from official Springer pages when the user asks for submission-ready work:

- `https://link.springer.com/journal/10664/aims-and-scope`
- `https://link.springer.com/journal/10664/submission-guidelines`

## Fit Criteria

The paper must read as applied software engineering research with a strong empirical component. Prefer claims that are:

- grounded in collected and analysed software engineering data;
- relevant to software development practice;
- replicable or expandable;
- explicit about methods, datasets, threats, and limitations.

For this repository, the strongest EMSE fit is the empirical study over jOOQ projects, supported by the LLM localisation method and detector validation.

## Submission Criteria

Check for:

- abstract length of 150 to 250 words;
- 4 to 6 keywords;
- concise and informative title;
- author names, affiliations, corresponding author email, and ORCID values if available;
- name-year citation style and alphabetized references;
- editable source files available for submission;
- declarations under `Statements and Declarations`;
- competing interests statement;
- data availability and artifact availability statements;
- AI-use documentation in Methods or an equivalent section when generative AI contributed beyond copy editing;
- all figures and tables cited in order;
- no undefined abbreviations in the abstract.

## Desk-Reject Checks

Flag immediately:

- framing as a shortened master's thesis;
- broad textbook background;
- excessive tool implementation detail;
- unsupported novelty claims;
- missing empirical method detail;
- missing threats to validity;
- missing declarations;
- inconsistent Springer formatting.


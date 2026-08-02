# Feedback Remediation Matrix

Status: structural and claim-bounding revisions implemented; submission and empirical-extension blockers remain

| Feedback | Status | Implemented response | Acceptance check |
|---|---|---|---|
| Retain the empirical structure | Implemented | Preserve Introduction, Related Work, Study Design, Results, Discussion, Threats, and Conclusion | Top-level sequence remains recognisable |
| Combine result sections | Implemented | Use one `Results` section with RQ1--RQ4 subsections | Exactly one top-level Results section exists |
| Reduce operational method detail | Implemented | Move split formula, provider settings, retry/cost/runtime details to Online Resource 1 | Main text retains only RQ-relevant rationale |
| Increase uncertainty analysis | Implemented | Report class-specific support and confidence tiers; identify low-confidence population outputs | Weak classes are not interpreted like strong classes |
| Validate population outputs | Bounded, not performed | State that no separate manual population audit was available; do not accuracy-correct outputs | Manuscript never implies population validation |
| Control co-occurrence for project size | Bounded, not performed | Recast RQ3 as exploratory unadjusted co-detection and remove weak-class construct claims | No size-independent or causal claim remains |
| Reframe scientific contribution | Implemented | Centre occurrence-localised validation plus bounded mining; retitle accordingly | No contribution rests on editorial reorganisation |
| Demonstrate maintenance relevance | Implemented | Connect localised outputs to warning sites, hybrid rules, documentation, and maintenance inspection | Introduction states concrete stakeholder consequences |
| Add comparator table | Implemented | Compare SQLInspect, API/AST rules, LLM smell studies, and this study by representation, labels, localisation, validation, and repository use | Cited table exists in Related Work |
| Move thesis provenance | Implemented | Remove it from the Introduction; add prior-dissemination declaration and cover-letter disclosure | Introduction contains no thesis-conversion paragraph |
| Use a stable supplementary citation | Partially implemented | Cite the concrete file as Online Resource 1 with a contents description | DOI remains a hard blocker |
| Record exact reproducibility identifiers | Blocked | Add a visible metadata confirmation gate for provider IDs, prompt/artifact version, commits, and collection snapshot | Acceptance fails until identifiers are supplied |
| Identify corresponding author | Blocked | Add an explicit confirmation gate rather than infer author approval | Acceptance fails until approved |
| Complete author contributions | Blocked | Retain the author-confirmation marker | Acceptance fails until both authors approve wording |
| Deposit immutable artifact | Blocked | Retain the archival-identifier marker | Acceptance fails until a persistent identifier is supplied |
| Preserve primary detector result | Implemented | Keep 0.88 primary and 0.93 as optimistic sensitivity analysis | Abstract contains 0.88, not 0.93 |

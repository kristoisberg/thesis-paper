# Reviewer Risk Checklist

Status: feedback-remediated; substantial empirical and submission risks remain

## Construct Validity

- One annotator produced both passes; Kappa 0.834 measures temporal consistency, not independent agreement.
- Corrected ground truth is optimistic because detector disagreements triggered review.
- No independent manual audit tested whether held-out class error transfers to the 602-project outputs.
- Keyless Entry and Fear of the Unknown population counts are low-confidence flags, not census-quality estimates.
- IoU 0.5 and the static jOOQ statement proxy remain study-specific constructs.

## Internal and Reliability Risks

- Model/prompt comparisons and the final test call set are single-run observations.
- Zero temperature, structured output, project-disjoint splits, fixed seeds, and disabled fallbacks improve control but do not estimate run-to-run variance.
- OpenRouter routing and provider/model changes prevent exact endpoint reproduction.
- Exact provider identifiers, prompt/artifact version, repository commits, and collection snapshot still require confirmation.

## External and Conclusion Validity

- Findings apply to the analysed GitHub Java/jOOQ corpus with committed generated classes, not all jOOQ or enterprise systems.
- Corpus counts inherit class-dependent error and were not accuracy-adjusted.
- RQ3 reports exploratory co-detection only: project size was not controlled, and high marginal prevalence inflates overlap.
- API patterns are associations, not causes; static statement proxies are not runtime SQL counts.
- Population validation, repeated runs, independent annotation, and size-controlled analysis remain future empirical work.

## Desk-Reject Gate

- The Introduction now leads with occurrence-localised validation and maintenance consequences, not thesis conversion.
- Related Work includes a cited comparison table; Results is a single section with four RQ subsections.
- Thesis reuse is disclosed in declarations and the cover letter.
- Online Resource 1 is cited specifically rather than promised vaguely.
- Submission readiness must fail until corresponding author, author contributions, reproducibility identifiers, and immutable archive DOI are confirmed.

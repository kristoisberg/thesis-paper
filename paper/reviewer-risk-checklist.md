# Reviewer Risk Checklist

Status: initial risk pass

## Construct Validity

- Single annotator: Kappa 0.834 shows consistency over time, not agreement between independent experts.
- Corrected ground truth: corrected scores are optimistic because corrections were discovered through the tool's outputs.
- Localisation: IoU >= 0.5 must be justified as a practical line-span overlap threshold.
- Proxy density: "occurrences per 100 jOOQ statements" uses static jOOQ API references, not executed SQL statements.

## Internal Validity

- Prompting-strategy results are descriptive because statistical significance was not tested.
- Few-shot examples may overfit edge cases from the training set.
- LLM output nondeterminism remains possible even with zero temperature and structured outputs.
- OpenRouter/backend routing may affect reproducibility for open-weight models.

## External Validity

- Results apply directly to GitHub open-source Java projects using jOOQ with generated classes committed to source.
- Results may not generalise to closed-source enterprise systems, non-Java systems, other query builders, or projects that generate jOOQ classes only at build time.
- GitHub Code Search limits and Maven/Gradle-oriented search terms may miss relevant projects.

## Conclusion Validity

- Do not claim complex prompting is worse in general; only say it did not consistently improve this evaluation and increased cost/runtime.
- Do not claim API methods cause antipatterns; claim they are frequently associated with detected occurrences.
- Do not compare density values directly with plain SQL studies without explaining granularity and statement-count differences.

## Desk-Reject Avoidance

- Lead with empirical contribution and scale.
- Remove thesis framing and tutorial background.
- Document AI use in methods/declarations.
- Include artifact availability.
- Keep limitations direct and visible.


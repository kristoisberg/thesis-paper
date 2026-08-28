# ESE Step 9: discussion and validity review

Date: 2026-08-28

## Synthesis

The current Discussion repeats results, ranks incomparable evaluation tasks, and explains class differences with unsupported causes. Threats to Validity contains most required limitations, but presents them as a flat thesis narrative rather than as limits on specific claims.

## Critical findings

1. Remove the claimed relationship between class frequency and agreement. The rare 31 Flavors and Rounding Errors classes have high observed F1, so the reported results do not support that pattern.
2. Remove numeric performance rankings against PL/SQL classification and SQLInspect. Their representations, class definitions, and output units differ, and the study has no evaluated deterministic seven-class jOOQ baseline.
3. Rebuild Discussion around occurrence-level validation, relation to existing detectors, and the implications of recurring source-fragment patterns.
4. Separate measured findings from proposals for deterministic or hybrid rules, retrieved context, call-resolution analysis, and documentation studies.
5. Rebuild Threats under construct, internal, external, conclusion, and reliability validity.

## Required discussion content

- Occurrence matching tests class, count, and source span. Micro F1 was 0.869, varied by 0.010 across tested IoU thresholds, and ranged from 0.481 to 0.974 by class.
- The disagreement review supports observed error types, including local query semantics, inferred relationships, missing-value conventions, occurrence grouping, and span boundaries. It does not identify model reasoning or training-data causes.
- Existing SQL extraction, rule-based detection, and PL/SQL classification work should be compared by representation and output unit rather than by F1.
- The dominant source fragments identify candidate strata for independent audits and deterministic or hybrid baselines. They do not establish API risk, documentation effects, or design flaws.

## Required validity coverage

- **Construct:** study-specific definitions, single-annotator agreement, IoU/event matching, flags rather than prevalence, fragment categories rather than API risk, and unmeasured developer utility.
- **Internal:** detector-informed revision bias, data-dependent class and split selection, preliminary-frame duplicate and exclusion list, and one validation partition.
- **External:** dated GitHub target population, search omissions, open-source boundary, unsupported classes and query builders, and absence of a corpus transfer audit.
- **Conclusion:** sparse project support, conditional project bootstrap, descriptive one-run configuration comparisons, and limits of IoU sensitivity.
- **Reliability:** temporal reannotation versus independent reproducibility, one detector run, hosted-model drift, missing source/detector revisions and request artefacts, and partial rather than exact replay.

## Delete or compress

- Delete the speculative three-item class-frequency explanation.
- Delete direct metric comparisons with prior detectors.
- Delete the UI roadmap, generic prompting-framework expansion, and work-process reflections.
- Compress future work to independent annotation, repeated runs, corpus transfer audits, exposure denominators, resolved call targets, and same-task deterministic or hybrid baselines.

---
name: emse-novelty-positioner
description: Position and verify the novelty of an Empirical Software Engineering manuscript against current primary literature. Use when strengthening contribution claims, related work, or introduction novelty paragraphs involving static analysis, API- or AST-based rules, LLM code-smell detection, localisation, thesis-derived work, or possible overlap with existing EMSE studies.
---

# EMSE Novelty Positioner

Frame novelty as a defensible difference in research design and evidence.

## Comparison Workflow

1. Verify current related work from primary papers and official publication records.
2. Compare the manuscript along four axes:
   - extraction-based detectors such as SQLInspect;
   - API- or AST-specific rules;
   - LLM-based code-smell classification;
   - LLM-based line-level localisation or static-analysis evaluation.
3. Record for each comparator its input representation, target task, localisation unit, empirical scale, and principal limitation.
4. State what the paper combines that the individual comparators do not.
5. Add citations next to each contrast and weaken any unverified priority claim.

## Positioning for This Paper

Emphasise the combination of:

- direct analysis of dynamic \jooq Java and generated schema code;
- multi-label, multi-occurrence line-span localisation with explicit matching rules;
- validation on a held-out, manually annotated dataset;
- use of the validated detector as an instrument for prevalence, co-occurrence, and API-association analysis across 602 projects.

Do not claim novelty merely because an LLM is applied to \jooq. Do not claim superiority over SQLInspect or AST rules without a controlled comparison.

## Thesis Relationship

Require an explicit statement that identifies:

- the thesis on which the article is based;
- which dataset, software, experiments, and results originate there;
- what the article selects, reframes, synthesises, or extends;
- that no new experiment is implied unless one was actually performed.

Prefer transparent overlap language over vague repository references.

## Output

Produce:

- a compact comparison matrix;
- one sharp introduction paragraph;
- related-work integration requirements;
- contribution wording with bounded claims;
- missing or weak citations that require verification.

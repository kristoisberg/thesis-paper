# ESE Step 7: Study Design review

Date: 2026-08-28

Scope: `paper/sections/03_study_design.tex`

## Critical findings

- The section still combines repository sampling, detector configuration results, tool documentation, and corpus analysis as separate thesis chapters rather than one empirical pipeline.
- The held-out protocol omits the selected model and prompt, the one-run design, test-set frame, surviving reference and prediction counts, and the robustness procedures.
- The corpus and API-coding procedures do not state the complete analysis frame or a reproducible category-assignment rule.
- The reproducibility statement overclaims that all artefacts survive, and the AI-use disclosure lists obsolete thesis sections instead of separating research, coding, drafting, and editing assistance.

## Required structure

1. Study overview
2. Repository mining and target population
3. Operational scope
4. Sampling, reference annotation, and reliability
5. Project-disjoint partitioning
6. Detector configuration and execution
7. Localisation evaluation and error analysis
8. Corpus measures and API-pattern coding
9. Reproducibility and AI-use disclosure

## Required corrections

- Define the study population as the repositories identified by the dated GitHub search and filters, without claiming representativeness of all jOOQ projects.
- State that the 61-project sample came from the preliminary 603-project corpus and that the final corpus run used 602 projects.
- Retain the seven-class support rule, project-disjoint 21/20/20 split, label-informed seed search, and per-class project support.
- State the selected detector configuration in Study Design: Claude Opus 4.5, reasoning disabled, temperature 0.0, and Zero-Shot prompts.
- Describe the primary held-out run, one-to-one occurrence matching, IoU sensitivity, project-cluster bootstrap, and original versus detector-informed annotations.
- State that the corpus run covered 602 repositories and 17,450 relevant files and includes the sampled repositories.
- Define API coding as precedence-ordered string and regular-expression matches over detector-returned code fragments, with unmatched flags retained as other or uncategorised.
- Identify the frozen commits and missing raw responses, request metadata, source-repository revisions, and complete corpus file frame.

## Material to move online or remove

- Sampling-distribution plots and Head/Tail equations
- The 19-class annotation table and detailed exclusion essays
- Split-optimisation equations and the inaccurate dataset-use figure
- Omitted-model history, prompt iteration history, per-configuration result tables, and anomaly transcript
- Component architecture, tool workflow, CLI output, dependency inventory, and configuration-interface documentation
- Classification-only evaluation procedure and configuration cost-accounting detail

## Reviewer synthesis

No new empirical work is required. Step 7 is a consolidation and disclosure correction. The main paper should retain enough detail to reconstruct the study decisions while directing implementation and diagnostic material to the Online Resources.

# Introduction gap wording

Scope: the final two sentences of paragraph three in `paper/sections/01_introduction.tex`, and their transition into the following study objective. Discussion only; manuscript unchanged.

The passage introduces class labels, localisation agreement, and a reference process before explaining them. "How closely" is ambiguous between source proximity and agreement, while "reference process" obscures manual annotation. The claim that evidence is "needed before" counts can be interpreted leaves the reason implicit and overstates the dependency for descriptive flag counts.

Recommended replacement, incorporating the following study-objective paragraph:

> Existing evaluations leave open how well a detector can identify and locate individual SQL antipatterns in jOOQ source. We address this gap by comparing an LLM-based detector's predicted antipattern classes and source locations with manual annotations from held-out projects. We then analyse its flags across repositories in light of this evaluation.

This connects the representation problem to RQ1 and then RQ2. Explain the underlying motivation in discussion: similar aggregate counts can conceal differences in which occurrences are found. Retain "flags" for corpus output; reference agreement alone does not establish corpus prevalence.

Review input: writing-reviewer, supplemented by the primary agent's contextual analysis. Principles: A2 logical chaining, A5 claim-first exposition, B5 one idea per sentence, B7 concision.

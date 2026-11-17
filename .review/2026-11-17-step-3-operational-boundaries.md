# Step 3: operational boundaries, context, and independence

Date: 17 November 2026.

Status: complete. The historical rules, annotations, predictions, model runs, and numerical results are unchanged. The paper now distinguishes annotation criteria from detector instructions where their boundaries differ.

## Applied changes

- Relabelled Table 1 as annotation criteria and linked its interpretation to the detector-configuration subsection. This avoids implying that annotation and detector rules were identical.
- Clarified that ID Required's naming branch concerns the primary-key column, not the constraint name. The standalone `id` condition remains sufficient even without a visible alternative key. Its interpretation as a broad screening condition is stated near the definition.
- Added substring convenience methods and conservative unresolved-input inclusion to the search criterion. The SELECT/WHERE boundary is identified as annotation scope; the detector's broader regex/clause scope is stated in Methods.
- Corrected the description of 31 Flavors annotation: numeric ranges representing discrete business categories were included, while ordinary validity ranges and emptiness checks were excluded. Detector instructions retained their broader range exclusion. Constraint-versus-column span instructions are also distinguished.
- Described the primary-or-unique-key annotation criterion for Keyless Entry separately from the detector's primary-key instruction.
- Made the nullable/non-NULL-default screening condition explicit for Fear of the Unknown. Threats explains that a default does not prevent explicit NULLs and that human inspection could use business logic absent from a single-file detector request. Query-rule specificity is also distinguished.
- Explained visible schema evidence, including `asEnumDataType` and `getChecks`, and exclusion of standalone EnumType target files. Excluding enum implementation files does not eliminate enum references in table declarations.
- Clarified the chronology: codebook refinement covered the full annotation sample before partitioning; later prompt iteration and configuration selection excluded test projects. Removed the stronger implication of end-to-end test independence.
- Described case-sensitive lexical file selection, the three generated-source indicators, their use in prompt dispatch and corpus source roles, and separate Keys context.
- Specified implemented-detector Keys candidate recognition, longest character-level relative-path prefix, sorted tie handling, and empty context when no candidate exists.
- Described the implemented detector's default 240,000-character Claude budget, execution override, target priority, head/tail or prefix shortening, and remaining-space Keys shortening. The unmeasured truncation frequency and imperfect token-capacity proxy are stated in Threats.
- Removed the blanket assertion that all configurations had identical source/output preparation. The replication guide now explains the validation-notebook execution path and the different held-out/corpus decoding policies.

The manuscript presents these as study procedures and substantive limitations. Source comparisons, historical version distinctions, and detailed audit evidence remain in the replication guide and this record.

## Annotation and prompt evidence

Study inputs were read from `/home/kristoi/masters-thesis` at the frozen study revision `9913a7670fce52b135651f95ff18cd505c61b142`.

| Boundary | Source evidence |
|---|---|
| ID Required checks a column named ID and separately considers alternative keys. | `diagrams/decision/id-required.puml:11–20`; `prompts/zero-shot/ddl.md:3`. |
| Search annotation covers SELECT/WHERE LIKE/ILIKE and substring calls, including negative variants and unknown wildcard inputs. | `diagrams/decision/poor-mans-search-engine.puml:11–23`. |
| Search instructions include regex and unresolved inputs, exclude prefix search, and impose no SELECT/WHERE restriction. | `prompts/zero-shot/dml-dql.md:3`; historical embedded query prompt. |
| 31 Flavors annotation includes category ranges and uses CHECK-definition lines. | `diagrams/decision/31-flavors.puml:11–15`, including the explicit `order_status >= 0 AND order_status <= 3` example. |
| 31 Flavors instructions exclude range comparisons generally and request column-definition lines. | `prompts/zero-shot/ddl.md:6`; historical `src/prompts.ts:12`. |
| Keyless annotation accepts a suitable primary/unique key; the instruction names a primary key. | `diagrams/decision/keyless-entry.puml:13`; `prompts/zero-shot/ddl.md:4`; historical `src/prompts.ts:10`. |
| Fear of the Unknown treats nullable plus non-NULL default as sufficient and also permits business-logic inspection. | `diagrams/decision/fear-of-the-unknown.puml:11–23`; `prompts/zero-shot/ddl.md:7`. |
| The query tree enumerates notIn/self-equality, while the query instruction explicitly requires known nullability. | `diagrams/decision/fear-of-the-unknown.puml:30–36`; `prompts/zero-shot/dml-dql.md:5`; historical `src/prompts.ts:31`. |

The key/range/nullability/search clauses were also checked across Few-Shot, Chain-of-Thought, and Tree-of-Thought study prompt files. No instruction or annotation file was edited. The newly identified 31 Flavors and Keyless Entry differences extend the original plan's search-rule check. Their effects on individual scores were not estimated or asserted.

The numeric-range 31 Flavors false negative already reported in Results is consistent with the documented range-boundary difference. This observation does not establish that the instruction difference was its exclusive cause, so no causal attribution was added.

## Implemented-detector evidence

The following primary source revisions were inspected:

- Held-out execution: [80f3ff4](https://github.com/kristoisberg/jooq-antipattern-detector/tree/80f3ff4eeabdc3fec860bc35bb9a4566fe130763).
- Corpus execution: [245b50a](https://github.com/kristoisberg/jooq-antipattern-detector/tree/245b50aa381d9917e5febf9f4ab0cd13d1b9d944).

Both revisions' file-discovery selectors match `analysis/corpus_normalization.py`: 22 excluded path fragments, the three inclusion terms `org.jooq`, `Tables`, `tables`, 22 excluded signatures, and the three generated-source indicators. This verifies policy equivalence, not universal equivalence of historical traversal or decoded request contents.

`src/file-discovery.ts` sorts repository-relative paths, collects literal `public class Keys ` candidates before target filtering, and maximises character-level common prefixes. Strict comparison preserves the first sorted candidate in a tie; absence of candidates supplies empty context. There is no minimum proximity threshold. Only schema prompts attach Keys content.

`src/model.ts` resolves the matched Claude default as `200000 × 4 × 0.3 = 240000` characters, with an explicit override taking precedence. `src/analyzer.ts` passes this budget to `src/prompt-builder.ts`. The builder subtracts template space, prioritises numbered target source, then uses remaining space for Keys. It attempts head/tail retention with an omission marker and otherwise retains a prefix. Keys truncation retains a prefix with an ellipsis. No count of affected original requests or proof of the effective override was inferred from this source policy.

Four execution-source files were confirmed byte-identical between the historical revisions:

| File | Shared SHA-256 |
|---|---|
| `src/prompts.ts` | `08fd0d14121d17dac9c8ab50915af9cf0e57b85ced9929c270d549b212b6b369` |
| `src/prompt-builder.ts` | `0c039411b4a01b330f7a4f1e563d48f2a479a8ef24396f1ea80b8060ff721d92` |
| `src/model.ts` | `50c278db7e4b3ea1838c8d0fa07233d942f1d91ee16aaa10f6c562f7660753e4` |
| `src/analyzer.ts` | `045d6e92b8877ff9da5c64cbde624188ed90e37b78214973d1befa606a6480e5` |

The held-out implementation reads Latin-1, whereas the corpus implementation tries strict UTF-8 and falls back to Latin-1. The local replication guide records this distinction without claiming identical complete requests.

The validation notebooks are another execution path: unsorted Python glob enumeration, full-path `os.path.commonprefix`, direct opening of the chosen Keys file, and no implemented character-budget policy. The paper therefore scopes sorted ties, empty-context fallback, and truncation to the held-out/corpus detector. The old corpus-counting notebook's src-only traversal is likewise distinguished from recursive detector/article discovery in the guide.

Embedded detector prompts match between execution revisions but are not byte-identical to the study Markdown templates. They use “Beware of the Unknown” and add explanation/fix instructions. The localisation analysis normalises that class name; the verified class-boundary clauses match the corresponding study Zero-Shot instructions. No template identity across those two different representations is claimed.

## Verification and remaining scope

- `make paper` succeeds, producing a 31-page PDF.
- The final build has no undefined citations/references, no overfull vertical boxes, and no new overfull horizontal boxes. Two small pre-existing line-overflow warnings remain in Introduction lines 22–23 and Study Design lines 5–6. A new prompt-description overflow was removed by rephrasing the sentence.
- Extracted PDF text confirms the annotation-criteria caption, category-range inclusion, explicit prompt differences, sample-informed codebook description, Keys rule, and character budget.
- `git diff --check` passes. Numerical result tables, CSV/JSON analysis outputs, frozen study inputs, detector code, and prompts were not modified. No new model calls or annotations were made.
- No commits, pushes, or external publications were performed. New replication-guide details require inclusion when final analysis/documentation versions are published; existing code and study links already expose the primary sources.
- Sparse-project result context and the compact class-level revised-count table remain assigned to step 5. Baseline positioning and literature corrections remain assigned to step 6. Quantitative method specification remains assigned to step 4.

## Author clarifications after the rule comparison

The author reviewed the apparent differences individually. These clarifications qualify the initial comparison of written instructions above:

- Decision trees documented variants encountered in the annotated sample. Prompts deliberately included additional relevant variants; regex search was absent from that sample. Broader prompt coverage is therefore not itself an annotation inconsistency.
- The author attributed Keyless Entry's primary-key-only wording to prompt imprecision and recalled no unique-key variants in validation. The paper states the omission without claiming a newly verified absence count or an estimated effect on results.
- The blanket range exclusion for 31 Flavors was overly broad. Category-encoding ranges were intended to remain in scope.
- CHECK-based 31 Flavors occurrences were intended to return constraint-definition lines. The prompt's generic column-definition instruction failed to express that distinction.
- Query-level Fear of the Unknown annotation did check nullability. Its omission from the flowchart was an implicit step, not a demonstrated difference in annotation and detection criteria. The paper now states the shared requirement.

No historical prompts or annotations were changed. The manuscript and replication guide incorporate the clarified interpretation; the earlier literal source comparisons remain available here as an audit trail.

### Further clarification of validation coverage and observed spans

The author subsequently confirmed that both non-primary unique-key references for Keyless Entry and category-encoding numeric ranges for 31 Flavors were absent from validation. The paper now explains that these cases did not expose the corresponding prompt imprecisions during validation. This is author-supplied methodological clarification, not a new event-level classification or recount.

For CHECK-based 31 Flavors occurrences, the author also reported that inspected model responses consistently returned the intended constraint-definition spans despite the generic column-definition instruction. The manuscript describes those inspected responses without asserting a frequency or attributing observed errors to the wording. The earlier general threat sentence naming span-rule differences was narrowed to screening and available-context limitations.

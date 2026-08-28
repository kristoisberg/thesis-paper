# ESE word restoration: Step 7 threats audit

Date: 2026-08-28

Status: completed. No manuscript, supplement, bibliography, analysis, or figure file changed.

## Starting state

- Step 7 starting HEAD: `fe2b24d0a9bc3a8dd7d7aff05be0080a11c96bdb`.
- Threats to Validity TeXCount: 926.
- Main-paper TeXCount after Step 6: 9,930.
- PDF-extracted words after Step 6: 12,352.
- Main PDF pages after Step 6: 31.
- Threats source SHA-256: `67b021d1d1f30133924d4b6f21828c63083a25810bdf1ff501e225080b4c48c7`.

## Review deployment and synthesis

Three read-only specialists reviewed the restored passages against `paper/sections/06_threats_to_validity.tex`:

- The consistency checker found no critical issue or warning and mapped every restored topic to existing validity coverage.
- The logic reviewer found no flow break, argument gap, structural issue, or redundancy and recommended keeping the section unchanged.
- The technical reviewer agreed that the five-subsection structure covers the central evidence boundaries, but proposed explicit sentences about iterative codebook revision and future gateway caching, plus more detailed manifest-search wording.

The majority verdict and the root audit support no manuscript change. The codebook's dependence on one annotator is already bounded under construct validity, and same-annotator repeatability versus independent reproduction is covered under reliability validity. The dated manifest search and applied filters are bounded under external validity, while Study Design states the omitted dependency forms directly. A cache-specific sentence would introduce a provider mechanism not evidenced for the recorded single-pass executions. The plan and baseline ledger were corrected because their claim that Threats already contained a caching limitation was stale.

## Coverage matrix

| Restored consequence | Existing validity coverage |
|---|---|
| Operational definitions, iterative annotation, and class-specific judgments | Construct validity limits counts to the study definitions and one annotator; reliability validity distinguishes temporal repeatability from independent reproduction. |
| One-to-one span matching and localisation disagreements | Construct validity limits the event and overlap construct; conclusion validity limits the IoU sensitivity analysis. |
| Detector-informed reference revision | Internal validity identifies preferential recovery of detector-visible errors and the optimistic revised analysis. |
| Label-informed class retention and split selection | Internal validity records data dependence; conclusion validity records sparse project support and conditional bootstrap interpretation. |
| Manifest search, result cap, checked-in generated classes, and preliminary-frame corrections | External validity bounds the dated identified population; internal validity records the duplicate and incomplete exclusion list. |
| One-run configuration selection and the restored Opus trade-off | Internal validity covers one validation partition and execution; conclusion validity rejects reliable ranking; reliability validity records unknown run variance. |
| Corpus averages and source-fragment categories | Construct validity limits flags, size adjustment, API exposure, and unresolved call targets; external validity records the missing corpus audit. |
| Broader taxonomies and other query builders | External validity states that transfer to unsupported classes and representations is unknown. |
| Hosted execution, provider metadata, and exact replay | Reliability validity covers service change, missing request/provider/source metadata, unavailable revised spans, partial reruns, and the inability to replay exact requests and source states. |

## Explicit preservation checks

- The manuscript does not claim that omitted repositories form a small population or that manifest mining was the best approach.
- Gateway wording permits future hosted-service change without asserting that undocumented routing affected the recorded runs.
- Missing source and detector revisions, raw responses, request identifiers, complete request and provider metadata, retry histories, and the complete corpus frame remain explicit.
- The distinction between surviving-output inspection, partial reruns, and exact replay remains explicit.
- No new limitation duplicates the method's local qualifications or the Discussion's proposed experiments.

## Counts and verification

| Measure | Before Step 7 | After Step 7 | Change |
|---|---:|---:|---:|
| Threats to Validity TeXCount | 926 | 926 | 0 |
| Main-paper TeXCount | 9,930 | 9,930 | 0 |
| PDF-extracted words, including references | 12,352 | 12,352 | 0 |
| Main PDF pages | 31 | 31 | 0 |
| Threats source SHA-256 | `67b021d...c48c7` | `67b021d...c48c7` | unchanged |

- `git diff HEAD -- paper/sections/06_threats_to_validity.tex` is empty.
- `make paper` completed successfully with both targets up to date.
- The main log contains no LaTeX errors, undefined citations or references, or overfull boxes.
- BibTeX reports no warnings.

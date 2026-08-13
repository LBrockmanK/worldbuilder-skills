---
type: review
title: 'Review: pipeline quality trial spec'
description: Adversarial review of the pipeline quality trial spec (fail-check gate,
  input restructuring, decomposition step)
tags:
- agent-ready
date: 2026-08-13
timestamp: 2026-08-13T22:08Z
resources: []
---

# Review: pipeline quality trial spec

## Rounds
## Round 1 — digest `3f820252…`, anchor `ba6466a5` (dirty), tokens 53090, 2026-08-13T15:47:34-05:00, 188s

Anchor: ba6466a5f50b8236308af62cafc897c52bf1e470 (dirty tree)
Artifact digest: 3f82025267b2b888435ae11cd91a74768e9986e348874866e7a7f2a1d6a541f4 (sha256 over the exact scoped bytes as delivered)
Scope: .claude/specs/2026-08-13-pipeline-quality-trial-fail-check-gate-input-restructuring-and-decomposition-step.md

1. The trial can silently graduate fact-corrupting transformations
   Location: .claude/specs/2026-08-13-pipeline-quality-trial-fail-check-gate-input-restructuring-and-decomposition-step.md:42-44,50-59
   Quote: `- S6 (distinct builder voice): Add an LLM-driven rewrite pass after deslop/deframe that converts the preprocessed input into compressed clinical shorthand (abbreviated, no articles, no hedging). This is a new preprocessing stage, not a mechanical rule. Any reproduction of input phrasing in the character-voice output becomes immediately detectable.`
   Type: completeness
   Severity: critical
   Effort-to-fix: medium
   Risk-of-fix: medium
   Channel: fix
   Body: S6 introduces a nondeterministic LLM transformation that can omit, alter, or invent facts, while the four human dimensions and two mechanical checks measure presentation, echo, slop, and divergence—not factual fidelity. Condition C validates only that each input fact appears in an outline, not that mappings and manifestations preserve its meaning or introduce nothing unsupported. A condition can therefore win and be permanently adopted despite producing factually wrong character notes, with no specified downstream check detecting that wrong output.

2. The claimed 61%-to-0.7% echo reduction compares different metrics
   Location: .claude/specs/2026-08-13-pipeline-quality-trial-fail-check-gate-input-restructuring-and-decomposition-step.md:20
   Quote: `Pipeline v2 reduced input-derived echo from 61% to 0.7% of entries, validating the upstream approach.`
   Type: correctness
   Severity: major
   Effort-to-fix: small
   Risk-of-fix: low
   Channel: fix
   Body: The cited retest explicitly states that 61% was convergence-detector precision on 23 reviewed findings, whereas 0.7% was an input-echo rate over 146 entries; it says the metrics are not directly comparable. Presenting them as before-and-after echo rates materially misstates the baseline and effect size used to justify this trial.

3. The stated current failure modes contradict the cited retest
   Location: .claude/specs/2026-08-13-pipeline-quality-trial-fail-check-gate-input-restructuring-and-decomposition-step.md:20
   Quote: `Echo and slop remain the primary failure modes that cost human review time.`
   Type: correctness
   Severity: major
   Effort-to-fix: small
   Risk-of-fix: low
   Channel: fix
   Body: The cited Pipeline v2 retest concludes that the original input-echo problem is gone, behavioral Soul entries show the least convergence, output does not converge on generic filler, and detected convergence is mostly legitimate factual similarity. The spec supplies no newer evidence establishing echo and slop as the remaining primary failures, so its description of current pipeline state is unsupported and contrary to its evidence.

4. The Aeon resource is overstated as validation
   Location: .claude/specs/2026-08-13-pipeline-quality-trial-fail-check-gate-input-restructuring-and-decomposition-step.md:20
   Quote: `the [Aeon's Notebook resource review](../research/2026-07-30-resource-review-aeon-s-notebook-decision-engine-and-helpful-default-convergence.md) independently validates a spread-fail-check-select mechanism`
   Type: correctness
   Severity: major
   Effort-to-fix: small
   Risk-of-fix: low
   Channel: fix
   Body: The cited review classifies the resource as “Inspire,” calls it not directly adoptable, and records an n=1/model-confounded test. It identifies the mechanism as a research lead, not an independent validation. This mischaracterizes the evidentiary status of a lead the trial is supposed to test.

5. Condition A does not define its interaction with the baseline’s existing gate
   Location: .claude/specs/2026-08-13-pipeline-quality-trial-fail-check-gate-input-restructuring-and-decomposition-step.md:34-36
   Quote: `**Condition A — Fail-check gate.** Baseline plus a formal divergence gate between variant generation and synthesis.`
   Type: completeness
   Severity: major
   Effort-to-fix: medium
   Risk-of-fix: medium
   Channel: fix
   Body: Current `generation-rules.md` already requires a qualitative divergence check, discarding and regenerating all three variants with one retry when they are insufficiently distinct. Because A is “Baseline plus” the new gate, the artifact does not say whether both gates run, in what order, whether their retry budgets stack, or whether the mechanical gate replaces the qualitative one. Different compliant executions therefore perform different interventions and numbers of generations.

6. Retry exhaustion is nondeterministic
   Location: .claude/specs/2026-08-13-pipeline-quality-trial-fail-check-gate-input-restructuring-and-decomposition-step.md:36
   Quote: `Retry up to 3 times; if all retries fail, flag the entry and proceed with the best spread available.`
   Type: completeness
   Severity: major
   Effort-to-fix: small
   Risk-of-fix: low
   Channel: fix
   Body: “Retry up to 3 times” does not establish whether the initial attempt plus three regenerations or three total attempts are allowed. “Best spread” has no selection rule: it could minimize the maximum pairwise similarity, minimize the mean, minimize the number of failing pairs, or use prose quality. The fallback output—and thus trial scores—cannot be reproduced unambiguously.

7. The trial is too small to test its stated echo premise
   Location: .claude/specs/2026-08-13-pipeline-quality-trial-fail-check-gate-input-restructuring-and-decomposition-step.md:48,86
   Quote: `Generate the Soul section for one test character with established Design Notes.`
   Type: completeness
   Severity: major
   Effort-to-fix: large
   Risk-of-fix: low
   Channel: escalate
   Body: At the asserted 0.7% baseline rate, a single Soul section with roughly ten entries has an expected echo count far below one. Observing zero echoes in every condition would be the ordinary outcome and cannot establish improvement or sufficiency. The spec provides no power target, minimum entry count derived from the baseline, confidence treatment, or other basis for interpreting a null result.

8. Stochastic generation is treated as a single controlled observation
   Location: .claude/specs/2026-08-13-pipeline-quality-trial-fail-check-gate-input-restructuring-and-decomposition-step.md:48,63
   Quote: `Use the same character across all four conditions to control for input complexity.`
   Type: completeness
   Severity: major
   Effort-to-fix: large
   Risk-of-fix: low
   Channel: escalate
   Body: Holding the character constant does not control ordinary LLM generation variance. The spec does not select or pin the model, prompt version, temperature, sampling parameters, run count, or generation order. Its cited prior variant-count protocol required multiple runs expressly because one run was insufficient, and the later discriminator trial used three runs per cell with pinned models and constant parameters. Here, random generation variance can decide adoption.

9. Condition C’s coverage requirement conflicts with the Soul-only output
   Location: .claude/specs/2026-08-13-pipeline-quality-trial-fail-check-gate-input-restructuring-and-decomposition-step.md:44,48
   Quote: `The model must first produce a redistribution outline: for each input fact, which output section and entry it maps to, and what behavioral manifestation it becomes. The outline is validated for coverage (every input fact appears at least once) before generation proceeds.`
   Type: consistency
   Severity: major
   Effort-to-fix: medium
   Risk-of-fix: medium
   Channel: fix
   Body: The trial generates only Soul, but C requires mapping every Design Notes fact across all output sections. The artifact does not say whether facts mapped to Background, Body, or Relationships are discarded, whether only Soul-routed facts enter every condition, or whether C must force every fact into Soul. These alternatives produce materially different inputs, output counts, and comparisons.

10. Echo scoring does not identify which version of the input is authoritative
   Location: .claude/specs/2026-08-13-pipeline-quality-trial-fail-check-gate-input-restructuring-and-decomposition-step.md:42,56,66
   Quote: `Any reproduction of input phrasing in the character-voice output becomes immediately detectable.`
   Type: completeness
   Severity: major
   Effort-to-fix: medium
   Risk-of-fix: medium
   Channel: fix
   Body: Condition B creates an LLM-rewritten, clinical-shorthand input, but the protocol says only “Design Notes” are shown to the reviewer and invokes the existing grader, which compares outputs to source Design Notes. It never states whether human and mechanical echo checks compare against the original notes, the deslop/deframe result, the S6 rewrite, or all of them. Echoing the intermediate rewrite may consequently be invisible rather than “immediately detectable.”

11. The claimed prior rubric and 0.3 precedent are false
   Location: .claude/specs/2026-08-13-pipeline-quality-trial-fail-check-gate-input-restructuring-and-decomposition-step.md:52,90
   Quote: `The trial design follows the precedent set by the selection mechanism trial (2026-08-08): same rubric dimensions, same blind-review methodology, same 0.3 improvement threshold.`
   Type: consistency
   Severity: major
   Effort-to-fix: medium
   Risk-of-fix: low
   Channel: fix
   Body: The selection trial used one holistic 1–3 score whose anchors combined staging, specificity, echo, and slop; it did not score four separate dimensions. Its 0.3 rule defined a tie range among mechanisms, not an improvement-over-baseline threshold. The new design may intentionally choose a different rubric and rule, but describing them as the same methodology is incorrect and obscures that these choices lack the asserted precedent.

12. Human and mechanical metrics lack reproducible scoring and aggregation rules
   Location: .claude/specs/2026-08-13-pipeline-quality-trial-fail-check-gate-input-restructuring-and-decomposition-step.md:52-59
   Quote: `3. **Input echo** — Does the phrasing reproduce Design Notes input? (1 = clear echo, 2 = partial overlap, 3 = fully transformed)`
   Type: completeness
   Severity: major
   Effort-to-fix: medium
   Risk-of-fix: low
   Channel: fix
   Body: “Clear,” “partial,” “fully transformed,” “moderate,” “some filler,” and “clean” have no operational boundaries, examples, adjudication rule, or calibration procedure. The spec also does not define whether means weight entries, runs, or conditions equally, how variable entry counts are handled, or the denominator for reported mechanical rates. Reviewers and implementers can reach different scores from the same outputs while following the text.

13. The blind key is not required to be concealed from the reviewer
   Location: .claude/specs/2026-08-13-pipeline-quality-trial-fail-check-gate-input-restructuring-and-decomposition-step.md:63-68
   Quote: `2. Strip condition labels. Assign random letter codes (W, X, Y, Z) to the four conditions.`
   Type: completeness
   Severity: major
   Effort-to-fix: small
   Risk-of-fix: low
   Channel: fix
   Body: Relabeling is not sufficient blinding if the same person generates the conditions, assigns the codes, and reviews them. The protocol does not separate generator/key-holder/reviewer roles, seal the mapping, or otherwise require that the reviewer lack access to it. “Before unblinding” states timing but does not define who controls or can inspect the key, leaving a reachable biased execution compliant with the protocol.

14. The success rule has unresolved ties and threshold arithmetic
   Location: .claude/specs/2026-08-13-pipeline-quality-trial-fail-check-gate-input-restructuring-and-decomposition-step.md:72
   Quote: `If multiple conditions improve, adopt the one with the highest sum of per-dimension means (equal weight across all four dimensions).`
   Type: completeness
   Severity: major
   Effort-to-fix: small
   Risk-of-fix: low
   Channel: escalate
   Body: No outcome is defined when improving conditions have equal sums. The artifact also does not specify whether 0.3 and 0.1 comparisons use raw or rounded means, despite small samples making boundary equality plausible. The adoption result is therefore not guaranteed to be unambiguous.

15. A null result is allowed to close three bundled leads without testing them separately
   Location: .claude/specs/2026-08-13-pipeline-quality-trial-fail-check-gate-input-restructuring-and-decomposition-step.md:38-42,86
   Quote: `Negative results are valuable: if the current pipeline's 0.7% echo rate cannot be meaningfully improved by these interventions, that validates Pipeline v2 as sufficient and closes the S1/S3/S6 findings.`
   Type: correctness
   Severity: major
   Effort-to-fix: medium
   Risk-of-fix: medium
   Channel: fix
   Body: S1, S3, and S6 are introduced simultaneously in Condition B. A failure of that bundle cannot establish that each individual lead is ineffective, especially when one component may counteract another and the trial is too small to observe the stated echo baseline. The adoption rule nevertheless closes all three, producing a stronger conclusion than the experimental conditions support.

16. S6 is assigned to contradictory pipeline stages
   Location: .claude/specs/2026-08-13-pipeline-quality-trial-fail-check-gate-input-restructuring-and-decomposition-step.md:42,76,82
   Quote: `This is a new preprocessing stage, not a mechanical rule.`
   Type: consistency
   Severity: major
   Effort-to-fix: medium
   Risk-of-fix: medium
   Channel: fix
   Body: D1 places the LLM rewrite after deslop/deframe and explicitly calls it a new stage. D6 says S1/S3/S6 modify the deslop/deframe preprocessing script, while Consequences says restructuring happens “in the deslop/deframe step.” These are different architectures with different intermediate artifacts, failure handling, and implementation locations; the adoption decision does not identify which one ships.

FINDINGS: 1 critical, 15 major, 0 minor, 0 nit

### Round 1 adjudication

1. **ACCEPT.** Add a fifth metric dimension (factual fidelity) and require mechanical coverage validation for Condition C's outline.
2. **ACCEPT.** Remove the misleading before/after comparison; state the metrics separately.
3. **ACCEPT in part.** The retest's mechanical findings and the user's subjective experience of echo/slop diverge. Reground the claim in the user's stated experience, not the retest data.
4. **ACCEPT.** Downgrade "validates" to "proposes."
5. **ACCEPT.** Specify that the mechanical fail-check gate replaces the existing qualitative divergence check in generation-rules.md for all conditions that include it (A, B, C).
6. **ACCEPT.** Clarify: 3 retries means 3 additional attempts (4 total). "Best spread" = the spread with the lowest maximum pairwise Jaccard similarity.
7. **ACCEPT with modification.** The trial's primary purpose is overall quality improvement (staging, specificity, slop reduction), not echo-rate reduction specifically. The 0.7% baseline echo rate is too low to measure further improvement at this sample size. Reframe accordingly; echo is one dimension among five, not the primary target. Reject the "too small" label — the trial is appropriately sized for quality comparison, which is what it's actually testing.
8. **ACCEPT.** Add 2 runs per condition with pinned model and temperature. The user's design principle (LLM time is cheap) supports this.
9. **ACCEPT.** Specify that the decomposition outline maps all facts but only Soul-routed facts proceed to variant generation for this trial.
10. **ACCEPT.** Specify echo comparison is always against the original Design Notes (pre-preprocessing), for both human and mechanical checks.
11. **ACCEPT.** Remove the false precedent claim. Own the four-dimension rubric and 0.3 threshold as new choices informed by but not identical to the prior trial.
12. **ACCEPT in part.** Add brief operational boundary examples for each anchor. Full calibration procedure is disproportionate for a trial of this size.
13. **ACCEPT.** Specify that the agent generates and assigns codes, the human reviews without access to the mapping until scoring is complete.
14. **ACCEPT.** Add tie-break: prefer the simpler (lower-numbered) condition.
15. **ACCEPT.** A null result records that the bundled approach did not improve quality. Individual S-findings remain open for future separate testing.
16. **ACCEPT.** Unify: S6 is a new LLM-driven preprocessing stage that runs after deslop/deframe. D6 and Consequences updated to match.

## Round 2 — digest `a79c638d…`, anchor `ba6466a5` (dirty), tokens 50427, 2026-08-13T17:07:59-05:00, 210s

Anchor: ba6466a5f50b8236308af62cafc897c52bf1e470 (dirty tree)
Artifact digest: a79c638da0d90c5787d07de67db97d9481692e54aba66a61563d3af826e0aebf (sha256 over the exact scoped bytes as delivered)
Scope: .claude/plans/2026-08-13-pipeline-quality-trial-implementation.md

1. Title: Execution depends on a nonexistent approval gate
   Location: .claude/plans/2026-08-13-pipeline-quality-trial-implementation.md:17
   Quote: `Execution requires the plan artifact's approval flip (see Approval Gate).`
   Type: completeness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: The plan contains no “Approval Gate” section or approval field. An implementing worker therefore cannot determine what must be flipped or how execution becomes authorized. This is a dangling placeholder and violates the requirement for actionable, non-vague instructions.

2. Title: Required parent directories are never created
   Location: .claude/plans/2026-08-13-pipeline-quality-trial-implementation.md:39-57
   Quote: `- Create: \`trials/2026-08-pipeline-quality/results/\` (directory)`
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: Task 1 creates `inputs`, `out`, and `results`, but not the `scripts` and `conditions` directories required by Tasks 2 and 3. Task 2’s write and `cd` operations and Task 3’s copies require those parents to exist. As ordered, execution can fail before either task produces its files.

3. Title: The fail-check rejects the D1 boundary value
   Location: .claude/plans/2026-08-13-pipeline-quality-trial-implementation.md:168-179
   Quote: `"passed": max_sim < threshold,`
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: D1 rejects a spread only when a pair “exceeds 0.25,” so a maximum similarity of exactly `0.25` must pass. This implementation requires similarity to be strictly below `0.25`, rejecting the boundary incorrectly. The supplied tests all pass but omit this boundary case, allowing the D1 violation through.

4. Title: Condition B applies S1 and S3 at the wrong pipeline stage
   Location: .claude/plans/2026-08-13-pipeline-quality-trial-implementation.md:222-231
   Quote: `Before deslop/deframe, restructure the Design Notes input:`
   Type: correctness
   Severity: major
   Effort-to-fix: medium (several sites within scope)
   Risk-of-fix: medium (alters behavior on existing paths)
   Channel: fix
   Body: D1 defines S1 as reorganizing the preprocessed input and S3 as bundling within that result, while S6 explicitly follows deslop/deframe. The plan instead runs S1/S3 on raw Design Notes before deslop/deframe. That tests a different cumulative condition and could let deslop/deframe undo or alter the restructuring.

5. Title: Restructured-input artifacts have no defined paths
   Location: .claude/plans/2026-08-13-pipeline-quality-trial-implementation.md:288-290
   Quote: `Save the restructured input alongside the output.`
   Type: consistency
   Severity: major
   Effort-to-fix: medium (several sites within scope)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: Task 4’s file manifest lists only `run-1.md` and `run-2.md`; it names no files for the restructured inputs. “Alongside” does not establish whether the input is embedded in each run, written as a separate per-run artifact, or shared across runs. This prevents consistent implementation and makes the nondeterministic S6 preprocessing stage unauditable.

6. Title: The mechanical-grader command targets a nonexistent script and interface
   Location: .claude/plans/2026-08-13-pipeline-quality-trial-implementation.md:298-307
   Quote: `python ../../skills/worldbuilder-grader/scripts/detect_input_echo.py \`
   Type: correctness
   Severity: major
   Effort-to-fix: medium (several sites within scope)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: The repository’s detector is `scripts/detect_input_echo.py`, not `skills/worldbuilder-grader/scripts/detect_input_echo.py`. Moreover, that module exposes Python functions but has no CLI accepting `--input` and `--output` or emitting the promised JSON. The command therefore fails before producing any grader report. Task 2 repeats the same incorrect source path in its interface declaration.

7. Title: No implementation can produce the required within-model divergence results
   Location: .claude/plans/2026-08-13-pipeline-quality-trial-implementation.md:296-298
   Quote: `Run the existing grader checks (\`skills/worldbuilder-grader/scripts/detect_input_echo.py\`) on all 8 outputs`
   Type: completeness
   Severity: major
   Effort-to-fix: medium (several sites within scope)
   Risk-of-fix: medium (alters behavior on existing paths)
   Channel: fix
   Body: D3 requires mechanical input-echo and within-model divergence rates for every condition. The referenced detector provides input-echo categorization and cross-model comparison, not a runner that parses each output’s variant spreads and calculates within-model divergence. Conditions A–C have gate results, but the baseline has no equivalent calculation. Consequently Task 5’s requested “low-divergence count” cannot be computed consistently across all four conditions even after correcting the script path.

8. Title: The inbox update leaves an unresolved implementation choice
   Location: .claude/plans/2026-08-13-pipeline-quality-trial-implementation.md:387-389
   Quote: `Remove or update the grader agent inbox item to reflect the trial outcome.`
   Type: completeness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: The instruction neither identifies the exact inbox entry nor defines which outcomes require removal versus an update or what an update must record. The repository contains a relevant grader-agent item, but the plan leaves its resulting state indeterminate, violating the prohibition on vague instructions.

FINDINGS: 0 critical, 8 major, 0 minor, 0 nit

### Round 2 adjudication

1. **ACCEPT.** The "see Approval Gate" reference is part of the standard plan header template and refers to the workflow process, not a section in the plan. However, it's confusing for a standalone reader. Remove the parenthetical.
2. **ACCEPT.** Add `scripts` and `conditions` directories to Task 1 Step 1.
3. **ACCEPT.** Change `<` to `<=` in fail_check.py and add a boundary test case.
4. **ACCEPT.** The spec says S1 reorganizes "the preprocessed input" and S6 follows deslop/deframe. Fix ordering: S1/S3 run after deslop/deframe, then S6 runs after S1/S3.
5. **ACCEPT.** Define paths for restructured inputs: `out/condition-{b,c}/restructured-input-run-{1,2}.md` for S1/S3 output, and `out/condition-{b,c}/clinical-input-run-{1,2}.md` for S6 output. Add to Task 4 file manifest.
6. **ACCEPT.** The grader script path needs verification at execution time. Replace the assumed CLI with a note to check the actual interface and adapt. Remove the incorrect path from Task 2's interface declaration.
7. **ACCEPT.** Add a step to Task 4 that runs the fail-check gate script on baseline variant spreads to produce comparable divergence data for Condition 0.
8. **ACCEPT.** Specify: the inbox item is item 3 (current numbering after the schema-gap item was removed). If a condition graduates, update to record the trial outcome and which improvements were adopted. If negative result, update to note the bundled approach was tested and did not improve quality.


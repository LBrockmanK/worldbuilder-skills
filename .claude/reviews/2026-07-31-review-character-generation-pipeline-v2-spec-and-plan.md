---
type: review
title: Review — Character Generation Pipeline v2 Spec and Plan
description: Adversarial review of the Pipeline v2 spec (input restructuring, doctrine
  additions, grader agent) and implementation plan (6 tasks).
tags:
- complete
date: 2026-07-31
timestamp: 2026-07-31T10:56Z
resources: []
---

# Review — Character Generation Pipeline v2 Spec and Plan
## Round 1 — digest `44dc71a8…`, anchor `28ce6bc6` (dirty), tokens unknown, 2026-07-30T20:28:33-05:00, 311s

Anchor: 28ce6bc6552dc6a63e9f8a63b3910289dde42673 (dirty tree)
Artifact digest: 44dc71a883dd66413707d2a9071981ac3cfd2c271c069a22bc999338bb441fea (sha256 over the exact scoped bytes as delivered)
Scope: .claude/specs/2026-07-31-character-generation-pipeline-v2-input-restructuring-doctrine-additions-and-grader-agent.md, .claude/plans/2026-07-31-character-generation-pipeline-v2-implementation-plan.md

1. Routing annotations are neither persisted nor applied to all freeform notes
   Location: spec:76-82; plan:467-469
   Type: consistency
   Severity: major
   Effort-to-fix: medium
   Risk-of-fix: medium
   Channel: fix
   Body: The anchored spec requires each freeform note to remain in place while gaining a routing hint, covering both Session Notes and Builder Context. The plan instead calls routing a “mental annotation” and applies it only to Session Notes. Nothing records the hints for later generation or future agents, and Builder Context is omitted.

2. The deslop pass returns slop unchanged
   Location: spec:84-91; plan:374-415, 463-465
   Type: correctness
   Severity: major
   Effort-to-fix: medium
   Risk-of-fix: medium
   Channel: fix
   Body: The anchored spec says slop phrasing must not enter generation. The proposed implementation records matches but appends the original line unchanged to `cleaned_lines`. Task 3 then tells generation to work from this supposedly cleaned copy, so every flagged slop phrase still reaches generation.

3. The preprocessing implementation does not consume the promised rule sources
   Location: spec:86-89; plan:32, 196-198, 325-371
   Type: completeness
   Severity: major
   Effort-to-fix: medium
   Risk-of-fix: medium
   Channel: fix
   Body: The anchored plan claims to apply `docs/slop-phrases.md` and `skills/writing-style.md`, and its interface says the former is an input. The implementation hard-codes a small subset and never reads either file. Numerous documented patterns and writing-style rules can therefore pass without detection, while future changes to those sources will not propagate.

4. Deframing silently deletes substantive facts along with meta-vocabulary
   Location: spec:88-91; plan:374-400, 463-465
   Type: correctness
   Severity: major
   Effort-to-fix: medium
   Risk-of-fix: high
   Channel: fix
   Body: Any matching meta term causes the entire line to be dropped from the working copy. A line such as “Assigned to the Steward’s House as town guard” loses the in-world fact that the character is a town guard. Although a `Change` suggests replacement or user review, no later step processes those changes before generation.

5. The third Design Notes subsection conflicts with the unchanged skill structure
   Location: plan:59-87, 141-155
   Type: consistency
   Severity: major
   Effort-to-fix: medium
   Risk-of-fix: medium
   Channel: fix
   Body: The existing skill defines exactly two Design Notes subsections and directs all Q&A capture into Session Notes. The plan adds Structured Doctrine but does not instruct implementers to revise those statements or the Design Notes self-check. The same Q&A facts are consequently directed to both Session Notes and Structured Doctrine, creating duplication and an internally contradictory structure.

6. The value-conflict stance taxonomy is undefined and non-exclusive
   Location: spec:68; plan:82-83, 153
   Type: completeness
   Severity: major
   Effort-to-fix: medium
   Risk-of-fix: high
   Channel: escalate
   Body: “Role-following,” “role-compromise,” “alignment-compromise,” and “alignment-following” are not defined, nor is it explained how the compromise categories differ or how to classify a stance involving both. This directly fails the requirement that doctrine additions be well-defined and non-overlapping. The artifacts provide no basis for choosing the intended semantics.

7. Contrast declaration has no valid behavior when there is no existing cast member
   Location: spec:66, 136-137; plan:79-80, 117-122
   Type: completeness
   Severity: major
   Effort-to-fix: medium
   Risk-of-fix: medium
   Channel: escalate
   Body: The field requires an existing cast member, but no omission, deferral, or substitute rule exists for the first character or a standalone character. The proposed “standalone note” also does not satisfy the existing Relationships format, which requires each bullet to name a relationship and archetype. The intended fallback is a product decision absent from the artifacts.

8. Memory charge categories lack an operational boundary and output syntax
   Location: spec:70, 132-134; plan:85-86, 102-114
   Type: completeness
   Severity: major
   Effort-to-fix: medium
   Risk-of-fix: medium
   Channel: escalate
   Body: “Explains patterns,” “shapes present behavior directly,” and “context only” do not provide a reliable rule for separating high, mid, and low memories. The plan also never defines how a charge tag fits the existing strict Background fact-pair syntax. Different implementers can classify or serialize the same memory differently.

9. Values-carry-costs uses the same input and output shape despite the anti-echo doctrine
   Location: spec:56, 62, 118, 132-135; plan:73-74, 111-114
   Type: consistency
   Severity: major
   Effort-to-fix: medium
   Risk-of-fix: medium
   Channel: fix
   Body: Structured fields are said to be deliberately shaped differently from output sections, and generation must not reproduce input phrasing. Yet both the input prompt and Background requirement use essentially `[Value] —/→ [what it cost]`. That makes direct reproduction the easiest compliant output and undermines the stated echo defense.

10. New Soul coverage has ambiguous counting and is absent from completion checks
   Location: spec:126-130; plan:89-100
   Type: completeness
   Severity: major
   Effort-to-fix: medium
   Risk-of-fix: medium
   Channel: fix
   Body: The plan does not say whether the four doctrine entries are additional to, or may satisfy, the existing 3–5 psychological-entry minimum. Core want can overlap “core drives in action,” while false belief or value conflict can overlap irrational behavior or contradiction. The plan also does not update the skill’s self-check, so completion can be declared without verifying any of these additions.

11. Multi-option generation omits the feasibility mechanism promised by the spec
   Location: spec:95-102; plan:481-506
   Type: completeness
   Severity: major
   Effort-to-fix: large
   Risk-of-fix: high
   Channel: fix
   Body: The anchored spec bases feasibility on shared cached context and parallel subagents. The implementation is only prose telling one agent to generate three variants, with no batching, cache boundary, subagent protocol, resource limit, or behavior after the single retry also fails. Its divergence check is an unmeasurable question rather than the specified fail-check.

12. The required 2-versus-3-versus-5 option-count trial is missing
   Location: spec:185-190; plan:530-590
   Type: completeness
   Severity: major
   Effort-to-fix: medium
   Risk-of-fix: low
   Channel: fix
   Body: The spec explicitly requires empirical testing of whether three variants is the correct cost/quality point. The only option-generation trial fixes the count at three and compares selection mechanisms. No plan task maps to the required count tradeoff.

13. The selection trial confounds selection quality with fresh generation variance
   Location: spec:106-114; plan:553-562
   Type: correctness
   Severity: major
   Effort-to-fix: medium
   Risk-of-fix: low
   Channel: fix
   Body: The trial generates the Soul section three separate times, once per mechanism. To compare selectors, all mechanisms must receive the same variant sets; otherwise differences may come from newly generated candidates rather than mechanical selection, judging, or synthesis. The resulting winner would not establish which mechanism is better.

14. The selection decision rules contradict each other
   Location: plan:564-566
   Type: consistency
   Severity: major
   Effort-to-fix: small
   Risk-of-fix: low
   Channel: fix
   Body: A tie is first resolved in favor of the cheaper mechanism, but if all mechanisms are within 0.3 the rule selects the judge. An exact three-way tie satisfies both conditions and produces different winners. Precedence must be explicit.

15. The supplied input-echo test suite cannot pass the supplied implementation
   Location: plan:623-629, 690-706, 740-746
   Type: correctness
   Severity: major
   Effort-to-fix: small
   Risk-of-fix: medium
   Channel: fix
   Body: The proposed character-trigram Jaccard score for the partial-overlap test strings is approximately 0.26984, while the test requires a value greater than 0.3. Thus “Expected: all tests pass” is false before any threshold tuning, because that assertion tests the overlap function itself rather than `ECHO_THRESHOLD`.

16. Phrasing-similarity selection is not empirically validated
   Location: spec:179-190; plan:607-746
   Type: completeness
   Severity: major
   Effort-to-fix: large
   Risk-of-fix: medium
   Channel: fix
   Body: The spec requires a trial of methods that separates phrasing similarity from semantic equivalence. The plan simply chooses whole-string character-trigram Jaccard and tunes one threshold against four synthetic examples. It compares no candidate methods, has no labeled corpus, and does not measure false positives or false negatives. Short echoed phrases embedded in longer output can be diluted below the threshold.

17. Cross-model convergence is described but never implemented
   Location: spec:157-166; plan:594-605, 763-783
   Type: completeness
   Severity: major
   Effort-to-fix: large
   Risk-of-fix: high
   Channel: fix
   Body: Task 5 claims three-way categorization, but its API returns only `input_echo` or `clean`. The skill merely says to “compare entries pairwise,” without defining entry alignment, similarity method, threshold, two-model agreement handling, or code/tests. The central cross-model half of Part C therefore has no executable plan.

18. The proposed grader skill is not a valid discoverable skill artifact
   Location: plan:748-790
   Type: correctness
   Severity: major
   Effort-to-fix: small
   Risk-of-fix: low
   Channel: fix
   Body: The proposed `skills/worldbuilder-grader/SKILL.md` starts directly with a heading and lacks the required YAML frontmatter containing at least `name` and `description`, unlike the repository’s skill structure. It may not be discovered or invoked as an agent skill.

19. The grader is exposed before its Parts A/B dependency and graduation gate are satisfied
   Location: spec:153-177; plan:594-606, 758-783, 806-816
   Type: consistency
   Severity: major
   Effort-to-fix: medium
   Risk-of-fix: medium
   Channel: fix
   Body: The spec says the convergence grader depends on Parts A and B and is ready for authoring-pipeline integration only if the retest graduates. Task 5 creates an immediately usable skill that labels surviving convergence as slop before Task 6 performs that retest. No experimental-only status or activation gate prevents premature use.

20. The convergence retest cannot evaluate its own graduation criteria
   Location: plan:830-848
   Type: correctness
   Severity: major
   Effort-to-fix: medium
   Risk-of-fix: medium
   Channel: fix
   Body: “At least 2 models,” one from each provider, supplies no within-family comparison, yet the protocol requires determining whether cross-provider convergence differs from within-family convergence. Correction generation is optional even though correction value is mandatory. “Acceptable” precision and “similar” consistency also have no thresholds, so “all four criteria must hold” is not reproducible.

21. Multiple task steps retain placeholders or omit required changed files
   Location: plan:143, 583-589, 746, 852, 867-879
   Type: completeness
   Severity: major
   Effort-to-fix: medium
   Risk-of-fix: low
   Channel: fix
   Body: The plan leaves the SKILL insertion location to the implementer, leaves threshold tuning open-ended, uses `[character]`, `[Winner]`, `[Result]`, `X%`, and `Y%`, and refers to “inbox item 9” without a path. Task 6 says to update the prior findings and inbox item but its commit stages only the new trial directory. This violates the no-placeholders/complete-steps criterion and would leave declared outputs uncommitted.

22. Material failure modes are absent from the risk analysis
   Location: spec:214-218
   Type: completeness
   Severity: major
   Effort-to-fix: medium
   Risk-of-fix: low
   Channel: fix
   Body: The anchored risks omit silent fact loss during deframing, similarity-detector false positives/negatives, unavailable multi-model data, retry exhaustion, ambiguous doctrine classification, selection-trial confounding, relationship-format incompatibility, and cost growth proportional to every entry plus judging/synthesis. These are reachable failure modes exposed by the plan, violating the requirement that risks be acknowledged.

23. The household test contains a tautological assertion
   Location: plan:225-230
   Type: correctness
   Severity: minor
   Effort-to-fix: small
   Risk-of-fix: low
   Channel: fix
   Body: `assert "household" not in ... or "household" in ...` is always true. The test therefore does not verify whether household framing is removed, replaced, or retained, despite its name and comment.

24. Task 1’s declared file scope omits a file it explicitly changes
   Location: plan:43-46, 117-122, 173-176
   Type: consistency
   Severity: minor
   Effort-to-fix: small
   Risk-of-fix: low
   Channel: fix
   Body: The task’s Files list omits `skills/worldbuilder-character/relationships.md`, although Step 3 modifies it and the commit stages it. This makes scope and review preparation misleading.

25. The value-conflict test cites a nonexistent spec section
   Location: plan:855-857
   Type: other
   Severity: nit
   Effort-to-fix: small
   Risk-of-fix: low
   Channel: fix
   Body: The plan refers to “spec 6.2”; the value-conflict stance is defined in 3.1(f), while section 6 contains only the empirical-testing list.

26. The proposed detector includes an unused import
   Location: plan:682-685
   Type: other
   Severity: nit
   Effort-to-fix: small
   Risk-of-fix: low
   Channel: fix
   Body: `Counter` is imported but never used. This has no behavioral effect but leaves misleading implementation debris in the exact code the plan directs workers to create.

FINDINGS: 0 critical, 22 major, 2 minor, 2 nit

### Adjudication

| # | Verdict | Note |
|---|---------|------|
| 1 | Accept | Routing annotations need persistence and Builder Context coverage |
| 2 | Accept | Flagged slop must be removed or rewritten, not passed through |
| 3 | Accept | Should reference source files, not hard-code subset |
| 4 | Accept | Deframe must flag for review, not silently drop lines |
| 5 | Accept | Skill Q&A instructions must route doctrine answers to Structured Doctrine |
| 6 | Accept | Define all four categories from RoleCDE paper (user decision: define precisely) |
| 7 | Accept | Roster assumption: users fill out an initial roster before in-depth generation; contrast against existing roster members or as the starting point for a new character |
| 8 | Accept | Add operational boundaries for charge categories |
| 9 | Accept | Reshape input format to differ from output |
| 10 | Accept | Doctrine entries are additional to existing minimums; update self-check |
| 11 | Accept | Add subagent protocol details |
| 12 | Accept | Add variant-count trial to Task 4 |
| 13 | Accept | Selection trial must use same variant sets across all mechanisms |
| 14 | Accept | Specify precedence for tie-breaking rules |
| 15 | Accept | Fix test bounds |
| 16 | Accept | Add tuning step |
| 17 | Accept | Implement cross-model convergence detection |
| 18 | Accept | Add frontmatter to grader skill |
| 19 | Accept | Add experimental gate |
| 20 | Accept | Expand retest to 3+ models |
| 21 | Partial reject | Trial-result placeholders ([Winner], X%, Y%) are inherent to trial tasks. Non-trial placeholders (SKILL insertion point, inbox path) accepted. |
| 22 | Accept | Add missing failure modes |
| 23 | Accept | Fix tautological test |
| 24 | Accept | Add relationships.md to file list |
| 25 | Accept | Fix section reference |
| 26 | Accept | Remove unused import |

## Round 2 — digest `98ec01a7…`, anchor `28ce6bc6` (dirty), tokens unknown, 2026-07-30T21:03:35-05:00, 272s

Anchor: 28ce6bc6552dc6a63e9f8a63b3910289dde42673 (dirty tree)
Artifact digest: 98ec01a71c5d29d0b7010ac48c499671b8c3c9b3eab0d3dacf22b01bdaf7b8b0 (sha256 over the exact scoped bytes as delivered)
Scope: .claude/specs/2026-07-31-character-generation-pipeline-v2-input-restructuring-doctrine-additions-and-grader-agent.md, .claude/plans/2026-07-31-character-generation-pipeline-v2-implementation-plan.md

1. Deslop preprocessing silently deletes substantive character facts
   Location: .claude/plans/2026-07-31-character-generation-pipeline-v2-implementation-plan.md:376-422, 470-472
   Type: correctness
   Severity: critical
   Effort-to-fix: medium
   Risk-of-fix: high
   Channel: fix
   Body: In the anchored scoped artifact, any line containing a slop pattern is omitted wholesale from `cleaned`. For example, a detailed fact containing “navigates” or “enduring” disappears rather than being rewritten. Although `changes` records the deletion and the original file survives, the generation instructions consume `cleaned` without requiring review of those changes. The resulting character output can silently omit source facts, which is undetected downstream.

2. `[multi]` routing annotations discard the actual destinations
   Location: .claude/specs/2026-07-31-character-generation-pipeline-v2-input-restructuring-doctrine-additions-and-grader-agent.md:89-95; .claude/plans/2026-07-31-character-generation-pipeline-v2-implementation-plan.md:474-476
   Type: completeness
   Severity: major
   Effort-to-fix: small
   Risk-of-fix: medium
   Channel: fix
   Body: The anchored spec requires each note to identify which output section or sections it feeds. The plan records every multi-section combination as the same `[multi]` tag, losing whether the intended destinations are Background+Soul, Body+Relationships, or another subset. Future generation agents therefore cannot apply the promised routing.

3. Generation rules incorrectly require factual Background entries to be stageable behavior
   Location: .claude/specs/2026-07-31-character-generation-pipeline-v2-input-restructuring-doctrine-additions-and-grader-agent.md:158-162; .claude/plans/2026-07-31-character-generation-pipeline-v2-implementation-plan.md:466, 478-503
   Type: consistency
   Severity: major
   Effort-to-fix: medium
   Risk-of-fix: medium
   Channel: fix
   Body: The anchored spec expressly exempts factual Background memories from the staging test. The plan applies the fact-to-manifestation rule to every section and states that all three variants pass the staging test. This rejects the permitted compressed-memory form and can transform Background facts into behavior, contradicting both the Background format and the stated exception.

4. The first-character contrast fallback is absent from every implementation instruction
   Location: .claude/specs/2026-07-31-character-generation-pipeline-v2-input-restructuring-doctrine-additions-and-grader-agent.md:66; .claude/plans/2026-07-31-character-generation-pipeline-v2-implementation-plan.md:80-81, 118-123, 153-154
   Type: completeness
   Severity: major
   Effort-to-fix: medium
   Risk-of-fix: medium
   Channel: fix
   Body: The anchored spec resolves the no-roster case by contrasting the first character with an archetype or trope. The template, Q&A prompt, and Relationships requirement still demand a cast member and never carry that fallback into implementation. Accepted Round 1 finding F7 therefore remains unresolved on the reachable first-character path.

5. Memory-charge implementation contradicts and omits the accepted operational rules
   Location: .claude/specs/2026-07-31-character-generation-pipeline-v2-input-restructuring-doctrine-additions-and-grader-agent.md:77-83; .claude/plans/2026-07-31-character-generation-pipeline-v2-implementation-plan.md:86-87, 103-115
   Type: consistency
   Severity: major
   Effort-to-fix: medium
   Risk-of-fix: medium
   Channel: fix
   Body: The anchored spec supplies removal/behavior tests and requires inline syntax such as `[high] Fact → consequence`. The implementation text omits those tests and syntax, and describes mid-charge memories as “still referenced” where the spec says the character does not actively revisit or react to them. Implementers can still classify and serialize the same memory incompatibly, so accepted F8 is not fully resolved.

6. Values-carry-costs retains the prohibited input/output isomorphism
   Location: .claude/specs/2026-07-31-character-generation-pipeline-v2-input-restructuring-doctrine-additions-and-grader-agent.md:56-62, 145-147; .claude/plans/2026-07-31-character-generation-pipeline-v2-implementation-plan.md:74-75, 112-115
   Type: consistency
   Severity: major
   Effort-to-fix: small
   Risk-of-fix: medium
   Channel: fix
   Body: The anchored spec says the input must be a short declarative sentence and specifically not a fact pair. The plan’s input template still prescribes `[Value] — [what it has cost]`, while output uses `[Value held] → [what it cost]`. Direct copying remains the easiest compliant transformation, leaving accepted F9 unresolved.

7. Mechanism 3 changes from unconditional synthesis to a conditional fallback
   Location: .claude/specs/2026-07-31-character-generation-pipeline-v2-input-restructuring-doctrine-additions-and-grader-agent.md:125-127; .claude/plans/2026-07-31-character-generation-pipeline-v2-implementation-plan.md:505-513, 558-569
   Type: consistency
   Severity: major
   Effort-to-fix: small
   Risk-of-fix: medium
   Channel: fix
   Body: The anchored spec defines Mechanism 3 as a synthesis pass over all three variants. The generation rules say to use synthesis only when no single variant is clearly best, while the trial claims to apply all three mechanisms to every spread. This makes the tested and deployable definition of Mechanism 3 inconsistent.

8. The execution step reintroduces the selection-trial confound
   Location: .claude/plans/2026-07-31-character-generation-pipeline-v2-implementation-plan.md:560-564, 581-583
   Type: consistency
   Severity: major
   Effort-to-fix: small
   Risk-of-fix: low
   Channel: fix
   Body: The anchored trial protocol correctly says to generate once and apply all selectors to the same variant sets. Its execution step instead directs workers to generate the Soul section three times using each mechanism. Following that step again confounds selector quality with generation variance, leaving accepted F13 unresolved.

9. The variant-count trial still confounds count with a single fresh generation
   Location: .claude/plans/2026-07-31-character-generation-pipeline-v2-implementation-plan.md:562-570
   Type: correctness
   Severity: major
   Effort-to-fix: medium
   Risk-of-fix: low
   Channel: fix
   Body: The anchored plan compares the original three-variant run with one new two-variant run and one new five-variant run. With no replication, counterbalancing, or shared candidate design, ordinary generation variance can determine the winning count. The trial may commit a default option count without establishing the required cost/quality effect.

10. Cross-model comparison treats unrelated entries as convergence
   Location: .claude/plans/2026-07-31-character-generation-pipeline-v2-implementation-plan.md:759-828
   Type: correctness
   Severity: major
   Effort-to-fix: medium
   Risk-of-fix: high
   Channel: fix
   Body: In the anchored implementation, each entry is compared with every entry from every other model in the section. There is no alignment by source fact, entry identity, or semantic subject. Similar generic phrasing in unrelated bullets can therefore be labeled cross-model convergence. Accepted F17 called out entry alignment explicitly, but the added implementation still omits it.

11. The supplied cross-model tests fail because the function is never imported
   Location: .claude/plans/2026-07-31-character-generation-pipeline-v2-implementation-plan.md:619-622, 831-864
   Type: correctness
   Severity: major
   Effort-to-fix: small
   Risk-of-fix: low
   Channel: fix
   Body: The anchored test module imports only `categorize` and `ngram_overlap`. The subsequently appended tests invoke `compare_cross_model` without importing it, producing `NameError` instead of the expected passing suite.

12. The detector discards evidence required by its own report contract
   Location: .claude/plans/2026-07-31-character-generation-pipeline-v2-implementation-plan.md:719-743, 773-825, 912-916
   Type: completeness
   Severity: major
   Effort-to-fix: medium
   Risk-of-fix: medium
   Channel: fix
   Body: `categorize` returns only a category. For input echo, `compare_cross_model` records an overlap of `0.0` and no matching input line; for nonconvergent entries it also replaces the measured best overlap with `0.0`. The grader skill nevertheless requires reports to identify the matching input line, and the function documents an overlap score. That report cannot be produced accurately from the specified interface.

13. Single-model runs incorrectly report entries as clean
   Location: .claude/specs/2026-07-31-character-generation-pipeline-v2-input-restructuring-doctrine-additions-and-grader-agent.md:176-179, 234; .claude/plans/2026-07-31-character-generation-pipeline-v2-implementation-plan.md:890-910
   Type: consistency
   Severity: major
   Effort-to-fix: small
   Risk-of-fix: low
   Channel: fix
   Body: The anchored spec says single-model operation must degrade to input-echo-only reporting because cross-model divergence cannot be assessed. The skill’s normal flow labels every non-echo entry `clean` and describes cross-model comparison as optional. It can therefore assert “No action needed” without having evaluated half of the clean criterion.

14. The retest still cannot determine whether all graduation criteria hold
   Location: .claude/specs/2026-07-31-character-generation-pipeline-v2-input-restructuring-doctrine-additions-and-grader-agent.md:181-190; .claude/plans/2026-07-31-character-generation-pipeline-v2-implementation-plan.md:957-976
   Type: correctness
   Severity: major
   Effort-to-fix: medium
   Risk-of-fix: medium
   Channel: fix
   Body: The anchored retest now supplies enough models for within-family comparison, but “acceptable” precision, “differs” for cross-provider signal, and “similarly” for consistency still have no thresholds. Correction generation remains conditional even though correction value is mandatory and all four criteria must hold. Accepted F20 is therefore only partially resolved, and different reviewers can reach opposite graduation decisions from identical results.

15. The deframe implementation does not strip the standalone `household` vocabulary required by the spec
   Location: .claude/specs/2026-07-31-character-generation-pipeline-v2-input-restructuring-doctrine-additions-and-grader-agent.md:97-102; .claude/plans/2026-07-31-character-generation-pipeline-v2-implementation-plan.md:327-339
   Type: correctness
   Severity: major
   Effort-to-fix: small
   Risk-of-fix: low
   Channel: fix
   Body: The anchored spec explicitly lists “household” as builder-level vocabulary. The regex table recognizes only the compound `household assignment`, so inputs such as “the household’s narrative role” retain the prohibited framing and can leak into generated content.

FINDINGS: 1 critical, 14 major, 0 minor, 0 nit

### Round 2 Adjudication

Escalated to human after Round 2. User accepted remaining findings as executor concerns.

| # | Verdict | Note |
|---|---------|------|
| 1 | Accept + fixed | Deslop now keeps flagged lines with inline `[FLAGGED]` marker instead of deleting |
| 2 | Accept as executor concern | [multi] tag granularity resolved during implementation |
| 3 | Accept as executor concern | Background staging-test exemption clarified during implementation |
| 4 | Accept as executor concern | First-character contrast fallback carried from spec to implementation |
| 5 | Accept as executor concern | Charge-tag syntax and operational tests carried to implementation |
| 6 | Accept as executor concern | Values-carry-costs template format refined during implementation |
| 7 | Accept as executor concern | Mechanism 3 definition unified during implementation |
| 8 | Accept + fixed | Execution step now matches protocol (same variant sets) |
| 9 | Accept as executor concern | Variant-count trial replication addressed during implementation |
| 10 | Accept as executor concern | Entry alignment for cross-model comparison addressed during implementation |
| 11 | Accept + fixed | Missing import added to test file |
| 12 | Accept as executor concern | categorize() return value enriched during implementation |
| 13 | Accept as executor concern | Single-model degradation behavior addressed during implementation |
| 14 | Accept as executor concern | Retest thresholds defined during implementation |
| 15 | Accept as executor concern | Standalone household pattern added during implementation |

**Review closed.** 3 findings fixed in refine round 2. 12 findings accepted as executor concerns — these are implementation-level details that the plan's executor resolves during task execution. The plan is approved for implementation with these known items carried forward.


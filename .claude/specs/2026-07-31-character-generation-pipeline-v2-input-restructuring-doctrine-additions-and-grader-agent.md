---
type: spec
title: Character Generation Pipeline v2 — Input Restructuring, Doctrine Additions,
  and Grader Agent
description: 'Spec for three coordinated changes to the character generation pipeline:
  structured doctrine fields in Design Notes with freeform overflow, multi-option
  generation with divergence validation, and an input-aware grader agent for convergence-based
  slop detection.'
tags:
- deprecated
superseded-by:
- "[[2026-08-15-character-card-architecture-q-a-workflow-block-model-and-export-interface]]"
date: 2026-07-31
timestamp: 2026-08-15T14:37Z
resources:
- "[[2026-07-30-convergence-validation-experiment-findings-and-graduation-assessment]]"
- "[[2026-07-30-resource-review-aeon-s-notebook-decision-engine-and-helpful-default-convergence]]"
- "[[2026-07-25-resource-review-hoplight-a-webnovel-author-s-ai-writing-guide-and-character-builder-v3]]"
- "[[2026-07-11-causal-character-writing-for-llm-roleplay-friction-engines-and-trait-word-poisoning]]"
- "[[2026-06-03-blueprint-rework-design]]"
- "[[0001-three-phase-architecture]]"
output:
- "[[2026-07-31-review-character-generation-pipeline-v2-spec-and-plan]]"
---

> **Partially superseded.** The [Character Card Architecture spec](2026-08-15-character-card-architecture-q-a-workflow-block-model-and-export-interface.md) supersedes the generation-related portions of this spec: multi-option generation, Design Notes as generation input, and the grader agent. Content principles remain in force: doctrine entries, trait-word ban, values-with-costs.

# Character Generation Pipeline v2 — Input Restructuring, Doctrine Additions, and Grader Agent

## 1. Problem Statement

The cross-model convergence validation experiment ([findings](../../trials/2026-07-convergence-validation/2026-07-30-convergence-validation-experiment-findings-and-graduation-assessment.md)) revealed three problems in the character generation pipeline:

**P1: Input-derived convergence.** Models faithfully reproduce Design Notes phrasing, producing convergent output that is not independent slop but verbatim echo. This dominates the convergence signal, making cross-model convergence unreliable as a slop detector. Of 23 human-reviewed findings, most traced to input reproduction rather than independent generation.

**P2: Meta framing leaks.** Builder-level organizational terms ("Steward's House," household assignments) appear in Design Notes and propagate into character content where they do not belong.

**P3: Doctrine gaps.** Five character-doctrine candidates identified across multiple independent sources (Character Builder V3, causal character writing research, Decision Engine, RoleCDE paper) fill gaps the current framework does not cover: values without demonstrated cost, no required false beliefs, no cast-level contrast declaration, no memory-charge routing, no value-conflict stance.

These problems are connected. P1 and P2 are input-pipeline problems that prevent the convergence metric from graduating. P3 introduces new structured input fields that, by design, are orthogonal to output sections and resist echo. Solving them together produces a pipeline where the grader agent concept (convergence-based slop detection) can function.

## 2. Scope

This spec covers three coordinated changes, kept distinct but cross-referenced:

**Part A: Input restructuring.** How Design Notes are organized, preprocessed, and annotated before generation. Includes structured doctrine fields, freeform overflow handling, the routing annotation step, and the deslop/deframe preprocessing pass.

**Part B: Generation changes.** How the worldbuilder-character skill uses the restructured inputs. Includes multi-option generation (per-entry spread with divergence validation), the fact-to-manifestation instruction, and selection/synthesis mechanism.

**Part C: Grader agent.** Input-aware convergence detection as a post-generation quality check. Includes input-similarity filtering, cross-model comparison, and the methodology for retesting the convergence metric after Parts A and B land.

**Out of scope:**
- Export phase changes (ainime export procedure, SillyTavern mapping study — separate inbox items)
- Internal document shape for export targets (inbox item 7 — runs after this)
- Additive-doctrine adoption (inbox item 5 — the staged generation approach is compatible with multi-option generation but is a separate decision)
- Relationship archetype changes (the 12-archetype system is stable and not affected)
- Runtime Decision Engine concepts (dice rolls, prefill injection — these are for dynamic roleplay, not static note generation)

## 3. Part A: Input Restructuring

### 3.1 Structured Doctrine Fields

The following fields are added to the Design Notes template as named entries captured during the Q&A grilling phase. Each is short (1–3 sentences), specific, and deliberately shaped differently from any output section, forcing the generation step to synthesize rather than echo.

**(a) Core want.** The deeper want underneath surface desires. Not "a promotion" but "to be seen as competent by people whose opinion she did not ask for." Restored from the Character Foundry's Soul exploration questions, which the blueprint rework moved to conversation but did not codify as a required output.

**(b) Core fear.** The outcome, realization, or loss hardest to face. Paired with core want — the two define the character's motivational axis. Same provenance as core want.

**(c) Values carry costs.** For each top-ranked value (2–3 values): name the value, then state what holding it has cost in a short declarative sentence (not fact-pair format — the input shape must differ from Background's `[Fact] → [consequence]` output to prevent direct echo). Also name the lowest values and one act proving they are not held. Source: Character Builder V3, validated by causal character writing research ("domain + drive + cost").

**(d) False belief.** At least one belief the character holds wrongly and acts on with confidence. Extends the knowledge-boundaries rule (framework.md) from expertise limits to epistemic errors. Include the character's stated way of handling not knowing. Source: Character Builder V3.

**(e) Contrast declaration.** Which existing cast member this character is built against, and on which axis. Nothing in the current doctrine asks whether two characters in a cast are distinguishable. This field sits at the cast level — it references another character by name and states the differentiating dimension. Assumes an initial roster exists before in-depth generation begins (the standard workflow fills out a roster first); the roster provides the contrast targets. For the first character in a brand-new project, contrast against an archetype or trope the character is designed to subvert. Source: Character Builder V3.

**(f) Value-conflict stance.** State the character's operating code in their own unlaundered words. Declare which way they go when that code meets conventional decency, using one of four positions:

- **Role-following:** the character acts on their own code and pays whatever social cost results. Conventional decency does not override.
- **Role-compromise:** the character acts on their code but softens the execution — they do the role-consistent thing in a way that minimizes visible friction. The action is the same; the manner is modulated.
- **Alignment-compromise:** the character defaults to conventional behavior but visibly strains against it. They do the decent thing, but the cost shows — resentment, withdrawal, or compensating behavior elsewhere.
- **Alignment-following:** the character abandons their code when it conflicts with conventional expectations. They conform, and the suppressed code surfaces as indirect behavior (passive aggression, displacement, self-sabotage).

Name the specific lever that tips them from their default position to the adjacent one. State how guilt shows behaviorally, if it shows at all. Source: RoleCDE (arXiv:2606.01552). Caveat: the paper's demonstrated mitigation is fine-tuning, not prompting — treat this as something a dilemma test must verify, not something assumed to work.

**(g) Charge-scored memories.** Each formative memory in Background carries an explicit charge tag. The operational test for each level:

- **High:** the character's present behavior would visibly change if this memory were removed. The memory is unresolved — it still produces observable action today (avoidance, overcompensation, repetition of a pattern). Test: can you write a Soul entry that starts "When [present trigger], they [behavior], because [this memory]"? If yes, it is high.
- **Mid:** the memory explains why a pattern exists but the pattern would persist without it — it has been absorbed into habit. The character does not actively revisit or react to the memory. Test: does removing this memory change any Soul entry? If no current behavior depends on it specifically, it is mid.
- **Low:** the memory provides context (origin, class, geography) that orients the reader but drives no specific present behavior. Test: does this memory appear in any Because clause? If not, it is low.

The charge determines which output layer the memory feeds: high-charge memories generate Soul entries (present behavioral impact), mid-charge feed Background fact pairs, low-charge may appear in Background or be omitted if they add nothing behavioral. The tag is written inline with the Background fact pair: `[high] Fact → consequence`. Source: Character Builder V3 (charge-scored memory routing), validated by causal character writing research (emotional memory hooks — "compressed sensory fragments carry more weight than explanation").

### 3.2 Freeform Notes

Session Notes and Builder Context continue to accept freeform bullet-point content — user-added facts, details, ideas, and material that does not fit the structured fields. No format change.

### 3.3 Routing Annotation Step

After the Q&A grilling and freeform capture are complete, a lightweight preprocessing pass annotates each freeform note with which output section(s) it feeds: Background, Body, Soul, Relationships, or multiple. This is annotation, not reorganization — the notes stay where the user wrote them, but each now carries a routing hint.

Freeform notes that feed multiple output sections are the most likely to force synthesis during generation, because the model must decompose one input fact into entries across different sections.

Notes that feed only one section carry higher echo risk and are flagged for the multi-option generation step to treat with extra scrutiny.

### 3.4 Deslop and Deframe Pass

Before generation, a preprocessing step runs on all Design Notes content (structured and freeform):

- **Deframe:** Strip meta-vocabulary that belongs to the builder/player abstraction layer, not the character's world. "Steward's House assignment," "household," "narrative function," "thematic mirror" — these are builder shorthand. Replace with in-world equivalents or flag for the user.
- **Deslop:** Apply the stop-slop phrase list and writing-style rules to the input text. Input phrasing that would be flagged as slop in the output should not enter the generation step as source material.

This pass modifies a working copy of the Design Notes, not the original. The original is preserved as the permanent builder record (per the blueprint rework decision).

## 4. Part B: Generation Changes

### 4.1 Multi-Option Generation (Per-Entry Spread)

For each entry the generation step would produce (each bullet in Background, Body, Soul, Relationships), the model generates three variant renderings instead of one.

**Spread rules:**
- The three variants must express the same underlying character fact but with genuinely different phrasing, emphasis, or behavioral angle.
- A fail-check validates divergence: if all three variants use substantially similar phrasing or structure, the spread is rejected and regenerated with an explicit instruction to diverge. One retry.
- Variants are generated with shared prompt context (Design Notes, framework rules, prior entries) cached; only the per-variant output is new. Subagents run in parallel for cost efficiency.

### 4.2 Selection Mechanism

Three selection mechanisms are defined. The implementation plan should include an empirical trial comparing them on a test character before committing to one:

**Mechanism 1 — Mechanical rules.** Score each variant against stop-slop phrase list, input-similarity check (string overlap with source Design Notes), and writing-style rules. Select the highest-scoring variant. Cheapest, deterministic, cannot judge creative quality.

**Mechanism 2 — Judge agent.** A separate agent picks the best of three with a short rationale, guided by the framework's staging test and writing-style rules. More flexible, catches quality issues rules cannot, adds one LLM call per entry.

**Mechanism 3 — Synthesis.** A final pass takes the strongest elements from all three variants and writes a synthesis. Most expensive, could produce output better than any individual variant.

The trial should test all three on the same character and compare output quality via blind human review (same methodology as the convergence experiment's blinded correction review, but with a rubric rather than paired comparison).

### 4.3 Fact-to-Manifestation Instruction

The generation prompt includes an explicit transformation rule: "Design Notes state what is true about the character. You write how that truth manifests as observable behavior. Reproduce the semantic content; never reproduce the phrasing. If the input says 'refuses credit,' your output describes what refusing credit looks like — the specific gesture, deflection, or subject change — without using the phrase 'refuses credit.'"

This is an instruction-level defense. It is not sufficient alone (the anti-slop research showed instruction-tuning artifacts survive genre-imitation prompts), but it layers with the structural defenses (multi-option spread, structured doctrine fields) to reduce echo.

### 4.4 Doctrine Coverage Requirements

The following are added to framework.md's coverage requirements:

**Soul section additions:**
- Core want as behavioral description (1 entry minimum). How the want shows — not "she wants respect" but what she does when she senses disrespect.
- Core fear as behavioral description (1 entry minimum). What the character does when the feared outcome approaches.
- False belief in action (1 entry minimum). A behavior the character performs because of something they believe that is not true.
- Value-conflict stance as behavioral description (1 entry minimum). What the character does when their operating code collides with conventional expectations.

**Background section additions:**
- Charge tags on all formative memories. High-charge memories must also generate a corresponding Soul entry.
- Values-carry-costs entries (2–3 entries). Fact-pair format: [Value held] → [what it cost].

**Relationships section addition:**
- Contrast declaration. One entry (may be a standalone note rather than a relationship entry) naming the cast member this character is built against and the axis of differentiation.

### 4.5 Anchor Repetition vs Single Source of Truth

The causal character writing research advocates repeating key anchors across sections for dense activation. The writing-style rule says each fact lives in one place. Resolution:

**Facts live in one place. Behavioral consequences of facts appear wherever they are relevant.** A formative event is stated once in Background. Its behavioral impact appears in Soul (psychological pattern), Body (physical habit it produced), and Relationships (how it shapes a specific dynamic) — each time as a behavioral description, not a restatement of the fact. The fact is the anchor; its consequences are the repetition. This satisfies both the dense-activation goal and the single-source-of-truth rule.

### 4.6 Compressed Sensory Fragments

The causal character writing research advocates dense sensory fragments as emotional memory hooks ("the last thing she remembers: lowering her yukata's collar, one word — run"). These are powerful but tension exists with the staging test — a memory is not current behavior.

Resolution: Compressed sensory fragments are permitted in Background as high-charge memory entries. They do not need to pass the staging test because Background is factual, not behavioral. Their corresponding Soul entry (required for high-charge memories) must be stageable — the present-day behavior the memory drives, not the memory itself.

## 5. Part C: Grader Agent

### 5.1 Purpose

A post-generation quality check that uses cross-model convergence as a slop-detection signal. Separated from the authoring agent (per inbox item 9). Depends on Parts A and B landing first — the convergence metric cannot function as a slop detector until the input-echo problem is addressed upstream.

### 5.2 Input-Aware Detection

Before comparing outputs across models, the grader compares each output entry against the source Design Notes. The comparison measures phrasing similarity (not semantic similarity — the content should match; the phrasing should not).

Entries with high phrasing similarity to input are categorized as **input-echo** rather than **convergence**. They may still indicate a quality problem (the generation step failed to transform), but they are a different kind of problem than two models independently producing the same slop.

The grader reports three categories:
- **Input-echo:** output phrasing closely matches input phrasing. Indicates transformation failure.
- **Cross-model convergence (input-filtered):** two or more models produced similar output phrasing that does not trace to input. Indicates slop.
- **Clean:** output phrasing diverges from input and from other models. No flag.

### 5.3 Convergence Metric Retest

After Parts A and B are implemented, rerun the convergence validation experiment:
- Generate notes for the same two characters (Kallya, Nadja) using the new pipeline
- Run the same two-judge detection (Opus 5, GPT Sol)
- Apply input-aware filtering
- Human-review the filtered findings
- Assess against the same four graduation criteria (precision, cross-provider signal, correction value, consistency)

If the metric graduates after the retest, the grader agent is ready for integration into the authoring pipeline. If it does not, the findings document what remains unresolved.

### 5.4 Phrasing Similarity Method

The specific method for measuring phrasing similarity (string overlap, n-gram comparison, embedding distance, or LLM-as-judge) is left to the implementation plan. The spec requires only that the method distinguishes phrasing similarity from semantic similarity — output that means the same thing as the input is correct; output that says it in the same words is echo.

## 6. Decisions Requiring Empirical Testing

This spec defines several mechanisms where the best option is not knowable in advance. The implementation plan should include trials for:

1. **Selection mechanism** (4.2): mechanical rules vs judge agent vs synthesis — blind human quality comparison on one test character.
2. **Value-conflict stance effectiveness** (3.1f): whether the stance declaration actually affects model behavior at inference time, or requires fine-tuning as the RoleCDE paper suggests. Test via dilemma scenarios against the character.
3. **Phrasing similarity method** (5.4): which method best separates echo from semantic match.
4. **Multi-option generation cost/quality tradeoff** (4.1): whether 3 variants is the right number, or 2 or 5 performs better.

## 7. Consequences

### What changes
- Design Notes template gains 7 structured doctrine fields (3.1 a–g)
- A routing annotation step is added between capture and generation (3.3)
- A deslop/deframe preprocessing pass is added (3.4)
- Generation becomes multi-pass: spread → validate → select per entry (4.1–4.2)
- framework.md gains new coverage requirements (4.4)
- The anchor-repetition tension is resolved (4.5)
- The compressed-fragment tension is resolved (4.6)
- A grader agent is specified as a separate post-generation check (5.1–5.4)

### What does not change
- The 12 relationship archetypes, Fiske lens, and generativity hierarchy
- The Background/Body/Soul/Relationships section structure
- The When/Behavior/Because formula
- The staging test (extended with the compressed-fragment exception for Background)
- The trait-word ban
- Writing-style.md rules
- The export phase
- ADRs 0001–0004

### Risks
- Coarser structured fields may not capture all nuance a user intends — the freeform overflow is the safety valve
- The fact-to-manifestation instruction may be ignored under instruction-tuning pressure — multi-option generation is the structural backup
- Value-conflict stance may not work via prompting alone — flagged for empirical testing
- Multi-option generation increases generation time and cost proportional to entry count (3 variants + selection per entry) — acceptable for one-time character creation but cost should be measured during trials
- Deframe pass may silently lose substantive facts bundled with meta-vocabulary on the same line — the pass must flag for user review rather than silently dropping lines
- Input-echo detection false positives: short common phrases may trigger n-gram overlap above threshold despite not being echo. False negatives: echoed phrases embedded in longer output may be diluted below threshold. Threshold tuning against a labeled corpus is needed before production use
- Cross-model convergence detection requires multi-model data that may not be available for every character — the grader must degrade gracefully (report input-echo only) when single-model data is all that exists
- Charge-category classification is subjective even with the operational test — different sessions may tag the same memory differently. The Q&A grilling phase should surface the tag and confirm it with the user
- Doctrine additions (4 new Soul entries) increase minimum entry count and generation time — entries are additional to existing minimums, not substitutes

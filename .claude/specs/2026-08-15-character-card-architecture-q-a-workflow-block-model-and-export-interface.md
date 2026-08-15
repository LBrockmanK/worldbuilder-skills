---
type: spec
title: Character Card Architecture — Q&A Workflow, Block Model, and Export Interface
description: Replaces the generation pipeline with a Q&A-into-card workflow. Defines
  the card format (Core block with Background/Body/Soul, addon blocks for Relationships,
  Intimate Dynamics, and Voice/Dialogue) and the conversational extraction workflow.
  Based on the research audit findings.
tags:
- complete
date: 2026-08-15
timestamp: 2026-08-15T13:03Z
resources: []
---

# Character Card Architecture — Q&A Workflow, Block Model, and Export Interface

## Context

The [research audit](../research/2026-08-14-research-audit-ideal-character-descriptions-for-ai-roleplay.md)
identified two central findings: content quality is the primary
constraint on character description output, and the generation
pipeline's input-echo problem is structural — the pipeline itself
creates the conditions for echo by separating input (Design Notes)
from output (generated sections). No trial has tested actual roleplay
quality; all evidence is theoretical, community-sourced, or taste-
tested.

This spec replaces the generation pipeline with a Q&A-into-card
workflow and reorganizes the character card into a block model. It
supersedes the generation-related portions of the
[Pipeline v2 spec](2026-07-31-character-generation-pipeline-v2-input-restructuring-doctrine-additions-and-grader-agent.md)
while preserving the content principles that spec established
(structured doctrine fields, trait-word ban, fact-to-manifestation
transformation).

### Architecture

Three layers, each changing independently:

1. **Card format definition** — a reference document defining blocks,
   entry structure, content requirements, and writing rules. Not a
   skill — a specification that skills and export tools read.
2. **Q&A workflow skill** — the conversation skill that builds card
   entries. Handles question sequencing, coverage checking, entry
   translation.
3. **Export layer** — reads a completed card and maps it to target
   platform fields. Out of scope for this spec; noted in the non-
   normative section.

## Decisions

### D1. Card format: block model

A character card comprises a **Core block** (universal) and optional
**addon blocks** attached when relevant.

#### D1.1 Core block

Three sections organized by information type:

- **Background** — Facts and formative events. What is true about
  the character. Entries are fact pairs: a formative fact and what it
  made true. No behavioral framing — other sections handle
  manifestation.
- **Body** — Physical presence and habits. What you see and
  experience physically. One stageable sentence per entry.
- **Soul** — Psychological and social behavior. How they think, feel,
  and act. Entries follow the When/Behavior/Because structure
  embedded naturally in prose.

Each section has a target entry range (not a rigid count):
Background 4–8, Body 3–5, Soul 5–8.

#### D1.2 Depth-of-access grid (conceptual model)

A 3×3 grid crosses the three information-type rows with a depth-of-
access progression:

| | Immediate | Over time | Hidden / foundational |
|---|---|---|---|
| **Background** | Known history, visible circumstances | Things they let slip, stories that emerge | Formative wound, what they never tell |
| **Body** | Surface features, first impression, obvious mannerisms | Subtle habits noticed with familiarity | Hidden under clothes — scars, marks, physical tells |
| **Soul** | Social persona, default behavior with strangers | True self that emerges with trust | Motivational engine — core want, fear, false belief, value-conflict stance |

The grid is a conceptual tool for the Q&A workflow, not a document
structure. Entries land in flat sections (Background, Body, Soul).
The Q&A process uses the grid to guide question order and a coverage
check flags under-represented columns. The grid maps to how roleplay
unfolds over time: column 1 early, column 2 as the relationship
develops, column 3 in moments of depth.

#### D1.3 Required doctrine entries

Within the Core block, certain entries are mandatory. A card is not
finalized until all are present or the user explicitly waives
specific entries with a recorded reason.

- Core want (behavioral — Soul). Provenance: Character Builder v3's
  Core slot; community consensus on motivational engine.
- Core fear (behavioral — Soul). Provenance: same as core want;
  fear and desire form the motivational axis.
- False belief the character acts on (Soul). Provenance: Character
  Builder v3; described as "a scene generator" in the
  [Hoplight review](../research/2026-07-25-resource-review-hoplight-a-webnovel-author-s-ai-writing-guide-and-character-builder-v3.md).
- Value-conflict stance: which way they go when values collide with
  morality, the lever that tips them, how guilt manifests (Soul).
  Provenance: Character Builder v3; graduated in
  [convergence retest](../../trials/2026-07-convergence-retest/retest-results.md)
  (behavioral influence 3/4 scenarios — the only functionally
  validated doctrine entry).
- At least one unresolved tension or competing pull (Soul).
  Provenance: community sources in
  [causal character writing research](../research/2026-07-11-causal-character-writing-for-llm-roleplay-friction-engines-and-trait-word-poisoning.md);
  resolved states become shortcuts models can collapse to.
- Values with costs: at least one top value with its stated price
  (Background or Soul). Provenance: Character Builder v3 via
  Hoplight review; "a value without a cost is decoration."

#### D1.4 Addon blocks

**Relationships.** Named dynamics with specific other characters.
One entry per relationship. Relevant for cast-based worldbuilding;
not needed for standalone characters. The existing 12-archetype
framework and coverage requirements carry forward.

**Intimate Dynamics.** Optional; the user decides at project
planning whether a character includes this block (a human judgment,
not a formula). Entries are behavioral prose in the same format as
Soul (When/Behavior/Because embedded naturally). Three coverage
areas with 1–2 entries each:

- Attraction expression: how they show interest
- Hesitation and limits: what makes them slow down or hold a boundary
- Specific dynamic (if applicable): behavioral signature and the
  emotional need it serves

Mandatory friction point: one internal contradiction in intimate
behavior (e.g., craves closeness but pulls back when it becomes
emotionally real). The depth-of-access progression applies as a
conceptual lens matching the Core grid model.

**Voice / Dialogue.** Recommended when the character will be
exported to platforms that support example dialogue (CCv2/v3
first_mes, mes_example) or when voice distinctiveness matters for
the project. 2–4 example dialogue snippets, each a composite
showing of the character pulling from multiple Core areas
simultaneously. Prescriptive situation categories ensure the
character is shown from different angles:

- Casual / social
- Conflict / pressure
- Vulnerability / intimacy
- Authority / power dynamic
- Alone / internal

The user picks 2–4 categories relevant to their character. Each
snippet includes enough scene context to set the situation (making a
standalone scenario field unnecessary). The working sheet notes
which Core areas each example exercises as a coverage sanity check.

### D2. Q&A workflow: conversational extraction

#### D2.1 Collaboration model

The AI asks targeted questions, the human answers, the AI translates
answers into card-format entries, the human approves or revises.
This is the default mode. The human can always override: writing
entries directly, editing AI-proposed entries, or skipping questions.

Source material (existing cards, stories, game files) can substitute
for human answers — the same Q&A flow applies, with an extraction
agent answering from the source. This mode is noted here as an
interface point; the extraction agent design is a separate concern.

#### D2.2 Question sequencing

Suggested block order:
1. Core: Background → Body → Soul
2. Addon blocks (if flagged): Relationships → Intimate Dynamics →
   Voice/Dialogue

Within each Core section, questions follow the depth-of-access
progression (immediate → over time → hidden/foundational) to build
from surface to depth. Addon blocks follow their own coverage
structure: Relationships works through named characters,
Intimate Dynamics through its three coverage areas, and
Voice/Dialogue through selected situation categories.

Voice/Dialogue comes last because it draws from Core content — the
examples demonstrate what the earlier sections established.

#### D2.3 Entry translation

When the AI translates a human answer into a card entry, it applies
writing rules scoped by section type:

**Background entries** (factual, not behavioral):
- Orwell co-anchor (shortest word, active voice, cut waste)
- No meta-vocabulary from the builder abstraction layer
- Entries are fact pairs, not behavioral descriptions — the staging
  test, action-line convention, and fact-to-manifestation
  transformation do not apply here

**Body and Soul entries** (behavioral):
- Action-line convention (present tense, observable/audible only)
- Staging test ("can a director stage this?") — applies to the
  When and Behavior portions; the Because clause states internal
  motivation and is exempt from the staging constraint
- Trait-word ban (no adjective labels; behavior earns the word)
- Orwell co-anchor (shortest word, active voice, cut waste)
- Fact-to-manifestation transformation (reproduce semantic content,
  never reproduce phrasing from the user's answer)
- When/Behavior/Because structure for Soul entries

These are defaults. The user can override any rule for their project.
All rules are subject to future revision based on functional roleplay
testing.

#### D2.4 Coverage checking

Coverage checking is advisory — the AI classifies entries against
the depth-of-access grid using its judgment during the Q&A process
and reports observations, not deterministic pass/fail.

After each Core section, the workflow reports which depth-of-access
columns appear under-represented (e.g., "your Soul entries are all
surface-level — want to explore what drives them underneath?") and
suggests follow-up questions to fill gaps. The user can accept the
suggestion or mark the section as complete.

After the full Core block is complete, a cross-section check reports
any required doctrine entries (D1.3) that are missing. Missing
mandatory entries must be addressed before the card is finalized —
the user can fill them or explicitly waive specific entries with a
recorded reason (D1.3).

#### D2.5 Working document

Entries accumulate in an Obsidian markdown note as they are approved.
Each section is a markdown heading. Entries are bullet points under
their section heading. The working document may carry labels or
annotations (grid position, coverage area) that the export step
strips.

The specific file layout within the vault is not prescribed by this
spec — it follows whatever vault structure convention is in effect.

### D3. What this replaces

This spec replaces the generation pipeline: the workflow where
Design Notes are written during a Q&A grilling session and then
a separate generation step produces card sections from those notes.

Specifically superseded:
- Multi-option generation with synthesis selection (the generation
  mechanism)
- Design Notes as a separate document that feeds generation (the
  input stage)
- The grader agent as a post-generation quality check. In the Q&A
  workflow, input-echo is eliminated by construction (no separate
  input document to echo from), and quality is addressed entry-by-
  entry during creation with human approval rather than post-
  generation automated checking.

Preserved from the generation pipeline era:
- Content principles carried forward in D1.3, with some
  simplification: Pipeline v2 required charge tags on memories,
  2–3 values-with-costs entries, lowest-value evidence, and a cast
  contrast declaration. This spec requires one values-with-costs
  entry minimum and drops charge tags, lowest-value evidence, and
  contrast declarations as mandatory (they remain good practice,
  not gated requirements).
- Writing rules as section-scoped defaults (D2.3)
- Deslop/deframe as a concept applicable to source-material
  extraction (a separate concern). In the Q&A context, fact-to-
  manifestation transformation serves a related but distinct
  purpose: it rephrases user answers into behavioral prose, but
  does not detect or remove meta-vocabulary or boilerplate the way
  deslop/deframe preprocessing did.
- The relationship archetype framework

## Consequences

### What changes

- The `worldbuilder-character` skill is rewritten around the Q&A
  workflow. The current `framework.md` and `generation-rules.md`
  are replaced by the card format definition and the Q&A workflow
  skill.
- Character notes gain the block structure (Core sections + addon
  blocks). The working document may carry optional labels or
  annotations during creation (D2.5).
- The export layer's dependency shifts from the generation pipeline's
  output to the new card format definition.
- Design Notes as a standalone document type are retired — the Q&A
  conversation is the design process, and its output is the card
  entries directly.

### What does not change

- The vault structure and file management (scraibe-owned).
- The relationship archetype framework.
- The writing rules (carried forward as defaults).
- The three-phase architecture (Seed → Wide → Export) and platform
  decoupling (ADR 0001, ADR 0003).

### Risks

- The Q&A workflow has not been tested in practice. The depth-of-
  access grid, question sequencing, and coverage checking are
  designed from theory — they may need significant revision after
  real use.
- Retiring the generation pipeline removes the option to batch-
  generate sections. A user wanting to move quickly can accept the
  AI's first proposed entry without revision (the human-override
  capability in D2.1), but the workflow is inherently entry-by-
  entry.
- The card format definition is a new document type that skills
  and export tools depend on. Changes to it ripple to both.

### Notes (non-normative)

The [research audit](../research/2026-08-14-research-audit-ideal-character-descriptions-for-ai-roleplay.md)
identifies functional roleplay validation as the largest evidence
gap. No trial has tested whether these principles produce better AI
portrayals. This spec is designed from theoretical argument and
community consensus. Functional testing should follow
implementation.

Source-material extraction (importing characters from existing cards,
stories, or game files) feeds into the Q&A workflow as an
alternative answer source. The extraction agent design is a separate
spec concern, captured in the project inbox.

Export to target platforms (ainime, CCv2/v3, others) is out of scope.
The card format is designed to be exportable — the
[extraction reliability map](../../docs/extraction-reliability-map.md)
documents field coverage across targets — but specific mappings are
separate work.

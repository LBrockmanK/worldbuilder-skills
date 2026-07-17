---
type: research
title: 'Resource review: World-Forge multi-agent world pipeline'
description: 'Review of AndreiNicu/World-Forge (MIT, SillyTavern world-package pipeline).
  Verdict: Inspire, one Integrate-grade extraction — behavioral-audit patterns feed
  the character-testing doctrine thread; Style Contract enumeration is a candidate
  for direction.md; its ST runtime reference and target templates are source material
  for a SillyTavern export target.'
tags:
- complete
date: 2026-07-17
timestamp: 2026-07-17T02:33Z
resources:
- https://github.com/AndreiNicu/World-Forge
---

# Resource review: World-Forge multi-agent world pipeline

## Goals

Single-item resource review. User's question: is there anything in
https://github.com/AndreiNicu/World-Forge we might want to learn from and
apply to worldbuilder-skills?

Fetched fresh 2026-07-16 (repo overview, README, full tree, LICENSE,
`agent_roles/03b_The_Voice_Auditor.md`,
`agent_roles/SHARED_Style_Contract_Reference.md`,
`templates/World_Seed_Template.md`, `contracts/README.md`,
`agent_roles/Auditioner/00_The_Auditioner.md`).

## Results

### What it is

World-Forge (MIT, 62 stars) is a multi-agent pipeline of markdown agent
specs — no application code — run inside an agentic IDE extension
(Kilo Code/Cline), that takes a user from an interviewed "World Seed" to a
complete SillyTavern package: V3 character cards, a three-tier lorebook
system (Tier 1 world / Tier 2 character / Tier 3 arc-or-sandbox), a chat
completion preset, and audit reports. Eleven-plus phase agents (Interviewer,
Refiner, Architect, Editor, three parallel auditors, Compiler, Prompt
Engineer) plus post-launch agents (Reviser, Converter, Brainstormer,
Auditioner). A companion SillyTavern fork consumes runtime contracts kept
canonical in the repo's `contracts/` directory.

It is the closest published analogue to this plugin found so far: same
problem shape (structured drafting → validation → export to a card+lorebook
runtime), different target (SillyTavern vs ainime-games.com) and different
host (IDE orchestrator vs Claude skills on scraibe).

### Answer to the user's question

Yes — mostly in its validation layer, which is far more developed than
ours, and directly serves a gap our own doctrine already flagged as missing
("testing doctrine for characters does not currently exist", item 10 of
[causal character writing](2026-07-11-causal-character-writing-for-llm-roleplay-friction-engines-and-trait-word-poisoning.md)).

**1. The Voice Auditor's behavioral test matrix (strongest learning).**
A build-time simulation pass after structural editing: generate sample
dialogue from the drafted material *as if you were the runtime model*, then
audit it. The scenario classes are the valuable part — the matrix must
contain more than the happy path:

- *on-script* — canonical beat, the case that almost never fails;
- *trigger collision* — two-plus behavioral triggers firing at once, chosen
  for maximum contradiction, verifying the spec resolves priority;
- *near-miss (false trigger)* — a scene that resembles a trigger context
  but should NOT fire it (kindness with a visible price attached), catching
  reflex misfires;
- *off-script pressure* — the user acts against the scene's grain;
- *coverage-void probe* — a scene deliberately aimed where card and state
  are silent, forcing the "would the model invent this" question;
- *lull* — user goes passive; do NPCs act on their own standing goals?

**2. Author/grader separation with a pre-committed failure.** Before
writing each sample, the auditor pre-commits the plausible failure, writes
the dialogue as a cold read with the expected-outcome columns out of view,
and audits afterward. "A line you had to consciously supply is a line the
drafts did not compel." Dialogue written to pass its own audit verifies
nothing. Directly applicable to how our blind-trial kit and any future
character self-check should be run.

**3. Evidence rule + counterfactual probe.** A PASS must cite both the
dialogue line and the spec line that compelled it; then ask whether the
same spec would equally permit the failing version. If yes, the verdict is
"present but NOT BINDING" — the fix is converting descriptive prose into
directive language or adding a missing context qualifier. This names a bug
class (mandates that exist but don't bind) our framework.md doesn't
currently distinguish from absence.

**4. Blind-line voice distinctiveness test.** Strip names from generated
dialogue; if you can't tell who is speaking from prose alone, the voice is
not distinct. Scales to a cross-NPC "distinctiveness matrix" for large
casts, where the failure mode is homogenization rather than per-character
infidelity.

**5. The Auditioner (post-launch cousin).** On-demand single-scenario
probe against a shipped world: one character, one scene, verdict forced to
YES / NO / IT DEPENDS (never "probably"), every behavior traced to a spec
line — an untraceable behavior is itself the finding. A nice UX shape if we
ever want a player-facing "would she do this?" skill.

**6. Style Contract as enumerated engine metadata.** Prose conventions —
perspective, tense, narration/dialogue/emphasis markers, paragraph
register — are captured once at seed time as *enums with canonical
directive prose per value*, then parameterized into the export preset;
per-card overrides are structured fields validated for coupling. Our
`direction.md` is free prose exported verbatim as `arcManagerGuidance`;
whether ainime's runtime warrants enumerated style fields is an open
question, but "declare conventions once, as fields, and derive directives
mechanically" is a cleaner contract than hoping free prose covers
perspective and tense.

**7. Skill-hygiene patterns worth copying regardless of domain.** Each
agent spec opens with a context manifest ("load exactly this / do NOT
load") — an explicit token-discipline device. The runtime-behavior
reference exists twice: authoritative long form plus a compact distillation
agents consult first. Contracts shared with the downstream runtime live in
one canonical directory, mirrored byte-identical with a CI drift check.

**8. Source material for a SillyTavern export target (user-added,
2026-07-16).** The plugin's Export phase was designed for multiple
frontend targets — phases 1 and 2 are platform-agnostic; only Export
writes platform field names. World-Forge is direct source material for a
SillyTavern target: `Notes_On_functionality.md` is an authoritative
reference for SillyTavern's runtime prompt-assembly behavior (with
`Notes_Quick_Reference.md` as the compact distillation); `templates/`
holds the target formats (V3 character card JSON, lorebook JSON, chat
completion preset JSON); `tools/validate_export.py` is a read-only
validator for the exported package; `contracts/` documents the runtime
seams. MIT license permits direct extraction and adaptation. Caveat: the
ST package is richer than a field mapping — World-Forge's three-tier
lorebook split and its preset/override architecture have no direct analog
in our Wide-phase notes, so an ST export needs a mapping study (which
note types feed which tier, what carries the preset's role) before a
skill gets written.

### Contrasts (noted, not adopted)

- **Anti-slop stance is inverted.** World-Forge explicitly refuses a house
  voice — "slop" is whatever the user's Style Contract says it is. Our
  plugin ships an opinionated writing doctrine as a quality floor. Both are
  coherent product decisions; theirs trades floor for fidelity to user
  taste. No change proposed, but it is the strongest published counter-
  position to our stop-slop approach and worth citing in the blind-trial
  writeup.
- **Tier axis differs from our layer axis.** Their tiers partition by
  permanence/scope (world / character / current-arc); our concept layers
  partition by discoverability (surface / mid / deep). The transferable
  part is the discipline ("every piece of information belongs to exactly
  one tier"), which we already approximate via type homes.

## Consolidation

Verdict: **Inspire**, with one Integrate-grade extraction. MIT-licensed,
so extraction is unencumbered; nothing to adopt wholesale (wrong host,
wrong orchestration model), no reason to ignore. The audit patterns
(items 1–4) attach to the existing character-testing thread — they should
inform the battle-test self-check candidate in
[causal character writing](2026-07-11-causal-character-writing-for-llm-roleplay-friction-engines-and-trait-word-poisoning.md)
and the design of any post-trial validation doctrine, not spawn a separate
workstream. The Style Contract idea (item 6) is a separate small question
against `defaults/templates/direction.md`. The Integrate-grade piece is
item 8: the user confirmed (2026-07-16) that multiple export frontends
were the point of the plugin's platform-agnostic phase design, which makes
World-Forge's SillyTavern runtime reference, target templates, and export
validator working source material for a future
`worldbuilder-sillytavern-export` skill — tracked via the mapping-study
inbox line below. Routing below.

### Routing (apply verbatim on approval)

**Amend inbox line 2** (the blind-trial line) — append to the existing
line, before its final period:

`; when the trial's results are folded into doctrine, also fold in the World-Forge audit patterns (scenario classes, cold-read author/grader separation, counterfactual probe / not-binding verdict, blind-line voice test) from the resource review`

**New inbox line:**

`- 2026-07-16T05:30: Evaluate enumerating style-contract fields (perspective, tense, markers, register) in defaults/templates/direction.md instead of relying on free prose, per the World-Forge resource review (Style Contract, item 6) — depends on what the ainime runtime actually honors; check docs/target-system.md first.`

**New inbox line (SillyTavern export target):**

`- 2026-07-16T05:45: SillyTavern as a second export target — Export phase was designed for multiple frontends. First step is a mapping study: which Wide-phase note types feed a V3 card vs the tiered lorebooks, and what carries the chat-preset role. Primary reference: World-Forge (MIT) — Notes_On_functionality.md / Notes_Quick_Reference.md for ST runtime behavior, templates/ + tools/validate_export.py for target formats; see the resource review (item 8).`

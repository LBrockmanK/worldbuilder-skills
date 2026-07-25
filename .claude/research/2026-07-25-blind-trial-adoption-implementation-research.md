---
type: research
title: Blind-Trial Adoption Implementation Research
description: 'Implementation research for adopting the 2026-07-23 blind-trial outcome:
  what stopslop and the additive doctrine concretely differ by, where they fold into
  shipped skills, and every site that renders relationship archetype labels.'
tags:
- human-ready
date: 2026-07-25
timestamp: 2026-07-25T15:37Z
resources: []
---

# Blind-Trial Adoption Implementation Research

## Goals

Establish what "adopt packet-1's instructions" means as concrete file
edits, before planning them. Three questions:

1. What does the stopslop style arm actually differ by, relative to
   shipped `skills/writing-style.md`?
2. What does the additive doctrine arm add, and how much of it is
   already shipped?
3. Where do relationship archetype labels get rendered, given the
   trial found all six arms misapplying them?

Results feed
[2026-07-25-blind-trial-adoption-cut-filler-additive-principles-relationship-labels.md](../plans/2026-07-25-blind-trial-adoption-cut-filler-additive-principles-relationship-labels.md).
Trial outcome:
[2026-07-23-writing-doctrine-blind-trial-results-viralys-nadja.md](2026-07-23-writing-doctrine-blind-trial-results-viralys-nadja.md).

## Results

### How the trial kit composes a packet

`trials/2026-07-writing-doctrine/build.py` concatenates, in order:
`src/base.md` with two markers replaced —
`<!-- DOCTRINE-BLOCK -->` at `base.md:99` and
`<!-- STYLE-BLOCK -->` at `base.md:104`. Doctrine levels:
`current` inserts nothing, `additive` inserts `doctrine-additive.md`,
`tensions` inserts `doctrine-additive.md` then `doctrine-tensions.md`.

`base.md` is assembled from the shipped skill files: its Background,
Body and Soul sections match `framework.md`, its Writing Rules match
`SKILL.md:82-106`, and it inlines `relationships.md` and `intimate.md`.

### The style axis is one section, not a rewrite

`src/style-current.md` is an edited subset of shipped
`skills/writing-style.md` — same rules, `###` instead of `##`, minus the
intro. `src/style-stopslop.md` differs from it by exactly two things:

- **Removed:** the `### Style Model` block (`style-current.md:1-12`).
- **Added:** `### Cut Filler` (`style-stopslop.md:1-19`).

**The Style Model removal is not a treatment and does not threaten
[ADR 0004](../adr/0004-action-line-style-model.md).** `base.md:62-65`
states the action-line convention independently of the STYLE-BLOCK, so
every arm — stopslop included — carried the action-line style model.
Dropping it from the style block was de-duplication. The style axis
therefore tested exactly one thing: presence or absence of Cut Filler.

Cut Filler bans five groups: throat-clearers, emphasis crutches, jargon
standing in for a plain verb, adverbs of degree, and vague declaratives.

**Overlap with shipped content.** Four of the five groups are new. The
fifth — vague declaratives ("the stakes are high", "the reasons are
structural") — is already covered by
`skills/writing-style.md:58-65` (*No significance inflation*).
`docs/slop-phrases.md` is not referenced by the trial file and covers a
different pattern scope (interiority hedging, copula avoidance, AI
vocabulary); it neither duplicates nor supersedes Cut Filler.

Appending Cut Filler verbatim would duplicate the vague-declaratives
rule, which `skills/writing-style.md:147` (*Single source of truth*)
forbids.

### The doctrine axis: five principles, three of them novel

`src/doctrine-additive.md` (71 lines) adds:

| Principle | Source | Shipped coverage |
|---|---|---|
| Banned Trait Words | `doctrine-additive.md:3-17` | Partial — `framework.md:70-80` has the label-vs-behavioral table but not the three-part replacement formula (domain / drive / cost) |
| Knowledge Boundaries | `doctrine-additive.md:19-30` | None |
| Unresolved States | `doctrine-additive.md:32-43` | Partial — `framework.md:105-110` (Contradictions) and `SKILL.md` starting-state rule cover internal friction, not leaving the character's direction open |
| The Specification Boundary | `doctrine-additive.md:45-57` | None |
| A Life in Motion | `doctrine-additive.md:59-70` | None |

The Specification Boundary is explicitly distinguished from the shipped
no-hedging rule (`SKILL.md:86`): no-hedging governs what you commit to
when you write a fact; the specification boundary governs which facts
you decline to write at all. Both can coexist, but the distinction has
to survive the fold-in or the two rules read as contradictory.

### Relationship labels are mandated in four places

The trial's "misapplied labels" finding has a simpler cause than
mis-orientation: the labels were never supposed to be visible, and four
separate instructions say otherwise. `relationships.md:23` states
archetypes "do not appear in the final card as labels" — and is
contradicted inside its own file.

| Site | Instruction |
|---|---|
| `skills/worldbuilder-character/relationships.md:76` | "**Format:** Bold `**Name — Archetype(s):**` prefix inline on the bullet" |
| `skills/worldbuilder-character/relationships.md:79-81` | Worked example bullet: `- **Mira — Kin:** ...` |
| `skills/worldbuilder-character/SKILL.md` (Relationships checklist) | "Each entry in bullet format with `**Name — Archetype(s):**` prefix" |
| `defaults/templates/character.md:37` | "_Named relationship dynamics. One bullet per relationship: **Name — Archetype(s):** [behavioral description]_" |

The operative format instruction and the worked example both won over
the line-23 disclaimer, which is why all six arms rendered labels.

### Authority carries no direction

`relationships.md:27` defines Authority bidirectionally: "mentor,
employer, elder, or superior upward; apprentice, subordinate, or ward
downward". Labelling a downward relationship "Authority" is therefore
correct as written — the shipped text, not the generating model,
produced the trial's Nadja/Liza result.

`Charge` (`relationships.md:47`) is the intended downward archetype but
currently excludes formal subordinates: "not their kin and **not a
formal subordinate**". Making Charge the downward counterpart requires
removing that exclusion, which widens the archetype's meaning.

Two dependent sites reference Authority as the power-asymmetry anchor
and would become wrong if Authority narrows to upward-only:
`relationships.md:53-55` (Coverage Requirements, both major and
supporting) and the Relationships checklist in `SKILL.md`.

### Build, test and lint

- Build: `python scripts/build-okf.py` — reads `defaults/okf.base.json`
  and `defaults/templates/*.md`, writes `defaults/okf.json`. Required
  after any template edit; `defaults/okf.json` is never hand-edited.
- Tests: `python -m pytest tests -q` — 14 unit tests across
  `tests/test_generate_templates.py` and `tests/test_build_trial_kit.py`.
- Lint: `doodle --strict skills`, configured by `.doodle.toml`
  (doodle-lint 1.0.0, project-word allowlist).
- CI runs both the pytest and lint jobs (`.github/workflows/tests.yml`).
- No pre-commit hooks.

## Consolidation

The adoption is smaller than "adopt packet-1" suggests. The style axis
reduces to one new section merged against an existing rule; the doctrine
axis reduces to three novel principles plus two partial extensions.

The relationship work is a separate concern that the trial surfaced
incidentally, and it is the more clearly-earned fix of the two: it
corrects a self-contradiction in shipped content rather than acting on a
single-cell preference. Its one judgment call — widening Charge to
absorb formal subordinates — was settled by the user on 2026-07-25.

Both threads edit `skills/worldbuilder-character/SKILL.md`, so they
should be sequenced rather than run in parallel.

---
name: worldbuilder-world-planning
description: Use at the start of every worldbuilding session — new project or returning one. Assesses current state, determines where you are in the pipeline, and routes to the right skill. Also use when entering a new phase, when unsure what to work on next, or when the project feels stuck or disorganized.
---

# World Planning

## Overview

This skill is the single entry point for all worldbuilding sessions. Every session starts here. It reads project state, determines the current phase, proposes next steps, and hands off to the appropriate skill.

**Hard gate principle:** Phase completion is a prerequisite, not a suggestion. No character work before the household structure in `world-seed.md` is complete. No lorebook or calendar before the foundation decisions are finalized. Each phase produces the context the next phase depends on.

**Ask by default:** At any decision point — a design choice, missing information, options to weigh — stop and surface it to the user. The cost of fixing errors in generated documents is higher than the cost of answering an upfront question.

---

## Opening Act: State Assessment

Before any other action, determine what exists.

### New project

If `worldbuilding-plan.md` does not exist at the project root, this is a new project.

1. Ask whether there is existing material to draw from — notes, documents, prior world exports, URLs, anything.
2. **If yes → route to `worldbuilder-ingestion`.** Ingestion characterizes the material, resolves conflicts upfront, produces an index, and routes back here with extracted content and a confirmed entry point.
3. **If no existing material** → ask the Early Project Decisions (see below), record answers in `worldbuilding-plan.md`, and route to `worldbuilder-world-foundation`.

Do not attempt to read and absorb material yourself before routing to ingestion. Ingestion is the skill designed for that work.

### Resuming a project

If `worldbuilding-plan.md` exists:

1. Read it.
2. Cross-check each "Done" status against the actual artifact file. If the plan says Done but the file is absent or obviously incomplete, note the discrepancy — artifacts are ground truth, not the plan document.
3. Identify the current phase and the next incomplete task.
4. Present a brief state summary to the user before routing anywhere:

   > "Here's where things stand: [phase and status summary]. Based on that, the next step is [proposed action]. Does that match your plan, or do you want to do something different?"

The user can redirect before any skill is invoked. Accept their override without question and follow it.

### Revision intent (v2.0)

If the user indicates they want to revise, improve, or substantially rework an existing project — not just continue it — treat this as a revision pass rather than a resume.

Route to `worldbuilder-ingestion` with the existing project documents as the material. Ingestion will:
- Assess what's in good shape vs. what needs work
- Establish the revision scope with the user (targeted improvement, full reprocess, expansion, or platform adaptation)
- Route to the appropriate phase or skill

The distinction from resume: resume means "continue where we left off"; revision means "here's what we want to change."

### State summary format

Keep it short — one short table and one line of proposed action is enough:

```
Phase 1 (Seed)        Done    → world-seed.md
Phase 2a (Lorebook)   Done    → lorebook.md
Phase 2b (Calendar)   Done    → calendar.md
Phase 2c (Story Dir.) Done    → story.md
Phase 2d (Roster)     Done    → characters/roster.md
Phase 2e (Blueprints) 6/24    → characters/blueprints/
Phase 3a (Cards)      2/24    → characters/cards/

Next: Continue blueprints. Suggested: dispatch 4 in parallel.
```

---

## Three-Phase Framework

### Phases and skills

| Phase | Group | Skill | Deliverable |
|---|---|---|---|
| 0. Ingestion | Pre-Seed | `worldbuilder-ingestion` | Ingestion index + extracted content |
| 1. Seed | Seed | `worldbuilder-world-foundation` | `world-seed.md` |
| 2a. Lorebook | Wide | `worldbuilder-lorebook` | `lorebook.md` |
| 2b. Calendar | Wide | `worldbuilder-calendar` | `calendar.md` |
| 2c. Story Direction | Wide | `worldbuilder-story-direction` | `story.md` |
| 2d. Character Roster | Wide | (this skill — see below) | `characters/roster.md` |
| 2e. Character Blueprints | Wide | `worldbuilder-character-blueprint` | `characters/blueprints/*.md` |
| 3a. Character Cards | Deliverables | `worldbuilder-character-blueprint` | `characters/cards/*.md` |
| 3b. Review | Deliverables | — | Sign-off across all documents |

### Dependency structure

```
[Ingestion — optional, when existing material exists]
    └─►
Seed (world-seed.md)
    └─► Character Roster
            ├─► Lorebook      ─┐
            ├─► Calendar       ├─► Character Blueprints ─► Cards ─► Review
            └─► Story Dir.    ─┘
```

The Seed phase is strictly sequential with everything that follows. The Character Roster must exist before blueprints begin. Lorebook, Calendar, and Story Direction are independent of each other and can proceed in parallel once the Roster exists. Individual characters are independent of each other once the Roster is complete.

### Phase 2d: Building the character roster

No dedicated skill exists for the roster. Build it here, with user input, before dispatching to `worldbuilder-character-blueprint`.

The user seeds the cast — names they already have, roles they know they want, characters with personal significance. From each seed, branch through relationships: who is in their household, who do they conflict with, who do they depend on? Fill structural gaps (unfilled archetype slots, households without characters) with proposals for the user to accept, modify, or reject. Never assign a character to a slot without the user's knowledge.

Roster entry format:

```
**[Name]** — [Household] | [Type: Major/Supporting] | [Species/age] | Available day [N]
Role: [one or two phrases]
Archetype: [slot from cast architecture]
Key relationships: [named, one per line]
Intimate Dynamics: Yes  ← only if applicable; omit line if not
Summary: [2–3 sentences of behavioral character, not physical description]
```

Coverage check before declaring the roster complete:
- All 6 romance archetype slots filled across gender presentations
- Non-romance archetypes placed: authority figure, mentor/elder, elderly anchor, child or teen, outcast/philosopher, practitioner, the one who left (or didn't), the secret-carrier
- 2–3 characters with meaningful negative-track content
- Every household has at least one character assigned
- Default count: 8 main / 16 side (range: 6–10 main, 6–20 side)
- Anti-redundancy check: no two romance candidates filling the same slot with the same execution

---

## Early Project Decisions

Ask these before beginning Phase 1. Record answers in `worldbuilding-plan.md`.

**Intimate dynamics scope:** Does this project include explicit intimate content? Options: all romance-eligible characters, a specific subset, or none. If the answer is "some" or "all," identify which characters and flag them in the roster with an `Intimate Dynamics: Yes` marker. This decision is made once and recorded — not revisited character by character. During blueprint work, check the roster flag; if absent, skip intimate dynamics without further consideration.

---

## Phase Completion Criteria

Use these checklists at each phase gate. If any item is unresolved, surface it to the user before proceeding.

### Seed phase complete

`world-seed.md` must contain all of the following:

- [ ] All six foundational questions answered (setting wound, community character, player connection, hidden layer, era, household clusters)
- [ ] Setting Summary written — time, place, society, tone; concrete and specific
- [ ] Genre & Tone written — primary genre, tonal range, content notes
- [ ] Inspirations and Tonal Inspirations listed with specifics
- [ ] Key Tropes & Themes: 8–12 entries
- [ ] Community Description written — social and emotional identity, not physical
- [ ] World Introduction written — pre-game player text
- [ ] Opening Story Arc written — evocative, not scripted
- [ ] Ongoing Story Direction placeholder (can be brief; expands after roster)
- [ ] Locations list: 10–14 named locations, one sentence each
- [ ] Art style reference written
- [ ] Musical theme written
- [ ] All 6–8 household clusters written with: function, internal tension, inter-household connections, trajectory, narrative hook
- [ ] No individual character names assigned yet — household types and counts only
- [ ] Every household has at least one named connection to another household

### Lorebook complete

- [ ] All three layers present (surface, mid, deep) with appropriate date gates
- [ ] Location entries written for all major locations
- [ ] Background NPC guidelines entry written, active from day 1
- [ ] Keywords cover realistic phrasings; no partial-match traps

### Calendar complete

- [ ] Era defined
- [ ] Weather pool written (6–8 types with narrative weight)
- [ ] Daily Planner Directive written covering all five structural elements
- [ ] All 4 major festivals written with full atmospheric descriptions
- [ ] All 4–5 minor observances written
- [ ] First-year one-time events written if needed

### Story Direction complete

- [ ] Opening arc written — evocative, not scripted
- [ ] All ongoing story direction sections present: author framing, romance pacing, dark themes, hidden layer handling, seasonal tone, pacing, year 2+ NPC relationships

### Character Roster complete

- [ ] All coverage check items from Phase 2d above verified
- [ ] Every character has: household, type, species/age, available day, role, archetype, key relationships, summary
- [ ] Intimate dynamics flags set where applicable

### Character Blueprints complete (per character)

- [ ] All three foundation dimensions filled out (body, environment, soul)
- [ ] 3–5 behavioral descriptions in When/Behavior/Because form
- [ ] Contradiction and irrational behavior identified with emotional root
- [ ] Influence thresholds drafted for all six bands
- [ ] Introduction and future storylines written
- [ ] `## Lorebook Candidates` section present (may be empty)

### Character Cards complete (per character)

- [ ] All prose assembled as a single flowing block — no internal headers
- [ ] Future Storylines section present and separate
- [ ] All six influence threshold bands present with 2–4 examples each
- [ ] Token count in target range (~900 supporting, ~1500 major)

### Review complete (full cast)

- [ ] Relationship synchronization verified: if A names B, B's card names A
- [ ] Every household's internal tension represented in at least one character card
- [ ] All romance candidates have romance arc guidance
- [ ] No generic threshold language (the engine handles warmth and distance automatically)
- [ ] Dark arc characters have hope-tending language and witness-not-savior framing

---

## Parallel Execution

### What can run in parallel

**Phases 2a, 2b, 2c** (Lorebook, Calendar, Story Direction) — fully independent once the Roster exists. Dispatch one agent per deliverable.

**Phase 2e, Character Blueprints** — once the roster exists, every character is independent. Dispatch in groups of 3–4 per agent.

**Phase 3a, Character Cards** — once a blueprint exists for a character, that card is independent. Parallelize freely.

### What must run sequentially

**Phase 1 (Seed)** before everything else.

**Phase 2d (Roster)** before any blueprints begin.

**Relationship Sync Pass** — run at two points: (1) after each household group of blueprints, while the characters are fresh in context; (2) a final pass after all cards are complete. The blueprint-level pass catches inconsistencies before they carry into card prose.

### Constructing agent prompts for parallel character work

Each agent needs, stated explicitly:

1. The roster — full document or at minimum the relevant household section
2. The target character's complete roster entry
3. Which skills to invoke
4. Where to save the deliverable
5. An explicit constraint: do not modify other character files or the roster

Example structure:
> "Write the blueprint for [Name] using `worldbuilder-character-blueprint`. Roster entry for [Name]: [paste]. Household members for context: [paste relevant entries]. Save to `characters/blueprints/firstname-lastname.md`. Do not modify the roster or any other character's file."

---

## Plan Document

Produce or update `worldbuilding-plan.md` at the project root at the start of a project and at each phase transition.

```markdown
# [World Name] — Worldbuilding Plan

**Setting summary:** [One sentence]
**Current phase:** [Phase name and number]
**Characters:** [Count and completion status]
**Last updated:** [Date]

---

## Early Project Decisions

Intimate dynamics scope: [all / subset / none]
Subset details (if applicable): [character names]

---

## Phase Status

| Phase | Group | Status | Deliverable | Notes |
|---|---|---|---|---|
| 1. Seed | Seed | Done / In Progress / Not Started | world-seed.md | |
| 2a. Lorebook | Wide | ... | lorebook.md | |
| 2b. Calendar | Wide | ... | calendar.md | |
| 2c. Story Direction | Wide | ... | story.md | |
| 2d. Roster | Wide | ... | characters/roster.md | |
| 2e. Blueprints | Wide | ... | characters/blueprints/ | X of Y complete |
| 3a. Cards | Deliverables | ... | characters/cards/ | X of Y complete |
| 3b. Review | Deliverables | ... | — | |

---

## Current Phase Tasks

- [ ] [Task with named deliverable]

---

## Parallel Work Opportunities

[What can be dispatched independently right now]

---

## Open Questions

[Unresolved decisions that need addressing before proceeding]
```

---

## Self-Review at Phase Gates

Before declaring a phase complete:

1. **Completeness** — Does every deliverable have all required sections? Run the checklist above.
2. **Internal consistency** — Do characters reference households that exist? Do households reference inter-connections that have been established?
3. **Open question scan** — Any placeholders, TODOs, or flagged decisions still outstanding? Surface them to the user before moving on.
4. **Forward dependency** — Does the next phase have everything it needs from this one?

If any check reveals an unresolved issue, ask the user before marking the phase done.

---

## Common Failure Modes

**Skipping the state assessment.** Invoking a skill without first reading worldbuilding-plan.md and the artifacts produces work that conflicts with decisions already made. The state assessment is not optional.

**Absorbing existing material without running ingestion.** When a new project has existing material, reading it and proceeding directly loses the characterization, conflict check, and routing that ingestion provides. Route through `worldbuilder-ingestion` even when the material seems simple — the index it produces becomes the reference point for everything downstream.

**Starting character work before the household structure is finalized.** Characters written without household context have no stakes and no web of inter-character meaning.

**Writing all characters sequentially in one session.** Context degrades across 24 characters in sequence. Parallelize aggressively once the roster exists.

**Skipping the relationship sync pass.** Characters written independently will have asymmetric relationship entries. The sync pass is the only mechanism that catches this.

**Papering over open questions.** An unresolved decision in the Seed phase propagates inconsistency through every later phase. Flag early, ask the user, do not guess.

**Treating phase gates as optional.** The dependency structure is real. Lorebook written before foundation decisions are finalized will contradict them. Calendar events written before the community's character is established will feel generic.

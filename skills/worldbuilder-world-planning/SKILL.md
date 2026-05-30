---
name: worldbuilder-world-planning
description: Use at the start of every worldbuilding session — new project or returning one. Assesses current state, determines where you are in the pipeline, and routes to the right skill. Also use when entering a new phase, when unsure what to work on next, or when the project feels stuck or disorganized.
---

# World Planning

## Overview

This skill is the single entry point for all worldbuilding sessions. Every session starts here. It reads project state, determines the current phase, proposes next steps, and hands off to the appropriate skill.

**Hard gate principle:** Phase completion is a prerequisite, not a suggestion. No character work before the household structure in `seed.md` is complete. No export work before character notes are complete. No lorebook or calendar before the foundation decisions are finalized. Each phase produces the context the next phase depends on.

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
Phase 1  (Seed)             Done    → seed.md
Phase 2a (Lorebook notes)   Done    → notes/
Phase 2b (Calendar/Events)  Done    → notes/
Phase 2c (Story Direction)  Done    → notes/
Phase 2d (Cast planning)    Done    → worldbuilding-plan.md
Phase 2e (Character notes)  6/24    → notes/
Phase 3  (Export)           0/24    → worldbuilder-ainime-export

Next: Continue character notes. Suggested: dispatch 4 in parallel.
```

---

## Three-Phase Framework

### Phases and skills

| Phase | Group | Skill | Deliverable |
|---|---|---|---|
| 0. Ingestion | Pre-Seed | `worldbuilder-ingestion` | Ingestion index + extracted content |
| 1. Seed | Seed | `worldbuilder-world-foundation` | `seed.md` |
| 2a. Lorebook notes | Wide | `worldbuilder-lorebook` | `notes/` |
| 2b. Calendar/Events | Wide | `worldbuilder-calendar` | `notes/` |
| 2c. Story Direction | Wide | `worldbuilder-story-direction` | `notes/` |
| 2d. Cast planning | Wide | (this skill — see below) | Cast plan in `worldbuilding-plan.md` |
| 2e. Character notes | Wide | `worldbuilder-character-blueprint` | `notes/` |
| 3. Export | Export | `worldbuilder-ainime-export` | Platform-specific outputs |
| 3b. Review | Export | — | Sign-off across all documents |

### Dependency structure

```
[Ingestion — optional, when existing material exists]
    └─►
Seed (seed.md)
    └─► Cast planning
            ├─► Lorebook notes  ─┐
            ├─► Calendar/Events  ├─► Character notes ─► Export ─► Review
            └─► Story direction  ─┘
```

The Seed phase is strictly sequential with everything that follows. Cast planning must complete before character notes begin. Lorebook notes, Calendar/Events, and Story Direction are independent of each other and can proceed in parallel once cast planning is done. Individual character notes are independent of each other once the cast plan exists.

### Phase 2d: Cast planning

No dedicated skill exists for cast planning. Build it here, with user input, before dispatching to `worldbuilder-character-blueprint`.

The user seeds the cast — names they already have, roles they know they want, characters with personal significance. From each seed, branch through relationships: who is in their household, who do they conflict with, who do they depend on? Fill structural gaps (unfilled archetype slots, households without characters) with proposals for the user to accept, modify, or reject. Never assign a character to a slot without the user's knowledge.

Record the confirmed cast in `worldbuilding-plan.md`. This is a planning document, not the character notes themselves — each character note is created by `worldbuilder-character-blueprint` and carries the authoritative information in its frontmatter and preamble.

Cast plan entry format (for `worldbuilding-plan.md`):

```
**[Name]** — [Household] | [Type: Major/Supporting] | [Species/age]
Role: [one or two phrases]
Archetype: [slot from cast architecture]
Key relationships: [named, one per line]
Intimate Dynamics: Yes  ← only if applicable; omit line if not
Summary: [2–3 sentences of behavioral character, not physical description]
```

Coverage check before declaring cast planning complete:
- All 6 romance archetype slots filled across gender presentations
- Non-romance archetypes placed: authority figure, mentor/elder, elderly anchor, child or teen, outcast/philosopher, practitioner, the one who left (or didn't), the secret-carrier
- 2–3 characters with meaningful negative-track content
- Every household has at least one character assigned
- Default count: 8 main / 16 side (range: 6–10 main, 6–20 side)
- Anti-redundancy check: no two romance candidates filling the same slot with the same execution

---

## Early Project Decisions

Ask these before beginning Phase 1. Record answers in `worldbuilding-plan.md`.

**Intimate dynamics scope:** Does this project include explicit intimate content? Options: all romance-eligible characters, a specific subset, or none. If the answer is "some" or "all," identify which characters and flag them in the cast plan with an `Intimate Dynamics: Yes` marker. This decision is made once and recorded — not revisited character by character. When creating character notes, check the cast plan flag; if absent, skip intimate dynamics without further consideration.

---

## Phase Completion Criteria

Use these checklists at each phase gate. If any item is unresolved, surface it to the user before proceeding.

### Seed phase complete

`seed.md` must contain all of the following:

- [ ] All six foundational questions answered (setting wound, community character, player connection, hidden layer, era, household clusters)
- [ ] Setting Summary written — time, place, society, tone; concrete and specific
- [ ] Genre & Tone written — primary genre, tonal range, content notes
- [ ] Inspirations and Tonal Inspirations listed with specifics
- [ ] Key Tropes & Themes: 8–12 entries
- [ ] Community written — social and emotional identity, not physical
- [ ] World Introduction written — pre-game player text
- [ ] Opening Situation written — evocative, not scripted
- [ ] Story Direction stub written (can be brief; expands after cast is established)
- [ ] Locations list: 10–14 named locations, one sentence each
- [ ] Art style reference written
- [ ] Musical theme written
- [ ] All 6–8 household clusters written with: function, internal tension, inter-household connections, trajectory, narrative hook
- [ ] No individual character names assigned yet — household types and counts only
- [ ] Every household has at least one named connection to another household

### Lorebook notes complete

- [ ] All three layers present (surface, mid, deep)
- [ ] Concept notes written for all major locations
- [ ] Background NPC guidelines concept note written
- [ ] `layer` frontmatter set on all concept notes

### Calendar/Events complete

- [ ] Era defined
- [ ] Weather pool written (6–8 types with narrative weight)
- [ ] All 4 major festivals written as event notes with full atmospheric descriptions
- [ ] All 4–5 minor observances written as event notes
- [ ] First-year one-time events written if needed

### Story Direction complete

- [ ] Opening arc written — evocative, not scripted
- [ ] All ongoing story direction sections present: author framing, romance pacing, dark themes, hidden layer handling, seasonal tone, pacing, year 2+ NPC relationships

### Cast planning complete

- [ ] All coverage check items from Phase 2d above verified
- [ ] Every character has: household, type, species/age, role, archetype, key relationships, summary
- [ ] Intimate dynamics flags set where applicable

### Character notes complete (per character)

- [ ] All three foundation dimensions filled out (body, environment, soul)
- [ ] 3–5 behavioral descriptions in When/Behavior/Because form
- [ ] Contradiction and irrational behavior identified with emotional root
- [ ] Relationship Behavior written covering default register, warmth, and distance
- [ ] Storylines written; introduction note created or flagged as pending
- [ ] Frontmatter complete with wikilinks on factions and archetype

### Export phase complete (per character)

See `worldbuilder-ainime-export` for export completion criteria. Export is the only phase that writes ainime field names.

### Review complete (full cast)

- [ ] Relationship synchronization verified: if A names B, B's note names A
- [ ] Every household's internal tension represented in at least one character note
- [ ] All romance candidates have romance arc guidance
- [ ] No generic relationship behavior language (the engine handles warmth and distance automatically)
- [ ] Dark arc characters have hope-tending language and witness-not-savior framing

---

## Parallel Execution

### What can run in parallel

**Phases 2a, 2b, 2c** (Lorebook notes, Calendar/Events, Story Direction) — fully independent once cast planning is complete. Dispatch one agent per deliverable.

**Phase 2e, Character notes** — once the cast plan exists, every character is independent. Dispatch in groups of 3–4 per agent.

**Phase 3, Export** — once a character note is complete, that character's export is independent. Parallelize freely.

### What must run sequentially

**Phase 1 (Seed)** before everything else.

**Phase 2d (Cast planning)** before any character notes begin.

**Relationship Sync Pass** — run at two points: (1) after each household group of character notes, while the characters are fresh in context; (2) a final pass after all notes are complete. The note-level pass catches inconsistencies before they carry into export.

### Constructing agent prompts for parallel character work

Each agent needs, stated explicitly:

1. The cast plan — full document or at minimum the relevant household section
2. The target character's complete cast plan entry
3. Which skills to invoke
4. Where to save the deliverable
5. An explicit constraint: do not modify other character files or the cast plan

Example structure:
> "Write the character note for [Name] using `worldbuilder-character-blueprint`. Cast plan entry for [Name]: [paste]. Household members for context: [paste relevant entries]. Save to `notes/firstname-lastname.md`. Do not modify the cast plan or any other character's file."

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
| 1. Seed | Seed | Done / In Progress / Not Started | seed.md | |
| 2a. Lorebook notes | Wide | ... | notes/ | |
| 2b. Calendar/Events | Wide | ... | notes/ | |
| 2c. Story Direction | Wide | ... | notes/ | |
| 2d. Cast planning | Wide | ... | worldbuilding-plan.md | |
| 2e. Character notes | Wide | ... | notes/ | X of Y complete |
| 3. Export | Export | ... | worldbuilder-ainime-export | X of Y complete |
| 3b. Review | Export | ... | — | |

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

**Writing all characters sequentially in one session.** Context degrades across 24 characters in sequence. Parallelize aggressively once the cast plan exists.

**Skipping the relationship sync pass.** Characters written independently will have asymmetric relationship entries. The sync pass is the only mechanism that catches this.

**Papering over open questions.** An unresolved decision in the Seed phase propagates inconsistency through every later phase. Flag early, ask the user, do not guess.

**Treating phase gates as optional.** The dependency structure is real. Lorebook written before foundation decisions are finalized will contradict them. Calendar events written before the community's character is established will feel generic.

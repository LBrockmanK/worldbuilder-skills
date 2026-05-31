---
name: worldbuilder-world-planning
description: Use at the start of every worldbuilding session — new project or returning one. Assesses current state, determines where you are in the pipeline, and routes to the right skill. Also use when entering a new phase, when unsure what to work on next, or when the project feels stuck or disorganized.
---

# World Planning

## Overview

This skill is the single entry point for all worldbuilding sessions. Every session starts here. It reads project state, determines the current phase, proposes next steps, and hands off to the appropriate skill.

**Hard gate principle:** Phase completion is a prerequisite, not a suggestion. No character work before the household structure in `seed.md` is complete. No export work before character notes are complete. No Wide-phase content before the foundation decisions are finalized. Each phase produces the context the next phase depends on.

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
Phase 1b (Direction doc)    Done    → direction.md
Phase 2a (Concept notes)    Done    → notes/
Phase 2b (Story notes)      Done    → notes/
Phase 2c (Location notes)   Done    → notes/
Phase 2d (Faction notes)    Done    → notes/
Phase 2e (Cast planning)    Done    → worldbuilding-plan.md
Phase 2f (Character notes)  6/24    → notes/
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
| 1b. Direction document | Seed | (this skill + `worldbuilder-story`) | `direction.md` |
| 2a. Concept notes | Wide | `worldbuilder-concept` | `notes/` |
| 2b. Story notes | Wide | `worldbuilder-story` | `notes/` |
| 2c. Location notes | Wide | `worldbuilder-location` | `notes/` |
| 2d. Faction notes | Wide | `worldbuilder-faction` | `notes/` |
| 2e. Cast planning | Wide | (this skill — see below) | Cast plan in `worldbuilding-plan.md` |
| 2f. Character notes | Wide | `worldbuilder-character` | `notes/` |
| 3. Export | Export | `worldbuilder-ainime-export` | Platform-specific outputs |
| 3b. Review | Export | — | Sign-off across all documents |

### Dependency structure

```
[Ingestion — optional, when existing material exists]
    └─►
Seed (seed.md)
    ├─► Concept notes (2a)  ─┐
    ├─► Story notes (2b)     │
    ├─► Location notes (2c)  ├─► Character notes (2f) ─► Export ─► Review
    ├─► Faction notes (2d)  ─┘         ▲
    └─► Cast planning (2e) ─────────────┘ (required gate)
```

Phases 2a–2e are independent of each other — all branch from the seed. The only hard dependency is that character notes (2f) require cast planning (2e) to be complete. Completing location and faction notes before character notes is recommended, not required.

The Seed phase is strictly sequential with everything that follows. Character notes require cast planning to be complete. All other Wide-phase work (2a–2e) is independent — individual phases can start immediately after the seed with no waiting on each other. Individual character notes are independent of each other once the cast plan exists.

### Phase 1b: Direction document

After seed.md is confirmed complete, produce `direction.md` before any Wide-phase work begins. This is the story engine's primary guard rail — it shapes every scene generated for this world.

Work through each section using `worldbuilder-story` for section templates and content guidance. Write for the world established in seed.md:

- **Author framing** — How the engine should approach characters and narration
- **Romance pacing** — Slow and earned; the primary guard against the engine's default escalation
- **Dark themes** — Permission and handling guidance
- **Hidden layer** (if applicable) — How the supernatural or concealed layer should surface
- **Seasonal tone** — Brief guidance on each period's emotional register
- **Pacing and scene structure** — Quiet scenes are valid; escalation ceiling; day-segment rhythms

direction.md frontmatter:
```yaml
type: project
status: draft | complete
last_updated: YYYY-MM-DD HH:mm
```

direction.md can be refined as the cast and story develop. The requirement before Wide-phase work is that all sections exist — a brief but complete document is better than a detailed stub.

---

### Phases 2c–2d: Location and faction notes

Once seed.md is complete, dispatch `worldbuilder-location` for each named location and `worldbuilder-faction` for each household cluster. These phases run in parallel with concept notes and story notes — no orchestration needed here; the blueprints are self-contained. Count of notes matches the seed's location list and household cluster list.

Location and faction notes provide context that character notes build on. Run them before character notes where possible.

---

### Phase 2e: Cast planning

No dedicated skill exists for cast planning. Build it here, with user input, before dispatching to `worldbuilder-character`.

The user seeds the cast — names they already have, roles they know they want, characters with personal significance. From each seed, branch through relationships: who is in their household, who do they conflict with, who do they depend on? Fill structural gaps (unfilled archetype slots, households without characters) with proposals for the user to accept, modify, or reject. Never assign a character to a slot without the user's knowledge.

Record the confirmed cast in `worldbuilding-plan.md`. This is a planning document, not the character notes themselves — each character note is created by `worldbuilder-character` and carries the authoritative information in its frontmatter and preamble.

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
- [ ] Locations list: 10–14 named locations, one sentence each
- [ ] Art style reference written
- [ ] Musical theme written
- [ ] All 6–8 household clusters written with: function, internal tension, inter-household connections, trajectory, narrative hook
- [ ] No individual character names assigned yet — household types and counts only
- [ ] Every household has at least one named connection to another household

### Direction document complete

- [ ] `direction.md` exists with `type: project` frontmatter
- [ ] All required sections present: author framing, romance pacing, dark themes, hidden layer handling, seasonal tone, pacing and scene structure
- [ ] Opening arc sketched at a broad level

### Concept notes complete

- [ ] All three layers present (surface, mid, deep)
- [ ] Background NPC guidelines concept note written
- [ ] `layer` frontmatter set on all concept notes

### Story notes complete

- [ ] `notes/direction.md` written with all required sections: author framing, romance pacing, dark themes, hidden layer handling, seasonal tone, pacing, year 2+ NPC relationships
- [ ] Opening arc note written — evocative, not scripted
- [ ] Key intention notes written for major story possibilities

### Location notes complete

- [ ] All named locations from seed.md have a note in `notes/`
- [ ] Each note passes the `worldbuilder-location` self-check
- [ ] Primary characters linked via `[[wikilinks]]` in frontmatter

### Faction notes complete

- [ ] All household clusters from seed.md have a faction note in `notes/`
- [ ] Each note passes the `worldbuilder-faction` self-check
- [ ] Member characters linked via `[[wikilinks]]` in frontmatter

### Cast planning complete

- [ ] All coverage check items from Phase 2e above verified
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

**Phases 2a–2e** — all Wide-phase work branches from the seed and is independent of every other Wide phase. Dispatch one agent per deliverable.

**Phase 2f, Character notes** — once the cast plan exists, every character is independent. Dispatch in groups of 3–4 per agent.

**Phase 3, Export** — once a character note is complete, that character's export is independent. Parallelize freely.

### What must run sequentially

**Phase 1 (Seed)** before everything else.

**Phase 2e (Cast planning)** before any character notes begin.

**Relationship Sync Pass** — run at two points: (1) after each household group of character notes, while the characters are fresh in context; (2) a final pass after all notes are complete. The note-level pass catches inconsistencies before they carry into export.

### Constructing agent prompts for parallel character work

Each agent needs, stated explicitly:

1. The cast plan — full document or at minimum the relevant household section
2. The target character's complete cast plan entry
3. Which skills to invoke
4. Where to save the deliverable
5. An explicit constraint: do not modify other character files or the cast plan

Example structure:
> "Write the character note for [Name] using `worldbuilder-character`. Cast plan entry for [Name]: [paste]. Household members for context: [paste relevant entries]. Save to `notes/firstname-lastname.md`. Do not modify the cast plan or any other character's file."

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
| 1b. Direction document | Seed | Done / In Progress / Not Started | direction.md | |
| 2a. Concept notes | Wide | ... | notes/ | |
| 2b. Story notes | Wide | ... | notes/ | |
| 2c. Location notes | Wide | ... | notes/ | X of Y complete |
| 2d. Faction notes | Wide | ... | notes/ | X of Y complete |
| 2e. Cast planning | Wide | ... | worldbuilding-plan.md | |
| 2f. Character notes | Wide | ... | notes/ | X of Y complete |
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

**Treating phase gates as optional.** The dependency structure is real. Concept notes and story notes written before the seed is finalized will contradict it — Wide-phase content depends on the foundation being locked.

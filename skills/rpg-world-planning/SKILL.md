---
name: rpg-world-planning
description: Use at the start of a new worldbuilding project, when entering a new phase, or when unsure what to work on next. Scopes the project, establishes phase dependencies, produces a worldbuilding-plan.md, and guides execution — including parallel agent dispatch for character work. Also use for mid-project phase audits or when the project feels stuck or disorganized.
---

# RPG World Planning

## Overview

Worldbuilding for LLM-powered games is a large multi-phase project with hard dependencies between phases. This skill governs the full pipeline: assessing what exists, decomposing into phases, producing a plan document, guiding phase gates, and identifying where parallel execution is safe.

**Hard gate principle:** Phase completion is a prerequisite, not a suggestion. No character work before household structure is complete. No household design before foundation decisions are finalized. Each phase produces the context the next phase depends on.

**Feedback principle:** At any decision point — a design choice, missing information, options to weigh — stop and ask the user. Do not assume or fill in the gap. A project derailed by a wrong assumption costs more to correct than the time spent asking. When in doubt, surface the question.

---

## Pipeline Overview

### Dependency structure

```
Foundation
    └─► Households
            ├─► Lorebook     ─┐
            ├─► Calendar      ├─► Character Roster ─► Blueprints ─► Cards ─► Review
            └─► Story Dir.   ─┘
```

Foundation and Households are strictly sequential. Lorebook, Calendar, and Story Direction are independent of each other and can proceed in parallel once Households are complete. Individual characters are independent of each other once the Roster exists.

### Phases and skills

| Phase | Skill | Deliverable |
|---|---|---|
| 1. Foundation | `rpg-world-foundation` | `foundational-decisions.md` |
| 2. Households | `rpg-world-foundation` | `households.md` |
| 3a. Lorebook | `rpg-lorebook` | `lorebook.md` |
| 3b. Calendar | `rpg-calendar` | `calendar.md` |
| 3c. Story Direction | `rpg-story-direction` | `story.md` |
| 4. Character Roster | `rpg-character-relationships` | `characters/roster.md` |
| 5. Character Blueprints | `rpg-character-blueprint` + `rpg-character-relationships` | `characters/blueprints/*.md` |
| 6. Character Cards | `rpg-character-blueprint` | `characters/cards/*.md` |
| 7. Review | — | Sign-off across all documents |

---

## Early Project Decisions

Ask these before beginning Phase 1. They shape the rest of the pipeline.

**Intimate dynamics scope:** Does this project include explicit intimate content? Options: all romance-eligible characters, a specific subset, or none. Record the decision in the plan document. If the answer is "some" or "all," identify which characters and flag them in the roster with an `Intimate Dynamics: Yes` marker. If the answer is "none," the `rpg-intimate-dynamics` skill is not invoked at any point in the pipeline.

This decision is made once and recorded — it is not revisited character by character. During blueprint work, the agent checks the roster flag; if it is absent, intimate dynamics is skipped without further consideration.

---

## Phase Completion Criteria

Use these as checklists at each phase gate. If any item is unresolved, surface it to the user before proceeding.

### Foundation complete
- [ ] All six foundational questions answered in `foundational-decisions.md`
- [ ] No remaining open questions flagged
- [ ] Setting name and character established
- [ ] Hidden layer origin decided

### Households complete
- [ ] All 6–8 household clusters written with: function, internal tension, inter-household connections, trajectory, narrative hook
- [ ] No individual character names assigned yet — household types and counts only
- [ ] Every household has at least one named connection to another household
- [ ] Cast architecture reviewed: six romance archetype slots covered, non-romance archetypes accounted for
- [ ] Anti-redundancy check: no two romance candidates filling the same archetype slot without distinguishing execution

### Lorebook complete
- [ ] All three layers present (surface, mid, deep) with appropriate date gates
- [ ] Location entries written for all major locations
- [ ] Background NPC guidelines entry written, active from day 1
- [ ] All keywords tested mentally: cover realistic phrasings, avoid partial-match traps

### Calendar complete
- [ ] Era defined
- [ ] Weather pool written (6–8 types with narrative weight noted)
- [ ] Daily Planner Directive written covering all five structural elements
- [ ] All 4 major festivals written with full atmospheric descriptions
- [ ] All 4–5 minor observances written
- [ ] First-year one-time events written if needed

### Story Direction complete
- [ ] Opening arc written — evocative, not scripted
- [ ] All ongoing story direction sections present: author framing, romance pacing, dark themes, hidden layer handling, seasonal tone, pacing, year 2+ NPC relationships

### Character Roster complete
- [ ] All characters assigned to households with name, type, species, age, available day, role, archetype, bullet summary
- [ ] Relationship web started — primary relationships listed per character
- [ ] Archetype coverage, sex balance, and count summary verified at bottom of roster

### Character Blueprints complete (per character)
- [ ] All three foundation dimensions filled out (body, environment, soul)
- [ ] 3–5 behavioral descriptions in When/Behavior/Because form
- [ ] Contradiction and irrational behavior identified with emotional root
- [ ] Influence thresholds drafted for all six bands
- [ ] Introduction and future storylines written

### Character Cards complete (per character)
- [ ] All prose assembled per card structure
- [ ] All six influence threshold bands present with 2–4 examples each
- [ ] Token count in target range (~900 supporting, ~1500 major)

### Review complete (full cast)
- [ ] Relationship synchronization verified: if A names B, B's card names A
- [ ] Every household's internal tension represented in at least one character card
- [ ] All romance candidates have romance arc guidance
- [ ] No generic threshold language (engine handles warmth/distance automatically)
- [ ] Dark arc characters have hope-tending language and "witness not savior" framing

---

## Parallel Execution

### What can run in parallel

**Phases 3a, 3b, 3c** (Lorebook, Calendar, Story Direction) — fully independent once Phase 2 is done. Dispatch one agent per deliverable.

**Phase 5, Character Blueprints** — once the roster exists, every character is independent of every other. Dispatch in groups of 3–4 per agent.

**Phase 6, Character Cards** — once a blueprint exists for a character, that card is independent. Parallelize freely.

### What must run sequentially

**Phases 1 and 2** (Foundation then Households) — each decision constrains the next.

**Phase 4, Character Roster** — the shared reference for all subsequent character work. Must be complete and reviewed before any blueprints begin.

**Relationship Sync Pass** — run at two points: (1) after each household/batch of blueprints, while characters are fresh in context; (2) a final pass after all cards are complete. The blueprint-level pass catches inconsistencies before they carry into card prose. The card-level pass catches anything that drifted further during card writing.

### Constructing agent prompts for parallel character work

Each agent needs, stated explicitly:

1. The roster — full document or at minimum the relevant household section
2. The target character's complete roster entry
3. Which skills to invoke
4. Where to save the deliverable
5. An explicit constraint: do not modify other character files or the roster

Example structure:
> "Write the blueprint for [Name] using `rpg-character-blueprint` and `rpg-character-relationships`. Roster entry for [Name]: [paste]. Household members for context: [paste relevant entries]. Save to `characters/blueprints/firstname-lastname.md`. Do not modify the roster or any other character's file."

---

## Plan Document

Produce or update `worldbuilding-plan.md` at the project root at the start of a project and at each phase transition. If the user specifies a different location, use that.

```markdown
# [World Name] — Worldbuilding Plan

**Setting summary:** [One sentence]
**Current phase:** [Phase name and number]
**Characters:** [Count and completion status]
**Last updated:** [Date]

---

## Phase Status

| Phase | Status | Deliverable | Notes |
|---|---|---|---|
| 1. Foundation | Done / In Progress / Not Started | foundational-decisions.md | |
| 2. Households | ... | households.md | |
| 3a. Lorebook | ... | lorebook.md | |
| 3b. Calendar | ... | calendar.md | |
| 3c. Story Direction | ... | story.md | |
| 4. Roster | ... | characters/roster.md | |
| 5. Blueprints | ... | characters/blueprints/ | X of Y complete |
| 6. Cards | ... | characters/cards/ | X of Y complete |
| 7. Review | ... | — | |

---

## Current Phase Tasks

- [ ] [Task with named deliverable]

---

## Parallel Work Opportunities

[What can be dispatched independently right now without waiting for other work]

---

## Open Questions

[Unresolved decisions that need to be addressed before proceeding]
```

---

## Self-Review at Phase Gates

Before declaring a phase complete:

1. **Completeness** — Does every deliverable have all required sections? Run the checklist above.
2. **Internal consistency** — Do characters reference households that exist? Do households reference inter-connections that have been established?
3. **Open question scan** — Any placeholders, TODOs, or flagged decisions still outstanding? Surface them to the user — do not paper over them.
4. **Forward dependency** — Does the next phase have everything it needs from this one?

If any check reveals an unresolved issue, ask the user before marking the phase done.

---

## Common Failure Modes

**Starting character work before households are designed.** Characters written without household context have no stakes and no web of inter-character meaning. The household structure is what gives characters significance beyond their relationship with the player.

**Writing all characters sequentially in one session.** Context degrades and quality declines across 24 characters in sequence. Parallelize aggressively once the roster exists.

**Skipping the relationship sync pass.** Characters written independently will have asymmetric relationship entries. The sync pass is the only mechanism that catches this.

**Papering over open questions.** An unresolved decision in Foundation propagates inconsistency through every later phase. Flag early, ask the user, do not guess.

**Treating phase gates as optional.** The dependency structure is real. Lorebook written before Foundation decisions are finalized will contradict them. Calendar events written before the town's character is established will feel generic.

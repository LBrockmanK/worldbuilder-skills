---
type: plan
title: Character Blueprint Rework Implementation Plan
description: Implementation plan for restructuring the worldbuilder-character skill so every note section produces behavioral descriptions.
tags: [complete]
date: 2026-06-03
timestamp: 2026-06-03T17:10
resources: []
---
# Character Blueprint Rework Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Restructure the worldbuilder-character skill so every note section produces behavioral descriptions, eliminating redundancy between Soul, Behavioral Descriptions, and Relationship Behavior.

**Architecture:** Five skill files are touched. The character note template is updated to match the new section structure. `framework.md` is fully rewritten (Background/Body/Soul replace Foundation/Behavioral Descriptions). `relationships.md` gets a targeted format update. `intimate.md` is rewritten to behavioral format only. `SKILL.md` is restructured to add the Q&A session flow, remove Relationship Behavior, and update all cross-references and self-check items.

**Spec:** `docs/superpowers/specs/2026-06-03-blueprint-rework-design.md`

---

## File Map

| File | Change |
|---|---|
| `skills/worldbuilder-setup/worldvault/_templates/character.md` | Full rewrite — new section structure |
| `skills/worldbuilder-character/framework.md` | Full rewrite — Background/Body/Soul replaces Foundation/Behavioral Descriptions |
| `skills/worldbuilder-character/relationships.md` | Targeted — entry format updated to bullet list with bold prefix |
| `skills/worldbuilder-character/intimate.md` | Full rewrite — behavioral format only, exploration questions removed |
| `skills/worldbuilder-character/SKILL.md` | Major rewrite — session flow added, Relationship Behavior removed, self-check updated |

---

## Task 1: Update character note template

**Files:**
- Modify: `skills/worldbuilder-setup/worldvault/_templates/character.md`

- [ ] **Step 1: Replace the template with the new structure**

Overwrite `skills/worldbuilder-setup/worldvault/_templates/character.md` with:

```markdown
---
type: character
status: draft
aliases: []
last_updated: YYYY-MM-DD HH:mm
factions: []
brief: ""
---

> For future agents: this is a character note. The filename is the character's name. Use `worldbuilder-character` to build it out.

## Design Notes

### Session Notes

_Q&A capture: what the user said they wanted this character to be. Raw intent, bullet points._

-

### Builder Context

_Narrative function, external references, design decisions, open questions. Bullet points. Leave blank if nothing to capture — do not pad._

-

## Background

_Where this character comes from. Declarative fact pairs: [Fact] → [what it made true]. No behavioral content._

-

## Body

_Physical behavioral descriptions. One entry per bullet._

-

## Soul

_Psychological and social behavioral descriptions. One entry per bullet._

-

## Relationships

_Named relationship dynamics. One bullet per relationship: **Name — Archetype(s):** [behavioral description]_

-
```

- [ ] **Step 2: Verify**

Read back `skills/worldbuilder-setup/worldvault/_templates/character.md`. Confirm:
- `## Design Notes` with `### Session Notes` and `### Builder Context` subheadings
- `## Background`, `## Body`, `## Soul`, `## Relationships` present
- `## Foundation`, `## Behavioral Descriptions`, `## Relationship Behavior` absent
- `## Intimate Dynamics` absent (only added to notes when flagged — not a default template section)

- [ ] **Step 3: Commit**

```
git add skills/worldbuilder-setup/worldvault/_templates/character.md
git commit -m "feat: update character note template to new section structure (#13)"
```

---

## Task 2: Rewrite framework.md

**Files:**
- Modify: `skills/worldbuilder-character/framework.md`

- [ ] **Step 1: Replace framework.md with new Background/Body/Soul content**

Overwrite `skills/worldbuilder-character/framework.md` with:

```markdown
# Character Framework — Background, Body & Soul

*Sub-file for `worldbuilder-character`. Read this when working on the Background, Body, and Soul sections.*

---

## Background

Where this character comes from. This section is different in kind from the sections that follow — it is causal context, not behavioral output. Read it to understand why behavioral descriptions exist; do not restate its content in Body or Soul.

**Format:** Bullet list. One entry per fact pair:

```
- [Formative fact] → [what it made true]
```

No prose, no elaboration beyond the pair. No behavioral framing — if the fact implies a behavioral pattern, that pattern belongs in Body or Soul as a behavioral description.

**What to cover:**
- Origin: where they grew up, what class and culture shaped them, what was valued and looked down on
- Formative events: key experiences and turning points that changed their trajectory
- Current situation: where they are now and how they feel about it (content, stuck, restless)

---

## Body

Physical behavioral descriptions — how this character's physicality shapes behavior in the world.

**Format:** Bullet list. One behavioral description per bullet, written as a prose sentence. The When/Behavior/Because structure is a writing guide — do not label the parts in the output. The sentence embeds all three elements naturally.

**Coverage prompts** (not all require an entry — only those that produce distinctive behavior):
- Appearance and how it draws or deflects attention
- Physical self-consciousness or pride and what it produces in behavior
- Embodied habits: how they carry themselves, what they do with their hands, how they occupy space

Thin Body sections are acceptable when nothing about a character's physicality is distinctive. Do not force entries.

*Example:*
```
- When she enters a room she doesn't know, she finds a wall or corner first — she grew up visible in ways she didn't choose, and learned to make herself an observer before becoming a subject.
```

---

## Soul

Psychological and general social behavioral descriptions. Two coverage areas written together as a single bullet list — no subheadings.

**Format:** Bullet list. One behavioral description per bullet, written as a prose sentence.

### The Formula

> When [trigger], they [behavior], because [underlying reason].

The formula is a construction guide. Write prose sentences that embed all three elements naturally — do not label the parts.

### Why behavioral descriptions outperform trait labels

| Trait | Label (avoid) | Behavioral (use) |
|---|---|---|
| Confident | "She is confident." | "When challenged, she responds with certainty, treating doubt as a personal insult rather than a reasonable position." |
| Stubborn | "He is stubborn." | "When someone pushes back, he doubles down. Changing his mind feels like losing, and he does not lose." |
| Kind | "They are kind." | "When someone is struggling, they drop everything to help — partly because they care, partly because being needed is the only time they feel valuable." |
| Nervous | "She is anxious." | "In new social situations she over-prepares what to say, then abandons all of it and talks too fast. She apologizes for things that are not her fault." |

Labels give the LLM one word to repeat. Behavioral descriptions force it to generate language that fits the behavior — dramatically more varied output.

### Coverage

**Psychological patterns (3–5 entries minimum):**
- Emotional triggers and responses
- Core drives in action — what does wanting to be respected actually look like when they're in a room?
- Irrational behavior with its emotional root (required — see note below)
- Self-image gap expressed as behavioral description
- Contradiction between presented self and actual self (required — one entry must name this)

> **Why the irrational behavior entry matters most:** LLMs default to writing rational, helpful-assistant-style characters. An irrational behavior with a clear emotional root forces the LLM to generate responses that feel human rather than algorithmic. It is the single most effective thing in this framework.

**General social register (2–3 entries minimum):**
- Default mode with strangers — what a first encounter with this character feels like
- What warmth looks like when it appears — specific behavior, not "they become warm"
- What distance or friction looks like — specific behavior, not "they become cold"
- Relationship-type variation if it exists (with authority figures vs. peers vs. someone they're protecting)

If the character has a distinctive speech pattern, include one entry describing it concretely.

### Contradictions

The most interesting characters contain contradictions. A character with no friction between what they want and what they do gives the LLM nothing to work with. The contradiction must appear as a behavioral description in the Soul bullet list — not as a standalone note.

- What do they present vs. what is actually true?
- What would make them change — what experience, person, or realization could break the pattern?

### The Because clause

The Because clause carries the psychological root. Draw it from the Q&A session capture in Design Notes — do not invent psychology the user has not provided. If no session note speaks to a specific behavior's root, ask before writing.
```

- [ ] **Step 2: Verify**

Read back `skills/worldbuilder-character/framework.md`. Confirm:
- `## Background`, `## Body`, `## Soul` headings present
- `## Foundation`, `## Behavioral Descriptions`, `## Environment` headings absent
- Soul section contains the formula, comparison table, coverage guide with psychological + social register, contradiction note, and Because clause note
- Background section describes declarative fact pairs format
- Body section describes behavioral bullet format with coverage prompts

- [ ] **Step 3: Commit**

```
git add skills/worldbuilder-character/framework.md
git commit -m "feat: rewrite framework.md — Background/Body/Soul replaces Foundation/Behavioral Descriptions (#13)"
```

---

## Task 3: Update relationships.md entry format

**Files:**
- Modify: `skills/worldbuilder-character/relationships.md`

The archetype guidance, coverage requirements, generativity hierarchy, perspective-focus rules, and cross-character capture guidance are all unchanged. Only the entry format is updated.

- [ ] **Step 1: Update the Writing Relationship Entries format line**

In `skills/worldbuilder-character/relationships.md`, find the Writing Relationship Entries section and replace the Format line:

Old:
```
**Format:** Archetype label(s) and name as a table row or bold header; behavioral description in the entry.
```

New:
```
**Format:** Bullet list. One entry per relationship. Bold `**Name — Archetype(s):**` prefix inline on the bullet, followed by behavioral description as prose sentence(s).

*Example:*
```
- **Mira — Kin:** When Mira dismisses her ideas in front of others, she doesn't argue — she brings the idea back later, one-on-one, where Mira has room to change her mind without losing face.
```
```

- [ ] **Step 2: Update the per-entry self-review section header**

Find:

```
### Per-entry self-review: internal state check
```

This section title is fine — no change needed. Verify the worked example still makes sense with the new bullet format. The example uses "Sophie pushes back on Vesper's decisions" — it is about perspective focus, not format, and remains valid.

- [ ] **Step 3: Verify**

Read back the Writing Relationship Entries section. Confirm:
- Old "table row or bold header" format description is gone
- New bullet format with `**Name — Archetype(s):**` prefix is described
- Example bullet is present
- The rest of the section (Fiske model, entry length guidance) is unchanged

- [ ] **Step 4: Commit**

```
git add skills/worldbuilder-character/relationships.md
git commit -m "feat: update relationships entry format to bullet list with bold prefix (#13)"
```

---

## Task 4: Rewrite intimate.md

**Files:**
- Modify: `skills/worldbuilder-character/intimate.md`

Exploration question sections are removed. The section becomes behavioral descriptions only, with the same format as Soul.

- [ ] **Step 1: Replace intimate.md with new behavioral-only content**

Overwrite `skills/worldbuilder-character/intimate.md` with:

```markdown
# Intimate Dynamics (Optional Section)

*Sub-file for `worldbuilder-character`. Only read this if the character's roster entry is flagged `Intimate Dynamics: Yes`. If the flag is absent, skip this file entirely.*

---

## Overview

Intimate dynamics follow the same principles as all other sections: behavioral descriptions, friction, and causality produce better results than labels. "Dominant" gives the LLM three stock phrases on loop. A behavioral description of how and why the character takes control — and when they don't — produces dynamic, varied interactions.

Exploration questions (what the dynamic gives them emotionally, how it connects to their history, what would go wrong) belong in the Q&A session and Design Notes, not in this section.

The decision about whether to include intimate dynamics is made once at project planning, recorded in the project plan, and reflected in the roster. It is not revisited character by character.

---

## Format

Bullet list. One behavioral description per bullet, written as a prose sentence. Same format as Soul — When/Behavior/Because embedded naturally, no visible labels.

---

## Coverage

Write entries covering:

- **Attraction expression:** How they show interest — direct or indirect, obvious or subtle, testing or charging forward
- **Hesitation and limits:** What makes them slow down, pull back, or hold a line — this is where tension and pacing come from
- **Specific dynamic (if present):** If the character is built around a specific dynamic, what is its behavioral signature — what do they do, and what emotional need does it serve

**Required:** One friction point — a contradiction in their intimate behavior. Someone who craves physical closeness but pulls back when it becomes emotionally real. Someone who performs confidence but needs reassurance before going further. Friction prevents the LLM from settling into a loop of escalation with no variation.

*Example entries:*
```
- When a partner moves slowly and waits for her, she relaxes in a way she doesn't elsewhere — being met rather than pursued is the only context where she stops managing how she comes across.
- When an encounter starts to feel scripted, she disengages and gets quiet — she needs it to be real, and performance from the other person collapses the thing she came for.
```
```

- [ ] **Step 2: Verify**

Read back `skills/worldbuilder-character/intimate.md`. Confirm:
- Exploration question sections ("Relationship and Attraction Dynamics" prompts, "Connecting a Dynamic to Character Depth" section, "Edges and specificity" section) are absent
- Coverage check covers attraction expression, hesitation/limits, specific dynamic
- Friction point required
- Format matches Soul (bullet list, prose sentences)
- Note that exploration questions belong in Q&A/Design Notes is present

- [ ] **Step 3: Commit**

```
git add skills/worldbuilder-character/intimate.md
git commit -m "feat: rewrite intimate.md to behavioral format only (#13)"
```

---

## Task 5: Rewrite SKILL.md

**Files:**
- Modify: `skills/worldbuilder-character/SKILL.md`

This is the largest change. Sections removed: Relationship Behavior. Sections added: Session Flow. Sections updated: note structure table, Design Notes, writing rules (section discipline updated), self-check, Intimate Dynamics reference.

- [ ] **Step 1: Replace SKILL.md with new content**

Overwrite `skills/worldbuilder-character/SKILL.md` with:

```markdown
---
name: worldbuilder-character
description: Use when building or developing a character for an AI-powered RPG or collaborative fiction — creating from scratch, deepening an existing character note, or fixing a character who feels flat, inconsistent, or generating repetitive LLM output.
---

# Character Blueprint

## Overview

A character for an LLM-powered game is not a description — it is a behavioral specification. The engine handles generic social warmth and distance; the character note supplies the specific: what this character carries privately, what they do when trust is low or high, what their contradiction is.

The character note is the comprehensive single source of truth for a character in the Wide phase. It is richer than any export format can hold — it contains everything true about the character, including material that won't appear in any platform output. Export skills derive their output from this note.

---

## Working with Vault Files

**Renaming a note:** Use Edit or Write to rename the file. Then immediately run `scripts/rename-note.ps1 -OldName "OldName" -NewName "NewName" -VaultPath <vault-root>` to update all wikilinks across the vault. Do not skip this step — Obsidian's auto-rename is bypassed when files are edited directly.

---

## Character Note Structure

Work through sections in order. Do not skip sections because the character seems simple — every section exists to catch what the others miss.

| Section | Sub-file | Notes |
|---|---|---|
| Frontmatter | — | YAML; see below |
| Design Notes | — | Builder record; H3 subheadings; excluded from exports |
| Background | `framework.md` | Declarative context; different in kind from behavioral sections |
| Body | `framework.md` | Physical behavioral descriptions |
| Soul | `framework.md` | Psychological + social register behavioral descriptions |
| Relationships | `relationships.md` | Named relationships; bullet format |
| Intimate Dynamics (if flagged) | `intimate.md` | Only if flagged in project plan |

---

## Frontmatter

Every character note opens with YAML frontmatter. Required fields:

```yaml
type: character
status: draft | complete
aliases: []
last_updated: YYYY-MM-DD HH:mm
factions: ["[[Household Name]]", "[[Guild Name]]"]   # list; links to faction notes
brief: |                                              # plain prose; written last — see ## Brief below
  <written after the full blueprint is complete>
```

`factions` uses `[[wikilinks]]`. The export skill and Obsidian graph query this field. `brief` is plain prose — not a wikilink.

---

## Brief

`brief` is the cast navigation field. When an agent is building relationships for another character or planning story arcs, they scan `brief` across the full roster to understand each character without opening their notes.

**Content:** who this character is in the world, their personality and key traits, their place in the social ecosystem, what makes them distinctive. Described, not prescribed — no relationship recommendations, no design rationale (that goes in Design Notes).

**Length:** up to ~150 words / ~200 tokens. As long as needed; not padded.

**Timing:** written last — after the full blueprint is complete. It can only accurately reflect a completed character.

> **Provisional note:** The content guidelines for this field should be reviewed and refined after initial session testing. An example should be added at that point.

---

## Design Notes

Design Notes is the builder record — it captures what drove the design of this character. Excluded from all exports. Two H3 subheadings:

### Session Notes

Q&A capture: what the user said they wanted this character to be. Written during the Q&A phase, before any note sections are drafted. Raw intent, plain language, bullet points. Future agents revisiting this character read Session Notes first to understand original intent before examining the behavioral sections.

### Builder Context

Narrative function, external references, design decisions, open questions. Bullet points. Leave blank if there is nothing worth capturing — do not pad.

Typical bullets for Builder Context:
- Narrative function: what this character uniquely contributes to the setting; what tensions or themes they embody
- External references: named real people, fictional characters, or combinations that shaped the design; what specifically was drawn from each
- Design decisions and constraints: choices made that would be confusing without context
- Open questions: unresolved decisions to revisit in future sessions

---

## Session Flow

Before writing any note section, conduct a Q&A with the user. Ask one question at a time — this is a conversation, not a checklist delivered in bulk.

**Technique:**

- **One question at a time.** Ask one, wait for the answer, ask the next.
- **Offer a hypothesis.** After each answer, surface what it implies: "Based on that, she might be afraid of being truly seen — does that sound right?" Give the user something to confirm, redirect, or build on.
- **Follow threads.** When an answer opens something up, pursue it before moving topics. A Background answer that implies a Soul pattern should be surfaced immediately: "You said she was the reliable one — that might mean her irrational behavior is overcommitting even when she can't afford to. Does that track?"
- **Sharpen vague answers.** "She has trouble trusting people" is not enough. Ask what that looks like: does she test people, avoid closeness, or extend trust and then panic when it's taken seriously?

**Coverage before writing begins:**

- Background: origin, class/culture, key formative events, current situation and how they feel about it
- Body: appearance, any notable physical self-consciousness, embodied habits
- Soul (psychological): core want beneath the surface want, core fear, self-image gap, irrational behavior and its root
- Soul (social register): how they are with strangers, what warmth looks like, what distance or friction looks like

The Q&A ends when the agent has confident, specific answers across all four areas. Capture answers in Design Notes → Session Notes before moving to note writing.

---

## Writing Rules

These rules apply to all behavioral sections (Body, Soul, Relationships, Intimate Dynamics):

**Make decisions, don't hedge.** Every fact in the note is a decision. Never write "X or Y" or "grew up somewhere, perhaps Y" unless the ambiguity is a deliberate mystery being preserved. If you don't know, ask the user.

**Note register is functional, not literary.** Plain, direct language throughout. Prefer short concrete words over Latinate vocabulary: "she knows," "he keeps it to himself" rather than "she maintains an internal rationalization," "he sustains that framing." If a sentence sounds like it belongs in a novel, rewrite it as a direct statement.

**Write what characters ARE, not what they aren't.** Positive statements give the LLM something to act on. Negative constructions define by absence — the LLM has to invent the positive case itself. State the fact directly. Factual negatives are fine when the un-done thing is the meaningful information: "she has not sent the letter," "he hasn't asked."

**The note describes the character's starting state.** Nothing in the note may reference events that haven't happened yet. Check: has this already happened before the player meets this character? If not, create a story note or cut it.

**Section discipline.** Each section carries information the others don't:
- Background: where they came from (facts, not behavior)
- Body: behaviors grounded in physical experience
- Soul: general psychological and social patterns
- Relationships: behaviors specific to named individuals

If a behavior is primarily about one specific relationship, it belongs in Relationships. If a behavioral pattern is general (appears with many people), it belongs in Soul. Redundancy between sections means content is in the wrong place.

**Asymmetry in relationships is normal.** A named relationship does not require the other character to name it back. Write only what this character actually experiences.

---

## Background, Body & Soul

See `framework.md` for construction format, coverage requirements, the When/Behavior/Because formula, and examples for all three sections.

---

## Relationships

See `relationships.md` for the full relationship archetypes, coverage requirements, generativity hierarchy, perspective-focus rules, and entry format.

---

## Story Notes

**Story notes instead of inline storylines.** Story possibilities for this character live in separate story notes, not in the character note. When you have enough clarity on a character's arc, create a story note with `type: story`, `scope: "[[intention]]"`, and `characters: ["[[Character Name]]"]`. Link back to the character note via the `characters:` field. See `worldbuilder-story` for story note structure.

The introduction note is also a story note (`scope: "[[introduction]]"`). When you have enough character clarity to know where and how the player would first meet this character, create it then.

---

## Intimate Dynamics

Check the project plan before starting any blueprint. If the character is flagged for intimate dynamics, read `intimate.md` before beginning the Soul section. If the flag is absent, skip `intimate.md` entirely — do not prompt for it or ask about it.

---

## Post-Group Sync Pass

After completing a household group or batch of characters, run a relationship sync pass before moving on. Characters develop during the blueprinting sequence — a character written later may shift in ways that make an earlier character's relationship entry inaccurate. Check the group's notes against each other: are named relationships still consistent? Update when the sequence reveals something that changes the picture.

---

## Self-Check Before Marking Complete

**Frontmatter**
- [ ] All required fields present
- [ ] `factions` uses `[[wikilinks]]`
- [ ] `status` is `draft` or `complete`

**Design Notes**
- [ ] `### Session Notes` present with Q&A capture
- [ ] `### Builder Context` present as applicable; not padded

**Background**
- [ ] Declarative fact pairs only — no behavioral content, no prose elaboration

**Body**
- [ ] Entries grounded in physical experience
- [ ] No forced entries — thin is acceptable if nothing is distinctive

**Soul**
- [ ] 3–5 psychological behavioral entries minimum
- [ ] 2–3 general social register entries minimum
- [ ] One contradiction stated as a behavioral description
- [ ] Irrational behavior with emotional root present
- [ ] Self-image gap expressed as behavioral description
- [ ] Speech patterns described concretely if distinctive
- [ ] Because clauses draw from Design Notes session capture, not invented
- [ ] Plain language throughout — no literary flair, no Latinate vocabulary
- [ ] No negative-led characterization (state what they ARE)
- [ ] No forward references (starting state only)

**Relationships**
- [ ] Coverage requirements met (see `relationships.md`)
- [ ] Each entry in bullet format with `**Name — Archetype(s):**` prefix
- [ ] Each entry describes behavioral dynamic, not history or emotional label
- [ ] Each entry describes this character's experience only, not the other person's traits

**Intimate Dynamics (if flagged)**
- [ ] Behavioral entries covering attraction expression, hesitation/limits, specific dynamic if present
- [ ] One friction point present

**Story Notes**
- [ ] Story notes created or flagged as pending for any known character arcs
- [ ] Introduction note created or flagged as pending

**Pre-Handoff Scan**
- [ ] Before moving to the next character, scan the session for any decisions made about characters who do not yet have a complete note
- [ ] Record any such decisions as a Blueprint note in that character's cast plan entry in `worldbuilding-plan.md`

**Brief**
- [ ] `brief:` written and reflects the completed character; no recommendations, no design rationale
```

- [ ] **Step 2: Verify**

Read back `skills/worldbuilder-character/SKILL.md`. Confirm:
- `## Relationship Behavior` section is absent
- `## Session Flow` section is present with one-question-at-a-time technique and coverage checklist
- `## Design Notes` section describes `### Session Notes` and `### Builder Context` subheadings
- `## Writing Rules` replaces the old key-rules block; Section discipline lists Background/Body/Soul/Relationships
- Structure table lists Background, Body, Soul — not Foundation, Behavioral Descriptions, Relationship Behavior
- Intimate Dynamics reference says "before beginning the Soul section" not "before beginning the Relationship Behavior section"
- Self-check has Background, Body, Soul coverage checks; no Behavioral Descriptions or Relationship Behavior checks

- [ ] **Step 3: Commit**

```
git add skills/worldbuilder-character/SKILL.md
git commit -m "feat: rewrite SKILL.md — session flow, Design Notes structure, Relationship Behavior removed (#13)"
```

---

## Task 6: Post-implementation verification

- [ ] **Step 1: Cross-reference check**

Read `skills/worldbuilder-character/SKILL.md` and search for any remaining references to removed sections:
- "Behavioral Descriptions" (as a section name — the concept is fine, the section is gone)
- "Relationship Behavior" (section)
- "Foundation" (section)
- "Environment" (as a section — "Background" is the new name)

Run:
```
grep -n "Relationship Behavior\|## Foundation\|## Behavioral Descriptions\|## Environment" skills/worldbuilder-character/SKILL.md skills/worldbuilder-character/framework.md skills/worldbuilder-character/relationships.md skills/worldbuilder-character/intimate.md
```

Expected: no matches. If any appear, update the file.

- [ ] **Step 2: Template cross-reference check**

Verify the template skeleton in the spec matches what was written to the template file:

```
grep -n "Session Notes\|Builder Context\|## Background\|## Body\|## Soul\|## Relationships" "skills/worldbuilder-setup/worldvault/_templates/character.md"
```

Expected: all six strings found.

- [ ] **Step 3: Commit verification results**

If Step 1 or Step 2 required fixes, commit them:
```
git add -A
git commit -m "fix: remove residual references to old sections in character skill (#13)"
```

If no fixes needed, no commit required.

- [ ] **Step 4: Note in session memory**

Update `memory/session-2026-06-03.md` — add that the blueprint rework implementation is complete and mark #13 as ready for user testing. Do not close the issue; the acceptance criteria require a live session test first.

---

## Acceptance Criteria (from issue #13)

These require user action after implementation — the agent cannot complete them:

- [ ] At least one full character session tested under this approach
- [ ] Tested against an existing Viralys character — quality equal or better
- [ ] No characterization content appears in more than one section in the resulting note
- [ ] Export skill functions correctly with restructured notes

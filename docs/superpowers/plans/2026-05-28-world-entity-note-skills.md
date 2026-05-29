# World Entity Note Skills Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add `worldbuilder-location-blueprint` and `worldbuilder-faction-blueprint` skills, and improve `worldbuilder-lorebook` with constraint-first concept note guidance.

**Architecture:** Three markdown skill files — two new, one modified. Skills are auto-discovered from `skills/<name>/SKILL.md`; no registration needed. All content is platform-agnostic Wide-phase guidance; nothing references ainime or any export target.

**Spec:** `docs/superpowers/specs/2026-05-28-world-entity-notes-design.md`

---

## File Map

| Action | File | Purpose |
|---|---|---|
| Create | `skills/worldbuilder-location-blueprint/SKILL.md` | New location note skill |
| Create | `skills/worldbuilder-faction-blueprint/SKILL.md` | New faction note skill |
| Modify | `skills/worldbuilder-lorebook/SKILL.md` | 5 targeted additions |
| Modify | `docs/restructure-notes.md` | Mark pending items complete |

---

## Context for Implementers

**Skill file format:** Every skill is a markdown file at `skills/<skill-name>/SKILL.md`. The file opens with YAML frontmatter containing `name` (the skill's identifier) and `description` (what triggers it). The rest is the skill content.

**No registration needed:** The plugin auto-discovers any directory under `skills/` that contains a `SKILL.md`. Creating the file is sufficient.

**Platform-agnostic rule:** These are Wide-phase skills. Never reference ainime field names (`settingSummary`, `loreEntries`, etc.) or any export platform. If guidance depends on an export target, it belongs in the export skill, not here.

**Existing reference:** Read `skills/worldbuilder-character-blueprint/SKILL.md` before starting. It is the model these skills follow — same structural philosophy, same register (functional, not literary), same self-check pattern.

---

## Task 1: Create `worldbuilder-location-blueprint` skill

**Files:**
- Create: `skills/worldbuilder-location-blueprint/SKILL.md`

- [ ] **Step 1: Create the skill directory and file**

Create `skills/worldbuilder-location-blueprint/SKILL.md` with the following complete content:

````markdown
---
name: worldbuilder-location-blueprint
description: Use when creating or deepening a location note for an AI-powered narrative game — building a named place from scratch, giving depth to a location that feels like a backdrop, or fixing a location that generates repetitive or atmospheric-only output.
---

# Location Blueprint

## Overview

A location for an LLM-powered narrative game is not a description — it is a behavioral specification. The engine handles generic scene-setting; the location note supplies the specific: who comes here and why, what the place does to the people in it, how it reads differently at different moments. A location that only answers "what does it look like?" is a backdrop. One that answers "what happens here, and how does this place push back on a scene?" is an actor.

The location note is the comprehensive Wide-phase single source of truth for a named place. It covers everything true about the location that shapes how the engine writes scenes set there. Export skills derive their output from this note.

---

## Location Note Structure

Work through sections in order. Do not skip sections because the location seems simple — every section exists to catch what the others miss.

| Section | Notes |
|---|---|
| Frontmatter | YAML; see below |
| Preamble | 2–3 sentences; see below |
| Concept | Narrative purpose; see below |
| Physical Form | Scale, condition, one vivid specific detail — not a floor plan |
| Social Life | Who comes here, why, what they want, what tensions exist |
| Behavioral Register | How this place reads across time, observer type, circumstances |
| History & Meaning | Why it exists, what it implies, secrets if any |

---

## Frontmatter

Every location note opens with YAML frontmatter. Required fields:

```yaml
type: location
status: draft | complete
aliases: []
last_updated: YYYY-MM-DD
region: "[[The Valley]]"           # link to region note
function: one phrase (plain text)
primary-characters: ["[[Name]]"]   # links to character notes
```

`region` and `primary-characters` use `[[wikilinks]]`. `function` stays plain text — it is usually too specific per location to warrant a navigable link.

---

## Preamble

2–3 sentences at the top of the note body (after frontmatter). Answers: what is this place, and when should this note be used?

> *The grain mill sits at the northern edge of the village and has been out of operation for fifteen years. Use this note whenever the player approaches the mill, asks about it, or encounters anyone connected to the Harrow family. It is the setting's primary location of unresolved guilt.*

Write it as if briefing a reader who needs to use the location correctly right now, without reading the full note.

---

## Concept

The narrative purpose of the location — not a description of what it looks like or what happened there. 3–5 sentences covering:

- What does this location bring to the setting that no other location does?
- What kinds of scenes can only happen here?
- What tension or theme does it anchor?

The concept drives all other section decisions. If two sections pull in different directions, the concept is the tiebreaker.

---

## Physical Form

1–3 sentences. Scale, age, condition, environment, one vivid specific detail.

Not a floor plan. The engine needs to know what kind of place this is, not where the furniture is. One concrete detail beats three paragraphs of layout.

> *The mill is a two-storey stone building with a collapsed east wall, open to the sky. The water wheel still turns sometimes when there's no wind.*

A room-by-room layout is not this section.

---

## Social Life

The ecosystem layer. Who comes here and why. What they do when they arrive. What they want that they might not get. What tensions exist between different regular visitors, or between visitors and whoever maintains the place.

Written as who-does-what, not who-is-there. Every fact in this section is a decision — "various locals may visit for various reasons" is not a Social Life entry.

Cover:
- The main types of people who come here and their reasons
- What they want that the place does or doesn't provide
- At least one tension — between visitor types, between regulars, or between the place and its visitors

---

## Behavioral Register

The section that turns a backdrop into an actor. How this place reads across variations:

- **Time:** day vs. night, busy periods vs. quiet, seasonal rhythm if relevant
- **Observer:** how an insider or regular experiences it differently from a stranger or first-timer — if that distinction would produce meaningfully different scenes
- **Circumstances:** normal operation vs. disrupted, crisis, or changed state

Not all axes apply to every location. Cover the variations that would produce different scenes; skip those that wouldn't. A remote ruin probably does not need an insider/stranger distinction. A village market square likely needs all three.

**The push-back test:** after writing this section, ask — *can this place act on the people in it?* A place that reads identically no matter who is present or what is happening is a backdrop. One that changes tone, creates friction, or imposes its own logic on a scene is a behavioral spec.

---

## History & Meaning

Why this place exists. What it carries from the past. What it implies about the world. Secrets if it has them.

Not required to be long — a sentence or two is often enough — but the "what it implies" question must be answered. A place that exists for no reason is a prop.

If the location is the subject of concept notes at different knowledge layers, link to those notes here rather than duplicating their content.

---

## Key Principles

**Make decisions, don't hedge.** Every fact in the note is a decision. "The mill burned under disputed circumstances" is a decision. "Something may have happened to the mill at some point" is an incomplete note.

**Note register is functional, not literary.** Plain, direct language throughout. "Locals avoid the east wing after dark" is correct. "Shadows cling to its ancient stones like a shroud of forgotten memory" belongs in prose, not a note. If a sentence sounds like it belongs in a novel, rewrite it as a direct statement.

**Physical Form is not the point.** A location note that is mostly Physical Form and thin on Social Life and Behavioral Register is description masquerading as specification. The behavioral sections carry more weight.

**Asymmetry is normal.** Not every location needs every axis of Behavioral Register. Write only what is true and useful.

---

## Self-Check Before Marking Complete

**Frontmatter**
- [ ] All required fields present
- [ ] `region` and `primary-characters` use `[[wikilinks]]`
- [ ] `status` is `draft` or `complete`

**Preamble**
- [ ] 2–3 sentences; answers what this place is and when to use this note
- [ ] Usable without reading the full note

**Concept**
- [ ] States what narrative function this location serves
- [ ] Names what kinds of scenes can only happen here

**Physical Form**
- [ ] 1–3 sentences; one vivid specific detail
- [ ] No floor plan

**Social Life**
- [ ] Names who comes here and why
- [ ] At least one tension in the ecosystem
- [ ] Written as who-does-what, not who-is-there

**Behavioral Register**
- [ ] At least one meaningful variation specified
- [ ] Push-back test passes: the place can act on the scene, not just contain it

**History & Meaning**
- [ ] States why the place exists
- [ ] States what it implies about the world
````

- [ ] **Step 2: Verify file exists and frontmatter is valid**

Run:
```
type "skills\worldbuilder-location-blueprint\SKILL.md" | findstr /n "name: description: type: status:"
```

Expected output includes lines with `name: worldbuilder-location-blueprint`, `description:`, `type: location`, `status: draft | complete`.

- [ ] **Step 3: Verify self-check covers all design spec requirements**

Open `docs/superpowers/specs/2026-05-28-world-entity-notes-design.md` and check the location self-check section. Confirm every item in the spec's self-check appears in the skill file's Self-Check section.

- [ ] **Step 4: Commit**

```bash
git add skills/worldbuilder-location-blueprint/SKILL.md
git commit -m "feat: add worldbuilder-location-blueprint skill

Location notes are behavioral specifications — who comes here, why,
and how the place pushes back on a scene — not descriptions.

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"
```

---

## Task 2: Create `worldbuilder-faction-blueprint` skill

**Files:**
- Create: `skills/worldbuilder-faction-blueprint/SKILL.md`

- [ ] **Step 1: Create the skill directory and file**

Create `skills/worldbuilder-faction-blueprint/SKILL.md` with the following complete content:

````markdown
---
name: worldbuilder-faction-blueprint
description: Use when creating or deepening a faction note for an AI-powered narrative game — any named group (noble household, merchant guild, religious order, criminal network, informal community). Also use when faction members feel interchangeable, or when faction identity is invisible in generated scenes.
---

# Faction Blueprint

## Overview

A faction note is not a roster — it is a shared behavioral specification. The engine handles generic social roles; the faction note supplies the specific: how this group acts as a collective, what its members do when they encounter strangers, how they present to outsiders, and how individuals vary beneath that shared surface.

When a faction is underspecified, the engine defaults to making every member a generic instance of their surface role — every guard gruff, every merchant greedy, faction identity invisible across scenes. The faction note exists to prevent this.

The faction note is the comprehensive Wide-phase single source of truth for any named group. Export skills derive their output from this note.

---

## Faction Note Structure

Work through sections in order.

| Section | Character blueprint analog | Notes |
|---|---|---|
| Frontmatter | — | YAML; see below |
| Preamble | Preamble | 2–3 sentences; what this faction is and when to use this note |
| Concept | Concept | What narrative engine does this faction run? |
| Origin & Purpose | Foundation | Founding, what it controls, its current goal(s) |
| Collective Behavior | Behavioral Descriptions | When/Behavior/Because for the group; Demeanor/Nature split |
| Membership | — | Ranks, acquisition/loss, ambiguity cases |
| Inter-Faction Web | Relationships | Direct allies/rivals only |
| Storylines | Storylines | Story possibilities anchored by this faction |

---

## Frontmatter

Every faction note opens with YAML frontmatter. Required fields:

```yaml
type: faction
status: draft | complete
aliases: []
last_updated: YYYY-MM-DD
members: ["[[Name]]"]   # links to character notes
function: one phrase (plain text)
```

`members` uses `[[wikilinks]]`. `function` stays plain text.

---

## Preamble

2–3 sentences. What is this faction and when should this note be used?

> *The Silt Brotherhood is a loosely-organized network of river traders who control most commercial traffic between the valley settlements. Use this note when the player deals with any river merchant, asks about trade or supply routes, or encounters anyone working the river. They are the faction most likely to have information the player needs and the least likely to offer it directly.*

Write it as if briefing a reader who needs to use the faction correctly right now.

---

## Concept

The narrative engine this faction runs. Not a description of its membership or its history — what does it *do* to the story? What conflicts does it generate or embody? What role does it fill that no other faction could?

A merchant guild and a thieves' guild that produce the same kinds of scenes have the same concept. That is a problem.

---

## Origin & Purpose

Three things, in order:

**Founding** — how the faction came to exist and what its original purpose was.

**Current holdings** — what it controls now. Be specific: resources, territory, monopoly, information, relationships, obligations owed to it. "Has influence" is not a holding.

**Active goal(s)** — what the faction is trying to achieve right now. Goals must be specific and active.

> *Controls the grain trade and intends to extend that monopoly to the river docks before the spring thaw.*

"Seeks to grow its power and influence" is not a goal.

Specific goals connect the faction to the events layer and make it a story engine.

---

## Collective Behavior

The key section. This is what makes faction members read as members.

**Phrasing rule throughout this section:** instructional, not descriptive. Write what members DO, not what they ARE.

> ✓ "When approached by an outsider asking about Brotherhood pricing, members deflect with friendly vagueness — they quote ranges rather than figures, suggest the player talk to the factor, and find a reason to be elsewhere if pressed. Show this."

> ✗ "Members are guarded and don't trust outsiders."

Descriptive phrasing tells the engine what to know. Instructional phrasing tells it what to do.

### Shared behavioral tendencies

3–5 entries in When/Behavior/Because form, applied to the group as a whole:

> When [situation], [members do X] because [faction value or principle].

Cover recognizable situations: encountering outsiders, handling internal conflict or challenge, interacting with rivals or authority, operating under scrutiny or pressure.

### The collective mask (Demeanor)

How members present as a group to people who don't know them. What a stranger interacting with any member of this faction expects to encounter — before individual personality comes through.

This is the shared surface: the thing that makes members recognizable as members.

### The variation layer (Nature)

The individual underneath the collective mask. Members share the Demeanor without sharing the same personality. Name the natural variation axes — do not write out every possible variation, just the axes that produce meaningfully different characters.

> *Loyalists vs. cynics. True believers vs. pragmatists who joined for the wages. Long-timers who remember the Brotherhood's origins vs. recent recruits who only know its current operation.*

This is what prevents members from being interchangeable. They wear the same mask; who they are underneath differs.

---

## Membership

Deliberately thin on named-member content — named members have their own character notes. Covers:

- **Ranks or tiers** if they exist (hierarchy only — no personalities here)
- **Acquisition** — how one becomes a member
- **Loss** — how membership ends or is revoked
- **Ambiguity cases** — former members, dual loyalties, contested membership, outsiders who function as members without formal standing

Ambiguity cases earn their place because characters who straddle faction lines are often the most narratively generative.

---

## Inter-Faction Web

Lightweight by design. Direct relationships only — alliances, rivalries, contested territory, historical grievances with active weight. No comprehensive opinion-of-everyone map.

Each entry:
```
[[Faction Name]] — allied / neutral / rival / enemy: one sentence on what drives it.
```

Relationships that don't bear on the current project do not go here.

---

## Storylines

Story possibilities anchored by this faction's existence. Not scripts — possibilities. Phrased as "could," "may," "there is a possibility that."

What could this faction do or reveal that no other faction could?

---

## Key Principles

**The member test.** After completing Collective Behavior, ask: if you wrote an unnamed member of this faction into a scene with no other characterization, would they read as a member? If not, the section is incomplete.

**Make decisions, don't hedge.** An active goal that is vague is not a goal. A Demeanor that could belong to any group is not a Demeanor.

**Collective Behavior is the priority section.** A faction note that is mostly Origin & Purpose and thin on Collective Behavior documents history without specifying behavior. History is less important than what the faction does.

**Instructional phrasing is not optional.** Descriptive phrasing in Collective Behavior will not produce behavioral consistency in output. Every entry must specify what members do.

---

## Self-Check Before Marking Complete

**Frontmatter**
- [ ] All required fields present
- [ ] `members` uses `[[wikilinks]]`
- [ ] `status` is `draft` or `complete`

**Preamble**
- [ ] 2–3 sentences; usable without reading the full note

**Concept**
- [ ] States what narrative engine this faction runs
- [ ] Names what conflicts it generates that no other faction could

**Origin & Purpose**
- [ ] Has a specific active goal (not "seeks power" or similar)
- [ ] Names what the faction currently controls (specific, not "influence")

**Collective Behavior**
- [ ] 3–5 When/Behavior/Because entries for the group
- [ ] Demeanor (collective mask) described
- [ ] Variation layer (Nature axes) named
- [ ] All entries phrased as instructional directives, not description
- [ ] Member test passes: an unnamed member would read as a member

**Membership**
- [ ] How membership is acquired and lost is stated
- [ ] Ambiguity cases addressed

**Inter-Faction Web**
- [ ] Direct relationships only
- [ ] Each entry has status + one sentence on what drives it

**Storylines**
- [ ] All entries phrased as possibility, not script
````

- [ ] **Step 2: Verify file exists and frontmatter is valid**

Run:
```
type "skills\worldbuilder-faction-blueprint\SKILL.md" | findstr /n "name: description: type: status:"
```

Expected output includes lines with `name: worldbuilder-faction-blueprint`, `description:`, `type: faction`, `status: draft | complete`.

- [ ] **Step 3: Verify self-check covers all design spec requirements**

Open `docs/superpowers/specs/2026-05-28-world-entity-notes-design.md` and check the faction self-check section. Confirm every item in the spec's self-check appears in the skill file's Self-Check section.

- [ ] **Step 4: Commit**

```bash
git add skills/worldbuilder-faction-blueprint/SKILL.md
git commit -m "feat: add worldbuilder-faction-blueprint skill

Faction notes are shared behavioral specifications — collective
Demeanor/Nature split and instructional When/Behavior/Because entries
make faction identity visible across scenes without cloning members.

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"
```

---

## Task 3: Improve `worldbuilder-lorebook`

**Files:**
- Modify: `skills/worldbuilder-lorebook/SKILL.md`

Five targeted changes. Read the full file before making any changes to understand the current structure.

- [ ] **Step 1: Add narrative purpose prompt after the Concept Note Frontmatter section**

Find the line:
```
## Alias Writing Guidance
```

Insert the following new section immediately before it:

```markdown
## Narrative Purpose

Before writing a concept note's content, answer one question:

> *What does the existence of this thing make impossible, costly, or inevitable in a scene that touches it?*

A concept note that cannot answer this question is description, not a constraint. Writing the answer first shapes everything that follows — it tells you what to include and what to cut.

---

```

- [ ] **Step 2: Add limitations and costs section after Alias Writing Guidance**

Find the line:
```
## The Three-Layer Structure
```

Insert the following new section immediately before it:

```markdown
## Limitations and Costs

For any concept note covering a rule-bearing concept — magic systems, institutions, cultural practices, social structures, belief systems, anything with internal logic that scenes must respect — include a limitations and costs block.

The block specifies:
- What the concept **cannot** do
- What it **costs or demands** from those who use it or participate in it
- What makes it **fail, break, or produce unexpected results**

A concept documented only by what it can do cannot constrain a scene. One documented by its limits and costs can.

**Example:** A healing magic concept note that says "healers can mend wounds and cure illness" does not constrain anything. One that adds "healing draws from the healer's own vitality — serious wounds leave the healer bedridden for an equal period, and healing the dying risks the healer's own death" constrains every scene that touches it.

Concept notes for rule-bearing concepts without a limitations block are incomplete. See the self-check at the end of this skill.

---

```

- [ ] **Step 3: Add two-layer iceberg split to the Three-Layer Structure section**

Find the following line (it appears at the end of the Deep layer subsection):
```
**Tone:** Confirmed and weighted. These entries feel like the answer to questions the surface layer raised. Don't explain everything — some things can remain permanent mystery.
```

Add the following block immediately after it (before the next `---` or `##`):

```markdown

---

## The Iceberg Split

Distinct from the surface/mid/deep classification, which governs editorial intent about pacing and register. The iceberg split operates *within a single note*, for cases where what people in the world believe and what is actually true diverge.

Where the gap between belief and truth is narratively significant, document both in the same note:

**Believed:** what characters in the world commonly say, assume, or act on — the public version, the legend, the received wisdom.

**True:** what actually happened, or how the thing actually works underneath the common understanding.

This lets the engine have characters speak and act from belief while the true version constrains what can actually happen and what specific informed characters know. A surface-layer note might record "everyone knows the mill fire was an accident." The true version (in the same note's iceberg block) is that it was arson. Characters on a surface-layer context act on the belief; characters with deep knowledge act on the truth.

Not every concept note needs this. Use it only when the gap between belief and truth is a live story element.

**Note on layer classification and runtime gating:** The surface/mid/deep layer on a concept note records authorial intent — this is when this knowledge should feel available to the player, and at this register it should be written. It is not a reliable mechanism for suppressing information from the engine at runtime; whether a given engine can actually gate context on conditions varies. The value of the layer classification is in how you write the content and in what the export layer can do with the metadata.

```

- [ ] **Step 4: Replace the Location Entries section with a pointer**

Find the entire Location Entries section:
```markdown
## Location Entries

Short. Physical character first, then narrative associations.

Cover:
- What the place looks like
- Who comes here, why, what they do
- What it means — the emotional or narrative weight of this location
- One vivid specific detail

One vivid detail beats three paragraphs of layout. "The old mill hasn't operated in fifteen years. The water wheel still turns sometimes when there's no wind." tells the engine more useful things than a floor plan.

Location entries are not image generation descriptions. They tell the engine what a place means and who uses it — not a visual reference. Image generation descriptions are a separate document.

---
```

Replace it with:

```markdown
## Location Notes

Location notes have their own dedicated skill: **`worldbuilder-location-blueprint`**. Use that skill when creating or deepening any named location. It provides the full note structure, section guidance, and self-check.

---
```

- [ ] **Step 5: Add completion self-check at the end of the file**

Append the following to the end of `skills/worldbuilder-lorebook/SKILL.md`:

```markdown

---

## Self-Check Before Marking Complete

**Complete when:** the note can constrain or shape any scene that touches this concept — a scene author knows what is impossible, what costs something, and what is inevitable because of this note.

**Limitations block check:** if this is a rule-bearing concept (magic system, institution, cultural practice, social structure, belief system), does the note include a limitations and costs block? A concept note without one is incomplete, regardless of how much descriptive content it contains.

**Over-documented when:** any section adds detail no scene will touch, or duplicates content already in a character, location, or faction note. Concept notes are meant to be short and dense — duplication bloats context for no gain.
```

- [ ] **Step 6: Verify all five changes are present**

Run a scan for the new section headers:
```
findstr /n "Narrative Purpose\|Limitations and Costs\|Iceberg Split\|Location Notes\|Self-Check Before" "skills\worldbuilder-lorebook\SKILL.md"
```

Expected: five matches, one for each addition.

- [ ] **Step 7: Read the full modified file and confirm it flows correctly**

Read `skills/worldbuilder-lorebook/SKILL.md` in full. Check:
- Narrative Purpose appears before Alias Writing Guidance
- Limitations and Costs appears before The Three-Layer Structure
- Iceberg Split appears within or immediately after the Three-Layer Structure section
- Location Entries has been replaced with the pointer
- Self-Check is the last section in the file

- [ ] **Step 8: Commit**

```bash
git add skills/worldbuilder-lorebook/SKILL.md
git commit -m "feat: deepen worldbuilder-lorebook with constraint-first concept guidance

Add narrative purpose prompt, limitations/costs block requirement,
iceberg split (believed vs. true), and completion self-check.
Retire location entries section — replaced by location-blueprint skill.

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"
```

---

## Task 4: Update `docs/restructure-notes.md`

**Files:**
- Modify: `docs/restructure-notes.md`

- [ ] **Step 1: Mark the pending items complete**

Find the Pending Work section at the bottom of `docs/restructure-notes.md`:

```markdown
**Low priority:**

- **Develop world and story skill equivalents to character system depth** — currently underspecified; needs equivalent rigor to blueprint process for locations, factions, and concept notes
```

Replace it with:

```markdown
**Low priority:**

- ✅ **Develop world and story skill equivalents to character system depth** — completed 2026-05-28: `worldbuilder-location-blueprint` and `worldbuilder-faction-blueprint` added; `worldbuilder-lorebook` deepened with constraint-first concept guidance. See `docs/superpowers/specs/2026-05-28-world-entity-notes-design.md`.
```

- [ ] **Step 2: Commit**

```bash
git add docs/restructure-notes.md
git commit -m "docs: mark world entity note skills as complete in restructure notes

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"
```

---

## Task 5: Final verification pass

**No file changes — read-only review.**

- [ ] **Step 1: Confirm both new skills are discoverable**

Run:
```
dir skills\ /b
```

Expected output includes `worldbuilder-location-blueprint` and `worldbuilder-faction-blueprint` alongside existing skill directories.

- [ ] **Step 2: Cross-check location skill against spec**

Open `docs/superpowers/specs/2026-05-28-world-entity-notes-design.md`, Deliverable 1 section. For each item in the spec's self-check, confirm the corresponding check appears in `skills/worldbuilder-location-blueprint/SKILL.md`.

- [ ] **Step 3: Cross-check faction skill against spec**

Open the spec, Deliverable 2 section. For each item in the spec's self-check, confirm the corresponding check appears in `skills/worldbuilder-faction-blueprint/SKILL.md`.

- [ ] **Step 4: Cross-check lorebook against spec**

Open the spec, Deliverable 3 section. Confirm all five additions are present in `skills/worldbuilder-lorebook/SKILL.md`:
1. Narrative purpose prompt — present before Alias Writing Guidance
2. Limitations and costs block — present before Three-Layer Structure
3. Iceberg split — present after Three-Layer Structure
4. Location entries retired — replaced with pointer to location-blueprint
5. Completion self-check — present at end of file

- [ ] **Step 5: Confirm no ainime field names appear in new or modified skill files**

Run:
```
findstr /i "settingSummary\|loreEntries\|storyTriggers\|arcManagerGuidance\|baseProfile\|ainime" "skills\worldbuilder-location-blueprint\SKILL.md" "skills\worldbuilder-faction-blueprint\SKILL.md" "skills\worldbuilder-lorebook\SKILL.md"
```

Expected: no matches. Any match is a platform-coupling violation — remove the reference.

- [ ] **Step 6: Confirm git log shows four clean commits**

Run:
```bash
git log --oneline -6
```

Expected: the four commits from Tasks 1–4 are present and correctly scoped.

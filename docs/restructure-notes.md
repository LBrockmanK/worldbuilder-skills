# Restructure Discussion Notes — 2026-05

Working notes from design discussions. These will be formalized into ADRs once the research phase (see `research-brief-worldbuilding-docs.md`) is complete and structure decisions are finalized.

---

## Decisions Reached

### Platform decoupling

**Decision:** Phases 1 and 2 are platform-agnostic. Only Phase 3 (Export) is platform-specific.

**Supersedes:** ADR-0002 (seed document uses target system field format). The seed document no longer writes ainime-games JSON field names. Same creative content, natural section headers.

**Rationale:** Coupling the creative process to a single export format means any change to that format — or any desire to target a different platform — requires reworking the creative documents. The creative content and the export format are independent concerns and should be separated.

**Implication:** A new export skill (`worldbuilder-ainime-export` or similar) does the real format-mapping work in Phase 3. It is the only skill that knows about `settingSummary`, `loreEntries`, `storyTriggers`, `arcManagerGuidance`, etc.

---

### Three conceptual areas

**Decision:** The Wide phase organizes content around three areas: World, Story, Characters. The Seed is the project proposal that precedes them.

The areas may manifest as folders or as note types in a flat structure — this is pending the research brief findings. They are conceptual groupings, not necessarily filesystem hierarchies.

---

### Lorebook is an export artifact

**Decision:** The lorebook format (keyword arrays, entry IDs, trigger mechanism) is platform-specific. It belongs entirely in the export phase.

World knowledge in the Wide phase is organized by what it *is*, not by how it will be delivered. The export skill reads world knowledge and packages it as lorebook entries. We do not maintain a separate lorebook document in the Wide phase.

**Implication:** The layer classification (surface/mid/deep) becomes frontmatter metadata on world documents rather than a lorebook-specific concern. The "Lorebook Candidates" section in Wide phase documents should be reconsidered — its function may be better served by note metadata.

---

### Story constraints

**Decision:** The story section has three distinct components that must not be collapsed:

1. **Direction** — prescriptive guidance to the AI on tone, pacing, escalation, dark theme handling. Fully applicable regardless of player behavior.
2. **Starting state** — what is factually true about the world when play begins.
3. **Intentions** — where we'd like things to go. Soft targets, not scripts. Player influence means these cannot be preordained outcomes.

The distinction matters because starting state is written as truth; intentions are conditional on player choices.

**ainime-specific note:** `storyTriggers` and `arcManagerGuidance` are export-layer artifacts. The export skill converts direction into `arcManagerGuidance` and intentions into `storyTriggers` where conditions allow.

---

### Frontmatter headers on all documents

**Decision:** All files carry YAML frontmatter with a machine-readable summary sufficient to understand the file's content without reading it.

**Rationale:** Enables fast scanning across large document sets (for both LLM and human), reduces the need for separate index/roster documents, and provides structured metadata the export skill can use.

Minimum useful frontmatter fields to determine — pending research brief. Character files are the reference point for what's already working.

**Implication:** The roster file (`characters/roster.md`) may become redundant if character file headers carry sufficient information. The same applies to other index documents.

---

### Flat vs. hierarchical structure

**Open question** — pending research brief.

Preliminary position: folder hierarchy (world/, story/, characters/) may be unnecessary if note types and frontmatter carry the organizational information. Flat Obsidian vault structures are common and may serve better for cross-cutting entities (an event that involves a character, a location, and a story beat).

---

### Obsidian as optional visualization layer

**Decision:** The document format is Obsidian-compatible markdown — YAML frontmatter plus wiki-link-style entity references. Users with Obsidian get graph visualization. Users without it have well-structured markdown files.

A true knowledge graph (RDF, property graph database) was considered and rejected: the overhead doesn't add interpretability for LLM-assisted workflows, and the pseudo-graph through consistent naming and wiki links is sufficient.

---

### Character system as the model

**Observation:** The character system (world-foundation → blueprint → card) is the most developed and refined part of the workflow. It has clear process, clear format, and clear quality criteria (negative tracks, influence thresholds, archetype coverage, household design).

World and Story are currently underspecified by comparison. Developing equivalent rigor for those areas is a future work item, informed by the research brief findings.

---

## Structure Decisions (from research findings)

### Vault structure: shallow hybrid by note type

6–8 folders by note type, flat within each. Not flat vault (breaks above ~50 notes). Not deep hierarchy (notes are multi-categorical). Organizing by type rather than by conceptual area (World/Story/Characters) solves cross-cutting entity placement. The three-area model is a mental map, not a folder hierarchy.

```
worldbuilding-plan.md
seed.md
log.md                  ← retcon and change log
characters/
locations/
factions/               ← households, organizations, groups
events/                 ← historical events, calendar events, story moments
concepts/               ← world rules, lore topics, magic systems, cultural facts
story/                  ← narrative direction, creative brief, intentions
_templates/
```

### Note types and frontmatter

Universal on every note:
```yaml
type: character | location | faction | event | concept | story
status: draft | complete
aliases: []
last_updated: YYYY-MM-DD
```

Type-specific:
```yaml
# character
factions: ["[[Household Name]]", "[[Guild Name]]"]   ← list; links to faction notes
role: plain text (too specific per character to warrant links)
archetype: "[[Initially Hostile]]"                   ← link; makes archetype groups queryable

# location
region: "[[The Valley]]"                             ← link
function: one phrase (plain; usually too specific)
primary-characters: ["[[Char1]]", "[[Char2]]"]       ← links

# faction/household
members: ["[[Char1]]", "[[Char2]]"]                  ← links
function: one phrase

# event
date: "[[Spring-08]]"                                ← link; clusters all events on a day
recurring: false                                     ← boolean, no link needed
characters: ["[[Char1]]"]                            ← links
location: "[[Location Name]]"                        ← link

# concept (lore)
layer: "[[surface]]"                                 ← link; clusters lore by depth
trigger-context: brief activation note (plain text)

# story
scope: "[[direction]]"                               ← link; groups direction vs intention vs arc
```

**Link convention:** anything that represents a category, entity, or concept worth filtering by or navigating to is a `[[wikilink]]` — even if the target note never gets created. Graph treats unresolved links as dangling nodes that still enable clustering. `status`, `last_updated`, `recurring`, and other operational/boolean fields stay as plain values.

**`available-from` removed entirely.** Date-gating of when characters or lore become available is an ainime-specific export decision. Does not belong in platform-agnostic note frontmatter. The ainime export skill handles this when packaging.

### "For future Claude" preamble

Every note body begins with 2–3 sentences describing what the note is and when to use it. Replaces the roster as a quick-reference layer for characters. From ghelburlabs' AI-First Vault Principle — reported to dramatically improve LLM retrieval relevance.

### Mandatory wikilinks

Explicit `[[Entity Name]]` references throughout note bodies. Highest-leverage single investment for LLM workflows (graphify data: ~50% of well-tended vaults have 12+ wikilinks per file; the other 50% have zero).

### Consistency process

- `log.md` at root — every retcon logged with date
- `confidence: high|medium|low` frontmatter for unstable canon
- `contested: true` for known contradictions (preserve both claims with dates, don't silently overwrite)
- Periodic lint: orphan notes, broken wikilinks, stale `last_updated`

### Character note scope (Wide phase)

The character note is the comprehensive single source of truth. Richer than the old blueprint because we are no longer constrained to what the ainime card format can hold. Includes:
- Blueprint content (behavioral dimensions, influence thresholds, relationships, future storylines)
- Roster-level quick-reference info (now in frontmatter)
- Design notes — why this character exists, narrative function, structural role
- Inspirations — real people or characters drawn from
- Extra facts — anything true that doesn't fit neat categories

The card (ainime `baseProfile`) is derived from the character note by the export skill.

### Lorebook Candidates concept

Dissolves as a separate concept. `concepts/` notes and relevant `events/` notes are world knowledge. The ainime export skill reads them and packages them into lorebook entries with keyword assignment. Layer classification (`surface | mid | deep`) lives in frontmatter on the concept note.

### ADR-0002 status

Formally superseded. Seed phase produces `seed.md` (project proposal and foundational decisions) — not `world-seed.md` in ainime field format.

---

## Story Note Structure

Story notes use hierarchy rather than distinct frontmatter per level. Each note has an `up:` link to its parent story note. The top-level note (grand direction / creative brief) has no parent.

```
direction.md (top level, up: absent)
  └── arc-opening-year.md (up: "[[direction]]")
        └── intention-first-festival.md (up: "[[arc-opening-year]]")
```

`scope` field retained to make level queryable in Dataview:
```yaml
type: story
status: draft | complete
aliases: []
last_updated: YYYY-MM-DD
up: "[[parent-story-note]]"     ← absent on top-level note
scope: "[[direction]]" | "[[arc]]" | "[[intention]]"
```

The top-level direction note = the creative brief / standing narrative guidance (what was arcManagerGuidance in ainime). Arc notes = major story sections. Intention notes = specific moments or developments the world is set up to enable (not preordained — player can affect them).

---

## Character Note Structure

The Wide-phase character note is the comprehensive single source of truth. Sections in order:

**Frontmatter** — type, status, aliases, last_updated, factions, role, archetype (as link)

**Preamble** — 2–3 sentences: what this character is and when to use this note ("For future Claude")

**Concept** — the character idea; what they bring to the setting; what they're for narratively

**Inspirations** — real people, existing characters, or combinations that shaped the design

**Design Notes** — meta-commentary: narrative function, structural role, what makes them interesting to write; excluded from all exports

**Foundation** — body, environment, soul (current blueprint Part 1)

**Behavioral Descriptions** — When/Behavior/Because form; contradictions (current blueprint Part 2)

**Relationships** — social web, named connections (current blueprint Relationships section)

**Relationship Behavior** — replaces "Influence Thresholds"; drops the ainime numbered-band convention entirely. Describes how this character acts and speaks across the like/dislike axis and across different relationship types. No fixed structure — written as behavioral description covering:
- How they present to people they don't know yet
- What warmth looks like when it's present (does it show? how?)
- What distance, coldness, or conflict looks like for this character specifically
- Any notable variation by relationship type (authority vs. peers vs. someone they're mentoring, etc.) if relevant to the character

The intimate dynamics section handles the romantic register when that flag is set. Export skills map this section to platform mechanics as needed.

**Appearance** — physical description; stays in character note, used by all export formats

**Storylines** — formerly "Future Storylines"; generic story possibilities for this character. Becomes ainime's `future_storylines`, SillyTavern's alternate greetings, or similar depending on export target. Not platform-specific in the note itself.

**Sections removed from blueprint:**
- Stage 1 (Roster entry) — replaced by frontmatter + preamble
- Stage 3 (Card) — moves to ainime export skill
- Part 6 Metadata (Available Day, Sprite Sets) — ainime-specific, moves to export skill
- Lorebook Candidates — dissolves; lore becomes concepts/ notes directly

---

## Templates and Obsidian Config

**Templates folder:** Copy note templates from skill instructions into `_templates/` in the project vault for human users. Claude operates without them. Low priority — note templates are in the skill.

**Obsidian config (future task):** Create a default `.obsidian/` config for new worldbuilding projects including:
- Useful plugins pre-configured: Dataview, Breadcrumbs, Smart Connections, Relations
- Folder structure already created
- Core settings (link format, new note location, etc.)

This is a setup step, likely as part of project initialization in `worldbuilder-world-planning` or a separate setup skill. Deprioritized for now; revisit when MCP / direct Obsidian integration is considered.

---

## Introduction Notes

The character introduction is its own story note, not a character file section. `type: story`, `scope: "[[introduction]]"`.

Rationale: a single introduction scene can bring multiple characters into contact with the player at once; keeping it in the character file would duplicate it or force an awkward primary-ownership choice. The introduction note can reference multiple characters and link to an arc if appropriate.

An introduction note may coincide with a calendar event (e.g., a festival is both a world event and where the player first meets three characters). When this happens the event note and the introduction note reference each other; they serve different purposes and both exist.

Story scope values: `"[[direction]]"`, `"[[arc]]"`, `"[[intention]]"`, `"[[introduction]]"`

Introduction note contains:
- Where and when first contact happens (or the general circumstance if undated)
- Who is present
- What brings the player into contact with them
- How each character registers a stranger
- The emotional register / what this scene establishes
- Link to arc if tied to one; `up:` absent or pointing to a broader arc note

---

## Open Questions

(None currently — all major structural decisions resolved pending implementation.)

---

## Completed This Session

- `docs/target-system.md` — ainime-games field reference (authoritative schema, format version 2)
- `CONTEXT.md` — added Expected Project File Structure section and What Goes Where table
- `skills/writing-style.md` — rewritten as technical spec register only; prose register deferred to export skill
- `skills/worldbuilder-ingestion/SKILL.md` — new skill covering all ingestion cases
- `skills/worldbuilder-world-planning/SKILL.md` — orchestrator behavior; ingestion routing; v2.0 revision case; updated phase table
- `skills/worldbuilder-calendar/SKILL.md` — removed dailyPlannerDirective references; redirected scene structure to arcManagerGuidance
- `skills/worldbuilder-story-direction/SKILL.md` — added scene structure hook from calendar; fixed dead reference; added Lorebook Candidates section
- `skills/worldbuilder-lorebook/SKILL.md` — added Lorebook Candidates review pass section
- `skills/worldbuilder-character-blueprint/SKILL.md` — added Lorebook Candidates section (partial update only; full rewrite pending)
- `docs/research-brief-worldbuilding-docs.md` — research brief dispatched to agent
- `docs/Worldbuilding Structure Research Results.md` — research findings (added by research agent)
- `docs/restructure-notes.md` — this file; design decisions log

---

## Pending Work (Next Session)

**High priority — implement structural decisions:**

1. **Formalize ADRs** — write ADR-0003 (platform decoupling, supersedes ADR-0002); update ADR-0001 for Export phase clarification

2. **Rewrite `worldbuilder-character-blueprint`** — the biggest change:
   - Drop Stage 1 (roster entry) — replaced by frontmatter + preamble
   - Drop Stage 3 (card assembly) — moves to ainime export skill
   - New note structure: frontmatter → preamble → concept → inspirations → design notes → foundation → behavioral descriptions → relationships → relationship behavior → appearance → storylines
   - Replace influence thresholds with relationship behavior (prose description, no fixed bands)
   - Rename future storylines → storylines
   - Remove lorebook candidates section (world knowledge goes to concepts/ notes directly)
   - Introduction moves out to its own story note (`scope: "[[introduction]]"`)

3. **Update `worldbuilder-world-foundation`** — remove ainime JSON field names from seed phase output; seed produces platform-agnostic `seed.md`

4. **Update `worldbuilder-world-planning`** — remove ainime-specific items from phase checklists (Available Day, Sprite Sets, Daily Planner Directive, token counts); update phase table for new note-based structure; replace roster step with character note frontmatter guidance

5. **Write `worldbuilder-ainime-export`** — receives: card prose assembly from character notes, influence band mapping from relationship behavior, available-from assignment, sprite sets, token targets, lorebook entry packaging from concepts/ notes, storyTriggers from events/ notes, arcManagerGuidance from story/ direction note

**Medium priority:**

6. **Update `worldbuilder-lorebook`** — remove platform-specific entry format; the skill now covers concepts/ note creation rather than lorebook entry writing

7. **Update `worldbuilder-calendar`** — remove storyTriggers/calendarConfig field framing; calendar becomes events/ notes with standard frontmatter

8. **Update `worldbuilder-story-direction`** — remove arcManagerGuidance framing; story direction becomes story/ notes with hierarchy

9. **Develop world and story skill equivalents to character system depth** — currently underspecified; needs equivalent rigor to blueprint process for locations, factions, and concept notes

**Low priority:**

10. **Templates folder** — copy note templates from skill instructions into `_templates/` in project vault for human users

11. **Default Obsidian config** — `.obsidian/` config for new worldbuilding projects: Dataview, Breadcrumbs, Smart Connections, Relations pre-configured; folder structure created; as part of project init in world-planning or separate setup skill

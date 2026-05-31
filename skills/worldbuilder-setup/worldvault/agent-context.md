---
type: reference
status: complete
last_updated: YYYY-MM-DD HH:mm
---

# Agent Context

> Read this note at the start of any vault session. It is a compact operational reference — not a worldbuilding note. User-editable.

---

## Note Type Schema

All notes carry universal frontmatter plus type-specific fields.

**Universal (all types):**
```yaml
type: character | location | faction | event | concept | story | project | reference
status: draft | complete
aliases: []
last_updated: YYYY-MM-DD HH:mm
```

**Character** — `notes/`
```yaml
factions: ["[[Household Name]]"]
role: plain text
archetype: "[[Initially Hostile]]"
```
Sections: Preamble, Concept, Inspirations, Design Notes, Foundation, Behavioral Descriptions, Relationships, Relationship Behavior, Appearance, Storylines

**Location** — `notes/`
```yaml
region: "[[The Valley]]"
function: one phrase
primary-characters: ["[[Name]]"]
```
Sections: Preamble, Concept, Physical Form, Social Life, Behavioral Register, History & Meaning

**Faction** — `notes/`
```yaml
members: ["[[Name]]"]
function: one phrase
```
Sections: Preamble, Concept, Origin & Purpose, Collective Behavior, Membership, Inter-Faction Web, Storylines

**Concept** — `notes/`
```yaml
layer: "[[surface]]"        # surface | mid | deep
trigger-context: brief plain text
```
Sections: Preamble, Limitations and Costs, Content

**Story** — `notes/`
```yaml
up: "[[parent-story-note]]"     # absent on top-level direction note
scope: "[[direction]]" | "[[arc]]" | "[[intention]]" | "[[introduction]]"
```
Sections: Preamble, Content

**Project** — vault root
```yaml
# no additional type-specific fields
```
Documents: `worldbuilding-plan.md`, `seed.md`, `log.md`

**Reference** — vault root
```yaml
# no additional type-specific fields
```
Documents: `agent-context.md` (this file)

**Link convention:** Anything that represents a category, entity, or concept worth filtering by uses a `[[wikilink]]`. Operational fields (`status`, `last_updated`, booleans) use plain values.

---

## Vocabulary

**Seed phase** — Clarification-heavy opening phase. Produces `seed.md`. _Avoid: Foundation phase, setup phase._

**Wide phase** — Expansive generative phase. Produces all character, location, faction, concept, and story notes in `notes/`. _Avoid: Development phase._

**Export phase** — Conversion phase. Packages Wide-phase notes into the target system format. The only phase that writes ainime field names. _Avoid: Deliverables phase._

**seed.md** — World foundation document. Plain prose with natural section headers. Not written in export format.

**Character note** — Comprehensive single source of truth for one character. Richer than any export format.

**Concept note** — A discrete piece of world knowledge in `notes/`. Layer-tagged: surface (freely shareable), mid (contextual), deep (revealed late).

**Story note** — Narrative direction document in `notes/`. Scope hierarchy: direction → arc → intention. Introduction notes have `scope: "[[introduction]]"`.

**Cast planning** — Wide-phase process of planning the full cast before writing individual notes. Produces the cast plan in `worldbuilding-plan.md`.

**Coverage check** — Pre-completion review: main/side ratio, household balance, archetype slot coverage, negative-track characters present.

---

## Skill Routing

| Task | Skill |
|---|---|
| New project setup | `worldbuilder-setup` (once only, then world-planning) |
| Session start / phase routing | `worldbuilder-world-planning` |
| Seed phase / world foundation | `worldbuilder-world-foundation` |
| Character notes | `worldbuilder-character` |
| Location notes | `worldbuilder-location` |
| Faction notes | `worldbuilder-faction` |
| Concept notes | `worldbuilder-concept` |
| Story notes | `worldbuilder-story` |
| Ingest existing material | `worldbuilder-ingestion` |
| Export to target system | `worldbuilder-ainime-export` |

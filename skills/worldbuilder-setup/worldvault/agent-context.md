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
factions: ["[Household Name](notes/Household Name.md)"]
brief: plain prose   # cast navigation summary; written last
```
Sections: Design Notes, Foundation, Behavioral Descriptions, Relationships, Relationship Behavior

**Location** — `notes/`
```yaml
region: "[The Valley](notes/The Valley.md)"
function: one phrase
primary-characters: ["[Name](notes/Name.md)"]
```
Sections: Preamble, Concept, Physical Form, Social Life, Behavioral Register, History & Meaning

**Faction** — `notes/`
```yaml
members: ["[Name](notes/Name.md)"]
function: one phrase
```
Sections: Preamble, Concept, Origin & Purpose, Collective Behavior, Membership, Inter-Faction Web, Storylines

**Concept** — `notes/`
```yaml
layer: "[surface](notes/surface.md)"   # surface | mid | deep
trigger-context: brief plain text
```
Sections: Preamble, Limitations and Costs, Content

**Story** — `notes/`
```yaml
up: "[Parent Note](notes/Parent Note.md)"     # absent on top-level direction note
scope: "[arc](notes/arc.md)"                 # arc | intention | introduction
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

**Link convention:** Named entity references (characters, locations, factions, events, concepts, story notes) use standard markdown links: `[Display Name](notes/Display Name.md)`. The filename matches the display name. Classification values (`layer`, `scope`, `date`) also use markdown links. Operational fields (`status`, `last_updated`, booleans) use plain strings. In body text, link to referenced notes on first mention per section — the `worldbuilder-linking` skill handles this as a post-pass.

---

## Vocabulary

**Seed phase** — Clarification-heavy opening phase. Produces `seed.md`. _Avoid: Foundation phase, setup phase._

**Wide phase** — Expansive generative phase. Produces all character, location, faction, concept, and story notes in `notes/`. _Avoid: Development phase._

**Export phase** — Conversion phase. Packages Wide-phase notes into the target system format. The only phase that writes ainime field names. _Avoid: Deliverables phase._

**seed.md** — World foundation document. Plain prose with natural section headers. Not written in export format.

**Character note** — Comprehensive single source of truth for one character. Richer than any export format.

**Concept note** — A discrete piece of world knowledge in `notes/`. Layer-tagged: surface (freely shareable), mid (contextual), deep (revealed late).

**Story note** — Narrative direction document in `notes/`. Scope hierarchy: direction → arc → intention. Introduction notes have `scope: "[introduction](notes/introduction.md)"`.

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

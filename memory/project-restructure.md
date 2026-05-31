---
name: project-restructure
description: Platform-decoupling architecture decisions for worldbuilder-skills; implementation state across sessions
metadata:
  type: project
---

Platform-decoupling restructure: Phases 1–2 are now platform-agnostic; only Phase 3 (Export) is platform-specific. The ainime-games field names no longer appear in Wide-phase documents. `worldbuilder-ainime-export` handles all field mapping.

**Why:** Coupling creative documents to one export format blocks retargeting and makes format changes painful.

**How to apply:** Any skill that writes ainime field names in Wide-phase output is wrong; flag it. The export skill is the only one that knows platform-specific fields.

## Architecture decisions (all finalized — see docs/restructure-notes.md)

- Vault structure: **flat `notes/` folder** for all Wide-phase content (character, location, faction, event, concept, story). Root holds project/reference docs.
- Root doc types: `project` (worldbuilding-plan.md, seed.md, log.md), `reference` (agent-context.md)
- Universal frontmatter: type, status, aliases, last_updated; type-specific fields use [[wikilinks]] for queryable categories
- `last_updated` format: `YYYY-MM-DD HH:mm` (frontmatter-modified-date plugin pre-installed in vault template, not yet enabled)
- "For future agents" preamble on every note body (2–3 sentences) — model-agnostic phrasing
- Lorebook dissolved: world knowledge lives in concept notes; ainime export skill packages them as lorebook entries
- Influence thresholds replaced by Relationship Behavior (prose description, no numbered bands)
- Introduction = separate story note (scope: "[[introduction]]"), not a character note section
- Story notes use hierarchy (up: link); scope field: direction | arc | intention | introduction
- Layer classification (surface/mid/deep) lives as frontmatter on concept notes
- Character note is comprehensive single source of truth; card is derived by export skill
- Bases use standalone `.base` files in `_bases/`; Home.md embeds with `![[filename.base]]`

## Implementation state

### Done
- ADR-0002 marked superseded; ADR-0003 written (platform decoupling)
- `worldbuilder-world-foundation` updated: seed produces `seed.md` (platform-agnostic)
- `worldbuilder-world-planning` updated: phase table, cast planning, export routing
- `worldbuilder-lorebook` updated: reframed as concept note creation skill
- `worldbuilder-calendar` updated: events/ → notes/; concept note guidance
- `worldbuilder-story-direction` updated: story/ → notes/; concept note guidance
- CONTEXT.md rewritten: flat notes/ structure, project/reference types, YYYY-MM-DD HH:mm format
- docs/agents/domain.md updated
- docs/target-system.md updated
- `worldbuilder-character-blueprint` rewritten: preamble/concept/inspirations/design notes; Relationship Behavior; intro removed; Lorebook Candidates removed
- `worldbuilder-location-blueprint` written to character system depth
- `worldbuilder-faction-blueprint` written to character system depth
- `worldbuilder-setup` skill created: copies worldvault template, asks for project name, hands off to world-planning
- `worldvault/` template created:
  - `.obsidian/` config (alwaysUpdateLinks, backlinks, templates → `_templates/`, all relevant core plugins, Bases enabled)
  - `frontmatter-modified-date` community plugin pre-installed (not yet enabled)
  - `_templates/` with 5 note templates (character, location, faction, concept, story)
  - `_bases/` with 7 Bases files (all-notes, characters, locations, factions, concepts, story, project-docs)
  - `Home.md` Bases dashboard (Project → All Notes → type sections)
  - Stub notes with frontmatter: worldbuilding-plan.md (type: project), seed.md (type: project), log.md (type: project), agent-context.md (type: reference)
  - Single `notes/` content folder
- Folder reference cascade: worldbuilder-world-planning, worldbuilder-ainime-export, worldbuilder-lorebook, worldbuilder-story-direction, worldbuilder-calendar all updated from type-specific folders → `notes/`
- `docs/restructure-notes.md`: full pass complete — old folder structure replaced with flat `notes/` decision; `last_updated` format fixed to `YYYY-MM-DD HH:mm`; roster reference updated
- `worldbuilder-world-planning`: phases 2d (Location notes) and 2e (Faction notes) added; old 2d→2f (Cast planning), 2e→2g (Character notes); dependency diagram and parallel execution updated
- `worldbuilder-character-blueprint`: four writing rules incorporated — plain/concrete language (Anglo-Saxon over Latinate), positive statements, starting-state-only rule, relationship POV; self-check updated

### Next
- Enable and configure frontmatter-modified-date plugin: set format to `YYYY-MM-DD HH:mm` in plugin settings

## Key files
- `docs/restructure-notes.md` — full architecture decisions and rationale (may have stale folder structure)
- `docs/target-system.md` — ainime-games field reference (export skill uses this)
- `skills/worldbuilder-setup/worldvault/` — vault template; canonical source for project structure
- `skills/worldbuilder-setup/SKILL.md` — setup skill

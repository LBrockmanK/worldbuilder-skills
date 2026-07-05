---
type: spec
title: "Design: worldvault Template and worldbuilder-setup Skill"
description: Design for the pre-configured worldvault Obsidian vault template and the worldbuilder-setup skill that installs it into new projects.
tags: [complete]
date: 2026-05-28
timestamp: 2026-05-28T17:10
resources: []
---
# Design: worldvault Template and worldbuilder-setup Skill

**Date:** 2026-05-28
**Status:** Approved

---

## Overview

Two deliverables:

1. **`worldvault/`** — a pre-configured Obsidian vault template that ships inside the setup skill directory. Contains folder structure, `.obsidian/` config, stub notes, note templates, and agent reference documentation.

2. **`worldbuilder-setup`** — a new skill that copies `worldvault/` into a user's working directory, asks a small number of infrastructure questions, and hands off to `worldbuilder-world-planning`.

This is the entry point for all new projects. Run once per project.

---

## Architecture

The vault template lives at `skills/worldbuilder-setup/worldvault/`. It is a self-contained initialization package — copying it into a working directory produces a functional, immediately usable Obsidian vault. No post-copy configuration is required.

The setup skill is the only consumer of `worldvault/`. Once copied, the vault is owned by the project, not by the skill set. Users may edit vault contents (including reference docs) without creating conflicts with future skill updates.

---

## Deliverable 1: `worldbuilder-setup` skill

### Trigger

Use when starting a new worldbuilding project from scratch. Runs once, before any other worldbuilder skill.

### Steps

1. **Copy `worldvault/`** — copy all contents of `skills/worldbuilder-setup/worldvault/` into the user's designated project vault directory (a new, empty folder they specify). Preserve the `.obsidian/` directory and all folder structure.

2. **Ask infrastructure questions** — minimal set of questions about project configuration, not creative decisions. The one confirmed question is project/world name (written into `worldbuilding-plan.md`). Additional questions to be added as the skill matures.

3. **Hand off** — confirm the workspace is ready and direct the user to `worldbuilder-world-planning` to begin the Seed phase.

### What this skill does not do

- No creative questions — genre, tone, setting, cast. Those belong in world-planning and world-foundation.
- No Obsidian Sync configuration — user decision, handled manually.
- No plugin installation — no community plugins at this stage (see Community Plugins below).

---

## Deliverable 2: `worldvault/`

### Location

`skills/worldbuilder-setup/worldvault/`

### Folder structure

```
worldvault/
├── .obsidian/              ← pre-configured Obsidian settings (copy as-is)
├── characters/             ← character notes (Wide phase)
├── locations/              ← location notes (Wide phase)
├── factions/               ← faction/household/organization notes (Wide phase)
├── concepts/               ← world knowledge notes (Wide phase)
├── story/                  ← direction, arc, intention, introduction notes
├── _templates/             ← note templates for human users
├── _attachments/           ← pasted media; Obsidian attachment folder target
├── Home.md                 ← Bases dashboard
├── worldbuilding-plan.md   ← project plan stub
├── log.md                  ← retcon and change log stub
├── seed.md                 ← world foundation stub (filled by world-foundation skill)
└── agent-context.md        ← compact reference for agents (user-editable)
```

No `events/` folder — narrative beats use `story/` notes; recurring cultural events use `concept/` notes.

### `.obsidian/` configuration

Pre-configured; copies as-is. Key settings:

- `alwaysUpdateLinks: true` — wikilinks auto-update when notes are renamed
- `attachmentFolderPath: "_attachments"` — pasted media goes to `_attachments/`
- `backlinkInDocument: true` — backlinks visible inline at note bottom
- Templates plugin folder: `_templates`
- Bases: enabled
- Core plugins: file-explorer, global-search, switcher, graph, backlink, canvas, outgoing-link, tag-pane, properties, page-preview, templates, note-composer, command-palette, editor-status, bookmarks, file-recovery, bases

No community plugins at this stage. **Obsidian-TTRPG-Community/Relations** is a candidate for a future iteration — it visualizes typed frontmatter relationships and supports custom relationship types — but is deferred because our relationship descriptions live in prose rather than frontmatter labels.

### Stub notes

**`worldbuilding-plan.md`** — project plan. Header with project name placeholder (filled by setup skill), phase tracking table, cast plan section. Body filled by `worldbuilder-world-planning`.

**`log.md`** — retcon and change log. Header only. Entries appended during development as canon shifts.

**`seed.md`** — world foundation. Header only. Body produced by `worldbuilder-world-foundation`.

**`agent-context.md`** — compact reference for agents working in the vault. Contains: note type schema (all types with required frontmatter fields), vocabulary (key terms from CONTEXT.md), skill routing (which skill handles which note type). User-editable — agents should read this note at the start of any vault session. Not a worldbuilding note; lives at vault root rather than in a content folder.

### `Home.md` — Bases dashboard

Single note at vault root. Contains one Base per note type, each with three views:

| View | Filter |
|---|---|
| All | No filter (default) |
| Draft | status = draft |
| Complete | status = complete |

**Per-type columns:**

| Base | Columns |
|---|---|
| Characters | name, status, role, archetype, factions, last_updated |
| Locations | name, status, region, function, last_updated |
| Factions | name, status, function, last_updated |
| Concepts | name, status, layer, last_updated |
| Story | name, status, scope, last_updated |

All views sorted by `last_updated` descending.

A summary Base at the top of the page shows all note types together: name, type, status, last_updated. Default view: All; additional views for Draft and Complete.

### `_templates/`

Six templates. Each contains the correct YAML frontmatter for its type and H2 section headers from the relevant skill. Frontmatter values are placeholders (blank or `YYYY-MM-DD`). Section bodies contain a single placeholder line so the structure is immediately visible.

**`character.md`**
```yaml
---
type: character
status: draft
aliases: []
last_updated: YYYY-MM-DD
factions: []
role: 
archetype: 
---
```
Sections: Preamble, Concept, Inspirations, Design Notes, Foundation, Behavioral Descriptions, Relationships, Relationship Behavior, Appearance, Storylines

**`location.md`**
```yaml
---
type: location
status: draft
aliases: []
last_updated: YYYY-MM-DD
region: 
function: 
primary-characters: []
---
```
Sections: Preamble, Concept, Physical Form, Social Life, Behavioral Register, History & Meaning

**`faction.md`**
```yaml
---
type: faction
status: draft
aliases: []
last_updated: YYYY-MM-DD
members: []
function: 
---
```
Sections: Preamble, Concept, Origin & Purpose, Collective Behavior, Membership, Inter-Faction Web, Storylines

**`concept.md`**
```yaml
---
type: concept
status: draft
aliases: []
last_updated: YYYY-MM-DD
layer: 
trigger-context: 
---
```
Sections: Preamble, Limitations and Costs, Content

**`story.md`**
```yaml
---
type: story
status: draft
aliases: []
last_updated: YYYY-MM-DD
up: 
scope: 
---
```
Sections: Preamble, Content

An inline comment immediately below the frontmatter lists which H2 sections apply per scope value (direction / arc / intention / introduction) and references the `worldbuilder-story-direction` skill for guidance. The comment is plain text in the template body, visible when the template is inserted.

**`worldbuilding-plan.md`** — not a content note template; the stub at vault root serves as its own template.

---

## What This Does Not Change

- `worldbuilder-world-planning` — no changes; setup hands off to it
- `worldbuilder-world-foundation` — no changes; fills `seed.md` stub
- All other skills — unchanged
- `CONTEXT.md` — the `events/` folder and event note type remain documented as valid; they are simply not included in the vault template at this stage

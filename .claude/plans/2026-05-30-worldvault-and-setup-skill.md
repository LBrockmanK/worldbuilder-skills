---
type: plan
title: worldvault Template & worldbuilder-setup Skill Implementation Plan
description: Implementation plan for building the worldvault Obsidian vault template and the worldbuilder-setup skill that copies it into new projects.
tags: [complete]
date: 2026-05-30
timestamp: 2026-05-30T17:10
resources: []
---
# worldvault Template & worldbuilder-setup Skill Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the `worldvault/` vault template and `worldbuilder-setup` skill — the entry point for all new worldbuilding projects.

**Architecture:** The vault template lives at `skills/worldbuilder-setup/worldvault/`; copying it into a project directory produces a fully configured Obsidian vault with the correct folder structure, pre-built Bases dashboard, note templates, and an agent reference doc. The `worldbuilder-setup` skill orchestrates the copy, asks for a project name, and hands off to `worldbuilder-world-planning`. A partial skeleton (`Vault/`) was created in a prior session at the repo root — this plan relocates it to the correct path and completes the remaining files.

**Tech Stack:** Markdown, YAML frontmatter, Obsidian (`.obsidian/` JSON config, Bases code blocks in `base` fences)

---

## File Map

```
skills/worldbuilder-setup/
├── SKILL.md                                      ← Task 7: new skill
└── worldvault/
    ├── .obsidian/                                ← Task 1: move from Vault/.obsidian/
    │   ├── app.json
    │   ├── appearance.json
    │   ├── backlink.json
    │   ├── core-plugins.json
    │   ├── templates.json
    │   └── workspace.json
    ├── characters/.gitkeep                       ← Task 2
    ├── locations/.gitkeep                        ← Task 2
    ├── factions/.gitkeep                         ← Task 2
    ├── concepts/.gitkeep                         ← Task 2
    ├── story/.gitkeep                            ← Task 2
    ├── _attachments/.gitkeep                     ← Task 2
    ├── _templates/                               ← Task 3
    │   ├── character.md
    │   ├── location.md
    │   ├── faction.md
    │   ├── concept.md
    │   └── story.md
    ├── worldbuilding-plan.md                     ← Task 4
    ├── log.md                                    ← Task 4
    ├── seed.md                                   ← Task 4
    ├── agent-context.md                          ← Task 5
    └── Home.md                                   ← Task 6
```

Delete: `Vault/` at repo root (untracked — Task 1)

---

## Task 1: Relocate vault skeleton to correct path

**Files:**
- Create: `skills/worldbuilder-setup/worldvault/.obsidian/app.json`
- Create: `skills/worldbuilder-setup/worldvault/.obsidian/appearance.json`
- Create: `skills/worldbuilder-setup/worldvault/.obsidian/backlink.json`
- Create: `skills/worldbuilder-setup/worldvault/.obsidian/core-plugins.json`
- Create: `skills/worldbuilder-setup/worldvault/.obsidian/templates.json`
- Create: `skills/worldbuilder-setup/worldvault/.obsidian/workspace.json`
- Delete: `Vault/` (entire directory — untracked, safe to remove)

- [ ] **Step 1: Create the skill and worldvault directories**

```powershell
New-Item -ItemType Directory -Force "skills/worldbuilder-setup/worldvault/.obsidian"
```

- [ ] **Step 2: Create app.json**

Create `skills/worldbuilder-setup/worldvault/.obsidian/app.json`:
```json
{
  "alwaysUpdateLinks": true,
  "showUnsupportedFiles": true,
  "attachmentFolderPath": "_attachments"
}
```

- [ ] **Step 3: Create appearance.json**

Create `skills/worldbuilder-setup/worldvault/.obsidian/appearance.json`:
```json
{}
```

- [ ] **Step 4: Create backlink.json**

Create `skills/worldbuilder-setup/worldvault/.obsidian/backlink.json`:
```json
{
  "backlinkInDocument": true
}
```

- [ ] **Step 5: Create core-plugins.json**

Create `skills/worldbuilder-setup/worldvault/.obsidian/core-plugins.json`:
```json
{
  "file-explorer": true,
  "global-search": true,
  "switcher": true,
  "graph": true,
  "backlink": true,
  "canvas": true,
  "outgoing-link": true,
  "tag-pane": true,
  "footnotes": false,
  "properties": true,
  "page-preview": true,
  "daily-notes": false,
  "templates": true,
  "note-composer": true,
  "command-palette": true,
  "slash-command": false,
  "editor-status": true,
  "bookmarks": true,
  "markdown-importer": false,
  "zk-prefixer": false,
  "random-note": false,
  "outline": true,
  "word-count": true,
  "slides": false,
  "audio-recorder": false,
  "workspaces": false,
  "file-recovery": true,
  "publish": false,
  "sync": false,
  "bases": true,
  "webviewer": false
}
```

- [ ] **Step 6: Create templates.json**

Create `skills/worldbuilder-setup/worldvault/.obsidian/templates.json`:
```json
{
  "folder": "_templates"
}
```

- [ ] **Step 7: Create workspace.json**

Create `skills/worldbuilder-setup/worldvault/.obsidian/workspace.json`:
```json
{
  "main": {
    "id": "main-split",
    "type": "split",
    "children": [
      {
        "id": "main-tabs",
        "type": "tabs",
        "children": [
          {
            "id": "home-leaf",
            "type": "leaf",
            "state": {
              "type": "markdown",
              "state": {
                "file": "Home.md",
                "mode": "preview"
              }
            }
          }
        ]
      }
    ],
    "direction": "vertical"
  },
  "left": {
    "id": "left-split",
    "type": "split",
    "children": [
      {
        "id": "left-tabs",
        "type": "tabs",
        "children": [
          {
            "id": "file-explorer-leaf",
            "type": "leaf",
            "state": {
              "type": "file-explorer",
              "state": { "sortOrder": "alphabetical" }
            }
          },
          {
            "id": "search-leaf",
            "type": "leaf",
            "state": {
              "type": "search",
              "state": { "query": "" }
            }
          },
          {
            "id": "bookmarks-leaf",
            "type": "leaf",
            "state": {
              "type": "bookmarks",
              "state": {}
            }
          }
        ]
      }
    ],
    "direction": "horizontal",
    "width": 300
  },
  "right": {
    "id": "right-split",
    "type": "split",
    "children": [
      {
        "id": "right-tabs",
        "type": "tabs",
        "children": [
          {
            "id": "backlink-leaf",
            "type": "leaf",
            "state": {
              "type": "backlink",
              "state": { "backlinkCollapsed": false, "unlinkedCollapsed": true }
            }
          },
          {
            "id": "outgoing-link-leaf",
            "type": "leaf",
            "state": {
              "type": "outgoing-link",
              "state": { "linksCollapsed": false, "unlinkedCollapsed": true }
            }
          },
          {
            "id": "tag-leaf",
            "type": "leaf",
            "state": {
              "type": "tag",
              "state": { "sortOrder": "frequency" }
            }
          }
        ]
      }
    ],
    "direction": "horizontal",
    "width": 300,
    "collapsed": true
  },
  "left-ribbon": {
    "hiddenItems": {
      "switcher:Open quick switcher": false,
      "graph:Open graph view": false,
      "canvas:Create new canvas": false,
      "bases:Create new base": false,
      "command-palette:Open command palette": false
    }
  },
  "active": "file-explorer-leaf",
  "lastOpenFiles": ["Home.md"]
}
```

- [ ] **Step 8: Verify all 6 .obsidian files exist**

```powershell
Get-ChildItem "skills/worldbuilder-setup/worldvault/.obsidian"
```
Expected: 6 files listed — `app.json`, `appearance.json`, `backlink.json`, `core-plugins.json`, `templates.json`, `workspace.json`

- [ ] **Step 9: Delete mislocated Vault/ from repo root**

```powershell
Remove-Item -Recurse -Force "Vault"
```

- [ ] **Step 10: Verify Vault/ is gone**

```powershell
Test-Path "Vault"
```
Expected: `False`

- [ ] **Step 11: Commit**

```bash
git add skills/worldbuilder-setup/worldvault/.obsidian/
git commit -m "feat: add worldbuilder-setup skill skeleton with .obsidian config"
```

---

## Task 2: Create content folders

**Files:**
- Create: `skills/worldbuilder-setup/worldvault/characters/.gitkeep`
- Create: `skills/worldbuilder-setup/worldvault/locations/.gitkeep`
- Create: `skills/worldbuilder-setup/worldvault/factions/.gitkeep`
- Create: `skills/worldbuilder-setup/worldvault/concepts/.gitkeep`
- Create: `skills/worldbuilder-setup/worldvault/story/.gitkeep`
- Create: `skills/worldbuilder-setup/worldvault/_attachments/.gitkeep`

- [ ] **Step 1: Create all 6 empty .gitkeep files**

Create each of these files with empty content (0 bytes):
- `skills/worldbuilder-setup/worldvault/characters/.gitkeep`
- `skills/worldbuilder-setup/worldvault/locations/.gitkeep`
- `skills/worldbuilder-setup/worldvault/factions/.gitkeep`
- `skills/worldbuilder-setup/worldvault/concepts/.gitkeep`
- `skills/worldbuilder-setup/worldvault/story/.gitkeep`
- `skills/worldbuilder-setup/worldvault/_attachments/.gitkeep`

- [ ] **Step 2: Verify folder structure**

```powershell
Get-ChildItem -Recurse "skills/worldbuilder-setup/worldvault" -Filter ".gitkeep"
```
Expected: 6 `.gitkeep` files listed

- [ ] **Step 3: Commit**

```bash
git add skills/worldbuilder-setup/worldvault/characters/ skills/worldbuilder-setup/worldvault/locations/ skills/worldbuilder-setup/worldvault/factions/ skills/worldbuilder-setup/worldvault/concepts/ skills/worldbuilder-setup/worldvault/story/ skills/worldbuilder-setup/worldvault/_attachments/
git commit -m "feat: add worldvault content folder structure"
```

---

## Task 3: Create note templates

**Files:**
- Create: `skills/worldbuilder-setup/worldvault/_templates/character.md`
- Create: `skills/worldbuilder-setup/worldvault/_templates/location.md`
- Create: `skills/worldbuilder-setup/worldvault/_templates/faction.md`
- Create: `skills/worldbuilder-setup/worldvault/_templates/concept.md`
- Create: `skills/worldbuilder-setup/worldvault/_templates/story.md`

- [ ] **Step 1: Create character.md template**

Create `skills/worldbuilder-setup/worldvault/_templates/character.md`:
```markdown
---
type: character
status: draft
aliases: []
last_updated: YYYY-MM-DD
factions: []
role: 
archetype: 
---

> For future Claude: this is a character note. The filename is the character's name. Use `worldbuilder-character-blueprint` to build it out.

## Preamble

_2–3 sentences orienting a future agent to this character._

## Concept

_What this character is and their core dramatic function._

## Inspirations

_Named references that calibrate tone and behavior._

## Design Notes

_Open constraints, outstanding questions, decisions to revisit._

## Foundation

_Background, history, how they got here._

## Behavioral Descriptions

_How they act, what they want, their voice._

## Relationships

_Who they are connected to and how._

## Relationship Behavior

_How they behave with the player as trust and intimacy grow._

## Appearance

_Physical description._

## Storylines

_Story arcs and participation._
```

- [ ] **Step 2: Create location.md template**

Create `skills/worldbuilder-setup/worldvault/_templates/location.md`:
```markdown
---
type: location
status: draft
aliases: []
last_updated: YYYY-MM-DD
region: 
function: 
primary-characters: []
---

> For future Claude: this is a location note. The filename is the location's name. Use `worldbuilder-location-blueprint` to build it out.

## Preamble

_2–3 sentences orienting a future agent to this location._

## Concept

_What this place is and why it matters._

## Physical Form

_What it looks, sounds, smells like._

## Social Life

_Who inhabits it, how they use it._

## Behavioral Register

_The emotional and dramatic register of this space._

## History & Meaning

_How this place came to be and what it represents._
```

- [ ] **Step 3: Create faction.md template**

Create `skills/worldbuilder-setup/worldvault/_templates/faction.md`:
```markdown
---
type: faction
status: draft
aliases: []
last_updated: YYYY-MM-DD
members: []
function: 
---

> For future Claude: this is a faction note. The filename is the faction's name. Use `worldbuilder-faction-blueprint` to build it out.

## Preamble

_2–3 sentences orienting a future agent to this faction._

## Concept

_What this faction is and its role in the world._

## Origin & Purpose

_How and why this faction formed._

## Collective Behavior

_How the faction acts as a group._

## Membership

_Who belongs, how membership works._

## Inter-Faction Web

_Relationships to other factions._

## Storylines

_Faction-level story participation._
```

- [ ] **Step 4: Create concept.md template**

Create `skills/worldbuilder-setup/worldvault/_templates/concept.md`:
```markdown
---
type: concept
status: draft
aliases: []
last_updated: YYYY-MM-DD
layer: 
trigger-context: 
---

> For future Claude: this is a concept note — a discrete piece of world knowledge. Layer values: `[[surface]]` (freely shareable), `[[mid]]` (contextual), `[[deep]]` (revealed late). Aliases become lorebook keyword candidates at export. Use `worldbuilder-lorebook` to build it out.

## Preamble

_2–3 sentences orienting a future agent to this concept._

## Limitations and Costs

_Constraints, exceptions, or costs that apply to this concept._

## Content

_The actual world knowledge: what this thing is, how it works._
```

- [ ] **Step 5: Create story.md template**

Create `skills/worldbuilder-setup/worldvault/_templates/story.md`:
```markdown
---
type: story
status: draft
aliases: []
last_updated: YYYY-MM-DD
up: 
scope: 
---

Scope values: `[[direction]]` (top-level creative brief), `[[arc]]` (major story section), `[[intention]]` (specific story possibility), `[[introduction]]` (first player–character contact). Set the `up:` field to the parent note for arc, intention, and introduction notes; leave blank on direction notes. See `worldbuilder-story-direction` for guidance on which sections to include per scope.

> For future Claude: this is a story note. Use `worldbuilder-story-direction` to build it out.

## Preamble

_2–3 sentences orienting a future agent to this story note._

## Content

_Narrative content appropriate to scope._
```

- [ ] **Step 6: Verify templates exist**

```powershell
Get-ChildItem "skills/worldbuilder-setup/worldvault/_templates"
```
Expected: 5 files — `character.md`, `concept.md`, `faction.md`, `location.md`, `story.md`

- [ ] **Step 7: Commit**

```bash
git add skills/worldbuilder-setup/worldvault/_templates/
git commit -m "feat: add worldvault note templates for all 5 content types"
```

---

## Task 4: Create stub notes

**Files:**
- Create: `skills/worldbuilder-setup/worldvault/worldbuilding-plan.md`
- Create: `skills/worldbuilder-setup/worldvault/log.md`
- Create: `skills/worldbuilder-setup/worldvault/seed.md`

- [ ] **Step 1: Create worldbuilding-plan.md**

Create `skills/worldbuilder-setup/worldvault/worldbuilding-plan.md`:
```markdown
# {{PROJECT_NAME}} — Worldbuilding Plan

> For future Claude: this is the project plan. Read it at the start of every session. The `worldbuilder-world-planning` skill maintains it. Do not modify the phase table or cast plan except through that skill.

## Phase Status

| Phase | Status | Notes |
|---|---|---|
| Seed | Not started | |
| Wide | Not started | |
| Export | Not started | |

## Cast Plan

_To be filled by `worldbuilder-world-planning` during Wide phase setup._
```

- [ ] **Step 2: Create log.md**

Create `skills/worldbuilder-setup/worldvault/log.md`:
```markdown
# Retcon & Change Log

> For future Claude: append to this log whenever established canon changes. Format: date, what changed, why. Most recent entry at top.

<!-- entries appended here -->
```

- [ ] **Step 3: Create seed.md**

Create `skills/worldbuilder-setup/worldvault/seed.md`:
```markdown
# World Foundation

> For future Claude: this is `seed.md` — the world foundation document produced by `worldbuilder-world-foundation` during the Seed phase. Do not write to this file directly; let the skill generate it.
```

- [ ] **Step 4: Verify stubs exist**

```powershell
Get-ChildItem "skills/worldbuilder-setup/worldvault" -File
```
Expected: `Home.md` absent (not yet), `worldbuilding-plan.md`, `log.md`, `seed.md` present

- [ ] **Step 5: Commit**

```bash
git add skills/worldbuilder-setup/worldvault/worldbuilding-plan.md skills/worldbuilder-setup/worldvault/log.md skills/worldbuilder-setup/worldvault/seed.md
git commit -m "feat: add worldvault stub notes (worldbuilding-plan, log, seed)"
```

---

## Task 5: Create agent-context.md

**Files:**
- Create: `skills/worldbuilder-setup/worldvault/agent-context.md`

- [ ] **Step 1: Create agent-context.md**

Create `skills/worldbuilder-setup/worldvault/agent-context.md`:

````markdown
# Agent Context

> Read this note at the start of any vault session. It is a compact operational reference — not a worldbuilding note. User-editable.

---

## Note Type Schema

All notes carry universal frontmatter plus type-specific fields.

**Universal (all types):**
```yaml
type: character | location | faction | event | concept | story
status: draft | complete
aliases: []
last_updated: YYYY-MM-DD
```

**Character** — `characters/`
```yaml
factions: ["[[Household Name]]"]
role: plain text
archetype: "[[Initially Hostile]]"
```
Sections: Preamble, Concept, Inspirations, Design Notes, Foundation, Behavioral Descriptions, Relationships, Relationship Behavior, Appearance, Storylines

**Location** — `locations/`
```yaml
region: "[[The Valley]]"
function: one phrase
primary-characters: ["[[Name]]"]
```
Sections: Preamble, Concept, Physical Form, Social Life, Behavioral Register, History & Meaning

**Faction** — `factions/`
```yaml
members: ["[[Name]]"]
function: one phrase
```
Sections: Preamble, Concept, Origin & Purpose, Collective Behavior, Membership, Inter-Faction Web, Storylines

**Concept** — `concepts/`
```yaml
layer: "[[surface]]"        # surface | mid | deep
trigger-context: brief plain text
```
Sections: Preamble, Limitations and Costs, Content

**Story** — `story/`
```yaml
up: "[[parent-story-note]]"     # absent on top-level direction note
scope: "[[direction]]" | "[[arc]]" | "[[intention]]" | "[[introduction]]"
```
Sections: Preamble, Content

**Link convention:** Anything that represents a category, entity, or concept worth filtering by uses a `[[wikilink]]`. Operational fields (`status`, `last_updated`, booleans) use plain values.

---

## Vocabulary

**Seed phase** — Clarification-heavy opening phase. Produces `seed.md`. _Avoid: Foundation phase, setup phase._

**Wide phase** — Expansive generative phase. Produces all character, location, faction, concept, and story notes. _Avoid: Development phase._

**Export phase** — Conversion phase. Packages Wide-phase notes into the target system format. The only phase that writes ainime field names. _Avoid: Deliverables phase._

**seed.md** — World foundation document. Plain prose with natural section headers. Not written in export format.

**Character note** — Comprehensive single source of truth for one character. Richer than any export format.

**Concept note** — A discrete piece of world knowledge in `concepts/`. Layer-tagged: surface (freely shareable), mid (contextual), deep (revealed late).

**Story note** — Narrative direction document in `story/`. Scope hierarchy: direction → arc → intention. Introduction notes have `scope: "[[introduction]]"`.

**Cast planning** — Wide-phase process of planning the full cast before writing individual notes. Produces the cast plan in `worldbuilding-plan.md`.

**Coverage check** — Pre-completion review: main/side ratio, household balance, archetype slot coverage, negative-track characters present.

---

## Skill Routing

| Task | Skill |
|---|---|
| New project setup | `worldbuilder-setup` (once only, then world-planning) |
| Session start / phase routing | `worldbuilder-world-planning` |
| Seed phase / world foundation | `worldbuilder-world-foundation` |
| Character notes | `worldbuilder-character-blueprint` |
| Location notes | `worldbuilder-location-blueprint` |
| Faction notes | `worldbuilder-faction-blueprint` |
| Concept notes | `worldbuilder-lorebook` |
| Story notes | `worldbuilder-story-direction` |
| Ingest existing material | `worldbuilder-ingestion` |
| Export to target system | `worldbuilder-ainime-export` |
````

- [ ] **Step 2: Verify agent-context.md exists and is non-empty**

```powershell
(Get-Item "skills/worldbuilder-setup/worldvault/agent-context.md").Length
```
Expected: non-zero byte count (file is ~2 KB)

- [ ] **Step 3: Commit**

```bash
git add skills/worldbuilder-setup/worldvault/agent-context.md
git commit -m "feat: add agent-context.md reference doc to worldvault"
```

---

## Task 6: Create Home.md Bases dashboard

**Files:**
- Create: `skills/worldbuilder-setup/worldvault/Home.md`

Home.md contains embedded Obsidian Bases using `base` code fences — one per note type plus a summary base at the top. Each base has three views (All, Draft, Complete), all sorted by `last_updated` descending.

**Note on Bases syntax:** The JSON shown follows the Obsidian Bases v1 embedded schema. After opening the vault in Obsidian (1.8+), verify each base renders its table correctly. If a base shows an error, open it in the Bases editor to inspect and adjust.

- [ ] **Step 1: Create Home.md**

Create `skills/worldbuilder-setup/worldvault/Home.md`. The file content contains six `base` code fences. Each fence is a JSON object — write the literal text shown below, preserving the triple-backtick fences:

````markdown
# {{PROJECT_NAME}}

> Project dashboard. Each section is a live Base — requires Obsidian 1.8+ with the Bases core plugin enabled.

---

## All Notes

```base
{
  "schemaVersion": "1",
  "columns": [
    { "id": "file-name", "field": "file.name", "type": "text" },
    { "id": "type", "field": "type", "type": "text" },
    { "id": "status", "field": "status", "type": "text" },
    { "id": "last_updated", "field": "last_updated", "type": "date" }
  ],
  "filters": {
    "conjunction": "AND",
    "conditions": []
  },
  "sort": [{ "field": "last_updated", "direction": "desc" }],
  "views": [
    { "id": "all", "name": "All", "type": "table" },
    {
      "id": "draft", "name": "Draft", "type": "table",
      "filters": {
        "conjunction": "AND",
        "conditions": [{ "field": "status", "operator": "eq", "value": "draft" }]
      }
    },
    {
      "id": "complete", "name": "Complete", "type": "table",
      "filters": {
        "conjunction": "AND",
        "conditions": [{ "field": "status", "operator": "eq", "value": "complete" }]
      }
    }
  ]
}
```

---

## Characters

```base
{
  "schemaVersion": "1",
  "columns": [
    { "id": "file-name", "field": "file.name", "type": "text" },
    { "id": "status", "field": "status", "type": "text" },
    { "id": "role", "field": "role", "type": "text" },
    { "id": "archetype", "field": "archetype", "type": "text" },
    { "id": "factions", "field": "factions", "type": "multitext" },
    { "id": "last_updated", "field": "last_updated", "type": "date" }
  ],
  "filters": {
    "conjunction": "AND",
    "conditions": [{ "field": "type", "operator": "eq", "value": "character" }]
  },
  "sort": [{ "field": "last_updated", "direction": "desc" }],
  "views": [
    { "id": "all", "name": "All", "type": "table" },
    {
      "id": "draft", "name": "Draft", "type": "table",
      "filters": {
        "conjunction": "AND",
        "conditions": [
          { "field": "type", "operator": "eq", "value": "character" },
          { "field": "status", "operator": "eq", "value": "draft" }
        ]
      }
    },
    {
      "id": "complete", "name": "Complete", "type": "table",
      "filters": {
        "conjunction": "AND",
        "conditions": [
          { "field": "type", "operator": "eq", "value": "character" },
          { "field": "status", "operator": "eq", "value": "complete" }
        ]
      }
    }
  ]
}
```

---

## Locations

```base
{
  "schemaVersion": "1",
  "columns": [
    { "id": "file-name", "field": "file.name", "type": "text" },
    { "id": "status", "field": "status", "type": "text" },
    { "id": "region", "field": "region", "type": "text" },
    { "id": "function", "field": "function", "type": "text" },
    { "id": "last_updated", "field": "last_updated", "type": "date" }
  ],
  "filters": {
    "conjunction": "AND",
    "conditions": [{ "field": "type", "operator": "eq", "value": "location" }]
  },
  "sort": [{ "field": "last_updated", "direction": "desc" }],
  "views": [
    { "id": "all", "name": "All", "type": "table" },
    {
      "id": "draft", "name": "Draft", "type": "table",
      "filters": {
        "conjunction": "AND",
        "conditions": [
          { "field": "type", "operator": "eq", "value": "location" },
          { "field": "status", "operator": "eq", "value": "draft" }
        ]
      }
    },
    {
      "id": "complete", "name": "Complete", "type": "table",
      "filters": {
        "conjunction": "AND",
        "conditions": [
          { "field": "type", "operator": "eq", "value": "location" },
          { "field": "status", "operator": "eq", "value": "complete" }
        ]
      }
    }
  ]
}
```

---

## Factions

```base
{
  "schemaVersion": "1",
  "columns": [
    { "id": "file-name", "field": "file.name", "type": "text" },
    { "id": "status", "field": "status", "type": "text" },
    { "id": "function", "field": "function", "type": "text" },
    { "id": "last_updated", "field": "last_updated", "type": "date" }
  ],
  "filters": {
    "conjunction": "AND",
    "conditions": [{ "field": "type", "operator": "eq", "value": "faction" }]
  },
  "sort": [{ "field": "last_updated", "direction": "desc" }],
  "views": [
    { "id": "all", "name": "All", "type": "table" },
    {
      "id": "draft", "name": "Draft", "type": "table",
      "filters": {
        "conjunction": "AND",
        "conditions": [
          { "field": "type", "operator": "eq", "value": "faction" },
          { "field": "status", "operator": "eq", "value": "draft" }
        ]
      }
    },
    {
      "id": "complete", "name": "Complete", "type": "table",
      "filters": {
        "conjunction": "AND",
        "conditions": [
          { "field": "type", "operator": "eq", "value": "faction" },
          { "field": "status", "operator": "eq", "value": "complete" }
        ]
      }
    }
  ]
}
```

---

## Concepts

```base
{
  "schemaVersion": "1",
  "columns": [
    { "id": "file-name", "field": "file.name", "type": "text" },
    { "id": "status", "field": "status", "type": "text" },
    { "id": "layer", "field": "layer", "type": "text" },
    { "id": "last_updated", "field": "last_updated", "type": "date" }
  ],
  "filters": {
    "conjunction": "AND",
    "conditions": [{ "field": "type", "operator": "eq", "value": "concept" }]
  },
  "sort": [{ "field": "last_updated", "direction": "desc" }],
  "views": [
    { "id": "all", "name": "All", "type": "table" },
    {
      "id": "draft", "name": "Draft", "type": "table",
      "filters": {
        "conjunction": "AND",
        "conditions": [
          { "field": "type", "operator": "eq", "value": "concept" },
          { "field": "status", "operator": "eq", "value": "draft" }
        ]
      }
    },
    {
      "id": "complete", "name": "Complete", "type": "table",
      "filters": {
        "conjunction": "AND",
        "conditions": [
          { "field": "type", "operator": "eq", "value": "concept" },
          { "field": "status", "operator": "eq", "value": "complete" }
        ]
      }
    }
  ]
}
```

---

## Story

```base
{
  "schemaVersion": "1",
  "columns": [
    { "id": "file-name", "field": "file.name", "type": "text" },
    { "id": "status", "field": "status", "type": "text" },
    { "id": "scope", "field": "scope", "type": "text" },
    { "id": "last_updated", "field": "last_updated", "type": "date" }
  ],
  "filters": {
    "conjunction": "AND",
    "conditions": [{ "field": "type", "operator": "eq", "value": "story" }]
  },
  "sort": [{ "field": "last_updated", "direction": "desc" }],
  "views": [
    { "id": "all", "name": "All", "type": "table" },
    {
      "id": "draft", "name": "Draft", "type": "table",
      "filters": {
        "conjunction": "AND",
        "conditions": [
          { "field": "type", "operator": "eq", "value": "story" },
          { "field": "status", "operator": "eq", "value": "draft" }
        ]
      }
    },
    {
      "id": "complete", "name": "Complete", "type": "table",
      "filters": {
        "conjunction": "AND",
        "conditions": [
          { "field": "type", "operator": "eq", "value": "story" },
          { "field": "status", "operator": "eq", "value": "complete" }
        ]
      }
    }
  ]
}
```
````

- [ ] **Step 2: Verify Home.md exists and is non-empty**

```powershell
(Get-Item "skills/worldbuilder-setup/worldvault/Home.md").Length
```
Expected: non-zero byte count (~5 KB)

- [ ] **Step 3: Commit**

```bash
git add skills/worldbuilder-setup/worldvault/Home.md
git commit -m "feat: add worldvault Home.md Bases dashboard"
```

---

## Task 7: Create worldbuilder-setup SKILL.md

**Files:**
- Create: `skills/worldbuilder-setup/SKILL.md`

- [ ] **Step 1: Create SKILL.md**

Create `skills/worldbuilder-setup/SKILL.md`:
```markdown
---
name: worldbuilder-setup
description: Use when starting a new worldbuilding project from scratch. Runs once, before any other worldbuilder skill. Copies the worldvault template into the user's project directory, asks for a project name, and hands off to worldbuilder-world-planning.
---

# Worldbuilder Setup

## Overview

This skill initializes a new worldbuilding project. It copies the pre-configured vault template into the user's designated project directory, writes in the project name, and hands off to `worldbuilder-world-planning`.

Run this skill once per project, before any other worldbuilder skill. It does not ask creative questions — genre, tone, cast, and setting all belong in world-planning and world-foundation.

---

## Steps

### Step 1: Identify the skill directory

The `worldvault/` folder that accompanies this skill file is the vault template. Locate it at the same directory level as this SKILL.md file.

### Step 2: Ask for the project directory

Ask:

> "Where should the project vault be created? Provide the full path to a new, empty folder — I'll copy the vault template there."

Wait for their answer. Confirm the target path either exists and is empty, or does not yet exist. If it does not exist, ask whether to create it.

### Step 3: Copy worldvault/ into the project directory

Copy all contents of `worldvault/` into the user's specified project directory. Preserve the full structure:
- `.obsidian/` and all files within
- Content folders: `characters/`, `locations/`, `factions/`, `concepts/`, `story/`
- `_templates/`, `_attachments/`
- All stub notes: `Home.md`, `worldbuilding-plan.md`, `log.md`, `seed.md`, `agent-context.md`

PowerShell:
```powershell
Copy-Item -Path "<skill-directory>/worldvault/*" -Destination "<project-directory>" -Recurse -Force
# Also copy hidden .obsidian directory explicitly:
Copy-Item -Path "<skill-directory>/worldvault/.obsidian" -Destination "<project-directory>/.obsidian" -Recurse -Force
```

Bash (macOS/Linux):
```bash
cp -r "<skill-directory>/worldvault/." "<project-directory>/"
```

### Step 4: Ask for project name

Ask:

> "What is the name of your world or project?"

Replace the `{{PROJECT_NAME}}` placeholder in two files in the project directory:

In `<project-directory>/worldbuilding-plan.md`, replace:
```
# {{PROJECT_NAME}} — Worldbuilding Plan
```
with:
```
# <ProjectName> — Worldbuilding Plan
```

In `<project-directory>/Home.md`, replace:
```
# {{PROJECT_NAME}}
```
with:
```
# <ProjectName>
```

### Step 5: Confirm and hand off

Confirm:

> "Your vault is ready at `<project-directory>`. Open it in Obsidian as a vault — use 'Open folder as vault' and point it to that folder. Then start with `worldbuilder-world-planning` to begin the Seed phase."

---

## What this skill does not do

- No creative questions. Genre, tone, setting, cast — those belong in world-planning and world-foundation.
- No Obsidian Sync configuration — user decision, handled manually.
- No plugin installation. No community plugins are included or required.
- No cloud integration. The vault is a local directory.
```

- [ ] **Step 2: Verify SKILL.md exists and is non-empty**

```powershell
(Get-Item "skills/worldbuilder-setup/SKILL.md").Length
```
Expected: non-zero byte count (~2 KB)

- [ ] **Step 3: Commit**

```bash
git add skills/worldbuilder-setup/SKILL.md
git commit -m "feat: add worldbuilder-setup skill"
```

---

## Self-Review Notes

- `{{PROJECT_NAME}}` placeholder appears in `worldbuilding-plan.md` and `Home.md`; SKILL.md Step 4 replaces both. ✅
- `.obsidian/` copy on PowerShell requires two `Copy-Item` calls because `-Force` on `*` glob skips hidden directories — SKILL.md calls both. ✅
- Bases `"field": "file.name"` used for the note name column in all bases — this is the Obsidian Bases convention for the note filename. ✅
- `_templates/` does not get a `.gitkeep` — it is populated by Task 3, so git tracks it through the template files. ✅
- `_attachments/` gets `.gitkeep` because it ships empty and must be tracked. ✅
- story.md template has the scope comment **immediately below frontmatter, before first H2** per spec. ✅
- No `events/` folder created — by design per spec. ✅
- Bases syntax note included in Task 6 — user should verify in Obsidian after first open. ✅

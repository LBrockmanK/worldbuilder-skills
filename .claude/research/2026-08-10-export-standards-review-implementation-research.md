---
type: research
title: Export-Standards Review Implementation Research
description: Implementation research for the keywords field and extraction reliability
  map. Covers concept template structure, OKF build process, keyword derivation, and
  target-system field inventory.
tags:
- complete
date: 2026-08-10
timestamp: 2026-08-10T02:41Z
resources:
- "[[2026-08-10-export-standards-review-keywords-field-and-extraction-reliability-map]]"
---

# Export-Standards Review Implementation Research

## Goals

Gather implementation facts for D1 (keywords field) and D2 (extraction
reliability map) from the approved spec.

## Results

**Concept note schema** (`defaults/okf.base.json`): concept type has
two type-specific fields: `layer` (text, required) and
`trigger-context` (text, optional). Universal fields include `tags`
(tags), `resources` (list), `aliases` (list). The `keywords` field
adds as `{type: "list", required: false}`.

**Template** (`defaults/templates/concept.md`): prose template with
frontmatter stubs. The `keywords` line goes after existing type-
specific fields.

**Build pipeline**: `python scripts/build-okf.py` reads
`defaults/okf.base.json` + `defaults/templates/*.md`, writes
`defaults/okf.json`. Template content is embedded in the output.

**Keyword derivation** (`skills/worldbuilder-ainime-export/SKILL.md`):
current process derives from `aliases` frontmatter + key terms in note
body. Syntax: single terms = OR, `keyword1+keyword2` = AND. The
keywords field would override this derivation when present.

**Target-system field inventory** (`docs/target-system.md`, 302 lines):
~40+ field paths across Setting, Adventure, Calendar, Lore, Characters,
Locations, Art Style tabs. Platform-managed fields: worldId, generated
images, UI theme, music, custom prompts. No existing extraction map.

## Consolidation

Two implementation tasks: (1) add `keywords` to concept schema and
template, rebuild OKF preset; (2) create extraction reliability map
in `docs/` alongside `target-system.md`.

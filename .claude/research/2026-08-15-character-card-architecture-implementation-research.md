---
type: research
title: Character card architecture — implementation research
description: 'Implementation context for the character card architecture plan: file
  geography, current skill structure, template mechanics, integration points.'
tags:
- complete
date: 2026-08-15
timestamp: 2026-08-15T13:05Z
resources: []
---

# Character card architecture — implementation research

## Files to change

**Create:**
- `skills/worldbuilder-character/card-format.md` — reference document
  defining blocks, entry structure, section-scoped writing rules.
  Replaces framework.md and generation-rules.md.

**Rewrite:**
- `skills/worldbuilder-character/SKILL.md` — currently 216 lines.
  Rewrite for conversational extraction workflow (D2).
- `defaults/templates/character.md` — update to new block model;
  retire Design Notes structured doctrine.

**Update:**
- `skills/worldbuilder-character/intimate.md` — add entry shape
  guidance (1-2 entries per coverage area, behavioral prose format).

**Retire:**
- `skills/worldbuilder-character/framework.md` — replaced by
  card-format.md.
- `skills/worldbuilder-character/generation-rules.md` — generation
  pipeline removed.

**Unchanged:**
- `skills/worldbuilder-character/relationships.md` — carries forward.
- `skills/writing-style.md` — carries forward.
- `scripts/build-okf.py` — re-run after template update.
- `defaults/okf.base.json` — unchanged.

## Current SKILL.md

216 lines. Session flow: Q&A before writing, one question at a
time, capture to Design Notes (Session Notes, Builder Context,
Structured Doctrine with 7 fields), then write sections. References
framework.md, generation-rules.md, intimate.md, relationships.md.
Self-check checklist at end.

## Build process

`build-okf.py` reads `okf.base.json`, inlines template content,
writes `okf.json`. Character type: `template_file: "character.md"`.

## Integration points

- SKILL.md references framework.md and generation-rules.md by name
- Template inlined by build-okf.py into okf.json
- writing-style.md referenced as governing document
- CONTEXT.md defines the character note type

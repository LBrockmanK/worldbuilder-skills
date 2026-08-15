---
type: research
title: Implementation Research — Card Format Amendments
description: File map and change points for implementing the Body appearance preamble
  and Story Beats addon block amendments.
tags:
- complete
date: 2026-08-15
timestamp: 2026-08-15T17:13Z
resources: []
---

# Implementation Research — Card Format Amendments

## File Map

| File | Change points |
|------|---------------|
| `skills/worldbuilder-character/card-format.md` | Body (23-33): add preamble. Addons (83-111): add Story Beats. Working-doc conventions: add exceptions |
| `skills/worldbuilder-character/SKILL.md` | Session Opening (32-41): Story Beats decision. Flow (44-69): Story Beats step. Checklist (137-150): add to enum. Story Notes (123-126): add boundary |
| `defaults/templates/character.md` | Body stub (21-25): preamble placeholder. Add Story Beats heading |
| `defaults/okf.base.json` | Regenerated via `python scripts/build-okf.py` |
| `skills/worldbuilder-ainime-export/card-assembly.md` | Future Storylines (91-101): consume Story Beats. Body prose (21): acknowledge preamble |
| `skills/worldbuilder-ainime-export/SKILL.md` | Story Beats export mapping |
| `extraction-reliability-map.md` | Does not exist; deferred |

## Notes

- No code; all changes are markdown content and one JSON regeneration
- `extraction-reliability-map.md` doesn't exist yet — creating it is out of scope for this plan; deferred to inbox
- Export SKILL.md appearance field (line 175) already draws from Body content — no change needed for D1

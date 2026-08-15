---
type: research
title: 'Implementation research: worldbuilder document review gate'
description: Implementation context for the review gate plan — skill structure, completion
  workflows, file conventions
tags:
- complete
date: 2026-08-15
timestamp: 2026-08-15T20:40Z
resources: []
---

# Implementation research: worldbuilder document review gate

## Goals

Implementation context for the review gate plan: skill structure,
completion workflows, shared resources, file conventions.

## Results

**Skill structure:** Skills use `SKILL.md` as the main instruction
file. Only `worldbuilder-character` has separate format docs
(card-format.md, relationships.md, intimate.md). Other entity skills
(concept, location, faction, event) embed everything in SKILL.md and
have no separate format documents.

**Completion workflow:** The character skill has a finalization gate
at `skills/worldbuilder-character/SKILL.md:163` with a completion
checklist ("Mark it `complete` when every item below passes"). The
relationships sub-doc has a separate pre-completion check at
`skills/worldbuilder-character/relationships.md:138`. card-format.md
defines a finalization gate at line 76-90 (required doctrine entries).

**Shared resources (all confirmed):**
- `docs/slop-phrases.md` — phrase-level review checklist
- `skills/writing-style.md` — prose doctrine
- `.claude/adr/0004-action-line-style-model.md` — action-line convention

**card-format.md section order:** Core block → Depth-of-access grid →
Required doctrine entries → Addon blocks → Section-scoped writing
rules → Working document conventions. Review criteria section goes
after Working document conventions (end of document).

**Other entity format docs:** None exist. Review criteria for other
entity types would go in their SKILL.md or in a new format doc when
created.

## Consolidation

The new skill (`skills/worldbuilder-review/SKILL.md`) follows the
established pattern. The first review criteria section goes in
card-format.md. Integration touches the character skill's completion
checklist. No code; all deliverables are instruction documents.

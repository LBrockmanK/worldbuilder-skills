---
type: research
title: Implementation Research — Source Ingestion Skill
description: File map and conventions for implementing the source ingestion skill.
tags:
- complete
date: 2026-08-15
timestamp: 2026-08-15T18:14Z
resources: []
---

# Implementation Research — Source Ingestion Skill

## Findings

- Target: create `skills/worldbuilder-source-ingestion/SKILL.md` (directory does not exist)
- Frontmatter pattern: `name: worldbuilder-source-ingestion`, `description: Use when...`
- Nine sibling skills follow `worldbuilder-` prefix convention
- Prose rules: `skills/writing-style.md` — stageable, present tense, no internal states
- scraibe:ingest override: use only for document creation (new_doc.py), skip judgment pass
- No other files needed — single SKILL.md creation

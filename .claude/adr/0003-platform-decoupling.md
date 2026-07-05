---
type: adr
title: Wide phase is platform-agnostic; only the Export phase targets a specific system
description: Decision that Phases 1 and 2 produce platform-agnostic notes and only the Export phase knows the target system's field names and format.
tags: [complete]
date: 2026-06-15
timestamp: 2026-06-15T17:10
resources: []
---
# Wide phase is platform-agnostic; only the Export phase targets a specific system

Phases 1 and 2 produce platform-agnostic notes. Phase 3 (Export) is the only phase that knows about the target system's field names and format.

The alternative — writing seed and Wide phase documents directly in ainime-games field format — was rejected because it couples the creative process to a single export target. Any change to that format, or any desire to target a different platform, requires reworking creative documents rather than just the export layer. The creative content and the export format are independent concerns and are treated as such.

**Supersedes ADR-0002**, which required the seed document to be written in ainime-games field format from day one.

## Implications

- `seed.md` is plain prose with natural section headers. The ainime export skill maps sections to fields.
- Character notes, concept notes, event notes, and story notes contain no JSON field names.
- `worldbuilder-ainime-export` is the only skill that writes `settingSummary`, `arcManagerGuidance`, `baseProfile`, `loreEntries`, `storyTriggers`, or any other ainime field name.
- Layer classification (`surface | mid | deep`) on concept notes is content metadata, not an ainime-specific concept — other export targets can use it differently.

## Considered Options

**Field-format documents throughout**: Write all documents in final target format from the start. Rejected — couples creative decisions to a single platform; format changes cascade everywhere.

**Export mapping file only (no skill)**: Maintain a mapping table and let users translate manually. Rejected — the translation work is non-trivial and error-prone; it belongs in a skill with clear guidance.

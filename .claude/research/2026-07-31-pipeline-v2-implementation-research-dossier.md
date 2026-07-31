---
type: research
title: Pipeline v2 Implementation Research Dossier
description: 'Implementation research for the Character Generation Pipeline v2 spec:
  file paths, current structures, integration points, test infrastructure, and open
  design questions for the planning phase.'
tags:
- complete
date: 2026-07-31
timestamp: 2026-07-31T00:45Z
resources:
- "[[2026-07-31-character-generation-pipeline-v2-input-restructuring-doctrine-additions-and-grader-agent]]"
---

# Pipeline v2 Implementation Research Dossier

## Key File Paths

| File | Role |
|------|------|
| `defaults/templates/character.md` | Design Notes template — gains 7 structured doctrine fields |
| `skills/worldbuilder-character/framework.md` | Coverage requirements — gains new Soul, Background, Relationships entries |
| `skills/worldbuilder-character/SKILL.md` | Skill entry point — Q&A flow, generation instructions |
| `skills/worldbuilder-character/relationships.md` | 12 archetypes — no changes |
| `defaults/okf.base.json` | OKF type definitions — no schema changes |
| `scripts/build-okf.py` | OKF builder — rerun after template changes |
| `docs/slop-phrases.md` | Stop-slop phrase list — prose format, 7 categories |
| `trials/2026-07-convergence-validation/detect_exact.py` | Sentence-level matching — reusable for input-echo detection |

## Current Structures

**Template** (`character.md`): Two H3 sections — Session Notes (Q&A capture) and Builder Context (narrative function, references). New structured fields go as a new subsection.

**Coverage requirements** (`framework.md`): Soul 3-5 psychological + 2-3 social + 1 boundary/pressure. Background fact pairs, no charge tags. Body physical behaviors, thin acceptable.

**Q&A flow** (`SKILL.md`): Embedded in skill, not separate. One question at a time, hypothesis-driven follow-up. Does not currently ask for the 7 new doctrine fields.

**Slop phrases** (`slop-phrases.md`): Prose checklist, not machine-readable. Needs wrapping for programmatic use.

**Detection scripts** (`detect_exact.py`): `strip_non_generated()` strips frontmatter and Design Notes. Reusable for input-echo detection.

**Test infrastructure**: pytest. Two existing test files (template generation, trial kit). No character-gen or slop-detection tests.

**Branch**: `convergence-validation-experiment`. Implementation needs new branch off master.

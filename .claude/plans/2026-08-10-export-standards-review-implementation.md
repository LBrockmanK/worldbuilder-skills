---
type: plan
title: Export-Standards Review Implementation
description: Implementation plan for the keywords field on concept notes and the extraction
  reliability map. 2 tasks.
tags:
- complete
date: 2026-08-10
timestamp: 2026-08-10T03:04Z
resources:
- "[[2026-08-10-export-standards-review-keywords-field-and-extraction-reliability-map]]"
- "[[2026-08-10-export-standards-review-implementation-research]]"
---

# Export-Standards Review Implementation

> **For agentic workers:** REQUIRED SUB-SKILL: Use core-workflow:subagent-driven-development (recommended) or core-workflow:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking. Execution requires the plan artifact's approval flip (see Approval Gate).

**Goal:** Add an optional `keywords` field to the concept note template and create an extraction reliability map classifying every ainime export field by derivation method.

**Architecture:** Two deliverables — a schema change with export-skill update (keywords field in okf.base.json + precedence rule in SKILL.md, propagated through the OKF build pipeline) and a reference document (a new markdown file in `docs/`). Task 1 must complete before Task 2, which reads the updated SKILL.md.

**Tech Stack:** Python (build-okf.py), YAML frontmatter, Markdown.

**Research dossier:** [Implementation Research](../research/2026-08-10-export-standards-review-implementation-research.md)

## Global Constraints

- Shipped content is model-neutral: never name a specific AI model in templates or skill instructions that reach end users.
- The OKF preset is generated: edit `defaults/okf.base.json` and `defaults/templates/*.md`, then run `python scripts/build-okf.py`. Never hand-edit `defaults/okf.json`.
- Extraction reliability map categories (structural, derived, constructed) are mutually exclusive. Classify at leaf-field granularity for compound fields.
- Map scope: fields the export workflow writes. Platform-managed fields (platform-assigned IDs, generated images, UI theme, music, custom prompts, publishing metadata) are out of scope. Exporter-constructed IDs (loreEntries[].id, storyTriggers[].id) are in scope.

---

### Task 1: Add keywords field to concept note schema and export skill

**Files:**
- Modify: `defaults/okf.base.json` (concept type field definitions)
- Modify: `skills/worldbuilder-ainime-export/SKILL.md` (keyword derivation instructions)
- Regenerate: `defaults/okf.json` (generated, via build-okf.py)

**Interfaces:**
- Consumes: existing concept type definition in okf.base.json; existing keyword derivation instructions in SKILL.md.
- Produces: `keywords` field available in concept note frontmatter; export skill instructs agents to prefer explicit keywords over derivation; OKF preset regenerated.

- [ ] **Step 1: Add keywords field to okf.base.json**

In `defaults/okf.base.json`, find the concept type's field definitions (after `trigger-context`). Add the keywords field:

```json
"keywords": {
  "type": "list",
  "required": false
}
```

- [ ] **Step 2: Update SKILL.md keyword derivation instructions**

In `skills/worldbuilder-ainime-export/SKILL.md`, find the Lorebook Entries section where keyword derivation is described. Add a paragraph before the existing derivation instructions:

```markdown
**Explicit keywords.** If a concept note has a non-empty `keywords`
frontmatter field, use those values directly as the entry's
`keywords[]`. Do not derive from aliases or body terms — the author
has specified the trigger words. When the field is absent or empty,
fall back to the derivation rules below.
```

- [ ] **Step 3: Rebuild the OKF preset**

```bash
python scripts/build-okf.py
```

Expected: script completes without error, `defaults/okf.json` is updated.

- [ ] **Step 4: Verify the generated preset includes the keywords field**

```bash
python -c "import json; d=json.load(open('defaults/okf.json')); fields=d['types']['concept']['fields']; print('keywords' in fields, fields.get('keywords'))"
```

Expected: `True {'type': 'list', 'required': False}`

- [ ] **Step 5: Verify SKILL.md precedence rule**

```bash
grep -A3 "Explicit keywords" skills/worldbuilder-ainime-export/SKILL.md
```

Expected: output shows the paragraph starting with "**Explicit keywords.**" followed by the non-empty/absent/empty precedence behavior.

- [ ] **Step 6: Commit**

```bash
git add defaults/okf.base.json defaults/okf.json skills/worldbuilder-ainime-export/SKILL.md
git commit -m "feat: add optional keywords field to concept notes

Spec D1: explicit lorebook trigger keywords for concept notes.
When present, export uses these as loreEntry keywords[] instead of
deriving from note content. Defaults to empty (preserves current
agent-derived behavior). SKILL.md updated with precedence rule."
```

Expected: commit created. Verify with `git log -1 --stat` — three files changed.

---

### Task 2: Create extraction reliability map

**Files:**
- Create: `docs/extraction-reliability-map.md`

**Interfaces:**
- Consumes: `docs/target-system.md` (ainime field schema), `skills/worldbuilder-ainime-export/SKILL.md` (current derivation logic), `skills/worldbuilder-ainime-export/card-assembly.md` (character baseProfile rules), `skills/worldbuilder-ainime-export/calendar.md` (calendar/storyTrigger rules).
- Produces: reference document classifying every export-written ainime field as structural, derived, or constructed; multi-target readiness section for CCv3 and ST worldinfo.

- [ ] **Step 1: Read the source documents**

Read these files to understand how each export field is sourced:

1. `docs/target-system.md` — the complete field schema. Identify every field the export workflow writes (skip platform-managed fields per Global Constraints).
2. `skills/worldbuilder-ainime-export/SKILL.md` — the field map and derivation rules. For each field, note whether it's extracted verbatim from a named section (structural), requires agent interpretation (derived), or has no note source (constructed).
3. `skills/worldbuilder-ainime-export/card-assembly.md` — character baseProfile assembly rules. Note all input sections.
4. `skills/worldbuilder-ainime-export/calendar.md` — calendar and storyTrigger rules. Note which values are defaults vs note-derived.
5. CCv3 and ST worldinfo format specs — available at `https://raw.githubusercontent.com/Coneja-Chibi/Hoplight/Mainstage/specs/formats/chara-card-v3.md` and `https://raw.githubusercontent.com/Coneja-Chibi/Hoplight/Mainstage/specs/formats/st-worldinfo.md`. Identify fields each target requires beyond what ainime uses.

- [ ] **Step 2: Create the extraction reliability map**

Create `docs/extraction-reliability-map.md` with this structure:

```markdown
# Extraction Reliability Map

Reference classifying every ainime export field by extraction method.
Maintained alongside the export skill. See spec:
[Export-Standards Review](../.claude/specs/2026-08-10-export-standards-review-keywords-field-and-extraction-reliability-map.md).

## Categories

- **Structural** — deterministic extraction from a known section,
  frontmatter field, or filename. No agent interpretation.
- **Derived** — agent interpretation, constrained by note section
  structure.
- **Constructed** — no source in notes. Configured or generated at
  export time (includes export-time defaults).

## Classification rules

- Every field the export workflow writes appears exactly once.
- Compound fields (storyTriggers[], loreEntries[], characters[],
  calendarConfig.weatherPools, artStyle.*, spriteSets[]) are
  classified at leaf-field granularity — each child gets its own row.
- Categories are mutually exclusive. When a field has a primary path
  and a fallback (e.g., keywords: explicit field or derived from
  body), classify by the primary path and note the fallback in the
  Source column.
- Fields appearing in multiple export sections (e.g., storyTriggers[] from both event and intention story notes) are placed in one table only — use the primary export section.
- Platform-managed fields (IDs, generated images, UI theme, music,
  custom prompts) are out of scope.

## Setting fields

| Field | Category | Source |
|-------|----------|--------|
| ... | ... | ... |

## Adventure fields

| Field | Category | Source |
|-------|----------|--------|
| ... | ... | ... |

## Calendar fields

| Field | Category | Source |
|-------|----------|--------|
| ... | ... | ... |

## Lore fields

| Field | Category | Source |
|-------|----------|--------|
| ... | ... | ... |

## Character fields

| Field | Category | Source |
|-------|----------|--------|
| ... | ... | ... |

## Location fields

| Field | Category | Source |
|-------|----------|--------|
| ... | ... | ... |

## Art style fields

| Field | Category | Source |
|-------|----------|--------|
| ... | ... | ... |

## Multi-target readiness (non-gating)

Additional fields required by non-ainime targets, classified by the
same three categories:

### CCv3 (Character Card V3)

| Field | Category | Candidate source |
|-------|----------|-----------------|
| ... | ... | ... |

### ST WorldInfo

| Field | Category | Candidate source |
|-------|----------|-----------------|
| ... | ... | ... |
```

Populate every table by reading the source documents from Step 1. For each field in `docs/target-system.md` that the workflow writes:
1. Find its derivation in SKILL.md, card-assembly.md, or calendar.md.
2. Classify: if it's copied verbatim from a named section or field → Structural. If the agent interprets note content → Derived. If no note source exists → Constructed.
3. Record the exact source (section name, frontmatter field, or "export-time default/configuration").

For multi-target sections, read the CCv3 and ST worldinfo specs from Step 1. Classify each additional field the same way (Structural/Derived/Constructed). Use "Candidate source" column since these targets have no implemented exporter.

- [ ] **Step 3: Verify completeness**

Count the fields in the map and compare against target-system.md:

```python
python -c "
import re
with open('docs/target-system.md') as f:
    ts = f.read()
with open('docs/extraction-reliability-map.md') as f:
    em = f.read()
# Extract field paths from map table rows
map_rows = [l for l in em.split('\n') if l.startswith('| \`')]
map_fields = set()
for r in map_rows:
    cols = [c.strip() for c in r.split('|')]
    if len(cols) >= 2:
        field = cols[1].strip('\`').strip()
        if field:
            map_fields.add(field)
# Check categories
valid_cats = {'Structural', 'Derived', 'Constructed'}
bad_cats = []
for r in map_rows:
    cols = [c.strip() for c in r.split('|')]
    if len(cols) >= 3:
        cat = cols[2].strip()
        if cat not in valid_cats:
            bad_cats.append(f'{cols[1].strip()}: {cat}')
print(f'Map fields: {len(map_fields)}')
print(f'Invalid categories: {len(bad_cats)}')
if bad_cats:
    for b in bad_cats[:5]:
        print(f'  {b}')
print(f'All categories valid: {len(bad_cats) == 0}')
"
```

Expected: 30+ map fields. 0 invalid categories. All categories valid: True.

- [ ] **Step 4: Commit**

```bash
git add docs/extraction-reliability-map.md
git commit -m "docs: add extraction reliability map for ainime export fields

Spec D2: classifies every export-written field as structural
(deterministic), derived (agent-constrained), or constructed
(export-time). Includes multi-target readiness section for CCv3
and ST worldinfo."
```

Expected: commit created. Verify with `git log -1 --stat` — one file created.

---
name: worldbuilder-source-ingestion
description: Use when bringing external source material into the worldbuilder — game assets, existing character cards, fiction excerpts, wiki pages, or any reference material that will feed the character Q&A workflow or other entity skills.
---

# Source Ingestion

*All prose this skill produces follows `../writing-style.md`. Read it
before writing any reference document.*

## Overview

Source ingestion extracts content from external material and organizes
it into reference documents. It does not interpret what the material
means. The Q&A workflow (worldbuilder-character and other entity
skills) handles interpretation when it consumes the references.

**Governing spec:** [Source Ingestion Skill Spec](../../.claude/specs/2026-08-15-source-ingestion-skill-reference-document-structure-and-extraction-principles.md)

---

## The No-Inference Principle

Ingestion extracts and organizes. It does not interpret.

**The boundary:** if producing a piece of output requires asking
"what does this mean?" rather than "what does this say?", it belongs
to the Q&A workflow, not this skill.

**What ingestion does:**
- Extracts content verbatim or with structural format conversion
- Records provenance per piece (file path, URL, page, section)
- Follows the source's own organization
- Notes source absences

**What ingestion does not do:**
- Label material thematically
- Identify behavioral patterns or psychological traits
- Propose card-format entries
- Map material to card blocks
- Synthesize across sources
- Rate confidence or importance
- Summarize (selecting what matters is interpretation)
- Declare one source as correcting another (record discrepancies)

**Permitted structural transformations** (exhaustive — anything else
is interpretation):
- Format conversion (TOML/JSON/XML to markdown)
- Reproducing existing speaker tags from tagged dialogue
- Stripping engine markup while preserving content
- Reproducing file/directory names as section headers
- Reproducing existing metadata labels from filenames, manifests,
  or other source structures

---

## Workflow

1. The user provides source material (files, URLs, documents)
2. Explore the source to map its file and directory structure
3. Extract content following the source's own organization
4. Output one or more reference documents
5. The Q&A workflow consumes the references as source material

### Exploring the source

Before extracting, map the source's structure: directory tree, file
types, file counts, naming conventions. Present this map to the user
and confirm which parts to extract. Large sources (thousands of files)
may need selective extraction — the user decides which directories
or file sets to include.

### Creating reference documents

Use the scraibe plugin's `new_doc.py` for document creation
(provenance stamping, frontmatter). Do not use scraibe:ingest's
judgment pass (source ranking, contradiction resolution, relevance
extraction) — those conflict with the no-inference principle.

```bash
python "<scraibe-plugin>/scripts/new_doc.py" --type reference \
  --title "<Entity> — <Source Label>" \
  --description "<what this document contains>" \
  --dir notes
```

Record source paths in the frontmatter `resources` field.

The script creates a date-prefixed filename. Rename the file to match
the naming convention (`<entity-name> — <source-label>.md`) using
the scraibe plugin's `rename_doc.py`.

---

## Source-Path Organization

Reference documents follow the source's own file and directory
structure. The source's directory organization is the partition.

- If a game organizes files under `Conversations/` and `Cutscenes/`,
  those directories become separate documents
- If a novel has no file structure, the document follows chapter/page
  order
- Mixed-content files (dialogue mixed with narration) are reproduced
  as-is without splitting by content type — the file is the unit

Content is ordered by source path (alphabetical or directory-tree
order) or by in-source sequence. No reordering by perceived
importance, narrative arc, or thematic grouping.

---

## Reference Document Structure

**Granularity:** one document per source directory or logical source
boundary (a wiki page, a data file, a directory of related files).
When sources are small, multiple directories can share a document
with section breaks preserving the source path as headings.

**Multi-entity sources:** when a source contains material about
multiple characters or entities (group conversations, ensemble
scenes), store the material once in a shared document. Each entity's
reference set links to the shared document. No per-entity splitting
or duplication.

**Naming:** `<entity-name> — <source-directory-or-label>.md`

---

## Extraction Guidance

What to capture from each source. Per-piece provenance (source file
path or section) is required for all extraction.

### Structured data

- All fields with values, reproduced as-is
- Field names and structure (nesting, arrays)
- Ambiguous field names: `[field purpose unclear]`
- Units, enums, cross-references preserved
- Source file path

### Text content (dialogue, narration, prose)

- Full text with speaker attribution where tagged
- Trigger/prerequisite conditions
- Expression/portrait/mood tags where present
- Branching choices with response paths
- Refresh/cooldown rates and gameplay mechanics
- Actions triggered (items given, state written, effects)
- Source file path for each block

### Narrative events (cutscenes, quests, story scripts)

- Scene setup: participants, location, preconditions
- Full dialogue/action sequence
- Branching points and outcomes
- State changes
- Follow-up triggers
- Source file path for each event

### Schedule and calendar data

- Timestamped locations and activities
- Day/season/weather conditions
- Scheduled vs. one-time events
- Participation conditions
- Source file path

### Visual assets

- File path and naming convention
- Available variants (expressions, outfits, seasons) reproduced from
  filenames and metadata — not from viewing images
- When images are viewed for physical description, mark every
  observation `[perceptual]` with the source image path
- Discrepancies between visual and text sources noted as
  discrepancies, not corrections

### External references (wiki, community, developer commentary)

- Content reproduced with source attribution (URL, page title,
  access date) — not summarized. If a source is too large to
  reproduce in full, reproduce the relevant sections with provenance
- `[official]` or `[community]` marker per source
- Discrepancies with other sources noted with both sides and
  provenance — never declared as corrections

---

## Source Absence Notes

Each reference document ends with a **Source Absences** section
noting what the extracted source does not contain. Absences are
factual observations about the source's coverage, stated relative to
the source's own apparent scope.

**Valid:** "This source contains no dialogue files for seasons after
Fall."

**Valid:** "No text-based physical description appears in this
source."

**Invalid (pipeline-specific):** "No information about core fear or
false belief." (Card-format concepts the source has no obligation to
contain.)

**Invalid (unbounded):** "Does not mention childhood pets." (The
source omits infinitely many facts — note structural gaps in the
source's own coverage only.)

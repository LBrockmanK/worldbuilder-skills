---
type: spec
title: Source Ingestion Skill — Reference Document Structure and Extraction Principles
description: 'Defines the worldbuilder source ingestion skill: what it produces (source-organized
  reference documents), the no-inference principle (extraction only, no interpretation),
  source-type guidance for game assets, existing cards, fiction, and external references.'
tags:
- complete
date: 2026-08-15
timestamp: 2026-08-15T18:10Z
resources: []
---

# Source Ingestion Skill — Reference Document Structure and Extraction Principles

## Context

The worldbuilder pipeline has two phases: bring material in, then
build characters from it. The [character card architecture](2026-08-15-character-card-architecture-q-a-workflow-block-model-and-export-interface.md)
defines the second phase — a Q&A workflow that takes answers (human or
source material) and translates them into card-format entries. The
first phase — getting source material into a structured form the Q&A
workflow can consume — has no skill, no defined output format, and no
documented principles.

A test case using Fields of Mistria game assets (NPC profiles, 103
dialogue files, 76 group conversations, 9 heart events, 22 story
events, seasonal schedules, wiki cross-reference, portrait analysis)
demonstrated that raw extraction from arbitrary sources produces
useful reference material. It also revealed the boundary problem:
when the extraction step interprets material (identifying core fears,
synthesizing behavioral patterns, proposing card entries), it
trespasses on the Q&A workflow's responsibility and produces
unlabeled inferences that downstream consumers treat as established
fact.

The scraibe plugin's `ingest` skill defines a generic two-pass
process (mechanical capture → judgment extraction) and the
`reference` document type. This spec builds on that base with
worldbuilder-specific structure and principles.

## Decisions

### D1. The No-Inference Principle

Source ingestion extracts and organizes. It does not interpret.

**What ingestion does:**
- Extracts content from source material verbatim or with structural
  transformation limited to format conversion (e.g., TOML parsed
  into readable markdown, XML tags stripped)
- Records provenance per piece: file path, URL, page, or section
  for each extracted item — not just document-level attribution
- Organizes output following the source's own structure
- Notes source absences (D5)

**What ingestion does not do:**
- Label material thematically ("work ethic," "family dynamics,"
  "vulnerability pattern")
- Identify behavioral patterns or psychological traits
- Propose card-format entries (core fear, false belief, etc.)
- Map material to card blocks (Background, Body, Soul)
- Synthesize across sources to draw conclusions
- Rate confidence or importance
- Summarize content (selecting what matters is interpretation)
- Declare one source as correcting another (that is a truth
  judgment — record discrepancies instead)

**The boundary:** if producing a piece of output requires asking
"what does this mean?" rather than "what does this say?", it belongs
to the Q&A workflow, not ingestion.

**Permitted structural transformations** (exhaustive list — anything
not on this list is interpretation):
- Format conversion (TOML/JSON/XML → markdown)
- Speaker attribution from tagged dialogue (reproducing existing
  tags, not inferring speakers)
- Stripping engine-specific markup while preserving content
- Reproducing existing file/directory names as section headers
- Reproducing existing metadata labels (e.g., portrait expression
  names from filenames)

### D2. Source-Path Organization

Reference documents follow the source's own file and directory
structure. Content is ordered by source path (alphabetical or
directory-tree order) or by in-source sequence.

The source's own directory organization is the partition — not a
content-type classification imposed by the extractor. If a game
organizes dialogue files under `Conversations/` and cutscenes under
`Cutscenes/`, that existing split becomes the document split. If a
novel has no file structure, the document follows chapter/page order.

**Mixed-content sources:** when a single file contains multiple
content types (dialogue mixed with narration, data mixed with
prose), reproduce the file as-is without splitting by content type.
The file is the unit.

**No reordering** by perceived importance, narrative arc, or
thematic grouping.

### D3. Reference Document Structure

Ingestion produces reference documents following the source's own
organization. Each document follows the scraibe `reference` type,
records provenance in frontmatter `resources`, and carries per-piece
source attribution in the body.

**Document granularity:** one document per source directory or
logical source boundary (a wiki page, a data file, a directory of
related files). The source's own structure determines the split —
not a content-type taxonomy. When sources are small, multiple
source directories can share a document with clear section breaks
preserving the source path as headings.

**Multi-entity sources:** when a source contains material about
multiple characters or entities (group conversations, ensemble
scenes), the material is stored once in a shared document. Each
entity's reference set links to the shared document rather than
duplicating the content. The shared document's provenance covers
the source; no per-entity splitting is performed.

**Document naming:** `<entity-name> — <source-directory-or-label>.md`
(e.g., `Adeline — Banked Lines.md`,
`Group Conversations — Adeline Celine Reina.md`).

### D4. Extraction Guidance

What to capture from any source. Per-piece provenance (source file
path or section) is required for all extraction, not just dialogue.

**Structured data:**
- All fields with their values, reproduced as-is
- Field names and structure (nesting, arrays)
- Ambiguous field names flagged: `[field purpose unclear]`
- Units, enums, cross-references preserved
- Source file path

**Text content (dialogue, narration, prose):**
- Full text with speaker attribution where tagged
- Trigger/prerequisite conditions
- Expression/portrait/mood tags where present
- Branching choices with response paths
- Refresh/cooldown rates and gameplay mechanics
- Actions triggered (items given, state written, effects)
- Source file path for each block

**Narrative events (cutscenes, quests, story scripts):**
- Scene setup: participants, location, preconditions
- Full dialogue/action sequence
- Branching points and outcomes
- State changes
- Follow-up triggers
- Source file path for each event

**Schedule and calendar data:**
- Timestamped locations and activities
- Day/season/weather conditions
- Scheduled vs. one-time events
- Participation conditions
- Source file path

**Visual assets:**
- File path and naming convention
- Available variants (expressions, outfits, seasons) reproduced
  from filenames and metadata — not from viewing the images
- When images are viewed for physical description, every
  observation is marked `[perceptual]` with the source image path,
  because interpreting stylized or pixel art is a perceptual
  judgment, not mechanical extraction
- Source discrepancies between visual and text sources noted as
  discrepancies (e.g., "Wiki states purple eyes; portrait
  `spr_portrait_adeline_spring_neutral.png` reads as teal
  `[perceptual]` — discrepancy noted"), not as corrections

**External references (wiki, community, developer commentary):**
- Content reproduced with source attribution (URL, page title,
  access date) — not summarized. If the source is too large,
  reproduce the relevant sections with provenance, not a digest
- `[official]` or `[community]` marker per source
- Discrepancies with other sources noted with both sides and
  provenance — never declared as corrections (which source is
  authoritative is a Q&A-workflow decision)

### D5. Source Absence Notes

Each reference document ends with a **Source Absences** section
noting what the extracted source does not contain. These are factual
observations about the source's coverage, not assessments of what a
character "should" have.

Absences are stated relative to the source's own apparent scope —
what the source seems to cover but does not include. They are not
tested against a checklist of character-building requirements.

**Valid:** "This source contains no dialogue files for seasons
after Fall — Winter dialogue may exist elsewhere or may not be
implemented."

**Valid:** "No text-based physical description appears in this
source. Physical appearance is represented only through portrait
image files."

**Invalid (pipeline-specific):** "No information about core fear
or false belief." (These are card-format concepts the source has
no obligation to contain.)

**Invalid (unbounded):** "Does not contain information about the
character's childhood pets." (The source omits infinitely many
facts — absence notes cover structural gaps in the source's own
coverage, not arbitrary missing facts.)

### D6. Skill Placement and Relationship to scraibe:ingest

The source ingestion skill is a worldbuilder skill at
`skills/worldbuilder-source-ingestion/SKILL.md`.

**Relationship to scraibe:ingest:** the worldbuilder skill uses
scraibe:ingest only for document creation (the `new_doc.py` call
that stamps provenance, frontmatter, and creates the file). It
explicitly skips scraibe:ingest's judgment pass — source ranking,
contradiction resolution, and relevance extraction all conflict
with D1 and are replaced by this spec's extraction-only approach.
The skill states this override in its own text.

**Workflow:**
1. The user provides source material (files, URLs, existing
   documents)
2. The skill explores the source to map its file/directory structure
3. The skill extracts content following the source's own
   organization, per D2 and D4
4. The output is one or more reference documents per D3
5. The Q&A workflow (worldbuilder-character or other entity skills)
   consumes the reference documents as source material

**Relationship to the Q&A workflow:** ingestion and the Q&A workflow
are independent phases. Ingestion does not need to know what card
blocks exist or what doctrine entries are required. Reference
documents carry per-piece provenance that downstream consumers —
including the Q&A workflow — can read to resolve source conflicts
and assess authority. The reference document is the interface
between the phases.

## Consequences

- New skill: `skills/worldbuilder-source-ingestion/SKILL.md`
- The skill references this spec for governing principles
- The skill states its override of scraibe:ingest's judgment pass
- The Q&A workflow's existing "source material substitutes for human
  answers" guidance in `worldbuilder-character/SKILL.md` remains
  unchanged — it already handles consumption correctly
- Inbox items #5 and #6 are resolved by this spec: #5 (extraction
  pipeline) is the skill itself; #6 (skill update) is the creation
  of the skill. The "on-demand extraction agents for automated Q&A"
  aspect of #6 is the Q&A workflow's existing capability, not a new
  ingestion feature

## Notes (non-normative)

The Fields of Mistria test case produced 5 reference documents with
mixed extraction and interpretation. Under this spec, the same test
case would produce source-path-organized documents without the
behavioral analysis, proposed Q&A entries, or depth-of-access
mapping. Those interpretive layers would be produced by the Q&A
workflow when it consumes the references.

The "on-demand extraction agents" concept from inbox item #6 — where
the Q&A workflow dispatches extractors to search reference documents
for answers to specific questions — is a consumption-side pattern,
not an ingestion-side feature. It works naturally when reference
documents are source-organized: an extractor can grep a dialogue
corpus for mentions of a topic without the ingestion step having
pre-labeled that topic.

---
type: spec
title: 'Export-Standards Review: Keywords Field and Extraction Reliability Map'
description: Review of Hoplight and export-format standards (CCv3, ST worldinfo, charx,
  canonical model) applied to internal note structure. Adds optional keywords field
  to lorebook-bound note types and defines an extraction reliability map classifying
  every export-target field by derivation method.
tags:
- complete
date: 2026-08-10
timestamp: 2026-08-10T02:38Z
resources:
- "[[2026-07-25-resource-review-hoplight-a-webnovel-author-s-ai-writing-guide-and-character-builder-v3]]"
- "[[0003-platform-decoupling]]"
---

# Export-Standards Review: Keywords Field and Extraction Reliability Map

## Context

The worldbuilder pipeline's trials have validated Wide-phase writing
quality (additive-doctrine discriminator, convergence validation). The
Export phase — where completed notes become platform payloads — has
received no comparable scrutiny.

This spec results from a field-level comparison of five Hoplight
format specifications (CCv3, ST worldinfo, charx, canonical model,
ST preset) against the project's eight note templates, the ainime
export skill, and the ainime JSON schema. The comparison asked four
questions:

1. Can the export agent reliably extract what it needs from finished
   prose notes?
2. Do notes carry enough metadata for export decisions, or does the
   agent have to invent values?
3. How cleanly do our notes map to targets beyond ainime?
4. Do the export standards reveal improvements to apply back to ainime
   or to our own note structure?

ADR 0003 (platform decoupling) remains in force: phases 1–2 produce
platform-agnostic notes; only the Export phase knows target-specific
fields. Changes here add optional metadata that helps extraction
without violating that boundary.

The free-prose decision for direction.md (Kevin, 2026-07-30) stands
unchanged.

## Decisions

### D1. Keywords field on concept note template

Add an optional `keywords` field to the frontmatter of the concept
note template.

```yaml
keywords: []  # optional, list of strings
```

**Behavior:** When present and non-empty, the export agent uses
these strings as `keys[]` for the corresponding lorebook entry
(ainime `loreEntries[].keywords`, CCv3
`character_book.entries[].keys`, ST worldinfo `entries[].key`).
When absent or empty, the export agent derives keywords from note
content — the current behavior, preserved as fallback.

**Why concept only:** Concept notes map to lorebook entries on
export (ainime `loreEntries[]`). Location and faction notes do not
currently map to lorebook entries; they can gain the field when an
export mapping is defined for them. Character notes map to character
cards (different field structure). Event notes map to
`storyTriggers[]` (activated by timing, not keywords). Seed, plan,
story, and direction notes have no lorebook mapping.

**What this solves:** Keyword derivation is the least reliable
extraction in the current export. The agent reads the note prose and
guesses which words will trigger the entry in conversation. Different
models or different runs may derive different keywords for the same
note. An explicit keywords field makes this deterministic and
author-reviewable — the author sees exactly which conversation
topics will surface this lore.

**What this does not add:** No `priority` or `order` field. In the
few cases where lorebook injection priority matters, the export agent
decides this based on layer classification and note type. No
activation timing metadata (`delay`, `cooldown`, `sticky`) — these
are purely target-specific tuning parameters set at export time.

### D2. Extraction reliability map

Create a reference document classifying every ainime export-target
field by extraction method. Three categories:

- **Structural:** Value is extracted deterministically from a known
  section or frontmatter field. Example: character `name` from the
  note filename.
- **Derived:** Value requires agent interpretation, but the note's
  section structure constrains the answer space. Example: character
  `baseProfile` assembled from Background + Body sections per
  card-assembly.md's five-paragraph rule.
- **Constructed:** Value has no source material in any note and is
  configured or generated at export time. Example: character
  `spriteSets[]` (file references assigned during export).

The map covers every field the export workflow writes in the
ainime JSON payload — the writable subset of the schema in
docs/target-system.md. Platform-managed fields (IDs, generated
images, publishing metadata) are out of scope.

Compound fields (`storyTriggers[]`, `loreEntries[]`,
`characters[]`) are classified at leaf-field granularity — their
children may use different extraction methods.

The map is maintained alongside the export
skill. When a field's extraction method changes (e.g., from derived
to structural because a template gained a new section), the map is
updated.

For multi-target export, the map extends to cover CCv3 and ST
worldinfo fields, noting which additional fields each target
requires beyond what ainime uses, and whether those fields are
structural, derived, or constructed from our notes.

### D3. Multi-target readiness assessment

Record, as a non-gating reference, the field gaps between our note
structure and non-ainime targets. The assessment lives in the
extraction reliability map document (D2), not as a separate
artifact. Key gaps identified:

- **`first_mes` and `mes_example`** (CCv3): Export-time
  constructions. No note captures a "first message" because ainime
  generates greetings dynamically. Candidate sources: character
  behavior and scenario context.
- **`system_prompt` and `post_history_instructions`** (CCv3):
  direction.md is a candidate source. Unlike ainime's verbatim
  `arcManagerGuidance` copy, these fields expect structured
  directives — transformation strategy to be determined by a future
  exporter design.
- **Content rating** (canonical model `presentation.content_rating`):
  Not captured in notes, not needed by ainime. Candidate approach:
  project-level configuration.
- **Character identity facts** (`pronouns`, `age`, `title`) from the
  canonical model: Extractable from character prose but not
  structured. Low priority — most targets embed these in the
  description field.

This assessment informs future export-target work (inbox items 4
and 5) without gating it.

## Consequences

- The concept note template gains one optional frontmatter field. No
  existing notes break — the field defaults to empty, preserving
  current agent-derived behavior.
- The extraction reliability map becomes a reference the export skill
  consults, making the export agent's derivation logic explicit and
  auditable rather than implicit in skill prose.
- Dead-entry detection (an entry with no keywords and no always-on
  flag can never fire) is already possible on the export output,
  where every entry has a concrete keyword array. For concept notes
  that use the keywords field, the check also becomes possible at
  the note level before export. This feeds into the export-procedure
  improvements tracked by inbox item 5.
- Multi-target gaps are documented but not resolved — this spec
  scopes to keywords and the map. SillyTavern export design (inbox
  item 4) and export-procedure improvements (inbox item 5) remain
  separate work items that can reference the map.

## Notes (non-normative)

The Hoplight format specs served as the primary reference for
understanding what export targets want. Hoplight's canonical model
provides a useful cross-format abstraction (Character, Lorebook,
LorebookEntry, Preset, Persona entities), though our pipeline does
not need to adopt it — ADR 0003's platform-decoupling already
achieves the same separation differently.

The six export-procedure borrowings identified in the Hoplight
resource review (export report, pre-flight check, field map
visibility, dead-entry detection, token estimates, declared cut
order) apply to how the export procedure behaves, not to what the
notes capture. They remain with inbox item 5.

The character template already incorporates the Character Builder
v3 doctrine candidates (values carry costs, false belief, contrast
declaration, value-conflict stance, charge-scored memories). No
character template changes are needed from this review.

---
name: worldbuilder-ingestion
description: Use when starting a worldbuilding project from existing material rather than from scratch. Covers SillyTavern character cards and lorebooks, media franchise adaptation, composite worlds assembled from multiple sources, and revision passes on existing projects (v2.0). Produces an ingestion index and extracted content before routing to the appropriate phase.
---

# Ingestion

## Overview

This skill handles projects that begin with existing material — anything from a folder of notes to a complete AI roleplay world export. It does not replace the seed phase; it feeds it. The seed document still gets produced, but informed by extracted content rather than developed from scratch through the six foundational questions.

The output of ingestion is:
- A characterization of the material (what exists, what's missing, what's inconsistent)
- An ingestion index mapping each piece to the three areas (World, Story, Characters) and noting how it will be used
- Extracted content ready for the seed and Wide phases to work from
- A list of quality flags and recommended passes
- The user's confirmation before any work proceeds

---

## Opening Act: Material Survey

### 1. Accept all provided material

Take whatever the user provides — files, pasted text, URLs, images, descriptions of what they have. Work with what Claude can read directly. If something is in a format that can't be read (proprietary binary, locked database export, etc.), say so and tell the user what they need to do to make it accessible before proceeding.

Don't ask for anything beyond what the user volunteers. If they provide one file, work with that file. If they describe a world verbally, work from the description.

### 2. Read everything before doing anything

Read all provided material fully before characterizing or extracting. Don't begin the index until the full picture is available — early impressions get corrected by later material.

### 3. Characterize what you have

For each piece of material, note:
- **Source type**: SillyTavern card, lorebook, franchise wiki, personal notes, prior world project, other
- **Coverage**: Which of the three areas does it touch? (World, Story, Characters) At what depth?
- **Completeness**: Sketch, partial, substantial, or near-complete for each area it covers
- **Quality signals** (see Quality Assessment below)

### 4. Upfront conflict check

Before producing the ingestion index, surface any contradictions in the material. This is the default. If the user wants to flag conflicts as they appear during work instead, they can say so.

Conflicts to check:
- The same character described differently in different sources
- World facts that contradict each other (location, timeline, history)
- Tone or genre inconsistencies between pieces
- Material from different creative contexts that may not combine cleanly

For each conflict: state what the conflict is, which sources are in tension, and ask the user to decide before proceeding.

### 5. Produce the ingestion index

The ingestion index is a structured document that answers three questions about the material before any work starts:

**What do we have?**
A brief summary of each source: type, coverage, quality.

**What are we doing with it?**
For each piece: include wholesale, transform and include, use as input for full process pass, use as reference only, or exclude. Explain the recommendation and let the user confirm.

**Where do we start?**
Based on coverage and completeness, which phase does this project actually enter at?
- Material covers Seed-level content only → produce seed document from extracted content, then proceed to Wide phase
- Material covers Wide-level content substantially → confirm seed, skip to Wide phase gap-filling
- Material is a near-complete prior world → see Revision Pass section

Present the index and wait for confirmation before extracting anything.

---

## Source Type Guidance

### SillyTavern Character Cards

SillyTavern V2 character cards are JSON objects. They may arrive as `.json` files or embedded in `.png` files (stored in image metadata). If the user provides a PNG card, they may need to extract the JSON first using SillyTavern's export function or a card reader tool.

**Field mapping:**

| ST field | Maps to |
|---|---|
| `name` | Character name |
| `description` | Primary character content — blueprint starting material |
| `personality` | Usually overlaps with description; fold into blueprint content |
| `scenario` | World / situation context; maps to world and seed material |
| `first_mes` | Tone and voice reference; don't transfer directly, use to calibrate register |
| `mes_example` | Dialogue examples; excellent voice reference, keep as a section in extracted content |
| `tags` | Classification reference; note but don't import directly |
| `system_prompt` | Platform-specific; note content for any standing guidance, don't import format |
| `character_book` | Embedded lorebook — see lorebook guidance below |

**What to look for:**
- Does the description rely on labels ("mysterious," "kind") or behaviors? Behavioral specificity is the quality signal.
- Is there any material that would serve as negative-track content — what makes this character difficult, guarded, or genuinely in conflict with the player?
- Are there any connections to other characters, places, or events? Or does this character exist in isolation?
- Are the dialogue examples in `mes_example` consistent with the description?

Cards that fail on more than one of these are candidates for a full blueprinting pass.

### SillyTavern / World Info Lorebooks

In the ainime/isekaizero platform, "world info" is the platform term for lorebook entries — the two names refer to the same thing. These skills use "lorebook" as the generic term; "world info" appears in ainime platform documentation.

Lorebooks are JSON files containing arrays of entries. Embedded character books follow the same structure.

**Entry fields:**

| ST field | Notes |
|---|---|
| `keys` | Trigger keywords — note these as activation context, not as final keywords |
| `content` | Lore text — extract this |
| `enabled` | Disabled entries: note existence, ask user whether to include |
| `constant` | If true, always active — this is standing context material, not triggered lore |
| `position` | ST-specific injection location — not transferred |
| `insertion_order` | ST-specific priority — not transferred |
| `selective` + `secondary_keys` | Complex trigger logic — simplify to content and activation context |

**Categorizing entries:**

After extracting, sort entries into three buckets:
- **World knowledge** — lore about places, history, culture, rules, events
- **Character-specific** — lore that is really about a specific character's backstory or context
- **Mechanical / system** — entries that are ST-specific mechanics (prompt injection, formatting instructions, persona framing). Flag these and ask the user which to keep.

Constant entries that describe the setting or world state are seed/world material, not lorebook entries in our structure.

### Media Franchise Material

Franchise material can come from wikis, official publications, fan compilations, or mixed sources. Quality and consistency vary widely.

**First decision: fidelity level**

Ask the user before extracting:
- **Strict adaptation** — stay faithful to established canon; don't invent what the source doesn't establish; gaps are flagged as "needs research" not "invent this"
- **Inspired-by** — use the franchise as a starting point; fill gaps with invented content; the world may diverge from canon

This decision affects everything downstream. Get it before proceeding.

**What to extract:**
- Setting: where, when, what the world is
- Established characters: who exists, what's known about them
- History and lore: what happened, what rules govern the world
- Story: what the current situation is

**What to flag:**
- Contradictions within the franchise (canon conflicts are common in large IPs)
- Material from fan sources that may not be reliable
- Areas where the source is thin and the fidelity decision will matter

Characters from media franchises almost always benefit from a blueprinting pass. Published character descriptions tend to be written for narrative purposes, not as AI behavioral specifications. Behavioral specificity, negative-track content, and relationship depth are usually absent.

### Prior-Workflow Worldbuilder Documents

When the project has character blueprints, notes, or other documents produced by an earlier version of this workflow (or a similar process), assess them carefully before deciding how to treat them.

**The key distinction:** An old blueprint may have been a *narrowing pass* — a planning step before full card writing — rather than the equivalent of what `worldbuilder-character-blueprint` produces today. In the current workflow, the character blueprint IS the full Wide-phase deliverable. An old planning-pass blueprint is source material, not a completed note.

**How to assess:**
- Compare the document structure to what `worldbuilder-character-blueprint` is expected to produce (frontmatter, preamble, concept, foundation, behavioral descriptions, relationships, relationship behavior, storylines)
- If the format matches and content is complete → treat as "use near-as-is" and note any gaps
- If the format differs — even if the content is solid — flag as "source material requiring reprocessing"

**In the ingestion index, mark prior-workflow blueprints as:**
> "Use as source input for `worldbuilder-character-blueprint` — content is good, structure requires reprocessing."

The content is valuable and should be used as input for the blueprint skill. It is not a substitute for running the skill. Do not mark prior-workflow blueprints as complete Wide-phase notes without explicit confirmation that the format matches.

---

### Composite Worlds

When material comes from multiple sources — mixing SillyTavern characters, franchise lore, personal notes — treat each source separately through the steps above, then reconcile.

Reconciliation questions:
- Where sources cover the same ground differently, which takes priority?
- Are there characters from different sources who occupy the same narrative role?
- Does the tone hold across sources, or is there a register conflict?

Establish a priority order for sources before extracting. The user decides; the skill surfaces the question.

---

## Revision Pass (v2.0)

When the existing material is a prior version of a world built with this workflow, the ingestion skill handles the opening differently. This is not ingestion of external material — it's a structured revision of existing project documents.

### Identify revision intent

Before doing anything, establish what the user wants to change. Options are not mutually exclusive:

- **Targeted improvement** — specific characters, lore areas, or story sections that need work
- **Full reprocess** — run existing material through the full workflow again, treating the prior version as input rather than as the final product
- **Expansion** — the existing world is good; add new content (new characters, new story arc, new area)
- **Platform adaptation** — the world was built for one platform; adapt it for another

### Assess the existing project

Read the existing project documents. Note:
- What's in good shape and doesn't need work
- What's thin, inconsistent, or below current quality standards
- What the user has identified as targets

### Scope and route

After the user confirms the revision scope:
- Targeted improvement → route directly to the relevant skill (blueprint pass for specific characters, lorebook review, etc.)
- Full reprocess → treat existing documents as ingestion input; produce a fresh seed document confirming or revising foundational decisions; proceed through phases
- Expansion → go to Wide phase gap-filling with the existing project as context
- Platform adaptation → the existing world documents are the input; route to the appropriate export skill

---

## Quality Assessment

For characters specifically, assess whether source material is sufficient to use near-as-is or whether a blueprinting pass is warranted.

**Use near-as-is when:**
- The description contains behavioral specificity — what the character *does*, not just what they *are*
- Some form of negative-track content exists (what makes them difficult, what they guard against, what they're in genuine conflict with)
- Relationship connections exist — this character has ties to other characters or places
- The description is specific enough to distinguish this character from a generic version of their archetype

**Recommend blueprinting when:**
- The description is mostly labels without behaviors
- There is no negative-track content
- The character exists in complete isolation
- The description could apply to any character of that type with minor substitution
- The character has only one emotional register

When recommending blueprinting, note it in the ingestion index with a one-sentence reason. The user decides whether to proceed with the pass.

---

## Routing After Ingestion

Once the ingestion index is confirmed:

**Material covers Seed phase content** — the world has a setting, tone, community, and rough situation established. Produce a seed document from the extracted content. The six foundational questions apply only to gaps. Confirm the seed document, then proceed to Wide phase.

**Material covers Wide phase content** — characters, lore, calendar, and story direction are substantially present. Confirm that the seed document reflects the foundation. Proceed directly to Wide phase gap-filling and quality passes.

**Mixed coverage** — some areas are Wide-phase complete, others are Seed-phase sketches. Treat each area at the level it's actually at. Don't delay Wide phase work on complete areas to wait for Seed phase work on thin ones.

**Quality passes needed** — characters flagged for blueprinting, lore needing review, etc. Incorporate these into the Wide phase plan rather than treating them as a separate stage.

---

## Working Principles

**Accept what you can; flag what you can't.** Claude can read text, JSON, images, PDFs, and URLs directly. Other formats may require the user to export or convert. Say so clearly and specifically: what needs to happen, not just that there's a problem.

**Characterize before extracting.** The index comes before the work. Don't begin writing extracted documents until the user has confirmed what they want done with each piece.

**Conflict resolution is upfront by default.** Surface contradictions before extraction. The user can override to flag-as-you-go if they prefer.

**Quality assessment is a recommendation, not a gate.** Flag characters for blueprinting, flag thin lore for expansion — but the user decides whether to run those passes. Proceed with what's accepted.

**The seed document still gets produced.** Even for near-complete material, the seed document anchors the project. It confirms or revises foundational decisions from the extracted content and gives the Wide phase a reference point.

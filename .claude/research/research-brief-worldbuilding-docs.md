---
type: reflection
title: "Research Brief: Worldbuilding Documentation Practices"
description: Research brief requesting best practices for organizing, structuring, and maintaining worldbuilding documentation across tools and use cases.
tags: [complete]
date: 2026-06-15
timestamp: 2026-07-11T15:04Z
resources: []
output: ["[[Worldbuilding Structure Research Results]]"]
---
# Research Brief: Worldbuilding Documentation Practices

## Purpose

We are designing a platform-agnostic worldbuilding workflow for AI-assisted interactive fiction and roleplay. The workflow produces a structured body of world knowledge (setting, story, characters) that can be exported to specific platforms (currently ainime-games.com, potentially others).

We need to understand best practices for organizing that knowledge — how to structure it, what metadata it needs, how to keep it consistent through iterative development, and how AI tools interact with it. Obsidian is our likely primary format, but findings should not be limited to it.

The workflow is not limited to AI roleplay. The same documentation structure should be usable for novel writing, game design, interactive fiction, or any creative project that builds a world. Do not constrain findings to the AI RP use case.

---

## Section 1: Obsidian for Worldbuilding and Creative Writing

### 1a. Vault structure approaches

- What are the common vault organization strategies for fiction writers and worldbuilders? Compare flat (all notes in one folder) vs. hierarchical (folders by type or area) approaches.
- What are the practical tradeoffs? When does flat work better than hierarchical? Are there hybrid approaches?
- How do experienced users handle cross-cutting entities — e.g., a festival that involves specific characters, a specific location, and a story beat? Where does it live, and how are the connections expressed?
- Are there published vault templates or starter kits for worldbuilding/fiction? What are the most widely used?

### 1b. Note types and frontmatter conventions

- What note types do worldbuilders commonly define? (Character, Location, Event, Faction, Concept, etc.)
- What YAML frontmatter fields are most commonly used for each type?
- How do experienced users balance structured frontmatter (machine-readable) with flowing prose (human-readable)?
- Are there conventions for indicating relationship/connection between notes beyond wiki-links? (e.g., specific frontmatter fields for related notes, aliases)
- How do people use tags vs. frontmatter fields vs. folder location for categorization?

### 1c. Plugins of interest

Focus on plugins relevant to:
- Fiction and worldbuilding specifically (Longform, WorldBuilding, etc.)
- Querying and aggregating notes (Dataview — what can it do for worldbuilding workflows?)
- Visualization and navigation (Graph view configuration, Juggl, Breadcrumbs for hierarchies)
- Templates and note creation workflows (Templater, QuickAdd)
- Any plugins designed specifically for AI-assisted writing

For each plugin of significant relevance: what problem it solves, how it's used in worldbuilding contexts, and any limitations.

### 1d. Community resources and examples

- Notable YouTube channels, blogs, or community members known for worldbuilding in Obsidian
- Example vaults (public or published) for fiction/worldbuilding
- r/ObsidianMD, r/worldbuilding, and similar community discussions about structure
- Any published "how I organize my fictional world in Obsidian" articles or videos

---

## Section 2: AI Tools Interfacing with Obsidian

### 2a. Current AI plugins and integrations

Survey the current landscape of AI plugins for Obsidian:
- Smart Connections (semantic search over vault)
- Obsidian Copilot and similar chat interfaces
- Any Claude-specific integrations
- Any tools that allow an LLM to read/write the vault as an agent

For each: what it does, how it interacts with note structure, what it needs from notes to work well.

### 2b. What makes notes more or less LLM-readable

- How does YAML frontmatter affect LLM interpretability?
- Does note length matter? Is there a practical optimal length for notes intended for LLM consumption?
- How do wiki-links affect LLM understanding? Does the LLM read them as references or as literal text?
- Do consistent section headers within notes help LLMs navigate?
- Are there any documented studies or community discussions comparing different note structures for LLM use?

### 2c. Context management

- For large vaults (hundreds of notes), how do people manage what context gets fed to an LLM at any given time?
- How does semantic search (Smart Connections etc.) compare to manual context selection for LLM-assisted writing?
- Are there documented workflows for LLM-assisted worldbuilding where the LLM maintains consistency across a large document set?
- What are the failure modes when LLMs interact with poorly structured vaults?

### 2d. Claude-specific considerations

- Are there documented Claude + Obsidian workflows (via MCP, Smart Connections, or other means)?
- How does Claude handle YAML frontmatter in practice? Does it read and produce it correctly?
- Are there known limitations in how Claude processes wiki-link syntax `[[Note Name]]`?

---

## Section 3: Worldbuilding Documentation Beyond Obsidian

### 3a. Series bibles (TV/film)

- What is the standard structure of a professional TV series bible?
- What sections are considered essential?
- How do series bibles handle the world/story/character intersection?
- Are any professional series bibles publicly available or described in detail?
- How are bibles maintained and updated as production progresses?

### 3b. Novel writing world bibles

- How do professional novelists organize their world documentation? Are there published author accounts?
- What tools do novelists commonly use (Scrivener, Notion, physical notebooks, custom systems)?
- How do authors of large shared universes (e.g., Brandon Sanderson's Cosmere) manage world documentation at scale?
- What's the difference in practice between a standalone novel world bible and a series world bible?

### 3c. Game design documents

- What's the standard structure of a video game design document for narrative/RPG games?
- How do AAA studios document their game worlds? Are there published design documents or postmortems that describe the process?
- How does lore documentation work in practice for games with large world-building (e.g., Mass Effect, Dragon Age, The Witcher)?
- What can be learned from game design about maintaining consistency across a large creative team?

### 3d. TTRPG setting documentation

- How do published TTRPG settings (Pathfinder, Forgotten Realms, Blades in the Dark, etc.) organize their world documentation?
- How do GMs organize campaign notes vs. world notes? What tools and structures are common?
- How does the "dungeon master's bible" compare to a novel world bible in structure and purpose?
- What worldbuilding frameworks exist in the TTRPG space? (e.g., Microscope, Kingdom, The Quiet Year as structured worldbuilding tools)

### 3e. Purpose-built worldbuilding tools

Survey the major dedicated worldbuilding tools:
- **World Anvil**: structure, strengths, limitations, who uses it and how
- **Scrivener**: how fiction writers use it for world documentation (not just prose)
- **Notion**: common templates and structures for worldbuilding
- **Campfire Write** and similar: what they offer compared to Obsidian
- **Legend Keeper** (TTRPG-focused): structure and features

For each: what it does that general tools don't, what it's missing, and who it's suited for.

---

## Section 4: AI Roleplay and Interactive Fiction Worldbuilding

### 4a. Lorebook conventions across platforms

- How is the lorebook concept implemented across different AI roleplay platforms? (SillyTavern, Character.AI, Janitor AI, Agnai, etc.)
- What are the structural differences? (Keyword vs. semantic vs. time-based activation; always-on vs. triggered; etc.)
- What do experienced users consider best practices for writing effective lorebook entries across platforms?
- Are there published guides or community wikis on lorebook writing?

### 4b. Context management in AI roleplay

- How do experienced users manage world context in long-running AI roleplay sessions?
- What's the practical effect of lorebook entry length and quantity on session quality?
- How do people structure world information for different context window sizes?

### 4c. Visual novel and interactive fiction documentation

- How do professional visual novel developers (particularly in the Japanese VN tradition and Western indies) document their worlds?
- Are there publicly available design documents from VN productions?
- How do IF/choice-based game writers organize their world documentation? (Inkle, Failbetter Games, etc.)

---

## Section 5: Knowledge Management Principles for Fiction

### 5a. Zettelkasten applied to fiction

- Has the Zettelkasten method been applied to worldbuilding or fiction writing? With what results?
- What's the argument for and against atomic notes in a fiction writing context?
- Are there notable practitioners who apply PKM methods to creative writing?

### 5b. Consistency maintenance at scale

- What methods do large creative teams (TV writers rooms, game studios) use to maintain world consistency?
- For solo creators: what systems or practices are documented for maintaining consistency in large document sets?
- What are the common failure modes of worldbuilding documentation? (Things becoming outdated, contradictions developing, etc.)
- Are there documented "world bible audit" practices — processes for reviewing consistency?

### 5c. Iterative development patterns

- How do professional creators handle world documentation in early stages vs. production stages? Does the structure change?
- What's the right level of detail to establish early? What gets left until later?
- How do people handle retconning or world changes — updating documentation when a decision changes something established?

### 5d. Single-source-of-truth patterns

- How do wiki-style documentation approaches (like those used by large fictional universes — Star Wars Legends wiki, Tolkien Gateway, etc.) maintain single-source-of-truth?
- What are the editorial and structural practices that keep large wikis consistent?
- What can a small-team creative workflow learn from these at scale?

---

## Key Questions to Answer

Regardless of where the findings come from, these are the specific questions we most need answered:

1. **Flat or hierarchical?** For a ~200-note worldbuilding vault covering world, story, and characters for a single project, what are the concrete tradeoffs of flat vs. folder-based organization?

2. **Note types and frontmatter:** What note types should a worldbuilding vault define, and what frontmatter fields are minimally necessary for each? What frontmatter fields add significant value vs. just adding noise?

3. **Cross-cutting entities:** When an entity (a festival, a conflict, a relationship) spans multiple domains (involves characters, a location, a story beat), what are the established patterns for organizing it? Where does it live? How are connections expressed?

4. **LLM readability:** What structural choices most improve LLM comprehension of a note? What choices most impede it? Any empirical findings or well-documented experiments preferred.

5. **Consistency maintenance:** What is the minimum viable process for a solo creator to maintain consistency in a worldbuilding document set through iterative development — without a full editorial team or wiki infrastructure?

6. **Scale signals:** At what point does a worldbuilding document set become hard to navigate? What structural investments pay off early vs. what can be deferred?

---

## Output Format

Findings should be organized by section. For each finding, note:
- The source or context (e.g., "Obsidian community consensus," "documented practice from Brandon Sanderson," "SillyTavern wiki")
- The core insight in plain language
- Any caveats or contexts where it doesn't apply

Prioritize concrete, actionable findings over general principles. We already have the general principles; we need specific structural and content guidance.

Where you find conflicting approaches or ongoing debates, document both sides rather than picking one.

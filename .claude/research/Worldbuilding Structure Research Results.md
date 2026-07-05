---
type: reference
title: "Comprehensive Research Brief: Worldbuilding Documentation Practices"
description: Research results on worldbuilding documentation practices covering vault structure, LLM-readable notes, and consistency processes.
tags: [complete]
date: 2026-06-15
timestamp: 2026-06-15T17:10
resources: []
---
# Comprehensive Research Brief: Worldbuilding Documentation Practices

**TL;DR**
- For a ~200-note worldbuilding project, the dominant community recommendation is a **shallow hybrid**: one note per entity (never a "characters.md" mega-file), 6–8 top-level folders by *type*, and connections expressed through `[[wikilinks]]` plus YAML frontmatter — not deep folder hierarchies. Flat-with-tags works below ~50 notes; folders-by-type plus Maps of Content is the consensus pattern above that.
- For LLM-readability, the emerging "AI-First Vault" consensus (Andrej Karpathy's LLM Wiki gist of early 2026 and its derivatives) is that machine-readable flat frontmatter + a 2–3 sentence "For future Claude" preamble + mandatory `[[wikilinks]]` + explicit source/confidence markers beats prose-heavy notes. Wikilinks survive LLM parsing well; nested YAML does not (Obsidian itself supports it weakly).
- The minimum viable consistency process for a solo creator is a Dataview-powered "series bible" dashboard auto-generated from frontmatter, a periodic "lint" pass (orphans, broken links, stale content, contradictions), and explicit retcon discipline (date-stamped change log + `contested: true` flags) — borrowed from the LLM-wiki workflow and from how Brandon Sanderson's continuity editor Karen Ahlstrom maintains the Cosmere.

---

## Section 1: Obsidian for Worldbuilding and Creative Writing

### 1a. Vault structure approaches

**Core insight — the "shallow hybrid" structure.** Loreteller's *Obsidian for Fiction Writers* guide and Obsidian Tavern's *Master Obsidian Worldbuilding in 30 Days* converge on 6–8 top-level folders with no further subdivision. Obsidian Tavern's prescription: `Characters / Locations / Events & History / Organizations & Factions / Systems / Story Notes / Resources / Templates` — "Eight folders maximum… Don't subdivide this further (no 'Main Characters' vs 'Supporting Characters' folders). Let importance emerge through connections." Loreteller adds a separate `Manuscript/` folder for the prose and a `Plot/` folder for outline and timeline.

The Anima setup guide adds numbered prefixes for sort order (`01-World Overview, 02-Geography, 03-Cultures & Peoples…`), which works well for TTRPG worlds where readers traverse top-down. For fiction this is usually unnecessary because Obsidian's quick-switcher and links are the navigation surface.

**Flat vs. hierarchical — tradeoffs.**
- **Flat (single folder, tags for type):** works below ~50 notes; minimal friction creating notes; relies entirely on link-following and search. Failure mode: noisy search when names overlap (a character "Storm" and a location "Storm Coast"), and you lose the ability to scope Dataview queries with `FROM "Characters"`.
- **Hierarchical deep (`Characters/Allies/Family/`):** breaks down because notes are inherently multi-categorical. P.D. Workman, who states "I have published over 130 books (and written more than that.) I am one of Canada's most prolific authors" with "somewhere over 80 books in Markdown, most of those in Obsidian," explicitly warns: "Everything in the wiki folder is fairly unstructured. These are down-and-dirty working files, not anything beautiful."
- **Shallow hybrid (folder per type, flat within):** the consensus default. Folders give Dataview a `FROM` clause and let templates auto-apply; flatness inside lets links handle relationships.

**Cross-cutting entities.** Three dominant patterns:
1. **One note per entity, regardless of how many domains it touches.** A festival lives in `Events/` and uses frontmatter and wikilinks to attach to characters, locations, and beats. Loreteller is explicit about *direction*: "Link from manuscript scenes to worldbuilding notes, not the reverse… Manual bidirectional linking creates maintenance work that defeats the purpose."
2. **Maps of Content (MOCs) for cross-cutting themes.** Obsidian Tavern: "As your vault grows beyond fifty notes, you'll start losing track of what you've created… This is where Maps of Content (MOCs) save your sanity. Think of them as dynamic table of contents." A festival MOC can list every related character, location, and scene as a Dataview query rather than as a literal note location.
3. **Typed relationships via the Relations or Breadcrumbs plugin.** Both let you declare typed edges (`ally:`, `spouse:`, `mentor:`, `up:`) that produce filtered relationship graphs. Breadcrumbs adds hierarchical "trail" views; Relations adds a focused family/network view with portraits.

**Published vault templates** (caveat: every reviewer warns "don't over-organize before writing"):
- **The Novelist** (Panos Sakalakis, Gumroad, free) — novel-writing + worldbuilding, uses Canvas heavily.
- **Disgraceland Worldbuilding Vault** (Mark Pratt, paid) — character/faction/territory templates with dynamic associations, live character tracker.
- **GCW Worldbuilding Obsidian Pack** (Gonzo Creative Works, itch.io).
- **juliandeleonguerrero/obsidian-worldbuilding-template** (GitHub, free) — targets both fantasy writers and TTRPG GMs.

### 1b. Note types and frontmatter conventions

**Common note types** (consensus across Loreteller, Anima, Obsidian Tavern, Nicole van der Hoeven's D&D vault, P.D. Workman):
Character / NPC, Location (region, settlement, building), Faction / Organization / Family, Event / Session / Historical event, Item / Artifact, Concept (magic system, technology, deity), Scene / Chapter (manuscript-side), Quest / Storyline, Race / Species, MOC / Dashboard.

**Minimal frontmatter by type** (from Anima and Nicole van der Hoeven):

*Character:*
```yaml
type: character
status: alive | dead | unknown
race: 
faction:
location:           # current
role:               # protagonist, ally, antagonist
first-appearance:
aliases: [Eli, "Lord Vareth"]
```

*Location:*
```yaml
type: location
region:
population:
government:
```

*Event:*
```yaml
type: event
date:               # in-world calendar
game_date:          # session/real-world
characters: [[Elena]], [[Kael]]
location: [[Thornwall]]
```

*Scene (manuscript):*
```yaml
type: scene
pov: "[[Elena]]"
chapter: 7
act: 2
status: draft | revising | final
conflict: brief one-line
wordcount: 
```

**Structured-vs-prose balance.** Loreteller's rule of thumb: frontmatter is for fields you will *query* with Dataview (status, type, POV, chapter, date). Everything else is prose. Anima recommends "Overview (2–3 sentence description)" as the first prose section under H2, then `## Notable Features / ## Key NPCs / ## History / ## Secrets / ## Connected Locations`. Consistent section headers matter both for human scanning and (per the LLM-wiki literature) for LLM navigation.

**Relationships beyond wikilinks.** Three mature patterns:
1. **Frontmatter typed-link lists:** `ally: ["[[Bob]]", "[[Alice]]"]`. Both Relations and Breadcrumbs treat this as canonical input.
2. **Aliases:** `aliases: [Elena, "Lord Vareth"]` lets `[[Elena]]` resolve to the full record.
3. **Backlinks** (default Obsidian "Linked mentions") — Loreteller's strong recommendation: "Backlinks handle this automatically."

**Tags vs. frontmatter vs. folders** — hardened community practice:
- **Folders** = note *type* (Dataview `FROM`, template auto-apply).
- **Frontmatter** = queryable attributes (status, POV, date, race, faction).
- **Tags** = transient/lateral concepts (`#openloops`, `#recent`, `#revisit`, `#plot-thread-X`) that cross types.

Caveat on nested YAML: the BBBBlog write-up documents that Obsidian's native frontmatter editor handles nested YAML poorly; flatten with prefixes (`series_name`, `series_num`) instead of `series: {name:, num:}`. Dataview's flattening rules also bite hard on nested structures.

### 1c. Plugins of interest

**Longform** (kevboh/longform) — the fiction-writing plugin. Operates by reading a `longform:` frontmatter entry on an index note; scenes are individual markdown files dragged into manuscript order in a sidebar. Compiles to a single markdown manuscript. P.D. Workman: "Longform is the big one… the crux of what makes writing a novel in Obsidian possible." Notable property: "Longform is built specifically to never alter the contents on your notes. The only note it rewrites is a project's index file." Supports multiple drafts per project and per-scene word-count goals.

**Dataview** — the worldbuilding aggregation engine. Loreteller's killer example is a self-updating series bible:
```dataview
TABLE role, status, first-appearance FROM "Characters" SORT role ASC
```
"This note becomes a dashboard. It pulls live data from your vault. Add a character, and they appear in the bible. Kill a character (set status: dead), and the table reflects it." Caveat: the developer is migrating to "DataCore" but it is not yet ready for production.

**Templater + QuickAdd** — dynamic templates that prompt for fields, auto-stamp dates, generate scene/character notes with consistent frontmatter.

**Smart Connections** (brianpetro) — local-first semantic search via on-device embeddings. Per Brian Petro in GitHub Discussion #432, the default model is "BGE-micro-v2 (Local, 512 tokens, 384 dim): This is a lightweight model suitable for smaller datasets and devices with limited resources." 4.9k GitHub stars (May 2026) and 786,090 downloads as of January 2026 per Grokipedia's Smart Connections entry. Per Smart Connections docs (GitHub issue #1244): sources shorter than the default minimum of 200 characters are skipped for embeddings; the `smart_env.json` `min_chars` setting defaults to 300 for block chunks.

**Breadcrumbs** (SkepticMystic) — typed hierarchical links. Declare `up:`, `down:`, `parent:`, `child:`, etc. in frontmatter; Breadcrumbs renders breadcrumb trails, matrix views, and graph paths. v4 is a complete rewrite. Useful for nested geography (Kingdom → Region → City → District → Building) where Obsidian's untyped graph is too noisy.

**Relations** (community plugin) — visualizes only declared typed relationships (ally, spouse, rival, descended-from), with portraits and a focused "family graph" mode. Solves the "Obsidian graph view is a hairball" complaint specifically for character networks.

**Charted Roots** — family-tree visualization with GEDCOM import, Canvas/PDF export, fictional-calendar support.

**Excalidraw / Canvas** — for hand-drawn maps, faction relationship diagrams. Canvas is built-in; Excalidraw is a community plugin. P.D. Workman uses Canvas for "State of the Union" brainstorming between books.

**Leaflet / Map View** — interactive map with markers that link to location notes; TTRPG-heavy use case.

**AI-assisted writing plugins.**
- **Smart Connections** — discovery + chat with vault context (free core; Pro tier adds inline decorators and Bases functions).
- **Obsidian Copilot** (logancyang) — chat panel, vault Q&A (separate vaultQA mode), inline edits, custom prompts. Effortless Academic's comparison: "Smart Connections is best for semantic search and note discovery… CoPilot excels at AI-assisted editing and vault-wide Q&A."
- **Text Generator / Smart Composer / Obsidian Local GPT** — generation-focused, support local models via Ollama.

### 1d. Community resources and examples

- **Loreteller** (loreteller.com) — opinionated, dense guides for fiction-in-Obsidian.
- **Obsidian Tavern** (obsidiantavern.com) — *Master Obsidian Worldbuilding in 30 Days*.
- **Nicole van der Hoeven** (nicolevanderhoeven.com + YouTube) — published her D&D 5e DM vault via Obsidian Publish; widely cited as the canonical TTRPG-in-Obsidian reference.
- **Josh Plunkett** — extensive YouTube playlist on Obsidian for TTRPG and worldbuilding, name-checked by LegendKeeper itself.
- **Obsidian TTRPG Tutorials** (obsidianttrpgtutorials.com) — companion site to a YouTube series.
- **P.D. Workman** (pdworkman.com) — the most detailed "how a working pro does it" account online.
- **r/ObsidianMD** and **r/worldbuilding** — useful for sentiment but largely point back to the named sites above.

---

## Section 2: AI Tools Interfacing with Obsidian

### 2a. Current AI plugins and integrations

**Smart Connections** (see §1c). What it needs from notes to work well: notes >200 characters, consistent terminology (it indexes meaning, not folder structure), and descriptive titles (the title is included in the embedding).

**Obsidian Copilot** (logancyang) — requires API key for cloud models (Claude, GPT, Gemini) or Ollama for local. Heavier dependency footprint than Smart Connections but does generation, not just retrieval.

**Claudesidian MCP** — full agent-mode capabilities including semantic search via Ollama embeddings; runs as an Obsidian plugin.

**aaronsb/obsidian-mcp-plugin** — runs as a proper Obsidian plugin, serves MCP over HTTP on `localhost:3001`, supports wikilink graph traversal, Dataview queries, and Obsidian Bases. Beta as of early 2026; install via BRAT only.

**iansinnott/obsidian-claude-code-mcp** — auto-discovers vaults via WebSocket on port 22360, multi-vault support, uses legacy "HTTP with SSE" transport for compatibility with current Claude clients.

**msdanyg/smart-connections-mcp** — reads the `.smart-env/` files Smart Connections already computed (does not re-embed); the only working embedding-based MCP path as of 2026.

**MarkusPfundstein/mcp-obsidian** — via the Local REST API plugin; exposes `list_files_in_vault`, `get_file_contents`, `search`, `patch_content`, `append_content`, `delete_file` tools.

**Filesystem-only path:** Claude Desktop's filesystem connector can read/write `.md` files directly. XDA Developers: "It's not doing anything clever, it's just interacting with your files the same way you would in File Explorer." Caveat (also XDA): "A proper Obsidian MCP server… includes automated wikilink management on rename or delete and can check backlinks before touching a file. The filesystem connector just doesn't play by those rules."

### 2b. What makes notes more or less LLM-readable

Empirical/community findings have crystallized into the "AI-First Vault" pattern (Karpathy's LLM Wiki gist Feb 2026, plus derivative work from Nous Research's Hermes Agent, ghelburlabs, NiharShrotri, SamurAIGPT, nashsu/llm_wiki, tashisleepy/knowledge-engine):

**What helps LLM comprehension:**
1. **Flat (not nested) YAML frontmatter.** Type, tags, sources, `last_updated`, confidence. The graphify project explicitly recommends *bypassing* the LLM for frontmatter and wikilink extraction with regex — they're already structured.
2. **Consistent H2 section headers** ("## Overview", "## History", "## Connections") let an LLM jump to the relevant slice without reading the whole note.
3. **Mandatory `[[wikilinks]]`** as the cross-reference primitive. Modern Claude and GPT models parse the syntax natively and follow it as a structural cue.
4. **Recency markers and confidence levels.** ghelburlabs' "AI-First Vault Principle": "machine-readable frontmatter, mandatory wikilinks, recency markers per external claim, source URLs preserved verbatim, confidence levels where applicable, and self-contained context so the note can be retrieved standalone."
5. **A "For future Claude" preamble** — 2–3 sentences of meta-context telling the LLM what the note is and when to use it. ghelburlabs reports this dramatically improves retrieval relevance.
6. **Atomic, self-contained notes.** Notes that assume context from a sibling note retrieve poorly.

**What impedes LLM comprehension:**
1. **Nested YAML frontmatter** — Obsidian's native editor handles it weakly, Dataview struggles, and LLMs sometimes mis-parse it.
2. **Notes under ~200 characters** — Smart Connections explicitly skips them per GitHub issue #1244; `smart_env.json min_chars` defaults to 300 for block chunks.
3. **Implicit references** ("the king" instead of `[[King Aldric]]`) — LLMs can usually infer, but retrieval-by-name fails.
4. **Very long notes (>2,000–3,000 words)** — get chunked unpredictably during retrieval.
5. **Inconsistent terminology** — "Lord Vareth" in one note and "the Vareth heir" in another; aliases in frontmatter fix this.

**Optimal length** — the converging community estimate is 200–800 words per note (≈ "readable in 30 seconds" per the Nous Research llm-wiki skill). The skill enforces: "Keep pages scannable — a wiki page should be readable in 30 seconds. Split pages over 200 lines."

**Wikilinks: literal or reference?** Modern LLMs (Claude 3.5/4+, GPT-4+) treat `[[Note Name]]` as a structured reference and produce them correctly when prompted. Older or smaller models sometimes render them as literal text.

**Documented empirical observation:** the graphify project reports that "~50% of files have 12+ wikilinks each (fully handled by regex); the other 50% have zero and need full LLM extraction" — direct evidence that explicit linking matters for LLM workflows on real-world vaults.

### 2c. Context management

**For large vaults (hundreds of notes):**
- **Semantic search + LLM** is the default. Surface 5–15 related notes via Smart Connections or an embeddings MCP, hand-pick which to keep, drag into Smart Context bundles.
- **Manual selection** still beats semantic retrieval when the LLM needs a *specific* canonical fact — semantic search may surface adjacent rather than authoritative notes.
- **MOC/index pages as anchors** — well-named index notes ("Magic System Overview", "Cast — Book 2") get high semantic weight.

**Failure modes when LLMs interact with poorly structured vaults:**
- **Hallucinated/broken cross-references after renames.** XDA Developers describes coming back to a vault "with half of the note links broken" after asking Claude (via filesystem MCP) to clean up filenames — the filesystem connector renames without backlink rewrite.
- **Contradictions silently overwritten.** The Nous Research llm-wiki skill explicitly mandates: "Handle contradictions explicitly — don't silently overwrite. Note both claims with dates, mark in frontmatter, flag for user review."
- **Stale content drift.** Without a `last_updated:` field, the LLM cannot tell which of two conflicting notes is current.
- **Token budget blowout.** Without folder structure or required-tag filter, semantic search returns too many marginally relevant notes; nashsu/llm_wiki and ghelburlabs implementations both expose a tunable context budget slider (4K–1M tokens).

**Documented worldbuilding-specific LLM workflows:** the most production-ready public examples are LLM-wiki implementations (Karpathy's gist, SamurAIGPT's llm-wiki-agent, NiharShrotri's local-Ollama version, nashsu/llm_wiki, tashisleepy/knowledge-engine). All converge on: raw sources → LLM ingest → entity pages + concept pages + `index.md` + `log.md`, with `[[wikilinks]]` as the cross-reference primitive and a periodic "lint" pass that surfaces orphans/contradictions.

### 2d. Claude-specific considerations

**Documented Claude + Obsidian workflows:**
- **Filesystem connector** (Claude Desktop native, no MCP). Simplest. Free-tier compatible. Caveat: no wikilink-aware rename.
- **mcp-obsidian** (MarkusPfundstein) via the Local REST API plugin — most tool-rich for read/write/search/patch/append.
- **obsidian-claude-code-mcp** (iansinnott) for Claude Code IDE workflows.
- **smart-connections-mcp** (msdanyg) when you want the embeddings Smart Connections already computed.
- **Claudesidian / aaronsb/obsidian-mcp-plugin** for full agent capabilities.

**Frontmatter handling.** Claude reads and produces YAML frontmatter correctly; an Obsidian forum thread announcing a community MCP server specifically advertises "Read & write notes — with full frontmatter support" as a feature, which suggests it isn't free in all MCPs. With well-formed flat YAML, Claude is reliable; nested YAML or non-string values degrade behavior.

**Wikilink handling.** Claude reliably emits `[[Note Name]]` and `[[Note|Alias]]` syntax when asked. It will not, however, validate that the target exists unless the MCP server exposes a tool to do so.

**Practical setup.** The QED42 and Souvik Pal guides both recommend a dedicated Claude project with an explicit system prompt instructing Claude to use the Obsidian tools, since it otherwise defaults to general reasoning. Per-chat permissioning is the safer default; only enable for vaults you're comfortable exposing.

---

## Section 3: Worldbuilding Documentation Beyond Obsidian

### 3a. Series bibles (TV/film)

**Standard structure** (consensus across ScreenCraft, StudioBinder, Final Draft, Industrial Scripts, Stage 32, ScriptFella, Greenlight Coverage). The modern series bible is 5–20 pages and contains:
1. Cover / logline (1–2 sentences)
2. One-sheet / overview (200–300 words)
3. Personal statement (why this story, why this writer)
4. Tone, style, voice, genre, comparable shows ("Show X meets Show Y")
5. World / setting rules
6. Pilot summary
7. Main characters with arcs (not just descriptions)
8. Season 1 episode breakdowns (paragraph each)
9. Multi-season arcs
10. Production notes (visual style, music, format)

**Essentials vs. optional.** Logline, characters-with-arcs, world rules, and the season-1 breakdown are universally cited as non-negotiable. Personal statement and concept art are optional but common in successful pitch bibles.

**World/story/character intersection.** Professional bibles treat the world as the *engine* — the setting must be capable of generating stories indefinitely. ScreenCraft: "You need to prove that your series has staying power."

**Publicly available bibles** (downloadable via Stage 32 and ScreenCraft archives): The Wire (David Simon's two-page "one-sheet" doctrine), Star Trek: TNG, Lost, Battlestar Galactica reimagined, Scrubs, The Corner, Stranger Things, Terra Nova, True Crime, The Starlost, Mad Men, New Girl. The Lost bible is widely cited as "all-time" — written before the writers knew most of the show, yet containing lynchpins that ran through to the finale.

**Maintenance during production.** Two parallel bibles:
- The **showrunner's bible** (vision, themes, long-arc plans) — relatively stable.
- The **character bible** maintained by the script coordinator / writers' assistant — episode-by-episode continuity facts. ScreenCraft: "The Character Bible, or as it's known in the writer's room 'the bible', is a collection of episode & character details tracking helpful information for the future writers of the show." Final Draft is explicit that script coordinators "make sure the polish drafts are set for when the scripts are sent out to showrunners, executive producers, network execs, TV directors, and talent."

### 3b. Novel writing world bibles

**Professional practice varies widely.** P.D. Workman, who states "I have published over 130 books (and written more than that.) I am one of Canada's most prolific authors" with "somewhere over 80 books in Markdown, most of those in Obsidian," uses Obsidian with an unstructured "wiki folder" per series, plus dataview-queried character/scene metadata. She is unusual in publishing her method publicly.

**Tools used by working novelists:** Scrivener (industry standard), Notion (rising, especially for series), Obsidian (rising in indie spaces), World Anvil (rising in indie fantasy/sci-fi), physical notebooks (still dominant for plotters in early stages), Google Docs / Word (for those who don't want the overhead).

**Brandon Sanderson / the Cosmere — the most-documented large-scale shared-universe workflow.** Maintenance is delegated to **Karen Ahlstrom**, Dragonsteel's full-time continuity editor. The Coppermind (17th Shard), citing Sanderson's own blog and JordanCon panels:
> "Karen maintains an internal wiki for Dragonsteel that started out as Brandon's own notes and has continued to grow… The wiki ensures that Brandon does not contradict himself, and contains a high level of detail on everything in the books such as characters, objects, and locations… She also maintains a master spreadsheet with the entire timeline of the cosmere. She is often forced to reconcile timeframes that are described differently on different planets, or are only given as relative dates in the text."

Per Dragonsteel Books' "Continuity in the Cosmere and Beyond": "He's said he tends to outline about ten thousand words for every hundred thousand in a finished book." Sanderson has been planning the Cosmere since *Elantris*, and Karen suggests "good places for Brandon to add them when she reads early drafts of the Stormlight Archive books" (spren placement). Takeaway for solo creators: at scale you need a dedicated continuity person *or* automation (Dataview/AI) to play that role.

**Standalone vs. series bibles.** Standalone novel bibles are typically lean — character sheets, a one-page world summary, a timeline. Series bibles balloon along three axes: a "state of the union" doc per book (P.D. Workman's term), a master timeline reconciling in-world and real-world dates, and `#openloops` tags for unresolved threads.

### 3c. Game design documents

**Standard structure for narrative games** (Anna Megill's Sweden Games Conference talk; Talebuddy template; NumberAnalytics primer; Pixune guide):
1. Project frame: premise, player fantasy, tone, narrative genre
2. World rules: magic/tech rules, hard constraints, social order, "what the game never contradicts"
3. Narrative pillars: core conflict, factions, locations, recurring themes
4. Character roles: protagonist, companions/NPCs, antagonist pressure
5. Key objects (objects story can attach to)
6. Major events (referenced in dialogue and art)
7. Locations (for level design)
8. Combat/economy overview (for narrative-mechanics alignment)
9. Production notes: branching complexity caps, naming rules, scope constraints, open canon questions
10. References (mood, art, music)

**AAA practice.** Anna Megill — narrative lead on Control (Remedy), Writers Guild of America Award nominee for Dishonored: Death of the Outsider (2017), now Lead Writer on the Cyberpunk sequel "Project Orion" at CD Projekt Red (announced February 6, 2024), with prior credits on Guild Wars 2 (ArenaNet) and Avatar: Frontiers of Pandora (Ubisoft Massive) — has presented her story-bible methodology publicly. On sustainable worldbuilding: "When we were writing Guild Wars 2, we had a full game with tons of expansions we had to account for, while still allowing writers (and players) to tell stories in the game's new space… You don't want to paint yourself into a corner, and that's what sustainable worldbuilding is — seeing it coming, putting all this stuff down, making it sustainable by thinking of the transmedia surrounding it." Live-service games need especially conservative lore commitments because expansion content is in-flight.

**Lore documentation at scale.** Games like Mass Effect, Dragon Age, and The Witcher use a layered approach: a tiered "depth model" (essential, secondary, tertiary lore). Andrew Bruce Sinclair's Project Chronos documentation explicitly describes this: "I organized the games story/lore into three depth levels so as to manage what is essential to present for the player and what are secondary and tertiary story/lore elements." Hollow Knight is the gold standard for lore-as-discovery; Red Dead Redemption 2's companion AI and dialogue systems are cited for character-as-system.

**Lessons for cross-team consistency.** Talebuddy: "Narrative contradictions usually come from unstated rules. Spell limits, resurrection logic, surveillance systems, and faction power all belong here." Documenting the *invisible* rules prevents drift more than documenting the visible characters and events.

### 3d. TTRPG setting documentation

**Published settings** (Forgotten Realms, Pathfinder, Eberron, Glorantha) organize as multi-volume layered references: a Campaign Setting core book (overview, regions, factions, deities), region-specific sourcebooks (Faerûn, Kara-Tur, Zakhara, Maztica), edition-specific updates, and novels/adventures that fill in detail. The wiki layer (Forgotten Realms Wiki, Pathfinder Wiki) handles cross-edition reconciliation.

**Forgotten Realms canon policy — the model for hierarchy-of-sources.** Per the official wiki: "We have created a hierarchy to determine which information should be given preference when a contradiction is discovered, but the less preferable information should not be excluded… Official Forgotten Realms sources (sourcebooks, novels, adventures, articles)…" Translated for a solo creator: when your own canon contradicts itself, both claims should be preserved with provenance and a hierarchy noted.

Notable counterpoint: Jeremy Crawford (Wizards of the Coast), speaking before D&D Live in July 2021: "For many years, we in the Dungeons & Dragons RPG studio have considered things like D&D novels, D&D video games, D&D comic books, as wonderful expressions of D&D storytelling and D&D lore, but they are not canonical for the D&D roleplaying game." Official publisher policy is far looser than fan-wiki policy.

**GM campaign notes vs. world notes** — standard split:
- **World notes** = stable canon (geography, factions, history, NPCs).
- **Campaign notes** = session logs, player decisions, current state.

Nicole van der Hoeven's published Obsidian D&D vault separates them with `type: session` for session notes vs. `type: NPC | place | item` for world notes. Dataview can then slice by `WHERE date > 2024-01-01` for "recent session events" vs. the static world.

**Structured collaborative worldbuilding TTRPGs.** These are themselves worldbuilding *frameworks* that produce documentation as a byproduct:

- **Microscope** (Ben Robbins, Lame Mage Productions, 2011) — "a fractal role-playing game of epic histories," GM-less, no prep. Players agree a Big Picture and two Bookend Periods, then build a timeline of nested **Period / Event / Scene** cards. A rotating Lens picks a Focus each round; players each add to the timeline; the round closes with a Legacy step. Microscope explicitly "forbids collaboration or brainstorming" during creation. Artifact: an index-card timeline transcribable directly into a world-history document. *Microscope Explorer* (2015) adds Factions, Future Periods, Interventions, and pre-built "seeds" like "After Lemuria Sinks" and "Who Watches the Watchmen?"

- **Kingdom 2nd Edition** (Ben Robbins, Lame Mage) — community-at-a-crossroads game with three Roles: **Power** ("If you tell people in the Kingdom to do something, they do it, whether they like it or not"), **Perspective** ("you say what happens if we choose one path or the other, and your predictions will come true"), **Touchstone** ("you show us how everyone in the Kingdom feels"). A Crossroad sheet tracks a yes/no community decision and a parallel Crisis track. K2 adds Legacy mode for multi-Crossroad campaign-style play. Artifacts: Crossroad sheets with resolved Yes/No outcomes and Perspective predictions.

- **The Quiet Year** (Avery Alder, Buried Without Ceremony, 2013) — map-drawing game. A 52-card deck represents 52 weeks/one year; suits = seasons (Hearts/Spring, Diamonds/Summer, Clubs/Autumn, Spades/Winter); each card poses a prompt. Three turn actions: Discover Something New, Start a Project (d6 placed on the map, ticks down weekly), Hold a Discussion ("A discussion never results in a decision being made"). The game ends when the King of Spades is drawn in Winter. **Contempt Tokens** (16 skull-shaped) carry social weight only — Adam Dixon (quoted in Wikipedia): "The clever thing about the contempt mechanic is that it has no hard mechanical impact on the game… its effect is purely social." Artifact: the collaboratively-drawn map plus an index card of Abundances/Scarcities. Spin-off: *The Deep Forest* (decolonization focus).

- **Dialect** (Thorny Games / Kathryn Hymes & Hakan Seyalioglu, 2018) — "A Game About Language and How It Dies." 3–5 players, three Ages. Pick a Backdrop, three Aspects, draw Archetype cards; play language-cards that generate vocabulary tied to Aspects; the language dies when the isolated community reconnects. Artifact: a documented dialect plus the community's story.

- **The Ground Itself** (Everest Pipkin, 2019) — one-session game about one place over geological/historical time. Cards drive prompts on a depleting deck so time-scales shorten as you play. Per Pipkin in *Filmmaker Magazine* (2024), groups "often use the game to establish history, ecologies and broader context for a world before jumping into D&D or another tabletop game."

These frameworks are useful even for solo writers as *generative scaffolds* — running a solo Microscope session can produce a multi-millennium timeline of canonical events that seeds a world bible.

### 3e. Purpose-built worldbuilding tools

**World Anvil.** Online, opinionated, all-in-one. Strengths: ready-made templates (locations, technology, characters, pantheons, cultures, magic systems, bestiary), 20 visual themes, public/private toggle for player-facing wikis. D&D Beyond forum sentiment is mixed: "Despite using it for a month, it would still take many times more time to create content there than it would on piece of paper… Interface feels very outdated." Pricing: free tier exists; most useful features behind subscription. **Best for:** TTRPG GMs who want a published player-facing wiki; fantasy/sci-fi novelists who want guided structure.

**Scrivener.** Industry-standard novel-writing tool, repurposable for worldbuilding. Literature & Latte's official guide ("How to Use Scrivener for Worldbuilding" by Kirk McElhearn): "Scrivener is an excellent tool for worldbuilding because it lets you organize dozens of interconnected notes and files in one project, view documents side by side, and easily reorganize your material as your world develops."

Concrete features for worldbuilding:
- **Binder folders:** Characters, Places (subfolders for towns/cities/regions/planets or for families/factions). Built-in Character and Setting sketch document templates; unlimited custom templates.
- **Research folder** holds text, PDFs, graphics, audio, video, web snapshots. Large items can be imported as aliases/shortcuts (Mac/Windows respectively) to avoid bloating the project.
- **Metadata system.** Gwen Hernandez, author of *Scrivener For Dummies*, in Writer Unboxed (Feb 22, 2022): "Scrivener has several types of metadata you can use to color code, organize, group, and search for your documents. They include Label, Status, Keywords, and Custom Metadata." Label is color-coded (typically used for POV), visible in Binder/Corkboard/Outliner; Status tracks document progress; Keywords are searchable and can be hierarchical; Custom Metadata fields are defined per-project and visible as Outliner columns; Synopsis (3–4 sentences) drives the Corkboard card face.
- **Snapshots** for per-document version history.
- **Compile** to ePub/PDF/DOCX/Kindle with format presets.

Notable Scrivener templates: Jen Terpstra's Complete Novel Writing Template with character/worldbuilding subpages; K.M. Weiland's free Outlining & Structuring template (built with Stuart Norfolk, July 2017) with color-coded notes — Weiland: "Since I now use Scrivener exclusively for my fiction (buh-bye, Word), I wanted to share with you an updated free Scrivener template based on my own process," with "orange notes" used for "world-building or thematic notes"; Belinda Crawford's Leviathan template.

**Scrivener vs. Obsidian:**
- Scrivener wins on: compile-to-manuscript, structured metadata + Corkboard/Outliner UI, document templates, snapshots, project targets.
- Obsidian wins on: bi-directional wikilinks + graph, plain-text portability, plugin extensibility, Canvas, free for personal use.
- Common hybrid: Obsidian for research/notes/worldbuilding, Scrivener for the manuscript. (towritewithwildabandon.com: "I use [Obsidian] exclusively for research and for story notes – themes, character names, story ideas.")
- Scrivener weaknesses (per Storyflow's 2026 review — caveat: from a competing product): "the interface looks dated, the iOS sync is fragile across more than two devices, the per-platform licensing is confusing, and the AI integration is non-existent."

**Notion.** StoryFlint's World Building Bible is the most-cited template — connected databases for locations, cultures, religions, creatures, languages, histories. Strengths: real-time multi-user collaboration, embedded databases, fast onboarding. Weaknesses: web-only (offline limited), data-portability concerns, can become a UI maze at scale.

**Campfire Write** — modular pricing (pay only for modules you use: manuscripts, characters, encyclopedias, relationships, timelines). LegendKeeper: "If you're looking for a platform that will give you lots of guide rails, Campfire Writing is a much more polished alternative to WorldAnvil." Trade-off: subscription costs add up.

**Kanka.io** — open-source-leaning, modular, cleaner interface than World Anvil, free tier most generous among campaign managers. "Heavily inspired by WorldAnvil, but boasts a lower pricepoint and a much cleaner interface" (LegendKeeper). Vibe is "game design" rather than "literary."

**LegendKeeper** — collaborative, TTRPG-focused, interactive maps, free-form whiteboards, real-time multiplayer, re-usable templates, one-click publishing. Strongest pick for D&D parties and creative teams.

**Fantasia Archive** — free, World Anvil-alike, open source.

**Obsidian Portal** — older, still functional, oriented to campaign management.

---

## Section 4: AI Roleplay and Interactive Fiction Worldbuilding

### 4a. Lorebook conventions across platforms

**SillyTavern (World Info / Lorebook).** The most-documented platform. The SillyTavern docs (docs.sillytavern.app) are the de facto canonical reference, supplemented by the community "World Info Encyclopedia" (rentry.co/world-info-encyclopedia) by kingbri, Alicat, and Trappu.

Core concepts:
- **Key/value pairs.** A keyword (or list) triggers an entry value. "When that key is mentioned in a prompt, the value is injected into it."
- **Activation modes:** keyword-triggered (default); **Always Active** (always injected — used for "the laws of physics in your world, the rules of your magic system, or the core personality traits of a character"); vector-based (semantic).
- **Scan Depth:** how many recent messages SillyTavern searches for keywords.
- **Scope:** Global, Character (one primary book per character + auxiliary), Persona, Chat.
- **Format conventions:** PList (`[Mossford: town, located in valley]`) for compact factual descriptions; Ali:Chat for example reactions/dialogue.
- **Filter to Characters / Character Exclusion:** restricts which character(s) can trigger an entry.
- **Recursive scanning:** an entry can trigger other entries.

**Best-practice patterns** (World Info Encyclopedia; MegaNova's "5 Lorebook Entry Types"):
1. **Behavioral rules entries** are highest-impact. A top SillyTavern character creator (300+ characters) quoted by MegaNova: "I spend 60% of my time on behavioral rules. That's what makes a character feel ALIVE. Appearance is forgettable, behavior is memorable."
2. **Hybrid matching** (keywords + vectors) for relationships beats either alone.
3. **Priority assignment:** "If it would break the character to forget it, priority 9–10. If it's just interesting, priority 5–6."
4. **Embedded lorebooks shipped with character cards** — SillyTavern prompts to import on character import.
5. **Procedural-guidance lorebooks** (Sphiratrioth666's pattern on HuggingFace) — entries used not as lore but as *instructions* (random dice tables, world-state rolls), triggered by codewords like "DC" or "AP."

**Character.AI, Janitor AI, Agnai.** Less well-documented publicly; lorebooks/memories are simpler — typically flat lists of fact entries with keyword triggers, less granular control over activation, recursion, and scope than SillyTavern. The general trend is convergence toward SillyTavern-like complexity.

### 4b. Context management in AI roleplay

**Length and quantity effects.** Community consensus:
- Cramming world info into the character card description gets "messy REAL fast" (arsturn.com). The lorebook pattern frees the card for personality/voice while keeping detail injectable on demand.
- Token economics (MegaNova): "Character Card Approach: token cost 3000+ tokens, result: less room for conversation history. Lorebook Approach: core personality in character card (800 tokens), world info in lorebook entries (fires only when needed)."
- For Always-Active entries, keep them short — they cost tokens every turn.

**Memory consolidation patterns.** SillyTavern-MemoryBooks (aikohanasaki) automates memory creation: mark scenes in chat, AI generates JSON-based summaries, stored as lorebook entries. Multi-tier consolidation: Clips → Memories → Arcs → Chapters → Books. Recommendation: separate memory lorebooks from world-info lorebooks for organization and per-book budget control via SillyTavern-LorebookOrdering (STLO).

**Context window sizing.** With 8K windows, keep total Always-Active under ~1,000 tokens and rely heavily on keyword triggering. With 200K+ windows (Claude, Gemini), dumping entire bibles in the system prompt is wasteful — keyword triggering remains more responsive because only relevant info gets the model's attention.

### 4c. Visual novel and interactive fiction documentation

**Visual novel design docs.** Standard sections (per VNDev Wiki, Lemma Soft Forums, Lars Martinson's public VN design doc): story (most extensive), characters, art assets (sprites with expression variants, backgrounds with time-of-day variants, CGs, GUI), audio, branching/flowcharts. VNDev Wiki: "Since the GDD is considered a living document, it should be revised and kept up to date as the game changes."

**Lemma Soft community sentiment:** GDD format is contested — many indies "wing it"; others use full GDDs. A common recommendation is to use **Twine** for visualizing branching even if Ren'Py is the final engine.

**Inkle / Failbetter (Mask of the Rose).** Both studios use the open-source **Ink** scripting language (since 2019, rebrand of Inklewriter). Emily Short, Failbetter's creative director, on Mask of the Rose: "Mask of the Rose is Failbetter's first project using Ink, though several of us at the studio have used it before in other contexts… Ink does all of that, and with less friction than many of the other systems in this space." Sea of Thieves and (per industry rumor) Valve have also used it.

**Public design docs available:** Lars Martinson's VN design doc is the most accessible solo-creator example. Mayadem Technology's Template Concept Document on Medium provides a structured template. Most major studio docs remain private.

**Tools used by IF/branching authors:** Inkle's Ink, Twine, Ren'Py, ChatMapper, Arcweave, Yarn Spinner. Worldbuilding documentation typically lives *outside* the branching tool (Scrivener, Notion, Obsidian) and is referenced as the dialogue/scene scripts pull from it.

---

## Section 5: Knowledge Management Principles for Fiction

### 5a. Zettelkasten applied to fiction

**Yes — explicitly endorsed by the Zettelkasten community.** Sascha Fast (zettelkasten.de): "I use my Zettelkasten for background research and worldbuilding for my fiction writing… I use my Zettelkasten for writing fiction fragments that form whole the stories."

**Atomic notes for fiction — the case for.** Fast describes a worked fantasy example — researching dangerous animals → splitting into atomic notes (crocs, hippos, components of real danger) → combining into a fictional "crohipo" → linking to fauna and language notes → using the principle of perceived danger as a reusable tool. The argument: atomic notes are *thinking tools*, not just storage. They scale because they let you discover unexpected connections. A Zettelkasten forum user "Loni" endorses the same: "To record [ideas] by small chunks has the same benefits that working with atomic notes."

**The case against (or, the friction).** Fiction often *wants* prose flow. Splitting a character into 12 atomic notes can fragment the lived feeling of them. The compromise most worldbuilders adopt: atomic for *concepts* (themes, magic principles, cultural tropes) and *not* atomic for *entities* (one note per character, one per location).

**Notable practitioners.** Sascha Fast (zettelkasten.de). The Zettelkasten forum hosts active fiction-writing threads. Loreteller and Obsidian Tavern implicitly endorse Zettelkasten-style atomic linking without naming it.

### 5b. Consistency maintenance at scale

**TV writers' rooms** maintain consistency through **script coordinator / writers' assistant** roles: detailed notes of story breaks, pitches, arcs; document/beat-board formatting; continuity tracking; final-script polish. Final Draft: "Once the script coordinators okay a final shooting draft, you can expect that the format, grammar, spelling, continuity, and overall aesthetics are as they should be." The writers' room itself enforces consistency through table reads, multi-pass script reviews (tone pass, theme pass, dialogue pass), and tools like WritersRoom Pro for digital index-card boards.

**Game studios** rely on the Narrative Bible + version control + writers'-room-style review. Story bibles must "have room to grow as different teams pitch ideas" (Megill).

**Brandon Sanderson / Dragonsteel** — a dedicated continuity editor (Karen Ahlstrom) maintains an internal wiki and a master Cosmere timeline spreadsheet, reconciles cross-planet timeframes, and checks artwork against canon with Isaac Stewart.

**Solo creators — minimum viable process:**
1. **One source of truth per fact.** Don't duplicate canon across notes; link instead.
2. **Frontmatter-driven dashboards.** Dataview series-bible queries auto-update; this catches "I killed Elena in book 1 but she appears in book 2" if `status:` is kept accurate.
3. **An open-loops tag** (P.D. Workman: `#openloops`) for unresolved threads.
4. **Periodic "lint" passes.** Per the Nous Research llm-wiki skill: orphan pages, broken wikilinks, missing index entries, malformed frontmatter, stale content (>90 days older than relevant new sources), contradictions on same-tagged pages, low-confidence pages with single sources.
5. **Explicit contradiction handling.** Don't silently overwrite. Mark `contested: true` in frontmatter; keep both claims with dates; flag for review.
6. **A retcon log.** When a decision changes established canon, date-stamp the change and the affected notes.

**Common failure modes:**
- Outdated canon — fixed by `last_updated:` + lint.
- Contradictions developing silently — fixed by lint + explicit handling.
- "Beautiful vault, no manuscript" — Loreteller's repeated warning.
- Aliases drifting (one character has six names across notes) — fixed by `aliases:` frontmatter.
- Wikilinks rotting after renames — fixed by Obsidian's auto-rename + wikilink-aware MCP tools rather than filesystem-only AI agents.

### 5c. Iterative development patterns

**Early stage vs. production stage.**
- **Early stage:** ScreenCraft, Industrial Scripts, and the GDD literature converge on "broad strokes only." Logline, tone, top-level world rules, main characters with arcs, season-1/book-1 broad-strokes summary. Don't drown in detail.
- **Production stage:** the bible becomes a *living document* maintained as a continuity reference, not a sales pitch. Sections shift: less "personal statement," more "character bible" (episode-by-episode facts).

**Right level of detail early on.** Establish:
- Hard constraints (magic/tech rules, social order, what the story will never contradict).
- Protagonist and antagonist with clear motivations and one-line arcs.
- Setting at the level needed for the first installment plus enough seeding for future stories.

Defer:
- Detailed NPC backstories beyond what scenes require.
- Geography of regions the story doesn't visit.
- Linguistic detail beyond names and flavor terms.
- Calendar/chronology precision (rough dates are enough — Karen Ahlstrom is reconciling this for Sanderson *after* publication).

**Handling retcons.**
- Add a date-stamped change entry to a `log.md` or change-log section.
- Update the contradicting note in place, preserving the prior version via Obsidian file history, Scrivener Snapshot, or git.
- Add `superseded: 2026-04-12` to the abandoned version if kept.
- Use the Forgotten Realms Wiki policy as a template: document the contradiction, preserve both, declare a hierarchy.

### 5d. Single-source-of-truth patterns

**Wiki-style governance (Forgotten Realms Wiki, Coppermind, Tolkien Gateway).** Editorial practices:
1. **Explicit canon hierarchy.** FR Wiki ranks: sourcebooks → novels → adventures → magazine articles → video games → ambiguous sources.
2. **Citation discipline.** Every assertion is footnoted to a primary source.
3. **Contradictions documented, not erased.** FR Wiki policy: "the less preferable information should not be excluded."
4. **Edition awareness.** Jeremy Crawford (WotC, July 2021 press briefing): "Every edition of the roleplaying game has its own canon as well… something that might have been treated as canonical in one edition is not necessarily canonical in another."
5. **Style and Manual of Style pages** govern formatting, voice, abbreviations.
6. **Spoiler policies** (Coppermind) gate information by book release.

**What a small-team creative workflow can adopt:**
- A SCHEMA file declaring note types, required frontmatter fields, and the canon hierarchy of *your* sources (e.g., "novel text > outline > worldbuilding doc > Discord chat with co-writer").
- An `index.md` / Home / MOC listing every canonical entity by type.
- A `log.md` or change-log section capturing every retcon with a date.
- Frontmatter fields: `confidence: high|medium|low`, `sources: [...]`, `last_updated:`, `contested: true` for known contradictions.
- A regular (weekly or per-chapter) lint pass — manual or scripted — for orphans, broken links, malformed metadata, stale content.

---

## Recommendations — Answers to the Key Questions

**1. Flat or hierarchical (~200-note vault)?** Use the **shallow hybrid**. 6–8 top-level folders by *note type* (Characters, Locations, Events, Factions, Systems, Story Notes, Templates, Resources), flat inside each. Folders enable Dataview `FROM` clauses and template auto-assignment; flatness lets links carry the structural weight. Below ~50 notes a single-folder + tags vault is fine; above ~50, folders pay off. Deep hierarchies (`Characters/Allies/Family/...`) are the worst of both worlds because notes are multi-categorical. *Threshold to revisit:* if you can't find a note within 30 seconds, restructure.

**2. Note types and minimal frontmatter.** Define at minimum: Character, Location, Faction, Event, Concept, Scene. *Minimal frontmatter (adds value):* `type` (always), `status` (alive/dead; draft/final), `aliases` (always for entities), `tags` (lateral concepts), `last_updated` (for AI workflows). *High-value additions:* `pov` + `chapter` + `act` for scenes; `region` for locations; `first-appearance` for characters; `confidence:` for unstable canon. *Adds noise without payoff:* deeply nested YAML, fields you never query, granular sub-categorization (e.g., "race" if everyone is human).

**3. Cross-cutting entities.** Three established patterns: (a) **one note per entity in the type that fits best** (a festival in Events) with frontmatter listing related characters/locations and prose narrating its role; (b) **a MOC for cross-cutting themes** that aggregates via Dataview rather than physical location; (c) **typed relationships in frontmatter** (`participants: [[Elena]], [[Kael]]`, `location: [[Thornwall]]`) so Breadcrumbs/Relations/Dataview can render the network. Express connection in frontmatter for queryable links, in wikilinks within prose for human reading. Avoid placing the festival "in" multiple folders or duplicating it.

**4. LLM readability.** *Most helps:* flat YAML with type/tags/last_updated; a 2–3 sentence "For future Claude" preamble; consistent H2 section headers; mandatory `[[wikilinks]]`; aliases declared in frontmatter; 200–800 words per note; explicit source/confidence markers. *Most impedes:* nested YAML; sub-200-character notes (invisible to Smart Connections); implicit references ("the king"); >2,000-word notes that get chunked unpredictably; inconsistent terminology. *Strongest empirical signal:* graphify's finding that ~50% of well-tended vaults have 12+ wikilinks per file (regex-extractable) while the other 50% have zero — explicit linking is the single highest-leverage investment for LLM workflows.

**5. Minimum viable consistency process — solo creator.**
- One Dataview "series bible" dashboard auto-aggregating characters, locations, scenes from frontmatter.
- `#openloops` (or equivalent) for unresolved threads.
- A `log.md` change-log appended whenever canon shifts.
- A weekly or per-chapter lint pass: orphans, broken links, stale notes (`last_updated` >90 days), duplicate entities (aliases mismatch).
- `confidence:` and `contested:` frontmatter for shaky claims.
- A canon hierarchy declared in a SCHEMA note (your own Forgotten Realms canon policy).

This replaces the Karen Ahlstrom role with ~3 minutes per week. It is *not* sufficient for a 40-book Cosmere — but it is sufficient for a trilogy. *Threshold to upgrade:* when contradictions slip through the lint pass twice running, hire a continuity reader.

**6. Scale signals — early investments vs. defer.**

*Hard-to-navigate signals:* you can't find a note from last month within 30 seconds; two notes exist for the same entity; you forget which of two contradicting facts is current; graph view is a hairball; Smart Connections returns irrelevant results.

*Invest early (before 50 notes):*
- One folder per note type (cheap to start, painful to add later).
- Templates for at least Character, Location, Scene.
- A consistent frontmatter schema (even minimal: type + tags + status).
- Aliases for every entity.

*Defer until needed:*
- Maps of Content (only when you can't find things — typically 50–100 notes).
- Dataview dashboards (when you have enough metadata to query).
- Custom CSS, complex themes, exotic plugins.
- A formal lint process (when contradictions first bite).
- AI integration (Smart Connections is cheap to add anytime).
- Compile/export rigging (when you actually need to deliver a manuscript).

---

## Caveats

- "Best practices" in this space are not validated empirically. Most are blog-post consensus from a handful of vocal practitioners — Loreteller, Obsidian Tavern, P.D. Workman, Sascha Fast, the SillyTavern docs maintainers, ghelburlabs. Treat reported consensus as informed convention, not law.
- The LLM-wiki literature is very new (Karpathy's gist is February 2026; derivative implementations all post-date that). Production track records are limited; some claims about LLM readability are inferred from architecture decisions rather than measured.
- World Anvil, Campfire, and LegendKeeper comparison sources are often written by or sponsored by competing tools (Storyflow, LegendKeeper itself). Tone-down their criticisms accordingly.
- Brandon Sanderson's continuity workflow is exceptional, not normative. Most solo novelists do not have a Karen Ahlstrom.
- Forgotten Realms canon-policy quotes are from Fandom-hosted community wikis, not Wizards of the Coast. Wizards' own policy (per Crawford 2021) is far looser: "Whatever's best [for current needs]."
- Some product features and version numbers move fast — Smart Connections Pro tiers, Longform changes, MCP transport protocols, Breadcrumbs v4. Verify before depending on a specific feature.
- Dialect's publication year is given as 2016 by one Wikipedia source but the Thorny Games Kickstarter put physical copies in 2018; 2018 is more reliable.
- "Project Orion" attribution to Anna Megill at CD Projekt Red is from CDPR's February 6, 2024 announcement; her departure from Ubisoft Massive predates this and her Sweden Games Conference talk references Guild Wars 2 work at ArenaNet, not Ubisoft.
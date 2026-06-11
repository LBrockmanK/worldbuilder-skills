---
name: worldbuilder-linking
description: Use as a post-pass after any skill creates or edits vault notes. Adds markdown links for cross-references, back-links from other files, and empty links for entities that may not yet exist. Also use to find unresolved links as expansion targets. Designed to run as a subagent.
---

# Linking Pass

## Overview

This skill runs after another skill creates or edits note files. It ensures the vault's link graph is complete: forward links from the edited file to other notes, back-links from existing notes to the newly created file, and empty links to entities mentioned in text that have no note yet.

The process is script-heavy by design. The scripts handle the deterministic work (matching known entity names to notes). The LLM handles the judgment call: identifying entity references the scripts can't catch — names that aren't in any note's title or aliases, or references phrased indirectly.

**Run as a subagent** when called from another skill's session. This avoids loading the main context with inventory data and search results.

---

## When to Invoke

After any of these skills finishes writing or editing notes:
- `worldbuilder-character`
- `worldbuilder-location`
- `worldbuilder-faction`
- `worldbuilder-concept`
- `worldbuilder-event`
- `worldbuilder-story`

The calling skill or session should invoke this skill with the path(s) of the file(s) that were created or modified.

---

## Process

### Step 1: Inventory

Run the note inventory script to get the current state of all notes:

```powershell
scripts/list-notes.ps1 -VaultPath <vault-root> -Pretty
```

This produces a table of every note's name, type, status, aliases, and brief. Scan this output to understand the link targets available.

### Step 2: Deterministic forward + back linking

Run the linker script on the target file with reverse mode:

```powershell
scripts/link-notes.ps1 -TargetFile "notes/<filename>.md" -Reverse -VaultPath <vault-root>
```

This does two things:
1. **Forward links** — Scans the target file's body text for plain-text mentions of any note name or alias in the vault. Links the first unlinked occurrence per H2 section.
2. **Back-links** — Scans all other files for plain-text mentions of the target file's name and aliases. Links first unlinked occurrence per section in each file.

The script matches longest names first to prevent partial matches. It skips text already inside markdown links or code blocks. It does not touch frontmatter.

Use `-DryRun` first to preview changes if the edit scope seems large.

### Step 3: LLM review for unlisted entities

After the scripts run, read the target file and look for entity references the script could not catch. These are:

**Named entities without notes:**
- Characters mentioned by name who have no note and aren't in any note's aliases (a character's parent, a historical figure, a friend from before the story)
- Locations referenced by name that have no note
- Factions, groups, or organizations mentioned that have no note

**How to handle them:**
- Wrap each in a markdown link pointing to where the note would live: `[Mother's Name](notes/Mother's Name.md)`
- The target file does not need to exist. An empty link is intentional — it marks the reference as a potential expansion point and appears in unresolved link reports.
- Link on first mention per section, same as the script convention.
- Do NOT create notes for these entities. Just create the empty links.

**What to skip:**
- Generic references that aren't specific entities ("his friends", "the townspeople", "the old days")
- References that are clearly not note-worthy (a one-off mention of a historical period, a vague group)
- The note's own name in its own text

**Decision guidance:** If someone might someday want to click this name and read more about it, link it. If the name is just background color, leave it.

### Step 4: Back-link review for unlisted references

Read the files the script modified in Step 2 (the back-link pass). Verify the script's work looks correct — no false matches, no links to the wrong note when names are ambiguous.

Also scan nearby text in those files for indirect references to the target entity that the script missed because they use a phrasing not in the aliases list. If you find such references, link them.

### Step 5: Unresolved link report (optional)

Run the unresolved links report to show the current state of phantom links:

```powershell
scripts/unresolved-links.ps1 -VaultPath <vault-root>
```

This groups all links pointing to non-existent files by target, sorted by reference count. The most-referenced missing targets are natural candidates for the next note to write.

Report this to the calling session only if specifically requested, or if the count of new unresolved links created in this pass is notable (5+).

---

## Frontmatter Linking

The deterministic scripts do not modify frontmatter. Frontmatter entity links (factions, members, characters, region, location, up) should be written correctly by the skill that creates the note, using the format documented in CONTEXT.md:

```yaml
factions: ["[Household Name](notes/Household Name.md)"]
characters: ["[Name](notes/Name.md)"]
region: "[The Valley](notes/The Valley.md)"
```

If frontmatter links are missing or use the wrong format, fix them during the LLM review step.

---

## Link Format Reference

All links use standard markdown format with vault-root-relative paths:

```
[Display Name](notes/Display Name.md)
```

- The filename matches the display name (no case conversion or hyphenation)
- Paths are relative to the vault root
- Classification values (`layer`, `scope`, `date`) are also links: `"[surface](notes/surface.md)"`
- Empty links to non-existent files are valid and intentional

---

## Using Unresolved Links for World Expansion

When a session needs direction on what to build next, the unresolved links report is a natural source of expansion targets. The most-referenced phantom notes represent entities the world already talks about but hasn't defined — they are the organic next step.

```powershell
scripts/unresolved-links.ps1 -VaultPath <vault-root>
```

The output sorted by reference count tells you: "these are the things your world keeps mentioning but hasn't built yet." The world-planning skill can use this as input for prioritizing Wide-phase work.

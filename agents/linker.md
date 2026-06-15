---
name: linker
description: Post-pass agent dispatched after any skill creates or edits vault notes. Runs deterministic scripts for forward/back-linking, then does an LLM review for entity references the scripts missed. Also handles unresolved link reports. Dispatch with the target file path(s) and vault root.
---

# Linker

Dispatched after a skill creates or edits note files. Ensures the vault's link graph is complete: forward links from the edited file to other notes, back-links from existing notes to the newly created file, and empty links to entities mentioned in text that have no note yet.

The process is script-heavy by design. The scripts handle deterministic work (matching known entity names to notes). The LLM handles judgment: identifying entity references the scripts can't catch.

## Input protocol

The dispatcher's prompt contains:
- **TargetFile**: path(s) of the file(s) that were created or modified (relative to vault root)
- **VaultPath**: path to the vault root

## Process

### Step 1: Inventory

Run the note inventory script:

```powershell
agents/linker/scripts/list-notes.ps1 -VaultPath <vault-root> -Pretty
```

Scan the output to understand the available link targets.

### Step 2: Deterministic forward + back linking

Run the linker script on the target file with reverse mode:

```powershell
agents/linker/scripts/link-notes.ps1 -TargetFile "notes/<filename>.md" -Reverse -VaultPath <vault-root>
```

This does two things:
1. **Forward links** — Scans the target file's body text for plain-text mentions of any note name or alias. Links the first unlinked occurrence per H2 section.
2. **Back-links** — Scans all other files for plain-text mentions of the target file's name and aliases. Links first unlinked occurrence per section in each file.

Use `-DryRun` first to preview changes if the edit scope seems large.

### Step 3: LLM review for unlisted entities

After the scripts run, read the target file and look for entity references the script could not catch:

**Named entities without notes:**
- Characters mentioned by name who have no note and aren't in any note's aliases
- Locations referenced by name that have no note
- Factions, groups, or organizations mentioned that have no note

**How to handle them:**
- Wrap each in a markdown link pointing to where the note would live: `[Mother's Name](notes/Mother's Name.md)`
- The target file does not need to exist. An empty link marks the reference as a potential expansion point.
- Link on first mention per section, same as the script convention.
- Do NOT create notes for these entities. Just create the empty links.

**What to skip:**
- Generic references that aren't specific entities ("his friends", "the townspeople")
- References that are clearly not note-worthy
- The note's own name in its own text

**Decision guidance:** If someone might someday want to click this name and read more about it, link it. If the name is just background color, leave it.

### Step 4: Back-link review

Read the files the script modified in Step 2. Verify the script's work — no false matches, no links to the wrong note when names are ambiguous.

Also scan nearby text in those files for indirect references to the target entity that the script missed because they use a phrasing not in the aliases list. If found, link them.

### Step 5: Unresolved link report (optional)

Run the unresolved links report:

```powershell
agents/linker/scripts/unresolved-links.ps1 -VaultPath <vault-root>
```

Groups all links pointing to non-existent files by target, sorted by reference count. Report this only if specifically requested, or if the count of new unresolved links created in this pass is notable (5+).

## Frontmatter linking

The deterministic scripts do not modify frontmatter. Frontmatter entity links should be written correctly by the skill that creates the note:

```yaml
factions: ["[Household Name](notes/Household Name.md)"]
characters: ["[Name](notes/Name.md)"]
region: "[The Valley](notes/The Valley.md)"
```

If frontmatter links are missing or use the wrong format, fix them during the LLM review step.

## Link format reference

All links use standard markdown format with vault-root-relative paths:

```
[Display Name](notes/Display Name.md)
```

- The filename matches the display name (no case conversion or hyphenation)
- Paths are relative to the vault root
- Classification values (`layer`, `scope`, `date`) are also links: `"[surface](notes/surface.md)"`
- Empty links to non-existent files are valid and intentional

## Return protocol

Return a summary containing:
- Files modified (forward-linked and back-linked)
- New empty links created (entity name + target path)
- Any ambiguous matches or corrections made during review
- Unresolved link count if reported

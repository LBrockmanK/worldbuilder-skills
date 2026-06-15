---
name: worldbuilder-setup
description: Use when starting a new worldbuilding project from scratch. Runs once, before any other worldbuilder skill. Copies the worldvault template into the user's project directory, asks for a project name, and hands off to worldbuilder-world-planning.
---

# Worldbuilder Setup

## Overview

This skill initializes a new worldbuilding project. It copies the pre-configured vault template into the user's designated project directory, writes in the project name, and hands off to `worldbuilder-world-planning`.

Run this skill once per project, before any other worldbuilder skill. It does not ask creative questions — genre, tone, cast, and setting all belong in world-planning and world-foundation.

---

## Working with Vault Files

**Renaming a note:** Use Edit or Write to rename the file. Then immediately run `agents/linker/scripts/rename-note.ps1 -OldName "OldName" -NewName "NewName" -VaultPath <vault-root>` to update all markdown links across the vault. Do not skip this step — Obsidian's auto-rename is bypassed when files are edited directly.

---

## Steps

### Step 1: Identify the skill directory

The `worldvault/` folder that accompanies this skill file is the vault template. Locate it at the same directory level as this SKILL.md file.

### Step 2: Confirm the vault location

Propose a default and offer two opt-outs:

> "I'll copy the vault template into a `worldvault/` subfolder here. Let me know if you'd prefer a different location, or if you'd like to use the current directory itself as the vault."

Three branches — handle exactly one:

**Branch A — Default `worldvault/` subfolder or any named subfolder:**
If the path does not yet exist, create it and proceed to Step 3. If it exists and is empty, proceed to Step 3. If it exists and is **not empty** — stop. Do not touch any existing files. Say: "That folder already has files in it. Please specify a different path." Wait for a new path before continuing.

**Branch B — Root directory as vault, directory is empty:**
Proceed to Step 3 directly.

**Branch C — Root directory as vault, directory has existing files:**
Say:
> "This directory has existing files. I can move them into a `_source/` subfolder to make room for the vault template — please confirm before I move anything, or give me a different location instead."
Do not move any files until the user explicitly confirms. The `_source/` move is valid only in this branch, only after confirmation. Do not improvise it as a workaround for Branch A.

### Step 3: Copy worldvault/ into the project directory

Copy all contents of `worldvault/` into the user's specified project directory. Preserve the full structure:
- `.obsidian/` and all files within
- Content folder: `notes/`
- `_templates/`, `_attachments/`, `_bases/`
- All stub notes: `Home.md`, `worldbuilding-plan.md`, `log.md`, `seed.md`, `agent-context.md`

PowerShell:
```powershell
Copy-Item -Path "<skill-directory>/worldvault/*" -Destination "<project-directory>" -Recurse -Force
# Also copy hidden .obsidian directory explicitly:
Copy-Item -Path "<skill-directory>/worldvault/.obsidian" -Destination "<project-directory>/.obsidian" -Recurse -Force
```

Bash (macOS/Linux):
```bash
cp -r "<skill-directory>/worldvault/." "<project-directory>/"
```

### Step 4: Ask for project name

Ask:

> "What is the name of your world or project?"

Replace the `{{PROJECT_NAME}}` placeholder in two files in the project directory:

In `<project-directory>/worldbuilding-plan.md`, replace:
```
# {{PROJECT_NAME}} — Worldbuilding Plan
```
with:
```
# <ProjectName> — Worldbuilding Plan
```

In `<project-directory>/Home.md`, replace:
```
# {{PROJECT_NAME}}
```
with:
```
# <ProjectName>
```

### Step 5: Confirm and hand off

Confirm:

> "Your vault is ready at `<project-directory>`. Open it in Obsidian as a vault — use 'Open folder as vault' and point it to that folder. Then start with `worldbuilder-world-planning` to begin the Seed phase."

---

## What this skill does not do

- No creative questions. Genre, tone, setting, cast — those belong in world-planning and world-foundation.
- No Obsidian Sync configuration — user decision, handled manually.
- No plugin installation. No community plugins are included or required.
- No cloud integration. The vault is a local directory.

---
name: worldbuilder-setup
description: Use when starting a new worldbuilding project from scratch. Runs once, before any other worldbuilder skill. Copies the worldvault template into the user's project directory, asks for a project name, and hands off to worldbuilder-world-planning.
---

# Worldbuilder Setup

## Overview

This skill initializes a new worldbuilding project. It copies the pre-configured vault template into the user's designated project directory, writes in the project name, and hands off to `worldbuilder-world-planning`.

Run this skill once per project, before any other worldbuilder skill. It does not ask creative questions — genre, tone, cast, and setting all belong in world-planning and world-foundation.

---

## Steps

### Step 1: Identify the skill directory

The `worldvault/` folder that accompanies this skill file is the vault template. Locate it at the same directory level as this SKILL.md file.

### Step 2: Ask for the project directory

Ask:

> "Where should the project vault be created? Provide the full path to a new, empty folder — I'll copy the vault template there."

Wait for their answer. Confirm the target path either exists and is empty, or does not yet exist. If it does not exist, ask whether to create it.

### Step 3: Copy worldvault/ into the project directory

Copy all contents of `worldvault/` into the user's specified project directory. Preserve the full structure:
- `.obsidian/` and all files within
- Content folders: `characters/`, `locations/`, `factions/`, `concepts/`, `story/`
- `_templates/`, `_attachments/`
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

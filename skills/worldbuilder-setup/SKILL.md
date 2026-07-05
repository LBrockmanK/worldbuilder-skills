---
name: worldbuilder-setup
description: Use when starting a new worldbuilding project. Adopts scraibe with the worldbuilder OKF preset, installs the vault chrome, and hands off to worldbuilder-world-foundation.
---

# Worldbuilder Setup

## Overview

This skill turns a directory into a worldbuilding project: scraibe's OKF machinery configured with the worldbuilder type registry, an Obsidian vault around it, and the three project documents created. Run it once per project, before any other worldbuilder skill.

Scraibe owns file management from here on — document creation, frontmatter enforcement, status lifecycle, inbox, audit. This skill only writes the configuration and chrome, then gets out of the way. It asks no creative questions; genre, tone, cast, and setting belong to `worldbuilder-world-foundation`.

The project root is the directory the user is working in. If they want the vault somewhere else, ask them to name the directory and use that as the project root throughout.

## Steps

### Step 1: Check scraibe

Glob `~/.claude/plugins/marketplaces/*/scraibe/scripts/new_doc.py`. If nothing matches, stop: "This plugin requires the scraibe plugin. Install it first."

Record the matched scraibe plugin root (the directory containing `scripts/`) — later steps use its scripts and defaults. Never hardcode this path; resolve it fresh each run.

### Step 2: Write the config

Ask: "What is the name of your world or project?"

Copy this plugin's `defaults/okf.json` to `<project>/.claude/okf.json`. If `<project>/.claude/okf.json` already exists, stop — do not overwrite it. Say the project is already configured and suggest running `scraibe:setup` in configuration mode to change the registry.

### Step 3: Install the chrome

- Copy `<scraibe>/defaults/obsidian/` to `<project>/.obsidian/`.
- Overlay this skill's `worldvault/.obsidian/app.json` on top (it sets the attachment folder and link behavior).
- Copy this skill's `worldvault/Home.md` to the project root, replacing `{{PROJECT_NAME}}` with the project name.
- Copy this skill's `worldvault/_bases/` directory to `<project>/_bases/`.
- Create empty directories: `notes/`, `project/`, `_attachments/`.

Chrome lives at the vault root, outside the enforced paths — `Home.md` and the Bases carry no OKF frontmatter, and that is correct.

### Step 4: Create the project documents

Create the three `project/` documents with scraibe's `new_doc.py`, from the project root:

```
python <scraibe>/scripts/new_doc.py --config .claude/okf.json --dir project --type seed --title "<Name> World Foundation"
python <scraibe>/scripts/new_doc.py --config .claude/okf.json --dir project --type plan --title "<Name> Worldbuilding Plan"
python <scraibe>/scripts/new_doc.py --config .claude/okf.json --dir project --type direction --title "<Name> Story Direction"
```

Then seed `.claude/glossary.md` with the platform terminology:

```markdown
**lorebook** — the platform term is "world info" on ainime/isekaizero; both name the same thing. _Avoid_: world info (in vault docs).
```

### Step 5: Generate rules, validate, hand off

```
python <scraibe>/scripts/generate_rules.py --root .
python <scraibe>/scripts/validate.py project --root . --format human
```

Report the validation result to the user. Tell them the vault is ready to open in Obsidian ("Open folder as vault" on the project root; Bases need Obsidian 1.8+ with the Bases core plugin). Then hand off to `worldbuilder-world-foundation` for the seed conversation.

## What this skill does not do

- No creative questions — those belong to `worldbuilder-world-foundation`.
- No migration of pre-scraibe worldbuilder vaults — that is a `scraibe:setup` migration run with this registry.
- No Obsidian Sync configuration, plugin installation, or cloud integration.

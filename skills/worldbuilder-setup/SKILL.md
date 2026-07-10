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

Resolve the scraibe plugin root — the directory containing `scripts/new_doc.py`:

1. Read `~/.claude/plugins/installed_plugins.json` and take the `installPath` of the entry whose key starts with `scraibe@`.
2. If that file or key is missing, fall back to globbing `~/.claude/plugins/marketplaces/*/*/scripts/new_doc.py` — the plugin's directory is not necessarily named `scraibe` (in the fleet monorepo it is `okf-enforcement`).

If neither resolves, stop: "This plugin requires the scraibe plugin. Install it first."

Record the resolved root — later steps use its scripts and defaults. Never hardcode this path; resolve it fresh each run.

### Step 2: Write the config

Ask: "What is the name of your world or project?"

Copy this plugin's `defaults/okf.json` to `<project>/.claude/okf.json`. If `<project>/.claude/okf.json` already exists, stop — do not overwrite it. Say the project is already configured and suggest running `scraibe:setup` in configuration mode to change the registry.

### Step 3: Install the chrome

- Copy `<scraibe>/defaults/obsidian/` to `<project>/.obsidian/`.
- Overlay this skill's `worldvault/.obsidian/` directory on top (app config, community-plugin registration, and the vendored Templater plugin).
- Copy this skill's `worldvault/Home.md` to the project root, replacing `{{PROJECT_NAME}}` with the project name.
- Copy this skill's `worldvault/_bases/` directory to `<project>/_bases/`.
- Create empty directories: `notes/`, `project/`, `_attachments/`.

Chrome lives at the vault root, outside the enforced paths — `Home.md` and the Bases carry no OKF frontmatter, and that is correct.

### Step 4: Create the project documents

Create the three `project/` documents with scraibe's `new_doc.py`, from the project root. The script produces date-prefixed filenames; rename each to its canonical name afterward so every skill can reference `project/seed.md`, `project/plan.md`, and `project/direction.md` reliably.

```
python <scraibe>/scripts/new_doc.py --config .claude/okf.json --dir project --type seed --title "<Name> World Foundation" --description "World foundation document for <Name>"
  → rename the output file to project/seed.md

python <scraibe>/scripts/new_doc.py --config .claude/okf.json --dir project --type plan --title "<Name> Worldbuilding Plan" --description "Phase status and cast plan for <Name>"
  → rename the output file to project/plan.md

python <scraibe>/scripts/new_doc.py --config .claude/okf.json --dir project --type direction --title "<Name> Story Direction" --description "Standing creative brief for <Name>"
  → rename the output file to project/direction.md
```

Then seed `.claude/glossary.md` with the platform terminology:

```markdown
**lorebook** — the platform term is "world info" on ainime/isekaizero; both name the same thing. _Avoid_: world info (in vault docs).
```

### Step 5: Generate the creation templates

From the project root, with this plugin's root recorded as `<worldbuilder>`:

    python <worldbuilder>/scripts/generate_templates.py --config .claude/okf.json --out . \
      --dir "notes/=character,location,faction,event,concept,story" \
      --dir "project/=seed,plan,direction" \
      --obsidian

This writes `_templates/` (one template per type plus a type-picker per
directory) and points the vendored Templater's folder attachments at
them. From here on, a note created in `notes/` or `project/` inside
Obsidian receives compliant frontmatter at creation — the type-picker
asks one question in mixed directories.

### Step 6: Generate rules, validate, hand off

```
python <scraibe>/scripts/generate_rules.py --root .
python <scraibe>/scripts/validate.py project --root . --format human
```

Report the validation result to the user. Tell them the vault is ready to open in Obsidian ('Open folder as vault' on the project root; Bases and the vendored Templater need Obsidian 1.12.2+ with community plugins enabled for this vault). Then hand off to `worldbuilder-world-foundation` for the seed conversation.

## What this skill does not do

- No creative questions — those belong to `worldbuilder-world-foundation`.
- No migration of pre-scraibe worldbuilder vaults — that is a `scraibe:setup` migration run with this registry.
- No Obsidian Sync configuration, plugin installation, or cloud integration.

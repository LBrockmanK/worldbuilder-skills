---
name: worldbuilder-setup
description: Use when starting a new worldbuilding project. Installs the vault chrome and creation templates onto a scraibe-enabled project and hands off to worldbuilder-world-foundation.
---

# Worldbuilder Setup

## Overview

This skill turns a directory into a worldbuilding project: an Obsidian vault with worldbuilder's creation templates wired in, and the three project documents created. Run it once per project, before any other worldbuilder skill.

Scraibe owns file management from here on — document creation, frontmatter enforcement, status lifecycle, inbox, audit. This skill only installs the chrome and templates, then gets out of the way. It asks no creative questions; genre, tone, cast, and setting belong to `worldbuilder-world-foundation`.

**This skill writes no configuration into the project.** The worldbuilder type roster lives in this plugin, at `defaults/types.json`, and is read from there whenever it is needed. A project does not get a copy. What makes a project a worldbuilder project is that scraibe and this plugin are *enabled* for it — see Step 2.

The project root is the directory the user is working in. If they want the vault somewhere else, ask them to name the directory and use that as the project root throughout.

## Steps

### Step 1: Check scraibe

Resolve the scraibe plugin root — the directory containing `scripts/new_doc.py`:

1. Read `~/.claude/plugins/installed_plugins.json` and take the `installPath` of the entry whose key starts with `scraibe@`.
2. If that file or key is missing, fall back to globbing `~/.claude/plugins/marketplaces/*/*/scripts/new_doc.py` — the plugin's directory is not necessarily named `scraibe` (older installs used `okf-enforcement`).

If neither resolves, stop: "This plugin requires the scraibe plugin. Install it first."

Record the resolved root — later steps use its scripts and defaults. Never hardcode this path; resolve it fresh each run.

### Step 2: Check the project is adopted

Adoption is plugin enablement, and fleet:setup is its sole writer. Resolve the fleet plugin root the same way as Step 1 (the entry whose key starts with `fleet@`), then, from the project root:

```
python "<fleet>/scripts/plugin_enablement.py" --root . status
python "<fleet>/scripts/plugin_enablement.py" --root . show
```

Both conditions must hold:

- `status` exits 0 — a plugin selection is recorded for this project. Exit 1 means no selection exists at all: **stop** and tell the user to run `fleet:setup` in this project first.
- `show` lists both scraibe and this plugin as `enabled`. The marketplace suffix varies by install (`scraibe@<marketplace>`); match on the plugin name before the `@`. If either is missing or reads `disabled`, **stop** and tell the user to run `fleet:setup` and enable scraibe and worldbuilder-workflow for this project.

Do not work around a failed check by writing config into the project — there is no config to write, and proceeding would make "adopted" mean nothing.

Then ask: "What is the name of your world or project?"

### Step 3: Install the chrome

- Copy `<scraibe>/defaults/obsidian/` to `<project>/.obsidian/`.
- Overlay this skill's `worldvault/.obsidian/` directory on top (app config, community-plugin registration, and the vendored Templater plugin).
- Copy this skill's `worldvault/Home.md` to the project root, replacing `{{PROJECT_NAME}}` with the project name.
- Copy this skill's `worldvault/_bases/` directory to `<project>/_bases/`.
- Create empty directories: `notes/`, `project/`, `_attachments/`.

Chrome lives at the vault root — `Home.md` and the Bases carry no vault frontmatter, and that is correct. Scraibe's corpus rule excludes reserved spaces (`+/`, `repo/`, `.claude/`, `Imports/`), so nothing there is validated as a vault document.

### Step 4: Create the project documents

Create the three `project/` documents with scraibe's `new_doc.py`, from the project root. The script produces date-prefixed filenames; rename each to its canonical name afterward so every skill can reference `project/seed.md`, `project/plan.md`, and `project/direction.md` reliably.

```
python <scraibe>/scripts/new_doc.py --dir project --type seed --title "<Name> World Foundation" --description "World foundation document for <Name>"
  → rename the output file to project/seed.md

python <scraibe>/scripts/new_doc.py --dir project --type plan --title "<Name> Worldbuilding Plan" --description "Phase status and cast plan for <Name>"
  → rename the output file to project/plan.md

python <scraibe>/scripts/new_doc.py --dir project --type direction --title "<Name> Story Direction" --description "Standing creative brief for <Name>"
  → rename the output file to project/direction.md
```

`new_doc.py` takes no registry: `type` is an open value, and it writes frontmatter plus whatever body scaffold scraibe ships for that type. These three documents get their real bodies from Step 5's Templater templates and from `worldbuilder-world-foundation`, so a thin scaffold here is expected and fine.

Then seed `.claude/glossary.md` with the platform terminology:

```markdown
**lorebook** — the platform term is "world info" on ainime/isekaizero; both name the same thing. _Avoid_: world info (in vault docs).
```

### Step 5: Generate the creation templates

From the project root, with this plugin's root recorded as `<worldbuilder>`:

    python <worldbuilder>/scripts/generate_templates.py --out . \
      --dir "notes/=character,location,faction,event,concept,story" \
      --dir "project/=seed,plan,direction" \
      --obsidian

The generator reads its type roster from this plugin's own
`defaults/types.json` — there is no `--config`, and nothing is read from
the project.

This writes `_templates/` (one template per type plus a type-picker per
directory) and points the vendored Templater's folder attachments at
them. From here on, a note created in `notes/` or `project/` inside
Obsidian receives compliant frontmatter at creation — the type-picker
asks one question in mixed directories.

### Step 6: Validate and hand off

```
python <scraibe>/scripts/validate.py project --root . --format human
```

There is no rules-generation step: scraibe retired `generate_rules.py` and the generated-rules mechanism with it. Project conventions live in the project's own `CLAUDE.md`, which `scraibe:setup` maintains.

Report the validation result to the user. Tell them the vault is ready to open in Obsidian ('Open folder as vault' on the project root; Bases and the vendored Templater need Obsidian 1.12.2+ with community plugins enabled for this vault). Then hand off to `worldbuilder-world-foundation` for the seed conversation.

## What this skill does not do

- No creative questions — those belong to `worldbuilder-world-foundation`.
- No migration of pre-scraibe worldbuilder vaults — that is a `scraibe:setup` migration run.
- No plugin enablement — that is `fleet:setup`'s job. This skill only checks it.
- No Obsidian Sync configuration, plugin installation, or cloud integration.

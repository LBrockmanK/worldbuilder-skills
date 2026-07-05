---
type: plan
title: 'Retool implementation: worldbuilder on scraibe'
description: 'Task-by-task implementation of the 2026-07-04 retool spec: OKF preset
  build, setup adopter rewrite, skill pare-down, deletions, docs, and scratch-project
  verification.'
tags:
- complete
date: 2026-07-05
timestamp: 2026-07-05T07:36
resources:
- '[[2026-07-04-retool-worldbuilder-skills-on-scraibe-base]]'
---

# Retool implementation: worldbuilder on scraibe

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Retool the worldbuilder plugin to run on scraibe as its base: ship an OKF preset instead of a vault template, reduce eleven skills to nine craft/adopter/exporter skills with no file-management content, and verify the result in a scratch project.

**Architecture:** The plugin ships `defaults/okf.json` (built by `scripts/build-okf.py` from markdown template sources in `defaults/templates/`) plus a chrome overlay (`Home.md`, `_bases/`). `worldbuilder-setup` becomes a five-step adopter; scraibe's loop (orient/triage/audit/inbox) replaces the world-planning router; craft skills keep doctrine only. Spec: `.claude/specs/2026-07-04-retool-worldbuilder-skills-on-scraibe-base.md`.

**Tech Stack:** Markdown skill files, Python 3 (build script only), Obsidian Bases syntax, scraibe scripts (`new_doc.py`, `generate_rules.py`, `validate.py`).

## Global Constraints

- Never name a specific AI model in vault templates or skill content — model-neutral phrasing only ("future agents", not a product name).
- Skill prose follows the plugin's own writing doctrine: plain, concrete, no filler.
- Scraibe is a hard dependency. Skills locate its scripts by globbing `~/.claude/plugins/marketplaces/*/scraibe/scripts/` and stop with a clear message if absent. Never hardcode an absolute scraibe path in shipped skill content.
- OKF universal frontmatter (every typed doc): `type`, `title`, `description`, `tags` (exactly one status: `human-ready`/`agent-ready` open, `complete`/`deprecated`/`abandoned`/`archived` closed), `date`, `timestamp`, `resources`.
- Commit after every task with a conventional message; this repo's commits end with the Claude co-author line.
- This repo's own vault is enforced: docs under `.claude/` subdirs must stay OKF-valid (the hooks will police your edits — that is expected, not an error).

---

### Task 1: Template sources and build-okf.py

**Files:**
- Create: `defaults/templates/character.md`, `location.md`, `faction.md`, `event.md`, `concept.md`, `story.md`, `seed.md`, `plan.md`
- Create: `defaults/okf.base.json`
- Create: `scripts/build-okf.py`
- Modify: `defaults/okf.json` (becomes generated output; committed)

**Interfaces:**
- Produces: `defaults/okf.json` — consumed verbatim by Task 2's setup skill and Task 8's scratch trial. `python scripts/build-okf.py` regenerates it; exits non-zero if a template file named in `okf.base.json` is missing.

- [x] **Step 1: Create the eight template sources.** For character, location, faction, concept, story: copy the body (everything after the closing `---` of frontmatter) byte-for-byte from `skills/worldbuilder-setup/worldvault/_templates/<name>.md` — with one exception: in `story.md`, the sentence "the standing creative brief lives in `direction.md` (type: project), not in a story note" becomes "the standing creative brief lives in `project/direction.md` (type: direction), not in a story note". For the three new files use exactly:

`defaults/templates/event.md`:
```markdown
> For future agents: this is an event note. The filename is the event's name. Use `worldbuilder-event` to build it out. Timing (season, day, recurrence) belongs in the opening of What Happens, not in frontmatter.

## Design Notes

## What Happens

## Scene Effects
```

`defaults/templates/seed.md`:
```markdown
> For future agents: this is the world foundation document, produced by `worldbuilder-world-foundation` during the Seed phase.
```

`defaults/templates/plan.md`:
```markdown
> For future agents: this is the project plan. Read it at the start of a session when orienting.

## Phase Status

| Phase | Status | Notes |
|---|---|---|
| Seed | Not started | |
| Wide | Not started | |
| Export | Not started | |

## Cast Plan
```

- [x] **Step 2: Create `defaults/okf.base.json`** — the full config from the current committed `defaults/okf.json`, but with every `"template"` value replaced by a file reference key instead: `"template_file": "character.md"` (same for the other seven; `direction` and `reference` keep `"template": ""` and get no `template_file`).

- [x] **Step 3: Write `scripts/build-okf.py`:**
```python
#!/usr/bin/env python3
"""Regenerate defaults/okf.json from okf.base.json + defaults/templates/*.md."""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = os.path.join(ROOT, 'defaults', 'okf.base.json')
TEMPLATES = os.path.join(ROOT, 'defaults', 'templates')
OUT = os.path.join(ROOT, 'defaults', 'okf.json')


def main():
    with io.open(BASE, encoding='utf-8') as f:
        config = json.load(f)
    for name, spec in config.get('types', {}).items():
        ref = spec.pop('template_file', None)
        if ref is None:
            continue
        path = os.path.join(TEMPLATES, ref)
        if not os.path.isfile(path):
            sys.exit(f'Missing template file: {path}')
        with io.open(path, encoding='utf-8') as f:
            spec['template'] = f.read()
    with io.open(OUT, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(config, f, indent=2, ensure_ascii=False)
        f.write('\n')
    print(f'Wrote {OUT}')


if __name__ == '__main__':
    main()
```

- [x] **Step 4: Run and verify.** `python scripts/build-okf.py` → `Wrote .../defaults/okf.json`. Then verify the output is a superset-equal of the previous committed draft except the three new/changed templates: `python -c "import json;c=json.load(open('defaults/okf.json'));print(sorted(c['types']));print(all(c['types'][t]['template'] for t in ['character','location','faction','event','concept','story','seed','plan']))"` → prints the ten type names and `True`. Delete one template file temporarily, run again, confirm non-zero exit with `Missing template file`, restore it (`git checkout -- defaults/templates/`).

- [x] **Step 5: Commit.** `git add defaults scripts && git commit -m "feat: build OKF preset from markdown template sources"`

---

### Task 2: worldbuilder-setup rewrite and chrome overlay

**Files:**
- Rewrite: `skills/worldbuilder-setup/SKILL.md`
- Delete: `skills/worldbuilder-setup/worldvault/_templates/` (5 files), `worldvault/seed.md`, `worldvault/worldbuilding-plan.md`, `worldvault/log.md`, `worldvault/agent-context.md`, all of `worldvault/.obsidian/`
- Create: `skills/worldbuilder-setup/worldvault/.obsidian/app.json`
- Modify: `skills/worldbuilder-setup/worldvault/Home.md`, all files in `worldvault/_bases/` (7 existing), create `worldvault/_bases/events.base`

**Interfaces:**
- Consumes: `defaults/okf.json` from Task 1.
- Produces: the setup flow that Task 8's scratch trial executes; `_bases` views that filter on OKF frontmatter (`tags`, `timestamp`, `description`).

- [x] **Step 1: Rewrite SKILL.md** with this structure (write full prose; keep frontmatter name/description, update description to "Use when starting a new worldbuilding project. Adopts scraibe with the worldbuilder OKF preset, installs the vault chrome, and hands off to worldbuilder-world-foundation."):
  1. *Check scraibe.* Glob `~/.claude/plugins/marketplaces/*/scraibe/scripts/new_doc.py`; if absent, stop: "This plugin requires the scraibe plugin. Install it first." Record the matched scraibe root for later steps.
  2. *Write config.* Ask for the project name. Copy this plugin's `defaults/okf.json` to `<project>/.claude/okf.json` (do not overwrite an existing one — if present, stop and suggest `scraibe:setup` configuration mode).
  3. *Install chrome.* Copy `<scraibe>/defaults/obsidian/` to `<project>/.obsidian/`, then overlay this plugin's `worldvault/.obsidian/app.json`. Copy `worldvault/Home.md` (substitute `{{PROJECT_NAME}}`), `worldvault/_bases/`, and create empty `notes/`, `project/`, `_attachments/`.
  4. *Create project docs.* Via `<scraibe>/scripts/new_doc.py --config .claude/okf.json --dir project`: `--type seed --title "<Name> World Foundation"`, `--type plan --title "<Name> Worldbuilding Plan"`, `--type direction --title "<Name> Story Direction"`. Seed `.claude/glossary.md` with: `**lorebook** — the platform term is "world info" on ainime/isekaizero; both name the same thing. _Avoid_: world info (in vault docs).`
  5. *Generate and validate.* `python <scraibe>/scripts/generate_rules.py --root .` then `python <scraibe>/scripts/validate.py project --root . --format human`; report, then hand off to `worldbuilder-world-foundation` for the seed conversation.
- [x] **Step 2: Prune worldvault.** `git rm -r skills/worldbuilder-setup/worldvault/_templates skills/worldbuilder-setup/worldvault/.obsidian` and `git rm skills/worldbuilder-setup/worldvault/{seed.md,worldbuilding-plan.md,log.md,agent-context.md}`. Create `worldvault/.obsidian/app.json`:
```json
{
  "alwaysUpdateLinks": true,
  "showUnsupportedFiles": true,
  "attachmentFolderPath": "_attachments"
}
```
- [x] **Step 3: Rewrite the Bases.** Every `.base` file: filters drop `not file.inFolder("_templates")` and gain `file.inFolder("notes")` (`project-docs.base` uses `file.inFolder("project")`); status views become tag views; columns replace `status`→`tags`, `last_updated`→`timestamp`, add `description`. Pattern (apply per type; `characters.base` shown in full):
```yaml
filters:
  and:
    - 'type == "character"'
    - file.inFolder("notes")

views:
  - type: table
    name: All
    order:
      - file.name
      - description
      - tags
      - factions
      - timestamp

  - type: table
    name: Open
    filters:
      or:
        - tags.contains("human-ready")
        - tags.contains("agent-ready")
    order:
      - file.name
      - description
      - tags
      - factions
      - timestamp

  - type: table
    name: Complete
    filters: 'tags.contains("complete")'
    order:
      - file.name
      - description
      - tags
      - factions
      - timestamp
```
  Type-specific columns replacing `factions` above — locations: `region`, `function`; factions: `members`, `function`; concepts: `layer`, `trigger-context`; story: `scope`, `up`; events: `characters`, `location`, `layer`; all-notes: `type` only; project-docs: `type` only. Create `events.base` with the pattern. Add an `## Events` section embedding `![[events.base]]` to `Home.md` (after Factions).
- [x] **Step 4: Verify.** `grep -rn "last_updated\|status ==\|_templates" skills/worldbuilder-setup/worldvault/` → no matches. `ls skills/worldbuilder-setup/worldvault/` → `Home.md`, `_attachments`, `_bases`, `.obsidian` only.
- [x] **Step 5: Commit.** `git add -A skills/worldbuilder-setup && git commit -m "feat: setup becomes scraibe adopter; worldvault reduced to chrome"`

---

### Task 3: Move cast planning into world-foundation; retire world-planning

**Files:**
- Modify: `skills/worldbuilder-world-foundation/SKILL.md`
- Delete: `skills/worldbuilder-world-planning/` (entire directory)

**Interfaces:**
- Consumes: nothing from other tasks (content move within skill prose).
- Produces: `worldbuilder-world-foundation` as the sole owner of seed + cast planning; no skill references `worldbuilder-world-planning` afterward (Task 7 sweeps).

- [x] **Step 1: Extract the survivors from world-planning.** From `skills/worldbuilder-world-planning/SKILL.md` copy the *content* (not the routing) of: the Wide-phase cast-plan portions of `## Three-Phase Framework` (the phase 2f cast-planning process: roster from household design, coverage check against seed themes), `## Phase Completion Criteria` (the per-phase "done" definitions), and `## Parallel Execution` (which Wide-phase note types can proceed independently and what blocks on what). Add to `skills/worldbuilder-world-foundation/SKILL.md` as a new `## Wide Phase Planning` section after `## Cast Architecture`, rewritten to address the *plan document* (`project/plan.md`) as the artifact: the cast plan lives in its `## Cast Plan` section, phase status in its table. Remove all "route to X skill" and session-start-assessment language — orient/triage own that now.
- [x] **Step 2: Update world-foundation's plumbing.** In `## Seed Document`: the seed is `project/seed.md`, already created by setup; the skill fills its body and sets its status tag to `complete` when confirmed. In `## Opening Act: Ingestion`: replace references to `worldbuilder-ingestion` with `scraibe:ingest` (capture sources as reference docs first, then extract). Delete any instruction to create files by hand or write frontmatter.
- [x] **Step 3: Delete the router.** `git rm -r skills/worldbuilder-world-planning`
- [x] **Step 4: Verify.** `grep -rn "world-planning" skills/` → only historical mentions inside `.claude/` docs remain (skills clean). `grep -n "Wide Phase Planning" skills/worldbuilder-world-foundation/SKILL.md` → present.
- [x] **Step 5: Commit.** `git commit -am "refactor: world-foundation absorbs cast planning; retire world-planning router"`

---

### Task 4: Craft-skill light pass (character, location, faction, concept, story)

**Files:**
- Modify: `skills/worldbuilder-character/SKILL.md` (+ `framework.md`, `relationships.md`, `intimate.md` if they reference paths/frontmatter), `skills/worldbuilder-location/SKILL.md`, `skills/worldbuilder-faction/SKILL.md`, `skills/worldbuilder-concept/SKILL.md`, `skills/worldbuilder-story/SKILL.md`

**Interfaces:**
- Consumes: registry field names from Task 1 (`description` not `brief`, `timestamp` not `last_updated`, status tags).
- Produces: skills whose only file-facing instruction is "create notes with scraibe's `new_doc.py`; the generated rules carry the schema."

Apply to each of the five skills, then the two insertions:

- [x] **Step 1: Delete plumbing sections.** Remove `## Working with Vault Files` (character:16, location:16, faction:18, concept:28, story:53), `## Frontmatter` / `## Concept Note Frontmatter` (character:38, location:38, faction:40, concept:34), and `## Brief` (character:56, location:58, faction:59, concept:54) — the Brief content-writing guidance (what a good one says) survives where it is genuinely about writing, folded into each skill's Overview as one short paragraph headed "**Description field:**" (1–2 behavioral sentences, written last). Replace each deleted frontmatter section with nothing; where the skill's note-structure section lists frontmatter properties, trim to a sentence: "Frontmatter is defined by the project's OKF registry; `new_doc.py` stamps it at creation and the generated rules describe it."
- [x] **Step 2: Retarget stale references.** In all five files replace `notes/` path prescriptions and any `status: draft`/`status: complete` phrasing with status-tag phrasing (`tags` carries one status; open while working, `complete` when the self-check passes). `last_updated`→ remove (automatic). References to the linker agent → delete the sentence (rules instruct agents to wikilink entity names inline).
- [x] **Step 3: Domain insertions.** `worldbuilder-concept` `## Lore` section, add: "Imported lorebook entries marked `constant` describe standing setting state — that is seed/world material for `project/seed.md`, not a concept note." `worldbuilder-character` `## Design Notes`, add if absent: "Imported character cards: judge by behavioral specificity, negative-track content, and connections; a card failing more than one needs the full pass, not transcription."
- [x] **Step 4: Verify.** `grep -rln "Working with Vault Files\|last_updated\|brief:" skills/worldbuilder-{character,location,faction,concept,story}/` → no matches; `grep -rn "status: draft" skills/` → no matches.
- [x] **Step 5: Commit.** `git commit -am "refactor: craft skills keep doctrine, drop file plumbing"`

---

### Task 5: Event skill heavy pass

**Files:**
- Modify: `skills/worldbuilder-event/SKILL.md`

**Interfaces:**
- Consumes: event registry entry from Task 1 (fields `characters`, `location`, `layer`; no in-world `date`, no `recurring`, no `brief`).

- [x] **Step 1:** Delete `## Working with Vault Files` (line 16) and `## Brief` (line 55; fold its content-guidance sentence into Overview as the "**Description field:**" paragraph per Task 4's pattern). Replace the whole `## Event Note Frontmatter` section (lines 34–53) with:
```markdown
## Event Note Fields

Frontmatter is defined by the project's OKF registry — `new_doc.py` stamps it and the generated rules describe it. Two writing notes: `aliases` carries every realistic way the event is mentioned in dialogue ("the festival," "harvest time"); the export skill derives keyword triggers from it. Timing — season, day, recurrence — is not a field: open What Happens with when the event takes place and how often.
```
- [x] **Step 2:** Update `## Lifecycle` (line 124): "stub" phrasing becomes status-tag phrasing (create early via `new_doc.py`, leave open; mark `complete` after the self-check).
- [x] **Step 3: Verify.** `grep -n "recurring\|last_updated\|brief\|status: draft" skills/worldbuilder-event/SKILL.md` → no matches (case-sensitive; "Brief" as a heading also gone).
- [x] **Step 4: Commit.** `git commit -am "refactor: event skill — timing to body text, registry owns frontmatter"`

---

### Task 6: Export skill update

**Files:**
- Modify: `skills/worldbuilder-ainime-export/SKILL.md`, `calendar.md`, `card-assembly.md`

**Interfaces:**
- Consumes: OKF frontmatter (`description`, status tags) from Task 1's registry.

- [x] **Step 1:** In all three files: every read of `brief` becomes `description`; every completeness check on `status` becomes a status-tag check (`## Prerequisites` gate: `project/seed.md` tagged `complete`, every exported character's note tagged with a closed status). Path references: notes live in `notes/`, project docs in `project/` (`seed.md`, `plan.md`, `direction.md` — not vault root). Event in-world dates: `calendar.md` mapping reads timing from each event's What Happens opening, not a `date` field.
- [x] **Step 2:** Confirm the `../../docs/target-system.md` reference still resolves (file is untouched); output format statements stay non-OKF.
- [x] **Step 3: Verify.** `grep -rn "brief\|status:\|last_updated" skills/worldbuilder-ainime-export/` → no matches except prose uses of the English word "brief" if any (rewrite those too for grep cleanliness).
- [x] **Step 4: Commit.** `git commit -am "refactor: export reads OKF frontmatter; paths to notes/ and project/"`

---

### Task 7: Deletions, repo docs, and leftover sweep

**Files:**
- Delete: `skills/worldbuilder-ingestion/`, `agents/` (linker already exported to scraibe repo), `dev-feedback.md`
- Rewrite: `CONTEXT.md`
- Modify: `README.md`, `CLAUDE.md`, `.claude-plugin/plugin.json` (description), `docs/agents/domain.md`, `memory/project-restructure.md`

**Interfaces:**
- Consumes: everything prior — this task documents the end state.

- [x] **Step 1: Delete.** `git rm -r skills/worldbuilder-ingestion agents && git rm dev-feedback.md`
- [x] **Step 2: Rewrite `CONTEXT.md`** (keep its role: single-context domain terminology). Required content, in this order: what the plugin is (craft skills + OKF preset on the scraibe base; scraibe owns file management); the player-vault layout diagram from the spec's "Vault layout" section, copied; the ten registry types with one-line definitions; the status-tag lifecycle (scraibe's six, what open/closed means for creative notes and export gating); the three phases as guidance (plan.md's table is the tracker; export skill gates itself); pointers — spec (`.claude/specs/2026-07-04-retool-worldbuilder-skills-on-scraibe-base.md`), `defaults/okf.json` + build script, `docs/target-system.md`.
- [x] **Step 3: Update the small files.** `README.md`: skill list to the nine survivors, add "Requires the scraibe plugin" line, terminology pointer stays. `CLAUDE.md`: no content about worldvault remains; add one line under the domain-docs section: "Requires scraibe (hard dependency); its vault conventions govern `.claude/`." `.claude-plugin/plugin.json`: description mentions scraibe base. `docs/agents/domain.md`: remove linker-agent mentions, fix any file-structure diagram to the new tree. `memory/project-restructure.md`: append a dated line to Implementation state: "2026-07-05: retool on scraibe base implemented — see spec/plan in .claude/; worldvault reduced to chrome; skills 11→9."
- [x] **Step 4: Leftover sweep (spec Verification #4).** Run and clear each: `grep -rn "world-planning\|worldbuilder-ingestion\|linker" skills/ README.md CONTEXT.md CLAUDE.md docs/agents/` and `grep -rn "log\.md\|agent-context\.md\|last_updated\|brief:" skills/ CONTEXT.md README.md`. Historical docs in `.claude/` are exempt (they describe the past).
- [x] **Step 5: Commit.** `git commit -am "feat: retool docs and deletions — plugin is craft skills + preset on scraibe"`

---

### Task 8: Scratch-project trial (spec Verification #1–3)

**Files:**
- Create (scratch only, not committed): a throwaway project directory under the session scratchpad.

**Interfaces:**
- Consumes: the full retooled plugin.

- [x] **Step 1: Simulate setup.** In a fresh scratch dir, execute `worldbuilder-setup`'s steps literally as the skill now states them (glob scraibe, copy config, chrome, `new_doc.py` × 3, glossary, `generate_rules.py`, `validate.py`). Expected: validation reports 0 critical on `project/`.
- [x] **Step 2: Entity round-trip.** Create one character and one event via `new_doc.py --config .claude/okf.json --dir notes`; fill each body minimally per its template sections; run `python <scraibe>/scripts/validate.py notes --root <scratch> --format human`. Expected: 0 critical, 0 warning.
- [x] **Step 3: Export dry-run.** Walk `worldbuilder-ainime-export`'s Prerequisites and Field Map against the scratch vault manually (no platform upload): confirm the skill's instructions locate `description`, status tags, and `project/seed.md` where they now are — i.e., following the text verbatim hits no dead reference. Fix any skill text that misdirects, amend the relevant commit's file, re-run.
- [x] **Step 4: Report.** Record pass/fail per check in the plan checkboxes here and note anything odd in `.claude/inbox.md`. Remind the user of the one human check remaining: open the scratch vault in Obsidian and confirm Home.md's Bases render (spec Verification #5).
- [x] **Step 5: Final commit if fixes occurred**, then `python <scraibe>/scripts/generate_index.py .claude/plans` and mark this plan's status tag `complete`.

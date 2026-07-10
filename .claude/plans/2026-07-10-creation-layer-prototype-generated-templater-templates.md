---
type: plan
title: 'Creation-layer prototype: generated Templater templates'
description: 'Implementation plan for the human-compliance-stack creation layer: generate_templates.py
  emitting per-type Templater templates and type-pickers from okf.json, Templater
  2.23.1 vendored into the worldbuilder chrome, trialed in the Emberwick scratch vault,
  built for immediate graduation to okf-enforcement'
tags:
- agent-ready
date: 2026-07-10
timestamp: 2026-07-10T00:12Z
resources: []
---

# Creation-layer prototype: generated Templater templates

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Humans creating notes in a scraibe vault get compliant OKF frontmatter before their first keystroke: `generate_templates.py` derives Templater templates from `okf.json`, Templater 2.23.1 ships vendored and configured in the worldbuilder chrome, and the Emberwick scratch vault proves the flow.

**Architecture:** The generator is a sibling of scraibe's `generate_rules.py` — pure stdlib Python reading the registry, emitting one template per type plus a suggester-based type-picker per mixed-type directory into `_templates/`, and (with `--obsidian`) pointing the vendored Templater `data.json` `folder_templates` at them. It contains zero worldbuilder-specific logic and graduates verbatim to `okf-enforcement/scripts/` at the merge point. Spec: fleet vault `.claude/specs/2026-07-09-vault-human-compliance-stack.md`.

**Tech Stack:** Python 3 stdlib (json, argparse, os), stdlib `unittest`; Templater 2.23.1 (pinned release assets); Obsidian Templater syntax (`tp.file.title`, `tp.system.suggester`, `tp.file.include`, global `moment`).

## Global Constraints

- Never name a specific AI model in shipped template content — model-neutral phrasing only.
- `generate_templates.py` must not import or hardcode anything worldbuilder-specific — directory/type mappings arrive via CLI arguments; it graduates to okf-enforcement unchanged.
- Stdlib-only Python; tests runnable as `python tests/test_generate_templates.py`.
- OKF frontmatter skeletons emit every required universal property (`type`, `title`, `description`, `tags`, `date`, `timestamp`, `resources`) plus the type's own `fields`; exactly one status tag, the registry's first open status.
- Timestamps in templates are UTC minute-precision: `<% moment.utc().format("YYYY-MM-DDTHH:mm[Z]") %>` (never `tp.date.now`, which is local).
- **Prerequisite for the live trial:** Templater 2.23.1 requires Obsidian ≥ 1.13.0; machine 2 runs 1.8.4 — Kevin upgrades Obsidian before Task 4's human steps (also unlocks the Obsidian CLI evaluated in the fleet research doc).
- Commit after every task in the worldbuilder submodule (attached `master`, not detached HEAD); pin bump in the parent at the end. Commits end with the Claude co-author line.
- This repo's `.claude/` vault is enforced — the scraibe hooks will police plan/inbox edits; that is expected.

---

### Task 1: generate_templates.py with tests

**Files:**
- Create: `scripts/generate_templates.py`
- Test: `tests/test_generate_templates.py`

**Interfaces:**
- Produces: `python scripts/generate_templates.py --config <okf.json> --out <vault_root> [--dir <path>=<type>[,<type>...]]... [--obsidian]`
  - Emits `_templates/type-<name>.md` for every type named in any `--dir` (all registry types when no `--dir` given).
  - Emits `_templates/new-<dirslug>.md` picker for each `--dir` with more than one type; a single-type dir attaches its type template directly (no picker).
  - `--obsidian` merges `templates_folder`, `trigger_on_file_creation_mode: "folder"`, and `folder_templates` into `<out>/.obsidian/plugins/templater-obsidian/data.json` (creating it if absent, preserving unrelated keys).
  - Returns exit 0 on success; exit 2 with a message naming the unknown type if a `--dir` references a type not in the registry.

- [ ] **Step 1: Write the failing tests.**

```python
"""Tests for generate_templates.py. Run: python tests/test_generate_templates.py"""
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPT = os.path.join(ROOT, 'scripts', 'generate_templates.py')

REGISTRY = {
    "universal_properties": {
        "type": {"type": "text", "required": True},
        "title": {"type": "text", "required": True},
        "description": {"type": "text", "required": True},
        "tags": {"type": "tags", "required": True},
        "date": {"type": "date", "required": True},
        "timestamp": {"type": "datetime", "required": True},
        "resources": {"type": "list", "required": True},
        "aliases": {"type": "list", "required": False},
    },
    "types": {
        "character": {"fields": {"factions": {"type": "list"}},
                      "template": "## Design Notes\n\n## Background\n"},
        "event": {"fields": {"characters": {"type": "list"},
                             "layer": {"type": "text"}},
                  "template": "## What Happens\n"},
        "plan": {"fields": {}, "template": ""},
    },
    "tags": {"status": {"mutually_exclusive": True,
                        "values": ["human-ready", "agent-ready", "complete"],
                        "open": ["human-ready", "agent-ready"],
                        "closed": ["complete"]}},
    "enforced_paths": {"notes/": {"level": "full"},
                       "project/": {"level": "full"}},
}


class GeneratorTests(unittest.TestCase):
    def setUp(self):
        self.dir = tempfile.mkdtemp()
        self.config = os.path.join(self.dir, 'okf.json')
        with open(self.config, 'w', encoding='utf-8') as f:
            json.dump(REGISTRY, f)

    def tearDown(self):
        shutil.rmtree(self.dir, ignore_errors=True)

    def run_gen(self, *args):
        return subprocess.run(
            [sys.executable, SCRIPT, '--config', self.config,
             '--out', self.dir, *args],
            capture_output=True, text=True)

    def read(self, rel):
        with open(os.path.join(self.dir, rel), encoding='utf-8') as f:
            return f.read()

    def test_type_template_skeleton(self):
        r = self.run_gen('--dir', 'notes/=character,event')
        self.assertEqual(r.returncode, 0, r.stderr)
        t = self.read('_templates/type-character.md')
        self.assertIn('type: character', t)
        self.assertIn('title: <% tp.file.title %>', t)
        self.assertIn('- human-ready', t)          # first open status
        self.assertIn('timestamp: <% moment.utc().format("YYYY-MM-DDTHH:mm[Z]") %>', t)
        self.assertIn('date: <% moment.utc().format("YYYY-MM-DD") %>', t)
        self.assertIn('factions: []', t)           # list field -> []
        self.assertIn('## Design Notes', t)        # body appended
        self.assertNotIn('aliases', t)             # optional universal skipped

    def test_text_field_and_empty_body(self):
        self.run_gen('--dir', 'notes/=event', '--dir', 'project/=plan')
        e = self.read('_templates/type-event.md')
        self.assertIn('layer: ""', e)              # text field -> ""
        p = self.read('_templates/type-plan.md')
        self.assertTrue(p.rstrip().endswith('---'))  # empty body tolerated

    def test_picker_for_mixed_dir_only(self):
        self.run_gen('--dir', 'notes/=character,event', '--dir', 'project/=plan')
        picker = self.read('_templates/new-notes.md')
        self.assertIn('"character"', picker)
        self.assertIn('"event"', picker)
        self.assertIn('tp.system.suggester', picker)
        self.assertIn('tp.file.include', picker)
        self.assertFalse(os.path.exists(
            os.path.join(self.dir, '_templates', 'new-project.md')))

    def test_obsidian_config_written_and_merged(self):
        cfgdir = os.path.join(self.dir, '.obsidian', 'plugins',
                              'templater-obsidian')
        os.makedirs(cfgdir)
        with open(os.path.join(cfgdir, 'data.json'), 'w') as f:
            json.dump({"command_timeout": 5}, f)
        self.run_gen('--dir', 'notes/=character,event',
                     '--dir', 'project/=plan', '--obsidian')
        data = json.loads(self.read('.obsidian/plugins/templater-obsidian/data.json'))
        self.assertEqual(data['command_timeout'], 5)          # merged, not clobbered
        self.assertEqual(data['templates_folder'], '_templates')
        self.assertEqual(data['trigger_on_file_creation_mode'], 'folder')
        self.assertIn({'folder': 'notes', 'template': '_templates/new-notes.md'},
                      data['folder_templates'])
        self.assertIn({'folder': 'project', 'template': '_templates/type-plan.md'},
                      data['folder_templates'])

    def test_unknown_type_fails(self):
        r = self.run_gen('--dir', 'notes/=dragon')
        self.assertEqual(r.returncode, 2)
        self.assertIn('dragon', r.stderr)

    def test_default_all_types_one_picker(self):
        r = self.run_gen()
        self.assertEqual(r.returncode, 0, r.stderr)
        picker = self.read('_templates/new-note.md')
        for t in ('character', 'event', 'plan'):
            self.assertIn(f'"{t}"', picker)


if __name__ == '__main__':
    unittest.main(verbosity=2)
```

- [ ] **Step 2: Run tests to verify they fail.**

Run: `python tests/test_generate_templates.py`
Expected: errors — `scripts/generate_templates.py` does not exist.

- [ ] **Step 3: Write the generator.**

```python
#!/usr/bin/env python
"""Generate Obsidian Templater templates from an OKF registry.

Write-side sibling of generate_rules.py: one Templater template per
registry type (frontmatter skeleton + type body) in <out>/_templates/,
a suggester type-picker per mixed-type directory, and (--obsidian) the
folder_templates wiring in the vendored Templater data.json. Generic
over any okf.json — no worldbuilder knowledge; graduates verbatim to
okf-enforcement/scripts/.
"""
import argparse
import json
import os
import sys

MOMENT_TS = '<% moment.utc().format("YYYY-MM-DDTHH:mm[Z]") %>'
MOMENT_DATE = '<% moment.utc().format("YYYY-MM-DD") %>'
UNIVERSAL_ORDER = ('type', 'title', 'description', 'tags', 'date',
                   'timestamp', 'resources')


def empty_value(ftype):
    return {'list': '[]', 'tags': '[]', 'checkbox': 'false',
            'number': ''}.get(ftype, '""')


def type_template(config, tname):
    spec = config['types'][tname]
    status = config['tags']['status']['open'][0]
    lines = ['---',
             f'type: {tname}',
             'title: <% tp.file.title %>',
             'description: ""',
             'tags:',
             f'  - {status}',
             f'date: {MOMENT_DATE}',
             f'timestamp: {MOMENT_TS}',
             'resources: []']
    for fname, fspec in (spec.get('fields') or {}).items():
        if fname in UNIVERSAL_ORDER:
            continue
        lines.append(f'{fname}: {empty_value(fspec.get("type", "text"))}')
    lines.append('---')
    body = (spec.get('template') or '').strip()
    return '\n'.join(lines) + '\n' + (('\n' + body + '\n') if body else '')


def picker_template(types):
    choices = json.dumps(types)
    return ('<%*\n'
            f'const choices = {choices};\n'
            'const type = await tp.system.suggester(choices, choices);\n'
            'const tmpl = tp.file.find_tfile("_templates/type-" + type);\n'
            'tR += await tp.file.include(tmpl);\n'
            '%>')


def dir_slug(path):
    return path.strip('/').replace('/', '-') or 'note'


def parse_dirs(pairs, config):
    """[(path, [types])] from --dir path=a,b; validates type names."""
    out = []
    for pair in pairs:
        path, _, names = pair.partition('=')
        types = [t.strip() for t in names.split(',') if t.strip()]
        for t in types:
            if t not in config['types']:
                print(f'error: unknown type {t!r} in --dir {pair!r}',
                      file=sys.stderr)
                sys.exit(2)
        out.append((path, types))
    return out


def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(content)


def update_obsidian_config(out_root, attachments):
    p = os.path.join(out_root, '.obsidian', 'plugins',
                     'templater-obsidian', 'data.json')
    data = {}
    if os.path.isfile(p):
        with open(p, encoding='utf-8') as f:
            data = json.load(f)
    data['templates_folder'] = '_templates'
    data['trigger_on_file_creation_mode'] = 'folder'
    data['folder_templates'] = [
        {'folder': folder.strip('/'), 'template': template}
        for folder, template in attachments]
    write(p, json.dumps(data, indent=2) + '\n')


def main():
    ap = argparse.ArgumentParser(description='Generate Templater templates '
                                             'from an OKF registry')
    ap.add_argument('--config', required=True)
    ap.add_argument('--out', required=True)
    ap.add_argument('--dir', action='append', default=[],
                    help='path=type[,type...] — types allowed in that dir')
    ap.add_argument('--obsidian', action='store_true',
                    help='wire folder_templates into the vendored '
                         'Templater data.json')
    args = ap.parse_args()

    with open(args.config, encoding='utf-8') as f:
        config = json.load(f)

    if args.dir:
        dirs = parse_dirs(args.dir, config)
    else:
        dirs = [(p, sorted(config['types']))
                for p in config.get('enforced_paths', {})]
        # no --dir: one shared picker over all types
        all_types = sorted(config['types'])
        dirs = [(p, all_types) for p, _ in dirs] or [('', all_types)]

    emitted = set()
    attachments = []
    for path, types in dirs:
        for t in types:
            if t not in emitted:
                write(os.path.join(args.out, '_templates', f'type-{t}.md'),
                      type_template(config, t))
                emitted.add(t)
        if len(types) == 1:
            attachments.append((path, f'_templates/type-{types[0]}.md'))
        else:
            name = (f'new-{dir_slug(path)}.md' if args.dir
                    else 'new-note.md')
            write(os.path.join(args.out, '_templates', name),
                  picker_template(types))
            attachments.append((path, f'_templates/{name}'))

    if args.obsidian:
        update_obsidian_config(args.out, attachments)
    print(f'{len(emitted)} type template(s), '
          f'{len(attachments)} folder attachment(s).')


if __name__ == '__main__':
    main()
```

Implementation note: the no-`--dir` default branch assigns `dirs` twice as written — simplify to a single expression (`[(p, all_types) for p in config.get('enforced_paths', {})] or [('', all_types)]`) while keeping the `new-note.md` shared-picker name.

- [ ] **Step 4: Run tests to verify they pass.**

Run: `python tests/test_generate_templates.py`
Expected: 6 tests, OK.

- [ ] **Step 5: Commit.**

```bash
git add scripts/generate_templates.py tests/test_generate_templates.py
git commit -m "feat: generate Templater templates from the OKF registry"
```

---

### Task 2: Vendor Templater 2.23.1 into the chrome

**Files:**
- Create: `skills/worldbuilder-setup/worldvault/.obsidian/plugins/templater-obsidian/{main.js,manifest.json,styles.css,data.json}`
- Create: `skills/worldbuilder-setup/worldvault/.obsidian/community-plugins.json`

**Interfaces:**
- Consumes: nothing from Task 1 (static assets; the generator overwrites `data.json`'s wiring at setup time).
- Produces: the chrome overlay Task 3's setup flow copies; `data.json` baseline with worldbuilder's two folder attachments.

- [ ] **Step 1: Download the pinned release assets.**

```bash
cd skills/worldbuilder-setup/worldvault/.obsidian
mkdir -p plugins/templater-obsidian
for f in main.js manifest.json styles.css; do
  curl -sL -o "plugins/templater-obsidian/$f" \
    "https://github.com/SilentVoid13/Templater/releases/download/2.23.1/$f"
done
python -c "import json;print(json.load(open('plugins/templater-obsidian/manifest.json'))['version'])"
```
Expected: `2.23.1`.

- [ ] **Step 2: Write the config baseline** `plugins/templater-obsidian/data.json`:

```json
{
  "templates_folder": "_templates",
  "trigger_on_file_creation_mode": "folder",
  "folder_templates": [
    {"folder": "notes", "template": "_templates/new-notes.md"},
    {"folder": "project", "template": "_templates/new-project.md"}
  ]
}
```

- [ ] **Step 3: Check scraibe's `community-plugins.json`** (`cat ../../../../okf-enforcement/defaults/obsidian/community-plugins.json`) and write this overlay's copy extending it — expected result:

```json
["frontmatter-modified-date", "templater-obsidian"]
```

(If scraibe's file lists anything else, keep those entries too — the overlay must be a superset.)

- [ ] **Step 4: Commit.**

```bash
git add skills/worldbuilder-setup/worldvault/.obsidian
git commit -m "feat: vendor Templater 2.23.1 into the vault chrome (pinned; needs Obsidian >= 1.13)"
```

---

### Task 3: Setup skill wires the creation layer

**Files:**
- Modify: `skills/worldbuilder-setup/SKILL.md` (Step 3 chrome copy; new template-generation step; final report text)

**Interfaces:**
- Consumes: Task 1's CLI (`--dir`, `--obsidian`), Task 2's overlay layout.
- Produces: the setup flow Task 4 executes literally.

- [ ] **Step 1: Update Step 3 ("Install the chrome").** Replace the app.json-only overlay bullet with: "Overlay this skill's `worldvault/.obsidian/` directory on top (app config, community-plugin registration, and the vendored Templater plugin)." Keep the remaining bullets.

- [ ] **Step 2: Insert a new step between Steps 4 and 5**, renumbering the old Step 5 to 6:

```markdown
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
```

- [ ] **Step 3: Update the final report text** (old Step 5, now 6): the Obsidian line becomes "Tell them the vault is ready to open in Obsidian ('Open folder as vault' on the project root; Bases and the vendored Templater need Obsidian 1.13+ with community plugins enabled for this vault)."

- [ ] **Step 4: Verify.** `grep -n "generate_templates\|1.13" skills/worldbuilder-setup/SKILL.md` → both present; step numbering is sequential 1–6.

- [ ] **Step 5: Commit.**

```bash
git commit -am "feat: setup generates creation templates and ships Templater chrome"
```

---

### Task 4: Emberwick trial

**Files:**
- Modify (scratch only, not committed): `C:\Users\cpnbe\Documents\worldbuilder-scratch`

**Interfaces:**
- Consumes: everything prior, executed as the setup skill states it.

- [ ] **Step 1: Apply to the scratch vault.** Copy the Task 2 overlay into `worldbuilder-scratch/.obsidian/` (plugins dir + community-plugins.json), then run the Task 3 Step-5 command verbatim from the scratch root. Expected: `9 type template(s), 2 folder attachment(s).` (the registry's tenth type, `reference`, is deliberately unmapped — it is scraibe:ingest's output, not a human-creation type).

- [ ] **Step 2: Agent-side verification.**

```bash
ls _templates/          # 9 type-*.md + new-notes.md + new-project.md
python -c "import json; d=json.load(open('.obsidian/plugins/templater-obsidian/data.json')); print(d['trigger_on_file_creation_mode'], len(d['folder_templates']))"
```
Expected: `folder 2`. Also confirm `type-character.md` opens with `---`, contains `factions: []` and the moment.utc timestamp line, and ends with the character body sections.

- [ ] **Step 3: Human steps (Kevin).** Upgrade Obsidian to ≥ 1.13. Open the scratch vault, enable community plugins for it, then: create a new note in `notes/` → the type-picker should prompt; choose `location`; name the note `Ashen Lantern`. Verify the frontmatter arrived filled (type, title from filename, one `human-ready` tag, UTC timestamp) and the location body sections are present.

- [ ] **Step 4: Validate the human-created note.**

```bash
python <scraibe>/scripts/validate.py notes --root . --format human
```
Expected: 0 critical (description is empty but present — if validate flags empty description as warning, record it in the sub-vault inbox as a template-vs-validator gap to resolve at graduation).

- [ ] **Step 5: Record the trial** in the sub-vault inbox (pass/fail per check, any friction) and check off this plan's boxes.

---

### Task 5: Close out and pin bump

- [ ] **Step 1:** Fleet inbox line (parent vault `.claude/inbox.md`): the creation layer is prototyped and trialed; `generate_templates.py` graduates to `okf-enforcement/scripts/` and Templater vendoring to scraibe's `defaults/obsidian/` at the merge point — okf-enforcement inbox gets the pointer.
- [ ] **Step 2:** Regenerate the sub-vault plans index; flip this plan's tag to `complete` when the trial passes (Kevin confirms).
- [ ] **Step 3:** Commit the submodule on `master`, push, pin bump in the parent on `machine-2`, push, `sync.py --check` clean.

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
        self.assertIs(data['trigger_on_file_creation'], True)   # 2.20.x boolean key
        self.assertIs(data['enable_folder_templates'], True)    # 2.20.x boolean key
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

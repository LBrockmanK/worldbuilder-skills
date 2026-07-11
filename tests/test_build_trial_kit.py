import base64
import json
import os
import re
import subprocess
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KIT = os.path.join(ROOT, "trials", "2026-07-writing-doctrine")

SENTINELS = {
    "style": {"current": "### Four Failure Modes", "stopslop": "### Vary Rhythm"},
    "doctrine": {"additive": "### Knowledge Boundaries", "tensions": "### Anchor Repetition"},
}


class TestTrialKitBuild(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.out = tempfile.mkdtemp()
        subprocess.run(
            [sys.executable, os.path.join(KIT, "build.py"), cls.out], check=True
        )
        cls.packets = {}
        for i in range(1, 7):
            with open(os.path.join(cls.out, f"packet-{i}.md"), encoding="utf-8") as f:
                cls.packets[i] = f.read()
        with open(os.path.join(cls.out, "key.md"), encoding="utf-8") as f:
            key_raw = f.read()
        payload = re.search(r"```\n(.+?)\n```", key_raw, re.S).group(1)
        cls.key = json.loads(base64.b64decode(payload))

    def test_key_is_a_permutation_of_all_six_cells(self):
        cells = {(v["style"], v["doctrine"]) for v in self.key.values()}
        self.assertEqual(len(self.key), 6)
        self.assertEqual(
            cells,
            {(s, d) for s in ("current", "stopslop")
             for d in ("current", "additive", "tensions")},
        )

    def test_no_markers_or_comments_leak(self):
        for text in self.packets.values():
            self.assertNotIn("<!--", text)

    def test_packets_share_identical_frame(self):
        with open(os.path.join(KIT, "src", "base.md"), encoding="utf-8") as f:
            base = f.read().strip()
        seg1, rest = base.split("<!-- DOCTRINE-BLOCK -->")
        seg2, seg3 = rest.split("<!-- STYLE-BLOCK -->")
        segments = [re.sub(r"\n{3,}", "\n\n", s.strip()) for s in (seg1, seg2, seg3)]
        for i, text in self.packets.items():
            pos = 0
            for n, seg in enumerate(segments, start=1):
                idx = text.find(seg, pos)
                self.assertNotEqual(idx, -1, "packet-%d missing frame segment %d" % (i, n))
                pos = idx + len(seg)

    def test_axis_content_matches_key(self):
        for name, cell in self.key.items():
            text = self.packets[int(name.split("-")[1])]
            for style, sentinel in SENTINELS["style"].items():
                if cell["style"] == style:
                    self.assertIn(sentinel, text, name)
                else:
                    self.assertNotIn(sentinel, text, name)
            self.assertEqual(
                SENTINELS["doctrine"]["additive"] in text,
                cell["doctrine"] in ("additive", "tensions"), name)
            self.assertEqual(
                SENTINELS["doctrine"]["tensions"] in text,
                cell["doctrine"] == "tensions", name)

    def test_model_neutrality(self):
        for text in self.packets.values():
            for banned in ("claude", "anthropic", "gpt", "openai", "gemini"):
                self.assertNotIn(banned, text.lower())


if __name__ == "__main__":
    unittest.main()

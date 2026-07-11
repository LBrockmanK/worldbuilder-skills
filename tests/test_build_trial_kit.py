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

    def test_committed_kit_matches_current_src(self):
        """Lock the committed packet-*.md and key.md to the current src/
        blocks. Reconstructs the six possible cell assemblies in memory
        the same way build.py does, then checks the committed kit
        against that reconstruction. Reads the committed kit directory
        directly; does not invoke build.py. Assertion messages are kept
        generic on purpose: a failure here must never print a cell name
        next to a packet number, since the human scorer may read this
        output before the blind read is done."""
        src = os.path.join(KIT, "src")

        def read_src(name):
            with open(os.path.join(src, name), encoding="utf-8") as f:
                return f.read().strip()

        styles = {"current": "style-current.md", "stopslop": "style-stopslop.md"}
        doctrines = {
            "current": [],
            "additive": ["doctrine-additive.md"],
            "tensions": ["doctrine-additive.md", "doctrine-tensions.md"],
        }
        base = read_src("base.md")

        assemblies = {}
        for style in styles:
            for doctrine in doctrines:
                doctrine_text = "\n\n".join(read_src(n) for n in doctrines[doctrine])
                packet = base.replace("<!-- STYLE-BLOCK -->", read_src(styles[style]))
                packet = packet.replace("<!-- DOCTRINE-BLOCK -->", doctrine_text)
                packet = re.sub(r"\n{3,}", "\n\n", packet)
                if not packet.endswith("\n"):
                    packet += "\n"
                assemblies[(style, doctrine)] = packet

        committed_packets = {}
        for i in range(1, 7):
            with open(os.path.join(KIT, "packet-%d.md" % i), encoding="utf-8") as f:
                committed_packets[i] = f.read()

        with open(os.path.join(KIT, "key.md"), encoding="utf-8") as f:
            key_raw = f.read()
        payload = re.search(r"```\n(.+?)\n```", key_raw, re.S).group(1)
        committed_key = json.loads(base64.b64decode(payload))

        # (a) each committed packet matches exactly one reconstructed assembly
        matched_cells = {}
        for i, text in committed_packets.items():
            matches = [cell for cell, assembly in assemblies.items() if assembly == text]
            if len(matches) != 1:
                self.fail("packet-%d does not match any current-src assembly" % i)
            matched_cells[i] = matches[0]

        # (b) the six packets cover all six cells exactly once
        if sorted(matched_cells.values()) != sorted(assemblies.keys()):
            self.fail("committed packets do not cover all six current-src cells exactly once")

        # (c) the committed key's mapping agrees with the content match
        for i, cell in matched_cells.items():
            key_entry = committed_key.get("packet-%d" % i)
            if key_entry is None:
                self.fail("committed key disagrees with packet content")
            key_cell = (key_entry["style"], key_entry["doctrine"])
            if key_cell != cell:
                self.fail("committed key disagrees with packet content")


if __name__ == "__main__":
    unittest.main()

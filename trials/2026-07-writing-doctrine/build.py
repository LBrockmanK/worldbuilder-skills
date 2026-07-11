#!/usr/bin/env python3
"""Assemble the six trial packets from src/ blocks and seal the key.

Every run reshuffles the packet-to-cell assignment. Rebuild only for a
fresh trial (never after outputs exist for the current packets).
Packets and key.md are generated; never hand-edit them.
"""
import base64
import json
import os
import random
import re
import sys

KIT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(KIT, "src")

STYLES = {"current": "style-current.md", "stopslop": "style-stopslop.md"}
DOCTRINES = {
    "current": [],
    "additive": ["doctrine-additive.md"],
    "tensions": ["doctrine-additive.md", "doctrine-tensions.md"],
}

KEY_HEADER = """# Trial key — DO NOT OPEN

Decode only after every score and the preference ranking are recorded
on the rubric sheet. The fenced block is base64; it decodes to the
packet-to-cell map.
"""


def read(name):
    with open(os.path.join(SRC, name), encoding="utf-8") as f:
        return f.read().strip()


def write(path, text):
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text if text.endswith("\n") else text + "\n")


def main():
    out_dir = sys.argv[1] if len(sys.argv) > 1 else KIT
    base = read("base.md")
    cells = [(s, d) for s in STYLES for d in DOCTRINES]
    random.shuffle(cells)
    key = {}
    for i, (style, doctrine) in enumerate(cells, start=1):
        doctrine_text = "\n\n".join(read(n) for n in DOCTRINES[doctrine])
        packet = base.replace("<!-- STYLE-BLOCK -->", read(STYLES[style]))
        packet = packet.replace("<!-- DOCTRINE-BLOCK -->", doctrine_text)
        packet = re.sub(r"\n{3,}", "\n\n", packet)
        write(os.path.join(out_dir, "packet-%d.md" % i), packet)
        key["packet-%d" % i] = {"style": style, "doctrine": doctrine}
    payload = base64.b64encode(
        json.dumps(key, indent=2).encode("utf-8")).decode("ascii")
    write(os.path.join(out_dir, "key.md"),
          KEY_HEADER + "\n```\n" + payload + "\n```")


if __name__ == "__main__":
    main()

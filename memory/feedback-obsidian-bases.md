---
name: feedback-obsidian-bases
description: Obsidian Bases must use standalone .base files in a _bases/ folder, not embedded base code fences in markdown notes
metadata:
  type: feedback
---

Obsidian Bases do not work as embedded `base` code fences in markdown notes. Use standalone `.base` files stored in a `_bases/` folder, and embed them in notes with `![[filename.base]]` syntax.

**Why:** Attempted inline base fences in Home.md produced no output — the code block just rendered as plain text. Obsidian Bases requires standalone files.

**How to apply:** In worldvault, the `_bases/` folder holds one `.base` file per note type (plus a summary base). `Home.md` embeds them with `![[basename.base]]`. The `_bases/` folder must be included in the SKILL.md copy step.

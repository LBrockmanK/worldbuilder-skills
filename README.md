# worldbuilder-skills

Claude Code skills for building a game world on the [ainime-games.com](https://ainime-games.com) world builder platform. Install these skills once; run them in Claude Code to get an AI-assisted worldbuilding pipeline from blank page to finished export.

---

## What these skills do

The skills guide you through three sequential phases:

### Seed phase (Phase 1)

The clarification-heavy opening phase. Claude asks the foundational questions — setting, tone, household structure, hidden layer — and produces `seed.md`, a platform-agnostic world proposal that every later phase builds on.

**Key output:** `seed.md`

### Wide phase (Phase 2)

The expansive generative phase. With the seed confirmed, Claude builds out the world's content: concept notes (lore), story notes (narrative direction), location notes, faction notes, cast planning, and individual character notes. All creative decisions live here. Nothing in Phase 2 is ainime-specific.

**Key outputs:** character notes, concept notes, story notes, location notes, faction notes, event notes in `notes/`

### Export phase (Phase 3)

The conversion phase. Wide-phase notes are read by the export skill and packaged into ainime-games.com format. This is the only phase that writes ainime field names.

**Key output:** ainime character cards and supporting JSON fields

---

## Skills

| Skill | When to use |
|---|---|
| `worldbuilder-setup` | Starting a brand-new project — run once |
| `worldbuilder-world-planning` | Start of every session (new or returning) |
| `worldbuilder-world-foundation` | Seed phase — builds `seed.md` |
| `worldbuilder-ingestion` | Starting from existing material (SillyTavern cards, prior exports, notes) |
| `worldbuilder-concept` | Wide phase — writes concept notes |
| `worldbuilder-story` | Wide phase — writes story notes |
| `worldbuilder-location` | Wide phase — writes location notes |
| `worldbuilder-faction` | Wide phase — writes faction notes |
| `worldbuilder-character` | Wide phase — builds individual character notes |
| `worldbuilder-ainime-export` | Export phase — converts character notes to ainime format |

---

## How to start

### New project

Run `worldbuilder-setup` once. It copies the vault template into your project directory and hands off to `worldbuilder-world-planning` to begin the Seed phase.

### Returning session

Run `worldbuilder-world-planning`. It reads your project state, tells you where you are in the pipeline, and routes to the right next skill.

> **When in doubt, start with `worldbuilder-world-planning`.** It handles both new and returning projects and will route to setup if nothing exists yet.

---

## Installing the skills

These skills are distributed as a Claude Code plugin package. Install the plugin through Claude Code's plugin manager — you do not install individual skill files manually. For step-by-step installation instructions, find this plugin's listing in the Claude Code plugin marketplace.

Once installed, invoke any skill using the `/` command prefix in Claude Code (e.g., `/worldbuilder-setup`, `/worldbuilder-world-planning`).

---

## Project vocabulary

The skills use consistent terminology throughout. Key terms:

- **Seed phase / Wide phase / Export phase** — the three pipeline phases
- **`seed.md`** — the world foundation document produced in Phase 1
- **Character note** — the comprehensive Wide-phase document for a single character
- **Concept note** — a discrete piece of world knowledge (exported as a lorebook entry)
- **Story note** — a narrative direction document (direction, arc, or intention scope)

Full terminology reference: [`CONTEXT.md`](CONTEXT.md)

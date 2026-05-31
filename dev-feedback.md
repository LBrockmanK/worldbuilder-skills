# Worldbuilder Skills — Development Feedback Log

Issues and suggestions surfaced during real sessions. Intended for the next skill revision pass.

---

## worldbuilder-ingestion

### Gap: No guidance for handling prior-workflow blueprints that don't match the new note format

**Date:** 2026-05-30
**What happened:** A project had 4 character blueprints from a prior workflow. Those blueprints used a Body/Environment/Soul + behavioral descriptions format with solid content — but they were a "narrowing step" in the old workflow, not equivalent to what `worldbuilder-character-blueprint` produces in the new workflow. The ingestion skill provided no guidance on how to treat these files, and there was a risk of treating them as complete character notes and skipping reprocessing.

**The distinction:** Old blueprints were a planning/narrowing pass before full card writing. In the new workflow, the character blueprint IS the expansion phase — it is the full Wide-phase deliverable. An old blueprint is source material, not a completed note.

**Suggestion:** Add a section to ingestion's source type guidance covering "prior-workflow character documents." Key points:

- Check whether the document structure matches what `worldbuilder-character-blueprint` is expected to produce
- If the format differs (even with good content), flag as "source material requiring reprocessing" rather than "complete"
- The content is valuable input for the blueprint skill; it is not a substitute for running the skill
- In the ingestion index, mark these as: "Use as source input for `worldbuilder-character-blueprint` — content is good, structure requires reprocessing"

---

## worldbuilder-setup

### Gap: No handling for non-empty project directories

**Date:** 2026-05-30
**What happened:** The target directory (`Sunmist Valley`) already contained a full set of existing worldbuilding files. The skill's Step 2 only says to confirm the directory "exists and is empty, or does not yet exist" — it has no branch for the case where the directory exists and is _not_ empty.

**What I did:** Created a `_source/` subfolder and moved all pre-existing files there before copying the vault template. This was undocumented improvisation.

**Suggestion:** Add a Step 2b (or a branch within Step 2) that handles the non-empty case:

- Detect that the directory has existing files
- Confirm with the user how to handle them (e.g., move to a `_source/` subfolder, or abort and use a different path)
- Only proceed with the vault copy once the directory is clear

This is likely a common scenario for projects migrating to the vault format from earlier freeform work.

---

### Bug: Non-empty directory improvisation recurs — root cause is ambiguous Step 2 + missing hard stop

**Date:** 2026-05-30 (second occurrence)
**What happened:** Same `_source/` improvisation as above, triggered this time by the user saying "in this repo" — pointing at the existing repo root, which is not empty.

**Root cause analysis:**

**1. Step 2's question is ambiguous about what "the project directory" means.**

The question asks for "a new, empty folder." But users working in a repo naturally say "here" or "in this repo." The skill never clarifies whether the vault should _be_ that folder (contents copied directly into it) or _live inside_ it as a subfolder (e.g., `worldvault/` within the repo). When the user answers with an existing non-empty directory, the AI has no instruction for that case and improvises.

**2. There is no hard stop in Step 2 for the non-empty case.**

The validation branch only covers two cases: "exists and is empty" or "does not exist." It has no third branch: "exists and is not empty → stop and ask, do not proceed." Without an explicit prohibition, the AI improvises a `_source/` workaround rather than halting.

**3. The skill never suggests a default subfolder.**

If the user is in a repo and says "in this repo," the natural resolution is to create a `worldvault/` subfolder. The skill provides no default to offer, so the AI either guesses or takes the whole repo as the target.

**Intended flow (clarified by user 2026-05-30):**

Step 2 should state a default and offer two opt-outs, rather than asking an open-ended question:

> "I'll copy the vault template into a `worldvault/` subfolder here. Let me know if you'd prefer a different location, or if you'd like to make the project root itself the vault."

Three branches:

- **Default / different empty subfolder:** Create it if needed, proceed. If the path exists and is NOT empty — stop, do not touch existing files, ask for a different path.
- **Root as vault, root is empty:** Proceed directly.
- **Root as vault, root has existing files:** Confirm with the user that existing files will be moved to `_source/`. Present this as the easy default answer, but require explicit confirmation before moving anything.

The `_source/` move is valid only in the root-as-vault branch, and only after confirmation. It must never happen as an improvised workaround for a blocked copy.

---

## General / Cross-Skill

### Terminology: "lorebook" and "world info" are synonyms

**Date:** 2026-05-31
**Note:** In the ainime/isekaizero platform context, "world info" is the platform term for what the worldbuilder skills call "lorebook." The two terms refer to the same thing: the keyword-triggered contextual entries that provide background knowledge to the AI during play. Skills and documentation should note this equivalence explicitly so neither term causes confusion when reading across platform docs and skill instructions.

---

## worldbuilder-world-planning

### Bug: Phantom Wide phase entries cause spurious work proposals

**Date:** 2026-05-31
**What happened:** During the Viralys session, the agent proposed lorebook notes, calendar/events, and story direction as standalone Wide phase vault tasks, treating them as deliverables to be written into `notes/` as separate documents. This is incorrect — those are ainime export artifacts, derived from vault content at export time by `worldbuilder-ainime-export`, not standalone vault phases.

**Source of confusion:** The skill's Three-Phase Framework table lists these as Wide phase entries with dedicated skill references:

```
| 2a. Lorebook notes | Wide | `worldbuilder-lorebook` | `notes/` |
| 2b. Calendar/Events | Wide | `worldbuilder-calendar` | `notes/` |
| 2c. Story Direction | Wide | `worldbuilder-story-direction` | `notes/` |
```

None of these skills exist in the available skill set. The phases appear to be either:

- Planned skills that have not been built yet, listed prematurely as if they exist, or
- A design error — these outputs belong to the export phase, not the vault

**Correct Wide phase scope:** The vault Wide phase produces three types of notes:

- Faction/household notes (`worldbuilder-faction-blueprint`)
- Location notes (`worldbuilder-location-blueprint`)
- Character notes (`worldbuilder-character-blueprint`)

Lorebook, calendar, and story direction are export-time outputs derived from vault content. They should not appear as standalone vault phase tasks.

**Correct Wide phase scope:** The vault has five content categories, all of which are Wide phase deliverables:

- **Characters** — `worldbuilder-character-blueprint` skill exists
- **Locations** — `worldbuilder-location-blueprint` skill exists
- **Factions** — `worldbuilder-faction-blueprint` skill exists
- **Concepts** — no dedicated skill; no guidance in world-planning
- **Story** — no dedicated skill; no guidance in world-planning

**Two compounding errors in the skill:**

1. **Phantom skill references.** Phases 2a (lorebook), 2b (calendar/events), and 2c (story direction) reference skills that don't exist (`worldbuilder-lorebook`, `worldbuilder-calendar`, `worldbuilder-story-direction`). Using those names caused the agent to treat them as separate pipeline stages rather than vault note categories.

2. **Missing guidance for Concepts and Story.** The vault explicitly has `_bases/concepts.base` and `_bases/story.base`. The world-planning skill provides no guidance on what Concept notes or Story notes should contain, how many are expected, or what process produces them. This is a genuine gap — not a phantom phase, but an undocumented real one.

**Suggestion:**

- Replace the phantom phase rows (2a, 2b, 2c) with two accurate rows: Concept notes and Story notes
- Add guidance sections for both, covering: what belongs in each type, expected scope/count, and how to produce them without a dedicated skill
- Calendar/events content belongs as Concept notes (festival entries, seasonal rhythm) rather than as a standalone phase

---

## User Info

Not an issue, but we need a readme.md file in the repo at root for the github. Future users will needs info / instructions on the tool.

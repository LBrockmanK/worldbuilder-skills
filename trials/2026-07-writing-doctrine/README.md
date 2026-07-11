# Trial Runner

Instructions for the agent orchestrating this trial. Follow them in order.

## 1. What this is

This is a blind writing trial: six sealed instruction packets, one
character, six independent agents, each writing one character note;
the human scores the results blind.

## 2. Setup

Copy this folder into the project. A scratch location is fine. Run
`brief-procedure.md` to produce `brief.md`. Create an empty `out/`
directory.

## 3. Dispatch

For each packet, 1 through 6, dispatch one fresh agent with exactly:

- Its packet file (`packet-<N>.md`).
- `brief.md`.
- Read access to the project vault.
- The instruction to write its note to `out/note-<N>.md`.

Agents run independently. No shared context between them. No agent
sees another packet or another agent's output. No agent asks the user
questions. No agent uses any installed worldbuilding skill.

## 4. Collect and hand off

Confirm all six output files exist in `out/`. Give the human
`rubric.md` and the `out/` folder. Do not open `key.md` yourself. The
human decodes it only after the rubric is fully scored.

## 5. Regeneration note

`build.py` in the source repo generates the packets and `key.md`.
Never hand-edit either. A rebuild reshuffles the key, so never rebuild
once outputs exist for the current packets. Rerunning the trial on
another character after the key has been decoded is unblinded;
rebuild the kit (fresh shuffle) in the source repo before any rerun
once the key has been seen.

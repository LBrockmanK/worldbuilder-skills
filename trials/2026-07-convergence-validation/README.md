# Convergence Validation Trial

## What this tests

Whether independent generation agents, given identical skill
instructions and character inputs, converge on the same structural and
tonal decisions — or diverge in ways that reveal under-specified areas
of the skill framework.

Two characters (Nadja, Kallya) are generated multiple times each.
Outputs are compared for structural consistency, doctrine compliance,
and content convergence. Divergence points become candidates for skill
tightening.

Standing rules for trials — blind protocol, probe classes, rubric
construction — live in `../METHODOLOGY.md` where it exists.

## Directory layout

```
inputs/          Extracted character inputs + instruction packet
out/             Generated character notes (one per run)
detection/       Automated detection results
corrections/     Human correction markup
reports/         Per-run and summary reports
```

## Setup

1. Install dependencies (stdlib only; no third-party packages).
2. Run extraction against the Viralys worldvault:

```bash
cd trials/2026-07-convergence-validation
python extract_inputs.py "<path-to-viralys-worldvault>"
```

3. Build the instruction packet from current skill files:

```bash
python build_packet.py
```

4. Verify `inputs/` contains five files: `nadja-inputs.md`,
   `kallya-inputs.md`, `world-context.md`, `roster.md`, `packet.md`.

## Generation

Dispatch independent agents with:
- `inputs/packet.md` (skill instructions + writing doctrine)
- The relevant `inputs/{character}-inputs.md`
- `inputs/world-context.md` and `inputs/roster.md`
- Instruction to write output to `out/`

Agents run independently. No shared context between them. No agent
sees another agent's output.

## Analysis

Detection scripts (Task 3) scan outputs for doctrine violations and
structural gaps. Reports land in `reports/`.

## Regeneration

`extract_inputs.py` and `build_packet.py` regenerate from source.
Never hand-edit files in `inputs/`. Re-extract if the source
characters or skill files change.

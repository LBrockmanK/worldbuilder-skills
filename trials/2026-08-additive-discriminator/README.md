# Additive-Doctrine Discriminator Trial

Measures whether the additive doctrine measurably changes model
behavior using two graduated detection components: input-echo
detection and within-model divergence.

## Trial design

- **Arms:** current (baseline), additive (doctrine overlay), stopslop
  (style overlay as reference delta)
- **Characters:** Nadja, Kallya
- **Models:** claude-sonnet-5, claude-opus-4-6
- **Runs:** 3 per cell
- **Total generations:** 36

## Usage

Full run (generate + detect):

    python run_trial.py

Detection only (rerun on existing outputs):

    python run_trial.py --detect-only

Dry run (print prompts, no API calls):

    python run_trial.py --dry-run

## Requirements

    pip install anthropic

Set `ANTHROPIC_API_KEY` in environment.

## Outputs

- `out/` — 36 generated character notes
- `report.json` — structured metrics
- `summary.md` — human-readable comparison report

## Spec

See `.claude/specs/2026-08-09-additive-doctrine-discriminator-trial.md`.

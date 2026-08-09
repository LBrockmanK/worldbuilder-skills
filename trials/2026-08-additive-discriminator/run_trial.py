"""Additive-doctrine discriminator trial runner.

Two phases:
1. Generation: Claude API calls to produce character notes.
2. Detection: input-echo and within-model divergence metrics.

Usage:
    python run_trial.py                  # full run (generate + detect)
    python run_trial.py --detect-only    # rerun detection on existing outputs
    python run_trial.py --dry-run        # print prompts, no API calls
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys

TRIAL_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(TRIAL_DIR, "..", ".."))
OUT_DIR = os.path.join(TRIAL_DIR, "out")

sys.path.insert(0, PROJECT_ROOT)
from scripts.detect_input_echo import categorize, ngram_overlap

# --- Constants ---

CHARACTERS = ["nadja", "kallya"]
ARMS = ["current", "additive", "stopslop"]
MODELS = ["claude-sonnet-5", "claude-opus-4-6"]
RUNS_PER_CELL = 3
TEMPERATURE = 1.0
MAX_TOKENS = 4096

# --- Source paths ---

SRC_DIR = os.path.join(PROJECT_ROOT, "trials", "2026-07-writing-doctrine", "src")
RETEST_DIR = os.path.join(PROJECT_ROOT, "trials", "2026-07-convergence-retest")

DESIGN_NOTES = {
    "nadja": os.path.join(RETEST_DIR, "nadja-cleaned.md"),
    "kallya": os.path.join(RETEST_DIR, "kallya-cleaned.md"),
}
BASE_PATH = os.path.join(SRC_DIR, "base.md")
OVERLAY_PATHS = {
    "current": None,
    "additive": os.path.join(SRC_DIR, "doctrine-additive.md"),
    "stopslop": os.path.join(SRC_DIR, "style-stopslop.md"),
}

# --- Trial matrix ---

MATRIX = [
    {"character": char, "doctrine": arm, "model": model}
    for char in CHARACTERS
    for arm in ARMS
    for model in MODELS
]


def _read(path: str) -> str:
    with open(path, encoding="utf-8") as f:
        return f.read()


def assemble_prompt(character: str, doctrine: str) -> str:
    """Assemble the full prompt for one generation.

    Structure: base instructions + doctrine/style overlay + design notes.
    """
    parts = [_read(BASE_PATH)]

    overlay_path = OVERLAY_PATHS[doctrine]
    if overlay_path is not None:
        parts.append(_read(overlay_path))

    parts.append("# Design Notes\n\n" + _read(DESIGN_NOTES[character]))

    return "\n\n".join(parts)


def output_path(character: str, doctrine: str, model: str, run: int) -> str:
    """Return the output file path for one generation."""
    model_short = model.replace("claude-", "")
    return os.path.join(OUT_DIR, f"{character}-{doctrine}-{model_short}-run{run}.md")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Additive-doctrine discriminator trial")
    parser.add_argument("--detect-only", action="store_true",
                        help="Skip generation, run detection on existing outputs")
    parser.add_argument("--dry-run", action="store_true",
                        help="Print prompts and exit, no API calls")
    parser.add_argument("--out-dir", default=OUT_DIR,
                        help="Output directory for generated notes")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    if args.dry_run:
        for cell in MATRIX:
            prompt = assemble_prompt(cell["character"], cell["doctrine"])
            print(f"--- {cell['character']}/{cell['doctrine']}/{cell['model']} ---")
            print(f"Prompt length: {len(prompt)} chars")
            print(prompt[:200] + "...\n")

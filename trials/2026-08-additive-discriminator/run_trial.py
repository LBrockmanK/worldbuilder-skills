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

try:
    import anthropic
except ImportError:
    anthropic = None

TRIAL_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(TRIAL_DIR, "..", ".."))
OUT_DIR = os.path.join(TRIAL_DIR, "out")

sys.path.insert(0, PROJECT_ROOT)
from scripts.detect_input_echo import categorize, ngram_overlap

SYSTEM_PROMPT = (
    "You are a character designer for an LLM-powered game. "
    "Write a complete character note following the instructions provided. "
    "Output only the character note in markdown, no commentary."
)

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


def generate_one(
    client,
    model: str,
    prompt: str,
    max_tokens: int = MAX_TOKENS,
    temperature: float = TEMPERATURE,
) -> str:
    """Generate one character note via the Claude API."""
    response = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        temperature=temperature,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.content[0].text


def generate_all(
    matrix: list[dict],
    runs: int,
    out_dir: str,
    dry_run: bool = False,
) -> dict[str, str]:
    """Run all generations and save outputs.

    Returns {output_file_path: generated_content}.
    """
    if anthropic is None:
        raise ImportError("pip install anthropic")

    os.makedirs(out_dir, exist_ok=True)
    client = anthropic.Anthropic()
    results = {}
    total = len(matrix) * runs
    done = 0

    for cell in matrix:
        prompt = assemble_prompt(cell["character"], cell["doctrine"])
        for run in range(1, runs + 1):
            done += 1
            path = output_path(cell["character"], cell["doctrine"],
                               cell["model"], run)
            # Use out_dir override if provided
            if out_dir != OUT_DIR:
                fname = os.path.basename(path)
                path = os.path.join(out_dir, fname)

            if dry_run:
                content = f"# Dry Run\n\n{cell}"
            else:
                print(f"[{done}/{total}] {cell['character']}/{cell['doctrine']}"
                      f"/{cell['model']} run {run}...")
                content = generate_one(client, cell["model"], prompt)

            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
            results[path] = content

    return results


if __name__ == "__main__":
    args = parse_args()
    out_dir = args.out_dir or OUT_DIR

    if args.dry_run:
        for cell in MATRIX:
            prompt = assemble_prompt(cell["character"], cell["doctrine"])
            print(f"--- {cell['character']}/{cell['doctrine']}/{cell['model']} ---")
            print(f"Prompt length: {len(prompt)} chars")
            print(prompt[:200] + "...\n")
        sys.exit(0)

    if not args.detect_only:
        print(f"Generating {len(MATRIX) * RUNS_PER_CELL} notes...")
        generate_all(MATRIX, RUNS_PER_CELL, out_dir)
        print("Generation complete.\n")

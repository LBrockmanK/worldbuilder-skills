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


def extract_entries(note_text: str) -> list[str]:
    """Split a character note into entries by ## headings.

    Excludes frontmatter, H1 title, and subheadings (### and below).
    Returns body text of each ## section. Empty sections are dropped.
    """
    # Strip frontmatter
    text = note_text
    if text.startswith("---"):
        end = text.find("---", 3)
        if end != -1:
            text = text[end + 3:].strip()

    # Split on ## headings
    sections = re.split(r"^## .+$", text, flags=re.MULTILINE)

    entries = []
    for section in sections[1:]:  # skip everything before first ##
        # Strip subheadings
        body = re.sub(r"^###+ .+$", "", section, flags=re.MULTILINE)
        body = body.strip()
        if body:
            entries.append(body)

    return entries


def _cell_key(character: str, doctrine: str, model: str) -> str:
    model_short = model.replace("claude-", "")
    return f"{character}/{doctrine}/{model_short}"


def run_detection(out_dir: str) -> dict:
    """Run input-echo and within-model divergence over all outputs.

    Returns structured report with per-cell metrics and summary.
    """
    cells = {}

    # Validate: all 36 output files must exist
    expected = len(CHARACTERS) * len(ARMS) * len(MODELS) * RUNS_PER_CELL
    found = 0
    for char in CHARACTERS:
        for arm in ARMS:
            for model in MODELS:
                model_short = model.replace("claude-", "")
                for run in range(1, RUNS_PER_CELL + 1):
                    fname = f"{char}-{arm}-{model_short}-run{run}.md"
                    if os.path.exists(os.path.join(out_dir, fname)):
                        found += 1
    if found < expected:
        raise FileNotFoundError(
            f"Expected {expected} output files, found {found}. "
            f"Run generation first or check --out-dir."
        )

    for char in CHARACTERS:
        input_notes = _read(DESIGN_NOTES[char])

        for arm in ARMS:
            for model in MODELS:
                model_short = model.replace("claude-", "")
                key = _cell_key(char, arm, model)

                # Collect runs
                run_texts = []
                run_entry_overlaps = []

                for run in range(1, RUNS_PER_CELL + 1):
                    fname = f"{char}-{arm}-{model_short}-run{run}.md"
                    fpath = os.path.join(out_dir, fname)

                    text = _read(fpath)
                    run_texts.append(text)

                    # Input-echo per entry
                    entries = extract_entries(text)
                    if not entries:
                        raise ValueError(
                            f"No entries extracted from {fpath}. "
                            f"Check note format (needs ## headings)."
                        )
                    overlaps = []
                    for entry in entries:
                        result = categorize(entry, input_notes)
                        overlaps.append(result["overlap"])

                    run_mean = sum(overlaps) / len(overlaps) if overlaps else 0.0
                    run_entry_overlaps.append({
                        "run": run,
                        "mean_overlap": run_mean,
                        "echo_count": sum(
                            1 for o in overlaps if o >= 0.35
                        ),
                        "total_entries": len(entries),
                    })

                # Cell-level echo aggregation
                run_means = [r["mean_overlap"] for r in run_entry_overlaps]
                cell_echo_mean = (
                    sum(run_means) / len(run_means) if run_means else 0.0
                )
                total_entries = sum(r["total_entries"] for r in run_entry_overlaps)
                total_echo = sum(r["echo_count"] for r in run_entry_overlaps)
                cell_echo_rate = (
                    total_echo / total_entries if total_entries > 0 else 0.0
                )

                # Within-model divergence: pairwise on full note text
                pairwise_overlaps = []
                for i in range(len(run_texts)):
                    for j in range(i + 1, len(run_texts)):
                        pairwise_overlaps.append(
                            ngram_overlap(run_texts[i], run_texts[j])
                        )
                divergence_mean = (
                    sum(pairwise_overlaps) / len(pairwise_overlaps)
                    if pairwise_overlaps else 0.0
                )

                cells[key] = {
                    "character": char,
                    "doctrine": arm,
                    "model": model_short,
                    "echo_mean": cell_echo_mean,
                    "echo_rate": cell_echo_rate,
                    "pairwise_overlap_mean": divergence_mean,
                    "runs": run_entry_overlaps,
                    "pairwise_overlaps": [
                        round(o, 4) for o in pairwise_overlaps
                    ],
                }

    # Summary: cross-arm deltas
    summary = _compute_summary(cells)

    return {"cells": cells, "summary": summary}


def _compute_summary(cells: dict) -> dict:
    """Compute cross-arm deltas and per-dimension breakdowns."""

    def arm_means(arm: str, metric: str) -> list[float]:
        return [
            v[metric] for v in cells.values() if v["doctrine"] == arm
        ]

    def mean(values: list[float]) -> float:
        return sum(values) / len(values) if values else 0.0

    current_echo = mean(arm_means("current", "echo_mean"))
    additive_echo = mean(arm_means("additive", "echo_mean"))
    stopslop_echo = mean(arm_means("stopslop", "echo_mean"))

    current_div = mean(arm_means("current", "pairwise_overlap_mean"))
    additive_div = mean(arm_means("additive", "pairwise_overlap_mean"))
    stopslop_div = mean(arm_means("stopslop", "pairwise_overlap_mean"))

    # Per character x model consistency check
    add_echo_wins = 0
    add_div_wins = 0
    combos = 0
    for char in CHARACTERS:
        for model in MODELS:
            model_short = model.replace("claude-", "")
            ck = _cell_key(char, "current", model)
            ak = _cell_key(char, "additive", model)
            if ck in cells and ak in cells:
                combos += 1
                if cells[ak]["echo_mean"] < cells[ck]["echo_mean"]:
                    add_echo_wins += 1
                if cells[ak]["pairwise_overlap_mean"] < cells[ck]["pairwise_overlap_mean"]:
                    add_div_wins += 1

    # Per-model breakdown
    per_model = {}
    for model in MODELS:
        model_short = model.replace("claude-", "")
        per_model[model_short] = {}
        for arm in ARMS:
            vals_echo = [v["echo_mean"] for v in cells.values()
                         if v["doctrine"] == arm and v["model"] == model_short]
            vals_div = [v["pairwise_overlap_mean"] for v in cells.values()
                        if v["doctrine"] == arm and v["model"] == model_short]
            per_model[model_short][arm] = {
                "echo": mean(vals_echo),
                "pairwise_overlap": mean(vals_div),
            }

    # Per-character breakdown
    per_character = {}
    for char in CHARACTERS:
        per_character[char] = {}
        for arm in ARMS:
            vals_echo = [v["echo_mean"] for v in cells.values()
                         if v["doctrine"] == arm and v["character"] == char]
            vals_div = [v["pairwise_overlap_mean"] for v in cells.values()
                        if v["doctrine"] == arm and v["character"] == char]
            per_character[char][arm] = {
                "echo": mean(vals_echo),
                "pairwise_overlap": mean(vals_div),
            }

    return {
        "additive_vs_current": {
            "echo_delta": additive_echo - current_echo,
            "divergence_delta": additive_div - current_div,
            "echo_consistent_wins": f"{add_echo_wins}/{combos}",
            "pairwise_overlap_consistent_wins": f"{add_div_wins}/{combos}",
        },
        "stopslop_vs_current": {
            "echo_delta": stopslop_echo - current_echo,
            "divergence_delta": stopslop_div - current_div,
        },
        "arm_means": {
            "current": {"echo": current_echo, "pairwise_overlap": current_div},
            "additive": {"echo": additive_echo, "pairwise_overlap": additive_div},
            "stopslop": {"echo": stopslop_echo, "pairwise_overlap": stopslop_div},
        },
        "per_model": per_model,
        "per_character": per_character,
    }


def write_summary(report: dict, path: str) -> None:
    """Write the human-readable summary report."""
    s = report["summary"]
    lines = [
        "# Additive-Doctrine Discriminator Trial — Results\n",
        "## Arm means\n",
        "| Arm | Echo mean | Pairwise overlap mean |",
        "|---|---|---|",
    ]
    for arm in ["current", "additive", "stopslop"]:
        m = s["arm_means"][arm]
        lines.append(f"| {arm} | {m['echo']:.4f} | {m['pairwise_overlap']:.4f} |")

    avsc = s["additive_vs_current"]
    svsc = s["stopslop_vs_current"]
    lines += [
        "",
        "## Cross-arm deltas (vs current)\n",
        "| Comparison | Echo delta | Divergence delta |",
        "|---|---|---|",
        f"| additive | {avsc['echo_delta']:+.4f} | {avsc['divergence_delta']:+.4f} |",
        f"| stopslop | {svsc['echo_delta']:+.4f} | {svsc['divergence_delta']:+.4f} |",
        "",
        "## Consistency (additive vs current)\n",
        f"- Echo: additive lower in {avsc['echo_consistent_wins']} "
        f"character×model combinations",
        f"- Pairwise overlap: additive lower in {avsc['pairwise_overlap_consistent_wins']} "
        f"character×model combinations",
    ]

    lines += [
        "",
        "## Per-model breakdown\n",
    ]
    for model_short, arms in s["per_model"].items():
        lines.append(f"### {model_short}\n")
        lines.append("| Arm | Echo mean | Pairwise overlap mean |")
        lines.append("|---|---|---|")
        for arm in ["current", "additive", "stopslop"]:
            m = arms[arm]
            lines.append(f"| {arm} | {m['echo']:.4f} | {m['pairwise_overlap']:.4f} |")
        lines.append("")

    lines += [
        "## Per-character breakdown\n",
    ]
    for char, arms in s["per_character"].items():
        lines.append(f"### {char}\n")
        lines.append("| Arm | Echo mean | Pairwise overlap mean |")
        lines.append("|---|---|---|")
        for arm in ["current", "additive", "stopslop"]:
            m = arms[arm]
            lines.append(f"| {arm} | {m['echo']:.4f} | {m['pairwise_overlap']:.4f} |")
        lines.append("")

    lines += [
        "## Per-cell detail\n",
        "| Cell | Echo mean | Echo rate | Pairwise overlap mean |",
        "|---|---|---|---|",
    ]
    for key in sorted(report["cells"].keys()):
        c = report["cells"][key]
        lines.append(
            f"| {key} | {c['echo_mean']:.4f} | {c['echo_rate']:.4f} "
            f"| {c['pairwise_overlap_mean']:.4f} |"
        )

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


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

    print("Running detection...")
    report = run_detection(out_dir)

    report_path = os.path.join(TRIAL_DIR, "report.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)
    print(f"Report saved to {report_path}")

    summary_path = os.path.join(TRIAL_DIR, "summary.md")
    write_summary(report, summary_path)
    print(f"Summary saved to {summary_path}")

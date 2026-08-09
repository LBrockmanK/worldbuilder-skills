"""Run input-echo and cross-model convergence detection on retest outputs."""

import json
import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
from scripts.detect_input_echo import categorize, compare_cross_model, ngram_overlap

RETEST_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(RETEST_DIR, "out")
INPUT_DIR = os.path.join(
    os.path.dirname(RETEST_DIR), "2026-07-convergence-validation", "inputs"
)

CHARACTERS = ["kallya", "nadja"]
MODELS = ["sonnet", "sol", "terra"]


def extract_entries(filepath: str) -> tuple[list[str], list[list[str]]]:
    """Extract synthesized entries from PART 1 and variant groups from PART 2.

    Returns (synthesized_entries, variant_groups) where variant_groups
    is a list of [varA, varB, varC] per entry.
    """
    with open(filepath, encoding="utf-8") as f:
        content = f.read()

    # Split on PART markers
    part1 = ""
    part2 = ""
    if "PART 1" in content and "PART 2" in content:
        parts = re.split(r"#+\s*PART\s*2", content, maxsplit=1)
        part1_match = re.split(r"#+\s*PART\s*1", parts[0], maxsplit=1)
        if len(part1_match) > 1:
            part1 = part1_match[1]
        part2 = parts[1] if len(parts) > 1 else ""
    elif "Part 1" in content and "Part 2" in content:
        parts = re.split(r"#+\s*Part\s*2", content, maxsplit=1)
        part1_match = re.split(r"#+\s*Part\s*1", parts[0], maxsplit=1)
        if len(part1_match) > 1:
            part1 = part1_match[1]
        part2 = parts[1] if len(parts) > 1 else ""
    else:
        part1 = content
        part2 = ""

    # Extract entries from PART 1: bullet lines or paragraphs
    entries = []
    for line in part1.split("\n"):
        line = line.strip()
        if not line:
            continue
        if line.startswith("#"):
            continue
        if line.startswith("*") and line.endswith("*"):
            continue
        if line.startswith("---"):
            continue
        # Strip leading bullet
        if line.startswith("- "):
            line = line[2:]
        elif line.startswith("* "):
            line = line[2:]
        if len(line) > 30:
            entries.append(line)

    # Extract variant groups from PART 2
    variant_groups = []
    current_group = []
    for line in part2.split("\n"):
        line = line.strip()
        if not line or line.startswith("#") or line.startswith("---"):
            if len(current_group) >= 2:
                variant_groups.append(current_group)
                current_group = []
            continue
        # Look for variant labels
        var_match = re.match(
            r"(?:\*\*)?Variant\s+[A-E].*?(?:\*\*)?[:\s]+(.*)", line, re.IGNORECASE
        )
        if var_match:
            text = var_match.group(1).strip()
            if text:
                current_group.append(text)
            continue
        # Also try "**A.**" or "A:" patterns
        var_match2 = re.match(r"(?:\*\*)?[A-E][.):]\s*(?:\*\*)?\s*(.*)", line)
        if var_match2:
            text = var_match2.group(1).strip()
            if text:
                current_group.append(text)
            continue
        # Continuation of previous variant
        if current_group and len(line) > 20:
            current_group[-1] += " " + line

    if len(current_group) >= 2:
        variant_groups.append(current_group)

    return entries, variant_groups


def load_input_notes(character: str) -> str:
    path = os.path.join(INPUT_DIR, f"{character}-inputs.md")
    with open(path, encoding="utf-8") as f:
        return f.read()


def within_model_convergence(variant_groups: list[list[str]]) -> list[dict]:
    """Measure divergence within each variant group."""
    results = []
    for i, group in enumerate(variant_groups):
        if len(group) < 2:
            continue
        pairs = []
        for a in range(len(group)):
            for b in range(a + 1, len(group)):
                overlap = ngram_overlap(group[a], group[b])
                pairs.append(overlap)
        avg_overlap = sum(pairs) / len(pairs) if pairs else 0
        results.append({
            "entry_index": i,
            "num_variants": len(group),
            "avg_pairwise_overlap": round(avg_overlap, 3),
            "max_pairwise_overlap": round(max(pairs), 3) if pairs else 0,
            "low_divergence": avg_overlap > 0.25,
        })
    return results


def main():
    report = {}

    for char in CHARACTERS:
        input_notes = load_input_notes(char)
        char_report = {"models": {}, "cross_model": {}, "within_model": {}}

        entries_by_model = {}

        for model in MODELS:
            filepath = os.path.join(OUT_DIR, f"{char}-{model}.md")
            if not os.path.exists(filepath):
                print(f"SKIP: {filepath} not found")
                continue

            entries, variants = extract_entries(filepath)
            entries_by_model[model] = entries

            # Per-entry input-echo check
            echo_count = 0
            clean_count = 0
            for entry in entries:
                result = categorize(entry, input_notes)
                if result["category"] == "input_echo":
                    echo_count += 1
                else:
                    clean_count += 1

            # Within-model convergence
            wm_results = within_model_convergence(variants)
            low_div_count = sum(1 for r in wm_results if r["low_divergence"])

            char_report["models"][model] = {
                "total_entries": len(entries),
                "input_echo": echo_count,
                "clean": clean_count,
                "variant_groups_parsed": len(variants),
                "low_divergence_groups": low_div_count,
            }
            char_report["within_model"][model] = wm_results

        # Cross-model convergence
        if len(entries_by_model) >= 2:
            findings = compare_cross_model(entries_by_model, input_notes)
            categories = {}
            for f in findings:
                cat = f["category"]
                categories[cat] = categories.get(cat, 0) + 1

            # Cross-provider vs within-family
            cross_provider_findings = [
                f for f in findings
                if f["category"] == "cross_model_convergence"
                and (
                    (f["model"] == "sonnet" and f["match_model"] in ("sol", "terra"))
                    or (f["model"] in ("sol", "terra") and f["match_model"] == "sonnet")
                )
            ]
            within_family_findings = [
                f for f in findings
                if f["category"] == "cross_model_convergence"
                and f["model"] in ("sol", "terra")
                and f["match_model"] in ("sol", "terra")
            ]

            total_cross = sum(
                len(entries_by_model[m]) for m in entries_by_model
            )

            char_report["cross_model"] = {
                "category_counts": categories,
                "total_entries_compared": total_cross,
                "cross_provider_convergence_count": len(cross_provider_findings),
                "within_family_convergence_count": len(within_family_findings),
            }

            # Save detailed findings
            char_report["cross_model_findings"] = [
                {k: v for k, v in f.items() if k != "entry" or len(v) < 100}
                for f in findings
                if f["category"] == "cross_model_convergence"
            ]

        report[char] = char_report

    # Print summary
    print("=" * 60)
    print("CONVERGENCE RETEST DETECTION REPORT")
    print("=" * 60)

    for char in CHARACTERS:
        cr = report[char]
        print(f"\n--- {char.upper()} ---")
        for model, stats in cr["models"].items():
            print(
                f"  {model}: {stats['total_entries']} entries, "
                f"{stats['input_echo']} echo, {stats['clean']} clean, "
                f"{stats['variant_groups_parsed']} variant groups, "
                f"{stats['low_divergence_groups']} low-divergence"
            )

        cm = cr.get("cross_model", {})
        if cm:
            print(f"  Cross-model categories: {cm.get('category_counts', {})}")
            print(
                f"  Cross-provider convergence: {cm.get('cross_provider_convergence_count', 0)}"
            )
            print(
                f"  Within-family convergence: {cm.get('within_family_convergence_count', 0)}"
            )
            total = cm.get("total_entries_compared", 1)
            cross_prov = cm.get("cross_provider_convergence_count", 0)
            within_fam = cm.get("within_family_convergence_count", 0)
            if total > 0:
                print(
                    f"  Cross-provider rate: {cross_prov / total * 100:.1f}%"
                )
                print(
                    f"  Within-family rate: {within_fam / total * 100:.1f}%"
                )

    # Save full report
    report_path = os.path.join(RETEST_DIR, "detection-report.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, default=str)
    print(f"\nFull report saved to {report_path}")


if __name__ == "__main__":
    main()

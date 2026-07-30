"""Compile detection results into human-review reports.

Adapted from the brief's template: works with the actual trial data
(two LLM judges, no exact-match or embedding results).

Usage: python compile_report.py
"""
import json
from pathlib import Path
from collections import defaultdict

BASE = Path(__file__).parent


def load_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def pair_key(finding):
    """Canonical key for matching findings across judges."""
    return (finding["pair"], finding["pair_type"])


def sentences_overlap(a, b, threshold=0.6):
    """Check if two sentence pairs are about the same convergence."""
    words_a = set(a.lower().split())
    words_b = set(b.lower().split())
    if not words_a or not words_b:
        return False
    overlap = len(words_a & words_b) / min(len(words_a), len(words_b))
    return overlap >= threshold


def find_agreements(opus5_findings, sol_findings):
    """Find findings flagged by both judges (same pair, similar sentences)."""
    agreements = []  # list of (opus5_idx, sol_idx) pairs
    sol_used = set()
    for oi, of in enumerate(opus5_findings):
        for si, sf in enumerate(sol_findings):
            if si in sol_used:
                continue
            if pair_key(of) != pair_key(sf):
                continue
            if sentences_overlap(of["sentence_a"], sf["sentence_a"]) or \
               sentences_overlap(of["sentence_b"], sf["sentence_b"]):
                agreements.append((oi, si))
                sol_used.add(si)
                break
    return agreements


def compile_detection_report():
    opus5 = load_json(BASE / "detection/judge-opus5.json")
    sol = load_json(BASE / "detection/judge-sol.json")

    opus5_findings = opus5["findings"]
    sol_findings = sol["findings"]
    agreements = find_agreements(opus5_findings, sol_findings)
    opus5_agreed = {a[0] for a in agreements}
    sol_agreed = {a[1] for a in agreements}

    # --- Summary stats ---
    def count_by(findings, key, value):
        return sum(1 for f in findings if f[key] == value)

    def type_counts(findings):
        wc = sum(1 for f in findings if f["pair_type"] == "within-claude")
        wg = sum(1 for f in findings if f["pair_type"] == "within-gpt")
        cp = sum(1 for f in findings if f["pair_type"] == "cross-provider")
        return wc, wg, cp

    o_wc, o_wg, o_cp = type_counts(opus5_findings)
    s_wc, s_wg, s_cp = type_counts(sol_findings)

    lines = ["# Detection Report", ""]
    lines.append("## Method summary")
    lines.append("")
    lines.append("- **Method 1 (exact match):** 0 findings after stripping "
                 "verbatim Design Notes (all matches were reproduced source "
                 "material, correctly excluded)")
    lines.append("- **Method 2 (embedding similarity):** skipped (no API key)")
    lines.append("- **Method 3 (LLM-as-judge):** two judges ran — "
                 "Opus 5 and GPT-5.6 Sol")
    lines.append("")

    lines.append("## Judge comparison")
    lines.append("")
    lines.append("| Metric | Opus 5 | GPT Sol |")
    lines.append("|--------|--------|---------|")
    lines.append(f"| Total findings | {len(opus5_findings)} | "
                 f"{len(sol_findings)} |")
    lines.append(f"| CONVERGENT | "
                 f"{count_by(opus5_findings, 'verdict', 'CONVERGENT')} | "
                 f"{count_by(sol_findings, 'verdict', 'CONVERGENT')} |")
    lines.append(f"| NEAR-CONVERGENT | "
                 f"{count_by(opus5_findings, 'verdict', 'NEAR-CONVERGENT')} | "
                 f"{count_by(sol_findings, 'verdict', 'NEAR-CONVERGENT')} |")
    lines.append(f"| Within-Claude | {o_wc} | {s_wc} |")
    lines.append(f"| Within-GPT | {o_wg} | {s_wg} |")
    lines.append(f"| Cross-provider | {o_cp} | {s_cp} |")
    lines.append(f"| Agreed (both flagged) | {len(agreements)} | "
                 f"{len(agreements)} |")
    lines.append("")
    lines.append("**Systematic bias note:** Opus 5 flagged more within-Claude "
                 "pairs ({} of {} findings). Sol flagged more cross-provider "
                 "pairs ({} of {} findings).".format(
                     o_wc, len(opus5_findings),
                     s_cp, len(sol_findings)))
    lines.append("")

    # --- Group by character, then pair ---
    # Collect all findings with judge attribution
    all_tagged = []
    for i, f in enumerate(opus5_findings):
        char = f["pair"].split()[0]
        all_tagged.append({
            **f,
            "character": char,
            "judge": "Opus 5",
            "agreed": i in opus5_agreed,
        })
    for i, f in enumerate(sol_findings):
        char = f["pair"].split()[0]
        all_tagged.append({
            **f,
            "character": char,
            "judge": "GPT Sol",
            "agreed": i in sol_agreed,
        })

    by_char = defaultdict(lambda: defaultdict(list))
    for t in all_tagged:
        by_char[t["character"]][t["pair"]].append(t)

    lines.append("---")
    lines.append("")
    lines.append("## Findings by character and pair")
    lines.append("")

    flag_num = 0
    for char in sorted(by_char):
        lines.append(f"### {char.capitalize()}")
        lines.append("")
        for pair in sorted(by_char[char]):
            findings = by_char[char][pair]
            pair_type = findings[0]["pair_type"]
            lines.append(f"#### {pair} ({pair_type})")
            lines.append("")
            for f in findings:
                flag_num += 1
                agreed_mark = " **[BOTH JUDGES]**" if f["agreed"] else ""
                lines.append(f"**#{flag_num}** [{f['judge']}] "
                             f"{f['verdict']}{agreed_mark}")
                lines.append("")
                lines.append(f"> **A:** {f['sentence_a']}")
                lines.append(f">")
                lines.append(f"> **B:** {f['sentence_b']}")
                lines.append("")
                lines.append(f"*Reasoning:* {f['reasoning']}")
                lines.append("")
                lines.append("- [ ] True positive")
                lines.append("- [ ] False positive")
                lines.append("")

    return "\n".join(lines)


def compile_correction_report():
    opus5 = load_json(BASE / "detection/judge-opus5.json")
    sol = load_json(BASE / "detection/judge-sol.json")

    lines = ["# Correction Report", ""]
    lines.append("Each entry shows a CONVERGENT finding from either judge. ")
    lines.append("The correction placeholder will be filled after human ")
    lines.append("review of the detection report.")
    lines.append("")

    # Collect all CONVERGENT findings, deduplicated by pair + sentence_a
    seen = set()
    entries = []
    for source_name, data in [("Opus 5", opus5), ("GPT Sol", sol)]:
        for f in data["findings"]:
            if f["verdict"] != "CONVERGENT":
                continue
            key = (f["pair"], f["sentence_a"][:60])
            if key in seen:
                continue
            seen.add(key)
            entries.append({**f, "judge": source_name})

    by_char = defaultdict(list)
    for e in entries:
        char = e["pair"].split()[0]
        by_char[char].append(e)

    entry_num = 0
    for char in sorted(by_char):
        lines.append(f"## {char.capitalize()}")
        lines.append("")
        for e in by_char[char]:
            entry_num += 1
            lines.append(f"### Entry {entry_num}")
            lines.append("")
            lines.append(f"**Pair:** {e['pair']} ({e['pair_type']})")
            lines.append(f"**Judge:** {e['judge']}")
            lines.append(f"**Sentence A:** {e['sentence_a']}")
            lines.append(f"**Sentence B:** {e['sentence_b']}")
            lines.append("")
            lines.append("**Correction:** _(to be generated after review)_")
            lines.append("")
            lines.append("- [ ] Improved")
            lines.append("- [ ] Neutral")
            lines.append("- [ ] Worse")
            lines.append("")

    lines.append(f"---")
    lines.append(f"")
    lines.append(f"Total entries: {entry_num}")

    return "\n".join(lines)


def main():
    reports = BASE / "reports"
    reports.mkdir(exist_ok=True)
    (reports / "detection-report.md").write_text(
        compile_detection_report(), encoding="utf-8")
    (reports / "correction-report.md").write_text(
        compile_correction_report(), encoding="utf-8")
    print("Reports written to reports/")


if __name__ == "__main__":
    main()

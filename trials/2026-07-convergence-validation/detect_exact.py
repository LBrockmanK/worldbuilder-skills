"""Method 1: Exact-match sentence detection.

Splits two character notes into sentences, normalizes whitespace,
finds verbatim matches. Outputs JSON with matched sentences and their
locations in each file.

Usage: python detect_exact.py <note_a> <note_b>
       python detect_exact.py --all-pairs <out_dir> <character>
"""
import sys
import re
import json
from pathlib import Path
from itertools import combinations

MODELS = ['opus46', 'opus5', 'sol', 'terra']
PAIR_LABELS = {
    ('opus46', 'opus5'): 'within-claude',
    ('sol', 'terra'): 'within-gpt',
}

def strip_non_generated(text):
    """Remove frontmatter and Design Notes — only compare generated content."""
    lines = text.split('\n')
    out = []
    in_frontmatter = False
    in_design_notes = False
    for line in lines:
        if line.strip() == '---' and not out:
            in_frontmatter = True
            continue
        if in_frontmatter:
            if line.strip() == '---':
                in_frontmatter = False
            continue
        if re.match(r'^##\s+Design Notes', line):
            in_design_notes = True
            continue
        if in_design_notes and re.match(r'^##\s+', line) and 'Design Notes' not in line:
            in_design_notes = False
        if in_design_notes:
            continue
        out.append(line)
    return '\n'.join(out)

def split_sentences(text):
    """Split on sentence boundaries. Preserves sentence content."""
    text = strip_non_generated(text)
    raw = re.split(r'(?<=[.!?])\s+', text)
    return [s.strip() for s in raw if s.strip() and len(s.strip()) > 10]

def normalize(s):
    return ' '.join(s.split()).lower().strip()

def find_exact_matches(text_a, text_b):
    sents_a = split_sentences(text_a)
    sents_b = split_sentences(text_b)
    norm_a = {normalize(s): s for s in sents_a}
    norm_b = {normalize(s): s for s in sents_b}
    matches = []
    for key in set(norm_a) & set(norm_b):
        matches.append({
            'sentence_a': norm_a[key],
            'sentence_b': norm_b[key],
            'normalized': key,
        })
    return matches

def pair_type(model_a, model_b):
    key = tuple(sorted([model_a, model_b]))
    return PAIR_LABELS.get(key, 'cross-provider')

def run_all_pairs(out_dir, character):
    out_dir = Path(out_dir)
    results = []
    for ma, mb in combinations(MODELS, 2):
        file_a = out_dir / f'{character}-{ma}.md'
        file_b = out_dir / f'{character}-{mb}.md'
        matches = find_exact_matches(
            file_a.read_text(encoding='utf-8'),
            file_b.read_text(encoding='utf-8'),
        )
        results.append({
            'pair': f'{ma}-vs-{mb}',
            'type': pair_type(ma, mb),
            'character': character,
            'match_count': len(matches),
            'matches': matches,
        })
    return results

def run_four_way(out_dir, character):
    """Compare all 4 models together. For each sentence, count how many
    models produced it. Sentences appearing in 3+ models are strong slop;
    2 models is the pairwise baseline."""
    out_dir = Path(out_dir)
    from collections import Counter
    sent_to_models = {}
    for model in MODELS:
        path = out_dir / f'{character}-{model}.md'
        for s in split_sentences(path.read_text(encoding='utf-8')):
            key = normalize(s)
            if key not in sent_to_models:
                sent_to_models[key] = {'normalized': key, 'models': [], 'examples': {}}
            sent_to_models[key]['models'].append(model)
            sent_to_models[key]['examples'][model] = s

    results = []
    for key, data in sent_to_models.items():
        n = len(data['models'])
        if n >= 2:
            results.append({
                'normalized': key,
                'model_count': n,
                'models': data['models'],
                'examples': data['examples'],
                'character': character,
            })
    results.sort(key=lambda x: -x['model_count'])
    return results

if __name__ == '__main__':
    if sys.argv[1] == '--all-pairs':
        out_dir, character = sys.argv[2], sys.argv[3]
        results = run_all_pairs(out_dir, character)
        print(json.dumps(results, indent=2))
    elif sys.argv[1] == '--four-way':
        out_dir, character = sys.argv[2], sys.argv[3]
        results = run_four_way(out_dir, character)
        print(json.dumps(results, indent=2))
    else:
        a, b = Path(sys.argv[1]), Path(sys.argv[2])
        matches = find_exact_matches(
            a.read_text(encoding='utf-8'),
            b.read_text(encoding='utf-8'),
        )
        print(json.dumps(matches, indent=2))
        print(f'\nTotal: {len(matches)} exact matches')

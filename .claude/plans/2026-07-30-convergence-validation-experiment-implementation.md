---
type: plan
title: Convergence validation experiment implementation
description: 'Implementation plan for the cross-model convergence metric validation
  experiment: trial kit setup, 8 generations, 3 detection methods, correction pass,
  report assembly'
tags:
- complete
date: 2026-07-30
timestamp: 2026-07-30T14:16Z
resources:
- '[[2026-07-30-cross-model-convergence-metric-validation-experiment]]'
- '[[2026-07-30-convergence-validation-experiment-implementation-research]]'
---

# Convergence Validation Experiment Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use
> core-workflow:subagent-driven-development (recommended) or
> core-workflow:executing-plans to implement this plan task-by-task.
> Steps use checkbox (`- [ ]`) syntax for tracking. Execution requires
> the plan artifact's approval flip (see Approval Gate).

**Goal:** Validate whether cross-model convergence reliably identifies
slop in character notes, and whether automated corrections based on
convergence flags improve the output.

**Architecture:** Trial kit at `trials/2026-07-convergence-validation/`
following the pattern established by `trials/2026-07-writing-doctrine/`.
Python scripts for input extraction, detection, and report compilation.
Agent dispatches for character generation (Claude models) and Codex CLI
for GPT models. Reports in Markdown for human review.

**Tech Stack:** Python 3, numpy (cosine similarity), an embedding API
(third-party, not Claude or GPT — Voyage AI recommended), Codex CLI
(GPT generation)

**Spec:**
[2026-07-30-cross-model-convergence-metric-validation-experiment.md](../specs/2026-07-30-cross-model-convergence-metric-validation-experiment.md)

**Research dossier:**
[2026-07-30-convergence-validation-experiment-implementation-research.md](../research/2026-07-30-convergence-validation-experiment-implementation-research.md)

## Global Constraints

- Finished character notes (nadja.md body, kallya.md body below their
  Design Notes sections) must never be visible to generation models.
- Embedding model and LLM judge must not be from the Claude or GPT
  families — avoids circularity.
- All three detection methods run independently on every pairwise
  comparison; results merge only at the reporting stage.
- Trial kit follows the directory and procedural pattern from
  `trials/2026-07-writing-doctrine/`.

---

## File Structure

```
trials/2026-07-convergence-validation/
├── README.md                       # Experiment procedure
├── extract_inputs.py               # Extracts Design Notes + world context
├── build_packet.py                 # Assembles instruction packet from skill files
├── detect_exact.py                 # Method 1: exact-match sentence detection
├── detect_embedding.py             # Method 2: embedding similarity detection
├── compile_report.py               # Merges detection + correction into reports
├── inputs/
│   ├── packet.md                   # Assembled instruction packet (generated)
│   ├── nadja-inputs.md             # Session Notes + Builder Context (extracted)
│   ├── kallya-inputs.md            # Session Notes + Builder Context (extracted)
│   ├── world-context.md            # seed.md + agent-context.md (extracted)
│   └── roster.md                   # Cast names + brief descriptions (extracted)
├── out/
│   ├── nadja-opus46.md             # 8 generated character notes
│   ├── nadja-opus5.md
│   ├── nadja-sol.md
│   ├── nadja-terra.md
│   ├── kallya-opus46.md
│   ├── kallya-opus5.md
│   ├── kallya-sol.md
│   └── kallya-terra.md
├── detection/
│   ├── exact-results.json          # Method 1 pairwise output
│   ├── exact-nadja-4way.json       # Method 1 four-way output
│   ├── exact-kallya-4way.json      # Method 1 four-way output
│   ├── embedding-results.json      # Method 2 pairwise output
│   ├── embedding-nadja-4way.json   # Method 2 four-way output
│   ├── embedding-kallya-4way.json  # Method 2 four-way output
│   ├── judge-results.json          # Method 3 output
│   └── unflagged-sample.json       # Random sample for false-negative estimation
├── corrections/
│   └── {character}-{model}-corrections.json  # Per-note correction sets
└── reports/
    ├── detection-report.md         # Detection flags for human review
    └── correction-report.md        # Flagged sentence + rewrite pairs
```

---

### Task 1: Trial kit setup and input extraction

**Files:**
- Create: `trials/2026-07-convergence-validation/extract_inputs.py`
- Create: `trials/2026-07-convergence-validation/build_packet.py`
- Create: `trials/2026-07-convergence-validation/README.md`
- Create: `trials/2026-07-convergence-validation/inputs/` (5 files)

**Interfaces:**
- Consumes: Viralys project files, skill files from this repo
- Produces: `inputs/packet.md` (used by Task 2 for generation),
  `inputs/{character}-inputs.md` (used by Task 2), `inputs/world-context.md`
  (used by Task 2), `inputs/roster.md` (used by Task 2)

- [ ] **Step 1: Create trial directory structure**

```bash
mkdir -p trials/2026-07-convergence-validation/{inputs,out,detection,corrections,reports}
```

- [ ] **Step 2: Write extract_inputs.py**

```python
"""Extract experiment inputs from the Viralys project.

Pulls Design Notes (Session Notes + Builder Context) from each
character note, world context from seed.md and agent-context.md,
and cast roster from the notes directory. Writes to inputs/.

Usage: python extract_inputs.py <viralys_worldvault_path>
"""
import sys
import re
from pathlib import Path

CHARACTERS = {
    'nadja': {'notes_range': (21, 45)},
    'kallya': {'notes_range': (21, 56)},
}

WORLD_CONTEXT_FILES = ['seed.md', 'agent-context.md']

def extract_design_notes(note_path, start_line, end_line):
    """Extract lines from start_line to end_line (1-indexed, inclusive)."""
    lines = note_path.read_text(encoding='utf-8').splitlines()
    return '\n'.join(lines[start_line - 1:end_line])

def extract_roster(notes_dir):
    """List character names and their one-line descriptions from filenames."""
    entries = []
    for f in sorted(notes_dir.glob('*.md')):
        stem = f.stem
        first_heading = ''
        for line in f.read_text(encoding='utf-8').splitlines():
            if line.startswith('# '):
                first_heading = line.lstrip('# ').strip()
                break
        entries.append(f"- **{stem}**: {first_heading}")
    return '\n'.join(entries)

def main():
    vault = Path(sys.argv[1])
    notes_dir = vault / 'notes'
    out = Path('inputs')
    out.mkdir(exist_ok=True)

    for name, cfg in CHARACTERS.items():
        note_path = notes_dir / f'{name}.md'
        start, end = cfg['notes_range']
        content = extract_design_notes(note_path, start, end)
        (out / f'{name}-inputs.md').write_text(
            f'# {name.title()} — Design Notes\n\n{content}\n',
            encoding='utf-8',
        )
        print(f'Extracted {name} design notes (lines {start}-{end})')

    world_parts = []
    for fname in WORLD_CONTEXT_FILES:
        fpath = vault / fname
        if fpath.exists():
            world_parts.append(f'## {fname}\n\n{fpath.read_text(encoding="utf-8")}')
            print(f'Extracted {fname}')
    (out / 'world-context.md').write_text(
        '# World Context\n\n' + '\n\n---\n\n'.join(world_parts) + '\n',
        encoding='utf-8',
    )

    roster = extract_roster(notes_dir)
    (out / 'roster.md').write_text(
        '# Cast Roster\n\n' + roster + '\n',
        encoding='utf-8',
    )
    print(f'Extracted roster ({len(roster.splitlines())} characters)')

if __name__ == '__main__':
    main()
```

- [ ] **Step 3: Write build_packet.py**

```python
"""Assemble the instruction packet from current skill files.

Combines the character generation skill instructions, writing doctrine,
and slop-phrase reference into a single packet for generation agents.

Usage: python build_packet.py
"""
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent

SKILL_FILES = [
    'skills/worldbuilder-character/SKILL.md',
    'skills/worldbuilder-character/framework.md',
    'skills/worldbuilder-character/relationships.md',
    'skills/worldbuilder-character/intimate.md',
]

DOCTRINE_FILES = [
    'skills/writing-style.md',
    'docs/slop-phrases.md',
]

def main():
    parts = ['# Character Generation Instruction Packet\n']
    parts.append('## Skill Instructions\n')
    for rel in SKILL_FILES:
        path = REPO_ROOT / rel
        parts.append(f'### {rel}\n\n{path.read_text(encoding="utf-8")}\n')

    parts.append('---\n\n## Writing Doctrine\n')
    for rel in DOCTRINE_FILES:
        path = REPO_ROOT / rel
        parts.append(f'### {rel}\n\n{path.read_text(encoding="utf-8")}\n')

    parts.append('---\n\n## Generation Directive\n')
    parts.append(
        'Write a complete character note following the skill instructions '
        'above. Work through every section in order: Design Notes '
        '(reproduce the provided session notes and builder context), '
        'Background, Body, Soul, Relationships, Intimate Dynamics '
        '(if flagged). Apply the writing doctrine throughout. '
        'Do not skip sections. Do not ask questions — all inputs are '
        'provided.\n'
    )

    out = Path('inputs/packet.md')
    out.write_text('\n'.join(parts), encoding='utf-8')
    print(f'Wrote packet ({len(out.read_text(encoding="utf-8"))} chars)')

if __name__ == '__main__':
    main()
```

- [ ] **Step 4: Run extraction and packet assembly**

```bash
cd trials/2026-07-convergence-validation
python extract_inputs.py "D:\Sync\Collective Consciousness\Games\Ainime\WIP\Viralys\worldvault"
python build_packet.py
```

Verify: `inputs/` contains 5 files (nadja-inputs.md, kallya-inputs.md,
world-context.md, roster.md, packet.md). Spot-check that nadja-inputs.md
contains only Design Notes (session notes + builder context), not the
finished Background/Body/Soul sections.

- [ ] **Step 5: Review extracted inputs for contamination**

Read each extracted input file. Confirm no content from the finished
character note body (Background, Body, Soul, Relationships sections)
leaked into the inputs. The Design Notes section is builder-side
context that existed before generation — it is the input, not the
output.

- [ ] **Step 6: Write README.md**

Document the experiment procedure: what the experiment tests, how to
run each phase, what the expected outputs are, and where the reports
land. Follow the format established by
`trials/2026-07-writing-doctrine/README.md`.

- [ ] **Step 7: Commit**

```bash
git add trials/2026-07-convergence-validation/
git commit -m "feat: set up convergence validation trial kit with input extraction"
```

---

### Task 2: Character note generation (8 notes)

**Files:**
- Create: `trials/2026-07-convergence-validation/out/` (8 note files)

**Interfaces:**
- Consumes: `inputs/packet.md`, `inputs/{character}-inputs.md`,
  `inputs/world-context.md`, `inputs/roster.md` (all from Task 1)
- Produces: 8 character notes at `out/{character}-{model}.md`
  (used by Task 3 for detection)

**Prerequisites:** Confirm Codex CLI is available and can invoke GPT-5.6
Sol and Terra. Run `codex --help` or equivalent to verify.

- [ ] **Step 1: Generate Nadja under Claude Opus 4.6**

Dispatch an agent with model override `claude-opus-4-6`. The agent
prompt includes:
1. The full content of `inputs/packet.md`
2. `inputs/nadja-inputs.md`
3. `inputs/world-context.md`
4. `inputs/roster.md`
5. Instruction: write the complete character note to
   `trials/2026-07-convergence-validation/out/nadja-opus46.md`

The agent has read access to the inputs directory but not to the
Viralys project's finished notes.

- [ ] **Step 2: Generate Nadja under Claude Opus 5**

Same as step 1 with model override `claude-opus-5`. Output to
`out/nadja-opus5.md`.

- [ ] **Step 3: Generate Nadja under GPT-5.6 Sol**

Via Codex CLI. Provide the same inputs (packet + character inputs +
world context + roster) as a single prompt. Output to
`out/nadja-sol.md`.

```bash
codex --model gpt-5.6-sol --input inputs/packet.md --input inputs/nadja-inputs.md \
  --input inputs/world-context.md --input inputs/roster.md \
  --output out/nadja-sol.md
```

Adjust invocation syntax to match actual Codex CLI interface. The
content and model are fixed; the invocation method is the variable.

- [ ] **Step 4: Generate Nadja under GPT-5.6 Terra**

Same as step 3 with model `gpt-5.6-terra`. Output to
`out/nadja-terra.md`.

- [ ] **Step 5: Generate Kallya under all four models**

Repeat steps 1-4 with `inputs/kallya-inputs.md`. Outputs:
`out/kallya-opus46.md`, `out/kallya-opus5.md`, `out/kallya-sol.md`,
`out/kallya-terra.md`.

Claude generations can run in parallel (two agents). GPT generations
can run in parallel if Codex CLI supports it.

- [ ] **Step 6: Verify all 8 outputs**

For each of the 8 output files:
1. File exists and is non-empty.
2. Contains all expected sections (Design Notes, Background, Body,
   Soul, Relationships, and Intimate Dynamics if flagged).
3. Word count is in a reasonable range (compare to existing character
   notes — expect 1500-4000 words).

```bash
for f in out/*.md; do echo "$f: $(wc -w < "$f") words"; done
```

- [ ] **Step 7: Commit**

```bash
git add trials/2026-07-convergence-validation/out/
git commit -m "data: 8 generated character notes for convergence validation"
```

---

### Task 3: Detection pipeline

**Files:**
- Create: `trials/2026-07-convergence-validation/detect_exact.py`
- Create: `trials/2026-07-convergence-validation/detect_embedding.py`
- Create: `trials/2026-07-convergence-validation/detection/` (4 result files)

**Interfaces:**
- Consumes: 8 note files from `out/` (Task 2)
- Produces: `detection/exact-results.json`,
  `detection/embedding-results.json`, `detection/judge-results.json`,
  `detection/unflagged-sample.json` (all used by Task 4)

- [ ] **Step 1: Write detect_exact.py**

```python
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

def split_sentences(text):
    """Split on sentence boundaries. Preserves sentence content."""
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
```

- [ ] **Step 2: Test detect_exact.py on synthetic input**

Create two small test files with known overlapping sentences:

```bash
cd trials/2026-07-convergence-validation
cat > /tmp/test_a.md << 'EOF'
She wipes the counter without looking up. The kitchen runs on her
schedule, and everyone knows it. When someone drops a plate, she
replaces it before they apologize.
EOF
cat > /tmp/test_b.md << 'EOF'
The kitchen runs on her schedule, and everyone knows it. She keeps
the larder stocked three days ahead. When someone drops a plate, she
replaces it before they apologize.
EOF
python detect_exact.py /tmp/test_a.md /tmp/test_b.md
```

Expected: 2 exact matches ("The kitchen runs on her schedule..." and
"When someone drops a plate...").

- [ ] **Step 3: Write detect_embedding.py**

```python
"""Method 2: Embedding similarity detection.

Embeds sentences from two notes, computes pairwise cosine similarity,
flags pairs above threshold. Uses Voyage AI (voyage-3-large) to avoid
Claude/GPT family circularity.

Usage: python detect_embedding.py <note_a> <note_b> [--threshold 0.92]
       python detect_embedding.py --all-pairs <out_dir> <character> [--threshold 0.92]

Requires: VOYAGE_API_KEY environment variable.
"""
import sys
import json
import os
import numpy as np
from pathlib import Path
from itertools import combinations

MODELS = ['opus46', 'opus5', 'sol', 'terra']
DEFAULT_THRESHOLD = 0.92

def split_sentences(text):
    import re
    raw = re.split(r'(?<=[.!?])\s+', text)
    return [s.strip() for s in raw if s.strip() and len(s.strip()) > 10]

def embed_sentences(sentences, api_key):
    """Embed via Voyage AI. Returns list of embedding vectors."""
    import requests
    resp = requests.post(
        'https://api.voyageai.com/v1/embeddings',
        headers={'Authorization': f'Bearer {api_key}'},
        json={'input': sentences, 'model': 'voyage-3-large'},
    )
    resp.raise_for_status()
    data = resp.json()['data']
    return [d['embedding'] for d in data]

def cosine_similarity(a, b):
    a, b = np.array(a), np.array(b)
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))

def find_similar_pairs(text_a, text_b, api_key, threshold):
    sents_a = split_sentences(text_a)
    sents_b = split_sentences(text_b)
    if not sents_a or not sents_b:
        return []

    all_sents = sents_a + sents_b
    embeddings = embed_sentences(all_sents, api_key)
    emb_a = embeddings[:len(sents_a)]
    emb_b = embeddings[len(sents_a):]

    pairs = []
    for i, (sa, ea) in enumerate(zip(sents_a, emb_a)):
        for j, (sb, eb) in enumerate(zip(sents_b, emb_b)):
            sim = cosine_similarity(ea, eb)
            if sim >= threshold:
                pairs.append({
                    'sentence_a': sa,
                    'sentence_b': sb,
                    'similarity': round(sim, 4),
                })
    return pairs

def run_all_pairs(out_dir, character, api_key, threshold):
    out_dir = Path(out_dir)
    results = []
    for ma, mb in combinations(MODELS, 2):
        file_a = out_dir / f'{character}-{ma}.md'
        file_b = out_dir / f'{character}-{mb}.md'
        pairs = find_similar_pairs(
            file_a.read_text(encoding='utf-8'),
            file_b.read_text(encoding='utf-8'),
            api_key, threshold,
        )
        results.append({
            'pair': f'{ma}-vs-{mb}',
            'character': character,
            'threshold': threshold,
            'flag_count': len(pairs),
            'flags': pairs,
        })
    return results

def run_four_way(out_dir, character, api_key, threshold):
    """Embed all sentences from all 4 models, cluster by similarity.
    Report sentences where 3+ models converge."""
    out_dir = Path(out_dir)
    all_sents = []
    sent_meta = []
    for model in MODELS:
        path = out_dir / f'{character}-{model}.md'
        for s in split_sentences(path.read_text(encoding='utf-8')):
            all_sents.append(s)
            sent_meta.append({'model': model, 'sentence': s})

    embeddings = embed_sentences(all_sents, api_key)
    clusters = []
    used = set()
    for i in range(len(all_sents)):
        if i in used:
            continue
        cluster = [i]
        for j in range(i + 1, len(all_sents)):
            if j in used:
                continue
            if cosine_similarity(embeddings[i], embeddings[j]) >= threshold:
                cluster.append(j)
        if len(set(sent_meta[k]['model'] for k in cluster)) >= 2:
            used.update(cluster)
            models = list(set(sent_meta[k]['model'] for k in cluster))
            clusters.append({
                'model_count': len(models),
                'models': models,
                'character': character,
                'threshold': threshold,
                'sentences': {sent_meta[k]['model']: sent_meta[k]['sentence'] for k in cluster},
            })
    clusters.sort(key=lambda x: -x['model_count'])
    return clusters

if __name__ == '__main__':
    api_key = os.environ['VOYAGE_API_KEY']
    threshold = DEFAULT_THRESHOLD
    if '--threshold' in sys.argv:
        idx = sys.argv.index('--threshold')
        threshold = float(sys.argv[idx + 1])
        sys.argv.pop(idx)
        sys.argv.pop(idx)

    if sys.argv[1] == '--all-pairs':
        out_dir, character = sys.argv[2], sys.argv[3]
        results = run_all_pairs(out_dir, character, api_key, threshold)
        print(json.dumps(results, indent=2))
    elif sys.argv[1] == '--four-way':
        out_dir, character = sys.argv[2], sys.argv[3]
        results = run_four_way(out_dir, character, api_key, threshold)
        print(json.dumps(results, indent=2))
    else:
        a, b = Path(sys.argv[1]), Path(sys.argv[2])
        pairs = find_similar_pairs(
            a.read_text(encoding='utf-8'),
            b.read_text(encoding='utf-8'),
            api_key, threshold,
        )
        print(json.dumps(pairs, indent=2))
        print(f'\nTotal: {len(pairs)} pairs above {threshold}')
```

- [ ] **Step 4: Test detect_embedding.py on synthetic input**

Use the same test files from step 2. Run:

```bash
python detect_embedding.py /tmp/test_a.md /tmp/test_b.md --threshold 0.90
```

Expected: the two exact-match sentences should appear with similarity
close to 1.0. "She keeps the larder stocked three days ahead" should
not appear (unique to file B). Adjust threshold if needed based on
observed scores.

- [ ] **Step 5: Run Method 1 (exact match) on all pairs**

```bash
cd trials/2026-07-convergence-validation
python detect_exact.py --all-pairs out nadja > detection/exact-nadja.json
python detect_exact.py --all-pairs out kallya > detection/exact-kallya.json
python -c "
import json
nadja = json.load(open('detection/exact-nadja.json'))
kallya = json.load(open('detection/exact-kallya.json'))
json.dump(nadja + kallya, open('detection/exact-results.json', 'w'), indent=2)
print('Exact match results:')
for r in nadja + kallya:
    print(f\"  {r['character']} {r['pair']} ({r['type']}): {r['match_count']} matches\")
"
```

- [ ] **Step 6: Run Method 2 (embedding similarity) on all pairs**

```bash
cd trials/2026-07-convergence-validation
python detect_embedding.py --all-pairs out nadja > detection/embedding-nadja.json
python detect_embedding.py --all-pairs out kallya > detection/embedding-kallya.json
python -c "
import json
nadja = json.load(open('detection/embedding-nadja.json'))
kallya = json.load(open('detection/embedding-kallya.json'))
json.dump(nadja + kallya, open('detection/embedding-results.json', 'w'), indent=2)
print('Embedding similarity results:')
for r in nadja + kallya:
    print(f\"  {r['character']} {r['pair']}: {r['flag_count']} pairs above {r['threshold']}\")
"
```

- [ ] **Step 6b: Run 4-way convergence analysis**

Run both detection methods in 4-way mode, comparing all four model
outputs together instead of pairwise. This surfaces "convergence
breadth" — a sentence appearing in 3 or 4 models is a much stronger
slop signal than one caught in a single pair.

```bash
cd trials/2026-07-convergence-validation
python detect_exact.py --four-way out nadja > detection/exact-nadja-4way.json
python detect_exact.py --four-way out kallya > detection/exact-kallya-4way.json
python detect_embedding.py --four-way out nadja > detection/embedding-nadja-4way.json
python detect_embedding.py --four-way out kallya > detection/embedding-kallya-4way.json
python -c "
import json
for method in ['exact', 'embedding']:
    for char in ['nadja', 'kallya']:
        data = json.load(open(f'detection/{method}-{char}-4way.json'))
        by_count = {}
        for d in data:
            n = d['model_count']
            by_count[n] = by_count.get(n, 0) + 1
        print(f'{method} {char} 4-way: {by_count}')
"
```

- [ ] **Step 7: Prepare Method 3 inputs (LLM-as-judge)**

Merge flags from Methods 1 and 2 into a union set. Sample unflagged
sentence pairs for false-negative estimation.

```python
"""Prepare judge inputs: union of Method 1+2 flags plus random sample."""
import json
import random
from pathlib import Path

exact = json.loads(Path('detection/exact-results.json').read_text())
embed = json.loads(Path('detection/embedding-results.json').read_text())

flagged = set()
for r in exact:
    for m in r['matches']:
        flagged.add(m['normalized'])
for r in embed:
    for f in r['flags']:
        flagged.add(' '.join(f['sentence_a'].split()).lower().strip())

# Sample ~20 unflagged pairs per character for false-negative check
# (implementation: read all sentence pairs, exclude flagged, sample)

print(f'Total unique flagged sentences: {len(flagged)}')
print(f'Judge will review all {len(flagged)} flags + ~40 unflagged samples')
```

- [ ] **Step 8: Run Method 3 (LLM-as-judge)**

Dispatch a judge agent (Gemini 2.5 Pro) with
this prompt structure for each flagged pair:

> You are judging whether two sentences, generated independently by
> different AI models from the same character brief, express the same
> idea in the same phrasing. This is a slop detection test — high
> similarity means model-generic voice rather than author-specific
> voice.
>
> Sentence A: "{sentence_a}"
> Sentence B: "{sentence_b}"
>
> Verdict: CONVERGENT (same idea, same phrasing) or DIVERGENT (different
> enough to be author-specific). One sentence explaining your judgment.

Also run on the unflagged sample to estimate false negatives.
Write results to `detection/judge-results.json`.

- [ ] **Step 9: Commit detection results**

```bash
git add trials/2026-07-convergence-validation/detect_*.py
git add trials/2026-07-convergence-validation/detection/
git commit -m "data: detection pipeline results for convergence validation"
```

---

### Task 4: Correction pass and report assembly

**Files:**
- Create: `trials/2026-07-convergence-validation/compile_report.py`
- Create: `trials/2026-07-convergence-validation/corrections/` (per-note files)
- Create: `trials/2026-07-convergence-validation/reports/` (2 report files)

**Interfaces:**
- Consumes: `detection/` results (Task 3), `out/` notes (Task 2),
  `inputs/` (Task 1) for correction context
- Produces: `reports/detection-report.md` and
  `reports/correction-report.md` (delivered to reviewer)

- [ ] **Step 1: Run correction pass on all flagged sentences**

For each sentence flagged by any detection method, dispatch a
correction agent with this prompt:

> You are rewriting a sentence from a character note that was flagged
> as model-generic (it appeared nearly identically when two different
> AI models generated from the same brief). Rewrite it to preserve
> the semantic content while eliminating the generic phrasing.
>
> Character brief context:
> {relevant section from character inputs}
>
> Surrounding paragraph:
> {paragraph containing the flagged sentence}
>
> Flagged sentence: "{sentence}"
>
> Write one replacement sentence. Do not explain your changes.

The correction agent does not see the other model's output — it
rewrites from the character brief and note context alone.

Write results to `corrections/{character}-{model}-corrections.json`,
each entry containing: original sentence, rewrite, which methods
flagged it, which pairs produced it.

- [ ] **Step 2: Write compile_report.py**

```python
"""Compile detection and correction results into human-review reports.

Usage: python compile_report.py
"""
import json
from pathlib import Path
from collections import defaultdict

def load_json(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))

def compile_detection_report():
    exact = load_json('detection/exact-results.json')
    embed = load_json('detection/embedding-results.json')
    judge = load_json('detection/judge-results.json')

    lines = ['# Detection Report\n']
    lines.append('## Summary\n')

    total_exact = sum(r['match_count'] for r in exact)
    total_embed = sum(r['flag_count'] for r in embed)
    lines.append(f'- Method 1 (exact match): {total_exact} flags')
    lines.append(f'- Method 2 (embedding similarity): {total_embed} flags')
    lines.append(f'- Method 3 (LLM-as-judge): see per-flag verdicts below')
    lines.append('')

    lines.append('## Flags by character and pair\n')
    lines.append('Each flag shows: the convergent sentences side by side, ')
    lines.append('which method(s) caught it, which pair(s) produced it, ')
    lines.append('and the judge verdict if available.\n')

    # Group all flags by normalized sentence
    by_sentence = defaultdict(lambda: {
        'methods': set(), 'pairs': [], 'examples': [],
        'judge_verdict': None,
    })

    for r in exact:
        for m in r['matches']:
            key = m['normalized']
            by_sentence[key]['methods'].add('exact')
            by_sentence[key]['pairs'].append(
                f"{r['character']} {r['pair']} ({r['type']})")
            by_sentence[key]['examples'].append(
                (m['sentence_a'], m['sentence_b']))

    for r in embed:
        for f in r['flags']:
            key = ' '.join(f['sentence_a'].split()).lower().strip()
            by_sentence[key]['methods'].add('embedding')
            by_sentence[key]['pairs'].append(r['pair'])
            by_sentence[key]['examples'].append(
                (f['sentence_a'], f['sentence_b']))

    for i, (key, data) in enumerate(sorted(by_sentence.items()), 1):
        methods = ', '.join(sorted(data['methods']))
        pairs = '; '.join(data['pairs'][:3])
        sa, sb = data['examples'][0]
        lines.append(f'### Flag {i}\n')
        lines.append(f'**Methods:** {methods}')
        lines.append(f'**Pairs:** {pairs}')
        lines.append(f'**Sentence A:** {sa}')
        lines.append(f'**Sentence B:** {sb}')
        lines.append(f'**Your verdict:** [ ] True positive  [ ] False positive')
        lines.append('')

    return '\n'.join(lines)

def compile_correction_report():
    lines = ['# Correction Report\n']
    lines.append('Each entry shows a flagged sentence and its rewrite. ')
    lines.append('Judge each rewrite: improved / neutral / worse.\n')

    corrections_dir = Path('corrections')
    for f in sorted(corrections_dir.glob('*.json')):
        data = load_json(f)
        lines.append(f'## {f.stem}\n')
        for entry in data:
            lines.append(f'**Original:** {entry["original"]}')
            lines.append(f'**Rewrite:** {entry["rewrite"]}')
            lines.append(f'**Flagged by:** {", ".join(entry["methods"])}')
            lines.append(f'**Your verdict:** [ ] Improved  [ ] Neutral  [ ] Worse')
            lines.append('')

    return '\n'.join(lines)

def main():
    reports = Path('reports')
    reports.mkdir(exist_ok=True)
    (reports / 'detection-report.md').write_text(
        compile_detection_report(), encoding='utf-8')
    (reports / 'correction-report.md').write_text(
        compile_correction_report(), encoding='utf-8')
    print('Reports written to reports/')

if __name__ == '__main__':
    main()
```

- [ ] **Step 3: Run report compilation**

```bash
cd trials/2026-07-convergence-validation
python compile_report.py
```

Verify: `reports/detection-report.md` lists every flag with method
attribution and verdict checkboxes. `reports/correction-report.md`
lists every flagged sentence with its rewrite and quality checkboxes.

- [ ] **Step 4: Spot-check reports**

Open both reports. Verify:
1. Every flag from all three methods appears in the detection report.
2. Every flagged sentence has a corresponding correction entry.
3. No flags are duplicated.
4. The pair-type labels (within-claude, within-gpt, cross-provider)
   are correct.

- [ ] **Step 5: Commit and deliver**

```bash
git add trials/2026-07-convergence-validation/compile_report.py
git add trials/2026-07-convergence-validation/corrections/
git add trials/2026-07-convergence-validation/reports/
git commit -m "data: correction pass and review reports for convergence validation"
```

Deliver `reports/detection-report.md` and `reports/correction-report.md`
to the reviewer. The reviewer fills in verdict checkboxes for each
flag (true positive / false positive) and each correction (improved /
neutral / worse).

---

## After human review

The reviewer's filled-in reports determine the graduation decision per
the spec's success criteria:

1. **Precision**: at least one method's true-positive rate is acceptable.
2. **Cross-provider signal**: cross-provider pairs differ meaningfully
   from within-family pairs.
3. **Correction value**: rewrites judged "improved" outnumber
   "neutral" + "worse."
4. **Consistency**: results hold across both characters.

If all four hold: update METHODOLOGY.md section 5 status table —
move the convergence check (and/or individual methods) from
"Designed, validation path in section 6" to "Validated." Update
section 6 to record the experiment results and date.

If the metric fails: record the failure in METHODOLOGY.md section 6,
capture what was learned, and route the grader-agent concept to
alternative slop-detection approaches via a new inbox item.

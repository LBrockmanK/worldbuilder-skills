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

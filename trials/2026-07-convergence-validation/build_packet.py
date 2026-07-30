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

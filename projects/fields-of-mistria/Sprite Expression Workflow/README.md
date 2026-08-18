# Modular Portrait Expression Workflow

This project separates reusable authoring data from the flattened prompt files consumed by the target visual-novel platform.

## Authoring model

Prompt behavior is resolved in five layers, from broadest to most specific:

1. **Style preset** — canvas, framing, rendering style, and global negative constraints.
2. **Expression pack** — expression names and generic face/body direction.
3. **Character** — immutable identity, personality, and physicality.
4. **Sprite set** — outfit, approved references, expression pack, and one character-palette gradient.
5. **Expression override** — bespoke posing and acting for one character and sprite set.

The compiler flattens those layers into a `portrait-v1` text artifact: a readable header followed by one complete prompt per expression.

## Background standard

Every expression in a sprite set uses the same two-color character-palette gradient. The gradient is part of the sprite set's visual identity and does not change by emotion.

Emotion-gradient experiments are retained only under `diagnostics/` and in the original research files. They are not part of the production compiler contract. This avoids fixed colors that clash with some characters and character-specific adjustments that would destroy cross-character emotion consistency.

## Project layout

```text
schema/character.schema.json          Character and sprite-set contract
presets/styles/seiyo.json             Reusable Seiyo rendering preset
presets/expressions/seiyo-26.json     Existing 26-expression set
presets/expressions/core-24.json      Research-derived expression taxonomy; colors inactive
characters/celine.json                Active Celine Spring production specification
characters/celine.json                Current production and regression fixture
references/celine/                    Source sprite and characterization reference
diagnostics/celine/                   Generated comparisons and evaluation notes
sprites/celine/                       Approved production portraits and manifests
scripts/compile_prompts.py            Validator and prompt compiler
compiled/                             Generated platform-ready prompt files
tests/                                Compiler regression tests
```

The original research and example files remain unchanged as source material.

## Asset naming contract

Production portrait filenames are semantic identifiers for both the game and its AI controller:

```text
{character}_{sprite-set}_{expression}.png
```

Use lowercase snake case and stable expression IDs. Celine's approved Spring base is therefore `celine_spring_neutral.png`; later approved assets will use names such as `celine_spring_happy.png` and `celine_spring_worried_concerned.png`. Archived experiments append a descriptive suffix. Do not use generator IDs, timestamps, or vague names such as `base`, `final`, or `variant2` for production assets.

## Compile a sprite set

```powershell
python scripts/compile_prompts.py characters/celine.json --sprite-set spring --output compiled/celine_spring_character.txt
```

The production sequence has one checkpoint: approve and promote the generated neutral base, then generate the full expression pack directly from that neutral. Generate each expression independently; do not stop for a test-expression or personality-range pilot. Generation may be handled in observable batches so the user can cancel at any time, but batch boundaries are not approval gates.

Use `--only` only when isolating a targeted diagnostic or retry, not as a required pilot stage:

```powershell
python scripts/compile_prompts.py characters/celine.json --sprite-set spring --only neutral,happy,annoyed,angry,sad,surprised --output compiled/celine_spring_diagnostic_character.txt
```

## Identity and reference rules

- Identity anchors describe only stable visual facts. Do not put an emotion, pose, or background into them.
- Outfit anchors belong to a sprite set, not to the character.
- A new outfit normally means a new sprite set.
- References are ordered. The first should be the approved identity/base image; later images may clarify an outfit or feature.
- Expression prompts may alter face, head angle, gesture, and posture, but must preserve identity, clothing, and distinctive features.
- A requested gesture must fit inside the framing. If hands are important, the expression prompt must explicitly require a waist-up crop with both hands visible.

## Current production status

Celine's and Juniper's Spring sprite sets are complete under `sprites/`: each contains all 26 Seiyo expressions generated independently from its own approved neutral base, uses a fixed character-palette gradient, and maps every expression to a semantic filename in `manifest.json`. Generation notes and retained diagnostic candidates are recorded under `diagnostics/`.

The second-character test confirms that the shared style prefix and suffix, character-level identity anchors, sprite-set outfit anchors, fixed palette, and bespoke physicality layer generalize across markedly different characters. A cross-character portrait may calibrate the first base when text-only style direction drifts, but must not be supplied when generating that character's expression variants. The workflow is now ready to be extracted into a reusable skill. Expression selection by the platform is an established capability and is outside the scope of this workflow's testing.

Celine's Summer set is also complete with all 26 Seiyo expressions. This seasonal-outfit test confirms that a character can retain identity, personality-specific acting, and house style across a materially different costume when the new outfit receives its own approved neutral base, fixed gradient, references, manifest, and independently generated expression set.

# Celine Spring — Annoyed background comparison

## Inputs

- Primary identity/edit reference: `sprites/celine/spring/celine_spring_neutral.png`
- Character specification: `characters/celine.json`
- Expression: `annoyed`
- Generator: built-in ImageGen

## Acting direction held constant

Change only Celine's pose and expression to restrained annoyance appropriate to her bookish, gentle personality. She releases a quiet sigh while rolling her eyes upward; brows lifted; lips softly pursed. Her head angles back slightly. She touches two fingers lightly to one temple with a contained, precise gesture. Her posture remains modest and composed, conveying patient but unmistakable exasperation—no swagger, no hands on hips, no aggression.

Identity, outfit, Seiyo rendering, square edge-to-edge composition, and natural anatomy were explicitly locked to the approved base.

## Variants

### Character gradient

- File: `celine_spring_annoyed_candidate.png`
- Gradient: soft aqua-teal → warm pale cream
- Result: strongest continuity with the approved base and good silhouette separation. The pleasant palette slightly softens the emotional signal.

### Emotion gradient

- File: `celine_spring_annoyed_emotion_fixed.png`
- Gradient: burnt amber `#B86B32` → mid-grey `#808080`
- Result: annoyance reads more immediately and the valence shift is stronger. The amber competes with Celine's hair, gold accessories, and brown belt, reducing palette separation.

### Harmonized emotion gradient

- File: `celine_spring_annoyed_emotion_harmonized.png`
- Gradient: dusty mauve `#8A607A` → cool slate-grey `#707784`
- Result: retains a restrained low-valence emotional atmosphere while separating clearly from Celine's blonde hair, mint capelet, brown leather, and gold ornaments. This is the strongest emotion-gradient candidate of the three.

## Final workflow decision

The emotion-gradient approach is rejected for production. A rigid universal hue can collide with character colors, while character-specific harmonization removes the consistent emotion-to-color mapping that justified the approach.

All production expressions will use the sprite set's fixed character-palette gradient. The acting prompt keeps Celine's reserved physicality distinct from a generic athletic acting template and remains Celine's `annoyed` override. The fixed and harmonized emotion images remain archived evidence only.

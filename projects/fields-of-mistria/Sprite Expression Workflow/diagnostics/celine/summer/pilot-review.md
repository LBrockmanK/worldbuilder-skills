# Celine Summer personality-pilot review

## Generation

- Mode: built-in image generation, one independent call per portrait.
- Sole reference for every expression: `sprites/celine/summer/celine_summer_neutral.png`.
- Pilot: confident, laughing, annoyed, emotional, angry.
- Fixed gradient: soft muted sage green at top to warm pale cream at bottom.

## Shared QA

All five selected candidates preserve Celine's face, apparent age, peach-blonde hair, green-grey eyes, Seiyo linework and shading, sleeveless rose-pink dress, interlaced neckline trim, deep-plum belt, round gold buckle, viewer-left hanging belt end, and fixed gradient. All backgrounds reach every edge without frames. No portrait contains text, logos, signatures, watermarks, props, scenery, Spring costume leakage, or extra characters.

## Candidate results

- `confident_candidate_v1`: passes. Quiet assurance reads through the direct gaze, small smile, open shoulders, and precise open-palm gesture. Anatomy count: one head, two shoulders, two continuous arms, one complete visible hand with five plausible digits; the lowered hand is intentionally beyond the crop.
- `laughing_candidate_v1`: passes. The open laugh, closed happy eyes, lifted shoulders, and hand lightly covering the smile remain recognizably reserved Celine. Anatomy count: one head, two shoulders, two continuous arms, one complete visible hand with five plausible digits; the lowered hand is intentionally beyond the crop.
- `annoyed_candidate_v1`: rejected. Identity and costume passed, but the face read as worried or confused and the temple gesture resolved primarily as one pointing finger.
- `annoyed_candidate_v2`: passes. The upward eye-roll, pursed mouth, and paired fingertips at the temple clearly read as patient exasperation. Anatomy count: one head, two shoulders, two continuous arms, one complete visible hand with two extended fingertips and three naturally curled digits; the lowered hand is intentionally beyond the crop.
- `emotional_candidate_v1`: passes. Shining eyes, raised inner brows, fragile smile, and hand over the heart communicate grateful vulnerability. Anatomy count: one head, two shoulders, two continuous arms, one complete visible hand with five plausible digits; the lowered hand is intentionally beyond the crop.
- `angry_candidate_v1`: passes. Firm brows, set mouth, steady glare, straight shoulders, and lowered arms communicate Celine's quiet anger without generic aggression. Anatomy count: one head, two shoulders, two continuous arms, with both hands intentionally beyond the crop.

## Status

The user approved all five selected pilot candidates. They were promoted to production and added to the Summer manifest. Rejected `annoyed_candidate_v1` remains in diagnostics; accepted `annoyed_candidate_v2` was promoted.

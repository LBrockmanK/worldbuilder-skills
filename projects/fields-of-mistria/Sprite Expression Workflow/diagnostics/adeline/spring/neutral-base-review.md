# Adeline Spring neutral-base review

## Candidate v1 — rejected

- File: `adeline_spring_neutral_candidate_v1.png`
- Generation mode: built-in image generation, using the source pixel sprite as the provisional identity and outfit reference
- Dimensions: 1254 x 1254
- Status: rejected after user review; not approved or promoted
- Retry count: 0

### Review finding

- Identity, costume, gradient, and anatomy were coherent, but the rendering drifted from the established house style.
- Compared with Celine's approved neutral, v1 used glossier modern-anime rendering, sharper facial modeling, denser hair detail, heavier surface shading, and more ornate metallic and fabric treatment.
- User requested a retry using Celine's neutral as a style guide.

## Candidate v2 — rejected

- File: `adeline_spring_neutral_candidate_v2.png`
- Generation mode: built-in image generation, using Adeline's source sprite for identity/outfit and Celine's approved neutral as a style-only calibration reference
- Status: style correction succeeded, but rejected during internal visual QA; not approved or promoted
- Retry target: rendering style only

### Review finding

- Style: substantially aligned with Celine through softer rounded facial proportions, larger rounded eye construction, thin warm lines, flatter cel shading, simpler hair highlights, and restrained costume gloss.
- Reference leakage: none apparent; Celine's identity, coloring, costume, and palette were not copied.
- Defect: the lower hand and fingertips are cropped by the bottom canvas edge, failing the framing and anatomy requirements.

## Candidate v3 — rejected

- File: `adeline_spring_neutral_candidate_v3.png`
- Generation mode: built-in image generation, using Adeline's source sprite for identity/outfit and Celine's approved neutral as a style-only calibration reference
- Status: rejected after user review; not approved or promoted
- Retry target: simpler separated-hands pose with both hands fully inside the frame

### Review finding

- The prior internal QA incorrectly described an invented dark magenta bow as part of Adeline's identity. The user corrected that the source contains no bow.
- Style: rounded face and chin, oversized rounded eyes, thin warm line art, sparse soft cel shading, simple pastel hair highlights, and low-detail fabric treatment align closely with Celine's approved Seiyo neutral.
- Reference leakage: no fair skin, blonde hair, grey-blue eyes, teal palette, brooch, belt, costume construction, or pose from Celine is present.
- Outfit: plum-magenta ribbed sweetheart bodice, white puffed sleeves, white gold-edged cape, dark navy skirt, forehead ornament, gold earrings, choker, bangles, and floral cape embroidery are present.
- Background: the fixed muted deep indigo-purple to dusty rose-pink gradient reaches all four edges with no border, frame, text, signature, logo, or watermark.
- Expression and framing: composed attentive neutrality reads clearly; the generous waist-up crop includes both shoulders, elbows, wrists, hands, and every fingertip.
- Anatomy: one head, two shoulders, two arms, two elbows, two wrists, and two separated hands. The right shoulder traces to the bent right elbow, right wrist, and hand on the hip; the left shoulder traces to the lowered left elbow, left wrist, and relaxed left hand. No fused, missing, or duplicated limb is apparent.

- The broader pose and rendering still did not fit the intended character closely enough, so v3 remains diagnostic history only.

## Candidate v4 — rejected

- File: `adeline_spring_neutral_candidate_v4.png`
- Generation mode: built-in image generation, using Adeline's source sprite for identity/outfit and Celine's approved neutral as a style-only calibration reference
- Status: substantially improved, but rejected after user review; not approved or promoted
- Retry target: remove the hallucinated bow and return to Celine-like close portrait framing

### Review finding

- The face, close framing, rendering style, palette, high cape collar, and general character presentation were a much better fit.
- The hair was incorrectly rendered fully loose rather than in Adeline's subtle half-up ponytail.
- A small gold V-shaped headband was invented at the hairline even though the original has no headband or forehead accessory.

## Candidate v5 — rejected

- File: `adeline_spring_neutral_candidate_v5.png`
- Generation mode: built-in image edit, using v4 as the target, Adeline's source sprite for identity/outfit, and Celine's neutral as a style-only reference
- Status: rejected after user review because the crop ended above the established waist landmark; not approved or promoted
- Retry target: add the subtle half-up ponytail and remove the invented headband while preserving v4's successful collar and rendering

### Visual QA

- Identity: warm medium-brown skin, large violet eyes, asymmetric fringe, and long wavy pastel-pink hair remain consistent with Adeline.
- Hairstyle: a small upper-back section is gathered into a subtle half-up ponytail while most hair remains loose; no bow, ribbon, visible tie, clip, headband, circlet, or forehead ornament remains.
- Style: the close portrait, rounded eye construction, thin line work, simple cel shading, and pastel finish remain aligned with Celine's approved Seiyo neutral.
- Outfit: v4's high-collared white cape, gold edging, narrow gold choker, pointed earrings, and magenta ribbed bodice are preserved.
- Background: the fixed indigo-purple to dusty rose-pink gradient remains unchanged and reaches every edge.
- Expression and anatomy: composed neutrality reads clearly. One head and two shoulders are present; both upper arms enter the natural lower crop consistently, while elbows, wrists, and hands remain outside the frame by design. No duplicated or ambiguous visible limb is apparent.

## Candidate v6 — approved and promoted

- File: `adeline_spring_neutral_candidate_v6.png`
- Production file: `sprites/adeline/spring/adeline_spring_neutral.png`
- Generation mode: built-in image edit using v5 as the target, Adeline's source for lower-costume reconstruction, and Celine's neutral for coverage calibration only
- Status: approved by the user and promoted
- Retry target: expand the framing from a close bust to the shared Seiyo crop ending slightly below the belt

### Visual QA

- Identity and hairstyle: v5's face, warm medium-brown skin, violet eyes, asymmetric fringe, subtle half-up ponytail, loose pink hair, and bare hairline are preserved.
- Style: rounded eyes, thin line work, simple cel shading, and pastel finish remain aligned with the approved Seiyo family.
- Outfit and coverage: the high-collared white cape, gold trim, magenta ribbed bodice, complete waist and belt landmark, dark navy skirt below the belt, stacked bangles, and lower cape embroidery are visible.
- Background: the fixed indigo-purple to dusty rose-pink gradient reaches every edge with no border, text, signature, or watermark.
- Expression and framing: composed neutrality reads clearly; the portrait now matches Celine and Juniper by extending just below the belt without becoming a three-quarter-body composition.
- Anatomy: one head, two shoulders, two arms, two elbows, two wrists, and two separated hands are visible. Each shoulder traces continuously to its correct elbow, wrist, and hand; all fingertips are inside the canvas with no fused, missing, or duplicated limb apparent.
- Reference leakage: no Celine identity, hair, palette, or costume construction is present.

### Approval gate

The neutral-base gate is complete. The approved generated neutral is the first `identity-base`; the source sprite is now an `outfit-reference`. Stop here until the user requests the personality-range pilot. Preserve v1 through v5 as rejected diagnostic history.

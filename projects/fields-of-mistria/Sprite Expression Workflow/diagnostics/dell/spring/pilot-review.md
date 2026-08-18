# Dell Spring personality-range pilot review

## Pilot status

- Expressions: `confident`, `laughing`, `annoyed`, `emotional`, `angry`
- Generation mode: five independent built-in image-generation calls
- Reference policy: each candidate used only `sprites/dell/spring/dell_spring_neutral.png`; no cross-character portrait and no expression candidate was used as a reference
- Candidate version: v1 for all five expressions
- Status: all five passed internal visual QA, were approved by the user, and were promoted
- Retries: 0

## Shared invariants

- Identity and age: all candidates preserve Dell as the same unmistakably young child, with fair peach skin, large blue eyes, short tousled golden-blonde bob, uneven bangs, upward cowlick, and dark-rose rectangular hair clip on her right side.
- Style: delicate linework, large-eye construction, restrained pastel cel shading, and rendering density remain aligned with the approved neutral.
- Outfit: every candidate retains the coral-pink rolled-cuff collared shirt, rose-pink knotted neckerchief, blue-violet overall straps and dark buttons, square bib pocket, waist seam, and hip pockets.
- Background: the fixed periwinkle-blue to pale peach-pink gradient reaches every canvas edge in all five images, with no borders, text, logos, signatures, or watermarks.
- Framing: every pose is contained by a generous waist-up crop through the hip-pocket landmark; every required hand and fingertip is inside the canvas.
- Anatomy: every image contains one head, two shoulders, two arms, two elbows, two wrists, and two hands. Each shoulder traces continuously to its correct elbow, wrist, and hand; no missing, fused, ambiguous, extra, or duplicated limb is apparent.

## Candidate findings

### Confident v1 — approved and promoted

- File: `dell_spring_confident_candidate_v1.png`
- Production file: `sprites/dell/spring/dell_spring_confident.png`
- Acting: direct eyes, raised chin, fierce little grin, one hand on hip, and crisp salute communicate Dell's earnest self-appointed command rather than adult swagger.
- Anatomy: the saluting arm and hand-on-hip arm remain fully separate; both wrists and all fingers are readable.

### Laughing v1 — approved and promoted

- File: `dell_spring_laughing_candidate_v1.png`
- Production file: `sprites/dell/spring/dell_spring_laughing.png`
- Acting: closed laughing eyes, open childlike laugh, tipped head, raised loose hand, and stomach-holding hand produce energetic full-body delight.
- Anatomy: each shoulder traces cleanly to a separate hand; the raised fingers and lower hand are plausible and fully contained.

### Annoyed v1 — approved and promoted

- File: `dell_spring_annoyed_candidate_v1.png`
- Production file: `sprites/dell/spring/dell_spring_annoyed.png`
- Acting: upward glare, asymmetric brow tension, pout, and rigid hands-on-hips stance read as impatient interruption, distinct from neutral focus and genuine anger.
- Anatomy: the symmetrical separated arms reproduce the approved baseline construction without duplication or hand defects.

### Emotional v1 — approved and promoted

- File: `dell_spring_emotional_candidate_v1.png`
- Production file: `sprites/dell/spring/dell_spring_emotional.png`
- Acting: shining eyes with small gathered tears, raised inner brows, fragile grateful smile, and sudden stillness communicate being deeply moved without becoming the active `crying` expression.
- Anatomy: both arms trace continuously into two gently overlapped hands at the bib; the wrists and finger groups remain distinguishable and plausible.

### Angry v1 — approved and promoted

- File: `dell_spring_angry_candidate_v1.png`
- Production file: `sprites/dell/spring/dell_spring_angry.png`
- Acting: sharply lowered brows, blazing direct eyes, clenched teeth, forward lean, braced shoulders, and two low fists communicate genuine protective anger clearly beyond Dell's ordinary intensity.
- Anatomy: both arms and clenched fists are separated from the torso and from each other; both thumbs and natural folded-finger masses are readable, with no duplicated limb.

## Approval gate

The personality-range pilot gate is complete. Six production portraits now exist including neutral. Generate each of the remaining twenty expressions independently from the approved neutral only; do not use a pilot expression or cross-character portrait as a reference.

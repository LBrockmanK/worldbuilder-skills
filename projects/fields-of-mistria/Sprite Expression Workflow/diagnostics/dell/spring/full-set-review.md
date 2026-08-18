# Dell Spring remaining-expression review

## Batch status

- Scope: the twenty Seiyo-26 expressions not already approved as neutral or pilot portraits
- Generation mode: one independent built-in image-generation call per successful portrait
- Reference policy: every candidate used only `sprites/dell/spring/dell_spring_neutral.png`; no pilot candidate, other expression, source sprite, or cross-character portrait was used as a reference
- Candidate version: v1 for every expression
- Status: all twenty passed internal visual QA, were approved by the user, and were promoted
- Visual retries: 0
- Service-level retry: 1 wording-only retry for the `flirty` taxonomy slot. The image service blocked the adult-coded label when paired with a child, so the successful output was generated under Dell's authored non-romantic behavior name, `playful show-off`, and retained under the required `flirty` project ID. No blocked image candidate was produced.

## Shared QA

- Identity and age: every candidate preserves Dell as the same unmistakably young child, including fair peach skin, large blue eyes, short tousled golden-blonde bob, uneven bangs, upward cowlick, and right-side dark-rose rectangular hair clip.
- Style: all images retain the approved early-to-mid-2000s Key visual-novel eye construction, delicate linework, restrained pastel cel shading, and rendering density.
- Outfit: every image preserves the coral-pink rolled-cuff collared shirt, knotted rose neckerchief, blue-violet overall straps and dark buttons, square bib pocket, waist seam, and hip pockets.
- Background: every image retains the fixed periwinkle-blue to pale peach-pink gradient to all four canvas edges, with no frame, border, text, logo, signature, or watermark.
- Framing: every required gesture is fully contained in a waist-up composition through the hip-pocket landmark. `stoic` places relaxed fingertips close to the bottom edge but keeps them fully inside the canvas.
- Anatomy: each image contains one head, two shoulders, two arms, two elbows, two wrists, and two hands. Both shoulder-to-hand paths were traced in every candidate. No missing, fused, ambiguous, extra, or duplicated limb is apparent.

## Expression findings

- `amused`: crooked conspiratorial smile, sidelong eyes, near-mouth hand, and hand-on-hip posture clearly communicate contained private amusement. Both hands are plausible and separate.
- `beaming`: wide delighted grin, sparkling eyes, lifted shoulders, and two raised victory fists communicate explosive triumph. Both fists remain fully contained and anatomically plausible.
- `blushing`: strong cheek blush, averted eyes, suppressed pleased smile, back-of-head rub, and strap grip read as praise-induced self-consciousness. The pose remains strictly childlike.
- `comedic-shock`: enormous eyes, high brows, open gasp, and two spread hands produce unmistakable exaggerated shock. Each open hand has five plausible digits and remains separate from the torso.
- `crying`: streaming tears, trembling mouth, wiping fist, hunched shoulders, and strap grip clearly distinguish active grief from `sad` and `emotional`.
- `embarrassed`: vivid red face, hard-averted gaze, scrunched mouth, cheek press, and opposite strap grip communicate mortification. Arms are separated with no crossing.
- `emotional-shock`: wide fixed eyes, softly open mouth, rigid shoulders, one strap grip, and one motionless lowered hand communicate quiet stunned disbelief rather than comedy. The lowered fingertips remain inside the canvas.
- `flirty`: implemented as Dell's child-safe `playful show-off` behavior: cheeky grin, raised brow, bright eyes, and two proud thumbs-up gestures. It contains no romantic, glamorous, or adult-coded acting.
- `happy`: relaxed bright eyes, small contented smile, hand on hip, and open presenting hand communicate ordinary successful-patrol happiness, quieter than `beaming` or `laughing`.
- `intimate`: implemented as quiet familial trust: soft eyes, vulnerable smile, inward shoulders, and low clasped hands. The hands overlap plausibly and the pose contains no romantic framing.
- `nervous`: sideways darting eyes, raised worried brows, tense grin, sweat drop, hunched shoulders, and separate strap grips communicate attempted bravery.
- `sad`: downcast eyes, raised inner brows, small downward mouth, slumped shoulders, and low bib-edge grip communicate quiet defeat without active tears.
- `shy`: faint blush, lowered lashes, hesitant upward look, tucked chin, strap pinch, and small second-hand fidget communicate childlike shyness.
- `sleepy-tired`: drooping eyelids, loose mouth, eye-rubbing fist, sagging posture, and stubborn hand on hip communicate patrol exhaustion. Arms are cleanly separated.
- `smiling`: softened brows, warm closed-mouth smile, hand on hip, and relaxed palm over the bib pocket communicate approachable calm, distinct from `happy`.
- `stoic`: level brows, fixed gaze, firm mouth, squared shoulders, and rigid attention stance communicate a child imitating a legendary captain. Both low hands and fingertips are fully inside the canvas.
- `surprised`: widened eyes, raised brows, small open mouth, strap grip, and half-lifted open hand communicate genuine restrained surprise, clearly milder than `comedic-shock`.
- `upset`: wet averted eyes, furrowed brows, tight mouth, tense shoulders, and two strap grips communicate defensive hurt without becoming `crying` or `nervous`.
- `wary`: narrowed eyes, guarded torso angle, one hand on hip, and one forward stop hand communicate alert suspicion. The forward hand's enlargement is intentional foreshortening; it has five plausible digits and a continuous shoulder-to-wrist connection.
- `worried-concerned`: searching eyes, deeply furrowed brows, parted lips, forward lean, and tight hand clasp communicate urgent outward-focused concern. Both arms trace cleanly into the clasp.

## Approval gate

The remaining-expression gate is complete. All twenty approved candidates have been promoted under semantic production filenames, and the manifest now maps the complete Seiyo-26 set.

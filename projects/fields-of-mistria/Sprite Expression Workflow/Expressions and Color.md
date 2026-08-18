# A 24-expression palette for AI-driven game character sprites

**The strongest evidence supports a tiered set of 24 expressions paired to specific saturated hues fading toward white, grey, or black.** Ekman's basic six anchor the perceptually-distinct facial cores; Plutchik, Russell's circumplex, and the OCC model add narratively essential states (pride, relief, hope, contempt) that pure-face frameworks miss; Cowen & Keltner's 27-category study sets a defensible ceiling. On the color side, Valdez & Mehrabian's brightness-pleasure regression (Pleasure ≈ 0.69·Brightness) and Jonauskaite's 30-nation study (cross-cultural similarity r = 0.88) directly validate the proposed gradient logic: **brighter endpoints read positive, darker endpoints read oppressive, hue carries category**. The 24-expression set below covers all four valence/arousal quadrants of the circumplex, every Ekman primary plus contempt, the OCC story-beat states, and the iconic VN/JRPG nuance expressions (smug, flirty, despondent) — without the redundant overlaps that bloat 28+ sprite kits.

## How the set was bounded

Practitioner conventions and academic frameworks converge on **roughly 20–28** as the upper bound for genuinely distinct expressions. Visual-novel starter kits (TavernSprite's 28, Napalmnacey's 25, GB Patch's component-based 15+) cluster in this band, and Cowen & Keltner empirically find ~27 categories before gradients blur. Below 10 expressions you lose narrative range; above ~25 you start duplicating intensity ladders better handled by layered blush, tear, and brow components. **The sweet spot is 20–25 monolithic expressions plus optional layered overlays for sweat, tears, and blush** — the production pipeline used by Persona 5, Doki Doki Literature Club, and Argent Games.

Several "obvious" expressions were deliberately consolidated. Surprised and Shocked are the same Ekman category at different arousal levels (use one base plus an intensity overlay). Pleased collapses into Happy. Confident, Serious, and Fierce all collapse into Determined. Smug and Smirk merge. Annoyed becomes a low-intensity Angry (or a brow-only layer). Rage stays separate only because its visual signature (bared teeth, full-face flush) is qualitatively different from Anger — and is handled here as the high-intensity overlay variant of Angry rather than a base sprite.

## Color logic in three lines

The gradient scheme — **rich saturated hue → white for positive, → grey for neutral, → black for negative/dark** — is empirically robust. Valdez & Mehrabian (1994) showed brightness drives pleasure ratings nearly three times more than saturation, so the white/black axis is doing the heaviest emotional lifting. Hue then assigns category: **red for anger, blue for sadness, yellow for joy, green for disgust/contentment, purple for fear/pride, pink for love/embarrassment** — the universal anchors confirmed across 30 nations by Jonauskaite et al. (2020). Saturation should peak at the sprite-side endpoint of every gradient; a desaturated start fades muddily rather than dramatically.

Three edge cases warrant special handling. **Embarrassment is bivalent** — comedic blush trends positive, mortified shame trends negative — so it defaults to grey-fade with director override. **Surprise is valence-neutral** until context resolves it; default to grey. **Nostalgia is bittersweet**; sepia → grey reads as wistful adult memory, sepia → white as golden childhood.

## Tier 1: the core ten

These cover roughly 85% of dialogue beats and map cleanly onto Ekman's primaries plus the four expressions visual novels cannot live without (Embarrassed, Confused, Smug, Neutral).

| Expression | Narrative use | Hex | Hue | Fade |
|---|---|---|---|---|
| **Neutral** | Default listening, exposition | `#9E9E9E` | Mid-grey | → grey |
| **Happy** | Friendliness, agreement, small pleasures | `#FFC93C` | Warm gold-yellow | → white |
| **Sad** | Loss, regret, sympathy | `#2C5F8D` | Steel blue | → black |
| **Angry** | Conflict, frustration, hostility | `#DC143C` | Crimson | → black |
| **Surprised** | Plot reveals, sudden information | `#00D4FF` | Electric cyan | → grey |
| **Fearful** | Threat, danger, dread onset | `#5B2C82` | Deep violet | → black |
| **Disgusted** | Moral rejection, revulsion, bad food | `#9ACD32` | Chartreuse | → black |
| **Embarrassed** | Romance fluster, social misstep | `#FF8FA3` | Coral pink | → grey |
| **Confused** | Questions, lost, head-tilt beats | `#A89FB8` | Lavender-mauve | → grey |
| **Smug** | Teasing, knowing, light superiority | `#C9A227` | Mustard gold | → grey |

The crimson-vs-pink split is the single most important color decision in the set. Red's universal love/anger duality (Jonauskaite calls it the "most controversial" hue) is resolved by giving anger crimson and routing all affectionate/romantic beats through pink. **Chartreuse for disgust comes directly from Valdez & Mehrabian's finding that yellow-green is the single least pleasant hue** — the same reason Pixar painted Disgust that color. **Deep violet for fear** matches Pixar's *Inside Out* canon and Plutchik's wheel, while distinguishing fear from royal purple (pride) and aubergine (sinister) by hue position. **Mustard gold for Smug** captures self-satisfaction without competing with Triumphant's brighter gold.

## Tier 2: the extended ten

These add nuance for romance arcs, action beats, and emotional reveals that the core ten cannot carry alone.

| Expression | Narrative use | Hex | Hue | Fade |
|---|---|---|---|---|
| **Joyful (laughing)** | Open laughter, peak delight | `#FFD60A` | Sunny yellow | → white |
| **Despair (crying)** | Grief breakdown, sobbing | `#0B1F3A` | Midnight navy | → black |
| **Determined** | Resolve, pre-battle, focus | `#1E40AF` | Deep cobalt | → white |
| **Flirty** | Active charm, romantic initiation | `#FF4FA3` | Hot pink-magenta | → white |
| **Worried** | Sympathetic concern, anticipation | `#4A6378` | Muted slate blue | → grey |
| **Thoughtful** | Contemplation, problem-solving | `#5C7AA0` | Slate blue | → grey |
| **Hurt** | Physical pain, sudden emotional injury | `#D14B1F` | Burnt orange-red | → black |
| **Bored** | Disinterest, comedy reaction | `#7B7AA8` | Dusty indigo | → grey |
| **Tired** | Exhaustion, morning scenes | `#6B7B8C` | Dusty blue-grey | → grey |
| **Triumphant** | Victory, vindication, pride peak | `#FFC300` | Bright gold | → white |

The Joyful/Happy split is intensity-based: Happy is the workhorse smile, Joyful is the eyes-closed laugh. Likewise Despair is the visually distinct sobbing variant of Sad — its midnight navy reads as the bottom of the sadness spectrum where steel-blue Sad sits at the middle. **Determined deliberately fades to white** rather than grey because it carries heroic forward-momentum; if your story has grim or vengeful determination, swap to burgundy `#800020` → black for that variant. **Bored takes Pixar's *Inside Out 2* Ennui indigo directly** — dusty, low-arousal, instantly readable. The blue-grey distinction between Tired (energy drained, cooler) and Worried (anxious, more saturated) is subtle but works in gradients because the saturated sprite-side endpoint differentiates them clearly. **Hurt's burnt orange-red** sits between Anger's crimson and a sickly tone — it reads as sudden injury rather than sustained hostility.

## Tier 3: four signature expressions for genre range

These four extend the system convincingly into lighthearted, serious, dramatic, and dark territory respectively. Skip them for short or tonally-narrow projects; include them for AI-driven systems that need range.

| Expression | Narrative use | Hex | Hue | Fade |
|---|---|---|---|---|
| **Relieved** | Danger passed, exhalation, gratitude | `#7FD8C9` | Soft turquoise | → white |
| **Suspicious** | Mystery, social deduction, doubt | `#7A8C2C` | Olive | → grey |
| **Nostalgic** | Memory, reverie, bittersweet recall | `#B8763E` | Mid-sepia | → grey |
| **Sinister** | Villain reveal, menace, malice | `#2D0A3A` | Deep aubergine | → black |

**Turquoise for Relief** comes from Jonauskaite's strongest cross-cultural finding for that hue and matches the cooling/exhalation feel. **Sepia for Nostalgia** is the definitive choice — the photographic toning convention has been culturally cemented since the 1840s. **Aubergine for Sinister** draws on Argento and *Suspiria*-tradition supernatural horror; it sits well below fear's deep violet on the brightness axis, so the gradient to black amplifies the menace rather than competing with it. **Olive for Suspicious** threads a needle: green carries the "wary/jealous" valence (Hupka 1997) without sliding into Disgust's chartreuse.

## What this set deliberately omits

A few popular expressions were considered and rejected as redundant. **Pride** is covered by Triumphant (the visible behavioral form). **Annoyed** is Angry at lower intensity — handle via brow overlay. **Shocked** is Surprised at higher intensity — same overlay logic. **Contempt** could be added as a 25th (`#7C7438` mustard-olive → black) for villain-heavy games, but Smug plus Disgusted overlap most contempt beats. **Love** as a stand-alone expression is rare in practice; characters express love through Happy, Flirty, or Embarrassed in nearly every shipping VN. **Manic/unhinged** is genre-specific (yandere, horror reveals) and worth adding only for those projects — use deep magenta `#B83DBA` → black if needed. **Envy** can be added as teal `#0CC0D6` → black following *Inside Out 2* if your story leans on rivalry.

## Implementation notes for an AI-driven pipeline

Three production decisions strongly improve outcomes. First, **build sprites as layered components** (eyes, brows, mouth, blush, sweat, tears) rather than monolithic images — the AI controller can then compose novel blends like "smiling-with-tears" or "angry-and-crying" that single-image kits cannot express, matching the Persona 5 and Argent Games pipelines. Second, **boost saturation hard at the sprite-side end of every gradient** because Valdez & Mehrabian's regression shows saturation drives arousal even when brightness drives pleasure; a muted start fades muddily. Third, **let the LLM controller pick expressions via valence/arousal coordinates** rather than emotion names — this maps directly onto Russell's circumplex and produces more graceful interpolation between states than discrete keyword matching.

For global audiences, consider replacing pure white (`#FFFFFF`) with warm cream (`#FFF8E7`) at the bright endpoint. White carries mourning connotations in parts of East and South Asia, and cream preserves the brightness-pleasure effect while sidestepping the cultural ambiguity. The directionality of the gradient — getting *brighter* — is what reads as positive; the exact endpoint matters less than the trajectory.

## Conclusion

The 24-expression set is dense enough to handle dating sims, JRPGs, mystery games, and horror VNs without per-genre customization, but small enough that an artist can produce a complete sheet in a reasonable budget. Its central insight is that **emotion frameworks and color psychology converge on the same coarse structure** — Ekman's six map onto Jonauskaite's strongest universal hue associations, and the OCC story-beats correspond to predictable brightness/saturation profiles. The gradient-fade scheme exploits this convergence: hue does the categorical work, brightness does the valence work, and saturation does the arousal work. For an AI-powered system specifically, the highest leverage comes from layered component sprites combined with valence/arousal-coordinate selection — that combination turns 24 base expressions into an effectively continuous emotional surface.
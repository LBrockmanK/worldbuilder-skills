---
type: reference
title: "Luc — Conversations"
description: "Extracted dialogue from Luc's conversation bank: banked lines, market lines, museum lines, gift lines, festival lines, and bee facts thread."
tags:
- agent-ready
date: 2026-08-16
timestamp: 2026-08-16T18:00Z
resources:
- projects/fields-of-mistria/source/t2/Conversations/Bank/Luc/Banked Lines/
- projects/fields-of-mistria/source/t2/Conversations/Bank/Luc/Market Lines/
- projects/fields-of-mistria/source/t2/Conversations/Bank/Luc/Museum Lines/
- projects/fields-of-mistria/source/t2/Conversations/Bank/Luc/Gift Lines/
- projects/fields-of-mistria/source/t2/Conversations/Festival Lines/Luc/
- projects/fields-of-mistria/source/t2/Conversations/Threads/Luc/
---

# Luc — Conversations

Source: `source/t2/Conversations/` — bank (banked lines, market, museum, gifts), festival lines, and threads.

All dialogue is Luc speaking unless otherwise attributed. `[Ari]` is the player character name placeholder. `=Item=` and `$Item$` are item reference markers in the source.

---

## Banked Lines

Source: `Conversations/Bank/Luc/Banked Lines/` (46 files)

### ants_in_bed.c.toml

**ants_in_bed** — refresh: 1y | requires: time_of_day != night | portrait: sad
> "I used to go to sleep hugging my terrarium, but I kept getting ants in my bed..."

### basement.c.toml

**basement_1** — refresh: instantly | priority: basement | portrait: happy
> "Oh, hello! Greetings!"

### bed.c.toml

**bed** — refresh: 1w | priority: max | requires: time_of_day = night, luc_is_at = lucs_room/Luc Bed | portrait: think
> "Mama says we have to go to bed."
> (next) portrait: sad — "She doesn't believe me when I tell her I'm nocturnal!"

**bed_2** — refresh: 1w | priority: max | requires: time_of_day = night, luc_is_at = lucs_room/Luc Bed | portrait: think
> "Some people count sheep to fall asleep, but I like to count beetles."

### big_ant_dream.c.toml

**big_ant_dream** — refresh: 1y | portrait: think
> "I had a dream I was riding a big ant, like a horse."
> (next) portrait: happy, effect: cheery — "It sure would be neat if the Dragonguard could all ride big ants!"

### biggest_bug.c.toml

**biggest_bug** — refresh: 1y | portrait: think
> "I wonder what's the biggest bug that ever lived in Mistria..."

### caterpillar.c.toml

**caterpillar** — refresh: 1y | portrait: mad
> "Did you know a caterpillar can survive on only one large leaf a day? Amazing."

### cocoon.c.toml

**cocoon** — refresh: 1y | requires: time_of_day != night | portrait: happy, effect: sparkles
> "Sometimes, at night, I twirl up my sheets and pretend I'm in a cocoon!"

### cool_bug.c.toml

**cool_bug** — refresh: 1y | requires: luc_is_traveling_to_location = lucs_room, time_of_day = evening OR night | portrait: mad
> "Good night, [Ari]. Be sure to wake me up if you see a cool bug."

### dad_plays_lute.c.toml

**dad_plays_lute** — refresh: 1y | requires: hemlock_animation = lute_play, luc_is_at_location = same as hemlock | portrait: happy
> "Bella the orchid mantis likes when Papa plays the lute. She kind of sways around..."

### dell_leader.c.toml

**dell_leader** — refresh: 1y | requires: luc in dell's zone and maple's zone | portrait: happy
> "Dell's our leader!"
> (next) portrait: embarrassed — "She's cool and strong, but most importantly she listens to me talk about bugs."

### dells_going_in_the_fountain.c.toml

**dells_going_in_the_fountain** — refresh: 1y | requires: fountain_play = true, luc in dell's zone, dell near fountain | source: NAR-1263
> "There is a non-zero probability that Dell will jump in that fountain."

### dinner_is_important.c.toml

**dinner_is_important** — refresh: 1y | requires: time_of_day = evening, luc_activity = eat | portrait: happy
> "Dinner is very important! That's what Doctor Valen told me!"

### giant_insects.c.toml

**giant_insects** — refresh: 1y | requires: luc in errol's zone | portrait: happy
> "Mr. Errol says insects used to be REALLY ginormous in the past. I wanna see!"

### going_to_sleep.c.toml

**going_to_sleep** — refresh: 1y | requires: time_of_day = evening OR night | portrait: happy
> "It takes me a while to go to sleep because I have to say good night to all my bugs, going in alphabetical order by genus."

### good_at_bugs.c.toml

**good_at_bugs** — refresh: 1y | requires: museum_insect_count >= 15 | portrait: happy, effect: sparkles
> "[Ari], [Ari]! How'd you get so good at catching bugs?"

### great_at_bugs.c.toml

**great_at_bugs** — refresh: 1y | requires: museum_insect_count >= 30 | portrait: mad, effect: shock
> "Wow, [Ari]! You're like a legendary bugcatcher!"

Note: Source has a commented-out condition `museum_insect_legendary_count = 1, comparator = ">="`.

### greeting_ari.c.toml

**greeting_ari** — refresh: never | priority: max | requires: luc_has_met = false | source: NAR-791
> "Hello! Do you like bugs?"
> **Player choice:** "Y...yes?" (next .1) | "What?" (next .3)

Path 1:
> portrait: happy — "Excellent. My name's Luc! I'm so excited to have a fellow insect enthusiast in town. Finally!"
> portrait: neutral, effect: sparkles — "Wait until I tell my sisters!"

Path 2:
> "You know, insects? My name's Luc and I'm a junior member of The Royal Society of Entomology."
> portrait: happy — "I get a birthday card from them every year in recognition of my work. If you join, maybe you will too!"

### hayden_is_nice.c.toml

**hayden_is_nice** — refresh: 1y | requires: luc in hayden's zone | portrait: happy | source: NAR-752
> "Mister Hayden sure is nice... I like him."

### hungry_caterpillar.c.toml

**hungry_caterpillar** — refresh: 1y | requires: day_time >= 4:00pm, luc traveling to inn/general_store_home/lucs_room, day_of_week != friday | portrait: happy
> "I'm hungry, and sleepy... like a sleepy, hungry caterpillar..."

### i_like_bugs.c.toml

**i_like_bugs** — refresh: 1y | requires: date_time <= 2w (early game) | portrait: neutral
> "Do you like bugs, [Ari]? I think they're pretty neat."
> (next) portrait: happy — "If you see one you gotta let me know, okay?"

### insects_are_spies.c.toml

**insects_are_spies** — refresh: 1y | portrait: embarrassed | source: NAR-758
> "The Dragonguard spy network is all the insects I've trained to bring me information. It's, um... still a work in progress."

### insects_in_mines.c.toml

**insects_in_mines** — refresh: 1y | requires: had_item_lantern_moth = false | portrait: think
> "I wonder what kind of insects are in the Mines!"
> (next) portrait: neutral — "Dell says we'll explore there, when we're older. That's good, I'll be less scared by then."

Note: Source has a commented-out condition `museum_insect_upper_mines_count = 0`.

### loose_spider.c.toml

**loose_spider** — refresh: 1y | requires: luc_building = inn | portrait: think
> "I wonder how Arthur keeps getting out... I should record this in my Tarantula File."

### marrying_off.c.toml

**marrying_off** — refresh: 1y | requires: luc near maple, queen_maple = true | portrait: think
> "Queen Maple says she's marrying me off to a princess I've never met for political reasons, and if I'm lucky it might grow into love."
> (next) portrait: happy, effect: sparkles — "I don't get it, but I'll do it for the kingdom!"

### mom_is_kicking_dad.c.toml

**mom_is_kicking_dad** — refresh: 1y | requires: location = inn, josephine and hemlock near each other and eating, luc near both | source: NAR-756
> "Mama keeps kicking Daddy under the table... I wonder if he's in trouble."

### morning.c.toml

**morning** — refresh: 1y | requires: time_of_day = morning | portrait: happy
> "Morning, [Ari]! I'm thinking about what bugs the day will bring..."

### most_royal.c.toml

**most_royal** — refresh: 1y | requires: luc near maple | portrait: think
> "Maple asked me which bug is the most royal."
> (next) portrait: happy — "Most people think monarch butterfly, but I like sternocera aequisignata- the jewel beetle- way more."

### needs_trail_mix_mom_packed_snacks.c.toml

**mom_packed_trail_mix** — refresh: 1y | requires: time_of_day = morning OR afternoon | actions: gives trail_mix | source: NAR-754
> "Mom packed us lots of snacks, [Ari]! Here, you can have some."

### orchid_mantis_loose.c.toml

**orchid_mantis_loose** — refresh: 1y | requires: location = lucs_room, time_of_day = evening OR night | portrait: neutral
> "Hi [Ari]. I'm supposed to be sleeping, but Bella the orchid mantis got out."
> (next) portrait: think — "Maybe she went to the kitchen for a snack?"

### queen_bee.c.toml

**queen_bee** — refresh: 1y | requires: luc near maple | writes: queen_bee = true | portrait: sad
> "I'm teaching Maple about the worker bees of apis mellifera, but she only cares about the queen bee."

### queen_maple.c.toml

**queen_maple** — refresh: 1y | requires: luc near maple, time_of_day = morning | writes: queen_maple = true (expires 18h) | portrait: neutral
> "I promised Maple we'd play royals today, so for the rest of today she's Queen Maple."
> (next) portrait: mad — "Please act accordingly, [Ari]."

### rachelle.c.toml

**rachelle** — refresh: 1y | requires: time_of_day = morning | portrait: neutral
> "Rachelle woke me up today... she's a mantis religiosa, otherwise known as a praying mantis."
> (next) portrait: happy — "She's nice."

### rainy_day_insects.c.toml

**rainy_day_insects** — refresh: 1y | requires: weather = rainy | portrait: think
> "Some insects prefer to come out on rainy days, [Ari]."

### rainy_dragonguard_meeting.c.toml

**rainy_dragonguard_meeting** — refresh: 1y | requires: weather = rainy, luc near dell and maple
> "Dell likes to hold our Dragonguard meetings on rainy days. That's when we make all our plans for protecting Mistria!"

### register_1.c.toml

**register_1** — refresh: 1y | requires: location = inn, luc_is_at = inn/Inn Register
> "Ma and Pa are busy today, so I'm watching the register. I can make change, I'm good at math! Want to see?"

### register_2.c.toml

**register_2** — refresh: 1y | requires: location = inn, luc_is_at = inn/Inn Register
> "I like helping out, but I sure wish I could see over the counter."

### register_3.c.toml

**register_3** — refresh: 1y | requires: location = inn, luc_is_at = inn/Inn Register | portrait: happy
> "According to my calculations, today has seen a fifty percent boost in sales because I'm behind the counter."

### register_4.c.toml

**register_4** — refresh: 1y | requires: location = inn, luc_is_at = inn/Inn Register | portrait: happy
> "Hi [Ari]! Welcome to my house!"
> (next) portrait: embarrassed — "I mean, um, The Sleeping Dragon Inn."

### royal_dinner.c.toml

**royal_dinner** — refresh: 1y | requires: luc near maple, queen_maple = true | portrait: think
> "Queen Maple says it's time to partake of our royal dinner. I hope that's the same as our normal dinner."

### seen_any_beehives.c.toml

**seen_any_beehives** — refresh: 1y | portrait: embarrassed | source: NAR-748
> "Have you seen any beehives around? Why? Uh... no reason..."

### teaching_about_bees.c.toml

**teaching_about_bees** — refresh: 1y | requires: luc near maple | portrait: happy | source: NAR-749
> "Bees have a queen, but they can't have two, so one has to leave... and sometimes they fight it out for the crown!"

### travel_to_juniper.c.toml

**travel_to_juniper** — refresh: 1y | requires: luc traveling to bathhouse, juniper at bathhouse | portrait: think | source: NAR-753
> "Miss Juniper will answer all the Dragonguard's questions about potions... I think."

### travel_to_sleep.c.toml

**sleep_honeycomb** — refresh: 1y | requires: location = lucs_room, day_time >= 7:00pm | source: NAR-751
> "Time to get all curled up in my honeycomb..."

### week_one_pt_1.c.toml

**week_one_pt_1** — refresh: never | priority: max | requires: date_time < 14d, luc_was_last_spoken_to > 8h ago | source: NAR-792
> "Greetings, [Ari]! Have you cut the grass around your farm yet?"
> (next) portrait: happy — "Tall grass is a natural habitat for many insects."
> (next) portrait: think — "Vegetables are a good habitat too, I guess."

### week_one_pt_2.c.toml

**week_one_pt_2** — refresh: never | priority: max | requires: date_time < 14d | source: NAR-793
> "[Ari]! Have you broken up the rocks around your farm?"
> (next) portrait: happy — "Sometimes there's insects living underneath! I'd love to see what you find!"

### wish_hemlock_would_bring_to_beehives.c.toml

**wish_dad_would_bring_to_beehives** — refresh: 1y | requires: location != deep_woods | portrait: sad | source: NAR-750
> "*sigh* Wish Dad would take us to the woods sometime. I bet I could find a beehive there."

---

## Market Lines

Source: `Conversations/Bank/Luc/Market Lines/` (26 files)

### Darcy's Stall

Source: `market_darcy_1.c.toml` through `market_darcy_4.c.toml` | all require luc_activity = visit_darcy_stall | all priority: max, refresh: 1y

**market_darcy_1** (source: NAR-760)
> "Darcy's so nice! She always gives me and Maple =Hot Chocolate=."

**market_darcy_2** (source: NAR-761)
> "Last time Dell got coffee, she got sooo hyper... she kept calling all my insects "tiny dragons", and then she said SHE was turning into a dragon... wow, [Ari]. Just wow."

**market_darcy_3** (source: NAR-762)
> "Darcy's been making different flavors of hot chocolate... I really like the spicy one..."

**market_darcy_4** (source: NAR-763)
> "In the winter, hot chocolate... in the summer, chocolate milk... Darcy is the best."

### Louis's Stall

Source: `market_louis_1.c.toml` through `market_louis_4.c.toml` | all require luc_activity = visit_louis_stall | all priority: max, refresh: 1y | portrait: neutral

**market_louis_1** (source: NAR-767)
> "Mister Louis promised me that he would make me a full beetle print suit for my debut at the Royal Society of Entymology! Now I REALLY have to get in..."

Note: Source spells it "Entymology" (differs from "Entomology" used in greeting_ari.c.toml).

**market_louis_2** (source: NAR-768)
> "Did you know that silk comes from the cocoons of domesticated silkworms? Amazing!"

**market_louis_3** (source: NAR-769)
> "Mister Louis told me that some dyes are made from insect shells! Isn't that interesting?"

**market_louis_4** (source: NAR-1109)
> "Mister Louis says he'll consider insect prints for a future collection... I want a coat with a big praying mantis on the back."

### Merri's Stall

Source: `market_merri_1.c.toml` through `market_merri_4.c.toml` | all require luc_activity = visit_merri_stall | all priority: max, refresh: 1y | source: NAR-770 through NAR-773

**market_merri_1**
> "Miss Merri's booth always smells like wood and paint... it's not so bad, though."

**market_merri_2**
> "I wonder if Miss Merri has a tiny dresser for sale... it's for my pet spider, of course. She has lots of socks."

**market_merri_3**
> "I always check Miss Merri's booth for princessy furniture... Maple really wants it."

**market_merri_4**
> "Don't tell Miss Merri, but I once kept my pet termites in one of her dressers and it went... bad. Actually, don't tell Ma either..."

### Stillwell's Stall

Source: `market_stillwell_1.c.toml` through `market_stillwell_4.c.toml` | all require luc_activity = visit_stillwell_stall | all priority: max, refresh: 1y | source: NAR-774 through NAR-777

**market_stillwell_1**
> "I asked Mister Stillwell for a fortune about my new mayfly, and he started crying... but fortune-telling isn't very scientific... right?"

**market_stillwell_2**
> "I got a love fortune for my praying mantis... it was bad, which is good... I don't want her to eat her mate."

**market_stillwell_3**
> "Whenever I ask Mister Stillwell for a life fortune for one of my insects, he starts blubbering and stuff... maybe I should stop asking..."

**market_stillwell_4**
> "Maple always asks Mister Stillwell for a life fortune... she always manages to make them about becoming a princess."

### Taliferro's Stall

Source: `market_taliferro.c.toml` | all require luc_activity = visit_taliferro_stall | all priority: max, refresh: 1y

**market_taliferro_1** | portrait: think
> "If Miss Merri sells furniture, and Mister Louis sells clothing, and Miss Darcy sells coffee..."
> (next) portrait: neutral — "What does Mister Taliferro sell?"
> (next) portrait: mad — "Because if it's bad manners, I can find those from Dell for free!"

**market_taliferro_2** | portrait: sad
> "Mister Taliferro refused to make a dessert for my bee friend..."
> (next) portrait: happy, effect: cheery — "But that's okay! I gave her a flower and she seemed happy about it. She did a little dance and everything!"

**market_taliferro_3** | portrait: neutral
> "Mister Taliferro didn't want to make a mealworm souffle for my spider... I understand. I don't want to do it either."
> (next) portrait: happy — "And anyway, she's already really good at preparing it for herself!"

**market_taliferro_4** | portrait: think
> "If Mister Taliferro was an insect... maybe he'd be a $Cicada$!"
> (next) portrait: happy — "He's pretty and shiny, and yells a lot!"

### Vera's Stall

Source: `market_vera_1.c.toml` through `market_vera_4.c.toml` | all require luc_activity = visit_vera_stall | all priority: max, refresh: 1y | portrait: neutral or think

**market_vera_1** (source: NAR-781)
> "I told Miss Vera that some dyes are made from insects! She said she doesn't use that kind, though."

**market_vera_2** (source: NAR-782) | portrait: neutral
> "Some insects are attracted to bright colors..."
> (next) portrait: think — "Do you think bright hair would make bug catching easier?"

**market_vera_3** (source: NAR-783) | portrait: think
> "I guess I might dye my hair if it made insects think I was a flower... it would be easier to see them up close, don't you think?"

**market_vera_4** (source: NAR-1111) | portrait: think
> "Some insects can see more colors than the human eye! I wonder if Vera can dye my hair a color only pollinators can see..."

### Wheedle's Stall

Source: `market_wheedle_1.c.toml` through `market_wheedle_4.c.toml` | all require luc_activity = visit_wheedle_stall | all priority: max, refresh: 1y

**market_wheedle_1** | portrait: think
> "I asked Mister Wheedle if he makes his $Snake Oil$ by extracting oil from snakes. He said he'd never hurt a hair on a snake's head."
> (next) portrait: sad — "But [Ari]! Snakes don't have hair!"

**market_wheedle_2** | portrait: neutral
> "Mister Wheedle tried to sell me something called Bee Oil!"
> (next) portrait: sad — "When I told him that beeswax is solid at room temperature, he changed the subject..."

**market_wheedle_3** | portrait: neutral
> "Maple doesn't trust Mister Wheedle, but I don't know, he kind of reminds me of a clown!"
> (next) portrait: happy — "Maybe she'd like him more if he learned how to make balloon animals?"
> (next) portrait: think — "I bet he'd sell them for way more than my allowance, though..."

**market_wheedle_4** | portrait: happy
> "Mister Wheedle's always rubbing his hands together like a little praying mantis, or maybe a fly."
> (next) portrait: think — "He didn't seem very happy when I told him that, though..."

### Zorel's Stall

Source: `market_zorel_1.c.toml` | require luc_activity = visit_zorel_stall | priority: max, refresh: 1y

**market_zorel_1** | portrait: neutral
> "Did you know Zorel is friends with my Mom and Dad?"
> (next) portrait: happy — "They met back when my Dad was in a band!"

---

## Museum Lines

Source: `Conversations/Bank/Luc/Museum Lines/` (22 files)

All museum lines require the relevant item to have been donated (`museum_donated_<item> = true`) and that the player is NOT currently in the museum (`building = "museum", comparator = "!="`). All refresh: 1y.

### amber_trapped_insect.c.toml (source: NAR-183)

> "The =Amber Trapped Insect= in the Museum's collection is fascinating, [Ari]."
> (next) portrait: happy — "I see so many similarities to the insects of today!"

### bumblebee.c.toml

portrait: neutral
> "I saw the =Bumble Bee= at the Museum! They're so round and fluffy!"
> (next) portrait: mad — "Bee fact! People think they're called bumble bees because they're bumbling, but that's not true at all! It's because their genus is Bombus!"
> (next) portrait: happy — "Bombus means to buzz! So they're more like buzzing bees! Buzzz~!"

### cave_shrimp.c.toml

> "Mister Errol said you caught the =Cave Shrimp= at the Museum! Did you know that shrimps aren't insects? They're crustaceans! But I think they're cute anyway."

### copper_nugget_beetle.c.toml

> "I was so excited when I saw the =Copper Nugget Beetle= at the Museum, [Ari]! I'm not allowed in the Mines, so it was my first time seeing one!"
> (next) portrait: happy, effect: sparkles — "It's true... they do look like copper nuggets!"

### crystal_caterpillar.c.toml (source: NAR-230)

> "The shiny parts of a $Crystal Caterpillar$ are actually a defense mechanism! They're super sticky and break off easily."
> (next) portrait: happy, effect: drop — "Predators think that's gross, so they leave them alone! That wouldn't work on Dell, though."
> (next) portrait: think — "It's lucky that Dell is a friend to all caterpillars."

### fairy_bee.c.toml (source: NAR-214)

> "[Ari], I could NOT believe my eyes when I was at the Museum. A =Fairy Bee=! It's like a dream!"
> (next) portrait: think — "Juniper told me an old story about bad fairies cursed to be bees... but wouldn't it be the other way around?"
> (next) portrait: happy, effect: cheery — "I would LOVE to be a bee, personally."

### fire_wasp.c.toml

portrait: think
> "The $Fire Wasp$ is such a fascinating creature."
> (next) portrait: happy — "It has a really unique habitat, so I guess it would be hard to keep as a pet."
> (next) portrait: neutral — "I'll just have to keep visiting the one at the Museum!"

### flower_bee.c.toml

portrait: neutral
> "It's so cool to see a $Flower Bee$ at the Museum!"
> (next) portrait: happy — "Bee fact! You might think that bees are always yellow and black, but that's not true at all!"
> (next) portrait: wink — "Bees come in every color of the rainbow!"

### flower_crown_beetle.c.toml (source: NAR-227)

effect: cheery
> "Miss Celine was so excited to see the $Flower Crown Beetle$ at the Museum."
> (next) portrait: think — "I'm not sure why these beetles adorn themselves with little flowers. Camouflage, maybe?"
> (next) portrait: happy — "Miss Celine called it cute! Not a very scientific observation, but it is true."

### fur_bee.c.toml

portrait: neutral
> "There's now a $Fur Bee$ at the Museum. Please tell everyone to go visit it, [Ari]!"
> (next) portrait: wink — "I think they're the perfect ambassadors for all bee-kind! They're so cute and furry..."
> (next) portrait: happy, effect: cheery — "They're sure to make everyone a bee fan!"

### gem_shard_caterpillar.c.toml

portrait: neutral
> "The $Gem Shard Caterpillar$ at the Museum looks so unusual! I wonder what it looks like after it undergoes metamorphosis."

### jewel_beetle.c.toml (source: NAR-228)

portrait: happy
> "Mister Balor didn't like insects much, until I showed him the $Jewel Beetle$ at the Museum!"
> (next) portrait: think — "It just goes to show, there's an insect out there for everyone."

### luna_moth.c.toml (source: NAR-225)

> "The $Luna Moth$ at the Museum is so green! Did you know that the Luna Moth doesn't actually eat?"
> (next) portrait: happy, effect: cheery — "It uses the energy it stored up when it was a caterpillar!"

### moonlight_bee.c.toml

portrait: neutral
> "Amazing, [Ari], you found a $Moonlight Bee$! They're very special."
> (next) portrait: happy — "Bee fact! Most bees are only awake during the day, but $Moonlight Bees$ are nocturnal!"
> (next) portrait: wink, effect: sparkles — "That's why their eyes are even larger than normal! All five of them!"

### puddle_spider.c.toml

> "The =Puddle Spider= at the Museum is a wonderful specimen, [Ari]. Did you get to see it hunt?"
> (next) portrait: think — "According to my insect handbook, they watch for ripples on the surface of a puddle. A very unique way of catching prey!"

### sea_scarab.c.toml

portrait: happy
> "Wow, I've never seen a =Sea Scarab= before the one at the Museum! I wonder why its carapace is that pretty blue color? Is it trying to impress someone?"
> (next) portrait: mad, effect: sparkles — "Well, I'm impressed."

### snowball_beetle.c.toml (source: NAR-172)

effect: shock
> "I saw the =Snowball Beetle= you donated to the Museum, [Ari]! Wow! How does it make such perfectly round snowballs?"
> (next) portrait: think — "That's the power of nature. Dell could take some notes, her snowballs are always lopsided."

### speedy_snail.c.toml (source: NAR-229)

portrait: mad, effect: sparkles
> "Up to now, it's always been hard to study the $Speedy Snail$. It's super rare, and it always runs away super fast!"
> (next) portrait: think — "Do you suppose the red shell makes it go faster?"

### strobe_firefly.c.toml (source: NAR-215)

> "You caught a =Strobe Firefly=, [Ari]! I saw it at the Museum!"
> (next) portrait: happy, effect: loud — "The range of colors it can glow! Fascinating!"
> (next) portrait: think — "Is it for hunting? Warding off predators? A mating ritual? This requires further research..."

### sweet_bee.c.toml

portrait: neutral
> "The Museum's $Sweet Bee$ is such a pretty color!"
> (next) portrait: wink — "Bee fact! Most bees are really pale when they're born, and their colors get brighter after they're a day old..."
> (next) portrait: happy — "But $Sweet Bees$ are always pale. It's like they're cute babies forever!"

### tiny_dinosaur_skeleton.c.toml (source: NAR-165)

portrait: happy
> "Errol showed me the $Tiny Dinosaur Skeleton$ in the Pre-History collection! It's really neat!"
> (next) portrait: mad, effect: sparkles — "Wouldn't it be fun to have a tiny dinosaur in REAL LIFE?"

### windleaf_butterfly.c.toml

portrait: neutral
> "Did you know? The $Windleaf Butterfly$ at the Museum looks like dry leaves to hide itself from predators."
> (next) portrait: happy — "That's called an adaptation!"

---

## Gift Lines

Source: `Conversations/Bank/Luc/Gift Lines/gift_lines.c.toml`

All entries have `kind = "gift"`.

### Specific Gift Reactions

**grilled_cheese** — refresh: 2w | requires: gift_desire = loved, gift_given = grilled_cheese | portrait: happy, effect: sparkles
> "A =Grilled Cheese= sandwich! Wow! This will go great with Reina's soup of the day!"

**frog** — requires: gift_desire = hated, gift_given = frog | portrait: ugh, effect: shock
> "A $Frog$? No! It will eat up my insect collection! Dell's the frog-liker, not me!"

### Generic Loved Gift Lines

**loved_gift_1** — requires: gift_desire = loved | portrait: happy, effect: sparkles
> "You're so cool, [Ari]! Thanks for sharing something this amazing with me!"

**loved_gift_insects_1** — refresh: 1w | requires: gift_desire = loved, gift is one of [amber_trapped_insect, bumblebee, copper_beetle, fairy_bee, jewel_beetle, rhinoceros_beetle, roly_poly, sea_scarab, strobe_firefly] | portrait: happy, effect: cheery
> "[Ari], wow! What a rare specimen! Is this really for me? I have to document it right away!"

**loved_gift_insects_2** — same requirements | portrait: happy, effect: sparkles
> "Look at this rare beauty! You see the colors here? And the shape of the antennae? So cute!"

**loved_gift_insects_3** — same requirements | portrait: happy, effect: hearts
> "Whooooa, I love it! Look at those little legs! Thank you very much, [Ari]!"

### Generic Liked Gift Lines

**liked_gift_1** — requires: gift_desire = liked | portrait: happy
> "Yay, this is great, [Ari]! I gotta show my sisters!"

**liked_gift_edible** — refresh: 1w | requires: gift_desire = liked, gift is one of [cheese, chocolate, hot_cocoa, jam_sandwich] | portrait: happy
> "A snack! Thanks [Ari], I'm gonna share this with the Dragonguard!"

**liked_gift_insects_1** — refresh: 1w | requires: gift_desire = liked, gift is one of [ant, butterfly, cave_shrimp, cricket, fuzzy_moth, hummingbird_hawk_moth, inchworm, mistmoth, monarch_butterfly, orchid_mantis, pond_skater, praying_mantis, puddle_spider, river_snail, snowball_beetle, worm] | portrait: neutral
> "What a cool bug! How did you know I'd like this, [Ari]? Thank you!"

**liked_gift_insects_2** — same requirements | portrait: neutral
> "A new friend for my collection! Thanks [Ari], I'm gonna give this guy a good home!"

**liked_gift_insects_3** — same requirements | portrait: neutral
> "Wow, thanks [Ari]! You're a natural at bug-catching!"

### Generic Neutral Gift Lines

**neutral_gift** — requires: gift_desire = neutral | portrait: neutral
> "Thank you!"

**neutral_gift_2** — requires: gift_desire = neutral | portrait: think
> "Oh, for me? Let me think... yes, I think I can find room for it."

### Generic Disliked Gift Line

**disliked_gift** — requires: gift_desire = disliked | portrait: sad
> "Aw... I was hoping you were going to give me something interesting..."

### Birthday Gift

**birthday_gift** — priority: max | requires: gift_desire = neutral/liked/loved, luc_birthday within 24h | portrait: neutral
> "Wow! A birthday present! For me!"
> (next) portrait: happy — "Thank you, [Ari]!"

Note: Source has an empty condition `{ }` in the requires array (possible placeholder or error).

---

## Festival Lines

Source: `Conversations/Festival Lines/Luc/` (4 files)

### animal_festival.c.toml

All priority: max, refresh: 3m.

**animal_festival_0** — requires: animal_festival_today = true | portrait: neutral
> "Next year there should be a very small animal bracket for bugs!"

**animal_festival_small_dnp** — requires: animal_festival_today = true, small_animal_place = 0 | portrait: think
> "I gotta talk to Olric about Rocky, I've never even thought about having a pet rock before."
> (next) portrait: happy — "I bet it would get along great with my insect friends!"

### harvest_festival.c.toml

**harvest_festival_0** — priority: max, refresh: 3m | requires: harvest_festival_date 1d after | portrait: neutral
> "Did you know there are some insects that only feed on one kind of plant or fruit?"
> (next) portrait: think — "Maybe one day there will be a special kind of bug that only likes $Queen Berries$..."

### shooting_star.c.toml

**shooting_star_reina_follow_up_luc** — priority: max, refresh: 3m | requires: shooting_star_date_status = reina_went, shooting_star_festival_date 2d after, reina_is_partner = false | portrait: think
> "How come you and Reina got to stay out late watching the stars?"
> (next) portrait: sad — "I wanted to stay up late, too."

### spring_festival.c.toml

**pollinators** — priority: max, refresh: 3m | requires: spring_festival_date 1d after | portrait: happy
> "A festival with so many flowers is sure to bring out all my favorite pollinators!"
> (next) portrait: neutral — "What's your favorite, [Ari]?"
> **Player choice:** "Uhh... bees?" (next .2) | "Don't make me choose!" (next .3)

Path 1:
> portrait: happy — "They're so cute when they fall asleep inside a flower!"

Path 2:
> portrait: happy — "Haha, I feel the same way! They're all amazing! Hooray for Spring!"

---

## Threads — Bee Facts

Source: `Conversations/Threads/Luc/bee_facts.c.toml`

A sequential thread with three installments. Uses `nd_thread_mutex` and `nd_thread_delay` to gate progression. Requires `luc_heart_level >= 3` to start.

### Installment 1

**luc_bee_facts_1** — refresh: 1y | requires: nd_thread_mutex = undefined, nd_thread_delay = false, luc_bee_facts_finished = false, luc_heart_level >= 3 | writes: nd_thread_mutex = luc_bee_facts_1 (expires 1w), nd_thread_delay = true (expires 1d)

> "[Ari]! I've enrolled you in my bee facts!"
> (next) portrait: think — "Did you know that bees have six legs and five eyes? It's true!"
> (next) portrait: wink — "They have two big eyes, and three tiny eyes in the middle of their forehead!"
> (next) portrait: happy — "Okay, bye!"

### Installment 2

**luc_bee_facts_2** — refresh: instantly | requires: nd_thread_mutex = luc_bee_facts_1, nd_thread_delay = false | writes: nd_thread_mutex = luc_bee_facts_2 (expires 1w), nd_thread_delay = true (expires 1d)

> "It's time for another bee fact, [Ari]!"
> (next) portrait: happy — "A queen bee can lay over three thousand eggs per day! Worker bees come from eggs fertilized by the queen."
> (next) "Drones come from unfertilized eggs! And that's the end of today's bee fact!"

### Installment 3

**luc_bee_facts_3** — refresh: instantly | requires: nd_thread_mutex = luc_bee_facts_2, nd_thread_delay = false | writes: nd_thread_mutex = undefined, nd_thread_delay = true (expires 1d), luc_bee_facts_finished = true, luc_bee_facts_day = true (expires 3d)

> "[Ari]! New bee fact alert! It's super cool!"
> (next) portrait: wink — "Dad said it was a \"real thinker\"! Here it is:"
> (next) portrait: happy — "Our entire ecosystem would collapse without pollinators like bees."
> (next) effect: sparkles — "Okay, bye!"

### Cross-Character Reactions (within bee_facts.c.toml)

**luc_bee_facts_reina** — speaker: Reina | refresh: never | requires: nd_thread_mutex = luc_bee_facts_1 | portrait: happy, effect: sparkles
> "Did Luc tell you his bee fact? He worked so hard on it!"

**luc_bee_facts_maple** — speaker: Maple | refresh: never | requires: nd_thread_mutex = luc_bee_facts_2 | portrait: think
> "I didn't care much about bees until Luc told me there was a queen."
> (next) portrait: happy — "Now they're my favorite!"

**luc_bee_facts_hemlock** — speaker: Hemlock | refresh: never | requires: luc_bee_facts_day = true | portrait: happy, effect: drop
> "Did you hear Luc's latest bee fact? Bit of a barnburner, that one."

---

## Source Absences

- No Group Conversations directory for Luc (unlike some other characters who have paired/trio group conversations as separate files)
- No Heart Event conversation files in this extraction (heart events may exist elsewhere in the source tree)
- The Banked Lines do not include any lines gated on specific heart levels (the bee facts thread is the only heart-gated content)
- No seasonal variant dialogue — lines are gated by weather or time of day but not by season specifically
- The spelling "Entymology" (market_louis_1) vs. "Entomology" (greeting_ari) is a discrepancy in the source, recorded without resolution

define nc = Character(None, kind=bubble, image="Newscaster", callback=speaker("Newscaster"), voice_tag="newscaster")
define top_right = Character(None, what_style="top_right_text", window_style="top_right_window", statement_name="say-top-right")

label ch5_after_passion:
    $ set_chapter_progress(5)
    stop music fadeout 2.0
    scene black with fade

    stop music

    scene black
    centered "Chapter [chapter_list[5]['title']]"

    
    scene bg apartment_coffee
    play music "music/City_Center.opus" volume 0.15 fadein 1.0 fadeout 2.0
    show nic preset_casual:
        y1_2
        x0_8
    show nate preset_casual reverse face_happy:
        y1_2
        x0_2
        reverse
    show wolfrick preset_casual face_smiling reverse:
        y1_2
        x0_5
        reverse
    with fade

    alt "Description: The scene fades in to show the coffee table and couch, with Nate, Wolfrick and Nic."

    "Nate and I are sitting on the couch watching the news, and Nic is finishing up breakfast on the seat nearby."

    "He cooked the three of us breakfast to show his appreciation for letting him stay with us."

    "While Nate and I have been eating it slowly here and there, Nic is in a hurry."

    "He has a meeting at an auto shop nearby for a job – one he apparently had to reschedule from the day before because of his situation."

    "Luckily for him, the owner of that auto shop is an old friend from the rebellion! He basically agreed immediately to hire him, and just needed to vet Nic’s skill level."

    "Nate has been cuddling with me and every time something he is interested in is mentioned on screen, he and I have been talking about it – with Nic giving input here and there."

    "Over the course of the news broadcast, there have been segments on the I-I population, local charity events and the typical conspiracy report regarding the former High Emperor King Rexford."

    show nic:
        move_to_y(10)
        pause 0.1
        parallel:
            walk_z_back(0.5)
        parallel:
            walk_out_left(3)
        parallel:
            pause 0.2
            move_to_y(6)

    "Nic finishes his food and takes his plate to the kitchen. After a few moments of washing sounds from the sink, I hear him moving toward the bathroom."

    show nic:
        y0_6
        alpha 0
    show wolfrick:
        flip_back()

    "I turn toward Nate."

    show wolfrick -reverse:
        no_reverse

    voice "voice/5-after_passion/001.opus"
    w "So… about Nic being here…"

    show nate face_concerned
    play ambient "audio/effects/shower.opus" volume 0.2

    "We hear the sound of the shower running."

    "Nate looks toward me, a worried expression cast across his beautiful face."

    voice "voice/5-after_passion/002.opus"
    na "I promise, Wolfrick, it’s only until he gets back on his fe–"

    voice "voice/5-after_passion/003.opus"
    w "I think he should stay with us until he wants to get his own place."

    show nate face_shocked

    "Nate’s face is a mix of shock and confusion."

    voice "voice/5-after_passion/004.opus"
    na "W-Wolfrick!? Are you… do you mean that?"

    show wolfrick at nod

    "I laugh and nod."

    show wolfrick at no_offset

    voice "voice/5-after_passion/005.opus"
    w "Of course I do!"

    voice "voice/5-after_passion/006.opus"
    w "Nic being here has helped us come to understand one another a bit more, and I think it’ll be good to have him around."

    voice "voice/5-after_passion/007.opus"
    w "Besides…"

    voice "voice/5-after_passion/008.opus"
    w "He’s your – no, {i}our{/i} family."

    show nate face_happy:
        hug_right()

    "Nate smiles wide and lets out a squeal, wrapping his arms around me and kissing me deeply."

    stop music fadeout 2.0
    show nate:
        no_offset
        pause 1.0
        function add_attributes(["face_shocked"])
    show wolfrick:
        pause 1.0
        function add_attributes(["face_shocked"])

    "The sound of a breaking news story pulls our lips apart in time for both of us to be shocked and amazed at the sight on the television."

    show nate face_shocked
    show wolfrick face_shocked

    voice "voice/5-after_passion/009.opus"
    nc "...and ... it was just announced ... that the High Emperor King President Lycanus is taking [player_name] to be his noble consort!"

    "A generic looking human male walks up next to Lycanus as he gives a speech that the newscaster talks over."

    voice "voice/5-after_passion/010.opus"
    nc "His Highness is also said to be signing into effect the initiatives that were previously vetoed by the council and is also attempting to de-seat the entire council ... within the next month!"

    voice "voice/5-after_passion/011.opus"
    nc "It really makes you think about whether humans are people, just like us."

    voice "voice/5-after_passion/012.opus"
    nc "...and now, to George for the latest developments on the story surrounding the conspiracy theories recently brought up in popular media."

    voice "voice/5-after_passion/013.opus"
    nc "Some members of the Bulls on Parade believe the sky is actually just a box enclosing us within a vault, and that there is some overseer sending in humans as an {i}experiment{/i}. George–"

    play music "music/City_Center.opus" volume 0.15 fadein 1.0 fadeout 2.0

    "We look away from the TV at one another."

    "Nate’s mouth is wide open. He’s definitely excited about the initiatives…"

    "{i}My{/i} mouth is wide open as well, as I recognize the human from the alleyway that I met yesterday morning walking next to my old friend Lycanus."

    voice "voice/5-after_passion/014.opus"
    show wolfrick face_smiling

    w "Well, I guess that situation worked itself out."

    voice "voice/5-after_passion/015.opus"
    show nate face_happy

    na "Yeah, I’ll say. Lycanus has a human lover!"

    voice "voice/5-after_passion/016.opus"
    w "That guy…"

    voice "voice/5-after_passion/017.opus"
    na "Hmm?"

    voice "voice/5-after_passion/018.opus"
    w "...nevermind. Hey, Nate? Do you want to go make \”de-seat the council\” picket signs with me?"

    voice "voice/5-after_passion/019.opus"
    na "Wolfrick… that is the most romantic thing anyone has ever asked me."

    show wolfrick:
        quick_nod(2)
    show nate:
        pause 0.1
        quick_nod(2)

    "We laugh."

    stop music fadeout 2.0
    play sound "audio/effects/door_bang.opus" volume 0.4

    show wolfrick face_shocked
    show nate face_shocked

    "Then there’s a banging knock coming from the door, along with some shouting."

    stop ambient

    "The shower turns off."

    "Nate turns the TV off as well."

    voice "voice/5-after_passion/020.opus"
    zwho "{size=15}...better come the {size=20}fuck{/size} out here right now, you dragon bitch!{/size}"

    voice "voice/5-after_passion/021.opus"
    zwho "{size=15}I don’t know who the fuck you think you are leaving me, but I promise you you won’t like what happens when I get in there!{/size}"

    show nic shirt_robe face_shocked:
        y0_6
        alpha 1
        zoom 0.5
        walk_in_left(3.5)
    show wolfrick face_concerned
    show nate face_concerned

    "Nate and I look toward one another, and then Nic comes out of the bathroom with panic on his face."

    show nic face_concerned:
        no_offset
        x0_35

    voice "voice/5-after_passion/022.opus"
    ni "He’s here! Zephyr… he found me!"

    show wolfrick:
        move_to_y(10)
    show nate:
        move_to_y(10)
    pause 1
    scene bg apartment_dining
    show nic reverse shirt_robe face_concerned:
        y1
        x0_6
        reverse
    show nate preset_casual reverse face_concerned:
        y1
        x0_45
        reverse
    show wolfrick preset_casual reverse face_concerned:
        y1
        x0_8
        reverse
    with dissolve

    "We stand to move toward the door."

    show nate:
        push_right()
        walk_to(2, steps=2)
    show nic:
        pause 0.3
        walk_to(4, steps=2)

    "Nate places a hand on Nic's shoulder and pulls him back a bit."

    show nate:
        reset_pos(2)
    show nic:
        reset_pos(4)
    show wolfrick:
        walk_to(9, steps=2)
        parallel:
            hug_right()
        parallel:
            pause 0.4
            function add_attributes(["face_angry"])

    "I move to the door to look through the peephole and am greeted with the sight of Zephyr's ugly muzzle."

    voice "voice/5-after_passion/023.opus"
    z "I know you're there, wolf-bitch. I heard you all walk up to the door and I can smell your furry ass."

    show wolfrick face_angry:
        reset_pos(9)
        shake()
        pause 0.2
        flip_back(["face_stern"])
        pause 0.2
        nod()

    "I shake my head in annoyance and give Nate a glance, nodding."

    show wolfrick face_stern -reverse:
        no_offset
        no_reverse
    show nate:
        nod()

    "He gives me a nod in return and looks toward Nic, who is in his bath towel and looks worried."

    show nate:
        no_offset
    show nic:
        pause 1.5
        slow_nod()

    "Nic looks back and forth to us both, and then takes a deep breath, steeling himself."

    show nic:
        no_offset
        nod()

    "He nods."

    show nic:
        no_offset
    show wolfrick:
        flip()
        pause 0.1
        hug_right()

    play sound ["<silence 0.2>", "audio/effects/door_open.opus"] volume 0.5
    "I swing open the door and mean mug him."

    show wolfrick reverse:
        no_offset
        reverse

    "He looks down at me and returns the favor."

    voice "voice/5-after_passion/024.opus"
    w "Zephyr."

    voice "voice/5-after_passion/025.opus"
    z "Wolfrick."

    voice "voice/5-after_passion/026.opus"
    w "Still an abusive alcoholic, I see."

    "I smell the booze on him."

    voice "voice/5-after_passion/027.opus"
    z "Still a pipsqueak, I see. I ain't even got a buzz."

    voice "voice/5-after_passion/027-01.opus"
    na "Watch what you say, Zephyr."

    voice "voice/5-after_passion/027-02.opus"
    na "You might be twenty percent bigger, but Wolfrick has taken down bigger {i}and{/i} better men."

    voice "voice/5-after_passion/027-03.opus"
    ni "...if you could even call yourself a man."

    show wolfrick at shake

    "I wave a hand to silence them, letting them know I have the situation under control."

    show wolfrick at no_offset
    voice "voice/5-after_passion/028.opus"
    w "Nic can't talk right now, you need to leave."

    "He grimaces harder, if such a thing were possible."

    voice "voice/5-after_passion/029.opus"
    z "I can see him {i}right there{/i}. Send him out, punk!"

    "I scoff, mocking him with a dumb sounding voice."

    voice "voice/5-after_passion/030.opus"
    w "That's not gonna happen, {i}punk{/i}!"

    show nate:
        walk_to(7, 2.0)
        pause 0.1
        push_right()

    "Nate places a hand on my shoulder."

    show nate:
        reset_pos(7)
        hug_right()

    "He whispers in my ear."

    show nate:
        no_offset

    voice "voice/5-after_passion/031.opus"
    na "We should let him fight this fight, we'll be here for support."

    show wolfrick face_concerned
    voice "voice/5-after_passion/032.opus"
    w "What? No, I…"

    show wolfrick face_stern

    "I remember our talk. He's right, I take charge all the time."

    "This isn't my cause."

    "It's Nic's, and I should support him with it and not take the reins."

    show wolfrick:
        nod()
        walk_to(5.5)
    show nate:
        pause 0.2
        walk_to(4)
    show nic:
        pause 0.2
        walk_to(2)

    "I nod, and back up to let Zephyr in."

    show wolfrick:
        reset_pos(5.5)
        pause 2
        walk_to(7.5, 1, 2)
        flip_back()
    show nate:
        reset_pos(4)
        pause 2
        walk_to(9.5, 1, 2)
        pause 0.1
        flip_back()
    show nic:
        reset_pos(2)
        pause 2
        walk_to(1.5, 0.5, 1)
    show zephyr preset_casual:
        y1
        walk_in_right(8, 2)
        walk_to(4.5, 1, 2)

    "He cautiously enters, his eyes on mine the whole way, and walks up to Nic aggressively."

    alt "Description: Zephyr enters from the right. He is taller than everyone else by a full head, towering above the others. He wears a dark purple tanktop and dark pink jogging pants."

    show zephyr:
        reset_pos(4.5)
    show wolfrick -reverse:
        reset_pos(7.5)
        no_reverse
    show nate -reverse:
        reset_pos(9.5)
        no_reverse
    show nic:
        reset_pos(1.5)

    voice "voice/5-after_passion/033.opus"
    z "So, you decided to hide here, huh?"

    voice "voice/5-after_passion/034.opus"
    ni "I’m {i}not{/i} hiding."

    voice "voice/5-after_passion/035.opus"
    ni "I’m staying with them because the person who was {i}supposed{/i} to be my partner betrayed me."

    show zephyr face_angry at quick_shake

    "Zephyr is immediately angry and growls at Nic."

    show zephyr face_neutral
    voice "voice/5-after_passion/036.opus"
    z "I already {i}told you,{/i} I was doing that for you!"

    show nic face_angry at quick_nod

    "Nic is fed up. He scoffs."

    voice "voice/5-after_passion/037.opus"
    ni "How exactly does {i}you{/i} getting your {b}dick{/b} wet help {i}me{/i}?!"

    show zephyr face_sad

    "Zephyr stops and looks away."

    voice "voice/5-after_passion/038.opus"
    z "You have to believe me, I swear it wasn’t what it seemed."

    voice "voice/5-after_passion/039.opus"
    z "There were people who wanted to take you from me, so I made a deal to protect you."

    show nic at quick_nod

    "Nic scoffs again."

    voice "voice/5-after_passion/040.opus"
    ni "Honestly? {i}Good{/i}! Let them take me!"

    voice "voice/5-after_passion/041.opus"
    ni "I’d rather be with stupid mafia kidnappers than your abusive, matted-fur ass a second longer!"

    show wolfrick:
        walk_to(7, 0.5, 1)
    show nate:
        pause 0.2
        walk_to(9, 0.5, 1)

    "Not quite sure where all of the bark is coming from on Nic, Nate and I redouble our defensive placement."

    show wolfrick:
        reset_pos(7)
    show nate:
        reset_pos(9)

    "Don’t want to let Zephyr get an easy swing in if things get violent."

    "Nic seems ready for this, though."

    show zephyr face_neutral
    voice "voice/5-after_passion/042.opus"
    z "I didn’t go through all this shit just to have you {i}leave me{/i} like a punk ass bitch!"

    voice "voice/5-after_passion/043.opus"
    z "You’re {i}mine{/i}, Dominic."

    voice "voice/5-after_passion/044.opus"
    z "{b}Mine.{/b}"

    show nic:
        pause 0.2
        function add_attributes(["face_sad"])
        shake()
        pause 0.5
        function add_attributes(["face_neutral"])

    "Nic looks to waver for a moment, but looks at me and Nate and smiles."

    show nic face_angry:
        no_offset

    voice "voice/5-after_passion/045.opus"
    ni "Zephyr…"

    show nic:
        walk_to(2, 0.5, 1)

    "Nic moves closer to Zephyr, his voice calmer."

    show nic:
        reset_pos(2)
    show zephyr:
        move_to_y(14)

    "Zephyr takes Nic’s hands and gets on his knees."

    show zephyr face_sad:
        y1_4
    play music "music/June.opus" volume 0.1 fadein 1.0 fadeout 2.0

    voice "voice/5-after_passion/046.opus"
    z "I know I’m aggressive, and get angry sometimes, and I’m stronger than you – but I’d never hurt ya."

    show nic face_neutral

    "Nic’s face softens, and it looks like his plea is working."

    voice "voice/5-after_passion/047.opus"
    z "You just need to follow my lead, baby–"

    voice "voice/5-after_passion/048.opus"
    z "--let your big, bad wolf give ya the world."

    voice "voice/5-after_passion/049.opus"
    z "Let me protect you from everything, let me show you how much I love ya."

    voice "voice/5-after_passion/050.opus"
    z "I didn’t sleep with that shithead for nothin, baby!"

    voice "voice/5-after_passion/051.opus"
    z "I wouldn’t hurt you like that, I {i}had{/i} to do it."

    voice "voice/5-after_passion/052.opus"
    z "Nic, baby. I’m your wolf."

    voice "voice/5-after_passion/053.opus"
    z "I’m the only one for you!"

    voice "voice/5-after_passion/054.opus"
    z "You know me."

    voice "voice/5-after_passion/055.opus"
    ni "You know, that might have been enough for me before."

    voice "voice/5-after_passion/056.opus"
    ni "I used to just let you walk all over me and get away with shady shit."

    "Nic’s voice is deadly calm, his words seem to be chosen carefully."

    voice "voice/5-after_passion/057.opus"
    ni "It was never easy. I tried every day to be the same person I always was–"

    show nic face_angry

    "His gaze hardens a bit."

    voice "voice/5-after_passion/058.opus"
    ni "--even in spite of all of the shit I knew you’d done. Things your crew made you do, or you wanted to do, it doesn’t matter."

    voice "voice/5-after_passion/059.opus"
    ni "When you love someone, you put the best parts of yourself forward for them. When you can bring out the best in others, and they show it…"

    show nic face_neutral

    "Nic smiles at Nate and I again."

    voice "voice/5-after_passion/060.opus"
    ni "...and when they can do the same for you – you become something worth so much to one another."

    voice "voice/5-after_passion/061.opus"
    ni "You become family. That’s {i}real{/i} care, {i}real{/i} love."

    voice "voice/5-after_passion/062.opus"
    ni "Someone like you who only brings out the worst in others."

    show nic face_angry at quick_nod

    "Nic scoffs, looking Zephyr up and down."

    voice "voice/5-after_passion/063.opus"
    ni "You have no worth. Not to anybody."

    voice "voice/5-after_passion/064.opus"
    ni "Nothing will ever be good enough for you. You don’t deserve me."

    voice "voice/5-after_passion/065.opus"
    ni "Now prove to me you have even a {i}shred{/i} of dignity and give me our ATM card!"

    voice "voice/5-after_passion/066.opus"
    ni "I’m taking my money, and then you and I will never meet again."

    voice "voice/5-after_passion/067.opus"
    ni "I’m done supporting a criminal."

    voice "voice/5-after_passion/068.opus"
    z "B-but, baby!"

    show nic at shake

    "Nic shakes his head and holds out his hand."

    voice "voice/5-after_passion/069.opus"
    ni "Hand it over."

    show zephyr at quick_shake
    show nate face_neutral

    "Zephyr is…quivering?"

    "Tears are forming in his eyes, but he produces his wallet and takes the ATM card out of it."

    voice "voice/5-after_passion/070.opus"
    z "H-here. It’s yours."

    show nic face_neutral at nod

    "Nic smirks over Zephyr confidently and takes the card."

    "Somehow, he’s come out on top."

    voice "voice/5-after_passion/071.opus"
    ni "Now, there’s the door. {i}Please{/i} let it hit you on the way out."

    show zephyr:
        move_to_y(10)
        flip()
        walk_out_right()

    "With that, Zephyr scrambles to his feet and rushes out the door."

    hide zephyr
    show nate:
        walk_to(5)

    "Nic turns to us and smiles."

    show nate:
        reset_pos(5)

    voice "voice/5-after_passion/072.opus"
    ni "So, how’d I do?"

    stop music fadeout 2.0
    play music "music/Guardian Angel3.opus" volume 0.1 fadein 1.0 fadeout 2.0
    show nate face_happy:
        hug_left()

    "Nate is upon him in a flash, hugging him."

    show nate:
        no_offset
    show wolfrick face_smiling

    "I move to join them both."

    voice "voice/5-after_passion/073.opus"
    na "Nic, that was amazing!"

    voice "voice/5-after_passion/074.opus"
    na "You didn’t let him get to you and stood your ground."

    voice "voice/5-after_passion/075.opus"
    w "Yeah, I’m impressed! W-was that scary? Are you alright?"

    show nic at shake

    "Nic thinks for a moment and then shrugs."

    voice "voice/5-after_passion/076.opus"
    ni "Hmm… nah! At first I was scared, yeah. But then I realized I’m better off."

    voice "voice/5-after_passion/077.opus"
    ni "Oh! Anyway, I’ve gotta finish getting ready~"

    show nic:
        walk_out_right(1.6)

    "With that, he’s back into the bathroom."

    hide nic
    show nate:
        flip()

    "Nate and I look at one another."

    show nate reverse:
        reverse

    voice "voice/5-after_passion/078.opus"
    na "Talk about whiplash."

    voice "voice/5-after_passion/079.opus"
    w "Yeah…"

    show nate:
        flip_back(["face_sad"])

    "Nate looks to the side, sullenly."

    show nate face_sad -reverse:
        no_reverse
    show wolfrick face_stern

    "He probably feels guilty for something he shouldn't."

    "Having Zephyr come into the apartment, having Nic move in which brought Zephyr here…"

    "Nate beats himself up over things like that sometimes, but I don't know that that's what is wrong."

    "I decide to ask  and hear him out before jumping to conclusions."

    show wolfrick:
        hug_left()

    "I step closer to him."

    show wolfrick:
        no_offset

    voice "voice/5-after_passion/080.opus"
    w "Nate?"

    voice "voice/5-after_passion/081.opus"
    na "Yes, Wolfrick?"

    voice "voice/5-after_passion/082.opus"
    w "What's the matter?"

    show nate:
        flip()

    voice "voice/5-after_passion/083.opus"
    na "Are we going to… be okay?"

    show nate reverse:
        reverse

    "Oh. That's what he's worried about."

    voice "voice/5-after_passion/084.opus"
    na "I don't ever want to fight with you like what just happened here."

    show wolfrick face_smiling

    voice "voice/5-after_passion/085.opus"
    w "We'll be okay, Nate."

    "We have one thing going for us that Zephyr couldn't figure out."

    voice "voice/5-after_passion/086.opus"
    w "You're {i}more{/i} than enough for me."

    show nate face_happy

    "That one thing makes all the difference."

    show wolfrick at hug_left
    show nate at hug_right

    "I pull my manatee in close, and embrace him."

    show wolfrick at no_offset
    show nate at no_offset

    "No, not my manatee. My Nate."

    "I'm realizing more and more that I don't need to be the {i}wolf{/i} of his dreams."

    voice "voice/5-after_passion/087.opus"
    w "Nate, I'm here. Your husband is here."

    show wolfrick at hug_left

    "Nate gently hums and I nuzzle him gently."

    show wolfrick at no_offset

    voice "voice/5-after_passion/088.opus"
    na "Mmm… My husband~"

    stop music fadeout 2.0

    scene cg end with dissolve

    alt "Description: The scene fades to a drawing of Wolfrick, Nate and Nic standing together, Nic grinning while ruffling the other two's head."

    top_right "The End."

    scene black with fade

    centered "Thank you for playing!"

    scene black with fade

    $ set_chapter_progress(6)

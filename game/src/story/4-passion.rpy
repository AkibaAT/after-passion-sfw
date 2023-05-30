label ch4_passion:

    stop music

    scene black
    centered "Chapter [chapter_list[4][title]]"

    scene bg apartment_bedroom_main
    show nate reverse pants_chill face_sleeping:
        reset_pos(8.5, 4)
        reverse
    show wolfrick accessories_watch pants_joggers face_sad eyes_sad_closed:
        reset_pos(5, 4)
    with fade

    "Nate and I are lying in bed, about a foot apart."

    "It's been about two and a half hours since we both helped Nic to bed."

    "Nate wiped the puke from his face with a washcloth, then I carried him to his bedroom."

    "Nic didn't fuss much, and in his state he fell asleep pretty quickly."

    "Nate and I left his door cracked open a bit as well as our own just in case he ended up needing us."

    "..."

    "I want everything to go back to normal."

    "Nate got in bed and immediately turned away from me."

    "I thought our talk would have helped, but this is the same thing he's been doing for a few months now."

    "I miss him. He's so close, yet so far."

    "It might be a bit selfish, but I haven't gotten a really good night's sleep in so long."

    "I want to pull him in close, just hold him tight."

    "I know it will take time, but I need to feel him against me."

    "…"

    play sound "audio/effects/shuffling.opus" volume 0.1
    "I hear something outside the room, and listen carefully."

    show wolfrick -eyes_sad_closed

    play ambient "audio/effects/crying.opus" volume 0.8
    play sound "audio/effects/shuffling.opus" volume 0.2
    "A sniffle, and some shuffling."

    stop ambient
    play sound "audio/effects/slide_door_open.opus" volume 3
    "The sound of the balcony door sliding open."

    show wolfrick:
        flip()

    voice "voice/4-passion/001.opus"
    w "Nate…"

    show wolfrick reverse:
        reverse
    show nate:
        shake()
        pause 0.1
        flip_back(["face_neutral", "eyes_half"])
    play sound "<to 2>audio/effects/shuffling_cloth.opus" volume 0.8 fadeout 0.5

    "He stirs in his sleep and turns toward me."

    "Thankfully, he's a light sleeper."

    voice "voice/4-passion/002.opus"
    na "Hmm? What happened?"

    voice "voice/4-passion/003.opus"
    w "I think Nic is up. I heard sniffling."

    play sound ["<silence 0.8>", "<to 2>audio/effects/shuffling_cloth.opus"] volume 1.3 fadeout 0.5
    show nate -reverse:
        no_offset
        no_reverse()
        slow_nod()
        pause 0.5
        parallel:
            shake()
        parallel:
            pause 0.2
            function add_attributes(["shirt_chill"])
            pause 0.3
            function add_attributes(["accessories_glasses"])
        move_to_y(10)

    "He sighs and gets up from bed."

    show nate preset_super_casual:
        y1
        no_offset

    voice "voice/4-passion/004.opus"
    na "Well, I should go check on him."

    play sound "<to 2>audio/effects/shuffling_cloth.opus" volume 1.3 fadeout 0.5
    show wolfrick face_stern:
        parallel:
            shake()
        parallel:
            pause 0.2
            function add_attributes(["shirt_joggers"])
            pause 0.3
            function add_attributes(["accessories_glasses"])
        move_to_y(10)

    "I turn to get out of bed myself."

    show wolfrick preset_casual:
        y1
        no_offset

    voice "voice/4-passion/005.opus"
    na "You're coming with?"

    show wolfrick:
        nod()
    voice "voice/4-passion/006.opus"
    w "Of course, it's your cousin!"

    show wolfrick at no_offset
    show nate:
        flip(["face_happy"])

    "He looks away, and smiles."

    show wolfrick face_smiling
    show nate reverse:
        reverse
        flip_back(["face_neutral"])

    voice "voice/4-passion/007.opus"
    na "That’s so… sweet."

    voice "voice/4-passion/008.opus"
    na "You meant it when you said \"we\" were taking care of him, huh?"

    show wolfrick:
        nod()

    "I nod and put my hands on his shoulder, locking eyes with him."

    show wolfrick at no_offset

    voice "voice/4-passion/009.opus"
    w "Yes, I do."

    voice "voice/4-passion/010.opus"
    w "This is important to you, and that means it's important to me."

    voice "voice/4-passion/011.opus"
    na "Wolfrick, you don't need to worry about my causes…"

    show wolfrick:
        slow_nod()
        pause 0.5
        parallel:
            hug_right()
        parallel:
            pause 0.1
            function add_attributes(["face_smiling"])

    "I sigh and caress his cheek."

    show wolfrick face_smiling at no_offset

    voice "voice/4-passion/012.opus"
    w "Even if it's {i}your{/i} cause, I want to help because I care about you!"

    voice "voice/4-passion/013.opus"
    w "There's nothing I'd rather do than support you, even in the middle of the night!"

    voice "voice/4-passion/014.opus"
    w "...and I won't be able to sleep without you anyway."

    show wolfrick:
        hug_right()
    show nate face_happy:
        hug_left()

    "He smiles, and holds my hand against his cheek."

    show wolfrick:
        no_offset
        pause 0.5
        parallel:
            walk_z_front()
        parallel:
            fade_out()
    show nate:
        no_offset
        nod()
        parallel:
            walk_z_front()
        parallel:
            fade_out()

    "He nods to me and we walk off to find Nic."

    scene bg apartment_balcony_night
    show nic reverse shirt_robe face_sad:
        y1
        x0_5
        reverse
    with dissolve
    play sound "audio/effects/slide_door_open.opus" volume 5
    show nate preset_super_casual reverse:
        y1
        x1_3
        pause 0.1
        walk_in_right(7.5, 1.5)
    show wolfrick preset_casual face_stern reverse:
        y1
        x1_3
        pause 0.5
        walk_in_right(9.5)

    "We find him on the balcony, wrapped in a bathrobe and eyes wet with tears."

    show nate:
        reset_pos(7.5)
    show wolfrick:
        reset_pos(9.5)

    voice "voice/4-passion/015.opus"
    na "Nic, sweetie~ oh, no."

    show nate:
        hug_left()

    "Nate moves to hug Nic."

    show nate at no_offset
    show wolfrick:
        walk_to(2.5)
        flip()

    "I move to the other side of him and rub his shoulder to soothe him."

    show wolfrick reverse:
        reverse
        reset_pos(2.5)

    voice "voice/4-passion/016.opus"
    ni "Why is it so hard for him to just love me?!"

    "His voice is shaky and strained."

    "He doesn't sound drunk anymore, but now…"

    voice "voice/4-passion/017.opus"
    ni "I did everything and {i}gave{/i} everything I could for him!"

    voice "voice/4-passion/018.opus"
    ni "You would think it would be enough for {i}anybody{/i}, but with him {i}nothing{/i} will {i}{b}ever{/b}{/i} be enough!"

    "Nic sobs onto Nate's shoulder."

    "A moment passes and it seems like Nate can't think of something to say."

    show wolfrick at push_right

    "I decide to give him a nudge."

    show wolfrick at no_offset

    voice "voice/4-passion/019.opus"
    w "Zephyr brings out the worst in {i}everybody{/i}."

    voice "voice/4-passion/020.opus"
    na "Wolfri–"

    show nate face_shocked

    "I hold my hand up for Nate to wait, and when our eyes meet, I make a pleading expression."

    show nate face_concerned

    "I need to say what I have to say."

    show nate at nod

    "Nate nods and turns his attention back to Nic."

    show nate at no_offset

    voice "voice/4-passion/021.opus"
    ni "Don't I know it…"

    show wolfrick face_smiling
    voice "voice/4-passion/022.opus"
    w "But not you, Nic. Not you, ever."

    voice "voice/4-passion/023.opus"
    ni "Wha–"

    "He gasps and I see his eyes move to meet mine."

    "His tears break free from his eyelids and drip onto Nate's shoulder."

    voice "voice/4-passion/024.opus"
    w "I mean it, you really were always a bright, happy ray of sunshine any time we ever saw you two together."

    voice "voice/4-passion/025.opus"
    w "If there's one thing I know about you, it's that you never let others get you down."

    voice "voice/4-passion/026.opus"
    w "That's the thing I always think about whenever Nate brings you up. It's inspiring, really."

    "Nate looks to me as Nic seems to be processing and thinking about what my meaning might be."

    show nate face_neutral at nod

    "Nate nods as he seems to catch on."

    show nate at no_offset

    "I used a similar speech when we overthrew former High King Emperor Rexford, this one is just turned around to be positive."

    show wolfrick at nod

    "I nod to Nate for him to take the reins."

    show nate face_happy
    show wolfrick at no_offset

    "He smiles at me."

    voice "voice/4-passion/027.opus"
    na "Yeah, Nic. He's right."

    voice "voice/4-passion/028.opus"
    na "After everything he's done, and after all of the things he put you through, you stayed positive and joyful!"

    voice "voice/4-passion/029.opus"
    na "That's something I always think about."

    voice "voice/4-passion/030.opus"
    na "Whenever I'm having a bad day, or whenever someone hurts me, I remember how positive your outlook on everything is!"

    voice "voice/4-passion/031.opus"
    na "Nic."

    "Nic wipes his tears and looks at Nate."

    voice "voice/4-passion/032.opus"
    ni "Y-yes?"

    voice "voice/4-passion/033.opus"
    na "The best thing about you brings out the best in others {i}so often{/i} that it starts to become the best part in them–"

    show nate at hug_left

    "Nate hugs Nic."

    show nate at no_offset

    voice "voice/4-passion/034.opus"
    na "You're worth so much to so many people – us for example!"

    voice "voice/4-passion/035.opus"
    na "You're more than enough for Wolfrick and me."

    voice "voice/4-passion/036.opus"
    na "If you aren't enough for him, then he doesn't deserve you!"

    show nic at nod

    "Nic is sniffling but he nods."

    show nic at no_offset

    voice "voice/4-passion/037.opus"
    show nic face_neutral

    ni "Thank you, both of you."

    show nic face_sad:
        pause 2.5
        walk_out_right(1.4)
    show nate:
        pause 2
        flip()
        walk_out_right()
    show wolfrick:
        pause 2.5
        walk_out_right(1.5)
    play sound ["<silence 2.5>", "audio/effects/slide_door_open.opus"] volume 5

    "We stay on the balcony with him for a while and eventually, we move inside."

    scene black with fade

    "Nic gets ready to sleep again, putting on a chunky pair of headphones and plugging it into his walkman."

    "I told him he could borrow any of my CDs."

    play sound '/effects/snore.opus' volume 0.05
    "Nate and I are holding hands as we head back to the room, and before long we hear Nic's snoring coming from the other room."

    scene bg apartment_bedroom_main
    show nate pants_chill face_happy:
        reset_pos(8.5, 4)
    show wolfrick accessories_watch pants_joggers face_smiling:
        reset_pos(5, 4)
        pause 1.5
        flip()
    with fade

    "I turn to Nate in bed."

    "He's lying facing me. He's a half-foot away."

    "I see it in his eyes again."

    "That look of passion that I've come to love."

    $ set_chapter_progress(5)

    scene black with fade

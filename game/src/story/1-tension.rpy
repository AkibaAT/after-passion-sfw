label ch1_tension:

    stop music

    scene black
    centered "Chapter [chapter_list[1][title]]"

    scene bg city_day_4
    play music "music/City_Center.opus" volume 0.4 fadein 1.0 fadeout 2.0
    play sound "effects/city_crowd.opus" volume 0.1 loop
    show wolfrick preset_work face_concerned:
        y1
        x1_3
        pause 0.1
        walk_to(5)
    with dissolve

    "I'm late."

    show wolfrick:
        reset_pos(5)
        walk_out_left

    "Nate is waiting for me."

    scene bg city_day_3
    show wolfrick preset_work face_concerned:
        y1
        x1_3
        pause 0.1
        walk_to(5)
    with dissolve

    "I promised I'd get there in time to spend my lunch hour with him, but I'm behind by ten minutes."

    show wolfrick:
        reset_pos(5)
        walk_out_left

    "Shit. What kind of husband am I?"

    scene bg city_day_2
    show wolfrick preset_work face_concerned:
        y1
        x1_3
        pause 0.1
        walk_to(5)
    with dissolve

    "What a way to kick off our anniversary."

    show wolfrick:
        reset_pos(5)
        walk_out_left

    "I should have finished the call with my last client earlier than I did."

    scene bg city_day_1
    show wolfrick preset_work face_concerned:
        y1
        x1_3
        pause 0.1
        walk_to(5)
    with dissolve

    "We just got carried away talking about current events, like usual."

    show wolfrick:
        reset_pos(5)
        walk_out_left

    "I only noticed the time after they had mentioned they would have to take a lunch break soon."

    scene bg city_day_3
    show wolfrick preset_work face_concerned:
        y1
        x1_3
        pause 0.1
        walk_to(5)
    with dissolve

    "So now here I am, trying to manage as fast a pace as a hulking, muscular, six-foot-four wolf can without causing some commotion."

    show wolfrick:
        reset_pos(5)
        walk_out_left

    "I get a full hour for lunch, which thankfully doesn't start until I punch my time card out for it, but… still."

    scene black with dissolve

    "I should have left sooner."

    scene bg flower_shop_outside
    show wolfrick preset_work face_shocked:
        y1
        walk_in_right()
        block:
            nod()
            repeat
    with dissolve

    "Panting, I finally reach the arched wooden door with stained glass panes embedded in the upper half-circle."

    show wolfrick:
        reset_pos(8)
        nod(speed=1)

    "The rest of the storefront is pretty run-of-the-mill, but this door immediately caught my eye."

    show wolfrick face_happy:
        no_offset

    "When I pointed it out to Nate, he fell in love with this place. Now, five years later, here we are."

    show wolfrick face_stern

    "The sign on the door says {i}'Open'{/i} so he might be with a customer."

    show wolfrick eyes_closed

    "Not wanting to embarrass Nate, I close my eyes and listen for anyone in the store."

    show wolfrick -eyes_closed

    "I don't hear anyone on the inside of the storeroom moving around or talking."


    "I know I'm in the clear - my wolf senses are pretty good for that."

    show wolfrick face_happy

    "I steady myself, tidy my fur and clothes, and put on a smile."

    show wolfrick:
        parallel:
            walk_z_back
        parallel:
            walk_to(6)
        parallel:
            move_to_y(8.5)
        parallel:
            pause 0.5
            fade_out()
            
    play sound "effects/door_open.opus" volume 0.5

    "It's go time."

    scene bg flower_shop_inside
    show wolfrick preset_work face_blushing :
        y1
        walk_in_right()
    with dissolve

    stop music fadeout 2.0
    voice "voice/1-tension/001.opus"
    w "Happy anniversary, my love!"

    show wolfrick face_happy

    "I swing the door of Nate's flower shop open, making sure not to open it too fast but still make an excitable entrance!"

    show wolfrick face_stern

    "..."

    show wolfrick

    voice "voice/1-tension/002.opus"
    w "...Nate?"

    show wolfrick face_concerned

    "There really {i}is{/i} nobody here."

    show wolfrick at walk_to

    "I figured maybe Nate was sitting at his workstation making an arrangement or something."

    show wolfrick at center

    "I've told him before that he's uncannily silent when he works, and he just tells me it's how he focuses."

    show wolfrick at flip

    "Looking around, I try to find any sign of where he might be."

    show wolfrick reverse:
        x0_5
        reverse
        pause 0.5
        walk_to(8.5)
        pause 0.5
        hug_right()

    play sound ["<silence 2.5>", "<from 0.4>effects/door_full.opus"] volume 0.5
    "I decide to lock the door and flip the sign over to {i}'Closed'{/i} just in case."

    show wolfrick:
        reset_pos(8.5)
        pause 0.1
        flip_back()
        pause 0.5
        walk_to(-2.5, 3.0)

    "I turn toward his back office and make my way there."

    hide wolfrick

    "Within, I hear what sounds like a droning voice that is either very small and quiet or, somehow, very distant."

    play sound "effects/door_open.opus" volume 0.5
    play music "music/Guardian Angel1.opus" volume 0.15 fadein 1.0 fadeout 2.0
    scene bg flower_shop_backoffice
    show nate preset_work reverse:
        y1
        x0_75
        reverse
    show wolfrick preset_work reverse face_happy-with-eyes:
        y1
        x0_2
        reverse
    with dissolve

    "I open the door quietly and enter, seeing my adorable manatee husband standing, turned away from the door with his arms crossed."

    show wolfrick face_smiling

    "Nate is staring at the small television up in the corner of the room."

    show wolfrick face_stern

    voice "voice/1-tension/003.opus"
    w "Hey, love. What's going on with this?"

    show nate face_happy at flip_back()
    show wolfrick face_stern:
        pause 0.8
        nod

    "He turns his head toward me with a smile and I motion up toward the television."

    show nate -reverse at no_reverse

    voice "voice/1-tension/004.opus"
    na "Hey, sweetheart."

    show nate face_concerned at slow_nod:
        pause 1
        shake

    "He sighs and shakes his head."

    show nate face_neutral at no_offset

    voice "voice/1-tension/005.opus"
    na "The council vetoed the new initiatives from the peoples' representatives."

    voice "voice/1-tension/006.opus"
    na "There seems to be no support from the High Emperor King President Lycanus, either."

    show wolfrick face_shocked
    show nate face_concerned
    voice "voice/1-tension/007.opus"
    w "New… initiatives?"

    voice "voice/1-tension/008.opus"
    na "Yes, I mentioned them before - remember?"

    show wolfrick face_embarrassed at shake

    "I don't. I shrug and he sighs again. I probably should listen to him better."

    voice "voice/1-tension/009.opus"
    na "Those initiatives the citizens' representatives were trying to propose?"

    voice "voice/1-tension/010.opus"
    na "The ones which were in effort of making the lower-end of the housing economy more affordable…?"

    show wolfrick face_stern

    voice "voice/1-tension/011.opus"
    na "They would also allow for easier citizenship to the people who have begun to join us in this world recently."

    "Oh, right. I {i}do{/i} remember now."

    show wolfrick face_shocked at nod

    "I mouth an 'oh' as best as a wolf muzzle can and nod."

    show wolfrick face_concerned at no_offset

    voice "voice/1-tension/012.opus"
    w "Shit, maybe I should have heard that beggar out more. He might have been an {i}isekai'd individual{/i}."

    show wolfrick face_stern

    voice "voice/1-tension/013.opus"
    w "Oh well, I'll just report him to the Isekai Bureau of Science."

    show nate face_shocked

    "Nate looks at me with scrutiny."

    show nate face_sad

    voice "voice/1-tension/014.opus"
    na "You met an {i}I-I{/i} and want to put him through dealing with the {i}IBS{/i}?"

    show wolfrick face_happy at quick_nod

    "I chuckle."

    voice "voice/1-tension/015.opus"
    w "That's never {i}not{/i} funny."

    show nate face_happy
    show wolfrick face_stern at no_offset

    "He grins, in spite of himself."

    show wolfrick at walk_to
    show nate face_neutral

    "I move over to hug him."

    show wolfrick face_happy:
        reset_pos(5)
        pause 0.1
        hug_right()
    show nate face_shocked at hug_left

    "He is hugged, in spite of himself."

    show nate face_sad at no_offset
    show wolfrick face_shocked at no_offset

    voice "voice/1-tension/016.opus"
    na "You know that's an important cause to me, Wolfrick!"

    show wolfrick face_sad

    "I do, and now I feel bad."

    "Generally, I agree that all of the men who have been appearing in our world recently need proper assistance."

    "The way the council has been treating them is horrendous - they all end up living together in buildings that are even more cramped than hostels."

    show wolfrick face_stern

    "Still, Nate doesn't seem to notice the things I have."

    show wolfrick face_concerned

    voice "voice/1-tension/017.opus"
    w "All of the {i}I-I{/i} that I've come across seem to have the same… {i}thirst{/i} in their eyes."

    voice "voice/1-tension/018.opus"
    w "I thought that guy I met earlier was homeless, but he turned out to be one of them."

    voice "voice/1-tension/019.opus"
    w "I don't know, Nate. They all seem to want something. How'd you like to see them all stealing your man, huh? I know {i}I{/i} wouldn't want them stealing {i}mine{/i}!"

    show nate face_concerned at quick_shake

    "Nate scoffs."

    show nate face_angry at no_offset
    show wolfrick face_concerned

    voice "voice/1-tension/020.opus"
    na "You're not serious, Wolfrick? I'm worried about where they're {i}living{/i}, not who they're {i}riding{/i}."

    show nate face_neutral

    voice "voice/1-tension/021.opus"
    na "Anyway…"

    show wolfrick face_sad:
        flip_back()
        pause 0.7
        flip()

    "I look around. Nate was supposed to have lunch here already, but there's nothing."

    show wolfrick reverse face_stern:
        reverse
    show nate face_concerned

    "Looking back to Nate, he's sheepishly scratching his neck, looking away."

    voice "voice/1-tension/022.opus"
    w "Hey, Nate?"

    "..."

    voice "voice/1-tension/023.opus"
    na "...Yes, Wolfrick?"

    "..."

    show wolfrick face_concerned

    voice "voice/1-tension/024.opus"
    w "...Where's lunch? I'm hungry and we only have about forty-five minutes before I have to head back."

    show nate face_shocked at slow_nod

    "Nate sighs and looks me in the eye."

    show nate face_neutral at no_offset

    voice "voice/1-tension/025.opus"
    na "Well… you see, I sort of… forgot."

    show wolfrick face_sad

    voice "voice/1-tension/026.opus"
    w "...Oh."

    show nate face_concerned

    voice "voice/1-tension/027.opus"
    na "I tried to call you to give you a heads-up but you didn't answer, so I left a message. My bad."

    show wolfrick face_blushing

    voice "voice/1-tension/028.opus"
    w "Oh? Huh. I'll listen to it when I get back, what a pleasant surprise!"

    show nate face_shocked

    "Nate gives me a puzzled look."

    show nate face_neutral

    voice "voice/1-tension/029.opus"
    na "What? A surprise?"

    show wolfrick face_happy at nod

    voice "voice/1-tension/030.opus"
    w "Yes, I get to hear your voice at work as much as I want!"

    show nate at quick_nod(3)
    show wolfrick at no_offset:
        pause 0.1
        quick_nod(3)

    "Nate rolls his eyes, laughing. I chuckle too."

    show nate at no_offset
    show wolfrick at no_offset

    voice "voice/1-tension/031.opus"
    na "You're cheesey. Sorry for forgetting."

    show wolfrick face_stern

    voice "voice/1-tension/032.opus"
    w "That's alright, love. We'll make up for it {i}later on tonight{/i}, if you catch my drift~"

    show nate face_happy

    "He is blushing now."

    show wolfrick face_happy
    show nate face_neutral

    voice "voice/1-tension/033.opus"
    na "Dick, right?"

    voice "voice/1-tension/034.opus"
    na "Is that the drift? Did I get it right?"

    "He definitely catches the drift."

    show wolfrick:
        nod(2)
        pause 0.2
        function add_attributes(["face_blushing"])
        hug_right()

    "I laugh and move in to kiss him."

    show wolfrick face_blushing at no_offset

    voice "voice/1-tension/035.opus"
    w "Yes, you did."

    voice "voice/1-tension/036.opus"
    na "Mmmm you're all musky. Did you run here?"

    voice "voice/1-tension/037.opus"
    w "I might have~"

    show nate at nod(2)
    show wolfrick face_embarrassed

    "Nate laughs and I tickle his mustache with a finger, looking down into his eyes."

    show nate at no_offset

    "He didn't want to grow the mustache out, because he said it made him look like his father."

    "He only did it because I loved it so much."

    show wolfrick face_stern

    voice "voice/1-tension/038.opus"
    na "Well, you should probably go grab lunch and get back to the office. I'll grab something quick in a bit, we can have a nice dinner tonight."

    show wolfrick face_happy at nod

    "I nod."

    show wolfrick face_stern at no_offset

    voice "voice/1-tension/039.opus"
    w "Right-O."

    show wolfrick face_blushing at hug_right

    "I lean in and smooch him some more."

    show wolfrick at no_offset

    voice "voice/1-tension/040.opus"
    na "Mmmmfgh-luvya-mfgfhhh."

    show wolfrick face_stern

    voice "voice/1-tension/041.opus"
    w "Mffghg-luvyamore-mffffgh."

    show wolfrick face_happy
    show nate face_happy at quick_nod(3)

    "We part with a chuckle from him and a wink from me."

    show wolfrick at no_offset

    "I pop the finger guns."

    show wolfrick face_stern

    voice "voice/1-tension/042.opus"
    w "Hasta la vista, baby."

    show wolfrick:
        flip_back
        pause 0.1
        walk_out_left(1.7)
    show nate:
        pause 0.7
        walk_out_left(1.9)

    "Nate rolls his eyes, and follows me out of the office."

    scene bg flower_shop_inside
    show nate preset_work reverse:
        reverse
        xpos -0.5
        y1
        walk_to(9, 2.0, 4)
    show wolfrick preset_work reverse:
        reverse
        xpos 0
        y1
        walk_to(12, 2.1)
    with dissolve

    play sound ["<silence 1.5>", "effects/slap_eco.opus"] volume 0.6

    "He walks me to the door and I feel a slap on my ass as I'm heading out the door."

    hide wolfrick
    show nate at x0_9:
        hug_right(0.7)

    play sound ["<silence 0.4>", "effects/door_close.opus"] volume 0.5

    "I turn to retaliate but he shuts the arched door behind me."

    show nate:
        walk_z_front
        hug_right(0.3)
        pause 0.5
        walk_z_center

    "I laugh and see him winking at me through the window next to it as the sign flips over to {i}Open{/i}."

    "He's gonna get it {i}good{/i} later."

    stop music fadeout 2.0
    scene black with fade

    $ set_chapter_progress(2)

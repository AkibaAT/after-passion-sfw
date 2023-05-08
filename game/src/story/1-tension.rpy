label ch1_tension:

    $ set_chapter_progress(1)

    stop music

    scene bg city_day
    show wolfrick accessories_watch accessories_glasses face_concerned pants_formal shirt_formal at y1, x1_3:
        pause 0.1
        walk_to(9)

    "I'm late."

    show wolfrick at x0_9:
        pause 0.1
        walk_to(8, 1, 1)

    "Nate is waiting for me."

    show wolfrick at x0_8:
        pause 0.1
        walk_to(7, 1, 1)

    "I promised I'd get there in time to spend my lunch hour with him, but I'm behind by ten minutes."

    show wolfrick at x0_7:
        pause 0.1
        walk_to(6, 1, 1)

    "Shit. What kind of husband am I?"

    show wolfrick at x0_6:
        pause 0.1
        walk_to(5, 1, 1)

    "What a way to kick off our anniversary."

    show wolfrick at x0_5:
        pause 0.1
        walk_to(4, 1, 1)

    "I should have finished the call with my last client earlier than I did."

    show wolfrick at x0_4:
        pause 0.1
        walk_to(3, 1, 1)

    "We just got carried away talking about current events, like usual."

    show wolfrick at x0_3:
        pause 0.1
        walk_to(2, 1, 1)

    "I only noticed the time after they had mentioned they would have to take a lunch break soon."

    show wolfrick at x0_2:
        pause 0.1
        walk_to(1, 1, 1)

    "So now here I am, trying to manage as fast a pace as a hulking, muscular, six-foot-four wolf can without causing some commotion."

    show wolfrick at x0_1:
        pause 0.1
        walk_to(0, 1, 1)

    "I get a full hour for lunch, which thankfully doesn't start until I punch my time card out for it, but… still."

    show wolfrick at x0:
        pause 0.1
        walk_out_left(1.5)

    "I should have left sooner."

    scene bg flower_shop_outside
    show wolfrick accessories_watch accessories_glasses pants_formal shirt_formal face_shocked at y1, walk_in_right()

    "Panting, I finally reach the arched wooden door with stained glass panes embedded in the upper half-circle."

    "The rest of the storefront is pretty run-of-the-mill, but this door immediately caught my eye."

    "When I pointed it out to Nate, he fell in love with this place. Now, five years later, here we are."

    "The sign on the door says {i}'Open'{/i} so he might be with a customer."

    "Not wanting to embarrass Nate, I close my eyes and listen for anyone in the store."

    "I don't hear anyone on the inside of the storeroom moving around or talking."

    "I know I'm in the clear – my wolf senses are pretty good for that."

    "I steady myself, tidy my fur and clothes, and put on a smile."

    "It's go time."

    play sound "effects/door_open.opus"

    scene bg flower_shop_inside
    show wolfrick face_blushing accessories_glasses accessories_watch pants_formal shirt_formal at y1
    show wolfrick at walk_in_right

    w "Happy anniversary, my love!"

    show wolfrick face_happy

    "I swing the door of Nate's flower shop open, making sure not to open it too fast but still make an excitable entrance!"

    show wolfrick face_neutral

    "..."

    show wolfrick

    w "...Nate?"

    show wolfrick face_concerned

    "There really {i}is{/i} nobody here."

    show wolfrick at walk_to

    "I figured maybe Nate was sitting at his workstation making an arrangement or something."

    show wolfrick at center

    "I've told him before that he's uncannily silent when he works, and he just tells me it's how he focuses."

    show wolfrick reverse at flip

    "Looking around, I try to find any sign of where he might be."

    show wolfrick at x0_5:
        pause 0.5
        walk_to(8)
        pause 0.5
        hug_right

    "I decide to lock the door and flip the sign over to {i}'Closed'{/i} just in case."

    show wolfrick -reverse at x0_8, flip:
        pause 0.5
        walk_to(-2.5, 2.5)

    "I turn toward his back office and make my way there."

    "Within, I hear what sounds like a droning voice that is either very small and quiet or, somehow, very distant."

    scene bg flower_shop_backoffice
    play sound "effects/door_open.opus"
    show nate reverse accessories_hat accessories_glasses shirt_chill shirt_overall at y1, x0_75, reverse
    show wolfrick reverse accessories_watch accessories_glasses pants_formal shirt_formal at y1, x0_2, reverse

    "I open the door quietly and enter, seeing my adorable manatee husband standing, turned away from the door with his arms crossed."

    "Nate is staring at the small television up in the corner of the room."

    show wolfrick face_sad

    w "Hey, love. What's going on with this?"

    show nate face_happy at flip_back()
    show wolfrick face_neutral:
        pause 0.8
        nod

    "He turns his head toward me with a smile and I motion up toward the television."

    show nate -reverse

    na "Hey, sweetheart."

    show nate face_concerned at slow_nod:
        pause 1
        shake

    "He sighs and shakes his head."

    na "The new initiatives that were to be proposed by the citizens' representatives have apparently been vetoed by the council, and there seems to be no support from the High Emperor King President Lycanus."

    w "New… initiatives?"

    na "Yes, I mentioned them before – remember?"

    "I don't. I shrug and he sighs again. I probably should listen to him better."

    na "Those initiatives the citizens' representatives were trying to propose, most of which were in effort of making the lower-end of the housing economy more affordable and allowing for easier citizenship to the people who have begun to join us in this world recently."

    "Oh, right. I {i}do{/i} remember now."

    show wolfrick face_shocked at nod

    "I mouth an 'oh' as best as a wolf muzzle can and nod."

    show wolfrick face_concerned

    w "Shit, maybe I should have heard that beggar out more. He might have been an {i}isekai'd individual{/i}."

    w "Oh well, I'll just report him to the Isekai Bureau of Science."

    show nate face_shocked

    "Nate looks at me with scrutiny."

    show nate face_sad

    na "You met an {i}I-I{/i} and want to put him through dealing with the {i}IBS{/i}?"

    show wolfrick face_happy

    "I chuckle."

    w "That's never {i}not{/i} funny."

    show nate face_happy
    show wolfrick face_blushing

    "He grins in spite of himself."

    show wolfrick at walk_to behind nate
    show nate face_neutral

    "I move over to hug him."

    show wolfrick at hug_right
    show nate face_shocked at hug_left

    "He is hugged in spite of himself."

    show nate face_sad
    show wolfrick face_shocked

    na "You know that's an important cause to me, Wolfrick!"

    show wolfrick face_sad

    "I do, and now I feel bad."

    "Generally, I agree that all of the men who have been appearing in our world recently need proper assistance."

    "The way the council has been treating them is horrendous – they all end up living together in buildings that are even more cramped than hostels."

    "Still, Nate doesn't seem to notice the things I have."

    w "All of the ones I've come across seem to have the same… {i}thirst{/i} in their eyes."

    w "I thought that guy I met earlier was homeless, but he turned out to be one of them."

    show wolfrick face_angry

    w "I don't know, Nate. They all seem to want something. How'd you like to see them all stealing your man, huh? I know {i}I{/i} wouldn't want them stealing {i}mine{/i}!"

    show nate face_concerned

    "Nate scoffs."

    show nate face_angry

    na "You're not serious, Wolfrick? I'm worried about where they're {i}living{/i}, not who they're {i}riding{/i}."

    na "Anyway…"

    "I look around. Nate was supposed to have lunch here already, but there's nothing."

    "Looking back to Nate, he's sheepishly scratching his neck, looking away."

    w "Hey, Nate?"

    "..."

    na "...Yes, Wolfrick?"

    "..."

    w "...Where's lunch? I'm hungry and we only have about forty-five minutes before I have to head back."

    "Nate sighs and looks me in the eye."

    na "Well… you see, I sort of… forgot."

    w "...Oh."

    na "I tried to call you to give you a heads-up but you didn't answer, so I left a message. My bad."

    w "Oh? Huh. I'll listen to it when I get back, what a pleasant surprise!"

    "Nate gives me a puzzled look."

    na "What? A surprise?"

    w "Yes, I get to hear your voice at work as much as I want!"

    "Nate rolls his eyes, laughing. I chuckle too."

    na "You're cheesey. Sorry for forgetting."

    w "That's alright, love. We'll make up for it {i}later on tonight{/i}, if you catch my drift~"

    "He is blushing now."

    na "Dick, right?"

    na "Is that the drift? Did I get it right?"

    "He definitely catches the drift."

    "I laugh and move in to kiss him."

    w "Yes, you did."

    na "Mmmm you're all musky. Did you run here?"

    w "I might have~"

    "Nate laughs and I tickle his mustache with a finger, looking down into his eyes."

    "He didn't want to grow the mustache out, because he said it made him look like his father."

    "He only did it because I loved it so much."

    na "Well, you should probably go grab lunch and get back to the office. I'll grab something quick in a bit, we can have a nice dinner tonight."

    "I nod."

    w "Right-O."

    "I lean in and smooch him some more."

    na "Mmmmfgh-luvya-mfgfhhh."

    w "Mffghg-luvyamore-mffffgh."

    "We part with a chuckle from him and a wink from me."

    "I pop the finger guns."

    w "Hasta la vista, baby."

    "Nate rolls his eyes, and follows me out of the office."

    "He walks me to the door and I feel a slap on my ass as I'm heading out the door."

    "I turn to retaliate but he shuts the arched door behind me."

    "I laugh and see him winking at me through the window next to it as the sign flips over to {i}Open{/i}."

    "He's gonna get it {i}good{/i} later."

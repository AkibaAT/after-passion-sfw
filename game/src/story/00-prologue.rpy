label prologue:

    "..."

    "Why is my body wet?"

    "...and why do I feel like I hit my head?"

    scene bg dark_alley

    "I wake up in a shallow puddle, the ground around me covered in trash bags."

    "Some are torn open, but I'm resting against one that, thankfully, is not."

    "...How did I end up in an alleyway sleeping on trash?"

    "I can't remember. I can’t remember {i}anything{/i}."

    "I examine my hands and body. Everything seems fine. I see no injuries."

    "A normal human guy with normal human attributes."

    "It doesn’t take long for my exhaustion to wear off."

    "My head doesn't hurt for long, either."

    "After a few moments, I stand up and make my way toward the opening of the alleyway."

    "Just as I get there, I stumble and grab the wall to stabilize myself."

    "I look around to see a sight beyond my imagination."

    scene bg city_day

    play sound "effects/city_crowd.opus" volume 0.1 loop

    "Anthros. Anthros everywhere."

    "I don't know how I know what they are, but by golly I do."

    "I see them all – lion people, tiger people, bear people! Oh my!"

    "I stumble out of the alleyway and move my way around the street nearby."

    "Conscious of my not-very-clothed state, I shiver as a chill autumn breeze blows past me."

    "I also feel the heat of the various gazes upon me from many of the hot anthro men around."

    "Surely {i}someone{/i} will want to help a frail, weak human?"

    "Possibly the strong, handsome tiger waiting on a bench at the bus stop nearby?"

    "..."

    "The tiger man lets out a {i}tsk-tsk{/i} and turns his attention back to his newspaper."

    "Not him, I suppose."

    "Maybe the delightful looking otter standing across the street at the light?"

    "..."

    "The otter sees me looking his way and turns to cross over to the opposite corner."

    "Not him either, it seems."

    "..."

    "Suddenly, I smell it."

    "A strong, powerful, manly musk."

    "I turn to see him."

    "The most incredible, handsome, sexy wolf man is striding down the street toward me."

    "My memory is gone, yet I instinctively know this is a situation I want to work out in my favor."

    show wolfrick shirt_formal pants_formal accessories_glasses body_chill at y1, walk_in_right

    "I know what I must do."

    show wolfrick at walk_to()

    "I reach out toward him, my eyes full of fear and pleading and my body frail and lithe in comparison to his large, muscular frame."

    show wolfrick face_concerned at x0_5

    "\"P-please, Mister Wolf… I need… help!\""

    show wolfrick face_shocked

    "The wolf looks at me with shock before covering his nose, and hands me something from his pocket."

    show wolfrick face_sad

    "I look down at what appears to be a couple of dollar bills."

    w "There, that's all the cash I have."

    "I'm confused, and look toward him."

    show wolfrick face_concerned

    "\"W-what?\""

    w "Yeah, sorry. I wish I could help more, but I switched to debit a long time ago, man. Sorry."

    show wolfrick face_sad at walk_out_left(2)

    "He begins to walk away."

    "\"W-wait! Aren't you {i}my{/i} wolf? You're supposed to take me in and shelter me, let me smell your musk, fall in love with me!\""

    "The wolf looks back at me with increasing fear and starts to pick up his pace."

    "\"Come back! You're my wolf! Mine!\""

    "I watch as he turns a corner, and then disappears."

    scene black with dissolve
    stop sound

    show bg title
    $ renpy.movie_cutscene("videos/title.webm")

    hide bg title with dissolve

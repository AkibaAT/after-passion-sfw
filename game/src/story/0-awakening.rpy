label ch0_awakening:

    stop music

    voice "0-awakening/001.opus"
    "..."

    voice "0-awakening/002.opus"
    "Why is my body wet?"

    voice "0-awakening/003.opus"
    "...and why do I feel like I hit my head?"

    scene bg dark_alley

    voice "0-awakening/004.opus"
    "I wake up in a shallow puddle, the ground around me covered in trash bags."

    voice "0-awakening/005.opus"
    "Some are torn open, but I'm resting against one that, thankfully, is not."

    voice "0-awakening/006.opus"
    "...How did I end up in an alleyway sleeping on trash?"

    voice "0-awakening/007.opus"
    "I can't remember. I can’t remember {i}anything{/i}."

    voice "0-awakening/008.opus"
    "I examine my hands and body. Everything seems fine. I see no injuries."

    voice "0-awakening/009.opus"
    "A normal human guy with normal human attributes."

    voice "0-awakening/010.opus"
    "It doesn't take long for my exhaustion to wear off."

    voice "0-awakening/011.opus"
    "My head doesn't hurt for long, either."

    voice "0-awakening/012.opus"
    "After a few moments, I stand up and make my way toward the opening of the alleyway."

    voice "0-awakening/013.opus"
    "Just as I get there, I stumble and grab the wall to stabilize myself."

    voice "0-awakening/014.opus"
    "I look around to see a sight beyond my imagination."

    scene bg city_day

    play sound "effects/city_crowd.opus" volume 0.1 loop

    voice "0-awakening/015.opus"
    "Anthros. Anthros everywhere."

    voice "0-awakening/016.opus"
    "I don't know how I know what they are, but by golly I do."

    voice "0-awakening/017.opus"
    "I see them all – lion people, tiger people, bear people! Oh my!"

    voice "0-awakening/018.opus"
    "I stumble out of the alleyway and move my way around the street nearby."

    voice "0-awakening/019.opus"
    "Conscious of my not-very-clothed state, I shiver as a chill autumn breeze blows past me."

    voice "0-awakening/020.opus"
    "I also feel the heat of the various gazes upon me from many of the hot anthro men around."

    voice "0-awakening/021.opus"
    "Surely {i}someone{/i} will want to help a frail, weak human?"

    voice "0-awakening/022.opus"
    "Possibly the strong, handsome tiger waiting on a bench at the bus stop nearby?"

    "..."

    voice "0-awakening/023.opus"
    "The tiger man lets out a {i}tsk-tsk{/i} and turns his attention back to his newspaper."

    voice "0-awakening/024.opus"
    "Not him, I suppose."

    voice "0-awakening/025.opus"
    "Maybe the delightful looking otter standing across the street at the light?"

    "..."

    voice "0-awakening/026.opus"
    "The otter sees me looking his way and turns to cross over to the opposite corner."

    voice "0-awakening/027.opus"
    "Not him either, it seems."

    "..."

    voice "0-awakening/028.opus"
    "Suddenly, I smell it."

    voice "0-awakening/029.opus"
    "A strong, powerful, manly musk."

    voice "0-awakening/030.opus"
    "I turn to see him."

    voice "0-awakening/031.opus"
    "The most incredible, handsome, sexy wolf man is striding down the street toward me."

    voice "0-awakening/032.opus"
    "My memory is gone, yet I instinctively know this is a situation I want to work out in my favor."

    show wolfrick shirt_formal pants_formal accessories_glasses accessories_watch body_chill at y1, walk_in_right

    voice "0-awakening/033.opus"
    "I know what I must do."

    show wolfrick at walk_to()

    voice "0-awakening/034.opus"
    "I reach out toward him, my eyes full of fear and pleading and my body frail and lithe in comparison to his large, muscular frame."

    show wolfrick face_concerned at x0_5

    voice "0-awakening/035.opus"
    "\"P-please, Mister Wolf… I need… help!\""

    show wolfrick face_shocked

    voice "0-awakening/036.opus"
    "The wolf looks at me with shock before covering his nose, and hands me something from his pocket."

    show wolfrick face_sad

    voice "0-awakening/037.opus"
    "I look down at what appears to be a couple of dollar bills."

    voice "0-awakening/038.opus"
    w "There, that's all the cash I have."

    voice "0-awakening/039.opus"
    "I'm confused, and look toward him."

    show wolfrick face_concerned

    voice "0-awakening/040.opus"
    "\"W-what?\""

    voice "0-awakening/041.opus"
    w "Yeah, sorry. I wish I could help more, but I switched to debit a long time ago, man. Sorry."

    show wolfrick face_sad at walk_out_left(2)

    voice "0-awakening/042.opus"
    "He begins to walk away."

    voice "0-awakening/043.opus"
    "\"W-wait! Aren't you {i}my{/i} wolf? You're supposed to take me in and shelter me, let me smell your musk, fall in love with me!\""

    voice "0-awakening/044.opus"
    "The wolf looks back at me with increasing fear and starts to pick up his pace."

    voice "0-awakening/045.opus"
    "\"Come back! You're my wolf! Mine!\""

    voice "0-awakening/046.opus"
    "I watch as he turns a corner, and then disappears."

    scene black with dissolve
    stop sound

    show bg title
    $ renpy.movie_cutscene("videos/title.webm")

    hide bg title with dissolve

    $ set_chapter_progress(1)

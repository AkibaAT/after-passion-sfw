#default player_name="Human From The Alley"
label ch0_awakening:

    stop music

    scene black
    centered "Chapter [chapter_list[0][title]]"

    voice "voice/0-awakening/001.opus"
    "..."

    voice "voice/0-awakening/002.opus"
    "Why is my body wet?"

    voice "voice/0-awakening/003.opus"
    "...and why do I feel like I hit my head?"

    scene bg dark_alley

    voice "voice/0-awakening/004.opus"
    "I wake up in a shallow puddle, the ground around me covered in trash bags."

    voice "voice/0-awakening/005.opus"
    "Some are torn open, but I'm resting against one that, thankfully, is not."

    voice "voice/0-awakening/006.opus"
    "...How did I end up in an alleyway sleeping on trash?"

    voice "voice/0-awakening/007.opus" 
    "Aside from my name, I can't remember {i}anything{i}."

    voice "voice/0-awakening/MyNameIs.opus" 
    $ player_input = renpy.input("My name is...").strip()

    if player_input == "Sonic":
        $ player_name = "Sonic"
        voice "voice/0-awakening/ThatSoundsRight.opus" # Will need to replace this with sonic voice line lol
        "%(player_name)s. That sounds right."
        jump .ch0_awakening
    elif player_input == "Human From The Alley":
        $ player_name = "Human From The Alley"
        voice "voice/0-awakening/ThatSoundsRight.opus"
        "%(player_name)s. That sounds right."
        jump .ch0_awakening
    else:
        $ player_name = "Human From The Alley"

    "%(player_input)s..."

    "Hmm, that doesn't sound quite right. I think my name is %(player_name)s." #Voice needed
label .ch0_awakening:

    voice "voice/0-awakening/008.opus"
    "I examine my hands and body. Everything seems fine. I see no injuries."

    voice "voice/0-awakening/009.opus"
    "A normal human guy with normal human attributes."

    voice "voice/0-awakening/010.opus"
    "It doesn't take long for my exhaustion to wear off."

    voice "voice/0-awakening/011.opus"
    "My head doesn't hurt for long, either."

    voice "voice/0-awakening/012.opus"
    "After a few moments, I stand up and make my way toward the opening of the alleyway."

    scene bg dark_alley_exit with dissolve
    voice "voice/0-awakening/013.opus"
    "Just as I get there, I stumble and grab the wall to stabilize myself."

    voice "voice/0-awakening/014.opus"
    "I look around to see a sight beyond my imagination."

    scene bg city_day_4

    play sound "effects/city_crowd.opus" volume 0.1 loop

    voice "voice/0-awakening/015.opus"
    "Anthros. Anthros everywhere."

    voice "voice/0-awakening/016.opus"
    "I don't know how I know what they are, but by golly I do."

    voice "voice/0-awakening/017.opus"
    "I see them all - lion people, tiger people, bear people! Oh my!"

    voice "voice/0-awakening/018.opus"
    "I stumble out of the alleyway and move my way around the street nearby."

    voice "voice/0-awakening/019.opus"
    "Conscious of my not-very-clothed state, I shiver as a chill autumn breeze blows past me."

    voice "voice/0-awakening/020.opus"
    "I also feel the heat of the various gazes upon me from many of the hot anthro men around."

    voice "voice/0-awakening/021.opus"
    "Surely {i}someone{/i} will want to help a frail, weak human?"

    voice "voice/0-awakening/022.opus"
    "Possibly the strong, handsome tiger waiting on a bench at the bus stop nearby?"

    "..."

    voice "voice/0-awakening/023.opus"
    "The tiger man lets out a {i}tsk-tsk{/i} and turns his attention back to his newspaper."

    voice "voice/0-awakening/024.opus"
    "Not him, I suppose."

    voice "voice/0-awakening/025.opus"
    "Maybe the delightful looking otter standing across the street at the light?"

    "..."

    voice "voice/0-awakening/026.opus"
    "The otter sees me looking his way and turns, crossing over to the opposite corner.."

    voice "voice/0-awakening/027.opus"
    "Not him either, it seems."

    "..."

    voice "voice/0-awakening/028.opus"
    "Suddenly, I smell it."

    voice "voice/0-awakening/029.opus"
    "A strong, powerful, manly musk."

    voice "voice/0-awakening/030.opus"
    "I turn to see him."

    voice "voice/0-awakening/031.opus"
    "The most incredible, handsome, sexy wolf man is striding down the street toward me."

    voice "voice/0-awakening/032.opus"
    "My memory is gone, yet I instinctively know this is a situation I want to work out in my favor."

    show wolfrick preset_work:
        y1
        walk_in_right()

    voice "voice/0-awakening/033.opus"
    "I know what I must do."

    show wolfrick at walk_to

    voice "voice/0-awakening/034.opus"
    "I reach out toward him, my eyes full of fear and pleading and my body frail and lithe in comparison to his large, muscular frame."

    show wolfrick face_concerned at x0_5

    voice "voice/0-awakening/035.opus"
    "\"P-please, Mister Wolf… I need… help!\""

    show wolfrick face_shocked

    voice "voice/0-awakening/036.opus"
    "The wolf looks at me with shock before covering his nose, and hands me something from his pocket."

    show wolfrick face_sad

    voice "voice/0-awakening/037.opus"
    "I look down at what appears to be a couple of dollar bills."

    voice "voice/0-awakening/038.opus"
    w "There, that's all the cash I have."

    voice "voice/0-awakening/039.opus"
    "I'm confused, and look toward him."

    show wolfrick face_concerned

    voice "voice/0-awakening/040.opus"
    "\"W-what?\""

    voice "voice/0-awakening/041.opus"
    w "Yeah, sorry. I wish I could help more, but I switched to debit a long time ago, man. Sorry."

    show wolfrick face_sad at walk_out_left(2)

    voice "voice/0-awakening/042.opus"
    "He begins to walk away."

    hide wolfrick
    pause 0.5
    
    voice "voice/0-awakening/Freak.opus"
    w "Freak"

    voice "voice/0-awakening/043.opus"
    "\"W-wait! Aren't you {i}my{/i} wolf? You're supposed to take me in and shelter me, let me smell your musk, fall in love with me!\""

    voice "voice/0-awakening/044.opus"
    "The wolf looks back at me with increasing fear and starts to pick up his pace."

    voice "voice/0-awakening/045.opus"
    "\"Come back! You're my wolf! {i}{size=-4}Mii{size=-4}iii{size=-4}iiiin{size=-4}eeeee!{/size}{/size}{/size}{/size}{/i}\""

    voice "voice/0-awakening/046.opus"
    "I watch as he turns a corner, and then disappears."

    scene black with dissolve
    stop sound

    show bg title
    $ renpy.movie_cutscene("videos/title.webm")

    scene black with fade

    $ set_chapter_progress(1)

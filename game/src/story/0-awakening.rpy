default player_name="Human From The Alley"
define human = Character(None, image="Human", voice_tag="human")

label ch0_awakening:

    stop music

    scene black
    centered "Chapter [chapter_list[0][title]]"

    alt "Description: There is no light, and no information as to where you are."

    voice "voice/0-awakening/001.opus"
    human "..."

    voice "voice/0-awakening/002.opus"
    human "Why is my body wet?"

    voice "voice/0-awakening/003.opus"
    human "...and why do I feel like I hit my head?"

    scene bg dark_alley

    alt "Description: A dark alleyway is revealed, with a large bright opening at the far side."

    voice "voice/0-awakening/004.opus"
    human "I wake up in a shallow puddle, the ground around me covered in trash bags."

    voice "voice/0-awakening/005.opus"
    human "Some are torn open, but I'm resting against one that, thankfully, is not."

    voice "voice/0-awakening/006.opus"
    human "...How did I end up in an alleyway sleeping on trash?"

    voice "voice/0-awakening/007.opus" 
    human "Aside from my name, I can't remember {i}anything{i}."

    voice "voice/0-awakening/MyNameIs.opus"
    alt "Description: Please enter a name after the prompt, and confirm with the enter key."
    $ player_input = renpy.input("My name is...").strip()

    if player_input == "Sonic":
        $ player_name = "Sonic"
        voice "voice/0-awakening/ThatSoundsRight.opus" # Will need to replace this with sonic voice line lol
        human "%(player_name)s. That sounds right."
        jump .ch0_awakening
    elif player_input == "Human From The Alley":
        $ player_name = "Human From The Alley"
        voice "voice/0-awakening/ThatSoundsRight.opus"
        human "%(player_name)s. That sounds right."
        jump .ch0_awakening
    else:
        $ player_name = "Human From The Alley"

    human "%(player_input)s..."

    voice "voice/0-awakening/Ithinkmynameis.opus"
    human "Hmm, that doesn't sound right. I think my name is %(player_name)s." #Voice needed
label .ch0_awakening:

    voice "voice/0-awakening/008.opus"
    human "I examine my hands and body. Everything seems fine. I see no injuries."

    voice "voice/0-awakening/009.opus"
    human "A normal human guy with normal human attributes."

    voice "voice/0-awakening/010.opus"
    human "It doesn't take long for my exhaustion to wear off."

    voice "voice/0-awakening/011.opus"
    human "My head doesn't hurt for long, either."

    voice "voice/0-awakening/012.opus"
    human "After a few moments, I stand up and make my way toward the opening of the alleyway."

    scene bg dark_alley_exit with dissolve
    alt "Description: The alleyway opens up to a busy city street."
    voice "voice/0-awakening/013.opus"
    human "Just as I get there, I stumble and grab the wall to stabilize myself."

    voice "voice/0-awakening/014.opus"
    human "I look around to see a sight beyond my imagination."

    scene bg city_day_4
    alt "Description: A bright city scape is revealed."

    stop sound
    play sound "effects/city_crowd.opus" volume 0.25 loop

    voice "voice/0-awakening/015.opus"
    human "Anthros. Anthros everywhere."

    voice "voice/0-awakening/016.opus"
    human "I don't know how I know what they are, but by golly I do."

    voice "voice/0-awakening/017.opus"
    human "I see them all - lion people, tiger people, bear people! Oh my!"

    voice "voice/0-awakening/018.opus"
    human "I stumble out of the alleyway and move my way around the street nearby."

    voice "voice/0-awakening/019.opus"
    human "Conscious of my not-very-clothed state, I shiver as a chill autumn breeze blows past me."

    voice "voice/0-awakening/020.opus"
    human "I also feel the heat of the various gazes upon me from many of the hot anthro men around."

    voice "voice/0-awakening/021.opus"
    human "Surely {i}someone{/i} will want to help a frail, weak human?"

    voice "voice/0-awakening/022.opus"
    human "Possibly the strong, handsome tiger waiting on a bench at the bus stop nearby?"

    human "..."

    voice "voice/0-awakening/023.opus"
    human "The tiger man lets out a {i}tsk-tsk{/i} and turns his attention back to his newspaper."

    voice "voice/0-awakening/024.opus"
    human "Not him, I suppose."

    voice "voice/0-awakening/025.opus"
    human "Maybe the delightful looking otter standing across the street at the light?"

    human "..."

    voice "voice/0-awakening/026.opus"
    human "The otter sees me looking his way and turns, crossing over to the opposite corner.."

    voice "voice/0-awakening/027.opus"
    human "Not him either, it seems."

    human "..."

    voice "voice/0-awakening/028.opus"
    human "Suddenly, I smell it."

    voice "voice/0-awakening/029.opus"
    human "A strong, powerful, manly musk."

    voice "voice/0-awakening/030.opus"
    human "I turn to see him."

    voice "voice/0-awakening/031.opus"
    human "The most incredible, handsome, sexy wolf man is striding down the street toward me."

    voice "voice/0-awakening/032.opus"
    human "My memory is gone, yet I instinctively know this is a situation I want to work out in my favor."

    show wolfrick preset_work:
        y1
        walk_in_right()
    alt "Description: A wolf anthro is revealed, entering your vision from the right. He is dressed in a black suit and purple tie, and light blue pants. He is wearing glasses, and a wristwatch on his right arm."

    voice "voice/0-awakening/033.opus"
    human "I know what I must do."

    show wolfrick at walk_to

    voice "voice/0-awakening/034.opus"
    human "I reach out toward him, my eyes full of fear and pleading and my body frail and lithe in comparison to his large, muscular frame."

    show wolfrick face_concerned at x0_5

    voice "voice/0-awakening/035.opus"
    human "\"P-please, Mister Wolf… I need… help!\""

    show wolfrick face_shocked

    voice "voice/0-awakening/036.opus"
    human "The wolf looks at me with shock before covering his nose, and hands me something from his pocket."

    alt "Description: The wolf's expression turns sad."
    show wolfrick face_sad

    voice "voice/0-awakening/037.opus"
    human "I look down at what appears to be a couple of dollar bills."

    voice "voice/0-awakening/038.opus"
    w "There, that's all the cash I have."

    voice "voice/0-awakening/039.opus"
    human "I'm confused, and look toward him."

    alt "Description: The wolf looks at you with concern."
    show wolfrick face_concerned

    voice "voice/0-awakening/040.opus"
    human "\"W-what?\""

    voice "voice/0-awakening/041.opus"
    w "Yeah, sorry. I wish I could help more, but I switched to debit a long time ago, man. Sorry."

    show wolfrick face_sad at walk_out_left(2)

    voice "voice/0-awakening/042.opus"
    human "He begins to walk away."

    hide wolfrick
    pause 0.5
    alt "Description: The exits your vision to the left."
    
    voice "voice/0-awakening/Freak.opus"
    w "Freak"

    voice "voice/0-awakening/043.opus"
    human "\"W-wait! Aren't you {i}my{/i} wolf? You're supposed to take me in and shelter me, let me smell your musk, fall in love with me!\""

    voice "voice/0-awakening/044.opus"
    human "The wolf looks back at me with increasing fear and starts to pick up his pace."

    voice "voice/0-awakening/045.opus"
    human "\"Come back! You're my wolf! {i}{size=-4}Mii{size=-4}iii{size=-4}iiiin{size=-4}eeeee!{/size}{/size}{/size}{/size}{/i}\""

    voice "voice/0-awakening/046.opus"
    human "I watch as he turns a corner, and then disappears."

    scene black with dissolve
    stop sound

    alt "Description: An animated logo appears, a pink heart, the title \"After Passion\" fades into view, turns from pink to blue, and then the whole scene fades to black."
    show bg title
    $ renpy.movie_cutscene("videos/title.webm")

    scene black with fade
    alt "Description: The scene fades to black."

    $ set_chapter_progress(1)

label ch3_comfort:

    stop music

    scene black
    centered "Chapter [chapter_list[3]['title']]"

    scene bg apartment_dining
    show nic preset_casual face_angry:
        y1
        x0_8
    show nate preset_casual reverse:
        y1
        x0_5
        reverse
    show wolfrick preset_casual face_stern reverse:
        y1
        x0_2
        reverse
    with dissolve

    alt "Description: From left to right, Wolfrick, Nate and Nic are standing in the living room."

    "It's been a few hours since Nic arrived, and we're all just sitting at the table in the dining room drinking."

    "None of us have to work tomorrow since it's Saturday, but Nate still goes in to check on his shop for a few hours in the middle of the day."

    "Still…"

    "Nic is getting {i}plastered{/i}."

    "I get it, with the break-up and his money being basically held hostage…"

    voice "voice/3-comfort/001.opus"
    ni "That {i}stinky, matted-fur {b}bitch{/b}{/i} couldn't even handle an ounce of criticism!"

    "...he's been at it for a while."

    voice "voice/3-comfort/002.opus"
    ni "That {i}limp-knotted {b}fucker{/b}{/i} better not show his face right now."

    show wolfrick face_concerned

    "Shouldn't we be calming him down?"

    show nate at push_right

    "Seemingly on a similar wavelength, Nate reaches a hand out to Nic and pats his shoulder."

    voice "voice/3-comfort/003.opus"
    na "I know, hun. I know."

    voice "voice/3-comfort/004.opus"
    na "We're here, it'll be okay. If he shows up we've got your-"

    voice "voice/3-comfort/005.opus"
    ni "I {i}dare{/i} that {i}slimy-nosed {b}ass sniffer{/b}{i} to show his awful mug here!"

    voice "voice/3-comfort/006.opus"
    ni "I mean, he slept with my co-worker!"

    voice "voice/3-comfort/007.opus"
    ni "He did that shit and claimed it was to help {i}me{/i} out!"

    voice "voice/3-comfort/008.opus"
    show wolfrick body_crossed face_concerned

    w "That's horrible! What kind of man cheats on their partner?"

    voice "voice/3-comfort/009.opus"
    ni "I'm not going to miss the stupid shit he used to pull."

    voice "voice/3-comfort/010.opus"
    ni "I made most of the money, you know? He {i}still{/i} belittled me!"

    voice "voice/3-comfort/011.opus"
    ni "Constant remarks like \"You're my little dragon,\" and \"Let your wolf handle things, you're so fragile\"."

    voice "voice/3-comfort/012.opus"
    ni "I always hated that shit, he'd set himself above me in everything!"

    voice "voice/3-comfort/013.opus"
    na "Huh, that seems abusive. It sounds like he isolated you, too."

    voice "voice/3-comfort/014.opus"
    ni "Well, yeah. He made me stop talking to other people unless he liked them."

    voice "voice/3-comfort/015.opus"
    ni "He'd tell me I was {i}his{/i} and nobody else could have me."

    voice "voice/3-comfort/016.opus"
    ni "Like, I'm my own person! I can't stand that shit."

    voice "voice/3-comfort/017.opus"
    na "Wolves can get a bit territorial, it's part of the appeal - but that sounds extreme."

    voice "voice/3-comfort/018.opus"
    show wolfrick face_sad

    w "...I only do that because you said you want me to."

    "Nate looks my way as if trying to act as though he heard me but is focused on Nic."

    voice "voice/3-comfort/019.opus"
    ni "Yes, and he's always walking around all musky and sweaty - like, boy! You stink!"

    voice "voice/3-comfort/020.opus"
    na "Ugh, I know! It's not appealing."

    voice "voice/3-comfort/021.opus"
    w "...Hey! You said you like my musk!"

    voice "voice/3-comfort/022.opus"
    na "Yeah, love, that's alright."

    "Is he even listening to me?"

    voice "voice/3-comfort/023.opus"
    w "You should have said something-"

    voice "voice/3-comfort/024.opus"
    ni "Oh, and don't even get me started on the constant need to look my best physically, otherwise people {i}compare{/i} us!"

    voice "voice/3-comfort/025.opus"
    na "Oh, hun. Tell me about it! I couldn't keep it up, my sanity would have snapped before my body did!"

    voice "voice/3-comfort/026.opus"
    w "...I love your body regardless…"

    voice "voice/3-comfort/027.opus"
    show nate face_angry

    na "Fuck Zephyr, honestly!"

    "He definitely isn't listening."

    voice "voice/3-comfort/028.opus"
    ni "Goddamnit, he gets me {i}so{/i} worked up!"

    "Have I been awful to Nate?"

    "There are problems I'm seeing now that I think I could have seen sooner if I hadn't been looking at, well, {i}us{/i} from the outside."

    "Yeah… Zephyr has committed a long list of terrible deeds, and thankfully Nic is finally out of that relationship.."

    "...still…"

    show nate face_neutral

    "While I'm not nearly the abusive asshole Zephyr is, I feel like there's a line between us, and I am dancing on the very first treadings of it."

    "More than that, Nate has been so different lately, and it's starting to worry me."

    voice "voice/3-comfort/029.opus"
    na "Nic, hun… calm down, he's not here and you're safe."

    voice "voice/3-comfort/030.opus"
    w "Nate, do you think we could talk on the balcony for a minute?"

    show nate:
        flip_back()
        pause 0.2
        function add_attributes(["face_concerned"])

    "Nate looks at me with a concerned expression."

    show nate -reverse:
        no_reverse
    show wolfrick body_chill:
        flip_back()
        walk_out_left()

    play sound ['<silence 0.6>', 'audio/effects/door_open.opus'] volume 0.8
    "I stand up to walk out the balcony door."

    show nate:
        flip()
        pause 0.1
        push_right(2)
        pause 0.1
        flip_back()
        pause 0.1
        walk_out_left()

    "Nate pats Nic on the shoulder and stands up to follow."

    play ambient "audio/effects/day_balcony.opus" volume 0.05
    play music "music/Guardian Angel2.opus" volume 0.15 fadein 1.0 fadeout 2.0

    scene bg apartment_balcony_day
    show nate preset_casual:
        y1
        x1_3
    show wolfrick preset_casual reverse face_sad:
        y1
        x0_3
        reverse
    with dissolve
    show nate:
        walk_in_right()
    alt "Description: The scene switches to an outside of the balcony, Nate joining Wolfrick, who is standing next to the railing, lookíng sad and looking away from Nate."

    voice "voice/3-comfort/031.opus"
    na "Hey, love. What's up?"

    show wolfrick face_concerned
    show nate:
        reset_pos(8)

    voice "voice/3-comfort/032.opus"
    w "Am I that bad?"

    show nate face_shocked

    "I see the confusion on his face."

    voice "voice/3-comfort/033.opus"
    show nate face_concerned

    na "What are you talking about?"

    show wolfrick face_sad
    voice "voice/3-comfort/034.opus"
    w "Nate, you can barely listen to me or focus on me lately. Have I been driving you away?"

    show nate face_shocked

    "His eyes widen, and he looks away for a moment."

    show nate face_concerned
    voice "voice/3-comfort/035.opus"
    na "I don't think this is the best time to-"

    show wolfrick at quick_shake

    "I shake my head."

    show wolfrick face_concerned
    voice "voice/3-comfort/036.opus"
    w "Neither of us are nearly as plastered as Nic, if there's ever a time it's going to be now."

    show wolfrick face_sad
    voice "voice/3-comfort/037.opus"
    w "You had me thinking you enjoyed the stereotypical 'wolf boyfriend' things, and I'm just now finding out on our {i}third{/i} anniversary that you don't?"

    show nate face_sad
    show wolfrick face_concerned
    voice "voice/3-comfort/038.opus"
    na "Well, it's not that I don't enjoy them…"

    voice "voice/3-comfort/039.opus"
    na "There are aspects of that that are very appealing to me, but sometimes the expectations of that kind of relationship get rough!"

    voice "voice/3-comfort/040.opus"
    w "But… I don't {i}have{/i} any expectations of you, Nate! I just want to love you."

    voice "voice/3-comfort/041.opus"
    na "Wolfrick, {i}you{/i} don't have to expect them of me."

    voice "voice/3-comfort/042.opus"
    na "You being-"

    "Nate motions to all of me."

    voice "voice/3-comfort/043.opus"
    na "Well, {i}you{/i} - puts this… this {i}image{/i} of a put together couple into peoples' minds!"

    voice "voice/3-comfort/044.opus"
    na "A wolf with an amazing body and that musk, and his partner who {i}must{/i} be a cute, little submissive bottom!"

    voice "voice/3-comfort/045.opus"
    na "It's always \"Wolfrick makes the big bucks, Nate must be his trophy husband!\" or \"Wow, Nate! You must love having such a strong and protective wolf for a husband\"!"

    voice "voice/3-comfort/046.opus"
    na "Everyone around us says this stuff and everyone else holds the expectations against me {i}for{/i} you, but you never seem to notice!"

    "I'm stunned. Is his confidence taking blows from everyone all the time like this?"

    "Now that I think back, I understand what he means. If anything, he used to make remarks about this sort of thing."

    "I guess I took them at face value and tried to make myself the most wolf-esque man for him. I don't remember him actually {i}saying{/i} he wanted me to do that."

    "I look into Nate's eyes."

    "I need to express what I feel now."

    voice "voice/3-comfort/047.opus"
    w "It feels like you ignore me all the time."

    voice "voice/3-comfort/048.opus"
    w "You put your causes first, and I love that you care…"

    voice "voice/3-comfort/049.opus"
    w "...but sometimes you get so invested that you forget to do things I need help with, or outright don't listen when I'm trying to communicate."

    voice "voice/3-comfort/050.opus"
    na "Do I really? I guess I hadn't noticed…"

    voice "voice/3-comfort/051-1.opus"
    w "Well, there was earlier - you got so drawn in to the news broadcast that you forgot to order lunch."

    voice "voice/3-comfort/051-2.opus"
    w "Then I tried to make it up by making dinner for us, and that got ruined."

    voice "voice/3-comfort/052.opus"
    na "{i}Ruined?!{/i} My apologies for helping out my cousin, so sorry it interrupted {i}dinner{/i} but-"

    voice "voice/3-comfort/053.opus"
    w "N-no, that's not the issue, Nate! I don't care that you're - no, {i}we're{/i} - helping Nic!"

    voice "voice/3-comfort/054.opus"
    w "I'm upset that I couldn't make the night romantic for us!"

    "Nate is silent and I can see his eyes welling up."

    "I hate fighting with him, and it feels like we're heading that way."

    voice "voice/3-comfort/055.opus"
    w "Then, there's just now with Nic - don't get me wrong, I love you and your family will always be welcome."

    voice "voice/3-comfort/056.opus"
    w "You just…barely even acknowledged that I was there. It made me feel like I was eavesdropping while you guys were taking potshots at wolves in general."

    show wolfrick face_sad
    voice "voice/3-comfort/057.opus"
    w "It hurt, Nate."

    voice "voice/3-comfort/058.opus"
    na "Oh… I guess that was all pretty hurtful, yeah."

    voice "voice/3-comfort/059.opus"
    na "I'm sorry…"

    voice "voice/3-comfort/060.opus"
    na "I guess I feel like sometimes you make all the decisions for us, like while we were part of the resistance against the former High King Emperor Rexford."

    voice "voice/3-comfort/061.opus"
    na "I was hailed as some \"chosen one\" but it always felt like you did everything, up until the last second."

    voice "voice/3-comfort/062.opus"
    na "I guess after we succeeded in overthrowing him and helped assign Lycanus to the throne, I felt like I needed something of my own to focus on."

    voice "voice/3-comfort/063.opus"
    na "The flower shop helped, but there was something {i}missing{/i}."

    show wolfrick face_concerned
    show nate face_happy
    voice "voice/3-comfort/064.opus"
    na "I love flowers, don't get me wrong-"

    "Nate's eyes are aglow."

    "His brow is furrowed and he's intent."

    "I missed this look, he had it all the time back then."

    show nate face_neutral
    voice "voice/3-comfort/065.opus"
    na "But there just isn't any {i}passion{/i} in that for me."

    voice "voice/3-comfort/066.opus"
    na "Fighting for these causes - they're something I can do to make change, and {i}I'm{/i} in control of  leading the charge!"

    show wolfrick face_smiling

    "I smile, seeing him full of life." 

    "I suppose I {i}have{/i} been the one to take charge a lot."

    "I should let him take the reins every now and again, I know that."

    "Not allowing him to be able to handle a situation is unfair to him."

    voice "voice/3-comfort/067.opus"
    w "Nate… you're right."

    voice "voice/3-comfort/068.opus"
    w "I shouldn't take control from you like that, I'm sorry."

    voice "voice/3-comfort/069.opus"
    w "I promise, I'll work on that."

    voice "voice/3-comfort/070.opus"
    w "I love who you are so much, I guess I just need to take a step back sometimes and let you be that man."

    show nate face_happy:
        walk_to(5.5)

    "Nate smiles, and moves closer. He takes my hand in his."

    show nate face_neutral:
        reset_pos(5.5)

    voice "voice/3-comfort/071.opus"
    na "We'll get there, Wolfrick. We'll get there."

    voice "voice/3-comfort/072.opus"
    na "For the record, I don't {i}always{/i} want you to give me the reins. We need to handle things together, too."

    voice "voice/3-comfort/073.opus"
    na "...and I will do my best to listen to you more. I didn't realize I had started to ignore you."

    show wolfrick face_stern

    voice "voice/3-comfort/074.opus"
    na "I'm sorry, Wolfrick."

    show wolfrick:
        parallel:
            hug_right()
        parallel:
            pause 0.4
            function add_attributes(["face_smiling"])
    show nate:
        parallel:
            hug_left()
        parallel:
            pause 0.5
            function add_attributes(["face_happy"])

    "We share a hug, and then a kiss."

    show wolfrick face_smiling:
        no_offset
        pause 0.8
        walk_out_right(1.6)
    show nate face_happy:
        no_offset
        flip()
        walk_out_right()
    stop ambient
    play sound "effects/door_full.opus"
    scene bg apartment_dining
    show nate preset_casual reverse face_concerned:
        y1
        x1_3
        reverse
        walk_in_left()
    show wolfrick preset_casual reverse face_stern:
        y1
        x1_3
        reverse
        walk_in_left(5)
    with dissolve

    "After we head back inside, Nic is nowhere to be found."

    show nate face_neutral:
        reset_pos(2)
    show wolfrick:
        reset_pos(5)

    "At first, Nate has a look of worry, but that fades quickly."

    "We hear him in the bathroom through the walls."

    voice "voice/3-comfort/075.opus"
    ni "HHUUUUUURGGHHHHHLLLLLLBLHHHHHHHH–"

    show wolfrick:
        flip_back()
        pause 0.1
        parallel:
            quick_nod(2)
        parallel:
            pause 0.1
            function add_attributes(["face_smiling"])

    "I turn to Nate and chuckle."

    show wolfrick -reverse:
        no_offset
        no_reverse 
    show nate face_happy:
        nod()

    "He smirks at me and shrugs."

    stop music fadeout 2.0
    scene black with fade
    alt "Description: The scene fades to black."

    $ set_chapter_progress(4)

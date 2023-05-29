label ch2_romance:

    stop music
    scene bg apartment_kitchen
    show wolfrick accessories_glasses accessories_watch pants_joggers shirt_joggers at x0_4, y1
    with dissolve

    "..."

    "The table is set with our fine china and a couple of wine glasses."

    "I went and bought a nice new burgundy tablecloth just for the occasion, and the white dishes contrast it nicely."

    "There is a cute silver candelabra in the center, set with four candles to be lit when I see Nate walking over from the bus stop."

    "I used to buy him flowers, but since he opened the flower shop they've lost their impact."

    "As I'm waiting, I've been working on our dinner."

    "I've just finished roasting the vegetables and am now sautéing the fish - a beautiful pair of tilapias."

    "There's only so much time left to finish everything, and I need to make sure to get it all right."

    show wolfrick at flip

    "I look out the window after hearing a bus pull off outside."

    show wolfrick reverse at reverse

    "Nate is walking across the street toward the building. I only have about three minutes."

    show wolfrick at flip_back

    "I get home about two hours before Nate does every day, so there wasn't much time to waste anyway, but now…."

    show wolfrick -reverse at no_reverse

    "I finish the tilapias off and plate them, then use a bit of sherry to deglaze the pan and make a flavorful, light sauce to pour over the finished dish."

    "A minute passes."

    show wolfrick:
        parallel:
            walk_z_front(speed=2.0, steps=3)
        parallel:
            pause 0.5
            fade_to(0, 1.3)
    scene bg apartment_dining with dissolve
    show wolfrick accessories_glasses accessories_watch pants_joggers shirt_joggers at y1:
        walk_in_right(7)

    "I still manage to finish the dishes off with a garnish and get ready to light the candles."

    show wolfrick at x0_7, no_offset

    "Another minute of waiting, a smile plastered on my face."

    "I've finally gotten everything exactly how I want it."

    "It's going to be perfect. Nate's going to love it."

    "Tilapia is his favorite."

    "I barely get to cook for him anymore, and I made sure to have everything ready especially after the disaster of our not-lunch."

    "A third minute passes. He's not here."

    "The tension is killing me. It's not like I've ever counted the seconds between him getting off the bus and getting up here before."

    "But today is different. It's our fifth wedding anniversary."

    "We've been together for about eight years altogether but we never really took our anniversary seriously until after the wedding."

    "..."

    "It's been all of five minutes. I'm a bit worried."

    "My smile drops a bit and I walk toward the door."

    "I hear a bit of muffled talking in the hall, and a couple sets of footsteps approaching."

    show wolfrick at flip

    voice "voice/2-romance/001.opus"
    na "{size=-12}...and I know things have been rough, so I don't mind at all.{/size}"

    show wolfrick reverse at reverse

    ni "{size=-11}I just don't want to be a burden to you both, but if you're sure…{/size}"

    voice "voice/2-romance/003.opus"
    na "{size=-10}Nonsense. Just let me talk to him, he'll understand.{/size}"

    ni "{size=-9}Thank you. Should I… wait out here?{/size}"

    voice "voice/2-romance/005.opus"
    na "{size=-8}Mmmmm… maybe not. It's not like you two haven't met before."

    show wolfrick at walk_to(8.5)

    "Nate is speaking to a person with a familiar voice."

    show wolfrick:
        x0_85
        parallel:
            hug_right(0.5)
        parallel:
            pause 0.5
            function add_attributes(['face_shocked'])

    play sound 'audio/effects/door_open.ogg'

    "I open the front door and see them standing at the door with several bags of luggage."

    show wolfrick face_shocked at no_offset

    "As I look toward the bags of luggage and back up to Nate, he gives me an apologetic expression."

    show wolfrick face_concerned

    "I look to see the person standing next to Nate - his cousin, Nic."

    show wolfrick face_stern

    "Looking back to Nate, he puts on a smile."

    voice "voice/2-romance/006.opus"
    na "Happy anniversary… my love?"

    show wolfrick:
        shake()
        pause 0.2
        slow_nod()
        pause 0.2
        function add_attributes(['face_happy'])
        quick_nod(2)

    "I shake my head and sigh, chuckling."

    show wolfrick at no_offset

    voice "voice/2-romance/007.opus"
    w "Happy anniversary."

    show wolfrick face_stern

    "I turn toward Nic."

    show wolfrick face_concerned

    voice "voice/2-romance/008.opus"
    w "Hey, Nic. Moving in?"

    ni "H-hey. If it's alright with you, yeah. I… broke up with Zephyr. He kicked me out."

    show wolfrick face_happy

    voice "voice/2-romance/010.opus"
    w "Woah, that's great news!"

    show wolfrick face_stern:
        pause 0.7
        parallel:
            push_left(distance=10)
        parallel:
            pause 0.05
            function add_attributes(['face_shocked'])

    play sound 'audio/effects/hit_body.ogg'

    "I feel a slap on my arm."

    show wolfrick at no_offset

    voice "voice/2-romance/011.opus"
    na "Wolfrick! No, bad!"

    show wolfrick face_concerned

    voice "voice/2-romance/012.opus"
    w "What? You didn't like him either, we should be celebrating!"

    "Nic looks off to the side for a moment, and Nate pinches the bridge of his nose."

    "Nate puts a hand on Nic's shoulder."

    voice "voice/2-romance/013.opus"
    na "We'll just… be a moment."

    show wolfrick:
        walk_out_right()
    scene bg apartment_corner with dissolve
    show nate accessories_glasses accessories_hat_bucket shirt_chill pants_chill shirt_hoodie at y1:
        walk_in_right(9)
        pause 0.1
        push_right
        pause 0.1
        walk_to(7.5, 0.8, 1)
    show wolfrick -reverse accessories_glasses accessories_watch pants_joggers shirt_joggers at y1:
        walk_in_right(4, 1.2)

    "Nic nods and Nate ushers me inside, closing the door."

    show nate:
        x0_75
        no_offset
        push_left()
    show wolfrick:
        x0_4
        no_offset
        pause 0.1
        push_left(distance=10)
        flip()

    "He slaps my arm again."

    show nate at no_offset
    show wolfrick reverse face_concerned at no_offset, reverse

    voice "voice/2-romance/014.opus"
    w "Ow! Quit it!"

    show nate face_angry

    voice "voice/2-romance/015.opus"
    na "What is {i}wrong{/i} with you?! He's dealing with a lot right now."

    show wolfrick face_sad

    voice "voice/2-romance/016.opus"
    w "S-sorry, I was just surprised by - and happy for - the news! That guy sucked, Nate!"

    voice "voice/2-romance/017.opus"
    na "Regardless of that, seriously? Please try to have {i}at least{/i} a modicum of tact, Wolfrick!"

    voice "voice/2-romance/018.opus"
    na "Sometimes, I swear you can't hear yourself."

    show wolfrick:
        slow_nod()
        quick_nod()
        pause 0.2
        quick_shake(1)

    "I sigh and nod, shrugging."

    show wolfrick face_concerned at no_offset

    voice "voice/2-romance/019.opus"
    w "Yeah, you're right. I'll be more considerate of his emotions."

    show nate:
        nod()
        pause 0.2
        walk_to(6.5, 0.8, 1)

    show nate face_neutral

    "Nate nods, and moves closer."

    voice "voice/2-romance/020.opus"
    na "Wolfrick, please just apologize to him and then let's talk about him staying here for a bit?"

    show nate:
        pause 0.3
        walk_to(9)
    show wolfrick face_stern:
        nod()
        pause 0.2
        walk_to(7, 2)

    "I nod and we move back over to the door."

    show nate at x0_9:
        no_offset
        push_right()
        pause 0.2
        walk_out_right()
    show wolfrick at x0_7:
        no_offset
        pause 0.5
        walk_out_right(1.4)
    scene bg apartment_dining with dissolve
    show nic pants_chill shirt_chill face_sad at y1, x0_9
    play sound 'audio/effects/door_open.opus'

    "Nate opens it and Nic is leaning against the wall across the hall."

    show wolfrick accessories_glasses accessories_watch pants_joggers shirt_joggers at y1:
        walk_in_right(6)
        flip()

    "I motion for Nate to move out of the way and step in front of Nic."

    show wolfrick reverse:
        reset_pos(6)
        reverse
    show nic face_concerned

    "He sheepishly smiles, lifting his brows into a concerned expression."

    show wolfrick at hug_right

    "I put my hand on his shoulder and look him in the eyes."

    show wolfrick face_concerned at no_offset

    voice "voice/2-romance/021.opus"
    w "Look, I'm sorry Nic."

    voice "voice/2-romance/022.opus"
    w "I know you're hurting and that you have a lot of emotions to work through."

    voice "voice/2-romance/023.opus"
    w "We'd be more than happy to have you here while you get back on your feet!"

    voice "voice/2-romance/024.opus"
    w "We have a spare bedroom, and you're welcome to it."

    ni "Oh, that's… are you sure? I know this is sudden and I don't want to step on your toes…"

    voice "voice/2-romance/026.opus"
    na "Nonsense, you're family and you're in need."

    show wolfrick face_happy

    "I smile at Nate and lift up as many of the bags of luggage as I can."

    show wolfrick face_stern

    "Nic is holding a bag, and Nate has another one. I am carrying the other three."

    show wolfrick at walk_out_right
    show nic at walk_out_right

    "We move everything into the apartment and I lead Nic to the room."

    scene bg apartment_bedroom_spare with dissolve

    voice "voice/2-romance/027.opus"
    w "Here we are."

    voice "voice/2-romance/028.opus"
    na "We use it for extra storage."

    voice "voice/2-romance/029.opus"
    na "It's only got a few boxes in the corner but there's a twin bed and more than enough room."

    show nic face_sad pants_chill shirt_chill:
        y1
        x1_3
        pause 2
        walk_in_right(1, 2)
        pause 0.1
        slow_nod()
        pause 0.1
        flip()
        pause 0.1
        walk_to(2)
        pause 0.1
    show nate accessories_glasses accessories_hat_bucket shirt_chill pants_chill shirt_hoodie:
        y1
        x1_3
        walk_in_right(1, 2)
        pause 0.1
        slow_nod()
        pause 0.1
        flip()
        pause 0.1
        walk_to(8.5, steps=4)
        pause 0.2
        flip_back()
    show wolfrick accessories_glasses accessories_watch pants_joggers shirt_joggers:
        y1
        x1_3
        pause 1
        walk_in_right(1, 2)
        pause 0.1
        slow_nod()
        pause 0.1
        flip()
        pause 0.1
        walk_to(5.5, 1.2)
        pause 0.5
        flip_back()

    "I open the door, and lead the others inside. We leave Nic's luggage on the far side of the room and I move back to the doorway."

    show nic reverse:
        no_offset
        x0_2
        reverse
    show nate:
        no_offset
        x0_85
    show wolfrick:
        no_offset
        x0_55

    voice "voice/2-romance/030.opus"
    w "We have spare blankets and pillows inside one of those boxes..."

    voice "voice/2-romance/031.opus"
    w "We can wash them if they're too dusty."

    voice "voice/2-romance/032.opus"
    w "Just let us know!"

    voice "voice/2-romance/033.opus"
    na "Feel free to come get me if you need help unpacking!"

    voice "voice/2-romance/034.opus"
    na "I'm just going to go talk with Wolfrick, okay Nic?"

    ni "Y-yes. Thank you both, this is great! I'll just try to stay out of the way."

    voice "voice/2-romance/036.opus"
    na "Nonsense, you're more than welcome! Just try to relax and process your feelings for now."

    show nic at nod
    show nate:
        flip()
        walk_to(9, 1, 1)
    show wolfrick:
        pause 0.5
        flip()
        walk_to(6.5, 1, 1)

    "Nic nods and Nate nears the doorway."

    show nate:
        x0_9
        reverse
        flip_back()
        pause 0.1
        function add_attributes(['face_happy'])
        pause 0.7
        function remove_attributes(['face_happy'])
        flip()
        walk_out_right()
    show wolfrick:
        x0_65
        reverse
        pause 0.65
        function add_attributes(['face_happy'])
        pause 0.7
        function remove_attributes(['face_happy'])
        walk_out_right(2.3)

    "He turns to smile at me and I smile back, as we head out into the living room."

    scene bg apartment_couch with dissolve
    show nate accessories_glasses accessories_hat_bucket shirt_chill pants_chill shirt_hoodie:
        y1
        x1_3
        pause 1
        walk_in_right(5)
    show wolfrick accessories_glasses accessories_watch pants_joggers shirt_joggers:
        y1
        walk_in_right(2)
        flip()

    "Nate closes Nic's door and we move to the opposite end of the room."

    show nate at x0_5, no_offset
    show wolfrick reverse at x0_2, no_offset, reverse

    voice "voice/2-romance/037.opus"
    w "So, want to explain what happened? How did this all come to fruition?"

    voice "voice/2-romance/038.opus"
    na "Well, I was closing up the flower shop…"

    voice "voice/2-romance/039.opus"
    w "Yeah?"

    voice "voice/2-romance/040.opus"
    na "...and then I saw Nic dragging his luggage over toward it from the bus stop…"

    voice "voice/2-romance/041.opus"
    na "He told me what he told you, about Zephyr."

    voice "voice/2-romance/042.opus"
    na "I asked him if he had a place to stay or if he was just booted out onto the streets."

    voice "voice/2-romance/043.opus"
    w "Go on…"

    voice "voice/2-romance/044.opus"
    na "He told me Zephyr wouldn't let him get his portion of their money from the ATM with their card."

    voice "voice/2-romance/045.opus"
    na "Can you believe that?"

    show wolfrick at quick_nod

    "I scoff."

    voice "voice/2-romance/046.opus"
    w "What a scrub. I bet Nic's ‘portion' makes up a hundred percent of the money in that account."

    "Zephyr has never been well-received by anyone in Nic's immediate family, and honestly for good reason."

    show nate at slow_nod

    "Suddenly, Nate's sniffing the air."

    voice "voice/2-romance/047.opus"
    na "...Uh, do you smell fish?"

    "Oh, yeah. I forgot all about the dinner."

    show wolfrick at push_right

    "I point over toward the romantic display sitting just fifteen feet away."

    voice "voice/2-romance/048.opus"
    w "I made dinner, I was going to surprise you with your favorite for our anniversary."

    voice "voice/2-romance/049.opus"
    na "O-oh. Wolfrick, that's… so sweet."

    voice "voice/2-romance/050.opus"
    na "I'm so sorry, I didn't even consider you might have done something like this and now…"

    voice "voice/2-romance/051.opus"
    w "It's alright. I know it would be awkward and kind of rude to continue this while Nic is here."

    voice "voice/2-romance/052.opus"
    w "I'll ditch the candles and re-portion it to three plates and offer some to him."

    voice "voice/2-romance/053.opus"
    na "I'm sorry again, and thank you, Wolfrick."

    show nate at hug_left

    "Nate leans in and kisses me on the cheek."

    $ set_chapter_progress(3)

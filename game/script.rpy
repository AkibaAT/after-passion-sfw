define na = Character(None, image="Nathan", kind=bubble, callback=speaker("Nathan"))
define ni = Character(None, image="Nic", kind=bubble, callback=speaker("Nic"))
define w = Character(None, image="Wolfrick", kind=bubble, callback=speaker("Wolfrick"))

label start:

    scene bg apartment
    show nic face_sad pants_chill accessories_hat shirt_chill at x0_25
    show nic at y1
    show nic at reverse
    show nate pants_chill shirt_chill at x0_8
    show nate at y1
    show wolfrick shirt_formal pants_formal body_crossed face_sad at center

    ni "Go on... tell him."
    show wolfrick at flip

    w "Nathan... I... am really sorry that I stepped on your hat."
    w "Nathan... I... am really sorry that I stepped on your hat."
    w "Nathan... I... am really sorry that I stepped on your hat."
    w "Nathan... I... am really sorry that I stepped on your hat."

    show wolfrick face_neutral body_chill at reverse

    na "Ooooh, Wolfrick, my boy. I appreciate it, but it's just a leaf."

    show nic face_neutral

    na "I can simply grab a new one. It's no big deal, really."

    show nate at slow_nod

    "Bending down, Nathan picks up a brand new leaf."

    show nate accessories_hat
    show wolfrick face_happy

    na "There we go, good as new!"

    pause

    return

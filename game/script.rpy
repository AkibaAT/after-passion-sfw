define na = Character(None, image="nathan", kind=bubble)
define ni = Character(None, image="nic", kind=bubble)
define w = Character(None, image="wolfrick", kind=bubble)

label start:

    scene bg apartment
    show nic face_sad pants_chill accessories_hat shirt_chill at x0_25
    show nic at y1
    show nic at reverse
    show nate pants_chill shirt_chill at x0_8
    show nate at y1
    show wolfrick shirt_formal pants_formal body_crossed at center

    ni "Go on... tell him."
    show wolfrick at flip

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

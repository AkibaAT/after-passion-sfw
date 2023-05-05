init -1 python:
    def combineDisplay(layer_1, layer_2):
        return Composite((0, 0), (0, 0), layer_1, (0, 0), layer_2)

define na = Character(None, image="Nate", kind=bubble, callback=speaker("Nate"))
define ni = Character(None, image="Nic", kind=bubble, callback=speaker("Nic"))
define w = Character(None, image="Wolfrick", kind=bubble, callback=speaker("Wolfrick"))

label start:

    scene bg apartment
    show nic pants_chill accessories_hat shirt_chill at x0_25
    show nic at y1
    show nic at reverse
    show nate pants_chill shirt_chill accessories_glasses hat_leaf at x0_8
    show nate at y1
    show wolfrick shirt_formal pants_formal accessories_glasses body_chill at center

    pause
    ni "This text is a bit longer to test the talking animation."
    show wolfrick face_neutral at flip

    w "This text is a bit longer to test the talking animation."

    show wolfrick face_neutral body_chill at reverse

    na "This text is a bit longer to test the talking animation."

    show nic face_neutral

    na "I can simply grab a new one. It's no big deal, really."

    show nate at slow_nod

    "Bending down, Nathan picks up a brand new leaf."

    show nate accessories_hat
    show wolfrick face_happy

    na "There we go, good as new!"

    pause

    return

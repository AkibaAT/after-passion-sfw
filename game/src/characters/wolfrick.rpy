init -1 python:
    # Combine two displayables.
    def combineDisplay(background_d, foreground_d):
        return Composite((0, 0), (0, 0), background_d, (0, 0), foreground_d)

layeredimage wolfrick:
    xanchor 0.5
    yanchor 1.0
    yoffset 340

    group body auto prefix "body":
        attribute chill default
    group face auto prefix "face":
        attribute neutral default:
            speakAnim("Wolfrick", combineDisplay("wolfrick_face_neutral", "wolfrick_speak"), combineDisplay("wolfrick_face_neutral", "wolfrick_blink"))
        attribute angry:
            combineDisplay("wolfrick_face_angry", "wolfrick_blink")
        attribute concerned:
            speakAnim("Wolfrick", combineDisplay("wolfrick_face_concerned", "wolfrick_speak"), combineDisplay("wolfrick_face_concerned", "wolfrick_blink_big"))
        attribute embarrassed:
            speakAnim("Wolfrick", combineDisplay("wolfrick_face_embarrassed", "wolfrick_speak"), combineDisplay("wolfrick_face_embarrassed", "wolfrick_blink_big"))
        attribute sad:
            speakAnim("Wolfrick", combineDisplay("wolfrick_face_sad", "wolfrick_speak"), combineDisplay("wolfrick_face_sad", "wolfrick_blink_sad"))
        attribute shocked:
            combineDisplay("wolfrick_face_shocked", "wolfrick_blink_big")
    group accessories auto prefix "accessories"
    group pants auto prefix "pants"
    group shirt if_any ["body_chill"] auto prefix "shirt" variant "chill"
    group shirt if_any ["body_crossed"] auto prefix "shirt" variant "crossed"

image wolfrick_speak:
    alpha 0
    .2
    alpha 1
    "wolfrick_mouth_open"
    .2
    repeat

image wolfrick_blink:
    alpha 0
    pause renpy.random.randint(2, 5)
    alpha 1
    "wolfrick_eyes_half"
    .016
    "wolfrick_eyes_closed"
    .18
    "wolfrick_eyes_half"
    .016
    repeat

image wolfrick_blink_big:
    alpha 0
    pause renpy.random.randint(2, 5)
    alpha 1
    "wolfrick_eyes_big_half"
    .016
    "wolfrick_eyes_big_closed"
    .18
    "wolfrick_eyes_big_half"
    .016
    repeat

image wolfrick_blink_sad:
    alpha 0
    pause renpy.random.randint(2, 5)
    alpha 1
    "wolfrick_eyes_sad_half"
    .016
    "wolfrick_eyes_sad_closed"
    .18
    "wolfrick_eyes_sad_half"
    .016
    repeat

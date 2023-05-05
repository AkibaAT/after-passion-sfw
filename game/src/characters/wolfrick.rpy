define w = Character(None, image="Wolfrick", kind=bubble, callback=speaker("Wolfrick"))

layeredimage wolfrick:
    xanchor 0.5
    yanchor 1.0
    yoffset 340

    group body auto prefix "body":
        attribute chill default
    group face auto prefix "face":
        attribute neutral default:
            speakAnim("Wolfrick", combineDisplay("wolfrick_face_neutral_blinking", "wolfrick_speak"), "wolfrick_face_neutral_blinking")
        attribute angry:
            "wolfrick_face_angry_blinking"
        attribute concerned:
            speakAnim("Wolfrick", combineDisplay("wolfrick_face_concerned_blinking", "wolfrick_speak"), "wolfrick_face_concerned_blinking")
        attribute embarrassed:
            speakAnim("Wolfrick", combineDisplay("wolfrick_face_embarrassed_blinking", "wolfrick_speak"), "wolfrick_face_embarrassed_blinking")
        attribute sad:
            speakAnim("Wolfrick", combineDisplay("wolfrick_face_sad_blinking", "wolfrick_speak"), "wolfrick_face_sad_blinking")
        attribute shocked:
            "wolfrick_face_shocked_blinking"
    group accessories auto prefix "accessories"
    group pants auto prefix "pants"
    group shirt if_any ["body_chill"] auto prefix "shirt" variant "chill"
    group shirt if_any ["body_crossed"] auto prefix "shirt" variant "crossed"

image wolfrick_face_neutral_blinking = combineDisplay("wolfrick_face_neutral", "wolfrick_blink")
image wolfrick_face_angry_blinking = combineDisplay("wolfrick_face_angry", "wolfrick_blink")
image wolfrick_face_concerned_blinking = combineDisplay("wolfrick_face_concerned", "wolfrick_blink_big")
image wolfrick_face_embarrassed_blinking = combineDisplay("wolfrick_face_embarrassed", "wolfrick_blink_big")
image wolfrick_face_sad_blinking = combineDisplay("wolfrick_face_sad", "wolfrick_blink_sad")
image wolfrick_face_shocked_blinking = combineDisplay("wolfrick_face_shocked", "wolfrick_blink_big")

image wolfrick_speak:
    alpha 0
    .2
    alpha 1
    "wolfrick_mouth_open"
    .2
    repeat

image wolfrick_blink:
    alpha 0
    choice:
        5.0
    choice:
        2.2
    choice:
        4.5
    choice:
        0.4
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
    choice:
        5.0
    choice:
        2.2
    choice:
        4.5
    choice:
        0.4
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
    choice:
        5.0
    choice:
        2.2
    choice:
        4.5
    choice:
        0.4
    alpha 1
    "wolfrick_eyes_sad_half"
    .016
    "wolfrick_eyes_sad_closed"
    .18
    "wolfrick_eyes_sad_half"
    .016
    repeat

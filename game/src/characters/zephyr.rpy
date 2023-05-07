define z = Character(None, image="Zephyr", kind=bubble, callback=speaker("Zephyr"))

layeredimage zephyr:
    xanchor 0.5
    yanchor 1.0
    yoffset 340

    attribute reverse null

    group body auto prefix "body":
        attribute chill default
    group face auto prefix "face":
        attribute neutral default:
            speakAnim("Zephyr", combineDisplay("zephyr_face_neutral_blinking", "zephyr_speak"), "zephyr_face_neutral_blinking")
        attribute angry:
            "zephyr_face_angry_blinking"
        attribute concerned:
            speakAnim("Zephyr", combineDisplay("zephyr_face_concerned_blinking", "zephyr_speak"), "zephyr_face_concerned_blinking")
        attribute embarrassed:
            speakAnim("Zephyr", combineDisplay("zephyr_face_embarrassed_blinking", "zephyr_speak"), "zephyr_face_embarrassed_blinking")
        attribute sad:
            speakAnim("Zephyr", combineDisplay("zephyr_face_sad_blinking", "zephyr_speak"), "zephyr_face_sad_blinking")
        attribute shocked:
            "zephyr_face_shocked_blinking"
    group pants auto prefix "pants"
    group shirt if_any ["body_chill"] auto prefix "shirt" variant "chill"
    group shirt if_any ["body_crossed"] auto prefix "shirt" variant "crossed"

image zephyr_face_neutral_blinking = combineDisplay("zephyr_face_neutral", "zephyr_blink")
image zephyr_face_angry_blinking = combineDisplay("zephyr_face_angry", "zephyr_blink")
image zephyr_face_concerned_blinking = combineDisplay("zephyr_face_concerned", "zephyr_blink_big")
image zephyr_face_embarrassed_blinking = combineDisplay("zephyr_face_embarrassed", "zephyr_blink_big")
image zephyr_face_sad_blinking = combineDisplay("zephyr_face_sad", "zephyr_blink_sad")
image zephyr_face_shocked_blinking = combineDisplay("zephyr_face_shocked", "zephyr_blink_big")

image zephyr_speak:
    alpha 0
    .2
    alpha 1
    "zephyr_mouth_open"
    .2
    repeat

image zephyr_blink:
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
    "zephyr_eyes_half"
    .016
    "zephyr_eyes_closed"
    .18
    "zephyr_eyes_half"
    .016
    repeat

image zephyr_blink_big:
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
    "zephyr_eyes_big_half"
    .016
    "zephyr_eyes_big_closed"
    .18
    "zephyr_eyes_big_half"
    .016
    repeat

image zephyr_blink_sad:
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
    "zephyr_eyes_sad_half"
    .016
    "zephyr_eyes_sad_closed"
    .18
    "zephyr_eyes_sad_half"
    .016
    repeat

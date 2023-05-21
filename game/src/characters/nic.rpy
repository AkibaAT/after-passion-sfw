define ni = Character(None, image="Nic", kind=bubble, callback=speaker("Nic"), voice_tag="nic")

layeredimage nic:
    xanchor 0.5
    yanchor 1.0
    yoffset 340

    attribute reverse null

    always:
        "nic_body_chill"

    group face auto prefix "face":
        attribute neutral default:
            speakAnim("Nic", combineDisplay("nic_face_neutral_blinking", "nic_speak"), "nic_face_neutral_blinking")
        attribute concerned:
            speakAnim("Nic", combineDisplay("nic_face_concerned_blinking", "nic_speak"), "nic_face_concerned_blinking")
        attribute angry:
            speakAnim("Nic", combineDisplay("nic_face_angry_blinking", "nic_speak"), "nic_face_angry_blinking")
        attribute sad:
            speakAnim("Nic", combineDisplay("nic_face_sad_blinking", "nic_speak"), "nic_face_sad_blinking")
        attribute shocked:
            speakAnim("Nic", combineDisplay("nic_face_shocked_blinking", "nic_speak"), "nic_face_shocked_blinking")
    group accessories auto prefix "accessories"
    group pants auto prefix "pants"
    group shirt auto prefix "shirt"

image nic_face_neutral_blinking = combineDisplay("nic_face_neutral", "nic_blink_concerned")
image nic_face_concerned_blinking = combineDisplay("nic_face_concerned", "nic_blink_concerned")
image nic_face_angry_blinking = combineDisplay("nic_face_angry", "nic_blink_angry")
image nic_face_sad_blinking = combineDisplay("nic_face_sad", "nic_blink_sad")
image nic_face_shocked_blinking = combineDisplay("nic_face_shocked", "nic_blink_shocked")

image nic_speak:
    alpha 0
    .2
    alpha 1
    "nic_mouth_open"
    .2
    repeat

image nic_blink_concerned:
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
    "nic_eyes_concerned_half"
    .016
    "nic_eyes_concerned_closed"
    .18
    "nic_eyes_concerned_half"
    .016
    repeat

image nic_blink_angry:
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
    "nic_eyes_angry_half"
    .016
    "nic_eyes_angry_closed"
    .18
    "nic_eyes_angry_half"
    .016
    repeat

image nic_blink_sad:
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
    "nic_eyes_sad_half"
    .016
    "nic_eyes_sad_closed"
    .18
    "nic_eyes_sad_half"
    .016
    repeat

image nic_blink_shocked:
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
    "nic_eyes_shocked_half"
    .016
    "nic_eyes_shocked_closed"
    .18
    "nic_eyes_shocked_half"
    .016
    repeat

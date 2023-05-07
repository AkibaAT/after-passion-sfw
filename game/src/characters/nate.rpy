define na = Character(None, image="Nate", kind=bubble, callback=speaker("Nate"))

layeredimage nate:
    xanchor 0.5
    yanchor 1.0
    yoffset 340

    attribute reverse null
    attribute eyes_half null

    always:
        "nate_body_chill"

    group face if_not ["eyes_half"] auto prefix "face":
        attribute neutral default:
            speakAnim("Nate", combineDisplay("nate_face_neutral_blinking", "nate_speak"), "nate_face_neutral_blinking")
        attribute angry:
            speakAnim("Nate", combineDisplay("nate_face_angry_blinking", "nate_speak_reverse"), "nate_face_angry_blinking")
        attribute concerned:
            speakAnim("Nate", combineDisplay("nate_face_concerned_blinking", "nate_speak_reverse"), "nate_face_concerned_blinking")
        attribute happy:
            speakAnim("Nate", combineDisplay("nate_face_happy_blinking", "nate_speak_reverse"), "nate_face_happy_blinking")
        attribute sad:
            speakAnim("Nate", combineDisplay("nate_face_sad_blinking", "nate_speak_reverse"), "nate_face_sad_blinking")
    group face if_any ["eyes_half"] auto prefix "face":
        attribute neutral default:
            speakAnim("Nate", combineDisplay("nate_face_neutral_blinking_half", "nate_speak"), "nate_face_neutral_blinking_half")
        attribute angry:
            speakAnim("Nate", combineDisplay("nate_face_angry_blinking_half", "nate_speak_reverse"), "nate_face_angry_blinking_half")
        attribute concerned:
            speakAnim("Nate", combineDisplay("nate_face_concerned_blinking_half", "nate_speak_reverse"), "nate_face_concerned_blinking_half")
        attribute happy:
            speakAnim("Nate", combineDisplay("nate_face_happy_blinking_half", "nate_speak_reverse"), "nate_face_happy_blinking_half")
        attribute sad:
            speakAnim("Nate", combineDisplay("nate_face_sad_blinking_half", "nate_speak_reverse"), "nate_face_sad_blinking_half")
    group accessories auto prefix "accessories" multiple
    group pants auto prefix "pants"
    group shirt auto prefix "shirt" multiple:
        attribute chill:
            "nate_shirt_chill"
        attribute overall if_all "reverse":
            "nate_reverse_shirt_overall"
        attribute overall if_not "reverse":
            "nate_shirt_overall"

image nate_face_neutral_blinking = combineDisplay("nate_face_neutral", "nate_blink")
image nate_face_angry_blinking = combineDisplay("nate_face_angry", "nate_blink")
image nate_face_concerned_blinking = combineDisplay("nate_face_concerned", "nate_blink")
image nate_face_happy_blinking = combineDisplay("nate_face_happy", "nate_blink")
image nate_face_sad_blinking = combineDisplay("nate_face_sad", "nate_blink")

image nate_face_neutral_blinking_half = combineDisplay("nate_face_neutral", "nate_blink_half")
image nate_face_angry_blinking_half = combineDisplay("nate_face_angry", "nate_blink_half")
image nate_face_concerned_blinking_half = combineDisplay("nate_face_concerned", "nate_blink_half")
image nate_face_happy_blinking_half = combineDisplay("nate_face_happy", "nate_blink_half")
image nate_face_sad_blinking_half = combineDisplay("nate_face_sad", "nate_blink_half")

image nate_speak:
    alpha 0
    .2
    alpha 1
    "nate_mouth_open"
    .2
    repeat

image nate_speak_reverse:
    alpha 0
    .2
    alpha 1
    "nate_mouth_closed"
    .2
    repeat

image nate_blink:
    alpha 0
    choice:
        5.0
    choice:
        2.2
    choice:
        4.5
    alpha 1
    "nate_eyes_half"
    .016
    "nate_eyes_open"
    .18
    "nate_eyes_half"
    .016
    repeat

image nate_blink_half:
    "nate_eyes_half"
    choice:
        5.0
    choice:
        2.2
    choice:
        4.5
    alpha 1
    .016
    alpha 0
    .18
    alpha 1
    .016
    repeat

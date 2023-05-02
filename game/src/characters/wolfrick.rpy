layeredimage wolfrick:
    xanchor 0.5
    yanchor 1.0
    yoffset 340

    group body auto prefix "body":
        attribute chill default
    group face auto prefix "face"
    group accessories auto prefix "accessories"
    group pants auto prefix "pants"
    group shirt if_any ["body_chill"] auto prefix "shirt" variant "chill"
    group shirt if_any ["body_crossed"] auto prefix "shirt" variant "crossed"

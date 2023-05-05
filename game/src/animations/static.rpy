init -1 python:
    def combineDisplay(layer_1, layer_2):
        return Composite((0, 0), (0, 0), layer_1, (0, 0), layer_2)

transform pick_up:
    easein .04 yoffset -20
    easeout .05 yoffset 0

transform nod(repeatCount=1, speed=0.3, height=20):
    easein speed/2 yoffset height
    easeout speed/2 yoffset 0
    repeat repeatCount

transform quick_nod(repeatCount=1):
    nod(repeatCount, 0.2, 20)

transform slow_nod(repeatCount=1):
    nod(repeatCount, 0.6, 30)

transform shake(repeatCount=1, speed=0.72, distance=18):
    easein speed / 4 xoffset distance * -1
    easeout speed / 4 xoffset 0
    easein speed / 4 xoffset distance
    easeout speed / 4 xoffset 0
    repeat repeatCount

transform quick_shake(repeatCount=3):
    shake(repeatCount, 0.2, 10)

transform push_left(repeatCount=1, distance=20):
    easein .12 xoffset distance * -1
    easeout .16 xoffset 0
    repeat repeatCount

transform push_right(repeatCount=1, distance=20):
    easein .12 xoffset distance
    easeout .16 xoffset 0
    repeat repeatCount

transform hug_left(hold=1.0, speed=0.5, distance=25):
    easein speed/2 xoffset distance * -1
    pause hold
    easeout speed/2 xoffset 0

transform hug_right(hold=1.0, speed=0.5, distance=25):
    easein speed/2 xoffset distance
    pause hold
    easeout speed/2 xoffset 0

transform flip(speed=0.5):
    xzoom 1.0
    linear speed xzoom -1.0

transform flip_back(speed=0.5):
    xzoom -1.0
    linear speed xzoom 1.0

transform static_walk(repeatCount=3, speed=1.2):
    ease speed/(repeatCount * 2) yoffset -20
    ease speed/(repeatCount * 2) yoffset 0
    repeat repeatCount

transform fade_in(speed=1.0):
    alpha 0.0
    function flatten_child
    linear speed alpha 1.0

transform fade_to(transp=0.5, speed=1.0):
    function flatten_child
    linear speed alpha transp

transform fade_out(speed=1.0):
    alpha 1.0
    function flatten_child
    linear speed alpha 0.0

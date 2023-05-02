init -99 python:
    def flatten_child(trans, st, at):
        """Flattens the ATL Transform child and sets it."""
        flatten = Flatten(trans.child)
        trans.set_child(flatten)
        return None

transform walk_in_left(x=2.0, speed=1.2):
    function flatten_child
    xpos -0.1
    alpha 0
    parallel:
        linear speed/2 alpha 1.0
    parallel:
        easein speed xpos x/10
    parallel:
        static_walk(2, speed)

transform walk_in_right(x=8.0, speed=1.2):
    alpha 0
    xpos 1.1
    function flatten_child
    parallel:
        linear speed/2 alpha 1.0
    parallel:
        easein speed xpos x/10
    parallel:
        static_walk(2, speed)

transform walk_out_left(speed=1.2):
    function flatten_child
    parallel:
        pause speed/2
        linear speed/2 alpha 0.0
    parallel:
        easeout speed xoffset -400
    parallel:
        static_walk(2, speed)

transform walk_out_right(speed=1.2):
    function flatten_child
    parallel:
        pause speed/4
        linear speed/2 alpha 0.0
    parallel:
        easeout speed xoffset 400
    parallel:
        static_walk(2, speed)

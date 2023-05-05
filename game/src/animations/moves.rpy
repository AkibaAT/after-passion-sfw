init -99 python:
    def flatten_child(trans, st, at):
        """Flattens the ATL Transform child and sets it."""
        flatten = Flatten(trans.child)
        trans.set_child(flatten)
        return None

transform walk_in_left(x=2.0, speed=1.2):
    function flatten_child
    xpos -0.3
    parallel:
        easein speed xpos x/10
    parallel:
        static_walk(2, speed)

transform walk_in_right(x=8.0, speed=1.2):
    xpos 1.3
    function flatten_child
    parallel:
        easein speed xpos x/10
    parallel:
        static_walk(2, speed)

transform walk_out_left(speed=1.2):
    function flatten_child
    parallel:
        easeout speed xpos -0.3
    parallel:
        static_walk(2, speed)

transform walk_out_right(speed=1.2):
    function flatten_child
    parallel:
        easeout speed xpos 1.3
    parallel:
        static_walk(2, speed)

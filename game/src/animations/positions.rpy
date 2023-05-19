transform x0:
    xpos 0.0

transform x0_05:
    xpos 0.05

transform x0_1:
    xpos 0.1

transform x0_15:
    xpos 0.15

transform x0_2:
    xpos 0.2

transform x0_25:
    xpos 0.25

transform x0_3:
    xpos 0.3

transform x0_35:
    xpos 0.35

transform x0_4:
    xpos 0.4

transform x0_45:
    xpos 0.45

transform x0_5:
    xpos 0.5

transform x0_55:
    xpos 0.55

transform x0_6:
    xpos 0.6

transform x0_65:
    xpos 0.65

transform x0_7:
    xpos 0.7

transform x0_75:
    xpos 0.75

transform x0_8:
    xpos 0.8

transform x0_85:
    xpos 0.85

transform x0_9:
    xpos 0.9

transform x0_95:
    xpos 0.95

transform x1:
    xpos 1.0

transform x1_3:
    xpos 1.3

transform walk_to(x=5, speed=1.5, steps=3):
    parallel:
        easein speed xpos x/10
    parallel:
        static_walk(steps, speed)

transform move_to(x=5, speed=1.0):
    easein speed xpos x/10

transform y0_9:
    ypos 0.9

transform y1:
    ypos 1.0

transform y1_1:
    ypos 1.1

transform y1_2:
    ypos 1.2

transform y1_3:
    ypos 1.3

transform walk_z_back(z=0.8, speed=1.5, steps=2):
    parallel:
        easein speed zoom z
    parallel:
        static_walk(steps, speed)

transform walk_z_center(z=1, speed=1.5, steps=2):
    parallel:
        easein speed zoom z
    parallel:
        static_walk(steps, speed)

transform walk_z_front(z=1.15, speed=1.5, steps=2):
    parallel:
        easein speed zoom z
    parallel:
        static_walk(steps, speed)

transform reverse:
    xzoom -1.0

transform no_reverse:
    xzoom 1.0

transform set_solid(a=1.0):
    alpha a

transform align_x(x):
    offset [0, 0]
    xpos x/10

transform align_y(y):
    offset [0, 0]
    ypos 1.0 + y/10

transform reset_pos(x, y=0, solid=1.0):
    align_y(y)
    align_x(x)
    alpha solid

transform no_offset:
    offset [0, 0]

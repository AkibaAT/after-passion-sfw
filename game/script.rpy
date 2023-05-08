init -1 python:
    def set_chapter_progress(value, force=False):
        if (persistent.chapter_progress < value) or force:
            persistent.chapter_progress = value

default persistent.chapter_progress = 0

label start:
    stop music

    if persistent.chapter_progress == 0:
        call dummy from _call_dummy # This is only here for chapter select to replay the prologue
        call ch0_awakening from _call_ch0_awakening
    call ch1_tension from _call_ch1_tension
    call ch2_romance from _call_ch2_romance
    call ch3_comfort from _call_ch3_comfort
    call ch4_passion from _call_ch4_passion
    call ch5_after_passion from _call_ch5_after_passion

    return

label dummy:
    return

define chapter_list = [
    {'id': 0, 'title': _('0: Awakening, City Streets | 12:05 PM'), 'action': Start('_call_dummy')},
    {'id': 1, 'title': _('1: Tension, Flower Shop | 12:15 PM'), 'action': Start('_call_ch0_awakening')},
    {'id': 2, 'title': _('2: Romance, Apartment | 06:00 PM'), 'action': Start('_call_ch1_tension')},
    {'id': 3, 'title': _('3: Comfort, Apartment | 09:00 PM'), 'action': Start('_call_ch2_romance')},
    {'id': 4, 'title': _('4: Passion, Bedroom | 12:05 AM'), 'action': Start('_call_ch3_comfort')},
    {'id': 5, 'title': _('5: After Passion, Apartment | 9:00 AM'), 'action': Start('_call_ch4_passion')}
]

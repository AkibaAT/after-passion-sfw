init -1 python:

    # This is set to the name of the character that is speaking, or
    # None if no character is currently speaking.
    speaking = []

    # This returns speaking if the character is speaking, and done if the
    # character is not.
    def whileSpeakingCallback(name, speak_d, done_d, st, at):
        if name in speaking:
            return speak_d, .1
        else:
            return done_d, None

    # Curried form of the above.
    whileSpeaking = renpy.curry(whileSpeakingCallback)

    # Displays speaking when the named character is speaking, and done otherwise.
    def speakAnim(name, speaking_d, done_d=Null()):
        return DynamicDisplayable(whileSpeaking(name, speaking_d, done_d))

    # This callback maintains the speaking variable.
    def speakerCallback(name, event, **kwargs):
        global speaking

        if event == "show_done":
            if type(name) is str:
                speaking.append(name)
            if type(name) is list:
                for n in name:
                    speaking.append(n)

        elif event == "slow_done":
            speaking = []

    # Curried form of the same.
    speaker = renpy.curry(speakerCallback)

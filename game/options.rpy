﻿## This file contains options that can be changed to customize your game.
##
## Lines beginning with two '#' marks are comments, and you shouldn't uncomment
## them. Lines beginning with a single '#' mark are commented-out code, and you
## may want to uncomment them when appropriate.


## Basics ######################################################################

## A human-readable name of the game. This is used to set the default window
## title, and shows up in the interface and error reports.
##
## The _() surrounding the string marks it as eligible for translation.

define config.name = _("After Passion")


## Determines if the title given above is shown on the main menu screen. Set
## this to False to hide the title.

define gui.show_name = True


## The version of the game.

#define config.version = "1.0.3"


## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.

define gui.about = _p("""

Writing: Lavan

Sprites: Cody(0rang3)

Sprites Edits: Akiba

CGs: JadenPup

Audio Editing: Ryezun

Sounds: Akiba, Lavan, and Ryezun

Voice Acting Director: Lavan

Voice Acting: Akiba (as Wolfrick and Zephyr), Lavan (as Nic), and Ryezun (as Human, Nate, and Newscaster)

Lead Programmer: Akiba

Programming: Ryezun

Publishing: Akiba


CC By-NC-SA 4.0

Joao Picoito - Heavy Falling Feather

Joao Picoito - Palavras do Silencio

CC BY-NC 4.0

Kai Engel - June

CC By 4.0

Kathrin Klimek

Francesco Biondi - Seduction Jazz

'Guardian Angel' created by Haoran, edited for use.

""")


## A short name for the game used for executables and directories in the built
## distribution. This must be ASCII-only, and must not contain spaces, colons,
## or semicolons.

define build.name = "AfterPassion"


## Sounds and music ############################################################

## These three variables control, among other things, which mixers are shown
## to the player by default. Setting one of these to False will hide the
## appropriate mixer.

define config.has_sound = True
define config.has_music = True
define config.has_voice = True

define config.default_music_volume = 0.9
define config.default_sfx_volume = 0.9
define config.default_voice_volume = 0.9

## To allow the user to play a test sound on the sound or voice channel,
## uncomment a line below and use it to set a sample sound to play.

define config.sample_sound = "effects/city_crowd_sample.opus"
define config.sample_voice = [
    "voice/0-awakening/009.opus",
    "voice/1-tension/004.opus",
    "voice/5-after_passion/077.opus",
    "voice/0-awakening/038.opus",
    "voice/5-after_passion/025.opus"
]
define sample_music = "music/Guardian Angel_sample.opus"

## Uncomment the following line to set an audio file that will be played while
## the player is at the main menu. This file will continue playing into the
## game, until it is stopped or another file is played.

define config.main_menu_music = "music/Guardian Angel.opus"


## Transitions #################################################################
##
## These variables set transitions that are used when certain events occur.
## Each variable should be set to a transition, or None to indicate that no
## transition should be used.

## Entering or exiting the game menu.

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## Between screens of the game menu.

define config.intra_transition = dissolve


## A transition that is used after a game has been loaded.

define swing_horizontal = Swing(delay=0.5, vertical=True, reverse=True, background='#0a0d14', flatten=False)

define config.after_load_transition = swing_horizontal


## Used when entering the main menu after the game has ended.

define config.end_game_transition = None


## A variable to set the transition used when the game starts does not exist.
## Instead, use a with statement after showing the initial scene.


## Window management ###########################################################
##
## This controls when the dialogue window is displayed. If "show", it is always
## displayed. If "hide", it is only displayed when dialogue is present. If
## "auto", the window is hidden before scene statements and shown again once
## dialogue is displayed.
##
## After the game has started, this can be changed with the "window show",
## "window hide", and "window auto" statements.

define config.window = "auto"


## Transitions used to show and hide the dialogue window

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)

transform reset_self(child):
    child
define config.tag_transform = {
    "bg": reset_self
}


## Preference defaults #########################################################

## Controls the default text speed. The default, 0, is infinite, while any other
## number is the number of characters per second to type out.

default preferences.text_cps = 30


## The default auto-forward delay. Larger numbers lead to longer waits, with 0
## to 30 being the valid range.

default preferences.afm_time = 15
default preferences.gl_framerate = 60
default preferences.audio_when_minimized = False


## Save directory ##############################################################
##
## Controls the platform-specific place Ren'Py will place the save files for
## this game. The save files will be placed in:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## This generally should not be changed, and if it is, should always be a
## literal string, not an expression.

define config.save_directory = "AfterPassion-1682801508"


## Icon ########################################################################
##
## The icon displayed on the taskbar or dock.

define config.window_icon = "gui/window_icon.png"


## Build configuration #########################################################
##
## This section controls how Ren'Py turns your project into distribution files.

init python:
    renpy.music.register_channel("ambient", "sfx", True)

    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. If multiple patterns match, the first is
    ## used.
    ##
    ## In a pattern:
    ##
    ## / is the directory separator.
    ##
    ## * matches all characters, except the directory separator.
    ##
    ## ** matches all characters, including the directory separator.
    ##
    ## For example, "*.txt" matches txt files in the base directory, "game/
    ## **.ogg" matches ogg files in the game directory or any of its
    ## subdirectories, and "**.psd" matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**.toml', None)
    build.classify('**.yml', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('cache/**', None)
    build.classify('game/**.rpy', None)
    build.classify('game/images/**.png', None)
    build.classify('game/**.jpg', None)
    build.classify('game/**.mp3', None)
    build.classify('game/**.ogg', None)
    build.classify('game/**.wav', None)

    ## To archive files, classify them as 'archive'.

    build.archive('scripts', 'all')
    build.archive('images', 'all')
    build.archive('videos', 'all')
    build.archive('audio', 'all')

    build.classify('game/**.rpyc', 'scripts')

    build.classify('game/gui/**.png', 'images')
    build.classify('game/gui/fonts/*', 'images')
    build.classify('game/**.avif', 'images')
    build.classify('game/**.webp', 'images')

    build.classify('videos/**.webm', 'videos')

    build.classify('game/**.opus', 'audio')

    ## Files matching documentation patterns are duplicated in a mac app build,
    ## so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')


## A Google Play license key is required to perform in-app purchases. It can be
## found in the Google Play developer console, under "Monetize" > "Monetization
## Setup" > "Licensing".

# define build.google_play_key = "..."


## The username and project name associated with an itch.io project, separated
## by a slash.

define build.itch_project = "akibaokapi/after-passion"

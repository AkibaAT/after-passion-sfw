###############################################################################################################
### WORD COUNTER ##############################################################################################
###############################################################################################################

## Preferences ################################################################################################

# Name of the folder your script files are in, if any (for example: "script/")
define script_folder_path = ""


# A list of equivalent characters that should be counted as one. Given ("x", "y"), "y" will be counted as "x".
# For example, if "ann", "xann", and "nann" should all be considered "ann", write [("ann", "xann"), ("ann", "nann")]
define wordcounter_same = []

# A list of characters who should be hidden from the character statistics. They still contribute to the total file word count.
define wordcounter_hidden = ["extend"]


# Line and word counts for every character (True by default)
define wordcounter_characters = True

# Line and word counts for each .rpy file (True by default)
define wordcounter_files = True

# Line and word counts for every character, within each .rpy file (True by default)
define wordcounter_character_files = True

# Number of menus and available choices in the game
define wordcounter_menu_choices = True


# The old character statistics which only displays line counts (False by default)
define config.lint_character_statistics = False

###############################################################################################################
### The Code ##################################################################################################
###############################################################################################################

init python:

    import collections

    # The main function
    def wordcounter():

        all_stmts = list(renpy.game.script.all_stmts)
        all_stmts.sort(key=lambda n : n.filename)

        charastats = collections.defaultdict(Count)
        filestats = collections.defaultdict(Count)
        filecharastats = {}

        menu_count = 0
        options_count = 0

        for node in all_stmts:
            if isinstance(node, renpy.ast.Say):
                speaker = node.who
                for i in wordcounter_same:
                    if i[1] == speaker:
                        speaker = i[0]
                        break
                filestats[node.filename].add(node.what)
                if node.filename not in filecharastats:
                    filecharastats[node.filename] = collections.defaultdict(Count)
                if speaker not in wordcounter_hidden:
                    charastats[speaker if speaker else 'narrator' ].add(node.what)
                    filecharastats[node.filename][speaker if speaker else 'narrator' ].add(node.what)

            elif isinstance(node, renpy.ast.Menu):
                menu_count += 1
                for l, c, b in node.items:
                    options_count += 1

        if renpy.config.developer and wordcounter_characters:
            print("\n")
            report_character_stats(charastats)

        if renpy.config.developer and wordcounter_files:
            print("\n")
            report_file_stats(filestats)

        if renpy.config.developer and wordcounter_character_files:
            print("\n")
            report_file_chara_stats(filestats, filecharastats)

        if renpy.config.developer and wordcounter_menu_choices:
            print("\n")
            report_menu_stats(menu_count, options_count)

    # This makes sure the above function is actually called whenever you use Lint
    config.lint_hooks.append(wordcounter)

    # The print functions:
    def report_character_stats(charastats, title = True):

        if title:
            print("Character statistics:")

        count_to_char = collections.defaultdict(list)

        for char in charastats:
            count_to_char[charastats[char].blocks].append(char)

        for count, chars in sorted(count_to_char.items(), reverse=True):
            chars.sort()

            if len(chars) == 1:
                start = chars[0] + " has "
                end = humanize(charastats[chars[0]].words)
            elif len(chars) == 2:
                start = chars[0] + " and " + chars[1] + " have "
                end = humanize(charastats[chars[0]].words) + " and " + humanize(charastats[chars[1]].words)
            else:
                start = ", ".join(chars[:-1]) + ", and " + chars[-1] + " have "
                end = ""
                for char in chars[:-1]:
                    end += humanize(charastats[char].words) + ", "
                end += "and " + humanize(charastats[chars[-1]].words)

            print(" * " + start + humanize(count) +
                (" block" if count == 1 else " blocks") + " of dialogue, and " +
                end + " words" + (" each." if len(chars) > 1 else ".") )

    def report_file_stats(filestats):

        print("File statistics:")

        count_to_char = collections.defaultdict(list)

        for file in filestats:
            print(" * [" + file[5+len(script_folder_path):] + "] contains " + humanize(filestats[file].blocks) +
                    " dialogue blocks and " + humanize(filestats[file].words) + " words.")

    def report_file_chara_stats(filestats, filecharastats):

        print("Detailed File statistics:")

        count_to_char = collections.defaultdict(list)

        for file in filestats:
            print("[" + file[5+len(script_folder_path):] + "] contains " + humanize(filestats[file].blocks) +
                    " dialogue blocks and " + humanize(filestats[file].words) + " words:")
            report_character_stats(filecharastats[file], False)
            print("")

    def report_menu_stats(menu_count, options_count):

        print("Menu statistics:")

        print("The game has " + str(menu_count) + " menus, with a total of " + str(options_count) + " possible choices, \nfor an average of " +
        "{:,.2f}".format(options_count and options_count/menu_count or 0) + " choices per menu.")

    # Auxiliary functions directly copied from lint.py - I take no credit for these:
    def humanize(n):
        s = str(n)
        rv = []
        for i, c in enumerate(reversed(s)):
            if i and not (i % 3):
                rv.insert(0, ',')
            rv.insert(0, c)
        return ''.join(rv)

    class Count(object):
        def __init__(self):
            self.blocks = 0
            self.words = 0
            self.characters = 0

        def add(self, s):
            self.blocks += 1
            self.words += len(s.split())
            self.characters += len(s)

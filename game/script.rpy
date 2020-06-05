# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Doctor")
define b = Character("[name]")
define c = Character("Chris")
define d = Character("Bob")
define e = Character("Nurse")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg Clinic

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show a Chris


    # These display lines of dialogue.

    a "Next patient Please"

    b "Yes, on my way!"


    # This ends the game.

    return

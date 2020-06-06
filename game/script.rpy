# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Doctor")
define b = Character("[name]")
define c = Character("Chris")
define d = Character("Bob")
define e = Character("Nurse")
image clinic = "Clinic.jpg"
image doctor = "Doctor.jpg"
define f = Character ("???")
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg Clinic
    with dissolve
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show Doctor
    with dissolve
    show Mysterious Person
    with dissolve

    # These display lines of dialogue.

    a "Next patient Please..."

    "A doctor called. One person stood up and walked towards the examiner's room. The air feels tense. Somber. Melancholic. All of us Infected are getting examined for traces of Oripathy and its progress on our bodies. As we are new patients being admitted, we had to fill out some paperwork."

    "Several patients groaned while they are waiting to be called. Can you blame them? One instance, they are living out their lives doing whatever, the next treated as outcasts by society. Makes you realize what a horrible world we live in."

    f "Mmm. How many new patients today?"

    a "Looks like 12 today, sir."

    f "Alright. Keep up the good work."

    # This ends the game.


    return

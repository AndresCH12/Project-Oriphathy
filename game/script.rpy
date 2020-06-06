define a = Character("Doctor")
define b = Character("[name]")
define c = Character("Chris")
define d = Character("Bob")
define e = Character("Nurse")
image doctor = "Doctor.jpg"
image mperson = "Hellagur.png"
define f = Character ("???")

label start:

    scene bg Clinic
    with dissolve

    show doctor
    with dissolve
    a "Next patient Please..."

    "A doctor called. One person stood up and walked towards the examiner's room. The air feels tense. Somber. Melancholic. All of us Infected are getting examined for traces of Oripathy and its progress on our bodies. As we are new patients being admitted, we had to fill out some paperwork."

    "Several patients groaned while they are waiting to be called. Can you blame them? One instance, they are living out their lives doing whatever, the next treated as outcasts by society. Makes you realize what a horrible world we live in."

    hide doctor
    show mperson
    with dissolve

    f "Mmm. How many new patients today?"

    hide mperson
    show doctor

    a "Looks like 12 today, sir."

    hide doctor
    show mperson

    f "Alright. Keep up the good work."

    hide mperson
    pause

    return

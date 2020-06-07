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

    "Looks like a discussion behind the examiner's room. The door opened up, and out came an elderly man. A long coat with various loose belts drape over this elderly man. A fearsome yet kind appearance, and yet at first glance you can tell this elderly man has seen many conflicts. If anything, the sword he holds at his side is definitely not a decoration."

    show mperson

    f "Oh?"

    "The elderly man glances at me. After a glance, the elderly man pondered for a moment, and simply nodded. With a light bow, the elderly man then left the clinic."

    hide mperson
    with dissolve

    "I looked around after the elderly man left. A few more patients are in the room. Most of them do not appear to be Infected with Oripathy, but if they're here, they definitely are."

    "I looked back at my paperwork that I was in the middle of filling out. There are only a few places left that I need to write in."

    python:
        name = renpy.input("What is your name")
        name = name.strip()

        if not name:
            name = "Protag"

    python:
        age = renpy.input("what is your age?")
        age = age.strip()

        if not age:
            age = "22"

    python:
        gender = renpy.input("What is your gender?")
        gender = gender.strip()

        if not gender:
            gender = "male"
            
    a "Next patient please..."

    b "Yes!"

    pause

    return

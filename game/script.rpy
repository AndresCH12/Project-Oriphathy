default name = "Protag"
default age = 22
default gender = "Male"
default reunion = 0
default rhodesIsland = 0

define a = Character("Doctor")
define b = Character("[name]")
define c = Character("Chris")
define d = Character("Bob")
define e = Character("Nurse")
image doctor = im.Scale("Doctor.png", 700, 700)
image mperson = im.Scale("Hellagur.png", 700, 700)
image clinic = im.Scale("dark_light_clinic.jpg", 1368, 720)
define f = Character ("???")
define g = Character ("Alice")

label start:

    scene clinic
    with fade

    show doctor
    with dissolve

    a "Next patient, please."

    "A doctor called."

    "One person stood up and walked towards the examiner's room."

    "The air feels tense. Somber. Melancholic."

    "All of us Infected are getting examined for traces of Oripathy and its progress on our bodies."

    "As we are new patients being admitted, we had to fill out some paperwork."

    "Several patients groaned while they are waiting to be called."

    "Can you blame them? One instance, they are living out their lives doing whatever, the next treated as outcasts by society."

    "Makes you realize what a horrible world we live in."

    hide doctor
    with dissolve
    show mperson
    with dissolve

    f "Mmm. How many new patients today?"

    hide mperson
    show doctor

    a "Looks like 12 today, sir."

    hide doctor
    show mperson

    f "Alright. Keep up the good work."

    "Looks like a discussion behind the examiner's room."

    "The door opened up, and out came an elderly man. A long coat with various loose belts drape over this elderly man."

    "A fearsome yet kind appearance, and yet at first glance you can tell this elderly man has seen many conflicts."

    "If anything, the sword he holds at his side is definitely not a decoration."

    "The elderly man glances at me."

    f "Oh?"

    "After a glance, the elderly man pondered for a moment, and simply nodded. With a light bow, the elderly man then left the clinic."

    hide mperson
    with dissolve

    "I looked around after the elderly man left."

    "A few more patients are in the room. Most of them do not appear to be Infected with Oripathy, but if they're here, they definitely are."

    "I looked back at my paperwork that I was in the middle of filling out."

    "There are only a few places left that I need to write in."

    python:
        name = renpy.input("What is your name")
        name = name.strip()

        if not name:
            name = "Protag"

    python:
        age = renpy.input("What is your age?")
        age = age.strip()

        if not age:
            age = "22"

    python:
        gender = renpy.input("What is your gender?")
        gender = gender.strip()

        if not gender:
            gender = "male"



    a "Next patient, please."

    b "Yes!"

    "I stood up and headed towards the examiner's room."

    "I had not finished filling out the form when I was called."

    show doctor
    with dissolve

    a "You haven't finished filling out the paperwork? Well, no matter."

    a "Much of what is on that paperwork is for recordkeeping only and isn't that important, anyway."

    a "The world doesn't treat the Infected kindly after all."

    a "*sigh*"

    "The doctor sighed. She's not wrong, though."

    "The moment we become Infected, the entire world turned their back on us."

    a "Alright. First, a blood sample. Your arm, please."

    "Ah, yes. The quintessential blood draw. Who loves them, right? Needles are always fun."

    a "Now, an x-ray."

    "An uncomfortable experience."

    a "Alright. Unsurprisingly, you're a Stage I patient."

    menu:
        "How are you feeling right now?"

        "(Answer Normally).":

                b "I feel fine"

                a "Hmmm."

        "(Answer sarcastically).":

                b "To what? The fact that I am an Infected?"

                a "..."

    a "Alright, you're good to go."

    a "But before that, do you have any questions?"

    label oripathy_dialog:
    menu:
        "What is Oripathy?":

                a "You don't know? What kind of rock were you living under?"

                "I can't blame her for answering this way. Oripathy is common knowledge, after all."

                a "Oripathy is the name of the disease that you have. This is caused by being in too much contact with a crystallized black mineral known as Originium."

                a "Totally original name, I know. But it is what it is. I'm not the one who named it."

                "Of course I knew that. After all, I did dabble in the sales and transport of Originium. I felt as though I wasted both of our times even asking that."

                "In this world we call Terra, there exists a mineral known as Originium. It's a highly valued mineral used in all sorts of technology that we use, like medical or entertainment."

                "As it turns out, it is also a very good energy source, so a lot of countries are using it to power their machines."

                "A miracle resource, right? If only it really was a miracle."

                "For all the fabulous qualities Originium offers, of course it would come with strings attached. For starters, Oripathy."

                "The highly contagious disease you contract when you are exposed to Originium for too long."

                "Once you contract Oripathy, what really awaits you is death. There is no known cure for Oripathy, though medical advances are still trying."

                "At the very least, there have been success stories where Oripathy progress was slowed or even halted, but none for removing."

                "These minerals also cause what we call Catastrophes. Natural disasters, basically."

                "Originium in mass quantities can be found prior to a Catastrophe, so scientists believe there might be some connection."

                "Furthermore, as Originium is used pretty much universally, because Originium comes in limited stock, and because no one sane enough would ever wish a Catastrophe to occur on anyone, you would expect it be a very high in demand commodity, and as such is the result of numerous political disputes."

                "Thankfully, no actual war broke out over it, but it is definitely no secret that Originium is used as weapons of war."

                "The only thing I don't know, though, is this Stage I thing. So I ask about that."

                a "Ah. Oripathy is separated into three stages, which really means how much your body is succumbing to Oripathy. This is measured by the blood sample we took from you."

                a "By the way, that x-ray is to determine where else in your body Oripathy has taken root, if it hasn't already. Fortunately for you, no other organ has been affected yet."

                a "Since you are Stage I, Oripathy does not have much hold on you right now. Obviously this will change in time, but how much depends on many factors."

                b "Like?"

                a "Body build. Luck. Usage of Arts. Stuff like that. Ah, I would definitely not recommend using Arts."

                a "Oripathy may give you the power to cast them, but they only hasten Oripathy's progress. Try not to get into those situations where Arts become necessary."

                "Arts. In other words, spellcasting magic."

                a "By the way. Initial analysis shows that you are capable of using Arts, so I'll repeat myself: try not to use it, as tempting as they may be."

                b "Alright."

                a "Anything else?"

                jump oripathy_dialog

        "What is an Infected?":

                a "Tried looking at a mirror lately? You ARE one, after all."

                "Snarky doctor we have here."

                a "An Infected is someone suffering from Oripathy. Of course, that label has negative stigma attached to it."

                a "Everyone hates the Infected for a reason: they're afraid that the Infected will spread the disease."

                a "They're not wrong, either. Too much contact with Originium is only one way to get the disease."

                a "Physical contact with the Infected or objects contaminated by Oripathy is another."

                a "When an Infected dies from Oripathy, their corpse becomes a new catalyst for the disease. It's also highly contagious, too. Makes you think, really."

                a "Think about how dumb people really are. Physically beating an Infected in the hopes that the disease will go away?"

                a "Justifying murder for contracting Oripathy through no fault of their own?"

                a "Calling them outcasts and pushing them out of society because they're to blame for the existence of Oripathy?"

                a "Ladies and gentlemen, that's how you SPREAD a disease and cause a pandemic, not prevent one. And that will eventually lead to the downfall of civilization as we know it."

                a "To make matters worse, it's difficult to hide the fact that you're Infected. The Infected part of your body becomes crystallized and looks just like Originium."

                a" Most people will try to cover that part up with clothes or something, but eventually it will be too difficult to cover up."

                a "Either that or nosy and paranoid people will come to the conclusion that you are Infected simply because they think everything is their business and need to know everything."

                "Definitely not wrong there. Basic psychology states that when people are afraid, they become irrational."

                "And when people become irrational, they take actions they normally would not take and create tragedies that could easily have been prevented."

                "Furthermore, your normal body functions begin to degrade as Oripathy progresses through your body."

                "Difficulty hearing."

                "Difficulty breathing."

                "Mental instability."

                "You never know when you'll be able to wake up and see tomorrow as an Infected."

                "Somehow, I feel as though the doctor forced his opinion onto me, though."

                a "Anything else?"

                jump oripathy_dialog

        "How did I get this disease?":

                a "Am I really someone who would know that? Sorry, but I don't know every patient's life story, and unfortunately I cannot begin to care for that, given the number of patients I see every day."

                a "Look. I am an Infected, too. I can at least sympathize with other Infected, but I can't be bothered to remember every single of my patient's life story. Sorry, I'm not a saint."

                "Ouch."

                a "Anything else?"

                jump oripathy_dialog

        "What options do I have now?.":

                a "Crawl into a hole and cry until you die."

                a "Wander around the city and be mauled to death."

                a "Starve and drop dead."

                a "Be shot at because being an Infected is some sort of international crime."

                a "Be shipped off to a concentration camp to die like a slave."

                a "Any of them appeal to you?"

                "So basically, die."

                a "I'm being sarcastic. Half sarcastic."

                a "Unfortunately for you, death is really all that you can look forward to. Fortunately for you, you're not alone. Even the non-Infected die someday."

                a "You already know this, but while there is no cure for Oripathy, there are methods to slow it down or even stop it altogether."

                a "And here's the unfortunate part again: none of those methods are proven and decisive."

                a "These methods end up being on a case-by-case basis. So what works for one person may not work for another."

                a "That's also our job here at Azazel: find a way to slow, stop, and possibly even cure Oripathy. Ideally for everyone, not just a select number."

                a "But until those happen, all you can look forward to is living with Oripathy."

                a "I know, it's not exactly something you want to hear. But it's reality."

                a "I suppose you could pick a god and pray that we discover a cure for it, but it would probably take more than that for us to succeed."

                "The doctor sighed."

                a "Anything else?"

                jump oripathy_dialog

        "(Shake my head)":

                a "Very good. You're free to go. Next patient, please."

    hide doctor
    with dissolve

    "I thanked the doctor before leaving the clinic. I saw the next patient walk into the examiner's room. Pretty young, too."

    "A male voice called to me."

    f "Hey! How did it go?"

    "I turned around and saw three people."

    show chris happy
    with dissolve

    show bob normal at left
    with dissolve

    show alice neutral at right
    with dissolve
    pause
    hide Chris happy
    with dissolve
    hide bob normal
    with dissolve
    hide alice neutral
    with dissolve

    show alice neutral

    g "What did the doctor say? Was is serious?"

    b "No, it wasn't serious."

    hide alice neutral
    show chris happy
    c "That's a relief. Glad it wasn't serious."
    hide chris happy
    show bob cheer
    d "Alright! Let's go get something to eat!"

    hide bob cheer
    show chris normal
    c "Well, it is Bob's turn to foot the bill."

    hide chris normal
    show alice neutral
    g "Anything you want to eat in particular, Protag?"

    b "No, not really."

    hide alice neutral
    show bob cheer

    d "In that case, it's ramen! Ramen!"

    hide bob cheer
    show alice angry

    g "Again? Don't you ever get bored of eating the same thing over and over?"

    hide alice angry
    show bob yikes

    d "Hey! No one insults the ramen. Plus, today is black garlic ramen day. It's not the same as last time."

    hide bob yikes
    show alice angry

    g "..."

    hide alice angry with dissolve
    show chris neutral

    c "Yes, yes. All hail the bowl. Come on, let's get moving before it gets crowded."

    hide chris neutral with dissolve

    "And just like that, another peaceful day passes by without incident. But so long as we are considered Infected, how long will this bit of happiness last?"

    show bob normal

    d "Hey, [name]! Hurry up or we'll leave you behind!"

    hide bob normal with dissolve

    b "Yes, yes. I'm coming, I'm coming."

    "...Maybe it won't be so bad, being an Infected."

    pause

    return

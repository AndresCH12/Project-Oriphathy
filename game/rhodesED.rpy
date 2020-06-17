label rhodesED:
    show chris neutral

    c "Sorry to keep you waiting."

    "Chris arrived. He dropped his belongings and sat down to catch his breath."

    hide chris neutral
    show alice neutral

    g "No, I'm glad you're safe. Now we need to wait for Bob."

    hide alice neutral
    show chris neutral

    c "...No. Bob will not be coming with us."

    hide chris neutral
    show alice neutral

    g "What? Why?"

    hide alice neutral
    show chris pissed

    c "We had an argument a couple days ago."

    b "A falling out?"

    c "Bob believed that words are not enough. He never believed in violence, but he stated that historically some changes were brought about by violence. Today is probably that."

    hide chris pissed
    show alice neutral

    g "..."

    b "So we're just going to leave them behind?"

    hide alice neutral
    show chris neutral

    c "It is what it is. Sorry."

    hide chris neutral
    show alice neutral

    g "..."
    b "No, it's not your fault. Alice, what do you want to do?"

    "Alice stood silent."

    b "We won't force you to do anything. But you have to decide for yourself what you want to do."

    b "I have to agree with Chris on this one, though. Violence is never the solution. We have to keep trying to reach out to people in hopes to convince them that the Infected are no different from them."

    hide alice neutral

    "Alice continues to stay silent. She appears to be thinking things over."

    "And then..."

    show alice angry

    g "Alright. I made up my mind. Where ever you two go, I will follow."

    g "I lived my whole life simply being told what to do. I lived my whole life simply trying to satisfy everyone around me. To tell the truth, I'm sick and tired of it all. So..."

    g "Where ever you go. Whatever you do. Whatever happens. I will not run away."

    b "Okay."

    hide alice angry
    show chris neutral

    c "Alright. Let's go before this place becomes a battlefield."

    hide chris neutral

    "The three of us gathered our belongings once we were rested enough."
    "With me leading the way, the three of us kept crossing through alleyways and streets, avoiding as much of the fighting as we could."
    "Evidently, we could not avoid seeing the escalation of violence."
    "The senseless killings continue."
    "It looks like things are turning out unfavorably for the Ursus Guards."
    "Though better trained and better armed, the Ursus Guards are horribly outnumbered."
    "Already spread thin, it's taking the Ursus Guards everything they have just to prevent the rioters focused towards them."

    show chris neutral

    c "This really is a horrible sight. On top of that, apparently Rhodes Island is in Chernobog. I do not know what they're doing here, but clearly they are not part of the rioting."

    c "Once we get out of here, I am thinking of joining them. I talked to one of their members, and it looked like they are genuinely looking for a cure to Oripathy."

    c "They also do not discriminate against the Infected. Heck, the one I talked to WAS an Infected themselves."

    hide chris neutral
    show alice neutral

    g "..."

    b "Well, that makes sense. I suppose we're ditching the plan to move to Columbia?"

    hide alice neutral
    show chris neutral

    c "No. If you can cover the costs, I'll convince Bob to join us."

    c "We'll find jobs in Columbia to pay you back."

    b "...No, unfortunately. My connections were understanding, but they have their own positions to consider."

    c "Can't be helped."

    c "In that case, I would probably recommend joining Rhodes Island. We can then move to Columbia once we earned enough."

    hide chris neutral
    show alice neutral

    g "Alright."

    b "Sounds good to me."

    hide alice neutral

    scene black

    "In agreement, the three of us continue through Chernobog, the scenary forever eched into our minds."
    "........."
    "......"
    "..."

    "Nightfall. We have managed to escape Chernobog with little incident. In the end, the four of us did not reunite."
    "Stopping to catch our breaths once again and also sighing relief of escaping, we then found ourselves at the camp of our intended organization."

    scene warehouse

    show rio

    l "Who are you?"

    l "What business do you have with us?"

    hide rio
    show chris neutral

    c "Is this where Rhodes Island is stationed at? We would like to join."

    hide chris neutral
    show rio

    l "New recruits?"

    hide rio

    "The three operators looked at us, puzzled. One of the operators turned around and jestured."

    f "Hey. Let them through. They want to join us."

    show rio
    l "Go on ahead. Just follow the hallway until you reach a large room."

    hide rio

    "The Rhodes Island operators allowed us entry."
    "As it turns out, we were not the only ones. One of the operators told us that while they were looking for something in Rhodes Island, they were caught up with the Reunion assault and decided to help the Ursus Guards repel it. In doing so, they saved many lives, Infected or otherwise, who asked to join them."

    scene clinic
    with fade

    show doctor

    a "Okay, next applicant, please."

    hide doctor

    "Chris, Alice, and I walked into the room. This looks like Azazel all over again. The three of us put down our belongings and sat on the designated chairs."

    show doctor

    a "Typically, anyone who wants to join Rhodes Island have to take a medical examination for Oripathy progress, and take a proficiency exam. Before we do any of that, please allow me to ask one question."

    a "Why choose Rhodes Island?"

    hide doctor
    show chris neutral

    c "Violence only begets more violence. Rhodes Island is currently developing a cure for Oripathy, right? If that cure can end the discrimination against the Infected, I want to be a part of that."

    hide chris neutral
    show doctor

    a "Yes, that is true. However, there is no telling when we will succeed, or even if we will. What about you?"

    hide doctor
    show alice neutral

    g "I lived my whole life being told what to do and to appease others. I no longer desire that. I only wish to make my own choices from here on out, and this is the path I have chosen."

    hide alice neutral
    show doctor

    menu:
        "It sounded like you lived a hard life until now. And you?"

        "I am the same as Chris.":
            a "Just like him, there are many operators before you who thought the same."

        "I am the same as Alice":
            a "Everyone should be free to make their own choices for themselves. I am glad the two of you are doing just that."

        "(Other)":
            python:
                arguemnt = renpy.input("(Other)")
                argument = argument.strip()

                if not argument:
                        argument = "I am unsure of whether this path will bring us joy but, I will fight for what i think is right for the infected."

            a "That makes sense."

    a "Alright. Welcome to Rhodes Island."

    hide doctor
    show chris neutral

    c "That's it? Didn't you say we have to go through a medical exam and some test first?"

    hide chris neutral
    show doctor

    a "For now, no. We have no issues taking anyone who wishes to join us. How you will serve Rhodes Island will differ from the others, but you will all still serve Rhodes Island in the end."
    a "Naturally, we will prepare the documentations for you to fill out at a later date."

    hide doctor
    show alice soft

    g "Okay. Where do we go now?"

    hide alice soft
    show doctor

    a "Right now? We will assign the three of you to a room where you will rest."
    a "The thing is, we medics already have our hands full trying to treat everyone, so we can't do any medical examinations for the new recruits. And I am merely tasked with telling them what I have told you."
    a "Besides, even without a medical exam I can already tell you three are exhausted. Did you run all the way to us from the city of Chernobog?"
    a "This will also give you a chance to decide if Rhodes Island is really the right path for you."

    hide doctor
    show chris neutral

    c "..."

    hide chris neutral

    "The three of us remained silent. The doctor sighed."

    show doctor

    a "Well, if you weren't already committed, I suppose you wouldn't have shown up looking like you ran a marathon through Chernobog five times over."

    a "We also have a cafeteria open for you. I would recommend eating before you go to sleep."

    b "Okay."

    a "Go ahead and rest. You're free to go."

    hide doctor

    scene black

    "The three of us thanked the medic, grabbed our belongings, and left."
    "Looking at each other, our resolve remained firm. We have chosen to join Rhodes Island and rally to their cause. The process begins tomorrow, and with that our new lives."
    "........."
    "......"
    "..."

    "Little did we know that we would eventually meet face to face again. Not like this..."

    scene chaos city
    with fade

    f "Fancy seeing you here."

    "Out on the battlefield, I looked straight into the enemy. I was stunned at whom I was looking at."

    b "You...!"

    return

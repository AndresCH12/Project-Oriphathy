label reunionED:

    show bob normal

    d "Hey. Sorry I'm late."

    "Bob arrived. He dropped his belongings and sat down to catch his breath."

    hide bob normal
    show alice neutral

    g "No, I'm glad you're safe. Now we need to wait for Chris."

    hide alice neutral
    show bob normal

    d "...About that. Sorry, but Chris will not be meeting up with us anymore."

    hide bob normal
    show alice neutral

    g "What? Why?"
    hide alice neutral
    show bob normal

    d "We... had a falling out. A couple days ago, we ended up arguing over who was right."

    b "A falling out?"

    d "Yeah. Chris believed that we could one day see each other eye to eye. As much as I would love to see that happen, that will never happen. Today is proof of that."
    hide bob normal
    show alice neutral

    g "..."

    b "So we're just going to leave them behind?"

    hide alice neutral
    show bob normal

    d "Yeah. We don't have a choice."

    b "No, it's not your fault. Alice, what do you want to do?"

    hide bob normal
    show alice neutral

    "Alice stood silent."

    b "We won't force you to do anything. But you have to decide for yourself what you want to do."

    b "I have to agree with Bob on this one, though. Though violence is never the solution, sometimes it is necessary. At the very least, we should at least not allow ourselves to be used to it."

    "Alice continues to stay silent. She appears to be thinking things over."

    "And then..."

    hide alice neutral
    show alice angry

    g "Alright. I made up my mind. Where ever you two go, I will follow."

    g "I lived my whole life simply being told what to do. I lived my whole life simply trying to satisfy everyone around me. To tell the truth, I'm sick and tired of it all. So..."

    g "Where ever you go. Whatever you do. Whatever happens. I will not run away."

    b "Okay."

    hide alice angry
    show bob cheer

    d "Sounds great. Let's go, then."

    hide bob cheer

    "The three of us gathered our belongings once we were rested enough."
    "With me leading the way, the three of us kept crossing through alleyways and streets, avoiding as much of the fighting as we could."
    "Evidently, we could not avoid seeing the escalation of violence."
    "The senseless killings continue. It looks like things are turning out unfavorably for the Ursus Guards."
    "Though better trained and better armed, the Ursus Guards are horribly outnumbered."
    "Already spread thin, it's taking the Ursus Guards everything they have just to prevent the rioters focused towards them."

    show bob angry

    d "I know what you're thinking. This is a horrifying sight. Believe me when I say this: I'm not thrilled by the turn of events either."

    d "That being said, I am considering joining Reunion despite what they're doing here today. I'm tired of being pushed around."

    d "I'm tired of my voice not being heard. Being silenced. Ignored."

    hide bob angry
    show alice neutral

    g "..."

    b "Well, that makes sense. I suppose we're ditching the plan to move to Columbia?"

    hide alice neutral
    show bob normal

    d "Well, that really depends. Did you manage to secure the funding for us? If so, I can try to convince Chris to at least come with us."

    d "Obviously we'll pay you back, of course."

    b "...No, unfortunately. My connections were understanding, but they have their own positions to consider."

    d "Figured. Can't blame them, though."

    d "On the other hand, Reunion does pay pretty well. We could probably join them, make bank, and then run to Columbia."

    hide bob normal
    show alice neutral

    g "Alright."

    b "Sounds good to me."

    hide alice neutral

    scene black
    
    "In agreement, the three of us continue through Chernobog, the scenary forever eched into our minds."
    "................."
    "............"
    "......"

    "Nightfall. We have managed to escape Chernobog with little incident. In the end, the four of us did not reunite."
    "Stopping to catch our breaths once again and also sighing relief of escaping, we then found ourselves at the camp of our intended organization."

    scene warehouse
    show rs
    with dissolve

    k "Halt. Who goes there?"

    k "Huh? Infected? What are you doing here?"

    hide rs
    show bob yikes

    d "Is this the camp for Reunion? We would like to join."

    hide bob yikes
    show rs
    k "Join? You?"

    "The soldiers examined us questioningly. One of them nodded."

    k "Well, alright. I don't think there will be any issues in at least letting you apply. Go on ahead."
    hide rs

    "The soldier allowed us entry to their camp."
    "As it turns out, we were not the only ones. One of the soldiers told us that while they were attacking Chernobog, several Infected they inadvertedly saved expressed a desire to join them. The recruitment office they had set up is rather packed as a result."

    show rs

    a "Next. You three. Come in."

    a "Bob, Alice, and I entered the room. This looks like Azazel all over again. The three of us put our belongings down and sat at the designated chairs."

    a "You wish to join Reunion, correct? There is a procedure we typically do. Medical examinations, proficiency testing, stuff like that. Before we do that... allow me to ask each of you one question."

    a "Why? Why join Reunion?"

    hide rs
    show bob normal

    d "I'm tired of being rejected by society simply because I have Oripathy. It's the same for most in Reunion, right?"

    hide bob normal
    show rs

    a "Hmm. That is true. I myself am in agreement. What about you?"

    hide rs
    show alice neutral

    g "I lived my whole life being told what to do and to appease others. I no longer desire that. I only wish to make my own choices from here on out, and this is the path I have chosen."

    hide alice neutral
    show rs

    menu:
        "Hmm. Very well said. And you?"

        "I am the same as Bob.":
            a "Your kind is the most common we have here."

        "I am the same as Alice":
            a "That's not surprising. We Infected were always considered beneath the others in every possible way."

        "(Other)":
            python:
                arguemnt = renpy.input("(Other)")
                argument = argument.strip()

                if not argument:
                        argument = "I am unsure of whether this path will bring us joy but, I will fight for what i think is right for the infected."

            a "I can understand where you're coming from."

    a "Very well. We'll accept your application. Welcome to Reunion."

    hide rs
    show bob yikes

    d "Wait, that's it? No papers to sign, no training, nothing?"

    hide bob yikes
    show rs

    a "That's it. We never turn away anyone who wishes to join us. What role you will play in Reunion will, of course, differ, but you will be supporting our cause all the same."

    a "We'll just need a few things from you. Signatures for paperwork, medical submissions, stuff like that."

    hide rs

    show alice neutral

    g "Okay. Where do we go now?"

    hide alice neutral
    show rs

    a "Now? Right now, nowhere. Thing is, we didn't really expect this large of a turnout, so our medical staff is working around the clock to check everyone in. In the meantime, we have set up a temporary sleeping area for you."

    a "It is a long day for you, no? Take tonight to rest up. It'll also give you a chance to really decide if you want to go through with your decision. Reunion has, after all, formally declared war on the world now."

    a "I did say we never turn away anyone who wishes to join Reunion, but realistically we are no longer in a position to allow indecisive people to join us."
    hide rs
    show bob normal

    d "..."

    hide bob normal

    "The three of us remained silent. The examiner laughed."

    show rs
    a "I suppose you three have thought this through though. Sorry to patronize you then. But really, you three looked like you ran across the entirety of Chernobog all day. You three really looked ready to drop dead."

    a "Go grab a bite to eat, then sleep. We'll worry about the recruitment process tomorrow. Any other questions?"

    b "No, not really."

    a "Good. You may go now."

    hide rs

    scene black

    "The three of us thanked the examiner, grabbed our belongings, and left."
    "Looking at each other, our resolve remained firm. We have chosen to join Reunion and rally to their cause. The process begins tomorrow, and with that our new lives."
    "........."
    "......"
    "..."

    "Little did we know that we would eventually meet face to face again. Not like this..."

    scene chaos city
    with fade

    f "Oh? Now there's a face I haven't seen in a long time."

    "Out on the battlefield, I looked straight into the enemy. I was stunned at whom I was looking at."

    b "You...!"

    return

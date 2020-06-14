label Alice_backstory:

    scene street
    with fade

    "I spotted Alice wandering the city streets. It was a quiet street, somewhat tucked away from the city's quietier districts."

    g "Oh, [name]!"

    "Alice waved. It looked like she spotted me."

    show alice cheer
    with fade

    b "What are you doing here?"

    hide alice cheer
    show alice soft

    g "Nothing much. I just like how quiet this street is."

    "Alice is holding a book in her hand. She was probably reading it here, in a quiet place like this."

    b "Yeah?"

    g "Reminds me of home. Well, in a way."

    b "That's pretty unusual, coming from a Sarkaz."

    hide alice soft
    show alice angry

    g "What does that mean?!"

    menu:
        g "Are you calling all of us Sarkaz axecrazy?!"

        "No, that's not what I meant.":
            g "Then what do you mean?!"

            g "...Whatever."

        "Well, a lot of Sarkaz do end up working as a mercenary.":
            g "So you think I'm just like them?"

            g "..."

    hide alice angry
    show alice soft

    g "Well, whatever. Not all Sarkaz make a living fighting, you know."

    b "Then what did you do?"

    g "Me? Well, let's see..."

    "Alice looked up towards the sky, pondering for a moment."

    g "Compared to what Bob and Chris went through, I don't think mine is all that bad."

    g "But if you insist..."

    show black
    with fade

    g "I grew up in a desert town. It wasn't a very large town, and there weren't very many people."

    g "As a result, everyone in town pretty much knew each other. It was like all of us were one big family."

    g "Of course, this town, being in the middle of nowhere, means it has its share of problems."

    g "Like money. We do get travelling merchants from time to time, though. Merchants like you."

    g "But fsometimes we would need to venture out to gather supplies for ourselves."

    g "Danger is everywhere, too. Many of the townsfolk ended up becoming hunters."

    g "It was a pretty good life, of course."

    g "Until the war happened."

    pause 1.0

    g "I don't remember the exact details, but apparently it was a war fought by two foreign countries over a territory dispute."

    g "Both countries hired mercenaries to fight for them, alongside their own military."

    g "This isn't knew. Because of our build, Sarkaz typically make great figters."

    g "In exchange for trading their lives, they earn fame and pay."

    g "The offer made by both countries resulted in Sarkaz killing each other, but this is also normal."

    g "We Sarkaz have always been taught to fight, after all."

    pause 1.0

    g "Anyway. I was... somewhat of an anomoly as a Sarkaz. I was more of an intellectual, see?"

    hide alice neutral
    show alice cheer

    g "That's not a bad thing among Sarkaz. In fact, a lot of them were rather jealous of me."

    hide alice cheer
    show alice neutral

    g "One of the merchants who passed by noticed my intellectual capabilities and suggested that I enroll in an elite academy."

    g "The town's elder agreed with the merchant. Thought I should contribute as a Sarkaz in my own way, rather than the usual Sarkaz way."

    g "Actually, everyone agreed. I don't think there was anyone in opposition. So I agreed as well."

    g "Turns out that merchant was doing it on the side. That merchant was actually a professor. Talk about lucky, right?"

    g "So I ended up enrolling. It was a nice life, being a student in a far off land."

    g "Made some friends, too. Some nice, some... not so nice."

    "Alice closed her eyes for a moment"

    g "There was one who stood out, too. This one girl. A Sankta. Had a halo on her head and white wings on her back."

    g "She would go around hounding me. Scheming petty schemes against me. Doing ridiculous things to ridicule me."

    g "It started escalating. First it was little pranks. Then it intensified to vandalism. Eventually, it got physical."

    g "One time, she tried to trip me over during gym. Another, throw rocks while I was casting an Art."

    g "She eventually got expelled because the teachers got fed up with her."

    g "But if only that ended like that."

    g "I remembered her crying face that day she found out she was getting expelled."

    g "She said all she wanted was to be friends with me. Said she never met a Sarkaz before in her life."

    g "To prove her friendship, she gave me a pendant. It was a rather nice pendant."

    g "It was also nice that I was gullible enough to accept it."

    g "Turns out, that pendant is amde from Originium. The more dangerous and unstable kind."

    g "Merely touching it has a high risk of getting Oripathy. And I touched it without realizing it."

    g "That girl was an Infected. Pretty rare, since Sankta has natural resistence to Oripathy."

    g "That girl also despised Sarkaz. Wanted to be friends? Nothing more than a lie."

    g "But that didn't matter anymore. Because of her, and because of my gullibility, I ended up being an Infected."

    g "I told the professor who recruited me about this. Big mistake."

    g "That professor hates the Infected. The horrified look on his face is something I will never forget."

    g "He promptly chased me out of the school. Just like that, I lost my future."

    g "All thanks to someone who could not act her age."

    g "Why didn't I go back to my hometown, you ask?"

    g "Simple. Sarkaz is one of pride and honor. To return now would bring shame to my family."

    g "I couldn't do much, anyway. So, while I do continue to send letters to them, I naturally lie about my life at the academy."

    g "Meanwhile, I ended up here."

    show city_street
    with fade

    hide alice neutral
    show alice cheer

    g "See? Told you it's nothing serious."

    g "It's just a story of someone falling from grace. Kind of ironic, since I'm a Sarkaz and not a Sankta."

    b "Yeah, as a merchant I see a lot of oddballs here and there. Nothing like who you met, though."

    g "Even though I've been kicked out of the academy, the knowledge I gained can't be replaced."

    g "That's why, even as an Infected, there are still a lot of things I want to do."

    menu:
        g "What about you? Is there anything you want to do?"

        "I want to get back at the one who gave me so much problems.":

            b "If only that did not happen, I would not be in this situation."

            g "Oh? But then, if you were not in this situation, you would not have met us, right?"

            b "You have a point, but I still can't forgive that person for what they did to me."

            $ reunion += 1

        "I would like to go back to being a merchant, if possible.":

            b "I'm sure there are a lot of other stuff I could do, but in the end being a merchant is what I enjoy the most."

            g "Yeah? It's the money, isn't it?"

            b "Yep. Wait, no!"

        "I'd like to do something new.":

            b "Being a merchant is fun, but maybe it's time I do something new for a change."

            g "Yeah? Got something in mind?"

            b "No, not yet. Being a merchant means I had to defend myself on occasions, so maybe I'll try out the Sarkaz mercenary life."

            $ rhodesIsland += 1

    hide alice cheer
    show alice soft

    "Alice looked up towards the sky. It looks like some time has passed, because the sky wasn't cloudy before."

    g "It looks like it might rain in a bit, so I should probably get home."

    b "Yeah, okay."

    g "I'll talk to you later, okay? Goodbye."

    b "Goodbye."

    "Alice left, eventually fading from my sight."

    "A soft wind brushed against my face."

    pause 1.0

    show street
    with fade

    "........."
    "......"
    "..."

    "Another week passed. The passing was uneventful."

    jump Backstory

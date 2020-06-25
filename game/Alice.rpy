# Alice's backstory event.
# Variables used:
# alice = Alice
# protag = Player

label Alice_backstory:

    scene street
    with fade

    "I spotted Alice wandering the city streets. It was a quiet street, somewhat tucked away from the city's quietier districts."

    alice "Oh, [name]!"

    "Alice waved. It looked like she spotted me."

    show alice cheer
    with fade

    protag "What are you doing here?"

    hide alice cheer
    show alice soft

    alice "Nothing much. I just like how quiet this street is."

    "Alice is holding a book in her hand. She was probably reading it here, in a quiet place like this."

    protag "Yeah?"

    alice "Reminds me of home. Well, in a way."

    protag "That's pretty unusual, coming from a Sarkaz."

    hide alice soft
    show alice angry

    alice "What does that mean?!"

    menu:
        alice "Are you calling all of us Sarkaz axecrazy?!"

        "No, that's not what I meant.":
            alice "Then what do you mean?!"

            alice "...Whatever."

        "Well, a lot of Sarkaz do end up working as a mercenary.":
            alice "So you think I'm just like them?"

            alice "..."

    hide alice angry
    show alice soft

    alice "Well, whatever. Not all Sarkaz make a living fighting, you know."

    protag "Then what did you do?"

    alice "Me? Well, let's see..."

    "Alice looked up towards the sky, pondering for a moment."

    alice "Compared to what Bob and Chris went through, I don't think mine is all that bad."

    alice "But if you insist..."

    hide alice soft

    show black
    with fade

    show alice neutral

    alice "I grew up in a desert town. It wasn't a very large town, and there weren't very many people."

    alice "As a result, everyone in town pretty much knew each other. It was like all of us were one big family."

    alice "Of course, this town, being in the middle of nowhere, means it has its share of problems."

    alice "Like money. We do get travelling merchants from time to time, though. Merchants like you."

    alice "But sometimes we would need to venture out to gather supplies for ourselves."

    alice "Danger is everywhere, too. Many of the townsfolk ended up becoming hunters."

    alice "It was a pretty good life, of course."

    alice "Until the war happened."

    pause 1.0

    alice "I don't remember the exact details, but apparently it was a war fought by two foreign countries over a territory dispute."

    alice "Both countries hired mercenaries to fight for them, alongside their own military."

    alice "This isn't new. Because of our build, Sarkaz typically make great figters."

    alice "In exchange for trading their lives, they earn fame and pay."

    alice "The offer made by both countries resulted in Sarkaz killing each other, but this is also normal."

    alice "We Sarkaz have always been taught to fight, after all."

    pause 1.0

    alice "Anyway. I was... somewhat of an anomoly as a Sarkaz. I was more of an intellectual, see?"

    hide alice neutral
    show alice cheer

    alice "That's not a bad thing among Sarkaz. In fact, a lot of them were rather jealous of me."

    hide alice cheer
    show alice neutral

    alice "One of the merchants who passed by noticed my intellectual capabilities and suggested that I enroll in an elite academy."

    alice "The town's elder agreed with the merchant. Thought I should contribute as a Sarkaz in my own way, rather than the usual Sarkaz way."

    alice "Actually, everyone agreed. I don't think there was anyone in opposition. So I agreed as well."

    alice "Turns out that merchant was doing it on the side. That merchant was actually a professor. Talk about lucky, right?"

    alice "So I ended up enrolling. It was a nice life, being a student in a far off land."

    alice "Made some friends, too. Some nice, some... not so nice."

    "Alice closed her eyes for a moment"

    alice "There was one who stood out, too. This one girl. A Sankta. Had a halo on her head and white wings on her back."

    alice "She would go around hounding me. Scheming petty schemes against me. Doing ridiculous things to ridicule me."

    alice "It started escalating. First it was little pranks. Then it intensified to vandalism. Eventually, it got physical."

    alice "One time, she tried to trip me over during gym. Another, throw rocks while I was casting an Art."

    alice "She eventually got expelled because the teachers got fed up with her."

    alice "But if only that ended like that."

    alice "I remembered her crying face that day she found out she was getting expelled."

    alice "She said all she wanted was to be friends with me. Said she never met a Sarkaz before in her life."

    alice "To prove her friendship, she gave me a pendant. It was a rather nice pendant."

    alice "It was also nice that I was gullible enough to accept it."

    alice "Turns out, that pendant is amde from Originium. The more dangerous and unstable kind."

    alice "Merely touching it has a high risk of getting Oripathy. And I touched it without realizing it."

    alice "That girl was an Infected. Pretty rare, since Sankta has natural resistence to Oripathy."

    alice "That girl also despised Sarkaz. Wanted to be friends? Nothing more than a lie."

    alice "But that didn't matter anymore. Because of her, and because of my gullibility, I ended up being an Infected."

    alice "I told the professor who recruited me about this. Big mistake."

    alice "That professor hates the Infected. The horrified look on his face is something I will never forget."

    alice "He promptly chased me out of the school. Just like that, I lost my future."

    alice "All thanks to someone who could not act her age."

    alice "Why didn't I go back to my hometown, you ask?"

    alice "Simple. Sarkaz is one of pride and honor. To return now would bring shame to my family."

    alice "I couldn't do much, anyway. So, while I do continue to send letters to them, I naturally lie about my life at the academy."

    alice "Meanwhile, I ended up here."

    show city_street
    with fade

    hide alice neutral
    show alice cheer

    alice "See? Told you it's nothing serious."

    alice "It's just a story of someone falling from grace. Kind of ironic, since I'm a Sarkaz and not a Sankta."

    protag "Yeah, as a merchant I see a lot of oddballs here and there. Nothing like who you met, though."

    alice "Even though I've been kicked out of the academy, the knowledge I gained can't be replaced."

    alice "That's why, even as an Infected, there are still a lot of things I want to do."

    menu:
        alice "What about you? Is there anything you want to do?"

        "I want to get back at the one who gave me so much problems.":

            protag "If only that did not happen, I would not be in this situation."

            alice "Oh? But then, if you were not in this situation, you would not have met us, right?"

            protag "You have a point, but I still can't forgive that person for what they did to me."

            $ reunion += 1

        "I would like to go back to being a merchant, if possible.":

            protag "I'm sure there are a lot of other stuff I could do, but in the end being a merchant is what I enjoy the most."

            alice "Yeah? It's the money, isn't it?"

            protag "Yep. Wait, no!"

        "I'd like to do something new.":

            protag "Being a merchant is fun, but maybe it's time I do something new for a change."

            alice "Yeah? Got something in mind?"

            protag "No, not yet. Being a merchant means I had to defend myself on occasions, so maybe I'll try out the Sarkaz mercenary life."

            $ rhodesIsland += 1

    hide alice cheer
    show alice soft

    "Alice looked up towards the sky. It looks like some time has passed, because the sky wasn't cloudy before."

    alice "It looks like it might rain in a bit, so I should probably get home."

    protag "Yeah, okay."

    alice "I'll talk to you later, okay? Goodbye."

    protag "Goodbye."

    "Alice left, eventually fading from my sight."

    "A soft wind brushed against my face."

    hide alice soft
    with fade

    pause 1.0

    show street
    with fade

    "........."

    "......"

    "..."

    "Another week passed. The passing was uneventful."

    jump Backstory

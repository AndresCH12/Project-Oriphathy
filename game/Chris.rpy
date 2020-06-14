label Chris_backstory:

    scene room
    with fade
    show chris neutral

    "Chris appears to be sorting through his belongings."

    b "Hey, Chris!"

    hide chris neutral
    show chris happy

    c "Hey! Uh, watch your step, okay? I put out a lot of my belongings all over."

    b "Yeah, I can definitely see that."

    "On the ground were stacks of clothes and books. One of the books had the word 'Photo Album' on it."

    b "Hey, about that album..."

    menu:
        "That? Ah, that's just a book full of old photos. You want to take a look?"

        "Can I?":

            b "Are you sure?"

            c "Yeah, I'm sure. They're just photos."

        "I think I'll pass.":

            c "You sure about that? I don't really mind."


    c "That book is mostly photos of my family or my hometown."

    b "Really? How was your hometown?"

    c "Quiet. It's rather surprising given that it's an industrial city."

    b "Oh?"

    c "You want to hear more about it? Okay, give me a moment to finish up."

    b "Let me help."

    c "Thanks, but I can handle this. Why don't you take a seat over there? Make yourself a cup of tea or something while you wait."

    hide chris happy

    "Chris pointed towards a small round table. On top is a neatly folded tablecloth with two teacups on top. A box of teabags lie next to the teacups."

    "It did not take very long. It looked less like Chris cleaning up and more like Chris looking for something."

    "And sure enough, he was. He took out a small pocketwatch and placed it on the table."

    show chris happy

    c "There it is. Now then, my hometown."

    hide chris happy

    scene black
    with fade

    show chris neutral

    c "Like I said, it's an industrial city. It's one of the many cities dedicated to research and production of Originium-related products."

    c "My mother is a researcher at one of the labs; my father, an engineer."

    c "My older sister just graduated from high school, and my younger sister about to start elementary. I was 14 then."

    c "Though my parents are rarely home, the five of us lived a rather decent life. Not overly extravagant, of course, but fair off compared to most."

    c "Because of my parent's influences, I had an interest in Originium research."

    c "Though the rules typically state that outsiders aren't allowed, the research lab is generally okay with immediate friends and family."

    c "So, being a child of a researcher and engineer, I naturally had the privilege to study Originium first hand."

    c "Grateful for the opportunity, I dedicated whatever little free time I had to studying everything there is to know about Originium."

    c "That probably explains why I knew so much, right?"

    c "Well, an incident happened. One of the Originium product, fresh off the assembly line, was malfunctioning."

    c "It was a simple power unit the government requested, to determine if there is a more efficient way to use Originium as an energy source"

    c "I should mention that at this point, Originium was already a viable energy source. However, they are wholly inefficient."

    c "The product exploded as a result. Thankfully, the damages were very minor, and it's mostly because of my father's quick thinking."

    c "Because of my father, the team managed to move the unit quickly and safely to a sealed off room, where it exploded with little damage."

    c "However, it came at a cost."

    c "The team that handled the product contracted Oripathy as a result."

    c "They blamed my father for getting Oripathy, even despite knowing that being an Originium engineer means you may get Oripathy as a result."

    c "But they refused to listen. Even as they were forcibly banished, they still blamed my father for it."

    c "And it all went downhill from there."

    c "Bearing the weight and guilt of what happened, my father quit."

    c "Everyone knew it wasn't his fault, but he took responsibility anyway."

    c "There was just one thing they did not know: I actually saw that power unit the night before."

    c "I wanted to see it before anyone else, so I snuck into the lab."

    c "When I saw the power unit, I felt a rush of excitement well up inside of me."

    c "And then it started glowing. Almost as if it was calling out to me."

    c "So I reached towards it. I touched it."

    c "Nothing really... happened. The unit felt warm to the touch. And then it stopped glowing."

    c "I could not figure out what happened, so I left it at that."

    c "Of course, that was a mistake. A few days after that, I found out that my hand started growing black crystals."

    c "You know about this, right? The symptoms of Oripathy."

    c "My father was the first to find out. And once again, he blames himself."

    c "He desperately sought to cover it up. From my mom. From my sisters. From everyone else."

    c "Well, he was pretty bad at hiding stuff. My mom and sisters found it pretty much immediately."

    c "They were definitely better at keeping secrets than my dad, though, so somehow I managed to evade any of the persecutions the Infected face on a daily basis."

    c "I suppose I would be considered fortunate, then. Not once had I lived a life of hardship because I was an Infected."

    c "However, I knew that I can't live like this eventually. So far we were successful in keeping it a secret. How long can we keep doing this, though?"

    c "Against my entire family's protest, I decided to leave my hometown. Having known about what the Infected go through, I decided to find a cure for them."

    c "I had heard of the Reunion movement. It is a noble movement, but their method does not exactly agree with me."

    c "And that method is just standing around demanding someone else take action. Would it not be better if you yourself take action?"

    c "Well, that's probably easier said than done. If it were possible, I would imagine Reunion would have done it."

    c "Instead, I sought out clinics speciaiizing in Oripathy. Places like Azazel. And thankfully, they have allowed me to work part time as an intern."

    c "The acting manager also mentioned a Rhodes Island. Apparently it's another pharmaceudical company that consists of Infected and non-Infected."

    hide chris neutral
    with fade

    scene room
    with fade

    show chris happy
    with dissolve

    c "But yeah, that's that."

    b "Wow, that's impressive."

    "Chris took a sip of tea, and chuckled."

    c "It's not an extravagant story, but I hope it would at least be a positive one."

    b "Yeah, it definitely is."

    c "The acting manager did suggest that I go to Rhodes Island, though. Azazel, through a great company, is far too small."

    c "The acting manager suggested that I broaden my horizons, or something. That I should see the world for myself, not just Chernobog."

    c "So I probably will do that. Seek out and apply for a position at Rhodes Island."

    c "And I was wondering. Would you like to join me? With your logistical and merchant abilities, I would think you would be helpful to Rhodes Island as well."

    b "Me?"

    menu:
        c "Well, who else? What do you say?"

        "I'm flattered you think that.":
            b "If you think my skills would help, then I'm in."

            c "Great! I'll ask the acting manager for a recommendation for you too."

            $ rhodesIsland += 1

        "Let me think about it a bit more.":
            b "I'm not entirely sure if I want to continue as a merchant, anyway."

            c "I think you'll do fine, but okay. There's no need to rush."

        "I think I'll pass.":
            b "I don't think I'll fit in with a pharmaceudical company like Rhodes Island."

            c "Coming from someone who does business with Azazel, that's not convincing at all. But, if you say so."

            $ reunion += 1

    c "Thanks for hearing me out, though. I rarely get a chance to talk about my hometown."

    b "No, no. Thank you for the tea. It was a very interesting story."

    c "You're welcome."

    hide chris happy

    "I thanked Chris again before leaving his room."

    jump Backstory

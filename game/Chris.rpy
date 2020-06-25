# Chris' backstory event.
# Variables used:
# chris = Chris
# protag = Player

label Chris_backstory:

    scene room
    with fade
    show chris neutral

    "Chris appears to be sorting through his belongings."

    protag "Hey, Chris!"

    hide chris neutral
    show chris happy

    chris "Hey! Uh, watch your step, okay? I put out a lot of my belongings all over."

    protag "Yeah, I can definitely see that."

    "On the ground were stacks of clothes and books. One of the books had the word 'Photo Album' on it."

    protag "Hey, about that album..."

    menu:
        "That? Ah, that's just a book full of old photos. You want to take a look?"

        "Can I?":

            protag "Are you sure?"

            chris "Yeah, I'm sure. They're just photos."

        "I think I'll pass.":

            chris "You sure about that? I don't really mind."


    chris "That book is mostly photos of my family or my hometown."

    protag "Really? How was your hometown?"

    chris "Quiet. It's rather surprising given that it's an industrial city."

    protag "Oh?"

    chris "You want to hear more about it? Okay, give me a moment to finish up."

    protag "Let me help."

    chris "Thanks, but I can handle this. Why don't you take a seat over there? Make yourself a cup of tea or something while you wait."

    hide chris happy

    "Chris pointed towards a small round table. On top is a neatly folded tablecloth with two teacups on top. A box of teabags lie next to the teacups."

    "It did not take very long. It looked less like Chris cleaning up and more like Chris looking for something."

    "And sure enough, he was. He took out a small pocketwatch and placed it on the table."

    show chris happy

    chris "There it is. Now then, my hometown."

    hide chris happy

    scene black
    with fade

    show chris neutral

    chris "Like I said, it's an industrial city. It's one of the many cities dedicated to research and production of Originium-related products."

    chris "My mother is a researcher at one of the labs; my father, an engineer."

    chris "My older sister just graduated from high school, and my younger sister about to start elementary. I was 14 then."

    chris "Though my parents are rarely home, the five of us lived a rather decent life. Not overly extravagant, of course, but fair off compared to most."

    chris "Because of my parent's influences, I had an interest in Originium research."

    chris "Though the rules typically state that outsiders aren't allowed, the research lab is generally okay with immediate friends and family."

    chris "So, being a child of a researcher and engineer, I naturally had the privilege to study Originium first hand."

    chris "Grateful for the opportunity, I dedicated whatever little free time I had to studying everything there is to know about Originium."

    chris "That probably explains why I knew so much, right?"

    chris "Well, an incident happened. One of the Originium product, fresh off the assembly line, was malfunctioning."

    chris "It was a simple power unit the government requested, to determine if there is a more efficient way to use Originium as an energy source"

    chris "I should mention that at this point, Originium was already a viable energy source. However, they are wholly inefficient."

    chris "The product exploded as a result. Thankfully, the damages were very minor, and it's mostly because of my father's quick thinking."

    chris "Because of my father, the team managed to move the unit quickly and safely to a sealed off room, where it exploded with little damage."

    chris "However, it came at a cost."

    chris "The team that handled the product contracted Oripathy as a result."

    chris "They blamed my father for getting Oripathy, even despite knowing that being an Originium engineer means you may get Oripathy as a result."

    chris "But they refused to listen. Even as they were forcibly banished, they still blamed my father for it."

    chris "And it all went downhill from there."

    chris "Bearing the weight and guilt of what happened, my father quit."

    chris "Everyone knew it wasn't his fault, but he took responsibility anyway."

    chris "There was just one thing they did not know: I actually saw that power unit the night before."

    chris "I wanted to see it before anyone else, so I snuck into the lab."

    chris "When I saw the power unit, I felt a rush of excitement well up inside of me."

    chris "And then it started glowing. Almost as if it was calling out to me."

    chris "So I reached towards it. I touched it."

    chris "Nothing really... happened. The unit felt warm to the touch. And then it stopped glowing."

    chris "I could not figure out what happened, so I left it at that."

    chris "Of course, that was a mistake. A few days after that, I found out that my hand started growing black crystals."

    chris "You know about this, right? The symptoms of Oripathy."

    chris "My father was the first to find out. And once again, he blames himself."

    chris "He desperately sought to cover it up. From my mom. From my sisters. From everyone else."

    chris "Well, he was pretty bad at hiding stuff. My mom and sisters found it pretty much immediately."

    chris "They were definitely better at keeping secrets than my dad, though, so somehow I managed to evade any of the persecutions the Infected face on a daily basis."

    chris "I suppose I would be considered fortunate, then. Not once had I lived a life of hardship because I was an Infected."

    chris "However, I knew that I can't live like this eventually. So far we were successful in keeping it a secret. How long can we keep doing this, though?"

    chris "Against my entire family's protest, I decided to leave my hometown. Having known about what the Infected go through, I decided to find a cure for them."

    chris "I had heard of the Reunion movement. It is a noble movement, but their method does not exactly agree with me."

    chris "And that method is just standing around demanding someone else take action. Would it not be better if you yourself take action?"

    chris "Well, that's probably easier said than done. If it were possible, I would imagine Reunion would have done it."

    chris "Instead, I sought out clinics speciaiizing in Oripathy. Places like Azazel. And thankfully, they have allowed me to work part time as an intern."

    chris "The acting manager also mentioned a Rhodes Island. Apparently it's another pharmaceudical company that consists of Infected and non-Infected."

    hide chris neutral
    with fade

    scene room
    with fade

    show chris happy
    with dissolve

    chris "But yeah, that's that."

    protag "Wow, that's impressive."

    "Chris took a sip of tea, and chuckled."

    chris "It's not an extravagant story, but I hope it would at least be a positive one."

    protag "Yeah, it definitely is."

    chris "The acting manager did suggest that I go to Rhodes Island, though. Azazel, through a great company, is far too small."

    chris "The acting manager suggested that I broaden my horizons, or something. That I should see the world for myself, not just Chernobog."

    chris "So I probably will do that. Seek out and apply for a position at Rhodes Island."

    chris "And I was wondering. Would you like to join me? With your logistical and merchant abilities, I would think you would be helpful to Rhodes Island as well."

    protag "Me?"

    menu:
        chris "Well, who else? What do you say?"

        "I'm flattered you think that.":
            protag "If you think my skills would help, then I'm in."

            chris "Great! I'll ask the acting manager for a recommendation for you too."

            $ rhodesIsland += 1

        "Let me think about it a bit more.":
            protag "I'm not entirely sure if I want to continue as a merchant, anyway."

            chris "I think you'll do fine, but okay. There's no need to rush."

        "I think I'll pass.":
            protag "I don't think I'll fit in with a pharmaceudical company like Rhodes Island."

            chris "Coming from someone who does business with Azazel, that's not convincing at all. But, if you say so."

            $ reunion += 1

    chris "Thanks for hearing me out, though. I rarely get a chance to talk about my hometown."

    protag "No, no. Thank you for the tea. It was a very interesting story."

    chris "You're welcome."

    hide chris happy

    "I thanked Chris again before leaving his room."

    chris "Where did this come from? Well, whatever."

    "Looks like Chris is going to be cleaning up for a while yet."

    pause 1.0

    show street
    with fade

    "........."
    "......"
    "..."

    "Another week passed. The passing was uneventful."

    jump Backstory

# Bob's backstory event.
# Variables used:
# bob = Bob
# protag = Player

label Bob_backstory:

    scene warehouse
    with fade

    "Bob looks like he's grimancing over something."

    protag "Hey, what are you thinking about?"

    show bob normal

    bob "Oh, it's you."

    hide bob normal

    "Bob looks exhausted."

    show bob normal

    bob "Nothing. Just thinking."

    protag "About?"

    bob "...Have you ever known someone you cared for?"

    protag "That's kind of unexpected of you. Why?"

    menu:
        bob "Hah... Well, it's nothing. Don't worry about it."

        "If you say so.":
            pass

        "Come on, tell me what you're really thinking.":
            pass

    show bob normal

    bob "*sigh*"

    bob "Well, do you really want to know?"

    protag "I guess. But if you don't feel comfortable telling me, I'll stop hounding you."

    bob "No, it's fine."

    "Bob closed his eyes for a moment and took a deep breath."

    menu:
        "My story can be found in pretty much any history textbook. You could probably find at least a dozen like it."

        "Well yeah...":

            protag "That's not really surprising. History always has a nasty way of repeating itself."

        "Even so.":

            protag "It doesn't really discount you as a person."

    hide bob normal
    show bob cheer
    bob "Yeah, true."

    hide bob cheer
    show bob normal

    "Bob shrugged. It was as if my words had a sense of comfort over him."

    bob "This is a simple story of a dumb kid who didn't know any better."
    hide bob normal

    scene black
    with fade

    show bob normal

    bob "This kid was born to a simple family, in a simple city, in a simple country."

    bob "This family isn't completely wealthy, but it is also not poor. This family could put food on the table and keep everyone well fed."

    bob "This kid wants to go out and play. His parents always told him not to because of the Infected wandering about."

    bob "Naturally, the kid did not listen. Naturally, the kid did not understand why the Infected were bad."

    bob "One day, the parents and kid decided to go on a picnic at a nearby park."

    bob "So they went. And during that picnic, this kid met an old man."

    bob "A very kind old man. Loves children, like a lot of old people."

    bob "Problem is, this old man is an Infected. The kid did not know that."

    bob "How could he? The old man did cover it up."

    bob "It was idle chatter between the old man and the kid. The old man taught the kid stuff, the kid listened."

    bob "Because the both of them were having a great time, they decided to meet up again at that very park."

    bob "And so they did. Meeting after meeting, the kid slowly thought of the old man like his own grandpa."

    bob "Much like how the old man thought of the kid as his grandson."

    bob "...Until that day."

    bob "You know that once you're an Infected, it becomes increasingly difficult to hide it, right?"

    bob "Well, the old man was found out. The kid's parents found out about it by chance."

    bob "It would have ended rather peacefully, right? The parents take the kid away, warn the kid, and that's that."

    bob "If only reality was that kind."

    bob "The parents made a scene out of it. As a result, some nearby vigilantes were called into the park."

    bob "They grabbed the old man and forcefully rolled up his sleeves. Lo and behold, proof of the Infected."

    bob "The old man, oddly enough, did not resist. Perhaps he knew what his fate was."

    bob "The parents disciplined the child, pointing to the old man and not listening to them."

    bob "Then the old man spoke up. He asked to talk to the kid one more time."

    bob "The parents, and vigilantes, refused, of course. So the kid also begged."

    bob "Miraculously, they relented. And so the kid listened to the old man, not knowing that would be the last time they would ever speak."

    bob "The old man's words were very blunt."

    hide bob normal

    "Old Man" "Now you know the truth of this world. The truth of those deemed the Infected. Our fates have been decided the moment we became like this."

    "Old Man" "But I do not regret anything. Chatting with you is perhaps the greatest joy in whatever little life I have left."

    "Old Man" "I ask of you now one simple thing: to forget about me. To live on as though we have never met."

    show bob normal

    bob "The kid cried, of course. Saying stuff like 'No! I don't want to!' or 'Why can't we keep talking like this?'"

    bob "But the old man stayed silent, only shaking his head slowly."

    bob "The parents dragged the kid away. The vigilantes then surrounded the old man."

    bob "The kid of course never saw what happened, until later that night, when local news reported that an old man was beaten to death."

    bob "And of course, the parents pointed out that this is what the Infected deserved. What that old man deserved."

    bob "And because the kid disobeyed them, the kid would be grounded for a month."

    bob "Punishment for defying their parents. Punishment for getting close to the Infected."

    bob "A life lesson."

    bob "But the entire time, the one thing that kid could think about was why someone as kind as that old man deserved what he got."

    bob "Silly, right? You are systematically murdered for contracting a disease that is not your fault. Ludicrous world."

    "Bob took a deep breath before continuing."

    bob "Several years passed. This kid learns of the Reunion movement. It was a movement organized to protest against inhumane treatment towards the Infected."

    bob "Naturally, the kid, now grown up, decided to join the protest. He could not forget the old man no matter what, after all."

    bob "And like many protests, they end up violent because of some opportunists who decided to cause trouble and point the blame."

    bob "An explosion rocked the city hall. By sheer coincidence, that was very close to Reunion's rally."

    bob "And of course, the blame follows. Because it happened near the rally, people instantly jump to the conclusion that Reunion was behind it."

    bob "Overnight, Reunion was considered a group of terrorists who uses violence under the pretext of peace."

    bob "The bomb being made of Originium certainly did not help to argue against that."

    bob "As the result, the vigilantes used the bomb attack as justification to go after any Reunion supporters."

    bob "When Reunion held another rally inside an office building, another bomb went off. The building collapsed."

    bob "Many perished, either from the explosion or the collapse."

    bob "Of those who did survive? Coincidentally, they were confirmed to be Infected."

    bob "The bomb that went off that day had a special characteristic. It was the type that corrodes metal and weakens cement."

    bob "That bomb was designed specifically to destroy even the heaviest of fortifications. And it was used on a civilian building."

    menu:
        "That's horrible...":

            protag "It's really astonishing that anyone would even think of turning to violence to sabotage a peaceful message."

            hide bob normal
            show bob angry

            bob "Makes anyone's blood boil with anger."

            bob "Then again, you get idiots like them everywhere you look."

        "Did they ever find out who was behind the bombing attack?":

            protag "That's clearly a crime. Did they ever find who was responsible for it?"

            hide bob normal
            show bob angry

            bob "Just being reminded of their 'findings' make my blood boil."

            bob "The official statement is that an Infected, acting independantly from Reunion, resorted to terrorism."

            bob "Everyone knew how much bull that was, though. Everyone knew it was actually a rogue vigilante that carried it out."

            bob "There were people who absolutely hated the Infected and devised a scheme to use terrorism to turn everyone against the Infected. That rogue was one of them."

            bob "It's almost ludicrous how well it worked."

            bob "And of course, no one said a thing."

    hide bob angry
    show bob normal

    bob "Guess who was among the survivors of that office building. Yep. That kid."

    bob "Thankfully, injuries are minor. Unfortunately, the kid is tested and confirmed to have Oripathy."

    bob "As a result, the parents disowned the kid. Any questions towards them resulted in something like never knowing the kid or never giving birth to one."

    bob "Typical, really. At the end of the day, people will say whatever to save their own skin, even throwing their own flesh and blood under the bus."

    bob "The kid managed to escape from the hospital. Where did the kid go from there?"

    bob "Well, from being a part of the movement, the kid knew where Reunion was stationed at, so he went there."

    bob "Unfortunately, that place was cleaned out. Almost as though Reunion never existed."

    bob "Only one message was left. It was a simple sentence."

    bob "'The Infected will have their justice, one way or another.'"

    bob "Bummed but determined, the kid decided to scrounge out a living for himself, and eventually found his way to the wonderful city of Chernobog."

    bob "All this time, still holding the flames of Reunion, waiting for the day they return."

    hide bob normal
    with fade

    scene warehouse
    with fade
    show bob normal

    bob "And that's that. Not an exciting story, right?"

    protag "...Wow. I... um... I don't know what to say."

    bob "Well, like I said. It's not a unique story. You can find more like it in any history book."

    protag "People are fools, after all."

    hide bob normal
    show bob cheer

    bob "Right"

    hide bob cheer
    show bob normal

    bob "So? When Reunion gets back together, do you want to join me? We can put an end to the discrimination."

    protag "Huh?"

    bob "Reunion is no more, right now. But I believe they will come back. They definitely will."

    menu:
        protag "It would definitely make me feel better if I have someone watching my back, though."

        "Okay, I'm in!":
            protag "I definitely sympathize with you."

            bob "Awesome. I'm glad you agree with me."

            $ reunion += 1

        "Let me think about it a bit more. It is a big commitment.":
            protag "I would like to keep my options open right now."

            bob "Sure, there's no rush."

        "I'm sorry.":
            protag "Even though what happened to that old man was awful, I am a bit concerned about that message. So, I'll have to decline."

            bob "That's too bad."

            $ rhodesIsland += 1

    protag "But thank you for telling me all of this."

    bob "Yeah, sure. Honestly, being reminded of that is painful."

    hide bob normal

    "Bob shrugged again. The two of us waved each other goodbye, and then walked our separate ways."

    pause 1.0

    show street
    with fade

    "........."
    "......"
    "..."

    "Another week passed. The passing was uneventful."

    jump Backstory

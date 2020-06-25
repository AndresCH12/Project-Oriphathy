# This file will be called until all player choices have been exhausted at the very bottom
# Once again, by making use of the jump and label tags
# This entire file is a monologue by the player, so no name variables are used here

label choicebranch:

    scene street
    with fade

    "It's been a week since the checkup."

    "Aside from the fact that I became an Infected, life... did not seem to be much different."

    "The Infected are allowed to go grocery shopping. The Infected are allowed to dine out at restaurants."

    "All assuming the establishments even allow the Infected in."

    "Oripathy may be contagious, but it is not as though contraction of the disease is possible simply by being near one."

    "But to the normal person, such details matter little."

    "To the normal person, all they really need to know is that a disease called Oripathy exists, and those affected are called the Infected."

    "And as a result, the Infected are eyeballed with disgust. No surprises there."

    "Everywhere we look, the Infected attract unwanted attention to themselves."

    "Almost as if they are exotic animals, to the non-Infected."

    "But other than that, and maybe aside from the occasional assault by non-Infected, the Infected are typically left alone."

    "Pretty surprising, given that Chernobog is within Ursus territory."

    "The Ursus Empire is well known for their... forceful policies."

    "Infected are typically sentenced to death. Why Chernobog does not follow such a policy is a mystery."

    "Perhaps it is because the Ursus Empire is too large that enforcing their policies over a large landmass is proven more difficult than expected."

    "Perhaps not all of their policies are worth enforcing."

    "Perhaps it is impossible to exterminate an entire group of people."

    "Either way, the fact remains that the Infected are allowed to live relatively peacefully. So long as the Infected and non-Infected cross paths, anyway."

    scene street
    with fade

    "Well, this is a good time as any."

    # After viewing a character backstory, we return here. All lines above this are only displayed once.
    label Backstory:
    menu:
        "Now then, what should I do?"

        # Disappears after viewing this event
        "(Visit Bob)" if not Visit_Bob:
            $ Visit_Bob = True
            "I wonder if Bob is wandering around somewhere..."
            jump Bob_backstory

        # Disappears after viewing this event
        "(Visit Alice)" if not Visit_Alice:
            $ Visit_Alice = True
            "I wonder if Alice found any interesting novels lately..."
            jump Alice_backstory

        # Disappears after viewing this event
        "(Visit Chris)" if not Visit_Chris:
            $ Visit_Chris = True
            "I wonder if Chris scrounged up anything interesting lately..."
            jump Chris_backstory

        # This option will only display if all variables are set to true
        # By default, this is hidden
        "(Stay home.)" if Visit_Bob and Visit_Alice and Visit_Chris:
            "I think I'll stay home today and get some sleep."
            jump destruction_start

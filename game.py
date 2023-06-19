weapon = False

# Creating zombie encounter
def zombieMonster():
    actions = ["fight", "sneak"]
    global weapon
    print("A ravenous zombie has emerged in front of you, an insatiable appetite evident in its movements. You can either attempt to sneak past it, or muster up the courage to fight it. What will you choose to do?")
    userInput = ""
    while userInput not in actions:
        print("Choose: sneak or fight")  #input must be one of the keywords
        userInput = input()
        if userInput == "fight":
            if weapon:
                print("You run forward bravely, swinging the baseball bat at the zombies head. The zombie crumples to the ground, its body going limp. You move forward to find the front doors of the school wide opening, offering you escape from this nightmarish place. Congratulations! You have successfully escaped the zombie-infested school.")
            else:
                print("With a roar of courage, you rush at the zombie, only realizing at the last second that you are void of any weaponry or defense. The zombie easily bites your neck, killing you in an instant.")
            quit()      #the player has lost, the game has ended
        elif userInput == "sneak":
            print("You crouch in the shadows of the wall, the dark atmosphere of the school hallway hiding your presence from the zombie. You slowly make your way forward, successfully maneuvering past the zombie.")
            DeadBodiesRoom()
        else:
            print("Please enter one of the given choices.")

#Creating a new scenario with dead bodies
def DeadBodiesRoom():
    actions = ["move ahead", "turn around", "go right"]
    global weapon
    print("Quietly slipping through an ajar classroom door, you halt in shock as a pile of newly dead bodies lies to the right in front of you. It doesn't look like they were killed by a zombie. Is someone else in here with you? There is a closed door before you that seems to seeps with malice. Will you move ahead, turn around, or go right?")
    userInput = ""
    while userInput not in actions:
        print("Choose: move ahead, turn around, or go right")     #input must be one of the keywords
        userInput = input()
        if userInput == "move ahead":
            zombieMonster()
        elif userInput == "turn around":
            setUpTheStory()
        elif userInput == "go right":
            print("You cautiously move closer to inspect the bodies littering the ground. Something catches your eye, buried underneath all the limbs, and you reach down to pull out a wooden baseball bat from the jumble of corpses. You have obtained a weapon! Now will you move ahead or turn around?")
            weapon = True
            secondActions = ["move ahead", "turn around"]     #continue on with the game by asking again to choose
            userSecondInput = ""
            while userSecondInput not in secondActions:
                print("Choose: move ahead or turn around")
                userSecondInput = input()
                if userSecondInput == "move ahead":
                    zombieMonster()
                elif userSecondInput == "turn around":
                    setUpTheStory()
                else:
                    print("Please enter one of the given choices.")    #this is to check the second choice if user chooses to go right
        else:
            print("Please enter one of the given choices.")

#Creating a new scenario with noisy zombies
def manyZombieNoises():
    actions = ["cover ears", "hide", "turn around"]
    print("You enter a disheveled teachers lounge, dread building up as you realize the room is a dead end. Suddenly, a crescendo of undead growling becomes overwhelmingly loud and unbearable. It feels as though the sound alone is suffocating the room, and you are afraid your ears will burst. Is a hoard coming this way? You can either cover your ears, hide, or turn around. What will you do?")
    userInput = ""
    while userInput not in actions:
        print("Choose: cover ears, hide, or turn around")     #input must be one of these keywords
        userInput = input()
        if userInput == "cover ears":
            print("Unable to take the noise any longer, you cover your ears and close your eyes, perhaps unable to take the stress of the situation anymore, perhaps not wanting to see the cruel and gruesome ending you are about to meet. However, no matter how long you wait in the silence of your own fear, nothing happens. Opening your eyes in confusion, you realize you are back in your room as though nothing ever happened. Was it all a dream? Everything? Anyways, COngratulations! YOu have successfully escaped the zombie-infested school.")
            quit()
        elif userInput == "hide":
            print("With nowhere to continue forwards, and the sounds of zombies growing closer, you duck under a table and hold your breath, praying the tablecloth draped to the floor is enough to cover and keep you hidden. Unfortunately, zombies seem to be able to sense fear, as their arms reach under the table and drag you out into your demise.")
            quit()    #the player has lost, the game has ended
        elif userInput == "turn around":
            setUpTheStory()
        else:
            print("Please enter one of the given choices.")

#Creating a new scenario with a blood trail
def foundBloodTrail():
    actions = ["left", "right"]
    print("Carefully continuing on your trek through the school, you come across a T-intersection, with the hallway only splitting off to the left or to the right, unable to move forwards. A glimpse of red at the bottom of your vision pulls your focus down, and you notice a trail of blood on the floor that disappears down the flickering lights of the right path. Will you follow the blood trail to the right, or play it safe and go left?")
    userInput = ""
    while userInput not in actions:
        print("Choose: right or left")     #input must be one of these keywords
        userInput = input()
        if userInput == "right":
            humanEncounter()
        elif userInput == "left":
            print("Not taking a chance with the sinister aura that almost oozed from the right, you break into a sprint towards the left fork, almost crying in relief when you see a big sign above double doors that reads 'exit.' Congratulations! YOu have successfully escaped the zombie-infested school.")
            quit()
        else:
            print("Please enter one of the given choices.")

#Creating a new scenario with a mysterious human
def humanEncounter():
    actions = ["fight", "run away", "call out"]
    print("The lights suddenly flicker overhead, casting a faint silhouette of a hunched figure. You take a step back, unsure if the person in front of you has picked up on your presence. Are they friend...or foe? You can either decide to fight, call out, or run away. What will you do?")
    userInput = ""
    while userInput not in actions:
        print("Choose: fight, call out, or run away")     #input must be one of these keywords
        userInput = input()
        if userInput == "fight":
            print("Mustering up what courage you possess, you charge forwards, footsteps heavy against the silence between you two. However, the lights shut off for just a second, shrouding your surroundings in total darkness. When they come back, off for not more than a second, the man in the hallway is nowhere to be seen. Confused, you halt in your steps, now unsure if there was anyone else in here with you or if you were just seeing things.")
            foundBloodTrail()
        elif userInput == "run away":
            setUpTheStory()
        elif userInput == "call out":
            print("Deciding perhaps this man can offer help you call out to him, hoping the two of you can join forces to escape this school together. However, the mans profile does not so much as twitch in response. Looks like he doesn't want to speak...or can't. What will you do now?")
            secondActions = ["fight", "run away"]
            userSecondInput = ""
            while userSecondInput not in secondActions:
                print("Choose: fight or run away")
                userSecondInput = input()
                if userSecondInput == "fight":
                    print("Mustering up what courage you possess, you charge forwards, footsteps heavy against the silence between you two. However, the lights shut off for just a second, shrouding your surroundings in total darkness. When they come back, off for not more than a second, the man in the hallway is nowhere to be seen. Confused, you halt in your steps, now unsure if there was anyone else in here with you or if you were just seeing things.")
                    foundBloodTrail()
                elif userSecondInput == "run away":
                    setUpTheStory()
                else:
                    print("Please enter one of the given choices.")
        else:
            print("Please enter one of the given choices.")

def setUpTheStory():
    actions = ["north", "south", "east", "west"]
    print("You stand in front of a faded map of the school, trying to decide the fastest route to exit this place. The only company you have are the sounds of the snarling zombies pounding on the door you hastily barricaded. The direction of infested zombies you barely escaped from seems to be the north wing of the school, and from there splits off into an east wing, south wing, and west wing. What route will you choose to continue onwards?")
    userInput = ""
    while userInput not in actions:
        print("Choose: north, east, south, or west")
        userInput = input()
        if userInput == "east":
            DeadBodiesRoom()
        elif userInput == "south":
            humanEncounter()
        elif userInput == "west":
            manyZombieNoises()
        elif userInput == "north":
            print("Are you crazy? I just specifically stated that thats the direction you came from, infested with crazy zombies who want to eat you, and you want to go back? Do you have a death wish? No, I won't let you. Pick another direction.")
            secondActions = ["south", "east", "west"]
            userSecondInput = ""
            while userSecondInput not in secondActions:
                print("Choose: south, east, or west")
                userSecondInput = input()
                if userSecondInput == "east":
                    DeadBodiesRoom()
                elif userSecondInput == "south":
                    humanEncounter()
                elif userSecondInput == "west":
                    manyZombieNoises()
                else:
                    print("Please enter one of the given choices.")
        else:
            print("Please enter one of the given choices.")

if __name__ == "__main__":
    while True:
        print("The year is 3044.")
        print("A week ago a virus spread across the globe, turning those infected into hungry zombies who prey on others.")
        print("You are one of the few survivors, scavenging through towns and cities in search of supplies and food to survive.")
        print("However, one day you were quite unlucky, and became cornered in an abandoned school after being spotted and chased by a horde of zombies.")
        print("You must now find your way through and out of the school, with every action you make resulting in dire consequences.")
        print("Before we begin, what is your name?")
        userName = input()
        print("Be careful," +userName+ ", and choose your responses wisely.")
        setUpTheStory()

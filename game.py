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
            print("You cautiously move closer to inspect the bodies littering the ground. Something catches your eye, buried underneath all the limbs, and you reach down to pull out a wooden baseball bat from the jumple of corpses. You have obtained a weapon! Now will you move ahead or turn around?")
            weapon = True
            secondActions = ["move ahead", "turn around"]     #continue on with the game by asking again to choose
            userSecondInput = ""
            while userSecondInput not in actions:
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
        if userInput == "hide":
            print("With nowhere to continue forwards, and the sounds of zombies growing closer, you duck under a table and hold your breath, praying the tablecloth draped to the floor is enough to cover and keep you hidden. Unfortunately, zombies seem to be able to sense fear, as their arms reach under the table and drag you out into your demise.")
            quit()    #the player has lost, the game has ended
        if userInput == "turn around":
            setUpTheStory()
        else:
            print("Please enter one of the given choices.")

#Creating a new scenario with a journal
def foundJournal():
    actions = ["left", "right"]

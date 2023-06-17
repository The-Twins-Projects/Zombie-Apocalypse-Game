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

def DeadBodiesRoom():
    actions = ["Move ahead", "Turn around", "Go right"]
    global weapon
    print("Quietly slipping through an ajar classroom door, you halt in shock as a pile of newly dead bodies lies to the right in front of you. It doesn't look like they were killed by a zombie. Is someone else in here with you? ")

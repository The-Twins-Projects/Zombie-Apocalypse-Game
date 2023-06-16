weapon = False

# Creating zombie encounter
def zombieMonster():
    actions = ["fight", "sneak"]
    global weapon
    print("A ravenous zombie has emerged in front of you, its insatiable appetite evident in its movements. You can either attempt to sneak past it, or muster up the courage to fight it. What will you choose to do?")
    userInput = ""
    while userInput not in actions:
        print("Choose: sneak or fight")
        userInput = input()
        if userInput == "fight":
            if weapon:
                print("You run forward bravely, swinging the baseball bat at the zombies head. The zombie crumples to the ground, its body going limp. You move forward to find the front doors of the school wide opening, offering you escape from this nightmarish place. Congratulations! You have escaped.")
            else:
                print("With a roar of courage, you rush at the zombie, only realizing at the last second that you are void of any weaponry or defense. The zombie easily bites your neck, killing you in an instant.")
            quit()
        elif userInput == "sneak":
            print("You crouch in the shadows of the wall, the dark atmosphere of the school hallway hiding your presence from the zombie. You slowly make your way forward, successfully maneuvering past the zombie.")
            showDeadBodies()
        else:
            print("Please enter one of the given choices.")


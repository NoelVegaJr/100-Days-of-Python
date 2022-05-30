print("Welcome to treasure island.")
print("Your mission is to find the treasure.")

response = input("You're at a crossroad. Where do you want to go? Type \"left\" or \"right\"\n")

if response != "left":
    print("Fall into a hole.\nGame Over.")
else:
    print("You've come to a lake. There is an island in the middle of the lake.")
    response = input("Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n")

    if response != "wait":
        print("Attacked by trout.\nGame Over.")
    else:
        print("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue.")
        response = input("Which colour do you choose?\n")

        if response == "red":
            print("Burned by fire.\nGame Over.")
        elif response == "blue":
            print("Eaten by beasts.\nGame Over.")
        elif response == "yellow":
            print("You found the treasure!\nCongratulations. You Won!")
        else:
            print("Witch made stew out of you\nGame over.")
    

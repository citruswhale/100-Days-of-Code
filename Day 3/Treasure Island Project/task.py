import pics

print(pics.ship)
print("Ahoy mates let's find some treature!")
print("You are on a deserted island with a map that leads to a hidden treasure.")
print("You have a compass, a map, and a first aid kit.")
print("You are standing on a sandy beach with a dense jungle in front of you.")
print("You see a small cave to your left and a steep cliff to your right.")
choice = input("What do you do? type \"left\" or \"right\".\n").lower()
if choice == "left":
    print("You have reached a lagoon inside the cave.")
    print("There is a small patch of sand with gold glistening in the centre.")
    choice = input("Do you wish to swim or wait for a boat? Type \"swim\" or \"wait\".\n").lower()
    if choice == "wait":
        print("You wait for a boat and after a while a small boat arrives.")
        print("You get on it and travel till the boat docks against the patch of sand.")
        print("There are three doors in front of you, a blue one, a red one and a yellow one.")
        print("Only one of these door allows you to exit the boat safely.")
        choice = input("Which door do you choose? Type \"blue\", \"red\" or \"yellow\".\n").lower()
        if choice == "yellow":
            print("You have chosen the colour of treasure, the correct door and you exit the boat safely.")
            print("You have found the treasure and you are now rich.")
            print("You have been chosen to be a partner of the infamous company, Google! 😌")
            print()
            print(pics.box)
        else:
            print("You have chosen the wrong door and you become a corporate slave for the rest of your life! 😶‍🌫️")
            print()
            print(pics.comp)
    else:
        print("Oh no! A giant Octocat pulls you to the bottom of the ocean and slaps the life out of you 🐙.")
        print("You end up as its midnight snack!")
        print(pics.octo)
else:
    print("You reach the top of the cliff, but it breaks and you fall to your death. ☠️ Ouchie.")
    print()
    print(pics.mount)

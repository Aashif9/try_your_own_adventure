def start_adventure():
    print("Welcome to the Jungle Adventure!")
    print("You're standing at the entrance of a mysterious jungle.")
    print("Do you want to ENTER or RUN AWAY?")
    choice1 = input("Type 'enter' or 'run': ").lower()

    if choice1 == "enter":
        jungle_path()
    elif choice1 == "run":
        print("You chose to run away. Maybe next time!")
    else:
        print("Invalid choice. Game Over.")

def jungle_path():
    print("\nYou walk into the jungle and come to a fork in the path.")
    print("Do you go LEFT towards the dark cave or RIGHT towards the river?")
    choice2 = input("Type 'left' or 'right': ").lower()

    if choice2 == "left":
        cave()
    elif choice2 == "right":
        river()
    else:
        print("You stood there too long. A snake bit you. Game Over.")

def cave():
    print("\nYou enter the cave and find a treasure chest!")
    print("Do you OPEN it or LEAVE it alone?")
    choice3 = input("Type 'open' or 'leave': ").lower()

    if choice3 == "open":
        print("You found gold and jewels! You're rich!")
    elif choice3 == "leave":
        print("You leave it behind and walk away... peacefully. Game over.")
    else:
        print("Hesitation is dangerous. A bat startled you. You ran away.")

def river():
    print("\nAt the river, you see a boat and a bridge.")
    print("Do you take the BOAT or CROSS the bridge?")
    choice4 = input("Type 'boat' or 'bridge': ").lower()

    if choice4 == "boat":
        print("The boat had a leak... You sank. Game Over.")
    elif choice4 == "bridge":
        print("You crossed safely and reached a village. You're safe!")
    else:
        print("You waited too long. A crocodile appeared. Game Over.")
start_adventure()

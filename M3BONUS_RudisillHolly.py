# Holly Rudisill
# 09/29/2026
# M3BONUS - Let's Make a Deal
# A short text adventure. The player picks a door and wins a prize.

"""
PSEUDOCODE
Display the welcome banner
Ask the player to pick door 1, 2, or 3
If the player picks 1: go to the goat room
Else if the player picks 2: go to the car room
Else if the player picks 3: go to the briefcase room
Else: the host says that is not a door
"""

def door_1():
    print()
    print("Door 1 swings open.")
    print("A goat looks at you. It is chewing your ticket.")
    print("You win: one goat.")


def door_2():
    print()
    print("Door 2 swings open.")
    print("Lights flash. A small red car rolls out.")
    print("You win: a car.")


def door_3():
    print()
    print("Door 3 swings open.")
    print("A briefcase sits on a stool.")
    print("You win: the briefcase.")
    # TO DO (Part C): start the Buzzer Round from here.


def start():
    print("=" * 40)
    print("     WELCOME TO LET'S MAKE A DEAL")
    print("=" * 40)
    choice = int(input("Pick a door (1, 2, or 3): "))

    if choice == 1:
        door_1()
    elif choice == 2:
        door_2()
    elif choice == 3:
        door_3()
    else:
        print("The host frowns. That is not a door.")


# This line starts the game. Leave it at the bottom of the file.
start()

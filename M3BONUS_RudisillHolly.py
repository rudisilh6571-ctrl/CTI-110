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

    print()
    # TO DO (Part C): start the Buzzer Round from here.
    print("The host smiles. 'Time for the buzzer round.'")
    print()

    print("Hold the buzzer as long as you can.")
    print("The first 40 seconds pay the base rate.")
    print("Every second over 40 pays 1.5 times the base rate.")
    time_used = float(input("How many second did you hold the buzzer? "))
    print("Dollars per second: 10")
    print()

    print('------------ PRINT RECEIPT ------------')
    max_time = 60
   
    time_left = max_time - time_used

    if time_used > 40:
        base_winnings = 40 * 10 
        bonus_time = time_used - 40 
        bonus = bonus_time * 15
        total_winnings = bonus + base_winnings
    else:
        bonus = 0
        total_winnings = bonus + base_winnings

    # f-sting display of the prize and bonus
    print(f"{"Prize: ":<20}{"Briefcase":<10}")
    print(f"{"Seconds held: ":<20}{time_used:<10.2f}")
    print(f"{"Bonus seconds: ":<20}{bonus_time:<10.2f}")
    print(f"{"Base Pay: ":<20}${base_winnings:<10.2f}")
    print(f"{"Bonus Pay: ":<20}${bonus:<10.2f}")
    print(f"{"Total winnings: ":<20}${total_winnings:<10.2f}")

def start():
    print("=" * 40)
    print("     WELCOME TO LET'S MAKE A DEAL")
    print("=" * 40)
    choice = float(input("Pick a door (1, 2, or 3): "))

    if choice == 1:
        door_1()
    elif choice == 2:
        door_2()
    elif choice == 3:
        door_3()
    else:
        print("The host frowns. That is not a door.")

print(('-') * 40)
# This line starts the game. Leave it at the bottom of the file.
start()

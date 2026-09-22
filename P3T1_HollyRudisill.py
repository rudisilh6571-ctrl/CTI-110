# Holly Rudisill    
# 09/22/2026
# P3T1
# If statement practice

# main()  this is a program starting point
# you dont need to use it, but it is a very good idea
def main():
    # Part 1 - level check - what level the payer is at determining if they are high enough level to defeat the boss later 
    print("Hello and welcome to the dungeon")
    level = int(input("What is your level? "))
    if level >= 21:
        print("You can enter the dragon's spire dungeon")
    else:
        print("Try leveling up first.")

    #part 2 list your potions conditions for having enough potions

    potions = int(input("How Many potion do you have? "))
    if potions == 0:
        print("You need potions to go into the dungeon, come back when you have acquired health potions")
    elif potions == 1:
        print(f"You have {potions} potion.")
    elif potions > 1:
                print(f"You have {potions} potions.")
    else:
            print(f"How did you get {potions}, that is less than zero.")

    # part 3 Battle Boss conditions for winning the game 
    print("You are facing the Deluxe Orge")
    print("This will be a hard fight")
    if level >= 25:
            # possible to win
          if potions >3:
                print("It takes three potions to get him to low health.")
                print("You Win!")
          else:
                print("You ran out of healing before he was weakened")
                print("Game Over!")
    else:
          print("His armor is too strong!")
          print("Game Over!")

#at the bottom -- start the program
main()
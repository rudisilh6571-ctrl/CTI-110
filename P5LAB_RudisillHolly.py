# Holly Rudisill
# 10/27/2026
# P5LAB 
# simulate a self checkout machine with a randomizer for the totaled owed

import random


def main():
    print(f"You Owe ${disperse_change(amount_owed)}")
    # User Input
    amount = float(input("How much cash will you put in the self-checkout? $"))
    # amount = round(amount * 100)
    print(f"")


def disperse_change(amount_owed):
    amount_owed = round(random.uniform(0.01, 100.00), 2)
   
    # calculates the input and multiples by 100 to give a whole number
    dollars = amount // 100
    amount = amount % 100

    # takes out each denominations (ie. quarter, nickel and dime) and leave the remainder to calculate out the next change out

    if dollars == 1:
        print(f"{dollars} Dollar") # how many dollars fit
    elif dollars > 1:
        print(f"{dollars} Dollars") # what is left over 
    
        
    quarters = amount // 25
    amount = amount %  25
    if quarters == 1:
        print(f"{quarters} Quarter")
    elif quarters > 1:
        print(f"{quarters} Quarters")

    dimes = amount // 10
    amount = amount %  10
    if dimes == 1:
        print(f"{dimes} Dime")
    elif dimes > 1:
        print(f"{dimes} Dimes")


    nickels = amount // 5
    amount = amount %  5
    if nickels == 1:
        print(f"{nickels} Nickel")
    elif nickels > 1:
        print(f"{nickels} Nickels")

    pennies = amount // 1
    amount = amount %  1
    if pennies == 1:
        print(f"{pennies} Penny")
    elif pennies > 1:
        print(f"{pennies} Pennies")
    elif dollars == 0:
        print("No change")  #if user inputs 0.00 this is the only thing that prints


main()
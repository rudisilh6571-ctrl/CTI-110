# Holly Rudisill
# 10/29/2026
# P5LAB 
# simulate a self checkout machine with a randomizer for the totaled owed

import random # to import ramdom operations

def disperse_change(amount):
    # displays change
    print(f"Change is: {amount:.2f}")
    print("")
    # print out the change 
    amount = round(amount * 100)
    
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
    

def main(): # Dispays a menu of things and other functions does the task**
    # declare variables
    cost = 0.0
    amount_paid = 0.0
    change_owed = 0.0
    print("Welcome to the self-checkout simulator.")
    cost = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe ${cost:.2f}")
    # Ask use how much they will put in
    amount_paid = float(input("How much cash will you put in the self-checkout? $"))
    # calculate change owed
    change_owed = amount_paid - cost
    print("")
    disperse_change(change_owed)


main()
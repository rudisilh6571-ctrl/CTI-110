# Holly Rudisill    
# 09/24/2026
# P3LAB
# This program allows the user to enter a money (float) value with two places after the decimal

# User Input
amount = float(input("Enter the amount of money as a float: $"))
amount = round (amount * 100)

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
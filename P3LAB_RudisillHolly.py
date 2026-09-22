# Holly Rudisill    
# 09/10/2026
# P2LAB1
# This program allows the user to enter a money (float) value with two places after the decimal

# User Input
amount = float(input("Enter the amount of money as a float: $"))
dollars = amount // 1
print(f"{dollars}")
remainder = amount % 1   
print(f"{remainder:.2f}")
quarters = remainder // .25
print(f"{quarters:.0f}")
dimes = remainder // .10
print(f"{dimes:.0f}")
nickels = remainder / .05
print(f"{nickels:.0f}")
pennies = remainder // .01
print(f"{pennies:.0f}")
#if else statements to get the right output for each denomination of money


if dollars == 1:
    print(f"{dollars:.0f} Dollar")
else:
    print(f"{dollars:.0f} Dollars")

if quarters < 1:
    print(f"{quarters:.0f} Quarter")
else:
    print(f"{quarters:.0f} Quarters")

if dimes < 1:
    print(f"{dimes:.0f} Dime")
else:
    print(f"{quarters:.0f} Dimes")
#else:
    #print("No change")


"""
dollars = amount
quarters =
dimes = 
nickels = 
pennies = 
"""

"""
# Output
print(f"{amount} Dollars")
print(f"{amount} Dollar")
print(f"{amount} Quarters")
print(f"{amount} Quarter")
print(f"{amount} Dimes")
print(f"{amount} Dime")
print(f"{amount} Nickels")
print(f"{amount} Nickel")
print(f"{amount} Pennies")
print(f"{amount} Penny")
"""
# Holly Rudisill    
# 09/08/2026
# P1HW2
# Create a program that does some basic math on numbers that are entered

print("This program calculates and displays travel expenses")
print()
budget = int(input("Enter Budget: "))
print()
travel_dest = input("Enter your travel destination: ")
print()
gas_money = int(input("How much do you think you will spend on gas? "))
print()
accomodations = int(input("Approximately, how much will you need for accomodation/hotel? "))
print()
food_money = int(input("Last, how much do you need for food? "))

print()
print("-----------------Travel Expenses------------------")

print(f"Location: {travel_dest}")
print(f"Initial Budget: {budget}")
print()

print(f"Fuel: {gas_money}")
print(f"Accomodation: {accomodations}")
print(f"Food: {food_money}")
print()
expenses =  gas_money + accomodations + food_money 

remaining = budget - expenses
print()
print(f"Remaining Balance: {remaining}")
#print(f"{base_value} to the {exponent} power is {result} !!")1200
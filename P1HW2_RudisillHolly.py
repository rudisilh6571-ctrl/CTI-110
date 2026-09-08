# Holly Rudisill    
# 09/08/2026
# P1HW2
# Create a program that does some basic math on numbers that are entered

budget = int(input("Enter Budget: "))

travel_dest = input("Enter your travel destination: ")

gas_money = float(input("How much do you think you will spend on gas? "))

accomodations = float(input("Approximately, how much will you need for accomodation/hotel? "))

food_money = float(input("Last, how much do you for food? "))

print()
print("-----------------Travel Expenses------------------")

print(f"Location: {travel_dest}")
print(f"Initial Budget: {budget}")
print()

print(f"Fuel: {gas_money}")
print(f"Accomodation: {accomodations}")
print(f"Food: {food_money}")

expenses =  gas_money + accomodations + food_money 

remaining = budget - expenses

print(f"Remaining Balance: {remaining}")
#print(f"{base_value} to the {exponent} power is {result} !!")1200
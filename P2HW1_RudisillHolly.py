# Holly Rudisill
# 09/15/2026
# P2HW1
# Work exactly as was requested for P1HW2, only the output will be nicely formatted

print("This program calculates and displays travel expenses")
print()

# Asking user to enter the values of the destination, budget, and 3 expenses
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
# Differnt way to print the title with dashes
print('-' * 17, "Travel Expenses", '-' * 17)

# Displaying the values that the user inputted
print(f"{"Location:":25s} {travel_dest}")
print(f"{"Initial Budget:":25s} ${budget:.2f}")

print(f"{"Fuel:":25s} ${gas_money:.2f}")
print(f"{"Accomodation:":25s} ${accomodations:.2f}")
print(f"{"Food:":25s} ${food_money:.2f}")
# can also use print('-' * 51)
print("---------------------------------------------------") 

# Calculating expenses and remaining budget after expenses are added together
expenses =  gas_money + accomodations + food_money 
remaining = budget - expenses
print()

# Displaying the remainder of the user's travel budget
print(f"Remaining Balance: {remaining}")

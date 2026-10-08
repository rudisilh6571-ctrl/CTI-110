# Holly Rudisill
# 10/8/2026
# P4LAB2
# Use loops to display customer information 

# Ask use for Integer

print("Program Running with positive integer input")
user = "yes"
while user == "yes":   # runs the program if user is yes
    number = int(input("Enter an integer: "))
    i = 1
    if number >= 0:
        for i in range(1 , 13):
            total = number * i
            print(f"{number} * {i} = {total}")
        user = input("Would you like to run the program again? ")
    else:
        print("This program does not handle negative numbers.")

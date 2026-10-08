# Holly Rudisill
# 10/8/2026
# P4LAB2
# Use loops to display multiplication of positive integer times 1-12, does not accept negative integers

# Ask use for Integer

print("Program Running with positive integer input")
user = "yes"
while user != "no":   # runs the program if user is yes
    number = int(input("Enter an integer: ")) # asks user for input
    print()
    i = 1
    if number >= 0: # if user input is >= 0 run the calculations
        for i in range(1 , 13): # set it to range 1 thru 12 to multiply with user input
            total = number * i # calculations for multiplication table with users positive integer
            print(f"{number} * {i} = {total}") # show multiplication table
        print()    
        user = input("Would you like to run the program again? ") # request to see if user would like to run the program again
        print()
    else:
        print("This program does not handle negative numbers.") # prints if user choose number less than 0
print()
print("Exiting program...") # exits program if user does not choose yes for running the program again 
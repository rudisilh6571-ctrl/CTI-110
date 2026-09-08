# Holly Rudisill    
# 09/08/2026
# P1HW1
# Write code that collects information from user, processes information collected and display results to user

print("-----Calculating Exponents-----")
print()
# Part 1 Calculating  Exponents

base_value = int(input("Enter integer as the base value: "))
exponent = int(input("Enter integer as the exponent: "))

result = base_value ** exponent # 3**2 is three squared

print(base_value, "raised to the power of", exponent, "is", result, "!!")
# Antoher way to print the result.   print(f"{base_value} to the {exponent} power is {result} !!")

print() 
print()
print("-----Addition and Subtraction-----")
print()
# Part 2 Addition and Subtraction
# 3 numbers, start, add_this, sub_this
start = int(input("Enter the starting integer: "))
print("you typed", start)

add_this = int(input("Enter integer to add: "))
sub_this = int(input("Enter integer to subtract: "))

# Calculate the answer
answer = start + add_this - sub_this

# Print the answer print() print() also gives you two lines 
print("\n\n")
# should look like: "10 + 4 - 2 is equal to 12"
# Another way to print the answer   print(start, "+", add_this, "-", sub_this, "is equal to", answer) 
print(f"{start} + {add_this} - {sub_this} is equal to {answer}")
# Holly Rudisil
# #P4LAB1
# 10/01/2026
# for and while loop build a turtle

import turtle

# loop to create a turtle 
for number in range(7):
    print(number)

num = float(input("Enter a decimal value between 1 and 20: "))

while num < 1.0 or num > 20.0:
    print("Number is not in range")
    num = float(input("Try again: "))

print(f"Yay, you finally gave a valid value, {num}")
    
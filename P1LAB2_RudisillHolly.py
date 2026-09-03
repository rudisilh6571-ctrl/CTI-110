#Holly Rudisill
# 09/3/2026
# P1LAB2 Product Sales
# A program that demonstrates Input, Processing, and Output by calculating product sales.

#INPUT
#product_name = input("Enter your Product Name ")
#count = int("Enter Quantity ")
#unit_price = float("Enter Unit Price ")

#Change these to your own values for testing
product_name = "Hook"
count = 100 
unit_price = 39.99

#PROCESSING
total = count * unit_price

#OUTPUT
print("Welcome to the", product_name, "store.")
print("We have", count, product_name, "(s) at $", unit_price, "per unit.") 
print("Total cost for the all units is", f"${total:.2f}")




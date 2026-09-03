#Holly Rudisill
# 09/3/2026
# P1LAB2 Product Sales
# A program that demonstrates Input, Processing, and Output by calculating product sales.

#INPUT

#Instead we ask the user
#print("STORE STARTUP")
#print("_" * 10) # ten _ in a row
#product_name = input("Enter your Product Name: ")
#count = int(input("Enter Quantity: "))
#unit_price = float(input("Enter Unit Price: "))

#Hard coding sets values directly
product_name = "Hook"
count = 100 
unit_price = 39.99

#PROCESSING
total = count * unit_price
#Alternative to int and float conversion
#count = int(count) #convert string to integer: "100" -> 100
#unit_price = float(unit_price) #convert string to float: "3.25" -> 3.25
#total = count * unit_price # requires two numbers, returns a third number

#OUTPUT
print("Welcome to the", product_name, "store.")
print("We have", count, product_name, "(s) at $", f"{unit_price:.2f}", "per unit.") 
print("Total cost for the all units is", f"${total:.2f}")

#alternative method for two decimal places
#print(f"We have" {count} {product_name}(s) at ${unit_price:.2f} per unit.) 
#print(f"Total is: ${total:.2f}")




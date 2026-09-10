# Holly Rudisill    
# 09/10/2026
# P2LAB1
# Write code that uses a dictionary to store user input and displays output to the user

# input - create keys and values and request user to picka model from key


thisdict = {
  "Camaro": 18.21,
  "Prius": 52.36,
  "Model S": 110,
  "Silverado": 26
}

keys = thisdict.keys()

model = input("Enter a vehicle to see its mpg: ")
mpg = thisdict.values()
distance = float(input("How many miles will you drive the ", get.model, " ? "))

# processing - calculate the amount of gas need to drive the miles the user inputs

gallons = mpg * distance


# output

print(keys)

print(f"The {model} gets {mpg:.2f} .")

print(f"{gallons:.2f}(s), of gas are needed to drive the {model} {distance} miles.")
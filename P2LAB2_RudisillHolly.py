# Holly Rudisill    
# 09/15/2026
# P2LAB1
# Write code that uses a dictionary to store user input and displays output to the user

# input - create keys and values and request user to picka model from key


thisdict = {
  "Camaro": 18.21,
  "Prius": 52.36,
  "Model S": 110,
  "Silverado": 26
}

# Get keys from dictionary
keys = thisdict.keys()
print(keys)
print()
# First input output pair, Model and MPH for that Model
model = input("Enter a vehicle to see its mpg: ")
print()
mpg = thisdict[model]
print(f"The {model} gets {mpg:.2f} mpg.")
print()

# Ask for user input on how many miles they will drive
distance = float(input(f"How many miles will you drive the {model}? "))
print()

# processing - calculate the amount of gas need to drive the miles the user inputs and output results
gallons = distance / mpg 
print(f"{gallons:.2f} gallons(s), of gas are needed to drive the {model} {distance} miles.")
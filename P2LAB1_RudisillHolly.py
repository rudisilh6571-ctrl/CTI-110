# Holly Rudisill    
# 09/10/2026
# P2LAB1
# Write code that performs mathematical calculations and displays information to users

# Add math module so you can calculate with pi
import math

# Input of value for the circle
radius = float(input("What is the radius of the circle? "))
print()

# Processing - diameter = 2r, circumference = 2 pi r and area = pi x r^2
diameter = 2 * radius

circumference = 2 * math.pi * radius 

area = math.pi * radius ** 2

# Output

print("The diameter of the circle is",f"{diameter:.1f}")
print()

print("The circumference of the circle is", f"{circumference:.2f}")
print()

print("The area of the circle is", f"{area:.3f}")
print()

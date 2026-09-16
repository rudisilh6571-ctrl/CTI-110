# Holly Rudisill
# 09/15/2026
# P2HW2
# Write a program that asks the user to enter test grades for the following modules, using a separate input statement for each one

# Ask user to each module grade

mod1 = float(input("Enter grade for Module1: "))
mod2 = float(input("Enter grade for Module2: "))
mod3 = float(input("Enter grade for Module3: "))
mod4 = float(input("Enter grade for Module4: "))
mod5 = float(input("Enter grade for Module5: "))
mod6 = float(input("Enter grade for Module6: "))

# Calculate the grades, lowest, highest, sum and average

grade_list = [mod1, mod2, mod3, mod4, mod5, mod6]
print(grade_list)


# Print the result of the grade lowest, highest, sum, and average
print(('-') * 12, "Results", ('-') * 12)

print(f"{"Lowest Grade":20s} {lowest_grade:.2f}")
print(f"{"Highest Grade":20s} {highest_grade:.2f}")
print(f"{"Sum of Grades":20s} {sum_grades:.2f}")
print(f"{"Average":20s} {average:.2f}")


print(('-') * 40)


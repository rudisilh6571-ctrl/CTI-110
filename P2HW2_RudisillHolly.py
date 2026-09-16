# Holly Rudisill
# 09/16/2026
# P2HW2
# Write a program that asks the user to enter test grades for the following modules, using a separate input statement for each one

# Ask user to each module grade

mod1 = float(input("Enter grade for Module1: "))
mod2 = float(input("Enter grade for Module2: "))
mod3 = float(input("Enter grade for Module3: "))
mod4 = float(input("Enter grade for Module4: "))
mod5 = float(input("Enter grade for Module5: "))
mod6 = float(input("Enter grade for Module6: "))

# Storing all the grades in a list
grade_list = [mod1, mod2, mod3, mod4, mod5, mod6]
# to test if my list populated correctly print(grade_list)

# Calculate the grades, lowest, highest, sum and average

lowest_grade = min(grade_list)
highest_grade = max(grade_list)
sum_grades = sum(grade_list)
average = sum(grade_list) / len(grade_list)


# Print the result of the grade lowest, highest, sum, and average and format the output
print(('-') * 12, "Results", ('-') * 12)

print(f"{"Lowest Grade":21s} {lowest_grade}")
print(f"{"Highest Grade":21s} {highest_grade}")
print(f"{"Sum of Grades":21s} {sum_grades}")
print(f"{"Average":21s} {average:.2f}")


print(('-') * 40)


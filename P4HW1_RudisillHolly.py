# Holly Rudisill
# 10/8/2026
# P4HW1
# Write a program that asks the user to enter test grades for the following modules, using a separate input statement for each one

# Ask user to each module grade

num_scores = int(input("How many score do you want to enter? "))
#while num_scores <= num_scores:
# if num_scores >= 1:
i = 0
for i in range(1, num_scores + 1):
    user_scores = float(input(f"Enter score #{i} "))
# print("Exit program")
# print("INVALID score entered!")
# print("Score should be between 0 and 100.")

# Storing all the grades in a list
grade_list = []
grade_list.append[user_scores]
print(f"{grade_list}")

"""
mod1 = float(input("Enter grade for Module1: "))
mod2 = float(input("Enter grade for Module2: "))
mod3 = float(input("Enter grade for Module3: "))
mod4 = float(input("Enter grade for Module4: "))
mod5 = float(input("Enter grade for Module5: "))
mod6 = float(input("Enter grade for Module6: "))
"""

# to test if my list populated correctly print(grade_list)

# Calculate the grades, lowest, highest, sum and average

lowest_grade = min(grade_list)
modified_list = max(grade_list)
average = sum(grade_list) / len(grade_list)
grade_letter = (grade_list)

# Print the result of the grade lowest, highest, sum, and average and format the output
print("------------Results------------")

print(f"{"Lowest Grade:":21s} {lowest_grade}")
print(f"{"Modified List:":21s} {modified_list}")
print(f"{"Average:":21s} {average:.2f}")
print(f"{"Grade:":21s} {grade_letter}")


print(('-') * 40)


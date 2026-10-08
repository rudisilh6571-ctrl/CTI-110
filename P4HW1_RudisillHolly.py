# Holly Rudisill
# 10/8/2026
# P4HW1
# Write a program that asks the user to enter test grades for the following modules, using a separate input statement for each one

# Ask user to each module grade
numof_scores = int(input("How many score do you want to enter? "))

grade_list = []

for scores in range(1, numof_scores + 1):

    # Storing all the grades in a list
    grade = float(input(f"Enter score #{scores}: "))
    # num = grade_list()        
    while grade < 0 or grade > 100:
        print()
        print("INVALID score entered!!!!")
        print("Score should be between 0 and 100")
        grade = float(input(f"Enter score #{scores} again: "))
    grade_list.append(grade)
print()    
        
        

# test to make sure list is printing correctly
# print(f"{grade_list}")

# Calculate the grades, lowest, modified list, and average

lowest_grade = min(grade_list)
# drop the lowest score and then do average score and modified list
grade_list.remove(lowest_grade)
# list printed without lowest score
modified_list = (grade_list)
average = sum(grade_list) / len(grade_list)
# grade_letter = (grade_list) did not need to calcute grade letter using if/elif statement instead

# Give letter grade based on average score

if average >= 90:
    grade_letter = "A"
elif average >= 80:
    grade_letter = "B"
elif average >= 70:
    grade_letter = "C"
elif average >= 60:
    grade_letter = "D"
else: 
    grade_letter = "F"

# Print the result of the grade lowest, modified list, average of the scores, and letter grade of the average and format the output
print("--------------Results------------")

print(f"{"Lowest Grade":14s} {":"} {lowest_grade}")
print(f"{"Modified List":14s} {":"} {modified_list}")
print(f"{"Scores Average":14s} {":"} {average:.2f}")
print(f"{"Grade":14s} {":"} {grade_letter}")


print(('-') * 40)


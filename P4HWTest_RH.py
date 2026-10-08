# Holly Rudisill
# Test file for P4HW1

numof_scores = int(input("How many score do you want to enter? "))
#while num_scores <= num_scores:

grade_list = []
# looping thru number of grade user will enter
for scores in range(1, numof_scores + 1):
    if scores <= 100 and scores >= 0:
        # Storing all the grades in a list
        grade_list.append(float(input(f"Enter score #{scores} ")))
    else:    
        print("INVALID score entered!")
        print("Score should be between 0 and 100.")




# test to make sure list is printing correctly
# print(f"{grade_list}")

# Calculate the grades, lowest, modified list, and average

lowest_grade = min(grade_list)
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

print(f"{"Lowest Grade":<14} {":"} {lowest_grade}")
print(f"{"Modified List":<14} {":"} {modified_list}")
print(f"{"Scores Average":<14} {":"} {average:.2f}")
print(f"{"Grade":<14} {":"} {grade_letter}")


print(('-') * 40)

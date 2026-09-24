# Holly Rudisill
# 09/24/2026
# P3HW1
# debug and fix existing code ** This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
# TO DO: determine lowest, highest , sum and average for grades

low = min(grades)
high = max(grades)
sumof = sum(grades)
average =  sum(grades) / len(grades)
print()
# determine letter grade for average
# print(average)

print("------------Results------------")

print(f"{"Lowest Grade:":19s} {low}")
print(f"{"Highest Grade:":19s} {high}")
print(f"{"Sum of Grades:":19s} {sumof}")
print(f"{"Average:":19s} {average:.2f}")

# print which letter grade the student earned based on their average
print(('-') * 40)

if average >= 90:
    print('Your grade is: A')
elif average >= 80:
    print('Your grade is: B')
elif average >= 70:
    print('Your grade is: C')
elif average >= 60:
    print('Your grade is: D')
else:
    print('Your grade is: F')



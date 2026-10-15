# Holly Rudisill
# 10/15/2026
# P4HW2
# Salary calculator for multiple employees

# Request employees info
name = input("Enter employee's name or 'Done' to terminate: ")

# create accumaltor variables for overtime pay , regular pay, gross pay and employee count

overtimepay_total = 0
regularpay_total = 0
grosspay_total = 0
employee_count = 0

while name != 'Done': # while not done run this code to get employee payroll information and add totals together for diff pay type
    # and num of employee entered
    employee_count += 1 #increase employee count while running the program +1

    numofhours = float(input("Enter number of hours worked: "))
    payrate = float(input(f"What is {name}'s pay rate: "))
   
    # calculate the overtime if there is overtime to be calculated
    if numofhours > 40:
        overtime = numofhours - 40 # changed to minue bc modulus does not account for more than double the regular 40 hours ie. 100 hours worked
        overtimepay = overtime * 1.5 * payrate
        regularpay = 40 * payrate
        grosspay = overtimepay + regularpay
    # calculate just the gross pay and non overtime pay
    else:
        regularpay = numofhours * payrate
        grosspay = numofhours * payrate
        overtime = numofhours // 40
        overtimepay = 0

    # Print all employees payrate and gloss pay with formatting 
    print(f"{"Employee name: ":16s} {name}")
    print("")
    print(f"{"Hours Worked":<12}     {"Pay Rate":<8}     {"OverTime":<8}     {"OverTime Pay":<10}     {"RegHour Pay":<10}     {"Gross Pay":<10}")
    print(('-') * 85)
    print(f"{numofhours:<16.1f} {payrate:<12.1f} {overtime:<12.1f} {overtimepay:<16.2f} ${regularpay:<15.2f} ${grosspay:<12.2f}")

    print()
    # Adding total to themselves each time 
    overtimepay_total += overtimepay
    regularpay_total += regularpay
    grosspay_total += grosspay
    name = input("Enter employee's name or 'Done' to terminate: ")

print()
# Print total number of employees entered, total overtime paid, total regular pay, total gross pay

print(f"Total number of employees entered: {employee_count}")
print(f"Total amount paid for overtime: ${overtimepay_total:.2f}")
print(f"Total amount paid for regular hours: ${regularpay_total:.2f}")
print(f"Total amount paid in gross: ${grosspay_total:.2f}")
# Holly Rudisill
# 10/08/2026
# P4HW2
# Salary calculator for multiple employees

# Request employees info
name = input("Enter employee's name or 'Done' to terminate: ")
numofhours = int(input("Enter number of hours worked: "))
payrate = float(input(f"what is {name}'s pay rate: "))
print(('-') * 37)

# calculate the overtime if there is overtime to be calculated
if numofhours > 40:
    overtime = numofhours % 40
    overtimepay = overtime * 1.5 * payrate
    regularpay = 40 * payrate
    grosspay = overtimepay + regularpay
# calculate just the gross pay and non overtime pay
else:
    regularpay = numofhours * payrate
    grosspay = numofhours * payrate
    overtime = numofhours // 40
    overtimepay = 0

while name == "Done":
    #print all employees payrate and gloss pay with formatting 
    print(f"{"Employee name: ":16s} {name}")
    print("")
    print(f"{"Hours Worked":<12}     {"Pay Rate":<8}     {"OverTime":<8}     {"OverTime Pay":<10}     {"RegHour Pay":<10}     {"Gross Pay":<10}")
    print(('-') * 95)
    print(f"{numofhours:<16.1f} {payrate:<12.1f} {overtime:<12.1f} {overtimepay:<16.2f} ${regularpay:<15.2f} ${grosspay:<12.2f}")
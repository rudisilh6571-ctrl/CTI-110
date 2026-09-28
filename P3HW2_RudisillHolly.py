# Holly Rudisill
# 09/28/2026
# P3HW2
# Salary calculator

# Request employees info
name = input("Enter employee's name: ")
numofhours = int(input("Enter number of hours worked: "))
payrate = float(input("Enter employee's payrate: "))
print(('-') * 37)

# calculate the overtime and regular pay for the employee
if numofhours > 40:
    overtime = numofhours % 40
    overtimepay = overtime * 1.5 * payrate
    regularpay = 40 * payrate
    grosspay = overtimepay + regularpay
else:
    regularpay = numofhours * payrate
    grosspay = numofhours * payrate

#print all employees payrate and gloss pay with formatting 
print(f"{"Employee name: ":16s} {name}")
print("")
print(f"{"Hours Worked":<12}     {"Pay Rate":<8}     {"OverTime":<8}     {"OverTime Pay":<10}     {"RegHour Pay":<10}     {"Gross Pay":<10}")
print(('-') * 95)
print(f"{numofhours:<16.1f} {payrate:<12.1f} {overtime:<12.1f} {overtimepay:<16.2f} {regularpay:<15.2f} {grosspay:<12.2f}")
# Holly Rudisill
# 09/24/2026
# P3HW1
# formatting employee's pay 

# inputing employees values
name = input("Enter employee's name: ")
numofhours = int(input("Enter number of hours worked: "))
payrate = float(input("Enter employee's payrate: "))
print(('-') * 37)

# calculate the overtime and regular pay for the employee

regularpay = numofhours * payrate
overtime = numofhours % 40
if numofhours > 40:
    overtimepay = overtime * 1.5 * payrate
    grosspay = overtimepay + regularpay
else:
    print("No overtime pay for this pay period.")


print(f"{"Employee name: ":16s} {name}")
print("")
print(f"{"Hours Worked":<12}     {"Pay Rate":<8}     {"OverTime":<8}     {"OverTime Pay":<10}     {"RegHour Pay":<10}     {"Gross Pay":<10}")
print(('-') * 95)
print(f"{numofhours:<16.1f} {payrate:<12.1f} {overtime:<12.1f} {overtimepay:<16.2f} {regularpay:<15.2f} {grosspay:<12.2f}")
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
overtimepay = overtime * 1.5 * payrate
grosspay = overtimepay + regularpay


print(f"{"Employee name: ":16s} {name}")
print("")
print("Hours Worked     Pay Rate     OverTime     OverTime Pay     RegHour Pay     Gross Pay")
print(('-') * 60)
print(f"{numofhours:<12.2f} {payrate:<18.2f} {overtime} {overtimepay} {regularpay} {grosspay}")
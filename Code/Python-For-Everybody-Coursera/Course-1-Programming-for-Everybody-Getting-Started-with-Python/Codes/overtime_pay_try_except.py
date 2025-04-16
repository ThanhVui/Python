# Employees get 1.5x the hourly rate for hours worked above 40 hours.
# Error message for non-number input.
# One prompt then quit. No loop for this!

# Concepts: if, elif, else, try, except, input and print

try:
    hrs = float(input("Enter Hours: "))
    hourly_rate = float(input("Hourly Rate: "))

    overtime_multiplier = 1.5
    hourly_overtime = hourly_rate * overtime_multiplier

    if hrs <= 40:
        gross_pay = hrs * hourly_rate
        print(gross_pay)
    else:
        hrs_over = hrs - 40
        gross_pay_overtime = (40 * hourly_rate) + (hrs_over * hourly_overtime)
        print(gross_pay_overtime)

except ValueError:
    print("Error: Please enter a numeric value.")

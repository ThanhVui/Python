# Employees get 1.5x the hourly rate for hours worked above 40.
# Error message for non-number input.
# One prompt then quit. No loop for this!

# Concepts: if, elif, else, try, except, input, print, and function

def computePay(h, r):
    overtime_r = r * 1.5
    if h <= 40:
        return h * r
    else:
        return (40 * r) + (h - 40) * overtime_r

try:
    hourly_rate = float(input("Hourly rate: "))
    hours = float(input("Number of hours: "))
    p = computePay(hours, hourly_rate)
    print("Pay:", p)
except ValueError:
    print("Error: Please enter numeric input.")
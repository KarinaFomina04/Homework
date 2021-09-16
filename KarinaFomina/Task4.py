# Task 1.3
# Create a program that asks the user for a number and then prints out a list of all the [divisors] of that number.
# Examples:

# Input: 60
# Output: {1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60}

divider = int(input("Enter the number: "))
divisors_set = set()
dividend = 1
while dividend <= divider:
    if divider % dividend == 0:
        divisors_set.add(dividend)
    dividend += 1
print(divisors_set)


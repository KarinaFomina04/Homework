# Task 1.6
# Write a Python program to convert a given tuple of positive integers into an integer.
# Examples:

# Input: (1, 2, 3, 4)
# Output: 1234


tuple_number = (1, 2, 3, 4)
number = int(''.join(map(str, tuple_number)))
print(number)

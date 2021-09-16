# Task 1.1
# Write a Python program to calculate the length of a string without using the `len` function.

str_char = input("Enter characters: ")
length = 0
for i in str_char:
    length += 1
print(length)

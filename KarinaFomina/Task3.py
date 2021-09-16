# Task 1.3
# Write a Python program that accepts a comma separated sequence of words as input and prints the unique words
# in sorted form.
# Examples:

# Input: ['red', 'white', 'black', 'red', 'green', 'black']
# Output: ['black', 'green', 'red', 'white']

color_list = sorted(['red', 'white', 'black', 'red', 'green', 'black'])

new_color_list = []
for el in color_list:
    if el not in new_color_list:
        new_color_list.append(el)
print(new_color_list)

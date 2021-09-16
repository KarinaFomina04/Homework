# Task 1.2
# Write a Python program to count the number of characters (character frequency) in a string (ignore case of letters).
# Examples:

# Input: 'Oh, it is python'
# Output: {',': 1, ' ': 3, 'o': 2, 'h': 2, 'i': 2, 't': 2, 's': 1, 'p': 1, 'y': 1, 'n': 1}

count_str = input("Enter a sentence: ")
count_dict = {}
for k in count_str:
    key_dict = count_dict.keys()
    if k not in key_dict:
        count_dict[k] = 0
    count_dict[k] += 1
print(count_dict)

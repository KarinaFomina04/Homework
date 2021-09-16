# Task 1.4
# Write a Python program to sort a dictionary by key.

dict_numbers = {"1": "a", "4": "d", "3": "c", "0": "k", "5": "l", "2": "s", }
new_dict_numbers = {}
list_keys = list(dict_numbers.keys())
list_keys.sort()
for i in list_keys:
    print(i, ':', dict_numbers[i])

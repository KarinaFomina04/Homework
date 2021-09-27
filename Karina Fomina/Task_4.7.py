# Task 4.7
# Implement a function foo(List[int]) -> List[int] which, given a list of integers, return a new list such
# that each element at index i of the new list is the product of all the numbers in the original array except
# the one at i. Example:

# >>> foo([1, 2, 3, 4, 5])
# [120, 60, 40, 30, 24]

# >>> foo([3, 2, 1])
# [2, 3, 6]


list_num = [1, 2, 3, 4, 5]


def multiply_list(num):
    new_list = []
    product = 1
    for el in num:
        product *= el
    for el in num:
        new_list.append(product // el)
    return new_list


print(multiply_list(list_num))

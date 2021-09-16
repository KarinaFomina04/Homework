# Task 1.6
# Write a program which makes a pretty print of a part of the multiplication table.
# Examples:

# Input:
# a = 2
# b = 4
# c = 3
# d = 7

# Output:
# 	3	4	5	6	7
# 2	6	8	10	12	14
# 3	9	12	15	18	21
# 4	12	16	20	24	28


a = 2
b = 4
c = 3
d = 7

delimiter = "\t\t"


def print_list(lst, first_el):
    print(first_el, delimiter, delimiter.join(map(str, lst)))


def create_list(start, end, step):
    lst = []
    lst.extend(range(start, end, step))
    return lst


if a < b and c < d:
    new_list = create_list(c, d + 1, 1)
    print_list(new_list, "")
    for el in range(a, b + 1):
        new_list = create_list(el * c, el * d + 1, el)
        print_list(new_list, el)

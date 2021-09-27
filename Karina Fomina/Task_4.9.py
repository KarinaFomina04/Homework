# Task 4.9
# Implement a bunch of functions which receive a changeable number of strings and return next parameters:

# characters that appear in all strings

# characters that appear in at least one string

# characters that appear at least in two strings

# characters of alphabet, that were not used in any string

# Note: use string.ascii_lowercase for list of alphabet letters

# test_strings = ["hello", "world", "python", ]
# print(test_1_1(*strings))
# >>> {'o'}
# print(test_1_2(*strings))
# >>> {'d', 'e', 'h', 'l', 'n', 'o', 'p', 'r', 't', 'w', 'y'}
# print(test_1_3(*strings))
# >>> {'h', 'l', 'o'}
# print(test_1_4(*strings))
# >>> {'a', 'b', 'c', 'f', 'g', 'i', 'j', 'k', 'm', 'q', 's', 'u', 'v', 'x', 'z'}


import string

test_strings = ["hello", "world", "python"]


def test_1_1(*strings):
    new_set = set(strings[0])
    for el in strings:
        new_set.intersection_update(set(el))
    return new_set


print(test_1_1("hello", "world", "python"))


def test_1_2(*strings):
    new_set = set(strings[0])
    for el in strings:
        new_set.update(set(el))
    return new_set


print(test_1_2("hello", "world", "python"))


def test_1_3(*strings):
    union_pairs = set()
    for i in range(len(strings)):
        for j in range(len(strings)):
            if i < j:
                union_pairs.update(set(strings[i]).intersection(set(strings[j])))

    return union_pairs


print(test_1_3("hello", "world", "python"))


def test_1_4(*strings):
    union_all = set(strings[0])
    result = set(string.ascii_lowercase)
    for el in strings:
        union_all.update(set(el))

    return result.difference(union_all)


print(test_1_4("hello", "world", "python"))

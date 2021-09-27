# Task 4.5
# Implement a function get_digits(num: int) -> Tuple[int] which returns a tuple of a given integer's digits. Example:
#
# >>> split_by_index(87178291199)
# (8, 7, 1, 7, 8, 2, 9, 1, 1, 9, 9)


number = int(input("Enter the number: "))


def get_digits(num):
    list_digits = []
    for el in str(num):
        list_digits.append(int(el))
    tuple_digits = tuple(list_digits)

    print(tuple_digits)


get_digits(number)

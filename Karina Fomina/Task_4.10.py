# Task 4.10
# Implement a function that takes a number as an argument and returns a dictionary, where the key is a
# number and the value is the square of that number.

# print(generate_squares(5))
# >>> {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


square_num = 5


def generate_squares(num):
    num_dict = dict()
    for i in range(1, num + 1):
        num_dict[i] = i ** 2
    return num_dict


print(generate_squares(square_num))

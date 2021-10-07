# Task 5.5
# Implement a decorator remember_result which remembers last result of function it decorates and prints it
# before next call.


def remember_result(func):
    last_result = None

    def wrapper(*args):
        nonlocal last_result
        print(f"Last result = '{last_result}'")
        last_result = func(*args)
        return last_result

    return wrapper


@remember_result
def sum_list(*args):
    result = ""
    for item in args:
        result += item
    print(f"Current result = '{result}'")
    return result


sum_list('He', 'llo')
sum_list('Wor', 'ld')

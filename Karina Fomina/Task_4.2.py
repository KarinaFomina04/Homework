# Task 4.2
# Write a function that check whether a string is a palindrome or not.
# Usage of any reversing functions is prohibited. To check your implementation you can use strings from here.


palindrome_string = input("Enter palindrome word or a palindrome sentence to check: ")
newstring = "".join(filter(str.isalpha, palindrome_string)).lower()


def check_palindrome(str):
    distance = 1
    is_palindrome = True
    for i in range(len(str)):
        if str[i] != str[i - distance]:
            is_palindrome = False
            break
        distance += 2
    return is_palindrome


message = "Word or a sentence isn't palindrome"

if check_palindrome(newstring):
    message = "Word or a sentence is palindrome"

print(message)

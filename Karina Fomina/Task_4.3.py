# Task 4.3
# Implement a function which works the same as str.split method (without using str.split itself, ofcourse).


str_anime = "Naruto, JOJO, GTO, Evangelion, Drifters"
delimiter = ","
maximum = 2


def custom_split(str, delim=" ", maxsplit=None):
    lst_anime = []
    previous = 0
    split_count = 0
    for i in range(len(str)):
        if str[i] == delim:
            if i != previous or delim != " ":
                lst_anime.append(str[previous: i])
                split_count += 1
            previous = i + 1
            if split_count == maxsplit:
                break
    if previous != len(str) or delim != " ":
        lst_anime.append(str[previous::])
    return lst_anime


print("1. Library split")

print(str_anime.split(delimiter))

print("1. Custom split:")

print(custom_split(str_anime, delimiter))

print("2. Library split")

print(str_anime.split())

print("2. Custom split:")

print(custom_split(str_anime))

print("3. Library split")

print(str_anime.split(delimiter, maxsplit=maximum))

print("3. Custom split:")

print(custom_split(str_anime, delimiter, maxsplit=maximum))


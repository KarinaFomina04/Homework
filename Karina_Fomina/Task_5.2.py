# Task 5.2
# Implement a function which search for most common words in the file. Use data/lorem_ipsum.txt file as a example.
#
# def most_common_words(filepath, number_of_words=3):
#     pass
#
# print(most_common_words('lorem_ipsum.txt'))
# >>> ['donec', 'etiam', 'aliquam']


import pathlib
from pathlib import Path
import collections

dir_path = pathlib.Path.cwd()
path = Path(dir_path, "Data", "lorem_ipsum.txt")
number_of_words = 3


def most_common_words(f, numb_of_words):
    with open(f, 'r') as file:
        counter = {}
        words_list = file.read()
        words_list = words_list.lower()
        words_list = words_list.split()
        for elem in words_list:
            counter[elem] = counter.get(elem, 0) + 1
        doubles = {element: count for element, count in counter.items() if count > 1}
        new_doubles = collections.Counter(doubles).most_common(numb_of_words)
        list_max_repeat = []
        for el in new_doubles:
            list_max_repeat.append(el[0])
        return list_max_repeat


print(most_common_words(path, number_of_words))

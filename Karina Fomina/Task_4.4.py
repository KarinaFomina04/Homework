# Task 4.4
# Implement a function split_by_index(s: str, indexes: List[int]) -> List[str] which splits the s string by
# indexes specified in indexes. Wrong indexes must be ignored. Examples:
#
# >>> split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18])
# ["python", "is", "cool", ",", "isn't", "it?"]
#
# >>> split_by_index("no luck", [42])
# ["no luck"]


first_string = "pythoniscool,isn'tit?"
first_list = [6, 8, 12, 13, 18]


def split_by_index(s, indexes):
    second_list = []
    save = 0
    for i in range(len(indexes)):
        second_list.append(s[save:indexes[i]])
        save = indexes[i]
    second_list.append(s[indexes[len(indexes) - 1]::])

    return list(filter(lambda x: x != "", second_list))


print(split_by_index(first_string, first_list))

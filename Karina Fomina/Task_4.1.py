# Task 4.1
# Implement a function which receives a string and replaces all " symbols with ' and vise versa.


sentence_str = input("Enter sentences with quotation marks \" or ': ")


def change_symbol(str):
    double_quotes = "\""
    single_quotes = "'"
    for i in range(len(str)):
        if double_quotes == str[i:i + len(double_quotes)]:
            str = str[:i] + single_quotes + str[i + len(double_quotes):]
            continue
        if single_quotes == str[i:i + len(single_quotes)]:
            str = str[:i] + double_quotes + str[i + len(single_quotes):]

    return str


print(change_symbol(sentence_str))

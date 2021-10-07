# Task 5.1
# Open file data/unsorted_names.txt in data folder. Sort the names and write them to a new file called
# sorted_names.txt. Each name should start with a new line as in the following example:
#
# Adele
# Adrienne
# ...
# Willodean
# Xavier


import pathlib
from pathlib import Path

dir_path = pathlib.Path.cwd()
path = Path(dir_path, "Data", "unsorted_names.txt")
names = []
with open(path, 'r') as file:
    for line in file:
        names.append(line.strip("\n"))

with open("sorted_names.txt", "w") as file1:
    for line in sorted(names):
        file1.write(line + '\n')

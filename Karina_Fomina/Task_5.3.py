# Task 5.3
# File data/students.csv stores information about students in CSV format. This file contains the student’s names,
# age and average mark.
#
# Implement a function which receives file path and returns names of top performer students
# def get_top_performers(file_path, number_of_top_students=5):
#     pass
#
# print(get_top_performers("students.csv"))
# >>> ['Teresa Jones', 'Richard Snider', 'Jessica Dubose', 'Heather Garcia', 'Joseph Head']
# Implement a function which receives the file path with srudents info and writes CSV student information to the
# new file in descending order of age. Result:
# student name,age,average mark
# Verdell Crawford,30,8.86
# Brenda Silva,30,7.53
# ...
# Lindsey Cummings,18,6.88
# Raymond Soileau,18,7.27



import csv
import pathlib
from pathlib import Path
import operator

number_of_top_students = 5

dir_path = pathlib.Path.cwd()
students_name = Path(dir_path, "Data", "students.csv")


def get_top_performers(file_path, number):
    with open(file_path, 'r', newline="") as r_file:
        file_reader = csv.DictReader(r_file)
        new_list = []
        stud_name = []
        for rows in file_reader:
            new_list.append(rows)
        for row in new_list:
            row["average mark"] = float(row["average mark"])
        new_list.sort(key=operator.itemgetter("average mark"))
        new_list = new_list[-1: - 1 - number: -1]
        for row in new_list:
            stud_name.append(row["student name"])

        return stud_name


print(get_top_performers(students_name, number_of_top_students))


def write_descending_order_of_age(file_path):
    with open(file_path, 'r', newline="") as r_file:
        file_reader = csv.DictReader(r_file)
        new_list = []
        for rows in file_reader:
            new_list.append(rows)
        for row in new_list:
            row["age"] = int(row["age"])
        new_list.sort(key=operator.itemgetter("age"))
        new_list.reverse()
        fieldnames = ["student name", "age", "average mark"]
        with open("sorted_students_names.csv", 'w', newline="") as w_file:
            writer = csv.DictWriter(w_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(new_list)


print(write_descending_order_of_age(students_name))

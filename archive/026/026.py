# comprehension

import pandas as pd
import random

# For Loop
numbers = [1, 2, 3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)

# List Comprehension
new_list = [n + 1 for n in numbers]

# String as List
name = "Angela"
letters_list = [letter for letter in name]

# Range as List
range_list = [n * 2 for n in range(1, 5)]

# Conditional List Comprenhension
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]

upper_case_names = [name.upper() for name in names if len(name) > 4]

# Dictionary Comprehension
student_grades = {name: random.randint(1, 100) for name in names}
print(student_grades)

passed_students = {
    student: grade
    for (student, grade) in student_grades.items() if grade >= 60
}
print(passed_students)


# Pandas

pd_student = {
    "names": ["angela", "james", "lilly"],
    "score": [80, 70, 70]
}

df = pd.DataFrame(pd_student)


for (index, row) in df.iterrows():
    if row.names == "angela":
        print(row.score)


# Pandas
open_file = pd.read_csv(
    "archive/026/data/nato_phonetic_alphabet.csv")

read_data = open_file.to_dict()

dict1 = {row.letter: row.code for (index, row) in open_file.iterrows()}

print(dict1)

val = input("enter val").upper()

dict2 = {dict1[l] for l in val}
print(dict2)

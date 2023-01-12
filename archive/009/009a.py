# grading-program

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores:
    score = student_scores[student]
    value = ''
    if score > 90:
        value = "Outstanding"
    elif 90 > score > 80:
        value = 'Exceeds Expectations'
    elif 80 > score > 70:
        value = 'Acceptable'
    elif 70 > score:
        value = 'Fail'

    student_grades[student] = value


# 🚨 Don't change the code below 👇
print(student_grades)

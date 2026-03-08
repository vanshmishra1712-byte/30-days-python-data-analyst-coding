# Q26: Find the student with the highest marks

marks = {
    "Amit": 85,
    "Riya": 92,
    "John": 88,
    "Sara": 79
}

top_student = ""
highest_marks = 0

for student in marks:
    if marks[student] > highest_marks:
        highest_marks = marks[student]
        top_student = student

print(top_student)
print(highest_marks)
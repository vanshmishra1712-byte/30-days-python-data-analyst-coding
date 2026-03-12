# Day 30: Calculate average score for each student

data = {
    "Amit": [80, 90, 85],
    "Riya": [88, 92, 84],
    "John": [75, 70, 80]
}

result = {}

for student in data:
    total = 0
    count = 0

    for score in data[student]:
        total += score
        count += 1

    average = total / count
    result[student] = average

print(result)
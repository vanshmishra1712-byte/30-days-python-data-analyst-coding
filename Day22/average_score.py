# Q22: Calculate average score from a dictionary

scores = {
    "Amit": 85,
    "Riya": 90,
    "John": 78,
    "Sara": 92
}

total_score = 0
count = 0

for student in scores:
    total_score += scores[student]
    count += 1

average = total_score / count

print(average)
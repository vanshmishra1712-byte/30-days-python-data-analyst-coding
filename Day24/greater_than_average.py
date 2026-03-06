# Q24: Find numbers greater than the average of the list

numbers = [10, 20, 30, 40, 50]

total = 0
count = 0

# Step 1: calculate average
for num in numbers:
    total += num
    count += 1

average = total / count

# Step 2: collect numbers greater than average
result = []

for num in numbers:
    if num > average:
        result.append(num)

print(result)
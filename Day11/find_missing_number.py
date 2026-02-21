# Q11: Find the missing number in a list from 1 to N

numbers = [1, 2, 4, 5, 6]

# Step 1: find maximum number
max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num

# Step 2: check which number from 1 to max is missing
for i in range(1, max_num + 1):
    if i not in numbers:
        print(i)
        break
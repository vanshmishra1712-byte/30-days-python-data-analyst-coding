# Q14: Find largest and smallest element in a list

numbers = [12, 45, 3, 89, 22]

max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num

min_num = numbers[0]
for num in numbers:
    if num < min_num:
        min_num = num

print("Largest:", max_num)
print("Smallest:", min_num)
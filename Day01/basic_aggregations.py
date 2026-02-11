# Q1: Calculate sum, average, maximum and minimum from a list

numbers = [12, 45, 67, 23, 89, 34]

total_sum = 0
max_value = numbers[0]
min_value = numbers[0]

for num in numbers:
    total_sum += num
    if num > max_value:
        max_value = num
    if num < min_value:
        min_value = num

average = total_sum / len(numbers)

print("Total Sum:", total_sum)
print("Average:", average)
print("Maximum Value:", max_value)
print("Minimum Value:", min_value)

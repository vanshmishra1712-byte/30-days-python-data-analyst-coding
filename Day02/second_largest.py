# Q2: Find the second largest element in a list

numbers = [10, 20, 20, 40, 30]

unique_nums = list(set(numbers))

max_value = unique_nums[0]
for i in unique_nums:
    if i > max_value:
        max_value = i

unique_nums.remove(max_value)

second_max = unique_nums[0]
for i in unique_nums:
    if i > second_max:
        second_max = i

print(second_max)
# Q6: Remove duplicate elements from a list while preserving order

data = [1, 2, 2, 3, 4, 4, 5]

unique_data = []

for num in data:
    if num not in unique_data:
        unique_data.append(num)

print(unique_data)

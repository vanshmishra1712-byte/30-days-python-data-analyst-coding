# Q27: Count how many valid numbers exist in the list

data = [10, None, 25, 30, None, 40, 50, None]

count = 0

for value in data:
    if value is not None:
        count += 1

print(count)
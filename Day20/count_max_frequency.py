# Q20: Given a list of numbers, find how many times the maximum element appears.

numbers = [4, 2, 9, 9, 1, 9, 3]

max_num = numbers[0]
freq = 0

for i in numbers:
    if i > max_num:
        max_num = i

for j in numbers:
    if j == max_num:
        freq = freq + 1

print(freq)
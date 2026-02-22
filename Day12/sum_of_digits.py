# Q11: Given a number, find the sum of its digits.

num = 456

digit_sum = 0

while num > 0:
    digit_sum = digit_sum + num % 10
    num = num // 10

print(digit_sum)
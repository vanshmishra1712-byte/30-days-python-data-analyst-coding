# Q13: Given a list of numbers, count how many are:
# Positive
# Negative
# Zero

numbers = [3, -1, 0, 7, -5, 0, 2]

Positive = 0
Negative = 0
Zero = 0

for i in numbers:
    if i > 0:
        Positive = Positive + 1
    elif i < 0:
        Negative = Negative + 1
    else:
        Zero = Zero + 1

print("Positive:", Positive)
print("Negative:", Negative)
print("Zero:", Zero)
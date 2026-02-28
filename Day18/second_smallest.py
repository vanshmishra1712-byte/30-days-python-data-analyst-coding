# Q18: Find the second smallest element in a list

numbers = [12, 45, 3, 89, 22]

smallest = numbers[0]
second_smallest = None

for num in numbers:
    if num < smallest:
        second_smallest = smallest
        smallest = num
    elif num != smallest:
        if second_smallest is None or num < second_smallest:
            second_smallest = num

print(second_smallest)
# Q28: Group numbers into even and odd using a dictionary

numbers = [1, 2, 3, 4, 5, 6]

group = {
    "even": [],
    "odd": []
}

for num in numbers:
    if num % 2 == 0:
        group["even"].append(num)
    else:
        group["odd"].append(num)

print(group)
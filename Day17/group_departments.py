# Q17: Given a list of departments, group them and count how many times each department appears.

departments = ["HR", "IT", "HR", "Sales", "IT", "IT"]

group = {}

for i in departments:
    group[i] = group.get(i, 0) + 1

print(group)
# Q21: Given a list containing numbers and None values, remove all None values and return a clean list.

data = [10, None, 25, None, 40, 55, None]

new_lst = []

for i in data:
    if i is not None:
        new_lst.append(i)

print(new_lst)
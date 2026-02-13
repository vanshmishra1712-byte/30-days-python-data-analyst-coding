# Q3: Given a list of elements, count the frequency of each element.

data = ["HR", "IT", "HR", "Sales", "IT", "IT"]

data = ["HR", "IT", "HR", "Sales", "IT", "IT"]
freq = {}
for i in data:
    freq[i] = freq.get(i, 0) + 1
print(freq)
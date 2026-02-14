# Q4: Find the first non-repeating element in a list

data = [4, 5, 5, 2, 0, 4]

freq = {}

# Step 1: count frequency
for i in data:
    freq[i] = freq.get(i, 0) + 1

# Step 2: find first non-repeating in original order
for i in data:
    if freq[i] == 1:
        print(i)
        break

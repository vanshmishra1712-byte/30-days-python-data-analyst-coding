# Q16: Given two lists — one with names and one with scores — create a dictionary where each name maps to its score.

names = ["Amit", "Riya", "John"]
scores = [85, 90, 78]

dic = {}
for i in range(len(names)):
    dic[names[i]] = scores[i]

print(dic)
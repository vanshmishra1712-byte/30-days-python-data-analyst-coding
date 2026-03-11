# Q29: Count frequency of each word in a sentence

sentence = "data analysis is fun and data is powerful"

words = sentence.split()

freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

print(freq)
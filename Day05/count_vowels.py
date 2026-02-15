# Q5: Count number of vowels in a string

text = "Data Analyst"
vowels = ["a", "e", "i", "o", "u"]

vowel_count = 0

for ch in text.lower():
    if ch in vowels:
        vowel_count += 1

print(vowel_count)
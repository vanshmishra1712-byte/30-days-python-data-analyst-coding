# Q10: Count number of words in a sentence without using split()

sentence = "Python is very useful for data analysis"

word_count = 0
in_word = False

for ch in sentence:
    if ch != " " and not in_word:
        word_count += 1
        in_word = True
    elif ch == " ":
        in_word = False

print(word_count)
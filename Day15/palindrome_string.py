# Q15: Check whether a string is palindrome

text = "madam"
rev = ""

for ch in text:
    rev = ch + rev

if text.lower() == rev.lower():
    print("Palindrome")
else:
    print("Not Palindrome")
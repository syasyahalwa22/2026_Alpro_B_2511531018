# Name: Syasya Halwa Gazwani
# NIM: 2511531018
# Question 3

# A
text = "Informatika"
print(text[10])
print(text.upper())
print(text[0:20])

# B
text = "Syasya Halwa Gazwani"
count = 0
for char in text:
    if char.lower() in "aiueo":
        count += 1
print("Vowels:", count)
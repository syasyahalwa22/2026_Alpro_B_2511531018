# Name: Syasya Halwa Gazwani
# NIM: 2511531018

text = input("Masukkan kalimat: ")
clean = text.replace(" ", "").lower()

if clean == clean[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
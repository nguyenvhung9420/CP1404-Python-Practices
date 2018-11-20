import random
VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"

word_format = input("Word format, please: ")
word_formatOK = False
while word_formatOK == False:
    for char in word_format:
        if not char in "cv":
            word_formatOK = False
            word_format = input("Word format, please: ")
        else:
            word_formatOK = True
            print("Word format is OK.")

word = ""
for kind in word_format:
    if kind == "c":
        word += random.choice(CONSONANTS)
    else:
        word += random.choice(VOWELS)
print(word)
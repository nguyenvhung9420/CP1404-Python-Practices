import random
VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"


def wordFormatValidity(word_format):
    count_cv = 0
    for char in word_format:
        if (char in "cv") == True:
            count_cv += 1
    if count_cv == len(word_format):
        word_formatOK = True
    else:
        word_formatOK = False
    return word_formatOK


def main():
    word_format = input("Word format, please: ")
    word_formatOK = wordFormatValidity(word_format)

    while word_formatOK == False:
        word_format = input("Word format, please: ")
        word_formatOK = wordFormatValidity(word_format)

    word = ""
    for kind in word_format:
        if kind == "c":
            word += random.choice(CONSONANTS)
        else:
            word += random.choice(VOWELS)
    print(word)

main()
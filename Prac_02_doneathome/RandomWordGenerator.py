"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
WORDFORMAT_REP = "#%*"

wordFormatLength = 10
wordFormat = ""
word = ""

allChar = VOWELS + CONSONANTS + WORDFORMAT_REP

for i in range(wordFormatLength):
    wordFormat += random.choice(allChar)

#print(allChar)
print(wordFormat)

for kind in wordFormat:
    if (kind in VOWELS)==True or(kind in CONSONANTS)==True:
        capsOrNot = random.randint(0, 1)
        if capsOrNot == 1:
            word += kind.upper()
        else:
            word += kind
    if (kind in WORDFORMAT_REP)==True:
        if kind == "#":
            word += random.choice(VOWELS)
        elif kind == "%":
            word += random.choice(CONSONANTS)
        else:
            word += random.choice(VOWELS+CONSONANTS)

print(word)
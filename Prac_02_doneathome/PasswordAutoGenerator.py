"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""
import random

SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"
VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
WORDFORMAT_REP = "#%*0"

def main():
    maxLength = 0

    specialCharRequired = False

    minLength = 2

    maxLength = int(input("Please enter the maximum length of password you want: "))

    print("OK, Your password must be between 2 and", maxLength,
          "characters, and contain: ")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")

    if specialCharRequired:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)

    if specialCharRequired == True:
        password = PasswordGenerate(maxLength, "Y")
    else:
        password = PasswordGenerate(maxLength, "Y")

    while not is_valid_password(password, minLength, maxLength):
        print("Invalid password!")
        if specialCharRequired == True:
            password = PasswordGenerate(maxLength, True)
        else:
            password = PasswordGenerate(maxLength, False)

    print("Your {}-character password is valid: {}".format(len(password), password))

#------------------------------------------------------------------------------

def PasswordGenerate(passwordLength, specialCharRequired):

    wordFormatLength = passwordLength
    wordFormat = ""
    word = ""

    vowelsChoosen = False
    consonChoosen = False
    wordFormatRep_choosen = False

    allChar = VOWELS + CONSONANTS + WORDFORMAT_REP

    for i in range(wordFormatLength):
        #wordFormat += random.choice(allChar)
        rand = random.randint(1, 3)
        if rand == 1:
            if vowelsChoosen == True:
                wordFormat += random.choice(VOWELS)
                vowelsChoosen = not vowelsChoosen
            else:
                vowelsChoosen = not vowelsChoosen
        if rand == 2:
            if consonChoosen == True:
                wordFormat += random.choice(CONSONANTS)
                consonChoosen = not consonChoosen
            else:
                consonChoosen = not consonChoosen
        if rand == 3:
            if wordFormatRep_choosen == True:
                wordFormat += random.choice(WORDFORMAT_REP)
                wordFormatRep_choosen = not wordFormatRep_choosen
            else:
                wordFormatRep_choosen = not wordFormatRep_choosen



    print(wordFormat)
    capsOrNot = 0

    for kind in wordFormat:

        if (kind in VOWELS) == True or (kind in CONSONANTS) == True:
            capsOrNot = random.randint(0, 1)
            if capsOrNot == 1:
                word += kind.upper()
            else:
                word += kind

        if (kind in WORDFORMAT_REP) == True:
            if kind == "#":
                word += random.choice(VOWELS)
            elif kind == "%":
                word += random.choice(CONSONANTS)
            elif kind == "0":
                word += str(random.randint(0, 9))
            else:
                if specialCharRequired == "Y":
                    word += random.choice(SPECIAL_CHARACTERS)
                else:
                    word += random.choice(VOWELS + CONSONANTS)
    print(word)
    return word

#------------------------------------------------------------------------------

def is_valid_password(password, minLength, maxLength):
    """Determine if the provided password is valid."""
    # TODO: if length is wrong, return False:
    if len(password) < minLength or len(password) > maxLength:
        return False

    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0

    for char in password:
        # TODO: count each kind of character (use str methods like isdigit)
        if char.islower() == True:
            count_lower += 1

        if char.isupper() == True:
            count_upper += 1

        if char.isdigit() == True:
            count_digit += 1

        if (char in SPECIAL_CHARACTERS) == True:
            count_special += 1
            # pass

    # TODO: if any of the 'normal' counts are zero, return False:
    if count_lower == 0 or count_upper == 0 or count_digit == 0:
        return False

    # TODO: if special characters are required, then check the count of those and return False if it's zero
    if count_special == 0:
        return False

        # if we get here (without returning False), then the password must be valid:
    return True


main()

def main():
    ascii_num = 0
    ascii_char = ""

    #Changing from char to num:
    ascii_char = input("Please enter a character: ")

    while ascii_char.isdigit() == True:
        ascii_char = input("Please enter a character: ")

    ascii_num = ord(ascii_char)
    print("The ASCII code for {} is {}".format(ascii_char, ascii_num))

    #-----------------------------------------------------------------------------

    #Changing from num to char:
    ascii_num = getNumber(33, 127)
    ascii_char = chr(ascii_num)
    print("The character for {} is {}".format(ascii_num, ascii_char))


def getNumber(lowerbound, upperbound):
    ascii_num = int(input("Please input a number between {} and {}: ".format(lowerbound, upperbound)))
    while (ascii_num < lowerbound or ascii_num > upperbound):
        ascii_num = int(input("Sorry. Please input a number between {} and {}: ".format(lowerbound, upperbound)))
    return ascii_num

main()
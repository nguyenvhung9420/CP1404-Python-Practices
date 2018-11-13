
ascii_num = 0
ascii_char = ""

#Changing from char to num:
ascii_char = input("Please enter a character: ")

while ascii_char.isdigit() == True:
    ascii_char = input("Please enter a character: ")

ascii_num = ord(ascii_char)
print("The ASCII code for {} is {}".format(ascii_char, ascii_num))

#Changing from num to char:
ascii_num = 0
ascii_num = int(input("Please input a number between 33 and 127: "))

while (ascii_num < 33 or ascii_num > 127):
    ascii_num = int(input("Please input a number between 33 and 127: "))

ascii_char = chr(ascii_num)
print("The character for {} is {}.".format(ascii_num, ascii_char))

#Below is for printing full ASCII table:
ascii_num = 0
for i in range(33, 128, 1):
    ascii_num = i
    ascii_char = chr(ascii_num)
    print("{:>4}{:>5}".format(ascii_num, ascii_char))
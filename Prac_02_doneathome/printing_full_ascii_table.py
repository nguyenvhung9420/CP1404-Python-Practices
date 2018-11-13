#Below is for printing full ASCII table:
ascii_num = 0
ascii_char = ""
for i in range(33, 128, 1):
    ascii_num = i
    ascii_char = chr(ascii_num)
    print("{:>15}{:>5}".format(ascii_num, ascii_char), end='')
    print()


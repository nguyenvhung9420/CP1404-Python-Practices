#Below is for printing full ASCII table:
ascii_num = 0
ascii_char = ""

numCol = 0
numCol = int(input("Please enter a number of columns you want: "))

colInProgress = 0
#numOfLines  = (127-33+1)/numCol

#for i in range(numOfLines):
for i in range(33, 128, 1):
    ascii_num = i
    ascii_char = chr(ascii_num)
    print("{:>20}{:>4}".format(ascii_num, ascii_char), end='')
    colInProgress += 1
    if colInProgress == numCol:
        print()
        colInProgress =0


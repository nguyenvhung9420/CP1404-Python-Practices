def main():
    numbers = []
    i = 1

    errorOccured = True
    min_number = 0

    while min_number >= 0:
        num = (input("Number {}: ".format(i)))

        while isNum(num) == False:
            num = (input("Number {}: ".format(i)))

        numbers.append(int(num))
        i += 1
        min_number = min(numbers)

    i =1
    for num in numbers:
        print("The number {} is {}.".format(i, num))
        i += 1


def isNum(num):
    try:
        num_int = int(num)
        return True
    except ValueError:
        return False

main()
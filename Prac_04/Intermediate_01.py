
numbers = [None] * 5

for i in range(5):
    numbers[i] = int(input("Please type number {}: ".format(i+1)))

for num in numbers:
    print("The number is {}.".format(num))
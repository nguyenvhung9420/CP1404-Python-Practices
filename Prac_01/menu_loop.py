"""
1. Show the even numbers from x to y
2. Show the odd numbers from x to y
3. Show the squares from x to y
4. Exit the program
"""
from math import sqrt
from math import pow

x = int(input("Please type your x = "))
y = int(input("Please type your y = "))

menu = "(E) Show the even numbers from x to y \n(O) Show the odd numbers from x to y \n(S) Show the squares from x to y \n(Q) Quit the program"
print(menu)
userSelection = input(">>> ").upper()

while userSelection != "Q":
    if userSelection == "E":

        if y > x:
            for i in range (x, y, 1):
                if i%2==0:
                    print(i, end=' ')
        else:
            for i in range (y, x, 1):
                if i%2==0:
                    print(i, end=' ')

    elif userSelection == "O":

        if y > x:
            for i in range (x, y, 1):
                if not i%2==0:
                    print(i, end=' ')
        else:
            for i in range (y, x, 1):
                if not i%2==0:
                    print(i, end=' ')


    elif userSelection == "S":

            for i in range (x, y, 1):
                print(i**2, end=' ')

    print("\n")
    print(menu)
    userSelection = input(">>> ").upper()
print("Thanks.")
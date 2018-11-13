"""
get name
display menu
get choice
while choice != Q
if choice == H
display "hello" name
else if choice == G
display "goodbye" name
else
display invalid message
display menu
get choice
display finished message
"""

name = input("Please type your name: ")

while name == "":
    name = input("Please type your name: ")

menu = "(H)ello\n(G)oodbye\n(Q)uit"
print(menu)
userSelection = input(">>> ").upper()

while userSelection != "Q":
    if userSelection == "H":
        print("Hello {}".format(name))
    elif userSelection == "G":
        print("Goodbye {}".format(name))
    else:
        print("Invalid")

    print(menu)
    userSelection = input(">>> ").upper()
print("Thanks.")
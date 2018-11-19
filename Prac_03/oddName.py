"""
This is the odd File
"""

#Below is main() def:
def main():

    name = get_name()

    for i in range(len(name)):
        if i%2==0:
            print(name[i])


def get_name():
    print("Hello. This is the odd file.")
    name = input("Please type your name: ")
    while name == "":
        name = input("Please type your name: ")
    return name
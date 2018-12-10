"""Write a Guitar class that allows you to store one guitar with those fields (attributes):
● name (we could split this into make and model, but one name field will do us for now)
● year
● cost
Define the following methods:
● __init__ - with defaults name="", year=0, cost=0
● __str__ - which uses {} string formatting to return something like (using the values from above):
Gibson L-5 CES (1922) : $16,035.40
● get_age() - which returns how old the guitar is in years (e.g. the L-5 is 2017 - 1922 = 95)
● is_vintage() - which returns True if the guitar is 50 or more years old, False otherwise
Hint: try using get_age() to simplify the implementation of this method!"""

import datetime

class Guitar():
    def __init__(self, name, year, cost):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}) : ${:10,.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        now = datetime.datetime.now()
        return now.year - self.year

    def is_vintage(self):
        age = self.get_age()
        if age >= 50:
            return True
        else:
            return False

def main():

    finished = False
    guitars = []

    while finished == False:

        name = input("Name: ")
        year = input("Year: ")
        cost = (input("Cost: "))

        if (name == "" or year == "" or cost ==""):
            finished = True
        else:
            guitars.append(Guitar(name, int(year), int(cost)))
            print("{} added.".format(guitars[len(guitars)-1]))

    print("Here are my guitars:")
    i = 0
    for guitar in guitars:
        if guitar.is_vintage() == True:
            vintage_string = "(vintage)"
        else:
            vintage_string = ""
        print("Guitar {}: {:>20} ({}), worth ${:10,.2f} {}".format(i + 1,
                                                                   guitar.name, guitar.year, guitar.cost,
                                                                   vintage_string))

main()
import datetime
from operator import attrgetter

class Person():
    def __init__(self, firstname, lastname, birthyear):
        self.firstname = firstname
        self.lastname = lastname
        self.birthyear = birthyear

    def age(self):
        now = datetime.datetime.now()
        return now.year - self.birthyear

    def __str__(self):
        return "{} {} - {} year(s) old".format(self.firstname, self.lastname, self.age())

def main():
    list_of_people = []
    list_of_people.append(Person("Hung","Nguyen", 1991))
    list_of_people.append(Person("John", "Nguyen", 1992))
    list_of_people.append(Person("Jean", "Nguyen", 1987))
    list_of_people.append(Person("Blabla", "Nguyen", 1910))

    #list_of_people.sort(key=lambda x: x.age())
    list_of_people.sort(key=attrgetter("birthyear"), reverse=-1)

    for element in list_of_people:
        print(element)

main()
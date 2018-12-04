def getOneInfo(age):


    ageList = []
    for element in age.split("/"):
        ageList.append(int(element))
    return ageList


def main():
    personInfo = {}
    nameList = []
    ageOnePerson = []
    ageList = []
    i = 0
    for i in range(5):
        name = input("Please type your name: ")
        age = input("Please type your age (dd/mm/yyyy): ")
        ageOnePerson = getOneInfo(age)
        nameList.append(name)
        ageList.append(ageOnePerson)
    personInfo = dict(zip(nameList, ageList))
    print(personInfo)

main()
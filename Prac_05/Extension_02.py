def getOneInfo(age):


    ageList = []
    for element in age.split("/"):
        ageList.append(int(element))
    return ageList

def combineToDict(list1, list2):
    if len(list1) == len(list2):
        return dict(zip(list1, list2))
    else:
        print("Your two lists are not parallel, it means their length are not equal to each other, please review them.")
        return None

def main():
    personInfo = {}
    nameList = []
    ageOnePerson = []
    ageList = []
    i = 0
    for i in range(2):
        name = input("Please type your name: ")
        age = input("Please type your age (dd/mm/yyyy): ")
        ageOnePerson = getOneInfo(age)
        nameList.append(name)
        ageList.append(ageOnePerson)
        personInfo = combineToDict(nameList, ageList)

    print(personInfo)

main()
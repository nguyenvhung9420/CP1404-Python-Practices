def main():

    text = input("Please type something: ")

    word_to_count = {}

    for word in text:
        try:
            word_to_count[word] += 1
        except KeyError:
            word_to_count[word] = 1

    #print(word_to_count)
    word_to_count = sortDict(word_to_count)
    print(word_to_count)

    for key, value in word_to_count.items():
        if key != " ":
            print("{:>8s} : {:>10d}".format(key, value))
        else:
            print("space(s) : {:>10d}".format(value))


def sortDict(aDict):
    keyList = aDict.keys()
    valueList = []

    keyList = sorted(keyList)

    for i in range(len(keyList)):
        valueList.append(aDict[keyList[i]])

    newDict = {}
    newDict = dict(zip(keyList, valueList))

    print(newDict)
    return newDict

main()

#ahihi
#this is a feedback
import random

valueRange = [i for i in range(46)]
rangeEachLine = []
valueToUse = 0
print(valueRange)
print(len(valueRange))
print()

userPick = int(input("What picks do you want to choose? "))

#breakpoint()
for j in range(userPick):

    #print("#{} time: ".format(j))
    rangeEachLine = []

    for i in range(6):

        #print(valueRange)
        rannum = random.randint(1, len(valueRange)-1)
        valueToUse = valueRange[rannum]
        rangeEachLine.append(valueToUse)
        valueRange = [x for x in valueRange if x != valueToUse]


    rangeEachLine = sorted(rangeEachLine)
    for num in rangeEachLine:
        print("{:>2d} ".format(num), end='')
    print()

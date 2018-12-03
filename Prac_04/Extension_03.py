"""Write a program that asks the user for an indefinite set of strings
-
until an empty string
is entered
-
then
prints all of the strings that were repeated.
E.g. if the user entered: “hello”, “world is good”, “hello”, “john”, “good”... the program would print
“Strings repeated: hello”.
If no repeated strings are entered, the program should print “N
o repeated strings entered”."""

setOfStrings = []
emptyCount = 0

while emptyCount == 0:
    stringToAdd = input("Please type a string: ")
    setOfStrings.append(stringToAdd)
    if stringToAdd == "":
        emptyCount += 1

dupCount_times = []
dupCount_values = []
dupCount = 0

for j in range(len(setOfStrings)):

    #If we have already considered this value
    if setOfStrings[j] in dupCount_values:
        pass #donothing
    else:
        for i in range(len(setOfStrings)):
            if setOfStrings[j] == setOfStrings[i] and i != j:

                #Add that value to dupCount_Values:
                if (setOfStrings[i] in dupCount_values) == False:
                    dupCount_values.append(setOfStrings[i])
                    dupCount_times.append(2)
                else:
                    for k in range(len(dupCount_values)):
                        if dupCount_values[k] == setOfStrings[i]:
                            dupCount_times[k] += 1

#print(dupCount_times)
#print(dupCount_values)

if len(dupCount_values) == 0:
    print("No words repeated.")
else:
    for l in range (len(dupCount_values)):
        print("Word {} appeared {} times.".format(dupCount_values[l], dupCount_times[l]))



name = input("Please type your name? ")

while name == "":
    name = input("Please type your name? ")

VOWELS = "aeoui"
count = 0

for i in range(len(name)):
    if name[i] in VOWELS:
        count += 1


print("Out of {} characters of your name, {}, has {} vowels".format(len(name), name, count))

#print(count)

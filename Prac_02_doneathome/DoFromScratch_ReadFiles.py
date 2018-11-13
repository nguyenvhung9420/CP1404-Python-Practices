print("Python is now reading the name.txt")
file = open("./name.txt","w")

name = input("Please let us know your name: ")
print("Your name is {}. Your name is written into the file name.txt.\n".format(name))
print("Your name is {}".format(name), file=file)
file.close()

print("Python is now reading the numbers.txt")
file = open("./numbers.txt","r")
num = 0
total = 0

for line in file:
    num = int(line)
    print("Your number is: {}".format(line))
    total += num
print("The total is: {}".format(total))

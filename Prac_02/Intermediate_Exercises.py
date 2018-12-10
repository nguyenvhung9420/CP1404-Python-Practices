finished = False
result = 0

while finsihed:
    try:
        anInterger = int(input("Please enter an integer: "))
        #print("Your integer is: {}".format(anInterger))
        finished = True
    except ValueError:
        print("Please enter your integer again below.")
        
print("Your integer is: {}".format(anInterger))
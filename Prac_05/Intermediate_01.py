
colorPallettes = {}

colorNames = ['firebrick', 'firebrick1', 'firebrick2', 'firebrick3', 'firebrick4', 'FloralWhite', 'ForestGreen', 'gainsboro', 'GhostWhite', 'gold1']
colorCode = ['#b22222', '#ff3030', '#ee2c2c', '#cd2626', '#fffaf0', '#228b22', '#dcdcdc', '#f8f8ff', '#ffd700']

colorPallettes = dict(zip(colorNames, colorCode))
#print(colorPallettes)

print("We have some color names for you to choose: ")
for key in colorPallettes.keys():
    print(key)

nameToPrint = input("Please type the color name: ")
print(colorPallettes[nameToPrint])
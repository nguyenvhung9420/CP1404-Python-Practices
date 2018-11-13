"""
A shop requires a small program that would allow them to quickly work out total price for a number of items,
each with different prices.
The program allows the user to enter the number of items and the price of each different item.
Then the program computes and displays the total price of those items.
If the total price is over $100, then a 10% discount is applied to that total before the amount is displayed on the
screen.
"""
numberOfItems = 0
REDUCTION_RATE = 0.1
priceOfItem = 0
totalPrice = 0

numberOfItems = int(input("Please type the number of items: "))

while numberOfItems < 0:
    numberOfItems = int(input("Invalid number of items! Please type the number of items: "))

print("Number of items: {}".format(numberOfItems))

for i in range(numberOfItems):
    priceOfItem = 0
    priceOfItem = float(input("     Price of item #{}: ".format(i+1)))

    if priceOfItem > 100:
        priceOfItem = priceOfItem*(1-REDUCTION_RATE)

    totalPrice += priceOfItem

print("The total price for {} items is ${:,.2f}".format(numberOfItems, totalPrice))
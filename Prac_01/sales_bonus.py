"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

#sales = float(input("Enter sales: $"))
bonus_rate = 0
bonus_amount = 0
sales = 0
finished = False

while finished == False:

    try:
        sales = float(input("Enter sales: $"))

        if sales < 1000:
            bonus_rate = 0.1
        else:
            bonus_rate = 0.15

        finished = True
    except ValueError:
        print("Please input your sales again below:")

bonus_amount= sales*bonus_rate
print("Your bonus is {0}% which is equivalent to ${1}".format((bonus_rate*100), bonus_amount))
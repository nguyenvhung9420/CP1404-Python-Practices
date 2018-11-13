"""
If sales are $1,000 or over, the bonus is 15%.
"""

#sales = float(input("Enter sales: $"))
bonus_rate = 0
bonus_amount = 0

finished = False

while finished == False:

    try:
        sales = 0

        while sales >= 0:
            sales = float(input("Enter sales: $"))
            if sales < 1000:
                bonus_rate = 0.1
            else:
                bonus_rate = 0.15
            bonus_amount = sales * bonus_rate

            if sales >=0:
                print("Your bonus is {0}% which is equivalent to ${1}".format((bonus_rate * 100), bonus_amount))
            else:
                print("Your sales are negative.")

        finished = True
    except ValueError:
        print("Please input your sales again below:")


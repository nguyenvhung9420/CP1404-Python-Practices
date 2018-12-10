"""
This is electricity bill simulator
"""

import sys, traceback

tariffDict = {}
tariffChosen = ""
centsPerKwh = 0
dailyUse = 0
numberBillingDays = 0
estimatedBill_cents = 0
estimatedBill_dollars = 0

totalUsage = 0

finished = False

try:
    tariffDict = {"TARIFF_11":0.244618, "TARIFF_31":0.136928}

    print("Please choose your tariff, we have: ")

    for key, value in tariffDict.items():
        print("{} : {}".format(key, value))

    tariffChosen = input("Your choice >>> ")
    centsPerKwh = tariffDict[tariffChosen.upper()]

    dailyUse = float(input("Please enter daily use in kWh: "))
    numberBillingDays = int(input("Please enter number of billing days: "))

    totalUsage = numberBillingDays * dailyUse
    estimatedBill_cents = totalUsage * centsPerKwh
    estimatedBill_dollars = estimatedBill_cents / 100

    print("Estimated bill: ${:,.2f}".format(estimatedBill_dollars))
    finished = True

except ValueError:
    print("/!\ Please check your inputs, they may be invalid somewhere.")
    #traceback.print_exc(file=sys.stdout)
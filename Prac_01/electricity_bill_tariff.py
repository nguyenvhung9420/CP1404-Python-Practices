"""
This is electricity bill simulator
"""

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

tariffChosen = ""
centsPerKwh = 0
dailyUse = 0
numberBillingDays = 0
estimatedBill_cents = 0
estimatedBill_dollars = 0

totalUsage = 0

finished = False

try:
    tariffChosen = input("Please choose your tariff: 11 or 31 (type 11 or 31 as you want)? ")
    if tariffChosen == "11":
        centsPerKwh = TARIFF_11
    elif tariffChosen == "31":
        centsPerKwh = TARIFF_31
    else:
        raise ValueError

    dailyUse = float(input("Please enter daily use in kWh: "))
    numberBillingDays = int(input("Please enter number of billing days: "))

    totalUsage = numberBillingDays * dailyUse
    estimatedBill_cents = totalUsage * centsPerKwh
    estimatedBill_dollars = estimatedBill_cents / 100

    print("Estimated bill: ${:,.2f}".format(estimatedBill_dollars))
    finished = True

except ValueError:
    print("/!\ Please check your inputs, they may be invalid somewhere.")



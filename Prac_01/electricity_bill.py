"""
This is electricity bill simulator
"""

centsPerKwh = 0
dailyUse = 0
numberBillingDays = 0
estimatedBill_cents = 0
estimatedBill_dollars = 0

totalUsage = 0

finished = False

try:
    centsPerKwh = float(input("Please enter cents per kWh: "))
    dailyUse = float(input("Please enter daily use in kWh: "))
    numberBillingDays = int(input("Please enter number of billing days: "))

    totalUsage = numberBillingDays * dailyUse
    estimatedBill_cents = totalUsage * centsPerKwh
    estimatedBill_dollars = estimatedBill_cents / 100

    print("Estimated bill: ${:,.2f}".format(estimatedBill_dollars))
    finished = True

except ValueError:
    print("Please check your inputs, they may be invalid somewhere.")



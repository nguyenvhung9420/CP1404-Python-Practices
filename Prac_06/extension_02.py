
class Date():
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def addDays(self, dayToAdd):
        # Input date below:
        feb = calculFeb(self.year)
        monthDays = [31, feb, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        day = self.day
        day += dayToAdd
        month = self.month
        year = self.year


        while day > monthDays[month-1]:
            day = day - monthDays[month-1]
            month += 1
            if month > 12:
                month -= 12
                year += 1

        return Date(day, month, year)

def is_RomulusYear(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False

def calculFeb(year):
    if is_RomulusYear(year) == True:
        return 29
    else:
        return 28

def textMonth(month):
    monthInText = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    return monthInText[month - 1]

def main():
    year = int(input("Year: "))
    month = int(input("Month: "))
    day = int(input("Day: "))

    aDate  = Date(day, month, year)
    dayAdd = int(input("Please type the date you wanna add: "))
    aDate = aDate.addDays(dayAdd)

    print("{} - {} - {}".format(aDate.day, textMonth(aDate.month), aDate.year))

main()
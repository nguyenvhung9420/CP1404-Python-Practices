
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


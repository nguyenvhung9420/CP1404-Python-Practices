from taxi import Taxi
from car import Car

def main():
    prius = Taxi('Prius I', 100, 1.23)
    prius.drive(40)
    print(prius)
    prius.start_fare()
    print(prius.get_fare())

main()


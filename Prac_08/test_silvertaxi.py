from taxi import Taxi
from car import Car
from SilverServiceTaxi import SilverServiceTaxi

def main():
    prius = SilverServiceTaxi('Prius I', 100, 2)
    prius.drive(40)
    print(prius)
    prius.start_fare()
    print(prius.get_fare())

main()


from taxi import  Taxi

class SilverServiceTaxi(Taxi):
    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.flagfall = 4.50

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return "{}, {}km on current fare, ${:.2f}/km plus flagfall of $4.50".format(super().__str__(),
                                                             self.current_fare_distance,
                                                             self.price_per_km)

    def get_fare(self):
        """Return the price for the taxi trip."""
        return self.price_per_km * self.current_fare_distance * self.fanciness

    def start_fare(self):
        """Begin a new fare."""
        self.current_fare_distance = 0 + self.flagfall

    def drive(self, distance):
        """Drive like parent Car but calculate fare distance as well."""
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven
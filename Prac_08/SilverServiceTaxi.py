from taxi import  Taxi

class SilverServiceTaxi(Taxi):
    def __init__(self, name, fuel, price_per_km):
        super().__init__(name, fuel, price_per_km)
        self.fanciness = self.price_per_km * self.price_per_km
        self.flagfall = 4.50

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return "{}, {}km on current fare, ${:.2f}/km plus flagfall of $4.50".format(super().__str__(),
                                                             super().current_fare_distance,
                                                             super().price_per_km)

    def get_fare(self):
        """Return the price for the taxi trip."""
        return super().price_per_km * super().current_fare_distance

    def start_fare(self):
        """Begin a new fare."""
        super().current_fare_distance = 0 + self.flagfall

    def drive(self, distance):
        """Drive like parent Car but calculate fare distance as well."""
        distance_driven = super().drive(distance)
        super().current_fare_distance += distance_driven
        return distance_driven
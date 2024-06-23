#!/usr/bin/env python3

class Car:
    """A simple car."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.gas_tank_full = 0

    def get_descriptive_name(self):
        """Create a descriptive name of the car."""
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name.title()

    def read_odometer(self):
        """Print car's mileage."""
        print(f'The car has {self.odometer_reading} miles on it.')

    def update_odometer(self, mileage):
        """Set the odometer reading."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given miles to the current odomoter reading."""
        try:
            assert miles >= 0
        except AssertionError:
            print("You can't roll back an odometer!")
        else:
            self.odometer_reading += miles

    def fill_gas_tank(self):
        self.gas_tank_full = 100

    def read_gas_tank_amount(self):
        print(f"The car's gas tank is {self.gas_tank_full}% full.")

if __name__ == "__main__":

    my_new_car = Car('perodua', 'bezza', 2020)
    others_car = Car('perodua', 'myvi', 2016)

    print(my_new_car.get_descriptive_name())
    my_new_car.read_odometer()

    print(others_car.get_descriptive_name())
    others_car.read_odometer()

    my_used_car = Car('toyota', 'camri', 2015)
    print(my_used_car.get_descriptive_name())

    my_used_car.update_odometer(21_500)
    my_used_car.read_odometer()

    my_used_car.increment_odometer(-400)
    my_used_car.read_odometer()

    my_used_car.update_odometer(21_500)
    my_used_car.read_odometer()

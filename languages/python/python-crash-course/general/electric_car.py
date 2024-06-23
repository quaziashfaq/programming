#!/usr/bin/env python3

from car import Car

class Battery:
    '''Model a battery for an electric car.'''
    
    def __init__(self, battery_size=40):
        '''Initialize a battery for electric car.'''
        self.battery_size = battery_size

    def describe_battery(self):
        print(f'This car has a {self.battery_size}-kWh battery.')

    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f'This car can go about {range} miles on a full charge.')

    def upgrade_battery(self):
        if self.battery_size != 65:
            self.battery_size = 65
            print('Battery size is ugraded to 65.')
        else:
            print('Battery size is already upgraded to 65. No more upgrade!')


class ElectricCar(Car):
    '''This is an electric car class.'''

    def __init__(self, make, model, year):
        '''Initialize the electric car.'''
        super().__init__(make, model, year)
        self.battery = Battery()

    def read_gas_tank_amount(self):
        print(f'This is an electric car. There is no gas tank!')

    def fill_gas_tank(self):
        print(f'This is an electric car. There is no gas tank to fill up!')





if __name__ == '__main__':
    my_new_ecar = ElectricCar('nissan', 'leaf', 2024)
    print(my_new_ecar.get_descriptive_name())

    my_new_ecar.read_odometer()
    my_new_ecar.battery.describe_battery()
    my_new_ecar.battery.get_range()
    my_new_ecar.battery.upgrade_battery()
    my_new_ecar.battery.upgrade_battery()
    my_new_ecar.battery.get_range()



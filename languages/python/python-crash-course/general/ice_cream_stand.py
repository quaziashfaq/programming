#!/usr/bin/env python3

from restaurant import Restaurant

class IceCreamStand(Restaurant):
    def __init__(self, name):
        super().__init__(name, 'ice-cream')
        self.flavors = [
                'vanilla',
                'chocolate',
                'strawberry',
                'sorbet',
                'mango',
                ]

    def display_flavors(self):
        print(f'{self.restaurant_name} sells {self.cuisine_type}.')
        print(f'It has these flavors: ', end='')
        print(", ".join(self.flavors))


if __name__ == '__main__':
    an_ice_cream_stand = IceCreamStand('Quazi')
    an_ice_cream_stand.display_flavors()

#!/usr/bin/env python3

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0


    def describe_restaurant(self):
        print(f'Name: {self.restaurant_name.title()}:')
        print(f'\tCuisine Type: {self.cuisine_type.title()} food.')
        print(f'\tCusomers served today: {self.number_served}')

    def open_restaurant(self):
        print(f'{self.restaurant_name.title()} is open!')

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number
        

if __name__ == '__main__':
    restaurant = Restaurant('mohammadia', 'bangladeshi')
    restaurant.describe_restaurant()
    restaurant.open_restaurant()

    restaurant.set_number_served(10)
    restaurant.describe_restaurant()

    restaurant.increment_number_served(5)
    restaurant.describe_restaurant()


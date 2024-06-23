#!/usr/bin/env python3

available_toppings = [
        'mushrooms', 
        'olives', 
        'green peppers',
        'pepporoni',
        'pineapple',
        'extra cheese',
        ]

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
# requested_toppings =  []

if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping in available_toppings:
            print(f'Adding {requested_topping}')
        else:
            print(f'Sorry we are out of {requested_topping} now!')
else:
    print('Are you sure you want a plain pizza?')

print(f'\nFinished making your pizza!!')

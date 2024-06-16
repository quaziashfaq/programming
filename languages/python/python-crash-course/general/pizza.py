#!/usr/bin/env python3

def make_pizza(size, *toppings):
    print('\nMaking pizza with the following toppings:')
    for topping in toppings:
        print(f' - {topping}')



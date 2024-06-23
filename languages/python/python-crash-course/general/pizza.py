#!/usr/bin/env python3

def make_pizza(size, *toppings):
    print('\nMaking pizza with the following toppings:')
    for topping in toppings:
        print(f' - {topping}')


pizzas = [
        'cheese pizza',
        'pepperoni pizza',
        'hawaiian pizza',
        ]

friend_pizzas = pizzas[:]

pizzas.append('chicken pizza')
friend_pizzas.append('beef pizza')

print('My favorite pizzas are: ')
print(',\n'.join(pizzas))

print('')

print('My friend\'s favorite pizzas are: ')
print(',\n'.join(friend_pizzas))

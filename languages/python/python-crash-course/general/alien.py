#!/usr/bin/env python3

import random


colors = ['green', 'yellow', 'blue', 'red']
points = [5, 10, 15, 20]


def make_alien(color, point, speed):
    alien = {
            'color': color,
            'point': point,
            'speed': speed,
            }
    return alien

#alien_green = {'color': 'green', 'point': 5, 'speed': 'slow'}
#alien_yellow = {'color': 'yellow', 'point': 10, 'speed': 'medium'}
#alien_red = {'color': 'red', 'point': 15, 'speed': 'fast'}
#alien_blue = {'color': 'blue', 'point': 20, 'speed': 'very fast'}

# changed from declarative variable to build model
alien_green = make_alien('green', 5, 'slow')
alien_yellow = make_alien('yellow', 10, 'medium')
alien_red = make_alien('red', 15, 'fast')
alien_blue = make_alien('blue', 20, 'very fast')


aliens_family = [
                 alien_green, 
                 alien_yellow, 
                 alien_red,
                 alien_blue, 
                 ]


aliens_attacking = []
for i in range(1000):
    #choice = int(random.random() * 10000) % 4
    #aliens_attacking.append(aliens_family[choice])

    selected_alien = random.choice(aliens_family)
    aliens_attacking.append(selected_alien)

#print(',\n'.join(aliens_attacking))
#for index,alien in enumerate(aliens_attacking):
    #print(index, ": ", alien)

count = {
        'green': 0,
        'yellow': 0,
        'red': 0,
        'blue': 0,
        }
for alien in aliens_attacking:
    count[alien['color']] += 1


print(count)

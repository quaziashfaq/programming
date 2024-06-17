#!/usr/bin/env python3

import random

class Die:
    '''A Die Class to roll the dice.'''

    def __init__(self, sides):
        self.sides = sides

    def roll_die(self):
        return random.randint(1, self.sides)


if __name__ == '__main__':
    die6 = Die(6)
    print([die6.roll_die() for x in range(1,10)])

    die10 = Die(10)
    print([die10.roll_die() for x in range(1,10)])

    die20 = Die(20)
    print([die20.roll_die() for x in range(1,10)])

#!/usr/bin/env python3

from random import choice

class RandomWalk:
    '''A class to generate random walks.'''


    def __init__(self, num_points=5000):
        '''Initialize attributes of a walk.'''
        self.num_points = num_points 

        # all walsk start at (0, 0).
        self.x_values = [0]
        self.y_values = [0]


    def fill_walk(self):
        '''Calculate the points in the walk.'''

        while len(self.x_values) < self.num_points:
            x_step = self._calculate_step(choose_direction = [1, -1],
                                     choose_distance = [0, 1, 2, 3, 4])

            y_step = self._calculate_step(choose_direction = [1, -1],
                                     choose_distance = [0, 1, 2, 3, 4])

            # reject moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the new position
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)



    def _calculate_step(self, choose_direction, choose_distance):
        direction = choice(choose_direction)
        distance = choice(choose_distance)
        step = direction * distance
        return step


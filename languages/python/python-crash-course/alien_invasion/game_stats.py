#!/usr/bin/env python3

class GameStats:
    '''Track statistics for Alien Invasion.'''

    def __init__(self, ai_game):
        '''Initialize game's statistics.'''
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0

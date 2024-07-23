#!/usr/bin/env python3

class Settings:
    '''A class to store all settings for Alien Invasion.'''

    def __init__(self):
        '''Initialize the game's settings.'''
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 20

        # alien settings
        self.fleet_drop_speed = 10
        self.alien_destroyed_target_count = 100

        # How quickly the game speeds up
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        self.ship_speed = 2.5
        self.bullet_speed = 4.0
        self.alien_speed = 1.0

        # Fleet direction: right: 1, left: -1
        self.fleet_direction = 1

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_peed *= self.speedup_scale

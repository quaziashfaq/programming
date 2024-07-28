#!/usr/bin/env python3

import os
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''A class for Alien.'''
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # load the ship image and get its rect.
        dir_path = os.path.dirname(os.path.realpath(__file__))
        #print(dir_path)
        self.image = pygame.image.load(dir_path + '/images/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)


    def check_edges(self):
        '''Return True if alien is at edge of screen.'''
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    def update(self):
        ''' Move the alien to the right. '''
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x

#!/usr/bin/env python3

import pygame
import os

class Ship:
    '''A class to manage the ship.'''

    def __init__(self, ai_game):
        '''Initialize the ship and set its starting position.'''
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # load the ship image and get its rect.
        dir_path = os.path.dirname(os.path.realpath(__file__))
        #print(dir_path)
        self.image = pygame.image.load(dir_path + '/images/ship.bmp')
        self.image = pygame.transform.rotate(self.image, -90)
        self.rect = self.image.get_rect()

        # start each new ship at the bottom center of the screen
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)

        # Movement flag; start with a shift that's not moving.
        self.moving_up = False
        self.moving_down = False


    def update(self):
        '''Update the ship's position based on movement flags.'''
        # Update the ship's y value, not the rect.
        if self.moving_up and self.rect.top < 0:
            self.y -= self.settings.ship_speed
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
    
        # Update rect object from self.y
        self.rect.y = self.y

    def blitme(self):
        ''' Draw the ship at its current location.'''
        self.screen.blit(self.image, self.rect)

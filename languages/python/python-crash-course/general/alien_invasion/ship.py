#!/usr/bin/env python3

import pygame

class Ship:
    '''A class to manage the ship.'''

    def __init__(self, ai_game):
        '''Initialize the ship and set its starting position.'''
        self.screen = ai_game.screen
        print(self.screen)
        self.screen_rect = ai_game.screen.get_rect()
        print(self.screen_rect)

        # load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        print(self.image)
        self.rect = self.image.get_rect()
        print(f'Ship rect size: {self.rect}')

        # start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        print(self.rect.midbottom)
        print(self.rect)
        


    def blitme(self):
        ''' Draw the ship at its current location.'''
        self.screen.blit(self.image, self.rect)

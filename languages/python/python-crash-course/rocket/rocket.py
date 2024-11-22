#!/usr/bin/env python3


import sys
import os
import pygame

class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (128, 128, 128)
        self.rocket_speed = 1.5


class Rocket:
    def __init__(self, rocket_game):
        '''Initialize the rocket and setting the window and position.'''
        self.screen = rocket_game.screen
        self.settings = rocket_game.settings
        self.screen_rect = rocket_game.screen.get_rect()

        # load the rocket
        dir_path = os.path.dirname(os.path.realpath(__file__)) + '/'
        self.image = pygame.image.load(os.path.join(dir_path + 'rocket.png'))
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        ''' Updte the rocket's position based on movement flags.'''

        # Update rocket's x and y value
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.rocket_speed
        elif self.moving_left and self.rect.left > 0:
            self.x -= self.settings.rocket_speed
        elif self.moving_up and self.rect.top > 0:
            self.y -= self.settings.rocket_speed
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.rocket_speed

        # Then update self's rect object
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        ''' Drow the rocket at its current location. '''
        self.screen.blit(self.image, self.rect)



class RocketGame:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.bg_color = self.settings.bg_color
        
        pygame.display.set_caption('Rocket Game')
        self.rocket = Rocket(self)

    def run_game(self):
        while True:
            self._check_events()
            self.rocket.update()
            self._update_screen()
            self.clock.tick(60)

    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.rocket.blitme()
        pygame.display.flip()

        
    def _check_keydown_events(self, event):
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_RIGHT:
            self.rocket.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = True
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = False
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = False


    def _check_events(self):
        ''' Wait for keyboard events '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    

if __name__ == '__main__':
    rg = RocketGame()
    rg.run_game()
    

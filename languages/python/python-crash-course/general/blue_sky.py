#!/usr/bin/env python3

import sys
import pygame

class BlueSky:
    '''Creating a pygame window with a blue background.'''
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        self.bg_color = (135, 206, 235)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)
            pygame.display.flip()


if __name__ == '__main__':
    blue_sky = BlueSky()
    blue_sky.run_game()


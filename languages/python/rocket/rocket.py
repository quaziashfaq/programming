#!/usr/bin/env python3


import sys
import pygame

class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800

class RocketGame:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.bg_color = (128, 128, 128)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                
            self.screen.fill(self.bg_color)
            pygame.display.flip()
        
        



if __name__ == '__main__':
    rg = RocketGame()
    rg.run_game()
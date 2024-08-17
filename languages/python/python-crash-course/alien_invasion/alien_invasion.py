#!/usr/bin/env python3

import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from time import sleep
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

class AlienInvasion:
    '''Overall class to manage game assets and behavior.'''

    def __init__(self):
        '''Initialize the game and create game resourcse.'''
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        #self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption('Alien Invasion')
        
        # Create an instance to store game statstics and create a scoreboard
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

        self.aliens = pygame.sprite.Group()
        self._create_fleet()

        # Start alien invasion
        self.game_active = False
        self.alien_destroyed_count = 0
        #self.game_won = False

        # Make the play button
        self.play_button = Button(self, "Play")

    def run_game(self):
        '''Start the main loop for the game.'''
        while True:
            self._check_events()
            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()
            self.clock.tick(60)

    def _update_bullets(self):
        ''' Update positions of bullets and get rid of old bullets.'''
        self.bullets.update()
        # get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()
     
    def _check_bullet_alien_collisions(self):
        '''Check collisios between bullet and aliens.'''
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        #self.alien_destroyed_count += len(collisions)
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
            self.sb.prep_high_score()

        #if self.alien_destroyed_count == self.settings.alien_destroyed_target_count:
            #self.game_active = False
            #self.game_won = True
        #print(type(collisions)):
        if not self.aliens:
            # Create a new fleet and increase speed
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            # Increase level.
            self.stats.level += 1
            self.sb.prep_level()

    def _check_events(self):
        '''Watch for keyboard and mouse events.'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_play_button(self, mouse_pos):
        '''Start a new game when the player clicks Play.'''
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            # Reset the game settings:
            self.settings.initialize_dynamic_settings()
            # Hide the mouse cursor:
            pygame.mouse.set_visible(False)
            self._start_game()
            self.sb.prep_level()
            
    def _start_game(self):
        '''Start the game.'''
        # Reset the game stats
        self.stats.reset_stats()
        #self.sb.prep_score()
        self.game_active = True

        # Get rid of any remaining bullets ad aliens
        self.bullets.empty()
        self.aliens.empty()

        # Ceate a new fleet and center the ship
        self._create_fleet()
        self.ship.center_ship()

    def _check_keydown_events(self, event):
        '''Respond to key presses.'''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_p:
            self._start_game()

    def _check_keyup_events(self, event):
        '''Respond to key release.'''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        ''' Create a new bullet and add it to the bullets group. '''
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _create_fleet(self):
        '''Create the fleet of aliens.'''
        alien = Alien(self)
        #alien_width = alien.rect.width
        #self.aliens.add(alien)
        alien_width, alien_height = alien.rect.size
        current_x, current_y = alien_width, alien_height
        
        while current_y < (self.settings.screen_height) - 3 * alien_height:
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width

            current_x = alien_width # back to starting position
            current_y += 2 * alien_height # drow in the next row

    def _create_alien(self, x_position, y_position):
        ''' Create an alien and place it in the row. '''
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)
         
    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_aliens(self):
        '''Update the position of all aliens.'''
        self._check_fleet_edges()
        self.aliens.update()

        # Look for collision between aliens and ship
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        if self._check_aliens_bottom():
            self._ship_hit()

    def _check_aliens_bottom(self):
        '''Check if any alien has hit the bottom.'''
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                return True

    def _ship_hit(self):
        self.stats.ships_left -= 1
        if self.stats.ships_left > 0:
            self.bullets.empty()
            self.aliens.empty()

            # Create new fleet of aliens       
            self._create_fleet()
            self.ship.center_ship()

            # Pause
            sleep(0.5)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)
            #self.game_won = False

    def _update_screen(self):
        '''Update images on the screen, and flip to the new screen.'''
        # Redraw the screen druing each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)

        # Draw the scoreboard
        self.sb.show_score()

        # Daw the play button if the game is inactive.
        if not self.game_active:
            self.play_button.draw_button()

        # Make the most recently drawn screen visible.
        pygame.display.flip()

# Main function
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

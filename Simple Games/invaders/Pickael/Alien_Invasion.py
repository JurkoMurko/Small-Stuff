#Michael Wentworth
import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
class AlienInvasion:
    '''Overall class to manage game assets and behavior'''
    
    def __init__(self):
        """Initiliza the game, and create resources."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        #self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        #self.settings.screen_width = self.screen.get.rect().width
        #self.settings.screen_height = self.screen.get.rect().height
       
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        
        self._create_fleet()
        pygame.display.set_caption("Wendy's Parking Lot")
    
                   
    def run_game(self):
        '''Start the main loop for the game.'''
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_bullets()
            self._update_screen()
            
            # Get rid of bullets that have dissapeared
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
    
    def _create_fleet(self):
        '''Create the fleet of aliens.'''
        # Make an alien.
        alien = Alien(self)
        alien_width = alien.rect.width
        alien_height = alien.rect.height
        availible_space_x = self.settings.screen_width - (2 * alien_width)
        numbers_aliens_x = availible_space_x // (2 * alien_width)
        
        # determine number of rows
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)
        
        print(self.settings.screen_height, 3 * alien_height, ship_height)

        # Create the fleet of aliens
        for row_number in range(number_rows):
            for alien_number in range(numbers_aliens_x):
                self._create_alien(alien_number, row_number)
                
    def _create_alien(self, alien_number, row_number):
        '''create an alien AND place it in the row'''
        alien = Alien(self)
        alien_width = alien.rect.width
        alien_height = alien.rect.height
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)
    
    def _update_bullets(self):
        '''Update position of bullets and ger rid of old bullets'''
        #update bullet position
        self.bullets.update()
        # Get rid of bullets that have dissapeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
                
    def _check_events(self):
        """respond to keypress and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                   
    def _check_keydown_events(self, event):
        '''respond to key presses'''
        if event.key == pygame.K_RIGHT:
             self.ship.moving_right = True;
        elif event.key == pygame.K_LEFT:
             self.ship.moving_left = True;
        elif event.key == pygame.K_q:
            sys.exit();
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Rrespong to key releases"""
        if event.key == pygame.K_RIGHT:
             self.ship.moving_right = False;
        elif event.key == pygame.K_LEFT:
             self.ship.moving_left = False;
             
    def _fire_bullet(self):
        '''create a new bullet and add it to the bullets group'''
        if len(self.bullets) < self.settings.bullets_allowed: 
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
        
    def _update_screen(self):
        """Update images on the screen, and flip ot the new screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        pygame.display.flip()
    
if __name__ == '__main__':
    #make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()
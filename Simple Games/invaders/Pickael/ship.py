import pygame

class Ship:
    '''a class to manage the ship'''
    
    def __init__(self, ai_game):
        '''initialize the ship at starting position'''
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
            
        #load the ship image and get its rect
        self.image = pygame.image.load('gun.png')
        self.rect = self.image.get_rect()
        
        #start each new ship at the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom
    
        #store a decimal balue for the ship's horizontal position
        self.x = float(self.rect.x)
    
        #movement flag
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        """update the ship's position base on the movement flags."""
        if self.moving_right == True and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left == True and self.rect.left > 0:
            self.x -= self.settings.ship_speed
            
        #Update rect object from self.x
        self.rect.x = self.x
            
    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
    def blitme(self):
        '''draw the ship at its current location'''
        self.screen.blit(self.image, self.rect)
                                                                                                                         
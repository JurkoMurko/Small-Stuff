import pygame
class Settings:
    '''A class to store all settings for Alien Invasion'''
    
    def __init__(self):
        '''initialize the game's settings'''
        #screen settings
        self.screen_width = 900
        self.screen_height = 800
        self.bg_color = (110,200,233)
       
       #Ship Settings
        self.ship_speed = 5
        
       #Bullet settings
        self.bullet_speed = 4.8
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3
                
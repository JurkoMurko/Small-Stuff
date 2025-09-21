import pygame

class ship:
    """a class that manages the ship"""

    def __init__(shef, core_game):
        """init the ship and its cordinates"""
        self.screen = core_game.screen
        self.screen_rect  = core_game.screen.get_rect()

        # load image and rect
        self.image = pygame.image.load("ship.bmp")
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

    def draw(self):
        self.screen.blit(self.image, self.rect)
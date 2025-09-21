import pygame
import sys
from pygame.sprite import Sprite


class Settings:
    """ A class that stores all the game settings"""
    # speed = 1

    def __init__(self):
        """init"""
        # screen settings
        self.full_screen = False
        
        self.screen_width = 600
        self.screen_height = 400
        self.background_color = (230, 130, 230)
        
        self.speed = 150

        if self.full_screen == False:
            self.ship_speed = self.speed / self.screen_width
        
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)

class SpaceInvadersGame(Settings):
    """Main game class"""

    def __init__(self):
        super().__init__()
        pygame.init()
        pygame.display.set_caption("Alien Invasion")

        # set screen mode
        if self.full_screen == True:
            self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

        self.ship = Ship(self)
        self.bullet = Bullet(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """run a round of the game"""
        while True:
            self._check_event()
            self.ship.update()
            self.bullets.update()
            self._update_screen()

    def _check_event(self):
        """respond to keypresses and mouse events"""
        # listen for input events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_key_down(event)
            elif event.type == pygame.KEYUP:
                self._check_key_up(event)

    def _check_key_down(self, event):
        if event.key == pygame.K_RIGHT:
            # move ship to the right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # move ship to the right
            self.ship.moving_left = True
        elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_SPACE:
                self.bullet.fire()

    def _check_key_up(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        """update images on the screen and flip to the new screen."""
        # update what is to be drawn
        self.screen.fill(self.background_color)
        self.ship.draw()

        # draw
        pygame.display.flip()


class Ship(Settings):
    """a class that manages the ship"""

    def __init__(self, core_game):
        super().__init__()
        """init the ship and its cordinates"""
        self.screen = core_game.screen
        self.screen_rect  = core_game.screen.get_rect()

        # load image and rect
        self.image = pygame.image.load("ship.bmp")
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        # Movement Flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """update the ship's cordinates base on the movement flage"""
        if self.moving_right == True and self.rect.right < self.screen_rect.right:
            self.x += self.ship_speed
        elif self.moving_left == True and self.rect.left > self.screen_rect.left:
            self.x -= self.ship_speed

        # update rect
        self.rect.x = self.x

    def draw(self):
        self.screen.blit(self.image, self.rect)


class Bullet(Sprite, Settings):
    
    def __init__(self, core_game):
        super().__init__() 
        self.core = core_game

    def fire(self):
        self.rect = pygame.Rect(0,0, self.bullet_width, self.bullet_height)
        self.rect.midtop = self.coor.ship.rect.midtop

        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.bullet_speed
        self.rect.y = self.y

    def draw(self):
        pygame.draw.rect(core_game.screen, bullet_color, self.rect)



if __name__ == "__main__":
    SpaceInvadersGame().run_game()
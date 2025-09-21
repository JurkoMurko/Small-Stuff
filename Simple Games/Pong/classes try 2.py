import pygame
import sys
import random

pygame.init()
clock = pygame.time.Clock()

screen_width = 700
screen_height = 500

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")

player1_score = 0
player2_score = 0


class Ball:

    speed = 4

    def __init__(self, size):
        self.size = size
        self.rect = pygame.Rect(screen_width/2 - size/2, screen_height/2 - size/2, size, size)
        self.x = self.rect.x
        self.y = self.rect.y
        self.ball_speed_x = speed * random.choice((1, -1))
        self.ball_speed_y = speed * random.choice((1, -1))

    # yeah...nope! I don't want to learn class inheritance. plz no!
    # I don't want to.
    # You might not have to learn class inheritance...
    # even though they're super easy

    def ball_movement(self):

        self.x += self.ball_speed_x
        self.y += self.ball_speed_y

        if ball.top <= 0 or ball.bottom >= screen_height:
            self.ball_speed_y *= -1

        if ball.left <= 0:
            player1_score += 1
            score_time = pygame.time.get_ticks()

        if ball.right >= screen_width:
            player2_score += 1
            score_time = pygame.time.get_ticks()

        if ball.colliderect(player1) or ball.colliderect(player2):
            self.ball_speed_x *= -1

ball = Ball(30)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    ball.ball_movement()

    pygame.display.update()
    clock.tick(60)

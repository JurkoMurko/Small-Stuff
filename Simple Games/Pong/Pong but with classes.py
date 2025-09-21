import pygame
import sys
import random

# General Setup
pygame.init()

# Game variables
screen_width = 700
screen_height = 500
speed = 4

# Colors
bg_color = pygame.Color("grey12")
light_grey = (200, 200, 200)

# Text Variables
player1_score = 0
player2_score = 0
font_size = 32
game_font = pygame.font.Font("freesansbold.ttf", font_size)


class Paddle:

    paddle_height = 140
    paddle_width = 10

    player1_speed = 0
    player2_speed = 4

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.p = pygame.Rect(x, y, Paddle.paddle_width, Paddle.paddle_height)

    def player1_movement(self, p):
        player1.y += Paddle.player1_speed
        if p.top <= 0:
            p.top = 0
        if p.bottom >= screen_height:
            p.bottom = screen_height

    def player2_movement(self, p):
        if p.top < Ball.ball.y:
            p.top += Paddle.player2_speed
        if p.bottom > Ball.ball.y:
            p.bottom -= Paddle.player2_speed
        if p.top <= 0:
            p.top = 0
        if p.bottom >= screen_height:
            p.bottom = screen_height


class Ball:

    ball_size = 30
    ball = pygame.Rect(screen_width / 2 - ball_size / 2, screen_height / 2 - ball_size / 2, ball_size, ball_size)

    ball_speed_x = speed * random.choice((1, -1))
    ball_speed_y = speed * random.choice((1, -1))

    def __init__(self, x, y, size, speed):
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed

    def ball_movement(self):
        global score_time, player1_score, player2_score

        Ball.ball.x += Ball.ball_speed_x
        Ball.ball.y += Ball.ball_speed_y

        if Ball.ball.top <= 0 or Ball.ball.bottom >= screen_height:
            Ball.ball_speed_y *= -1

        if Ball.ball.left <= 0:
            player1_score += 1
            score_time = pygame.time.get_ticks()

        if Ball.ball.right >= screen_width:
            player2_score += 1
            score_time = pygame.time.get_ticks()

        if Ball.ball.colliderect(Paddle.player1) or Ball.ball.colliderect(Paddle.player2):
            Ball.ball_speed_x *= -1

    def ball_restart(self):
        global score_time

        current_time = pygame.time.get_ticks()
        Ball.ball.center = (screen_width / 2, screen_height / 2)

        if current_time - score_time < 700:
            number_three = game_font.render("3", False, light_grey)
            screen.blit(number_three, (screen_width / 2 - 10, screen_height / 2 + 20))
        if 700 < current_time - score_time < 1400:
            number_three = game_font.render("2", False, light_grey)
            screen.blit(number_three, (screen_width / 2 - 10, screen_height / 2 + 20))
        if 1400 < current_time - score_time < 2100:
            number_three = game_font.render("1", False, light_grey)
            screen.blit(number_three, (screen_width / 2 - 10, screen_height / 2 + 20))

        if current_time - score_time < 2100:
            Ball.ball_speed_x, Ball.ball_speed_y = 0, 0

        else:
            Ball.ball_speed_y = speed * random.choice((1, -1))
            Ball.ball_speed_x = speed * random.choice((1, -1))
            score_time = None


# Setting up the main window
pygame.display.set_caption("Pong")

screen = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()

# score timer
score_time = True

player1 = Paddle(screen_width - 20, screen_height / 2 - Paddle.paddle_height / 2)
player2 = Paddle(10, screen_height / 2 - Paddle.paddle_height / 2)

while True:
    # Handling input
    for event in pygame.event.get():
        # Quit
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Keys Bindings
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                Paddle.player1_speed += 4
            if event.key == pygame.K_UP:
                Paddle.player1_speed -= 4
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player1_speed = 0
            if event.key == pygame.K_UP:
                player1_speed = 0

    # Animations
    #Ball.ball_movement()
    player1.player1_movement(player1)
    player2.player2_movement(player2)

    # Visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, Paddle.player1)
    pygame.draw.rect(screen, light_grey, Paddle.player2)
    pygame.draw.ellipse(screen, light_grey, Ball.ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2, 0), (screen_width/2, screen_height))

    if score_time:
        Ball.ball_restart()

    # Text
    player1_text = game_font.render(f"{player1_score}", False, light_grey)
    player2_text = game_font.render(f"{player2_score}", False, light_grey)

    screen.blit(player1_text, (((screen_width/2) - (font_size/4) + (screen_width/30)), screen_height/2))
    screen.blit(player2_text, (((screen_width/2) - (font_size/4) - (screen_width/30)), screen_height/2))

    # Updating the window
    pygame.display.update()
    clock.tick(60)

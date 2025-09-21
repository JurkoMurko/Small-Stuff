import pygame
import sys
import random

# General Setup
# pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()

# Game variables
screen_width = 700
screen_height = 500

paddle_height = 140
paddle_width = 10
ball_size = 30

# Colors
bg_color = pygame.Color("grey12")
light_grey = (200, 200, 200)

# Movement speeds
speed = 4

# Text Variables
player1_score = 0
player2_score = 0
font_size = 32
game_font = pygame.font.Font("freesansbold.ttf", font_size)


# Animation functions
def ball_movement():
    global ball_speed_x, ball_speed_y, player1_score, player2_score, score_time

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        # pygame.mixer.Sound.play(pong_sound)
        ball_speed_y *= -1

    if ball.left <= 0:
        # pygame.mixer.Sound.play(score_sound)
        player1_score += 1
        score_time = pygame.time.get_ticks()

    if ball.right >= screen_width:
        # pygame.mixer.Sound.play(score_sound)
        player2_score += 1
        score_time = pygame.time.get_ticks()

    # Ball collisions with paddles
    if ball.colliderect(player1) and ball_speed_x > 0:
        # pygame.mixer.Sound.play(pong_sound)

        if abs(ball.right - player1.left) < 10:
            ball_speed_x *= -1
        elif abs(ball.bottom - player1.top) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1
        elif abs(ball.top - player1.bottom) < 10 and ball_speed_y < 0:
            ball_speed_y *= -1

    if ball.colliderect(player2) and ball_speed_x < 0:
        # pygame.mixer.Sound.play(pong_sound)

        if abs(ball.left - player2.right) < 10:
            ball_speed_x *= -1
        elif abs(ball.bottom - player2.top) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1
        elif abs(ball.top - player2.bottom) < 10 and ball_speed_y < 0:
            ball_speed_y *= -1


def player_movement():
    player1.y += player1_speed
    if player1.top <= 0:
        player1.top = 0
    if player1.bottom >= screen_height:
        player1.bottom = screen_height


def player2_movement():
    if player2.top < ball.y:
        player2.top += player2_speed
    if player2.bottom > ball.y:
        player2.bottom -= player2_speed
    if player2.top <= 0:
        player2.top = 0
    if player2.bottom >= screen_height:
        player2.bottom = screen_height


def ball_restart():
    global ball_speed_x, ball_speed_y, score_time

    current_time = pygame.time.get_ticks()
    ball.center = (screen_width/2, screen_height/2)

    if current_time - score_time < 700:
        number_three = game_font.render("3", False, light_grey)
        screen.blit(number_three, (screen_width/2 - 10, screen_height/2 + 20))
    if 700 < current_time - score_time < 1400:
        number_three = game_font.render("2", False, light_grey)
        screen.blit(number_three, (screen_width/2 - 10, screen_height/2 + 20))
    if 1400 < current_time - score_time < 2100:
        number_three = game_font.render("1", False, light_grey)
        screen.blit(number_three, (screen_width/2 - 10, screen_height/2 + 20))

    if current_time - score_time < 2100:
        ball_speed_x, ball_speed_y = 0, 0

    else:
        ball_speed_y = speed * random.choice((1, -1))
        ball_speed_x = speed * random.choice((1, -1))
        score_time = None

# Setting up the main window
pygame.display.set_caption("Pong")

screen = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()

ball = pygame.Rect(screen_width/2 - ball_size/2, screen_height/2 - ball_size/2, ball_size, ball_size)
player1 = pygame.Rect(screen_width - 20, screen_height/2 - paddle_height/2, paddle_width, paddle_height)
player2 = pygame.Rect(10, screen_height/2 - paddle_height/2, paddle_width, paddle_height)

ball_speed_x = speed * random.choice((1, -1))
ball_speed_y = speed * random.choice((1, -1))
player1_speed = 0
player2_speed = speed

# score timer
score_time = True

# Sound
# pong_sound = pygame.mixer.Sound("pong.ogg")
# score_sound = pygame.mixer.Sound("score.ogg")

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
                player1_speed += 4
            if event.key == pygame.K_UP:
                player1_speed -= 4
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player1_speed = 0
            if event.key == pygame.K_UP:
                player1_speed = 0

    # Animations
    ball_movement()
    player_movement()
    player2_movement()

    # Visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player1)
    pygame.draw.rect(screen, light_grey, player2)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2, 0), (screen_width/2, screen_height))

    if score_time:
        ball_restart()

    # Text
    player1_text = game_font.render(f"{player1_score}", False, light_grey)
    player2_text = game_font.render(f"{player2_score}", False, light_grey)

    screen.blit(player1_text, (((screen_width/2) - (font_size/4) + (screen_width/30)), screen_height/2))
    screen.blit(player2_text, (((screen_width/2) - (font_size/4) - (screen_width/30)), screen_height/2))

    # Updating the window
    pygame.display.update()
    clock.tick(60)

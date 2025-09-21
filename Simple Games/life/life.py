import pygame
from pygame.display import update 
from pygame.locals import *
 
pygame.init()
 
fps = 24
fpsClock = pygame.time.Clock()

width, height = 600, 600
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)

# game vars
num_blocks = 12
offset_percent = .9
offColor = '#424242'
onColor = '#f5f5f5'
gapColor = '#9e9e9e'
edit = False
data = [[False for _ in range(num_blocks)] for _ in range(num_blocks)]
dt = 1
update_time = 12
start = False

def update_vars():
    global block_size
    global blank_size
    block_size = (width / num_blocks) * offset_percent # figure out how to update these when offset% chnages
    blank_size = (width - (block_size * num_blocks)) / (num_blocks + 1)

update_vars()

# make the rects
cube_boys = [[pygame.Rect(0,0, block_size, block_size) for i in range(num_blocks)] for i in range(num_blocks)]

def event_checks(edit, num_blocks, start):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()

        if event.type == VIDEORESIZE:
            width, height = event.size
            height = width
            update_vars()
            screen = pygame.display.set_mode((width,height), pygame.RESIZABLE)

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            
            # is just converting the pos to a grid cord faster?
            for y in range(num_blocks):
                for x in range(num_blocks):
                    if cube_boys[y][x].collidepoint(pos) == True:
                        data[y][x] = not data[y][x]
    
        if event.type == KEYDOWN:
            if event.key == K_s:
                start = True

        if edit and event.type == KEYDOWN:
            if event.key == K_q:
                pygame.quit()
                quit()
            if event.key == K_UP:
                offset_percent += .05
                update_vars()
            if event.key == K_DOWN:
                offset_percent -= .05
                update_vars()
            if event.key == K_LEFT:
                if num_blocks > 1:
                    num_blocks -= 1
                    update_vars()
            if event.key == K_RIGHT:
                if num_blocks < width/3:
                    num_blocks += 1
                    update_vars()
            if event.key == K_s:
                edit = False

def ze_rules():
    total = 0 
    for j in range(-1,2):
        for k in range(-1,2):
            try:
                if data[y+j][x+k]:
                    total += 1
            except IndexError:
                pass
    if data[y][x]:
        total -= 1

    # ze rules
    to_True = []
    to_False = []

    if 2 >= total or total >= 5 and cube_boys[y][x]:
        to_False.append((x,y))                
    
    if not cube_boys[y][x] and total == 3:
        to_True.append((x,y))
    
    for cor in to_True:
        data[y][x] = True

    for cor in to_False:
        data[y][x] = False
    
# Game loop
while True:
    screen.fill(gapColor)
  
    event_checks(edit, num_blocks, start)
    print(start)

    for y in range(num_blocks):
        for x in range(num_blocks):
            # this only needs to run once if edit is off, but its dependednt on the two loops above
            cube_boys[y][x].topleft = (x * (blank_size + block_size) + blank_size , y * (blank_size + block_size) + blank_size)
            
            if dt >= update_time and start:
                ze_rules()

            # draw
            if data[y][x] == True:
                pygame.draw.rect(screen, onColor, cube_boys[y][x])
            else:
                pygame.draw.rect(screen, offColor, cube_boys[y][x])

    pygame.display.flip()
    fpsClock.tick(fps)

    if dt <= update_time:
        dt += 1
    else: 
        dt = 1
import pygame
from pygame.display import update 
from pygame.locals import *
 
def update_vars():
    global block_size
    global blank_size
    block_size = (width / num_blocks) * offset_percent # figure out how to update these better
    blank_size = (width - (block_size * num_blocks)) / (num_blocks + 1)

class Vars():
    def __init__(self) -> None:
        Vars.height = 600
        Vars.width = 600
        Vars.num_blocks = 12
        Vars.offset_percent = .9

    def __setattr__(self, name, value) -> None:
        object.__setattr__(self, name, value)

        Vars.block_size = (Vars.width / Vars.num_blocks) * Vars.offset_percent # figure out how to update these better
        Vars.blank_size = (Vars.width - (Vars.block_size * Vars.num_blocks)) / (Vars.num_blocks + 1)

        print("hi")

pygame.init()
vars = Vars()

fps = 24
fpsClock = pygame.time.Clock()

vars.height = 600

width, height = vars.width, vars.height
num_blocks = vars.num_blocks
offset_percent = vars.offset_percent

screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)

# -------------------------------------------------------------------------

offColor = '#424242'
onColor = '#f5f5f5'
gapColor = '#9e9e9e'

data = [[False for _ in range(num_blocks)] for _ in range(num_blocks)]
cube_boys = [[pygame.Rect(0,0, vars.block_size, vars.block_size) for i in range(num_blocks)] for i in range(num_blocks)]

edit = True
dt = 1
update_time = 12
start = False


# -------------------------------------------------------------------------------------------------

while True:    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()
        if event.type == VIDEORESIZE:
            width, height = event.size
            height = width
            update_vars()
            screen = pygame.display.set_mode((width,width), pygame.RESIZABLE)

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

    screen.fill(gapColor)


    for y in range(num_blocks):
        for x in range(num_blocks):
            # this only needs to run once if edit is off, but its dependednt on the two loops above
            cube_boys[y][x].topleft = (x * (vars.blank_size + vars.block_size) + vars.blank_size , y * (vars.blank_size + vars.block_size) + vars.blank_size)
            
            if dt >= update_time and start:
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
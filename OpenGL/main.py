import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from keyBinds import *
from random import randint

points = [[randint(-5, 5) for _ in range(3)] for i in range(100)]
points = [[0,1,3]]

for p in points:
    if [p[0] + 1, p[1], p[2]] in points:
        points.pop(p)

def cube(point, size=1):  # this is all very ugly and probably very slow
    glBegin(GL_LINES)

    def combinations_1(vert):
        for i in range(len(vert)):
            new = vert.copy()
            if(new[i] != point[i]):
                new[i] += size
            else:
                new[i] -= size

            glVertex3fv(tuple(vert))
            glVertex3fv(tuple(new))

    def combinations_2(vert):
        combinations_1(vert)
        for i in range(len(vert)):
            for j in range(i+1,len(vert)):
                new = vert.copy()
                new[i] -= size
                new[j] -= size
                combinations_1(new)

    combinations_2(point)

    glEnd()

def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0,0.0, -5)

    while True:
        # event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            for type, bul in key_flag.items(): # is this just too convoluted at this point?
                if event.type == type:
                    for kee, val in keys.items():
                        if event.key == val['code']:
                            val['flag'] = bul

        # moveing
        for key,val in keys.items():
            if val['flag']:
                glTranslatef(val['xDir'], val['yDir'], val['zDir'])

        # glRotatef(1, 1, 1, 2)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        
        # display all cubes
        for i in points:
            cube(i)

        pygame.display.flip()
        pygame.time.wait(10)

main()
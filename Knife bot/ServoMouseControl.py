import serial
import time
from codecs import decode
import pygame
from pygame.locals import *

'''
from math import sin, cos, radians
str(int(abs(180 * cos(radians(counter))))).zfill(3) + str(int(abs(180 * sin(radians(counter))))).zfill(3)
'''

pygame.init()

size = 180 * 4
width, height = size, size
konstant = size / 180
center = [width//2, height//2]

fps = 60
fpsClock = pygame.time.Clock()

screen = pygame.display.set_mode((width, height))
xy = [0,0]
num = 000000
fakeMousePos = [0,0]
LastPos = [0,0]
pygame.mouse.set_visible(False)

arduino = serial.Serial(port='COM3', baudrate=9600, timeout=0.01)

def cQUIT():
    arduino.close()
    pygame.quit()
    quit()

font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render(r'press "Q" to exit', True, (255,255,255))
textRect = text.get_rect()
textRect.center = tuple(center)


arduino.write(bytes(str(000000), 'utf-8'))

while True:
    screen.fill((0, 0, 0))
    screen.blit(text, textRect)

    for event in pygame.event.get():
        if event.type == QUIT:
            cQUIT()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                cQUIT()

        if event.type == pygame.MOUSEMOTION:
            xy = list(pygame.mouse.get_pos())
            diff = [xy[0] - center[0], xy[1] - center[1]]
            fakeMousePos = [fakeMousePos[0] + diff[0], fakeMousePos[1] + diff[1]]
            pygame.mouse.set_pos(width // 2, height // 2)
            
            # mouse prison   
            if fakeMousePos[0] >= width:
                fakeMousePos = [width, fakeMousePos[1]]
            if fakeMousePos[0] <= 0:
                fakeMousePos = [0, fakeMousePos[1]]
            if fakeMousePos[1] >= height:
                fakeMousePos = [fakeMousePos[0], height]
            if fakeMousePos[1] <= 0:
                fakeMousePos = [fakeMousePos[0], 0]
    

            num = int(180-(fakeMousePos[0] / konstant)) * 1000 + int(fakeMousePos[1] / konstant)
                
            arduino.write(bytes(str(num), 'utf-8'))

            # reading what the arduino gives back
            time.sleep(0.05)
            data = arduino.read(14) # num in read must = size of message
            out = decode(data, "unicode-escape") # from b string to normal string
            
            print(f"Arduino:  {out}\n Pygame:  X: {fakeMousePos[0]}  Y: {fakeMousePos[1]}\n\n", end="")

    fpsClock.tick(fps)
    pygame.display.update()

arduino.close()
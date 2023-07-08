# GTKM GAME JAM SNOOPY AND SKAJLAND
from player import bullet
from block import Block
import placeblock
from turret import Turret
import pygame
import time
import sys
screen = pygame.display.set_mode((800, 800))  # Creates the window
lastFrame = time.time_ns()
timePerFrame = 16666667
accumulator = 0
turret1 = Turret((400, 400))

blocks = []

all_bullets = [bullet(100,100)]

def update():

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                blocks.append(Block())
                placeblock.placeblock(blocks[-1])


def render():
    i = 0
    while i < len(all_bullets):
        bullet.render(all_bullets[i], screen)
        i+=1

    screen.fill('gray')
    for i in blocks:
        i.render(screen)
    turret1.render(screen)
    pygame.display.update()


while 1:
    currentTime = time.time_ns()

    accumulator += currentTime - lastFrame
    lastFrame = currentTime

    if accumulator >= timePerFrame:  # UPDATE I RENDER
        update()
        render()
        accumulator -= timePerFrame

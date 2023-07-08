# GTKM GAME JAM SNOOPY AND SKAJLAND
import player
from block import Block
from turret import Turret
import pygame
import time
import sys
screen = pygame.display.set_mode((800, 800))  # Creates the window
lastFrame = time.time_ns()
timePerFrame = 16666667
accumulator = 0
turret1 = Turret((400, 400))


def update():
    player.bullet.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                turret1.shoot()


def render():
    screen.fill('gray')
    turret1.render(screen)
    player.bullet.render()
    pygame.display.update()


while 1:
    currentTime = time.time_ns()

    accumulator += currentTime - lastFrame
    lastFrame = currentTime

    if accumulator >= timePerFrame:  # UPDATE I RENDER
        update()
        render()
        accumulator -= timePerFrame

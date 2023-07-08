# GTKM GAME JAM SNOOPY AND SKAJLAND
import pygame
import time
import sys
screen = pygame.display.set_mode((800, 800))  # Creates the window
lastFrame = time.time_ns()
timePerFrame = 16666667
accumulator = 0


def update():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print()

def render():
    screen.fill('White')
    pygame.display.update()


while 1:
    currentTime = time.time_ns()

    accumulator += currentTime - lastFrame
    lastFrame = currentTime

    if accumulator >= timePerFrame:  # UPDATE I RENDER
        update()
        render()
        accumulator -= timePerFrame

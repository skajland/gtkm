# GTKM GAME JAM SNOOPY AND SKAJLAND
from player import Player
from bullet import Bullet
from block import Block
from turret import Turret
import placeblock
import pygame
import time
import sys

screen = pygame.display.set_mode((800, 800))  # Creates the window
lastFrame = time.time_ns()
timePerFrame = 16666667
accumulator = 0
turret1 = Turret((screen.get_width() / 2, screen.get_height()))

blocks = []

all_bullets = [Bullet(200, 200)]
player1 = Player((screen.get_width() / 2, 0), (96, 96))


def update():
    for bullet in all_bullets:
        bullet.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                blocks.append(Block((96, 96)))
                placeblock.placeblock(blocks[-1])
    for block in blocks:
        for bullet in all_bullets:
            if bullet.bullet_rect.colliderect(block.block_rect):
                print("collision")


def render():
    screen.fill('darkgray')
    for bullet in all_bullets:
        bullet.render(screen)

    for block in blocks:
        block.render(screen)
    player1.render(screen)
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

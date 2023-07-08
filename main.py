# GTKM GAME JAM SNOOPY AND SKAJLAND
import asyncio
from button import Button
from player import Player
from bullet import Bullet
from block import Block
from turret import Turret
import placeblock
import pygame
import time
import sys

screen = pygame.display.set_mode((800, 800))  # Creates the window
turret1 = Turret((screen.get_width() / 2, screen.get_height()))

blocks = []

all_bullets = [Bullet(200, 800)]
player1 = Player((screen.get_width() / 2, 0), (96, 96))

button1 = Button("AMOGUS", (400, 400), (130, 130, 130, 70), (75, 75, 75, 50), (160, 160, 160, 150))


def update():
    screen.fill("darkgray")

    for bullet in all_bullets:
        bullet.update(blocks, screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if placeblock.endhighlight:
            if event.type == pygame.MOUSEBUTTONDOWN:
                placeblock.endhighlight = not placeblock.endhighlight

        button1.collision(event, equipblock)

    placeblock.blockhighlight()

    for block in blocks:
        for bullet in all_bullets:
            if bullet.bullet_rect.colliderect(block.block_rect):
                print("collision")


def equipblock():
    if not placeblock.endhighlight:
        blocks.append(Block((96, 96)))
        placeblock.block = blocks[-1]
    placeblock.endhighlight = not placeblock.endhighlight

def render():
    for bullet in all_bullets:
        bullet.render(screen)

    for block in blocks:
        block.render(screen)

    player1.render(screen)

    button1.render(screen)

    if placeblock.endhighlight:
        surf = pygame.Surface((placeblock.blockhighlite_rect.w, placeblock.blockhighlite_rect.h)).convert_alpha()
        surf.fill((23, 100, 255, 50))
        screen.blit(surf, (placeblock.blockhighlite_rect.x, placeblock.blockhighlite_rect.y))

    turret1.render(screen)
    pygame.display.update()


async def main():
    accumulator = 0
    lastFrame = time.time_ns()
    timePerFrame = 16666667
    while 1:
        currentTime = time.time_ns()

        accumulator += currentTime - lastFrame
        lastFrame = currentTime

        if accumulator >= timePerFrame:  # UPDATE I RENDER
            update()
            render()
            accumulator -= timePerFrame
        await asyncio.sleep(0)
asyncio.run(main())

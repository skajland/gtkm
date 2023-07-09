# GTKM GAME JAM SNOOPY AND SKAJLAND
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 800))  # Creates the window

import asyncio
import buttons
import usefull
from player import Player
from bullet import Bullet
from block import Block
from turret import Turret
import placeblock
import time
import sys

# screen = pygame.display.set_mode((800, 800))  # Creates the window
turret1 = Turret((screen.get_width() / 2, screen.get_height()))

all_bullets = [Bullet(200, 800)]
player1 = Player((screen.get_width() / 2, 0), (96, 96))


font = pygame.font.Font(None, 96)


def update():
    if not usefull.start_menu:
        screen.fill("darkgray")
        for bullet in all_bullets:
            bullet.update(usefull.blocks, screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            placeblock.update(event)
            buttons.update(event)

        placeblock.blockhighlight()

        for block in usefull.blocks:
            for bullet in all_bullets:
                if bullet.bullet_rect.colliderect(block.block_rect):
                    print("collision")
    else:
        screen.fill("darkgray")
        for event in pygame.event.get():
            buttons.start_screen_update(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


def equipblock(block_index):
    if not placeblock.endhighlight:
        usefull.blocks.append(Block(usefull.all_blocks[block_index[0]][0], usefull.all_blocks[block_index[0]][1]))
        placeblock.block = usefull.blocks[-1]
    placeblock.endhighlight = not placeblock.endhighlight


def render():
    if not usefull.start_menu:
        for bullet in all_bullets:
            bullet.render(screen)

        for block in usefull.blocks:
            block.render(screen)

        player1.render(screen)
        buttons.render()
        placeblock.render(screen)

        turret1.render(screen)
    else:
        rendered_font = font.render("Bulletron 2023", 1, 'Black')
        font_rect = rendered_font.get_rect()
        font_rect.center = (screen.get_width() / 2, screen.get_height() / 2 - 300)
        screen.blit(rendered_font, font_rect)
        buttons.start_screen_render()
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

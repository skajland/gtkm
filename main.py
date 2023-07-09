# GTKM GAME JAM SNOOPY AND SKAJLAND
import pygame
import asyncio
import buttons
import usefull
import player
from bullet import Bullet
from block import Block
import turret
import placeblock
import time
import sys

pygame.init()
screen = pygame.display.set_mode((912, 912))  # Creates the window
buttons.setup_buttons()
turret.setup()
player.setup()

all_bullets = [Bullet(200, 800)]

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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("summon")
                    all_bullets.append(Bullet(400, 800))
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

        player.render()
        buttons.render()
        placeblock.render(screen)

        turret.render()
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

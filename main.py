# GTKM GAME JAM SNOOPY AND SKAJLAND
import screens
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
menu1 = pygame.mixer.music.load("res/menu_comp.wav")
pygame.mixer.music.play(-1)
pygame.init()

screen = pygame.display.set_mode((912, 912))  # Creates the window
buttons.setup_buttons()
turret.setup()
player.setup()

all_bullets = [Bullet(200, 800)]

font = pygame.font.Font(None, 96)

ground = pygame.image.load("res/ground.png")


def update():
    if usefull.game_state == "Playing":
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
                    pygame.mixer.Sound("res/odbicie_comp.wav").play()
                    all_bullets.remove(bullet)
        for bullet in all_bullets:
            if bullet.bullet_rect.colliderect(player.player_rect):
                usefull.game_state = "Losing Screen"
    elif usefull.game_state == "Menu":
        screens.Menu.menu(screen)
    elif usefull.game_state == "Losing Screen":
        screens.LosingScreen.menu(screen)


def equipblock(block_index):
    if not placeblock.endhighlight:
        usefull.blocks.append(Block(usefull.all_blocks[block_index[0]][0], usefull.all_blocks[block_index[0]][1]))
        placeblock.block = usefull.blocks[-1]
    placeblock.endhighlight = not placeblock.endhighlight


def render():
    #screen.blit(ground,(32,32))


    if usefull.game_state == "Playing":
        for i in range(2):
            surf = pygame.Surface((912, 300)).convert_alpha()
            surf.fill((150, 50, 50, 50))  # Make Red
            screen.blit(surf, (0, 1*i*650))

        for bullet in all_bullets:
            bullet.render(screen)

        for block in usefull.blocks:
            block.render(screen)

        player.render()
        buttons.render()
        placeblock.render(screen)

        turret.render()
    elif usefull.game_state == "Menu":
        screens.Menu.render(screen, font)
    elif usefull.game_state == "Losing Screen":
        screens.LosingScreen.render(screen, font)
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

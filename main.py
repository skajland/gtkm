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
import waves
menu1 = pygame.mixer.music.load("res/menu_comp.wav")
pygame.mixer.music.play(-1)
pygame.init()

screen = pygame.display.set_mode((912, 912))  # Creates the window
buttons.setup_buttons()
turret.setup()
player.setup()

usefull.all_bullets = [Bullet(200, 800)]

font = pygame.font.Font(None, 96)

menu = pygame.transform.scale(pygame.image.load("res/Menu.png"), (24 * 6, 96 * 6))
menu_rect = menu.get_rect()
menu_rect.midright = (screen.get_width(), screen.get_height() / 2)

shadow = "1"

# ground = pygame.image.load("res/ground.png")

screen.fill("darkgray")
waves1 = 0
def update():
    global waves1
    if usefull.game_state == "Playing":
        if not len(usefull.all_bullets):
            for i in range(waves1):
                usefull.all_bullets.append(Bullet(400, 800))
            waves1 +=1

        for bullet in usefull.all_bullets:
            bullet.update(usefull.blocks, screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            placeblock.update(event)
            buttons.update(event)
        placeblock.blockhighlight()

        for block in usefull.blocks:
            for bullet in usefull.all_bullets:
                if bullet.bullet_rect.colliderect(block.block_rect):
                    pygame.mixer.Sound("res/odbicie_comp.wav").play()
                    usefull.all_bullets.remove(bullet)
        for bullet in usefull.all_bullets:
            if bullet.bullet_rect.colliderect(player.player_rect):
                usefull.game_state = "Losing Screen"
    elif usefull.game_state == "Menu":
        screens.Menu.menu(screen)
    elif usefull.game_state == "Losing Screen":
        screens.LosingScreen.menu(screen)


screen.fill("darkgray")
my_font = pygame.font.SysFont('Comic Sans MS', 30)
def render():
    global shadow
    #screen.blit(ground,(32,32))
    screen.fill("darkgray")

    if usefull.game_state == "Playing":
        for i in range(2):
            surf = pygame.Surface((912, 300)).convert_alpha()
            surf.fill((125, 60, 60, 50))  # Make Red
            screen.blit(surf, (0, 1*i*650))


        for bullet in usefull.all_bullets:
            bullet.render(screen)

        for block in usefull.blocks:
            block.render(screen)
        surf = pygame.Surface((90, 912))

        surf.fill((100, 100, 100, 50))  # Make Red
        screen.blit(surf, (840, 0))

        waves.render(screen)
        player.render()
        placeblock.render(screen)
        screen.blit(menu, menu_rect)
        buttons.render()
        turret.render()
        t = my_font.render("wave " + str(shadow), False, (0, 0, 0))
        screen.blit(t, (10, 10))
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

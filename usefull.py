import pygame
import sys

start_menu = True

blocks = []

all_blocks = (
    ("res/Brick.png", (96, 96)), ("res/Vase.png", (19 * 3.2, 31 * 3.2)),
    ("res/wiatrak/wiatrak1.png", (19 * 3.2, 31 * 4)))

def game_exit():
    pygame.quit()
    sys.exit()

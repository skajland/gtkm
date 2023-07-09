import pygame
import sys

game_state = "Menu"

blocks = []

all_blocks = (
    ("res/Brick.png", (96, 96)), ("res/Vase.png", (19 * 3.2, 31 * 3.2)),
    ("res/wiatrak/wiatrak1.png", (19 * 3.2, 31 * 4)))


def game_exit():
    pygame.quit()
    sys.exit()


def play_again():
    global game_state
    game_state = "Playing"

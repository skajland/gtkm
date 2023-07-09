import pygame
import sys
from block import Block
game_state = "Menu"


all_blocks = (
    ("res/Brick.png", (96, 96)), ("res/Vase.png", (19 * 3.2, 31 * 3.2)),
    ("res/wiatrak/wiatrak1.png", (19 * 3.2, 31 * 4)))

blocks = [Block(all_blocks[0][0], (100,912)), Block(all_blocks[0][0], (200,912))]
blocks[0].block_rect.x = -100
blocks[1].block_rect.x = +950
def game_exit():
    pygame.quit()
    sys.exit()


def play_again():
    global game_state
    game_state = "Playing"

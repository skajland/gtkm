import pygame
import sys
import waves
from block import Block
from bullet import Bullet
game_state = "Menu"


all_blocks = (
    ("res/Brick.png", (96, 96), 75, 15), ("res/Vase.png", (19 * 3.2, 31 * 3.2), 25, 5),
    ("res/wiatrak/wiatrak1.png", (19 * 3.2, 31 * 4), 50, 10))


all_bullets = [Bullet(200, 800)]

blocks = [Block(all_blocks[0][0], (100, 912), all_blocks[0][2]), Block(all_blocks[0][0], (200,912), all_blocks[0][2])]
blocks[0].block_rect.x = -100
blocks[1].block_rect.x = +850


def game_exit():
    pygame.quit()
    sys.exit()


def play_again(state):
    global game_state
    waves.waves = 0
    waves.coins = waves.coins_default
    all_bullets.clear()
    blocks.clear()
    print(state[0])
    game_state = state[0]

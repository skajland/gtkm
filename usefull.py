import pygame
import sys
import waves
from block import Block
from bullet import Bullet
game_state = "Menu"

waves1 = 0

all_blocks = (
    ("res/Brick.png", (96, 96), 75, 30), ("res/Vase.png", (19 * 3.2, 31 * 3.2), 50, 15),
    ("res/wiatrak/wiatrak1.png", (72, 92), 50, 20), ("res/barrel.png", (72, 80), 75, 15), ("res/Apple.png", (54, 64), 25, 5))


all_bullets = [Bullet(200, 800)]

blocks = [Block(all_blocks[0][0], (100, 912), all_blocks[0][2]), Block(all_blocks[0][0], (200,912), all_blocks[0][2])]
blocks[0].health = 9999999
blocks[1].health = 9999999
blocks[0].block_rect.x = -100
blocks[1].block_rect.x = +850


def game_exit():
    pygame.quit()
    sys.exit()


def play_again(state):
    global game_state, waves1, blocks
    waves1 = 0
    waves.coins = waves.coins_default
    all_bullets.clear()
    blocks.clear()
    blocks = [Block(all_blocks[0][0], (100, 912), all_blocks[0][2]),
              Block(all_blocks[0][0], (200, 912), all_blocks[0][2])]
    blocks[0].health = 999999
    blocks[1].health = 999999
    blocks[0].block_rect.x = -100
    blocks[1].block_rect.x = +850
    game_state = state[0]

import pygame


def placeblock(block):
    block.block_rect = pygame.mouse.get_pos()
    pass  # will spawn the block and follow the mouse
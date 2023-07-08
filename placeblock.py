import pygame


def placeblock(block):
    block.block_rect.center = pygame.mouse.get_pos()

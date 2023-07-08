import pygame


class Block:

    def __init__(self):
        self.block_img = pygame.image.load("res/TestBlock.png")
        self.block_rect = self.block_img.get_rect()

    def render(self, screen):
        screen.blit(self.block_img, self.block_rect)

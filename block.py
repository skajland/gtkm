import pygame


class Block:

    def __init__(self, scaler):
        self.block_img = pygame.transform.scale(pygame.image.load("res/Brick.png"), scaler)
        self.block_rect = self.block_img.get_rect()

    def render(self, screen):
        screen.blit(self.block_img, self.block_rect)

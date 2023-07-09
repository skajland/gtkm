import pygame


class Block:

    def __init__(self, img, scaler, health):
        self.block_img = pygame.transform.scale(pygame.image.load(img), scaler)
        self.block_rect = self.block_img.get_rect()
        self.health = health


    def render(self, screen):
        screen.blit(self.block_img, self.block_rect)

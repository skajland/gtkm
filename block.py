import pygame


class Block:
    block_img = pygame.image.load("res/TestBlock.png")
    block_rect = block_img.get_rect()

    def render(self, screen):
        screen.blit(self.block_img, self.block_rect)

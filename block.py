import pygame


class Block:
    fan1 = pygame.image.load("res/Bullet.png")
    fan2 = pygame.image.load("res/Bullet.png")
    fan3 = pygame.image.load("res/Bullet.png")
    def __init__(self, img, scaler, health):
        self.block_img = pygame.transform.scale(pygame.image.load(img), scaler)
        self.block_rect = self.block_img.get_rect()
        self.health = health
        self.stagefan = 0

    def render(self, screen):
        screen.blit(self.block_img, self.block_rect)
    def renderfan(self, screen):
        self.stagefan += 1
        if self.stagefan == 1:
            screen.blit(self.block_img, self.block_rect)
        elif self.stagefan == 2:
            screen.blit(self.block_img, self.block_rect)
        elif self.stagefan == 3:
            screen.blit(self.block_img, self.block_rect)
            self.stagefan = 0

import dataclasses

import pygame


class Bullet:
    bullet_img = pygame.image.load("res/Turret.png")

    def __init__(self, x, y):
        self.bullet_rect = self.bullet_img.get_rect()
        self.bullet_rect.x = x
        self.bullet_rect.y = y
    def ray(self,blocks ,screen):
        for i in range(5):
            screen.blit(self.bullet_img, (500, 400))

            for block in blocks:
                block.block_rect.collidepoint((self.bullet_rect.x * i, self.bullet_rect.y * i))
                screen.blit(self.bullet_img,(self.bullet_rect.x * i, self.bullet_rect.y * i))

    def update(self,blocks, screen):
        self.bullet_rect.y -= 0
        self.ray(blocks,screen)
    def render(self, screen):
        screen.blit(self.bullet_img, self.bullet_rect)  # Renders the object

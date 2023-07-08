import dataclasses

import pygame


class Bullet:
    bullet_img = pygame.image.load("res/Turret.png")

    def __init__(self, x, y):
        self.bullet_rect = self.bullet_img.get_rect()
        self.bullet_rect.x = x
        self.bullet_rect.y = y
    def ray(self):
        print()
    def update(self,blocks):
        self.bullet_rect.y += 1
        for block in blocks:
            print(block.block_rect.x)
    def render(self, screen):
        screen.blit(self.bullet_img, self.bullet_rect)  # Renders the object

import dataclasses

import pygame


class Bullet:
    bullet_img = pygame.image.load("res/Turret.png")

    def __init__(self, x, y):
        self.bullet_rect = self.bullet_img.get_rect()
        self.bullet_rect.x = x
        self.bullet_rect.y = y

    def update(self):
        self.y+=1

    def render(self, screen):
        screen.blit(self.bullet_img, self.bullet_rect)  # Renders the object

import dataclasses
import math

import pygame


class Bullet:
    bullet_img = pygame.image.load("res/Turret.png")

    def __init__(self, x, y):
        self.bullet_rect = self.bullet_img.get_rect()
        self.bullet_rect.x = x
        self.bullet_rect.y = y
    def ray(self,blocks ,screen):
        for i in range(5):
            radians = math.radians(20)#MAKE COMP(INTER) TIME

            x = self.bullet_rect.x + math.sin(radians) *50 * i
            y = self.bullet_rect.y - math.cos(radians) *50 * i

            for block in blocks:
                if block.block_rect.collidepoint((x, y)):
                    print("COL RAY")
                screen.blit(self.bullet_img,(x,y))

    def update(self,blocks, screen):
        self.bullet_rect.y -= 1
        self.ray(blocks,screen)
    def render(self, screen):
        screen.blit(self.bullet_img, self.bullet_rect)  # Renders the object

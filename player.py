import dataclasses

import pygame


class bullet:
    bullet_img = pygame.image.load("res/Turret.png")
    start_pos = ()
    def __init__(self,x,y ):
        self.x=x
        self.y=y
    bullet_pos = ()
    def update(self):
        print()
    def render(self,screen):
        screen.blit(self.bullet_img,(self.x, self.y))  # Renders the object

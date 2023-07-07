import pygame


class Zombie:
    zombie = pygame.image.load("images/Zombie.png")
    zombie_rect = zombie.get_rect()
    start_pos = ()

    def __init__(self, start_pos):
        self.start_pos = start_pos
        self.zombie_rect.y, self.zombie_rect.x = start_pos

    def move(self):
        self.zombie_rect.x -= 1

    def render(self, display):
        display.blit(self.zombie, self.zombie_rect)

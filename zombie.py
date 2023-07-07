import pygame


class Zombie:
    zombie = pygame.image.load("images/Zombie.png")
    # gets the rect of the image
    zombie_rect = zombie.get_rect()
    start_pos = ()

    def __init__(self, start_pos):
        # start position
        self.start_pos = start_pos
        self.zombie_rect.y, self.zombie_rect.x = start_pos

    def move(self):
        # Moves the zombie left
        self.zombie_rect.x -= 1

    def render(self, display):
        # Renders the zombie
        display.blit(self.zombie, self.zombie_rect)

import pygame


class Turret:
    turret_img = pygame.image.load("res/Turret.png")
    turret_rect = turret_img.get_rect()  # gets the rect of the image
    start_pos = ()

    def __init__(self, start_pos):
        # start position
        self.start_pos = start_pos
        self.turret_rect.y, self.turret_rect.x = start_pos

    def shoot(self):
        self.turret_rect.x -= 1

    def render(self, screen):
        screen.blit(self.turret_img, self.turret_rect)  # Renders the object

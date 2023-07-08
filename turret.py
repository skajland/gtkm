import pygame


class Turret:
    turret_img = pygame.transform.scale(pygame.image.load("res/Turret.png"), (128, 128))

    def __init__(self, start_pos):
        # start position
        self.start_pos = start_pos
        self.turret_rect = self.turret_img.get_rect()  # gets the rect of the image
        self.turret_rect.centerx, self.turret_rect.bottom = start_pos

    def shoot(self):
        self.turret_rect.x -= 1

    def render(self, screen):
        screen.blit(self.turret_img, self.turret_rect)  # Renders the object

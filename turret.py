import pygame


turret_img = pygame.transform.scale(pygame.image.load("res/Turret.png"), (128, 128))

screen = pygame.display.get_surface()

turret_rect = turret_img.get_rect()  # gets the rect of the image


def setup():
    global screen
    screen = pygame.display.get_surface()
    turret_rect.centerx, turret_rect.bottom = (screen.get_width() / 2, screen.get_height())


def shoot(self):
    self.turret_rect.x -= 1


def render():
    screen.blit(turret_img, turret_rect)  # Renders the object

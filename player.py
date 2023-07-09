import pygame


player_img = pygame.image.load("res/Dziad.png")


player_img = pygame.transform.scale(player_img, (128, 128))
player_rect = player_img.get_rect()
screen = None


def setup():
    global screen
    screen = pygame.display.get_surface()
    player_rect.centerx, player_rect.y = (screen.get_width() / 2, 40)


def render():
    screen.blit(player_img, player_rect)

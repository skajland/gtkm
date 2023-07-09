import pygame
coins_default = 50
coins = coins_default
font = pygame.font.Font(None, 64)


def render(screen):
    rendered_font = font.render(str(coins), 1, 'Black')
    font_rect = rendered_font.get_rect()
    font_rect.center = (screen.get_width() - 120, screen.get_height() / 2 - 350)
    screen.blit(rendered_font, font_rect)
    coins_img = pygame.image.load("res/Coins.png")
    coins_img_rect = coins_img.get_rect()
    coins_img_rect.midleft = (screen.get_width() - 100, screen.get_height() / 2 - 350)
    screen.blit(coins_img, coins_img_rect)

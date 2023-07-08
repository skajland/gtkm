import pygame


class Player:
    player_img = pygame.image.load("res/Dziad.png")

    def __init__(self, pos, scaler):
        self.player_img = pygame.transform.scale(self.player_img, scaler)
        self.player_rect = self.player_img.get_rect()
        self.player_rect.centerx, self.player_rect.y = pos

    def render(self, screen):
        screen.blit(self.player_img, self.player_rect)

import pygame


class bullet:
    bullet_img = pygame.image.load("res/Turret.png")
    bullet_rect = bullet_img.get_rect()  # gets the rect of the image
    start_pos = ()

    def __init__(self, start_pos):
        # start position
        self.start_pos = start_pos
        self.bullet_rect.y, self.bullet_rect.x = start_pos
    def update(self):
        print()
    def render(self, screen):
        screen.blit(self.bullet_rect, self.bullet_rect)  # Renders the object

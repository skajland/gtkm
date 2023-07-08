import pygame

pygame.init()


class Button:

    def __init__(self, what_to_say, pos):
        self.font = pygame.font.Font(None, 64)
        self.rendered_font = self.font.render(what_to_say, True, 'Black')
        self.font_rect = self.rendered_font.get_rect()
        self.font_rect.center = pos
        self.fader = False

    def collision(self, event):
        if self.font_rect.collidepoint(pygame.mouse.get_pos()):
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("PRESSED")
            self.fader = True
        else:
            self.fader = False

    def render(self, screen):
        screen.blit(self.rendered_font, self.font_rect)
        if self.fader:
            pygame.draw.rect(screen, 'Red', self.font_rect)

import pygame
pygame.init()


class Button:

    def __init__(self, what_to_say, pos, default_color, button_hovering_color, button_pressed_color, *func_arguments):
        self.func_arguments = func_arguments
        self.default_color = default_color
        self.button_hovering_color = button_hovering_color
        self.button_pressed_color = button_pressed_color
        self.font = pygame.font.Font(None, 64)
        self.rendered_font = self.font.render(what_to_say, True, 'Black')
        self.font_rect = self.rendered_font.get_rect()
        self.font_rect.midleft = pos
        self.button_state = "None"
        self.mouse_down = False

    def collision(self, event, func):
        if self.font_rect.collidepoint(pygame.mouse.get_pos()):
            if event.type == pygame.MOUSEBUTTONDOWN:
                if len(self.func_arguments) > 0:
                    func(self.func_arguments)
                self.button_state = "Pressed"
                self.mouse_down = True
            if event.type == pygame.MOUSEBUTTONUP:
                self.mouse_down = False
            if not self.mouse_down:
                self.button_state = "Hovering"
        else:
            self.button_state = "None"

    def render(self, screen):

        surf = pygame.Surface((self.font_rect.w, self.font_rect.h)).convert_alpha()
        screen.blit(self.rendered_font, self.font_rect)
        if self.button_state == "Pressed":
            surf.fill(self.button_pressed_color)
        elif self.button_state == "Hovering":
            surf.fill(self.button_hovering_color)
        else:
            surf.fill(self.default_color)

        screen.blit(surf, self.font_rect)


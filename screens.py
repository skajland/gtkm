import pygame
import buttons
import sys
import usefull


class LosingScreen:
    @staticmethod
    def menu(screen):
        screen.fill("darkgray")
        for event in pygame.event.get():
            buttons.play_again.collision(event, usefull.play_again)
            buttons.exit_button.collision(event, usefull.game_exit)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    @staticmethod
    def render(screen, font):
        rendered_font = font.render("You Won", 1, 'Black')
        font_rect = rendered_font.get_rect()
        font_rect.center = (screen.get_width() / 2, screen.get_height() / 2 - 300)
        buttons.play_again.render(screen)
        buttons.exit_button.render(screen)
        screen.blit(rendered_font, font_rect)


class Menu:
    @staticmethod
    def menu(screen):
        screen.fill("darkgray")
        for event in pygame.event.get():
            buttons.start_screen_update(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    @staticmethod
    def render(screen, font):
        rendered_font = font.render("Bulletron 2023", 1, 'Black')
        font_rect = rendered_font.get_rect()
        font_rect.center = (screen.get_width() / 2, screen.get_height() / 2 - 300)
        screen.blit(rendered_font, font_rect)
        buttons.start_screen_render()





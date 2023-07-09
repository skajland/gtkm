from button import Button
import usefull
import placeblock
import pygame
screen = None
start_button = None
exit_button = None
item_button1 = None
item_button2 = None
item_button3 = None
play_again = None


def setup_buttons():
    global start_button, exit_button, item_button1, item_button2, item_button3, screen, play_again
    screen = pygame.display.get_surface()
    play_again = Button("Play Again", (screen.get_width() / 2, screen.get_height() / 2), 96, (130, 130, 130, 70),
                          (75, 75, 75, 50), (160, 160, 160, 150))
    start_button = Button("Play", (screen.get_width() / 2, screen.get_height() / 2), 96, (130, 130, 130, 70), (75, 75, 75, 50), (160, 160, 160, 150))
    exit_button = Button("Exit", (screen.get_width() / 2, screen.get_height() / 2 + 96), 96, (130, 130, 130, 70), (75, 75, 75, 50), (160, 160, 160, 150))
    item_button1 = Button(pygame.image.load("res/Brick.png"), (screen.get_width() - 30, 200), 64, (130, 130, 130, 70), (75, 75, 75, 50), (160, 160, 160, 150), 0)
    item_button2 = Button(pygame.image.load("res/Vase.png"), (screen.get_width() - 30, 250), 64, (130, 130, 130, 70), (75, 75, 75, 50), (160, 160, 160, 150), 1)
    item_button3 = Button(pygame.image.load("res/wiatrak/wiatrak1.png"), (screen.get_width() - 30, 300), 64, (130, 130, 130, 70), (75, 75, 75, 50), (160, 160, 160, 150), 2)


def update(event):
    item_button1.collision(event, placeblock.equipblock)
    item_button2.collision(event, placeblock.equipblock)
    item_button3.collision(event, placeblock.equipblock)


def start_screen_update(event):
    start_button.collision(event, getoutofstartmenu)
    exit_button.collision(event, usefull.game_exit)


def getoutofstartmenu():
    usefull.game_state = "Playing"


def playagain():
    usefull.game_state = "Playing"


def render():
    item_button1.render(screen)
    item_button2.render(screen)
    item_button3.render(screen)


def start_screen_render():
    start_button.render(screen)
    exit_button.render(screen)

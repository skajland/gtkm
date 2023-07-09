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
item_button4 = None
item_button5 = None
play_again = None
menu_button = None


def setup_buttons():
    global start_button, exit_button, item_button1, item_button2, item_button3, screen, play_again, menu_button, item_button4, item_button5
    screen = pygame.display.get_surface()
    play_again = Button("Play Again", (screen.get_width() / 2, screen.get_height() / 2), 96, (130, 130, 130, 70),
                          (75, 75, 75, 50), (160, 160, 160, 150), "Playing")
    start_button = Button("Play", (screen.get_width() / 2, screen.get_height() / 2), 96, (130, 130, 130, 70), (75, 75, 75, 50), (160, 160, 160, 150), "Playing")
    menu_button = Button("Menu", (screen.get_width() / 2, screen.get_height() / 2 + 96), 96, (130, 130, 130, 70),(75, 75, 75, 50), (160, 160, 160, 150), "Menu")
    exit_button = Button("Exit", (screen.get_width() / 2, screen.get_height() / 2 + 96), 96, (130, 130, 130, 70), (75, 75, 75, 50), (160, 160, 160, 150))
    item_button1 = Button(pygame.transform.scale(pygame.image.load("res/Brick.png"), (52, 52)), (screen.get_width() - 60, 282), 64, (130, 130, 130, 70), (75, 75, 75, 50), (160, 160, 160, 150), 0)
    item_button2 = Button(pygame.transform.scale(pygame.image.load("res/Vase.png"), (20 * 2, 32 * 2)), (screen.get_width() - 60, 378), 64, (130, 130, 130, 70), (75, 75, 75, 50), (160, 160, 160, 150), 1)
    item_button3 = Button(pygame.transform.scale(pygame.image.load("res/wiatrak/wiatrak1.png"), (48, 64)), (screen.get_width() - 60, 474), 64, (130, 130, 130, 70), (75, 75, 75, 50), (160, 160, 160, 150), 2)
    item_button4 = Button(pygame.transform.scale(pygame.image.load("res/barrel.png"), (64, 64)), (screen.get_width() - 60, 570), 64, (130, 130, 130, 70), (75, 75, 75, 50), (160, 160, 160, 150), 3)
    item_button5 = Button(pygame.transform.scale(pygame.image.load("res/Apple.png"), (54, 64)), (screen.get_width() - 60, 570 + 96), 64, (130, 130, 130, 70), (75, 75, 75, 50), (160, 160, 160, 150), 4)

def update(event):
    item_button1.collision(event, placeblock.equipblock)
    item_button2.collision(event, placeblock.equipblock)
    item_button3.collision(event, placeblock.equipblock)
    item_button4.collision(event, placeblock.equipblock)
    item_button5.collision(event, placeblock.equipblock)


def start_screen_update(event):
    start_button.collision(event, getoutofstartmenu)
    exit_button.collision(event, usefull.game_exit)


def getoutofstartmenu(game_state):
    usefull.game_state = game_state[0]
    gamemus = pygame.mixer.music.load("res/game_comp.wav")
    pygame.mixer.music.play(-1)



def playagain():
    usefull.game_state = "Playing"


def render():
    item_button1.render(screen)
    item_button2.render(screen)
    item_button3.render(screen)
    item_button4.render(screen)
    item_button5.render(screen)


def start_screen_render():
    start_button.render(screen)
    exit_button.render(screen)

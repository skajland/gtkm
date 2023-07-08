import pygame

endhighlight = False
block = None


def update():
    blockhighlight()


def blockhighlight():
    global endhighlight, block
    if endhighlight:
        placeblock()


def placeblock():
    global block
    block.block_rect.center = pygame.mouse.get_pos()

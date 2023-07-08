import pygame

endhighlight = False
holding_shift = False
block = None

blockhighlite_rect = pygame.Rect(5, 5, 5, 5)


def blockhighlight():
    global endhighlight, block
    if endhighlight:
        placeblock()
        blockhighlite_rect.update(block.block_rect.x, block.block_rect.y, block.block_rect.width, block.block_rect.height)


def placeblock():
    global block
    block.block_rect.center = pygame.mouse.get_pos()

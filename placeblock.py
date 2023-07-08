import pygame
from block import Block

endhighlight = False
holding_shift = False
block = None

blockhighlite_rect = pygame.Rect(5, 5, 5, 5)


def blockhighlight():
    global block
    if endhighlight:
        placeblock()
        blockhighlite_rect.update(block.block_rect.x, block.block_rect.y, block.block_rect.width, block.block_rect.height)


def placeblock():
    global block
    block.block_rect.center = pygame.mouse.get_pos()


def equipblock(blocks, all_blocks, block_index):
    global endhighlight, block
    if not endhighlight:
        blocks.append(Block(all_blocks[block_index[0]][0], all_blocks[block_index[0]][1]))
        block = blocks[-1]
    endhighlight = not endhighlight
    return blocks

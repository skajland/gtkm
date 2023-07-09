import pygame

import player
import turret
import usefull
from block import Block

endhighlight = False
holding_shift = False
block = None
can_be_placed = True
blockhighlite_rect = pygame.Rect(5, 5, 5, 5)


def blockhighlight():
    global block, can_be_placed
    if endhighlight:
        placeblock()
        blockhighlite_rect.update(block.block_rect.x, block.block_rect.y, block.block_rect.width, block.block_rect.height)
        for block_checker in usefull.blocks:
            if not block_checker == usefull.blocks[-1]:
                if block_checker.block_rect.colliderect(blockhighlite_rect):
                    can_be_placed = False
                    break
                else:
                    can_be_placed = True
            if blockhighlite_rect.top >= player.player_rect.bottom + 100 and blockhighlite_rect.bottom + 100 <= turret.turret_rect.top:
                can_be_placed = True
            else:
                can_be_placed = False


def update(event):
    global endhighlight
    if can_be_placed:
        if endhighlight:
            if event.type == pygame.MOUSEBUTTONDOWN:
                endhighlight = not endhighlight


def render(screen):
    global can_be_placed
    if endhighlight:
        surf = pygame.Surface((blockhighlite_rect.w, blockhighlite_rect.h)).convert_alpha()

        if can_be_placed:
            surf.fill((23, 100, 255, 50))
        else:
            surf.fill((150, 50, 50, 50)) # Make Red
        screen.blit(surf, (blockhighlite_rect.x, blockhighlite_rect.y))

def placeblock():
    global block
    block.block_rect.center = pygame.mouse.get_pos()


def equipblock(block_index):
    global endhighlight, block
    if not endhighlight:
        usefull.blocks.append(Block(usefull.all_blocks[block_index[0]][0], usefull.all_blocks[block_index[0]][1]))
        block = usefull.blocks[-1]
    endhighlight = not endhighlight
    return usefull.blocks

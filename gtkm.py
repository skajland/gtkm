import pygame
# GTKM GAME JAM SNOOPY AND SKAJLAND

running = True

while running:
    print("test")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

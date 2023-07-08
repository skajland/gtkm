import dataclasses
import math
import random
import pygame

import block


class Bullet:
    bullet_img = pygame.transform.scale(pygame.image.load("res/Bullet.png"), (7 * 3, 16 * 3))
    bullet_img2 = pygame.image.load("res/Bullet.png")
    def __init__(self, x, y):
        self.bullet_rect = self.bullet_img.get_rect()
        self.bullet_rect.x = x
        self.bullet_rect.y = y
        self.dir = 0
    def bulletdir(self):
        radians = math.radians(self.dir)
        self.bullet_rect.x += math.sin(radians)*4
        self.bullet_rect.y -= math.cos(radians)

    def rotpos(self, i , rad):
        radians = math.radians(rad)+math.radians(self.dir)

        x = self.bullet_rect.x + math.sin(radians) * 50 * i
        y = self.bullet_rect.y - math.cos(radians) * 50 * i
        return x,y

    def rotpos2(self, i, rad):
        radians = math.radians(rad)

        x = self.bullet_rect.x + math.sin(radians) * 50 * i
        y = self.bullet_rect.y - math.cos(radians) * 50 * i
        return x, y

    def ray(self,blocks ,screen):
        hitF = False
        hitL = False
        hitR = False

        for i in range(7):
            xL,yL = self.rotpos(i, 20)
            x0,y0 = self.rotpos(i, 0)
            xR,yR = self.rotpos(i, -20)


            for block in blocks:
                def b(o):
                    return block.block_rect.collidepoint(o)

                if b(self.rotpos(i, 0)) or b(self.rotpos(i, 10)) or b(self.rotpos(i, -10)):
                    hitF=True
                if b(self.rotpos(i, 20)) or b(self.rotpos(i, 10)):
                    hitL=True
                if b(self.rotpos(i, -20)) or b(self.rotpos(i, -10)):
                    hitR = True

                #screen.blit(self.bullet_img,(xL,yL))
                #screen.blit(self.bullet_img,(xR,yR))
                #screen.blit(self.bullet_img,(x0,y0))

        #self.bullet_rect.y -= 1
        if not hitF:
            return
        if not hitL:
            self.dir += 1
            return
        if not hitR:
            self.dir -= 1
            return
    def rcb(self, blocks ,screen):
        hitL = False
        hitR = False
        for i in range(2):  # ALERT RCB


            for block in blocks:
                x, y = self.rotpos2(i, 20)

                def b(o):
                    return block.block_rect.collidepoint((o))

                if b(self.rotpos2(i, 80)):
                    hitL = True
                if b(self.rotpos2(i, -80)):
                    hitR = True
                #screen.blit(self.bullet_img2, (x, y))
                #screen.blit(self.bullet_img2, (self.rotpos2(i, 20)))

        if hitL:
            self.dir -= 5
            return
        if hitR:
            self.dir += 5
            return


    def update(self,blocks, screen):
        self.bulletdir()
        self.ray(blocks,screen)
        self.rcb(blocks,screen)

    def render(self, screen):
        rot = pygame.transform.rotate(self.bullet_img,-self.dir+3)
        screen.blit(rot, (self.bullet_rect.x-12 , self.bullet_rect.y))  # Renders the object

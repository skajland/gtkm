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
        self.hashonged = 0 #has changed
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
            self.hashonged +=1
            return
        print(random.random)
        if not hitL:
            self.hashonged = 0
            self.dir += 1
            return
        if not hitR:
            self.hashonged = 0
            self.dir -= 1
            return
    def rcb(self, blocks ,screen):
        hitF = False
        hitL = False
        hitR = False
        for i in range(2):  # ALERT RCB


            for block in blocks:
                x, y = self.rotpos2(i, 20)

                def b(o):
                    return block.block_rect.collidepoint((o))

                if not b(self.rotpos2(i, 0)):
                    hitF = True
                if b(self.rotpos2(i, 80)):
                    hitL = True
                if b(self.rotpos2(i, -80)):
                    hitR = True
                #screen.blit(self.bullet_img2, (x, y))
                #screen.blit(self.bullet_img2, (self.rotpos2(i, 0)))

        if self.dir > 80:
            self.dir = 80
        elif self.dir < -80:
            self.dir = -80

        if hitL:
            self.dir -= 5

        elif hitR:
            self.dir += 5
        if self.bullet_rect.y < 200:
            if self.bullet_rect.x > 400:
                self.dir -= 1
            if self.bullet_rect.x < 400:
                self.dir += 1

        '''elif hitF :
            if self.dir > 0:
                self.dir -= 1
            elif self.dir < -0:
                self.dir += 1
'''
    def update(self,blocks, screen):
        self.bulletdir()
        self.ray(blocks,screen)
        self.rcb(blocks,screen)

    def render(self, screen):
        rot = pygame.transform.rotate(self.bullet_img,-self.dir+3)
        screen.blit(rot, (self.bullet_rect.x-12 , self.bullet_rect.y))  # Renders the object

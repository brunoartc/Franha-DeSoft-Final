import pygame
import sys
from pygame.locals import *
import random

def menu(self):
	count = 0
	pygame.mouse.set_visible(1)
 	solo = Botao(400,300,"solo.png")
	multi = Botao(400,400,"multi.png")
    exit = Botao(400,500,"sair.png")
    cursor = Cursor([0,0])
    botoes = []
    botoes.append(solo)
    botoes.append(multi)
    botoes.append(exit)
    while 1:
        count += 1
        self.clock.tick(600)
 
        for event in pygame.event.get():

class Botao(pygame.sprite.Sprite):
     def __init__(self, x, y, image):
         pygame.sprite.Sprite.__init__(self)
         self.image = pygame.image.load(image)
         self.original = pygame.image.load(image)
         self.angulo = 0
         #posicao no quadro
         self.rect = self.image.get_rect()
         #posicao relativa
         self.pos_x = x
         self.pos_y = y

         self.rect.x = x
         self.rect.y = y

     def __str__(self):
         return self.name
 
 class Cursor(pygame.sprite.Sprite):
     def __init__(self, pos):
         pygame.sprite.Sprite.__init__(self)
         self.image = pygame.image.load("cursor.png")
         self.rect  = self.image.get_rect()
         self.rect.x, self.rect.y = pos
         self.selec = 1
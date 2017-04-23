import pygame
import sys
from pygame.locals import *
import random

class personagem:
	def __init__(self, vel):
		self.x=987/2
		self.y=607/2
		self.velocidade=vel
class obstaculo:
	def __init__(self):
		self.x=987
		self.yc=random.randint(-580,-200)
		self.yb=self.yc+607+random.randint(70,200)
		self.vel=1
		
cabron = personagem(1)
#sys.path.append('./data')
tela = pygame.display.set_mode((987, 607), 0, 32)
pygame.display.set_caption('Franha')
fundo = pygame.image.load("fundo.jpg").convert()
ara = pygame.image.load("a.png").convert_alpha()
pare = pygame.image.load("pareda.jpg").convert()

pareda=[]
pareda.append(obstaculo())


i=0
while True:
	tela.blit(fundo, (0, 0))

	while i < len(pareda):
		pareda[i].x-=pareda[i].vel	
		tela.blit(pare, (pareda[i].x , pareda[i].yc))
		tela.blit(pare, (pareda[i].x , pareda[i].yb))
		if pareda[i].x<-97:
			del pareda[i]
		if pareda[-1].x<(607-97):
			pareda.append(obstaculo())
		i+=1
				

	if i == len(pareda):
		i=0
		
	
	
	
	tela.blit(ara, (cabron.x-100,cabron.y-117/2))
	
	
	
	tecla = pygame.key.get_pressed()
	if tecla[K_SPACE] and (cabron.y+117)>200:
		cabron.y-=cabron.velocidade
	elif (cabron.y+50)<607:
		cabron.y+=cabron.velocidade
		
		
	for event in pygame.event.get():
		if event.type == QUIT:
				exit()
				
				
	pygame.display.update()
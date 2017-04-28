import pygame
import sys
from pygame.locals import *
import random

lin=[120,360,620]

class carro:
	def __init__(self, vel):
		self.pos=1
		self.x=lin[self.pos]-51
		self.y=1080/2-86
		self.vel=1

class obstaculo:
	def __init__(self):
		self.pos=random.randint(0,2)
		self.x=lin[self.pos]-120
		self.y=-164
		
	
		
	
#sys.path.append('./data')
pygame.font.init()
fonte = pygame.font.SysFont("monospace", 15)
pnt=0
tela = pygame.display.set_mode((720, 540), 0, 32)
pygame.display.set_caption('Oarro')
fundo = pygame.image.load("fundo.png").convert()
ara = pygame.image.load("carro.png").convert_alpha()
pare = pygame.image.load("obstaculo.png").convert()
tecla = pygame.key.get_pressed()
def NewGame():
	pnt=10
	TED=carro(1)

	obs=[]
	
	obs.append(obstaculo())



	i=0
	while True:
		tela.blit(fundo, (0, 0))
		
		i=0
		while i<len(obs):
			obs[i].y+=TED.vel
			if obs[-1].y>720/4:
				obs.append(obstaculo())
			if obs[0].y >720:
				del obs[0]
				pnt+=1
				TED.vel=1*int(pnt/10)
				print(TED.vel)
			tela.blit(pare, (obs[i].x , obs[i].y))
			if TED.pos==obs[i].pos and obs[i].y>720-164*2 and obs[i].y<720-134*2:
				print("perdeu")
				
			i+=1
			
			
		
		tecla = pygame.key.get_pressed()
		
		
			
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key==K_RIGHT:
					if TED.pos<2:
						TED.pos+=1
						TED.x=lin[TED.pos]-51
				print(TED.pos)
				if event.key==K_LEFT:
					if TED.pos>0:
						TED.pos-=1
						TED.x=lin[TED.pos]-51
						
						
			if event.type == QUIT:
					exit()
		tela.blit(ara, (TED.x , TED.y))
					
		pygame.display.update()
NewGame()
import pygame
import sys
from pygame.locals import *
import random

class personagem:
	def __init__(self, vel):
		self.x=987/2
		self.y=607/2-117/2
		self.velocidade=vel
class obstaculo:
	def __init__(self):
		self.x=987
		self.yc=random.randint(-580,-200)
		self.yb=self.yc+607+random.randint(120,190)
		self.vel=0.8
		self.point=False
		
		
def YouLose(placar):
	tela = pygame.display.set_mode((987, 607), 0, 32)
	pygame.display.set_caption('Franha')
	tecla = pygame.key.get_pressed()
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
					exit()
		tecla = pygame.key.get_pressed()
		if tecla[K_n]:
			NewGame()
		else:
			fundo = pygame.image.load("PERDEU.jpg").convert()
			tela.blit(fundo,(0,0))
			perdeu = fonte.render("'N' para novo jogo  Pontuacao:{}".format(placar), 1, (255,255,0))
			tela.blit(perdeu,(250,100))
			pygame.display.update()
			
	return None
		
	
#sys.path.append('./data')
pygame.font.init()
fonte = pygame.font.SysFont("monospace", 15)

tela = pygame.display.set_mode((987, 607), 0, 32)
pygame.display.set_caption('Franha')
fundo = pygame.image.load("fundo.jpg").convert()
ara = pygame.image.load("a.png").convert_alpha()
pare = pygame.image.load("pareda.jpg").convert()
tecla = pygame.key.get_pressed()
def NewGame():
	cabron = personagem(0.6)
	mexe=0.2

	pareda=[]
	pareda.append(obstaculo())

	placar=0


	i=0
	while True:
		tela.blit(fundo, (mexe, 0))
		mexe-=0.1
		if mexe<=-1934/2:
		
			mexe=0

		while i < len(pareda):
			pareda[i].x-=pareda[i].vel	
			tela.blit(pare, (pareda[i].x , pareda[i].yc))
			tela.blit(pare, (pareda[i].x , pareda[i].yb))
			if cabron.x+100> pareda[i].x and cabron.x< pareda[i].x+100:
				if cabron.y+50<pareda[i].yb and cabron.y>pareda[i].yc+607:
					if False==pareda[i].point:
						placar+=1
						pareda[i].point=True
					#print(placar)
				else:
					YouLose(placar)
				
			if pareda[i].x<-97:
				del pareda[i]
			if pareda[-1].x<(607-97):
				pareda.append(obstaculo())
			i+=1
					

		if i == len(pareda):
			i=0
			
		
		
		
		tela.blit(ara, (cabron.x,cabron.y))
		
		
		
		tecla = pygame.key.get_pressed()
		if tecla[K_SPACE] and (cabron.y+117)>200:
			cabron.y-=cabron.velocidade
		elif (cabron.y+50)<607:
			cabron.y+=cabron.velocidade
			
			
		for event in pygame.event.get():
			if event.type == QUIT:
					exit()
		placarpr = fonte.render(str(placar), 1, (255,255,0))
		tela.blit(placarpr, (100, 100))
					
		pygame.display.update()
NewGame()
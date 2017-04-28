import pygame
import sys
from pygame.locals import *
import random
rola=0
tamx=987
tamy=607

class Player:
	def __init__(self):
		self.x=0
		self.y=tamy/2-59/2
		self.vel=1
		
class Projetil:
	def __init__(self,x,y):
		self.x=x
		self.y=y
		self.vel=2
		
	
	
	
def YouLose(placar):
	tela = pygame.display.set_mode((tamx, tamy), 0, 32)
	pygame.display.set_caption('Franha')
	
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
pygame.display.set_caption('PewPew')
fundo = pygame.image.load("fundo.jpg").convert()
player = pygame.image.load("player1.png").convert_alpha()
#obstaculo = pygame.image.load("pareda.jpg").convert_alpha()
tecla = pygame.key.get_pressed()
players=[]
projeteis=[]
def NewGame():
	players.append(Player())
	rola,x=0,0
	while True:
		press=pygame.key.get_pressed()
		
		tela.blit(fundo, (rola, 0))
		tela.blit(player, (players[0].x, players[0].y))
		while x<len(projeteis):
			tela.blit(player, (projeteis[x].x, projeteis[x].y))
			x+=1
		x=0
		rola-=0.1
		if rola<=-1934/2:
			rola=0
		
		
		
		
		if press[K_UP] and players[0].y>0:
			players[0].y-=players[0].vel
		if press[K_DOWN] and players[0].y<tamy-59:
			players[0].y+=players[0].vel
		if press[K_LEFT] and players[0].x>0:
			players[0].x-=players[0].vel
		if press[K_RIGHT] and players[0].x<tamx-100:
			players[0].x+=players[0].vel
			
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					projeteis.append(Projetil(players[0].x, players[0].y))
					print(1)
			if event.type == QUIT:
					exit()
					
		pygame.display.update()
NewGame()
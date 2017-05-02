import pygame
import sys
from pygame.locals import *
import random
rola=0

tamx=987
tamy=607

tamplx=100
tamply=59

tampox=100
tampoy=59
placar= 0
dific=10 # mais proximo de 0 mais dificil

class Player:
	def __init__(self):
		self.x=0
		self.y=tamy/2-tamply/2
		self.projeteis=[]
		self.projeteismax=2
		self.vel=1
		self.vida=10
class Projetil:
	def __init__(self,x,y):
		self.x=x
		self.y=y
		self.vel=2
		
class Obstaculo:
	def __init__(self):
		self.x=tamx
		self.y=random.randint(0, tamy-tamply)
		self.vel=0.6
		self.vida=random.randint(0, 2+(placar/dific))
		
	
	
	
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
pygame.mixer.init(frequency = 44100, size = -16, channels = 2, buffer = 2**12) 
fonte = pygame.font.SysFont("monospace", 15)
tela = pygame.display.set_mode((987, 607), 0, 32)
pygame.display.set_caption('PewPew')
musica=pygame.mixer.Sound(file="The_moon.ogg")
laser=("laser.ogg")
fundo = pygame.image.load("fundo.jpg").convert()
tecla = pygame.key.get_pressed()
players=[]
objetos=[Obstaculo()]
pygame.mixer.Channel(0).play(musica, -1)
obstaculo = pygame.image.load("player1.png").convert_alpha()
player = pygame.image.load("player1.png").convert_alpha()


def NewGame():
	placar=0
	players.append(Player())
	rola,x=0,0
	tamx,tamy=987,607

	tamplx=100
	tamply=59
	
	tampox=100
	tampoy=59
	while True:
		
		press=pygame.key.get_pressed()
		
		tela.blit(fundo, (rola, 0))
		while x<len(players[0].projeteis) and len(players[0].projeteis)<=players[0].projeteismax:
			players[0].projeteis[x].x+=players[0].projeteis[x].vel
			tela.blit(player, (players[0].projeteis[x].x, players[0].projeteis[x].y))
			if players[0].projeteis[x].x>tamx:
				del players[0].projeteis[x]
			x+=1
				
		x=0
		if len(objetos)==0:
			objetos.append(Obstaculo())
		while x<len(objetos):
			objetos[x].x-=objetos[x].vel
			tela.blit(obstaculo, (objetos[x].x, objetos[x].y))
			if objetos[-1].x<tamx-tamx/4+(placar/dific):
				objetos.append(Obstaculo())
			if objetos[x].x<0-tampoy:
				del objetos[x]
				players[0].vida-=1
			if objetos[x].y-tamply<players[0].y and objetos[x].y+tamply>players[0].y and objetos[x].x+tamplx>players[0].x and objetos[x].x-tamplx<players[0].x:
				del objetos[x]
				players[0].vida-=1
				print("voce bateu, vida {}".format(players[0].vida))
			y=0
			
			
			
			while y<len(players[0].projeteis):
				if objetos[x].y-tampoy<players[0].projeteis[y].y and objetos[x].y+tampoy>players[0].projeteis[y].y and objetos[x].x+tampox>players[0].projeteis[y].x and objetos[x].x-tampox<players[0].projeteis[y].x:
					objetos[x].vida-=1
					if objetos[x].vida<0:
						del objetos[x]
						placar+=1
					del players[0].projeteis[y]
					print("voce acertou, vida {}".format("-1"))
					print("objstos {}".format(len(objetos)))
				y+=1
			x+=1
			
		x=0

			
		tela.blit(player, (players[0].x, players[0].y))
		perdeu = fonte.render("pontuacao{}, vida{}".format(placar,players[0].vida), 1, (255,255,0))
		tela.blit(perdeu,(250,100))
		
		
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
					if len(players[0].projeteis)<players[0].projeteismax:
						pygame.mixer.music.pause()
						pygame.mixer.music.load(laser)
						pygame.mixer.music.play(0)
						players[0].projeteis.append(Projetil(players[0].x, players[0].y))
					print("projeteis: {}".format(len(players[0].projeteis)))
			if event.type == QUIT:
					exit()
					
		pygame.display.update()
NewGame()
import pygame
import sys
from pygame.locals import *
import random
rola=0
tamTEx=987
tamTEy=607

tamplx=53
tamply=43

placar= 0
dific=10 # mais proximo de 0 mais dificil

class Player:
	def __init__(self):
		self.x=0
		self.y=tamTEy/2-tamply/2
		self.projeteis=[]
		self.projeteismax=2
		self.vel=1
		self.vida=10
class Projetil:
	def __init__(self,x,y,tamx=20,tamy=10):
		self.x=x
		self.y=y
		self.vel=2
		self.proj = pygame.image.load("tiro.png").convert_alpha()
		self.tamx=tamx
		self.tamy=tamy
		
class Obstaculo:
	def __init__(self,tamx=100,tamy=59):
		self.x=tamTEx
		self.y=random.randint(0, tamTEy-tamy)
		self.vel=0.6
		self.vida=random.randint(0, 2+(placar/dific))
		self.tamy=tamy
		self.tamx=tamx
		self.atingido=0
		self.item=random.randint(1, 121)
		self.tamx=20
		self.tamy=10
		if self.item<115:
			self.tamx=100
			self.tamy=59
			self.item=0
		
	
	
	
def YouLose(placar):
	tela = pygame.display.set_mode((tamTEx, tamTEy), 0, 32)
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
acerto=("acerto.ogg")
fundo = pygame.image.load("fundo.jpg").convert()
tecla = pygame.key.get_pressed()
players=[]
objetos=[Obstaculo()]
pygame.mixer.Channel(0).play(musica, -1)
obstaculo = pygame.image.load("player1.png").convert_alpha()
obstaculo1 = pygame.image.load("mais.png").convert_alpha()
player = pygame.image.load("nave.png").convert_alpha()


def NewGame():
	debgg=0
	player = pygame.image.load("nave.png").convert_alpha()
	cima,baixo,esquerda,direita,b,a=0,0,0,0,0,0
	placar=0
	players.append(Player())
	rola,x=0,0
	tamTEx,tamTEy=987,607

	tamplx=53
	tamply=43
	
	while True:
		
		press=pygame.key.get_pressed()
		
		tela.blit(fundo, (rola, 0))
		while x<len(players[0].projeteis) and len(players[0].projeteis)<=players[0].projeteismax:
			players[0].projeteis[x].x+=players[0].projeteis[x].vel
			tela.blit(players[0].projeteis[x].proj, (players[0].projeteis[x].x, players[0].projeteis[x].y))
			if players[0].projeteis[x].x>tamTEx:
				del players[0].projeteis[x]
			x+=1
				
		x=0
		if len(objetos)==0:
			objetos.append(Obstaculo())
		while x<len(objetos):
			objetos[x].x-=objetos[x].vel
			if objetos[x].atingido<0:
				if objetos[x].item==0:
					tela.blit(obstaculo, (objetos[x].x, objetos[x].y))
				elif objetos[x].item>0:
					tela.blit(obstaculo1, (objetos[x].x, objetos[x].y))
			objetos[x].atingido-=1
			if objetos[-1].x<tamTEx-tamTEx/4+(placar/dific):
				objetos.append(Obstaculo())
			if objetos[x].x<0-objetos[x].tamy:
				del objetos[x]
				players[0].vida-=1
			if objetos[x].y-tamply<players[0].y\
			and objetos[x].y+objetos[x].tamy>players[0].y\
			and objetos[x].x+objetos[x].tamx>players[0].x\
			and objetos[x].x-tamplx<players[0].x:
				if debgg==1: print(objetos[x].tamy, objetos[x].tamx)
				if objetos[x].item>0:
					del objetos[x]
					players[0].projeteismax+=1
					if debgg==1: print("voce bateu, projeteis maximos aumentados em 1 e vida {}".format(players[0].vida))
				else:
					del objetos[x]
					players[0].vida-=1
					pygame.mixer.music.load(acerto)
					pygame.mixer.music.play(0)
					if debgg==1: print("voce bateu, vida {}".format(players[0].vida))
			y=0
			
			while y<len(players[0].projeteis):
				if len(objetos)>0 and objetos[x].y-players[0].projeteis[y].tamy<players[0].projeteis[y].y and objetos[x].y+objetos[x].tamy>players[0].projeteis[y].y and objetos[x].x+objetos[x].tamx>players[0].projeteis[y].x and objetos[x].x-players[0].projeteis[y].tamx<players[0].projeteis[y].x:
					objetos[x].vida-=1
					objetos[x].atingido=10 #tempo apagado
					if objetos[x].vida<0:
						del objetos[x]
						x-=1
						#pygame.mixer.music.pause()
						pygame.mixer.music.load(acerto)
						pygame.mixer.music.play(0)
						placar+=1
					del players[0].projeteis[y]
					if debgg==1: print("voce acertou, vida {}".format("-1"))
					if debgg==1: print("objstos {}".format(len(objetos)))
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
		if press[K_DOWN] and players[0].y<tamTEy-59:
			players[0].y+=players[0].vel
		if press[K_LEFT] and players[0].x>0:
			players[0].x-=players[0].vel
		if press[K_RIGHT] and players[0].x<tamTEx-100:
			players[0].x+=players[0].vel
			
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					if len(players[0].projeteis)<players[0].projeteismax:
						#pygame.mixer.music.pause()
						pygame.mixer.music.load(laser)
						pygame.mixer.music.play(0)
						players[0].projeteis.append(Projetil(players[0].x, players[0].y+tamply/2))					
						if debgg==1: print("projeteis: {}".format(len(players[0].projeteis)),players[0].projeteis[y].tamy,players[0].projeteis[y].tamx)
				if event.key == pygame.K_UP and b==0:
					cima+=1
					if debgg==1: print("cima")
				if event.key == pygame.K_DOWN and cima==2:
					baixo+=1
					if debgg==1: print("baixo")
				if event.key == pygame.K_LEFT and baixo==2:
					esquerda+=1
					if debgg==1: print("e")
				if event.key == pygame.K_RIGHT and esquerda==1:
					direita+=1
					if debgg==1: print("d")
				if event.key == pygame.K_LEFT and direita==1 and esquerda==1:
					esquerda+=1
					if debgg==1: print("e")
				if event.key == pygame.K_RIGHT and esquerda==2 :
					direita+=1
					if debgg==1: print("d")
				if event.key == pygame.K_b and direita==2:
					b+=1
					if debgg==1: print("b")
				if event.key == pygame.K_a and b==1:
					if debgg==1: print("+100")
					player = pygame.image.load("medfrighter.png").convert_alpha()
					player=pygame.transform.rotate(player,90*3)
					players[0].projeteismax+=100
					debgg=1
				if event.key == pygame.K_TAB:
					cima,baixo,esquerda,direita,b,a=0,0,0,0,0,0
					if debgg==1: print("TAB")
				if cima>2 or a==1:
					if event.key == pygame.K_a or event.key == pygame.K_b or event.key == pygame.K_UP or event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT or event.key == pygame.K_DOWN:
						cima,baixo,esquerda,direita,b,a=0,0,0,0,0,0
						if debgg==1: print("TAB")
			if event.type == QUIT:
					exit()
					
		pygame.display.update()
NewGame()
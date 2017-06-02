import pygame
import sys
from pygame.locals import *
import random
from firebase import firebase
import time


imagens={"tiro":["tiro_inimigo.png","tiro_limao.png","missil1.png","esp_dilma.png","seguidor.png"],"skin":["","glados.png","dilma_boss"],"tamanhop":[[1,1],[75,108],[75,108]],"tamanhot":[[1,1],[40,20],[40,20]],"tamanhott":[[1,1],[60,100]],"inimigo normal":["inimigo1.png","inimigo2.png"]}
rola=0
tamTEx=987
tamTEy=607

tamplx=60
tamply=25

placar= 0
dific=10 # mais proximo de 0 mais dificil

firebase = firebase.FirebaseApplication('https://pf-chubby.firebaseio.com/', None)
def leaderboard():
	result = firebase.get('/leaderboard', None)
	return result
class Player:
	def __init__(self):
		self.x=0
		self.y=tamTEy/2-tamply/2
		self.projeteis=[]
		self.projeteismax=2
		self.vel=1
		self.vida=10
class Projetil:
	def __init__(self,x,y,tamx=40,tamy=20):
		self.x=x
		self.y=y
		self.vel=2
		self.proj = pygame.image.load("missil1.png").convert_alpha()
		self.tamx=tamx
		self.tamy=tamy
		
class Obstaculo:
	def __init__(self,ai=0,x=0,y=0,theme=0,off=1,tamx=100,tamy=59):
		self.theme=theme
		self.img = pygame.image.load("404.png").convert_alpha() #imagem padrao #erro
		self.x=tamTEx
		self.y=random.randint(0, tamTEy-tamy)
		self.vel=0.6
		self.vida=random.randint(1, 2+(placar/dific))
		self.tamy=tamy
		self.tamx=tamx
		self.atingido=0
		self.item=random.randint(0, 100) #item aleatorio
		self.tamx=20
		self.tamy=10
		self.dano=0
		self.ai=ai
		self.offscreen=off
		self.alive=0
		self.ataque=0
		self.tiros=0

		if ai==1:
			 #boss
			self.vida=random.randint(7, 20+(placar/dific))
			print(imagens["tamanhop"][theme])
			self.tamy=imagens["tamanhop"][theme+1][0]
			self.tamx=imagens["tamanhop"][theme+1][1]
			self.x=tamTEx-self.tamx
			self.dano=100
			self.vel=0.5
			self.y=random.randint(0, tamTEy-tamy)
			self.vai=0
			self.ataque=0
			self.tiros=0
			self.theme=random.randint(1,1)
			self.img = pygame.image.load(imagens["skin"][self.theme]).convert_alpha()
			pygame.mixer.Channel(0).play(pygame.mixer.Sound(file=musicas[self.theme]), -1)
			self.aipass=0
			
			
		elif ai==2:
			self.img = pygame.image.load(imagens["tiro"][self.theme]).convert_alpha() #tiro do boss
			self.tamy=imagens["tamanhott"][theme][0]
			self.tamx=imagens["tamanhott"][theme][1]
			self.x=x
			self.dano=2
			self.vel=2 + self.theme
			self.y=y
			self.vai=0
			self.offscreen=0

		elif ai==3:
			self.img = pygame.image.load(imagens["tiro"][self.theme+1]).convert_alpha() #tiro do boss com mira
			self.tamy=imagens["tamanhot"][theme][0]
			self.tamx=imagens["tamanhot"][theme][1]
			self.x=x
			self.dano=2
			self.vel=3
			self.y=y
			self.vai=0
			self.offscreen=0
			

		elif self.item<80:
			self.img = pygame.image.load(imagens["inimigo normal"][self.vida%2]).convert_alpha() #inimigo comum
			self.tamx=60
			self.tamy=60
			self.item=0
			self.dano=1
			
		elif self.item>=80 and self.item<85:
			self.tamx=40
			self.tamy=20
			self.offscreen=0
			self.item=1
			self.dano=0
			self.img = pygame.image.load("missil_mais.png").convert_alpha() #missel mais

		elif self.item>=85 and self.item<90:
			self.offscreen=0
			self.tamx=40
			self.tamy=20
			self.item=4
			self.dano=0
			self.img = pygame.image.load("missil_menos.png").convert_alpha() #inimigo comum
			
		elif self.item>=90 and self.item<95:
			print ("item2")
			self.tamx=40
			self.tamy=20
			self.item=2
			self.dano=0
			self.offscreen=0
			self.img = pygame.image.load("mais_vel.png").convert_alpha() #item fast

		elif self.item>=95 and self.item<100:
			print ("item2")
			self.tamx=40
			self.tamy=20
			self.item=3
			self.dano=0
			self.offscreen=0
			self.img = pygame.image.load("vel_menos.png").convert_alpha() #item fast
			
	
	
	
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



def NewGame():
	pygame.font.init()
	pygame.mixer.init(frequency = 44100, size = -16, channels = 3, buffer = 2**12) 
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
	player = pygame.image.load("a-29.png").convert_alpha()
	clock = pygame.time.Clock()
	debgg=0
	player = pygame.image.load("a-29.png").convert_alpha()
	cima,baixo,esquerda,direita,b,a=0,0,0,0,0,0
	placar=0
	players.append(Player())
	rola,x=0,0
	tamTEx,tamTEy=987,607
	
	chefe=0

	tamplx=60
	tamply=25
	fundos=[pygame.image.load("cave3.jpg").convert(),pygame.image.load("cave3.jpg").convert(),]
	musicas=["","portal.ogg",]
	while True:
		press=pygame.key.get_pressed()


		if placar%20==0 and placar!=0:
			objetos.append(Obstaculo(1))
		
		if chefe==0: 
			tela.blit(fundo, (rola, 0))
		else:
			tela.blit(fundos[chefe], (0, 0))
		while x<len(players[0].projeteis) and len(players[0].projeteis)<=players[0].projeteismax:
			players[0].projeteis[x].x+=players[0].projeteis[x].vel
			tela.blit(players[0].projeteis[x].proj, (players[0].projeteis[x].x, players[0].projeteis[x].y))
			if players[0].projeteis[x].x>tamTEx:
				del players[0].projeteis[x]
			x+=1
				
		x=0
		if len(objetos)==0 and chefe==0:
			objetos.append(Obstaculo())
		while x<len(objetos):
			if objetos[x].ai==0 or objetos[x].ai==2:
				objetos[x].x-=objetos[x].vel

			elif objetos[x].ai==3: #tiro que segue 
				if debgg==1: print("Tiro que segue")
				#if players[0].x+tamplx*1.01<objetos[x].x:
				objetos[x].x-=objetos[x].vel
				#elif players[0].x+tamplx*1.01>objetos[x].x:
				#	objetos[x].x+=objetos[x].vel
				if players[0].y+random.random()*300<objetos[x].y:
					objetos[x].y-=objetos[x].vel*1.5
				elif players[0].y-random.random()*300>objetos[x].y:
					objetos[x].y+=objetos[x].vel*1.5


			elif objetos[x].ai==1:
				if random.randint(1,1000)<2:
						objetos[x].vai=objetos[x].vai*-1
				chefe=objetos[x].theme
				if debgg==1: print("chefe")
				if debgg==1: print("x=",objetos[x].x,"y=",objetos[x].y,"ataque",objetos[x].ataque,objetos[x].tiros)
				

				if objetos[x].y<=tamTEy-objetos[x].tamy and objetos[x].vai==-1:
					objetos[x].y+=objetos[x].vel
					if objetos[x].y>tamTEy-objetos[x].tamy:
						objetos[x].vai=1
				
				elif objetos[x].y>=0:
					objetos[x].y-=objetos[x].vel
					if objetos[x].y<0:
						objetos[x].vai=-1
				if objetos[x].y+50>players[0].y and objetos[x].y-50<players[0].y:
					if random.randint(1,700)<2 and objetos[x].aipass==0:
						objetos[x].aipass=1
						objetos[x].vai=objetos[x].vai*-1
				else:
					objetos[x].aipass=0
				


				if objetos[x].y==players[0].y or objetos[x].alive%random.randint(30,100)==0: #o 20 random.randint(10,300+(placar/dific))
					objetos.append(Obstaculo(2,objetos[x].x,objetos[x].y)) #tiro normal boss
					objetos[x].alive=0

				if objetos[x].ataque%1000==1:
					if debgg==1: print("tri legal")
					#time.sleep(1)
					objetos.append(Obstaculo(3,objetos[x].x,objetos[x].y,objetos[x].theme))

				if objetos[x].ataque>objetos[x].theme*1300:
					objetos[x].ataque=0 #random.randint(1,3000+3*(placar/dific))
					objetos[x].tiros=100 #random.randint(1,200+3*(placar/dific))
					objetos[x].ataque+=1
				else:
					objetos[x].ataque+=1
					
				if objetos[x].tiros>0:
					if objetos[x].tiros%15==0: #random.randint(10,20+3*(placar/dific))
						objetos.append(Obstaculo(2,objetos[x].x,objetos[x].y,objetos[x].theme))
					
					objetos[x].tiros-=1
				objetos[x].alive+=1

			if objetos[x].atingido<0:
				if objetos[x].item==0:
					tela.blit(objetos[x].img, (objetos[x].x, objetos[x].y))
				elif objetos[x].item>0:
					tela.blit(objetos[x].img, (objetos[x].x, objetos[x].y))
			objetos[x].atingido-=1
			if objetos[-1].x<tamTEx-tamTEx/4+(placar/dific) and chefe==0 :
				objetos.append(Obstaculo())
			if objetos[x].x<0-objetos[x].tamy:
				
				if objetos[x].offscreen!=0:
					players[0].vida-=objetos[x].dano
				del objetos[x]
				break
				
			if objetos[x].y-tamply<players[0].y\
			and objetos[x].y+objetos[x].tamy>players[0].y\
			and objetos[x].x+objetos[x].tamx>players[0].x\
			and objetos[x].x-tamplx<players[0].x:
				if debgg==1: print(objetos[x].tamy, objetos[x].tamx)




				if objetos[x].item==1: #utilidade dos itens
					del objetos[x]
					players[0].projeteismax+=1
					if debgg==1: print("voce bateu, projeteis maximos aumentados em 1 e vida {}".format(players[0].vida))
				

				elif objetos[x].item==2:
					del objetos[x]
					players[0].vel+=0.25
					if debgg==1: print("voce bateu, velocidade aumentada em 0.25x e vida {}".format(players[0].vida))

				elif objetos[x].item==3:
					del objetos[x]
					players[0].vel-=0.25
					if debgg==1: print("voce bateu, velocidade aumentada em 0.25x e vida {}".format(players[0].vida))

				elif objetos[x].item==4:
					del objetos[x]
					players[0].projeteismax-=1	
					if debgg==1: print("voce bateu, velocidade aumentada em 0.25x e vida {}".format(players[0].vida))


				else:
					players[0].vida-=objetos[x].dano
					del objetos[x]
					pygame.mixer.music.load(acerto)
					pygame.mixer.music.play(0)
					if debgg==1: print("voce bateu, vida {}".format(players[0].vida))
			y=0
			while y<len(players[0].projeteis):
				if len(objetos)>0 and objetos[x].y-players[0].projeteis[y].tamy<players[0].projeteis[y].y and objetos[x].y+objetos[x].tamy>players[0].projeteis[y].y and objetos[x].x+objetos[x].tamx>players[0].projeteis[y].x and objetos[x].x-players[0].projeteis[y].tamx<players[0].projeteis[y].x:
					objetos[x].vida-=1
					objetos[x].atingido=10 #tempo apagado
					if objetos[x].vida<0:
						if objetos[x].ai==1:
							chefe=0
							pygame.mixer.Channel(0).play(musica, -1)
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
		if debgg==0: 
			perdeu = fonte.render("pontuacao{}, vida{}".format(placar,players[0].vida, font="ARIEL"), 1, (255,255,0))
		else:
			perdeu = fonte.render("B = BOSS SPAWN BACKSP=OBJ SPAWN pontuacao{}, vida{}".format(placar,players[0].vida), 1, (255,255,0))
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
			if event.type == QUIT:
				pygame.quit()
				pygame.exit()
				exit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					if len(players[0].projeteis)<players[0].projeteismax:
						#pygame.mixer.music.pause()
						pygame.mixer.music.load(laser)
						pygame.mixer.music.play(0)
						players[0].projeteis.append(Projetil(players[0].x, players[0].y+tamply/2))					
						if debgg==1: print("projeteis: {}".format(len(players[0].projeteis)),players[0].projeteis[y].tamy,players[0].projeteis[y].tamx, tamply/2)
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
					#player = pygame.image.load("medfrighter.png").convert_alpha()
					player=pygame.transform.rotate(player,90*2)
					players[0].projeteismax+=100
					players[0].vida+=100
					debgg=1
				if event.key == pygame.K_TAB:
					cima,baixo,esquerda,direita,b,a=0,0,0,0,0,0
					if debgg==1: print("TAB")
				if event.key == pygame.K_b and debgg==1:	
					objetos.append(Obstaculo(1))
				if event.key == pygame.K_BACKSPACE and debgg==1:	
					objetos.append(Obstaculo())
					if debgg==1: print("PLUSSS")
				if event.key == pygame.K_l and debgg==1:	
					leaderboard()
					firebase.post('/leaderboard',{"Orange":666})
					if debgg==1: print("leade")

				if cima>2 or a==1:
					if event.key == pygame.K_a or event.key == pygame.K_b or event.key == pygame.K_UP or event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT or event.key == pygame.K_DOWN:
						cima,baixo,esquerda,direita,b,a=0,0,0,0,0,0
						if debgg==1: print("TAB")
		#if Player[0].vida<=0:
		#	break
		#	YouLose()	
		pygame.display.update()
		clock.tick(200)
NewGame()
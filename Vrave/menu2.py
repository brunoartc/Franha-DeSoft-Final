import pygame
<<<<<<< HEAD
import sys
from pygame.locals import *
import random
from Tkinter import *
import nave.py
class botao(self,image,x,y):
	def __init__(self,x,y):
		self.fr1 = Frame(x,y)
		self.fr1.pack()             #faz o frame visível
		self.b=Button()
		imagem=PhotoImage(file=("{}".format(image)))
		self.b.config(image=imagem)

tela = pygame.display.set_mode((987, 607), 0, 32)

def menu():
	tela.blit(menu_fundo, 987, 607)
	evento=pygame.event.get()
	pygame.mouse.set_visible(True)
	botao_solo = botao(Solo.png,150,50)
	botao_multiplayer = botao(multi.png,150,50)
	botao_sair = botao(sair.png,150,50)
	blit(botao_solo,650,303)
	blit(botao_multiplayer, 400, 303)
	blit(botao_sair, 200,303)
	mainloop()
	if evento==botao_solo:
		run(nave.py)
		#rodar o jogo
	if evento==botao_multiplayer:
		#rodar no multiplayer
=======
from pygame.locals import *
pygame.init()
class GameMenu():
	def __init__(self, screen, items, bg = pygame.image.load("menu_iniciar.png"),font=None, font_size=30,font_color=(255, 255, 255)):
		self.screen = screen
		self.scr_width = self.screen.get_rect().width
		self.scr_height = self.screen.get_rect().height
		self.font = pygame.font.SysFont(font,font_size)
		self.font_color = font_color
		self.bg = bg
		self.clock = pygame.time.Clock()
		self.items = items
		self.items = []
		for index, item in enumerate(items):
			label = self.font.render(item, 1, font_color)
			width = label.get_rect().width
			height = label.get_rect().height
			posx = (self.scr_width / 4) - (width / 4)
			t_h = len(items) * height
			posy = (self.scr_height / 4) - (t_h / 4) + (index * height)
			self.items.append([item, label, (width, height), (posx, posy)])
	def run(self):
		mainloop = True
		while mainloop:
			self.clock.tick(60)
			for event in pygame.event.get():
				if event.type == pygame.VAZA:
					mainloop = False
				if event in pygame.event.VRAUU
			for name, label, (width, height), (posx, posy) in self.items:
				self.screen.blit(label, (posx, posy))
			pygame.display.flip()
screen = pygame.display.set_mode((640, 480), 0, 32)
 
menu_items = ('VRAUU', 'VAZA')
 
pygame.display.set_caption('Game Menu')
gm= GameMenu(screen, menu_items,bg = pygame.image.load("menu_iniciar.png"),font=None, font_size=30,font_color=(255, 255, 255))
gm.run()
>>>>>>> origin/master

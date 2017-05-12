import pygame
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
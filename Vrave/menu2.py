import pygame
from sys import *
import os
from pygame.locals import *
import random
from tkinter import *
from PIL import *
from nave import *

class introducao():
	def __init__(self):
		self.jan = Tk()
		self.jan.title("Introdução")
		self.jan.geometry('')
		self.intro_foto=PhotoImage(file="intro.png")
		self.intro = Label(self.jan,image=self.intro_foto).grid(columnspan=100, rowspan=100)
		self.cont = Button(self.jan,anchor=S,text="Continuar",font="ARIEL",command=lambda:self.inicio()).grid(column=75,row=95)

	def inicia(self):
		self.jan.mainloop()
			
	def inicio(self):
		self.jan.destroy()
		NewGame()

class Menu():
	def __init__(self):
		self.menu = Tk()
		self.menu.title('IodP')
		self.titulo=PhotoImage(file="titulo.png")

		self.menu_jan = Label(self.menu,image=self.titulo, height = 607,width = 987).grid(columnspan=3, rowspan=20)

		self.solo = PhotoImage(file="Solo.png")
		self.botao_solo = Button(self.menu_jan,image=self.solo,command=lambda:self.pos()).grid(column=0,row=5,padx=10,pady=150)

		self.LB = PhotoImage(file="lb.png")
		self.botao_lb = Button(self.menu_jan,image=self.LB,command=lambda:leaderboard()).grid(column=0,row=6)

		self.sair = PhotoImage(file="sair.png")
		self.botao_Sair = Button(self.menu_jan,image=self.sair,command=lambda:self.terminar_logo()).grid(column=2,row=5)

	def comeca(self):
		self.menu.mainloop()

	def terminar_logo(self):
		self.menu.destroy()
	def introducao(self):
		introducao()
	def pos(self):
		self.terminar_logo()
		cachorro=introducao()
		cachorro.inicia()

jogo=Menu()
jogo.comeca()
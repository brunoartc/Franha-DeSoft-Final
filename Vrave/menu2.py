import pygame
from sys import *
import os
from pygame.locals import *
import random
from tkinter import *
from intro import *
from PIL import *
from nave2 import *




#foto = open("menu_fundo.jpg")
#imagem = PhotoImage(foto)
def pos():
	introducao()
def qq():
	exit(0)

def Menu():
	#solo = PhotoImage(file="Solo.png")
	#sair = PhotoImage(file="sair.png")
	#LB = PhotoImage(file="lb.png")
	menu = Tk()
	menu.title('Chubby')
	menu.geometry('987x607')
	menu_jan = Label(menu,text="Chubby Bunnies").pack()

	botao_solo = Button(menu,text='solo',command=lambda:pos()).pack()

	botao_lb = Button(menu,text='LB',command=lambda:leaderboard()).pack()

	botao_Sair = Button(menu,text='sair',command=lambda:qq()).pack()	

	menu.mainloop()
Menu()
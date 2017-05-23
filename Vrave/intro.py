import pygame
import sys
import os
from pygame.locals import *
import random
from tkinter import *
from sys import exit
from nave2 import *



def inicio():
	NewGame()

def introducao():
	jan = Tk()
	jan.title("Introdução")
	jan.geometry('987x607')
	intro = Label(jan,text="Uma onda de corrupção, incerteza vem \n\
			separando nosso pais, você foi o único que conseguiu \n\
			se abster te tantas brigas fúteis e se concentrar nos\n\
			rais problemas da sociedade. Você então deve         \n\
			se concentrar em batalhar através dos lugares        \n\
			derrotando os maiores causadores de tanta desgraça,  \n\
			os políticos. Mas agentes da violência e ingorância  \n\
			irão te atrapalhar\
			TENHA CUIDADO	", font="ARIEL").pack()
	cont = Button(jan,anchor=S,text="Continuar",font="ARIEL",command=lambda:inicio()).pack()
	jan.mainloop()
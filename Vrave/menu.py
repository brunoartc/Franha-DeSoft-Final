import pygame
from pygame.locals import *
pygame.init()
class GameMenu():
    def __init__(self, screen, items, bg = pygame.image.load("MenuInicial.png")):
        self.screen = screen
        self.scr_width = self.screen.get_rect(11657).width
        self.scr_height = self.screen.get_rect(7169).height
 
        self.bg = bg
        self.clock = pygame.time.Clock()
 
        self.items = items
        self.items = []
        for index, item in enumerate(items):
            label = self.font.render(item, 1, font_color)
 
            width = label.get_rect().width
            height = label.get_rect().height
 
            posx = (self.scr_width / 2) - (width / 2)
            t_h = len(items) * height
            posy = (self.scr_height / 2) - (t_h / 2) + (index * height)
 
            self.items.append([item, label, (width, height), (posx, posy)])
 
    def run(self):
        mainloop = True
        while mainloop:
            self.clock.tick(60)
 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainloop = False
            self.screen.fill(self.bg)
            for name, label, (width, height), (posx, posy) in self.items:
                self.screen.blit(label, (posx, posy))
            pygame.display.flip()
screen = pygame.display.set_mode((640, 480), 0, 32)
 
menu_items = ('VRAUU', 'VAZA')
 
pygame.display.set_caption('Game Menu')
gm= GameMenu(screen, menu_items)
gm.run()
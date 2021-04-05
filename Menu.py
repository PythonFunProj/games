##PythonFun##

#To do: fix the background

import pygame
import random
from sys import exit
import os

abspath = os.path.abspath(__file__) #sets the location of the Meny.py as the working directory
dname = os.path.dirname(abspath)
os.chdir(dname)

pygame.init()

screen = pygame.display.set_mode((500,750)) #window
pygame.display.set_caption('PythonFun.exe')

mainclock = pygame.time.Clock()
font = pygame.font.SysFont(None,20)
run = True
background = pygame.image.load('backgroundmainmenu.png')


def draw_text(text, font, color, surface, x, y): #drawtext function
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj, textrect)

def main_menu(): #mainmenu function
    pygame.event.get()
    while run:
        screen.fill((0,0,0))
        screen.blit(background,[0,0])
        draw_text('-Main Menu-', font, (255,0,0), screen, 210,20)
        pygame.display.update()
        mainclock.tick(20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                    

main_menu()
pygame.quit()

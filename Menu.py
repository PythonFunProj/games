##PythonFun##

#To do: turn the button creation into a function for more efficiency
#       find a way to prevent the button from working when we are already clicking then gliding on the button

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
green = (0,200,0)
bright_green = (0,255,0)
red = (200,0,0)
bright_red = (255,0,0)


def draw_text(text, font, color, surface, x, y): #drawtext function
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj, textrect)

def main_menu(): #mainmenu function
    pygame.event.get()
    while run:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        action = click[0]
        screen.fill((0,0,0))
        screen.blit(background,[0,0])
        draw_text('-Main Menu-', font, (255,0,0), screen, 210,20)
        draw_text(str(mouse), font, (0,255,0),screen, 0, 0)
        
        if 250+50 > mouse[0] > 250-50 and 700 > mouse[1] > 700-25:
            pygame.draw.rect(screen, bright_red,(200,675,100,25))
            draw_text("QUIT", font, (50,50,50), screen, 235, 680)
            if click[0] == 1:
                pygame.quit()
                exit()

        else:
            pygame.draw.rect(screen, red,(200,675,100,25))
            draw_text("QUIT", font, (0,0,0), screen, 235, 680)
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        

        pygame.display.update()
        mainclock.tick(15)

main_menu()
pygame.quit()
##PythonFun##
#Menu program
#Author: Nicolas Traglia
#with the help of Loann Rio for some syntax error (how did I not see them)
#Last updated: 26/05/2021
#TODO: nothing yet for the mainmenu. maybe set the window size back to normal after closing some games -> look into return to mainmenu after closing game

import pygame
import random
from sys import exit
import os
from pygame import draw
import runpy
from pygame.locals import *
pltmain = "plateformermain.py"

abspath = os.path.abspath(__file__) #sets the location of the Menu.py as the working directory
dname = os.path.dirname(abspath)
os.chdir(dname)

pygame.init()

preview = pygame.image.load('previews/tin.png')
preview = pygame.transform.scale(preview,(250,250))
screen = pygame.display.set_mode((500,750)) #window
pygame.display.set_caption('PythonFun.exe')

mainclock = pygame.time.Clock()
font = pygame.font.SysFont(None,20)
run = True
secretbutton = False
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

def buttonmaker(posx, posy, buttonfunction, colorlight, colorreg, mouseinp, clickinp,text,img):
    global preview
    img1 = pygame.image.load(img).convert()
    img1 = pygame.transform.scale(img1,(250,250))
    if (int(posx) +50 > mouseinp[0] > int(posx) -50) and (int(posy) > mouseinp[1] > int(posy)-25):
        pygame.draw.rect(screen, colorlight, (int(posx)-50, int(posy)-25,100,25))
        preview = img1
        if  (clickinp[0]==1):
            runpy.run_path(path_name=buttonfunction)
    else:
        pygame.draw.rect(screen, colorreg, (int(posx)-50, int(posy)-25,100,25))
    draw_text(text, font, (0,0,0),screen,(posx-45),(posy-20))

def potato():
    print('potato')

def main_menu(): #mainmenu function
    pygame.event.get()
    
    while run:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        action = click[0]
        screen.fill((0,0,0))
        screen.blit(background,[0,0])
        buttonmaker(100, 100, 'plateformermain.py', (0,255,0), (0,200,0), mouse, click, 'PlateformerN','previews/plt.png')
        buttonmaker(100, 150, 'chess.py', (255,255,0), (200,200,0), mouse, click, 'Chess','previews/chess.png')
        buttonmaker(100, 200, 'tetris2.py', (255,0,0), (200,0,0), mouse, click, 'Tetris','previews/tetris.png')
        buttonmaker(100, 250, 'flappy_bird.py', (255,0,255), (200,0,200), mouse, click, 'Flappy Bird','previews/fb.png')
        buttonmaker(100, 300, 'demineur.py', (0,0,255), (0,0,200), mouse, click, 'Minesweeper','previews/ms.png')
        buttonmaker(100, 350, 'snake.py', (0,255,255), (0,200,200), mouse, click, 'Snake','previews/snake.png')
        buttonmaker(100, 400, 'planes.py', (255,255,255), (200,200,200), mouse, click, 'Planes','previews/planepromo.png')
        buttonmaker(100, 450, '2048.py', (200,200,200), (100,100,100), mouse, click, '2048','previews/2048.png')
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
            if event.type == KEYDOWN:
                if event.key == K_t:
                    global secretbutton
                    if secretbutton == True:
                        pass
                    else:
                        secretbutton == True  
                        buttonmaker(100, 500, 'parcour_client_2.1.py', (100,255,0), (75,200,000), mouse, click, 'PlateformerR','previews/plt.png')

        rectprev = preview.get_rect()
        rectprev.center = 325,200
        screen.blit(preview, rectprev)
        pygame.draw.rect(screen, (255,0,0), rectprev, 1)
        pygame.display.update()
        mainclock.tick(15)

main_menu()
pygame.quit()
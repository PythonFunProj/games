###plateformer###
#last updated: 23/04/2021
#To do: make levels + timer
import pygame
from pygame.locals import *
import os 
abspath = os.path.abspath(__file__) #sets the location of the .py file as the working directory
dname = os.path.dirname(abspath)
os.chdir(dname)
from levelsdata import wallsforlevel,killrectsforlevel,winrectsforlevel,spawnforlevel, backgroundforlevel, fakewallsforlevel
pygame.init()
pygame.mixer.init() ########################
s = 'sound'
jumpsound = pygame.mixer.Sound('sounds/SFX_Jump_09.wav')
hurtsound = pygame.mixer.Sound('sounds/SFX_Jump_50.wav')
wintouch = pygame.mixer.Sound('sounds/coin10.wav')
mainClock = pygame.time.Clock()
WINDOW = (800, 800)
screen = pygame.display.set_mode(WINDOW, 0, 32)
background = pygame.image.load('levelbackground/bgtitlescreen.png') 
walls = [pygame.Rect(0, 750, 800, 50)] #the walls and floors of the level
killrects = [pygame.Rect(0,749,50,10), pygame.Rect(750,749,50,10)] #This kind of rectangle kills the player 
winrects = [pygame.Rect(600,725,25,25)] #This kind of rectangle causes victory on contact 
fakewalls = [pygame.Rect(0,0,1,1)] ###################################
player = pygame.Rect(200, 725, 25, 25)
MOVESPEED = 15
MOVESPEEDy = 0
click = 0
jump = False
level = 0 ################################################################ test purposes, need to reset to 0 later
textinfo = 'Copyright lololol'
textcoord = [0, 700]
textcolor = (255,0,0)
spawn = [300, 600] 
collisionR, collisionL, collisionT, collisionB = False, False, False, False
moveLeft, moveRight, moveUp = False, False, False
font = pygame.font.SysFont(None,20)  

def drawscreen(walls,killrects,winrects):
    screen.blit(background,[0,0])
    for i in walls:
        pygame.draw.rect(screen, (0, 0, 0), i)
    for kr in range(len(killrects)):
        pygame.draw.rect(screen,(200,0,0),killrects[kr])
    for wr in range(len(winrects)):
        pygame.draw.rect(screen,(200,200,0),winrects[wr])
    pygame.draw.rect(screen, (0, 255, 0), player)
    pygame.display.update()

drawscreen(walls,killrects,winrects)
pygame.time.delay(3000)
level +=1
walls = wallsforlevel(level)
killrects = killrectsforlevel(level)
winrects = winrectsforlevel(level)
spawn = spawnforlevel(level)
background = backgroundforlevel(level)
player.left = (int(spawn[0]))
player.top = (int(spawn[1]))
drawscreen(walls,killrects,winrects)

def draw_text(text, font, color, surface, x, y):  ################################################################"
    """draw text function"""
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj, textrect)



while True:
    mousepos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                moveRight, moveLeft = False, True
            if event.key == K_RIGHT:
                moveLeft, moveRight = False, True
            if event.key == K_UP or event.key == K_SPACE:
                moveUp = True
            if event.key == K_a:
                click = 0
            #for dev purposes, a skip level key combination
            """if event.key == K_r:
                level += 1
                print(level)
                walls = wallsforlevel(level)
                killrects = killrectsforlevel(level)
                winrects = winrectsforlevel(level)
                spawn = spawnforlevel(level)
                background = backgroundforlevel(level)
                player.left = (int(spawn[0]))
                player.top = (int(spawn[1]))
                pygame.time.delay(500)
            #rewind time
            if event.key == K_t:
                level -= 1
                print(level)
                walls = wallsforlevel(level)
                killrects = killrectsforlevel(level)
                winrects = winrectsforlevel(level)
                spawn = spawnforlevel(level)
                background = backgroundforlevel(level)
                player.left = (int(spawn[0]))
                player.top = (int(spawn[1]))
                pygame.time.delay(500)"""
        if event.type == KEYUP:
            if event.key == K_LEFT:
                moveLeft = False
            if event.key == K_RIGHT:
                moveRight = False
            if event.key == K_UP or event.key == K_SPACE:
                moveUp = False
                
    collisionB = False
    """move/collision left"""
    if moveLeft and player.left > 0:
        player.left -= MOVESPEED
        for wall in walls[:]:
            if player.colliderect(wall):
                player.left = wall.right
                collisionB = True
    """move/collision right"""
    if moveRight and player.right < 800:
        player.right += MOVESPEED
        for wall in walls[:]:
            if player.colliderect(wall):
                player.right = wall.left
                collisionB = True
    screen.fill((35, 35, 60))  #draw player
    """fall"""
    player.bottom -= MOVESPEEDy
    MOVESPEEDy -= 1
    for wall in walls[:]:
        if player.colliderect(wall) and not jump:
            player.bottom = wall.top
            MOVESPEEDy = 0
            collisionB = True
    """jump"""
    if jump and MOVESPEEDy == 0:
        jump = False
    if moveUp and collisionB and not jump:
        jump = True
        pygame.mixer.Sound.play(jumpsound)
        MOVESPEEDy = 15
    """collision at the Top of the player"""
    for wall in walls[:]:
        if player.colliderect(wall) and jump:
            jump = False
            player.top = wall.bottom
            MOVESPEEDy = 0
            collisionT = True
    """collision with killrect""" #######################################################
    for kr in killrects[:]:
        if player.colliderect(kr):
            print("ouch")
            pygame.mixer.Sound.play(hurtsound)
            player.left = (spawn[0])
            player.top = (spawn[1])
    """collision with winrect""" ############################################################""
    for wr in winrects[:]:
        if player.colliderect(wr):
            pygame.mixer.Sound.play(wintouch)
            level += 1
            print(level)
            walls = wallsforlevel(level)
            killrects = killrectsforlevel(level)
            winrects = winrectsforlevel(level)
            spawn = spawnforlevel(level)
            fakewalls = fakewallsforlevel(level)
            background = backgroundforlevel(level)
            player.left = (int(spawn[0]))
            player.top = (int(spawn[1]))
    #"""new wall""" this is a previous function that was used  to create a new wall in-game but it was scrapped
    #x, y = pygame.mouse.get_pos()
    #draw_text(str(pygame.mouse.get_pos()), font, (0,255,0),screen, 0, 0)
    #if event.type == MOUSEBUTTONUP and click == 0:
    #    click = 1
    #    walls.append(pygame.Rect(x, y, 100, 100))
    #if click == 1:
    #    walls[len(walls) - 1].width = abs(x - walls[len(walls) - 1].left)
    #    walls[len(walls) - 1].height = abs(y - walls[len(walls) - 1].top)
    #    if event.type == MOUSEBUTTONDOWN:
    #        click = 2
    screen.blit(background,[0,0])
    """draw walls, killrect, winrect and fakewalls""" ##########################################################
    for i in range(len(walls)):
        pygame.draw.rect(screen, (0, 0, 0), walls[i])
    for kr in range(len(killrects)):
        pygame.draw.rect(screen,(200,0,0),killrects[kr])
    for wr in range(len(winrects)):
        pygame.draw.rect(screen,(200,200,0),winrects[wr])
    for fr in range(len(fakewalls)):
        pygame.draw.rect(screen,(0,0,0), fakewalls[fr])
    pygame.draw.rect(screen, (0, 255, 0), player)
    """draw text"""  ################################################################"
    
    draw_text(('x='+str(mousepos[0])+' y='+str(mousepos[1])), font,(255,255,255),screen,0,0)
    draw_text(textinfo, font, textcolor, screen, textcoord[0], textcoord[1])
    draw_text(("level: "+str(level)), font, (250,250,0), screen, 600,0)
    """end"""
    pygame.display.update()
    mainClock.tick(60) #nb of FPS
import pygame
levelwalls1 = [pygame.Rect(0, 750, 800, 50)]
levelwalls2 = [pygame.Rect(0, 750, 800, 50), pygame.Rect(350,700,50,50)]
levelwalls3 = [pygame.Rect(0, 750, 800, 50), pygame.Rect(350,600,50,150)]
levelwalls6 = [pygame.Rect(0, 750, 800, 50), pygame.Rect(0, 600, 200, 400)]
levelwalls7 = [pygame.Rect(0, 750, 800, 50), pygame.Rect(350,100,100,700), pygame.Rect(0,400,200,50), pygame.Rect(150,100,100,200)]
levelwalls16 = [pygame.Rect(0, 750, 800, 50), pygame.Rect(350, 0, 100, 400),pygame.Rect(350,500,100,300)]
levelwalls20 = [pygame.Rect(0, 750, 800, 50), pygame.Rect(350,0,25,75),pygame.Rect(425,0,25,75),pygame.Rect(350,75,100,50),pygame.Rect(375,75,50,725)]
levelwalls21 = [pygame.Rect(0, 750, 800, 50),pygame.Rect(0, 0, 1, 740)]

killzone1 = []
killzone4 = [pygame.Rect(350,740,50,10)]
killzone5 = [pygame.Rect(350,0,50,720)]
killzone6 = [pygame.Rect(200,740,450,10)]
killzone7 = [pygame.Rect(340, 90,120,100),pygame.Rect(225,125,55,155)]
killzone15 = [pygame.Rect(350,650,100,125)]
killzone16 = [pygame.Rect(0,0,800,50)]
killzone21 = [pygame.Rect(0,740,25,10),pygame.Rect(120,740,580,10)]

winzone1 = [pygame.Rect(765,715, 25, 25)]
winzone20 = [pygame.Rect(375,25,50,50)]
winzone22 = []

spawn1 = [50, 700]
spawn2 = spawn1
spawn3 = spawn1
spawn4 = spawn1
spawn5 = spawn1
spawn6 = [50, 550]

fakewall1 = [pygame.Rect(0,0,0,0)]
fakewall16 = [pygame.Rect(350, 400, 100,100)]

def wallsforlevel(currentlevel):
    if currentlevel == 1:
        return levelwalls1
    elif currentlevel == 2:
        return levelwalls2
    elif currentlevel == 3:
        return levelwalls3
    elif currentlevel == 6:
        return levelwalls6
    elif currentlevel == 7:
        return levelwalls7
    elif currentlevel == 16:
        return levelwalls16
    elif currentlevel == 20:
        return levelwalls20
    elif currentlevel == 21:
        return levelwalls21
    else:
        return levelwalls1

def killrectsforlevel(currentlevel):
    if currentlevel == 4:
        return killzone4
    elif currentlevel == 5:
        return killzone5
    elif currentlevel == 6:
        return killzone6
    elif currentlevel == 7:
        return killzone7
    elif currentlevel == 15:
        return killzone15
    elif currentlevel == 16:
        return killzone16
    elif currentlevel == 21:
        return killzone21
    else:
        return killzone1

def spawnforlevel(currentlevel):
    if currentlevel == 6:
        return spawn6
    else:
        return spawn1

def winrectsforlevel(currentlevel):
    if currentlevel == 20:
        return winzone20
    if currentlevel == 22:
        return winzone22
    else:
        return winzone1

def backgroundforlevel(currentlevel):
    if currentlevel ==1:
        return pygame.image.load('levelbackground/bg1.png')
    elif currentlevel == 2:
        return pygame.image.load('levelbackground/bg2.png')
    elif currentlevel == 3:
        return pygame.image.load('levelbackground/bg3.png')
    elif currentlevel == 4:
        return pygame.image.load('levelbackground/bg4.png')
    elif currentlevel == 8:
        return pygame.image.load('levelbackground/bg8.png')
    elif currentlevel == 10:
        return pygame.image.load('levelbackground/bg10.png')
    elif currentlevel == 13:
        return pygame.image.load('levelbackground/bg13.png')
    elif currentlevel == 14:
        return pygame.image.load('levelbackground/bg14.png')
    elif currentlevel == 15:
        return pygame.image.load('levelbackground/bg15.png')
    elif currentlevel == 16:
        return pygame.image.load('levelbackground/bg16.png')
    elif currentlevel == 17:
        return pygame.image.load('levelbackground/bg14.png')
    elif currentlevel == 18:
        return pygame.image.load('levelbackground/bg18.png')
    elif currentlevel == 19:
        return pygame.image.load('levelbackground/bg19.png')
    elif currentlevel == 22:
        return pygame.image.load('levelbackground/bg22.png')
    else:
        return pygame.image.load('levelbackground/bgtest.png')

def fakewallsforlevel(currentlevel):
    if currentlevel == 16:
        return fakewall16
    else:
        return fakewall1
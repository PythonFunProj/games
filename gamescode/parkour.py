import pygame
from pygame.locals import *
pygame.init()
mainClock = pygame.time.Clock()
WINDOW = (800, 800)
screen = pygame.display.set_mode(WINDOW, 0, 32)
walls = [pygame.Rect(0, 750, 800, 50), pygame.Rect(600, 600, 300, 300), pygame.Rect(200, 200, 50, 50), pygame.Rect(400,90,400,10)]
killrects = pygame.Rect(0,749,50,10) #This kind of rectangle kills the player
player = pygame.Rect(300, 600, 25, 25)
MOVESPEED = 15
MOVESPEEDy = 0
click = 0
jump = False
collisionR, collisionL, collisionT, collisionB = False, False, False, False
moveLeft, moveRight, moveUp = False, False, False
font = pygame.font.SysFont(None,20)

def draw_text(text, font, color, surface, x, y): #drawtext function
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj, textrect)

while True:
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
    pygame.draw.rect(screen, (0, 0, 255), player)
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
        MOVESPEEDy = 15
    """collision at the Top of the player"""
    for wall in walls[:]:
        if player.colliderect(wall) and jump:
            jump = False
            player.top = wall.bottom
            MOVESPEEDy = 0
            collisionT = True
    """collision with killrect"""
    if player.colliderect(killrects):
        print("ouch")
        player.left = (500)
        player.top = (700)
    """new wall"""
    x, y = pygame.mouse.get_pos()
    draw_text(str(pygame.mouse.get_pos()), font, (0,255,0),screen, 0, 0)
    if event.type == MOUSEBUTTONUP and click == 0:
        click = 1
        walls.append(pygame.Rect(x, y, 100, 100))
    if click == 1:
        walls[len(walls) - 1].width = abs(x - walls[len(walls) - 1].left)
        walls[len(walls) - 1].height = abs(y - walls[len(walls) - 1].top)
        if event.type == MOUSEBUTTONDOWN:
            click = 2
    """draw walls and killrect"""
    for i in range(len(walls)):
        pygame.draw.rect(screen, (0, 0, 0), walls[i])
    pygame.draw.rect(screen,(200,0,0),killrects)
    """draw text"""
    draw_text("this will hurt you", font, (255,0,0), screen, 0, 700)
    """end"""
    pygame.display.update()
    mainClock.tick(30) #nb of FPS 

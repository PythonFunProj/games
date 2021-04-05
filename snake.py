import pygame
from pygame.locals import *
import time, random
X = [3, 4, 5, 6, 7, 8, 9, 10]
Y = [5, 5, 5, 5, 5, 5, 5, 5]
nbeat = 0
yapple = 0
xapple = 0
done = True
pygame.init()
font = pygame.font.Font(None, 100)
while yapple in Y or xapple in X or xapple == 0:
    yapple = random.randint(2, 11)
    xapple = random.randint(2, 21)
mainClock = pygame.time.Clock()
WINDOW = (1200, 650)
screen = pygame.display.set_mode(WINDOW, 0, 32)
walls = [pygame.Rect(40, 40, 1110, 10), pygame.Rect(40, 40, 10, 560), pygame.Rect(40, 600, 1110, 10),
         pygame.Rect(1150, 40, 10, 570)]
moveLeft, moveRight, moveUp, moveDown = False, True, False, False
while done:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT and not moveRight:
                moveLeft, moveRight, moveUp, moveDown = True, False, False, False
            if event.key == K_RIGHT and not moveLeft:
                moveLeft, moveRight, moveUp, moveDown = False, True, False, False
            if event.key == K_UP and not moveDown:
                moveLeft, moveRight, moveUp, moveDown = False, False, True, False
            if event.key == K_DOWN and not moveUp:
                moveLeft, moveRight, moveUp, moveDown = False, False, False, True
    eat = 0
    if moveLeft:
        if X[len(X) - 1] - 1 == xapple and Y[len(Y) - 1] == yapple:
            X.append(xapple)
            Y.append(yapple)
            eat = 1
        else:
            for i in range(0, len(X) - 1):
                if X[len(X) - 1] - 1 == X[i] and Y[len(Y) - 1] == Y[i]:
                    print("lose")
                    done = False
            X[:] = X[1:] + X[:1]
            Y[:] = Y[1:] + Y[:1]
            X[len(X) - 1] = X[len(X) - 2] - 1
            Y[len(Y) - 1] = Y[len(Y) - 2]
    if moveRight:
        if X[len(X) - 1] + 1 == xapple and Y[len(Y) - 1] == yapple:
            X.append(xapple)
            Y.append(yapple)
            eat = 1
        else:
            for i in range(0, len(X) - 1):
                if X[len(X) - 1] + 1 == X[i] and Y[len(Y) - 1] == Y[i]:
                    print("lose")
                    done = False
            X[:] = X[1:] + X[:1]
            Y[:] = Y[1:] + Y[:1]
            X[len(X) - 1] = X[len(X) - 2] + 1
            Y[len(Y) - 1] = Y[len(Y) - 2]
    if moveUp:
        if X[len(X) - 1] == xapple and Y[len(Y) - 1] - 1 == yapple:
            X.append(xapple)
            Y.append(yapple)
            eat = 1
        else:
            for i in range(0, len(X) - 1):
                if X[len(X) - 1] == X[i] and Y[len(Y) - 1] - 1 == Y[i]:
                    print("lose")
                    done = False
            X[:] = X[1:] + X[:1]
            Y[:] = Y[1:] + Y[:1]
            Y[len(Y) - 1] = Y[len(Y) - 2] - 1
            X[len(X) - 1] = X[len(X) - 2]
    if moveDown:
        if X[len(X) - 1] == xapple and Y[len(Y) - 1] + 1 == yapple:
            X.append(xapple)
            Y.append(yapple)
            eat = 1
        else:
            for i in range(0, len(X) - 1):
                if X[len(X) - 1] == X[i] and Y[len(Y) - 1] + 1 == Y[i]:
                    print("lose")
                    done = False
            X[:] = X[1:] + X[:1]
            Y[:] = Y[1:] + Y[:1]
            Y[len(Y) - 1] = Y[len(Y) - 2] + 1
            X[len(X) - 1] = X[len(X) - 2]
    if eat == 1:
        nbeat += 1
        while yapple in Y and xapple in X:
            yapple = random.randint(2, 11)
            xapple = random.randint(2, 21)

    if not 1 < X[len(X)-1] < 22 or not 1 < Y[len(Y)-1] < 12:
        print("lose")
        done = False
    screen.fill((35, 35, 60))
    screen.blit(font.render(str(nbeat), True, (130, 0, 0)), (10, 10))
    for i in range(0, len(X)-1):
        pygame.draw.rect(screen, (0, 200, 0), pygame.Rect(50 * X[i], 50 * Y[i], 50, 50))
        pygame.draw.rect(screen, (20, 20, 20), pygame.Rect(50 * X[i], 50 * Y[i], 50, 50), 2)
    pygame.draw.rect(screen, (0, 100, 0), pygame.Rect(50 * X[(len(X)-1)], 50 * Y[(len(X)-1)], 50, 50))
    pygame.draw.rect(screen, (20, 20, 20), pygame.Rect(50 * X[(len(X)-1)], 50 * Y[(len(X)-1)], 50, 50), 2)
    pygame.draw.rect(screen, (200, 20, 20), pygame.Rect(50 * xapple, 50 * yapple, 50, 50))
    """draw walls"""
    for i in range(len(walls)):
        pygame.draw.rect(screen, (0, 0, 0), walls[i])
    """end"""
    pygame.display.update()
    time.sleep(0.4)

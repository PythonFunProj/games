import pygame
from pygame.locals import *
import time, random
import os
abspath = os.path.abspath(__file__) #sets the location of the Menu.py as the working directory
dname = os.path.dirname(abspath)
os.chdir(dname)

R = [1, 1, 1, 1, 1, 1, 1, 1]

body1 = pygame.image.load(r'snake2/body.png')
head = pygame.image.load(r'snake2/head.png')
tail = pygame.image.load(r'snake2/tail.png')
turn = pygame.image.load(r'snake2/turn.png')
water = pygame.image.load(r'snake2/water.png')
grass = pygame.image.load(r'snake2/grass.png')
apple = pygame.image.load(r'snake2/apple.png')


def body(d):
    R[:] = R[1:] + R[:1]
    R[len(R) - 1] = d

def apple1():
    R[:] = R[-1:] + R[:-1]


def main():
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
    clock = pygame.time.Clock()

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
            body(1)
            if X[len(X) - 1] - 1 == xapple and Y[len(Y) - 1] == yapple:
                X.append(xapple)
                Y.append(yapple)
                R.append(1)
                # body(1)
                eat = 1
                apple1()
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
            body(3)
            if X[len(X) - 1] + 1 == xapple and Y[len(Y) - 1] == yapple:
                X.append(xapple)
                Y.append(yapple)
                R.append(3)
                eat = 1
                apple1()
                # body(3)
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
            body(0)
            if X[len(X) - 1] == xapple and Y[len(Y) - 1] - 1 == yapple:
                X.append(xapple)
                Y.append(yapple)
                R.append(0)
                apple1()
                # body(0)
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
            body(2)
            if X[len(X) - 1] == xapple and Y[len(Y) - 1] + 1 == yapple:
                X.append(xapple)
                Y.append(yapple)
                R.append(2)
                eat = 1
                apple1()
                # body(2)
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
        screen.blit(water, (0, 0))

        for i in range(1, 22):
            for j in range(1, 12):
                screen.blit(grass, (50*i, 50 * j))

        print(X, 'x', '\n', Y, 'y', '\n', R)

        screen.blit(apple, (50 * xapple,  50 * yapple))

        screen.blit(pygame.transform.rotate(tail, 90*R[1]), (50 * X[0], 50 * Y[0]))

        for i in range(1, len(R)-1):
            if R[i] == R[i+1]:
                if R[i] in (0, 2):
                    screen.blit(body1, (50 * X[i], 50 * Y[i]))
                else:
                    screen.blit(pygame.transform.rotate(body1, 90), (50 * X[i], 50 * Y[i]))
            else:
                if (R[i] == 0 and R[i+1] == 3) or (R[i] == 1 and R[i+1] == 2):
                    screen.blit(turn, (50 * X[i], 50 * Y[i]))
                if (R[i] == 3 and R[i+1] == 2) or (R[i] == 0 and R[i+1] == 1):
                    screen.blit(pygame.transform.rotate(turn, 90*3), (50 * X[i], 50 * Y[i]))
                if (R[i] == 3 and R[i+1] == 0) or (R[i] == 2 and R[i+1] == 1):
                    screen.blit(pygame.transform.rotate(turn, 90*2), (50 * X[i], 50 * Y[i]))
                if (R[i] == 2 and R[i+1] == 3) or (R[i] == 1 and R[i+1] == 0):
                    screen.blit(pygame.transform.rotate(turn, 90*1), (50 * X[i], 50 * Y[i]))

        screen.blit(pygame.transform.rotate(head, 90*R[len(R)-1]), (50 * X[len(R)-1], 50 * Y[len(R)-1]))

        pygame.display.update()
        clock.tick(2)

main()
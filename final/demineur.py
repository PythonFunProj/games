import numpy as np
import random
import pygame
import os 
abspath = os.path.abspath(__file__) #sets the location of the .py file as the working directory
dname = os.path.dirname(abspath)
os.chdir(dname)
pygame.init()
def main():
    """variable:"""
    spacex, spacey = 0, 0
    level = 4
    time = 0
    width = 19
    length = 26
    nbbombe = 99
    lensquare = 40
    flag = 0
    click = 0
    color = [(0, 0, 175), (0, 200, 0), (175, 0, 0), (0, 0, 75), (0, 0, 75), (0, 0, 75)]

    """pygame relative:"""
    font = pygame.font.Font(None, 50)
    screen = pygame.display.set_mode((800, 640))
    display_surface = pygame.display.set_mode((int(lensquare*length), int(lensquare*width)))
    image = pygame.image.load(r'images/carré.jpg')
    image = pygame. transform. scale(image, (lensquare, lensquare))
    image2 = pygame.image.load(r'images/drapeau.jpg')
    image2 = pygame. transform. scale(image2, (lensquare, lensquare))
    image3 = pygame.image.load(r'images/mine.jpg')
    image3 = pygame. transform. scale(image3, (lensquare, lensquare))
    image4 = pygame.image.load(r'images/mine2.jpg')

    board = np.zeros((length, width), dtype=int)
    boardvisible = np.zeros((length, width), dtype=int)


    def board1():
        screen.fill([150, 150, 150])
        for i in range(0, length):
            for j in range(0, width):
                pygame.draw.rect(screen, (200, 200, 200), pygame.Rect(spacex + lensquare * i, spacey + lensquare * j, lensquare, lensquare))
                if boardvisible[i, j] == 0:
                    display_surface.blit(image, (spacex + lensquare * i, spacey + lensquare * j))
                    nombre = ''
                elif boardvisible[i, j] == -3:
                    display_surface.blit(image2, (spacex + lensquare * i, spacey + lensquare * j))
                    nombre = ''
                else:
                    nombre = boardvisible[i, j]
                    pygame.draw.rect(screen, (100, 100, 100), pygame.Rect(spacex + lensquare * i, spacey + lensquare * j, lensquare, lensquare))
                    pygame.draw.rect(screen, (200, 200, 200), pygame.Rect(spacex + lensquare * i+1, spacey + lensquare * j+1, lensquare-2, lensquare-2))
                screen.blit(font.render(str(nombre), True, color[boardvisible[i, j] - 1]), (spacex + lensquare * i + 10, spacey + lensquare * j + 4))
                if boardvisible[i, j] == -2:
                    pygame.draw.rect(screen, (200, 200, 200), pygame.Rect(spacex + lensquare * i, spacey + lensquare * j, lensquare, lensquare))
        pygame.draw.rect(screen, (0, 0, 0),
                         pygame.Rect(spacex -3, spacey -3, lensquare*length+3, lensquare*width+3), 3)

        pygame.display.flip()
    board1()
    done = True
    while done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = False
        x, y = pygame.mouse.get_pos()
        if time == 0:
            font2 = pygame.font.Font(None, 100)
            font3 = pygame.font.Font(None, 70)
            pygame.draw.rect(screen, (148, 141, 130), pygame.Rect(100, 100, int(lensquare*length) - 200, int(lensquare*width)-200))
            screen.blit(font2.render('level?', True, (60, 60, 60)), (220, 170))
            pygame.draw.rect(screen, (100, 100, 100), pygame.Rect(220, 300, 250, 100))
            pygame.draw.rect(screen, (100, 100, 100), pygame.Rect(580, 300, 250, 100))
            pygame.draw.rect(screen, (100, 100, 100), pygame.Rect(220, 455, 250, 100))
            pygame.draw.rect(screen, (100, 100, 100), pygame.Rect(580, 455, 250, 100))
            screen.blit(font3.render('easy', True, (180, 180, 180)), (285, 325))
            screen.blit(font3.render('medium', True, (180, 180, 180)), (613, 325))
            screen.blit(font3.render('hard', True, (180, 180, 180)), (285, 480))
            screen.blit(font3.render('expert', True, (180, 180, 180)), (613, 480))
            if pygame.mouse.get_pressed()[0]:
                if 220 < x < 570 and 300 < y < 400:
                    width = 8
                    length = 10
                    nbbombe = 11
                    lensquare = 55
                if 220 < x < 570 and 455 < y < 555:
                    width = 16
                    length = 20
                    nbbombe = 50
                    lensquare = 40
                if 580 < x < 830 and 300 < y < 400:
                    width = 9
                    length = 14
                    nbbombe = 15
                    lensquare = 47
                if 580 < x < 830 and 455 < y < 555:
                    width = 19
                    length = 26
                    nbbombe = 99
                    lensquare = 40
                time = 1
                image = pygame.transform.scale(image, (lensquare, lensquare))
                image2 = pygame.transform.scale(image2, (lensquare, lensquare))
                image3 = pygame.transform.scale(image3, (lensquare, lensquare))
                image4 = pygame.transform.scale(image4, (lensquare, lensquare))
                spacex, spacey = (1040 - int(lensquare*length))//2, (760 - int(lensquare*width))//2
                click = 1
        if time == 1:
            x, y = x - spacex, y - spacey
            board1()
            if pygame.mouse.get_pressed()[0] and click == 0:
                xb = x // lensquare
                yb = y // lensquare
                done = False
            if pygame.mouse.get_pressed()[2] and click == 0 and \
                    (boardvisible[x // lensquare, y // lensquare] == 0 or boardvisible[x // lensquare, y // lensquare] == -3):
                click = 1
                if boardvisible[x // lensquare, y // lensquare] == 0:
                    boardvisible[x // lensquare, y // lensquare] = -3
                    flag += 1
                else:
                    boardvisible[x // lensquare, y // lensquare] = 0
                    flag -= 1
                board1()
            if not pygame.mouse.get_pressed()[2] and not pygame.mouse.get_pressed()[0]:
                    click = 0
        pygame.display.flip()
    a = 0
    while a != nbbombe:
        a += 1
        x = random.randrange(0, length)
        y = random.randrange(0, width)
        if board[x, y] == 0:
            if xb-2 < x < xb+2 and yb-2 < y < yb+2:
                print(x, y, xb, yb)
                a -= 1
            else:
                board[x, y] = 9
        else:
            a -= 1
    for i in range(0, length):
        for j in range(0, width):
            if board[i, j] != 9:
                n = 0
                for k in range(0, 3):
                    for l in range(0, 3):
                        if length - 1 >= i+k-1 >= 0 and width-1 >= j+l-1 >= 0:
                            if board[i+k-1, j+l-1] == 9 and (k != 1 or l != 1):
                                n += 1
                board[i, j] = n
    done = True
    screen.fill([150, 150, 150])
    board1()
    print(board)
    while done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = False
        x, y = pygame.mouse.get_pos()
        x, y = x - spacex, y - spacey
        if pygame.mouse.get_pressed()[0] and click == 0:
            click = 1
            x = x//lensquare
            y = y//lensquare
            if board[x, y] == 9:
                for i in range(0, length):
                    for j in range(0, width):
                        if board[i, j] == 9:
                            display_surface.blit(image3, (spacex + lensquare * i-1, spacey + lensquare * j-1))
                while done:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            done = False
                    display_surface.blit(image4, (spacex + lensquare * x, spacey + lensquare * y))
                    screen.blit(font2.render('you lose', True, (200, 0, 0)), (220, 170))
                    pygame.display.flip()
                done = False
            elif board[x, y] == 0 and not boardvisible[x, y] == -3:
                xt = 0
                yt = 0
                boardvisible[x, y] = -1
                board[x, y] = -1
                try1 = 1
                while try1 != 0:
                    try1 = 0
                    for i in range(0, length):
                        for j in range(0, width):
                            if board[i, j] == -1:
                                board[i, j] = -2
                                for k in range(0, 3):
                                    for l in range(0, 3):
                                        if 0 <= i+k-1 <= length-1 and 0 <= j+l-1 <= width-1:
                                            if board[i+k-1, j+l-1] == 0:
                                                boardvisible[i + k - 1, j + l - 1] = -1
                                                board[i + k - 1, j + l - 1] = -1
                                                try1 += 1
                                            else:
                                                boardvisible[i + k - 1, j + l - 1] = board[i + k - 1, j + l- 1]
                board1()
            else:
                boardvisible[x, y] = board[x, y]
                board1()
        x, y = pygame.mouse.get_pos()
        x, y = x - spacex, y - spacey
        if pygame.mouse.get_pressed()[2] and click == 0 and\
                (boardvisible[x//lensquare, y//lensquare] == 0 or boardvisible[x//lensquare, y//lensquare] == -3):
            click = 1
            if boardvisible[x//lensquare, y//lensquare] == 0:
                boardvisible[x//lensquare, y//lensquare] = -3
                flag += 1
            else:
                boardvisible[x//lensquare, y//lensquare] = 0
                flag -= 1
            board1()
        if not pygame.mouse.get_pressed()[2] and not pygame.mouse.get_pressed()[0]:
            click = 0
        if flag == nbbombe:
            test = 0
            for i in range(0, length):
                for j in range(0, width):
                    if boardvisible[i, j] == 0:
                        test = 1
            if test != 1:
                for i in range(0, length):
                    for j in range(0, width):
                        if board[i, j] == 9:
                            display_surface.blit(image3, (spacex + lensquare * i-1, spacey + lensquare * j-1))
                screen.blit(font2.render('you win', True, (0, 0, 100)), (220, 170))
                pygame.display.flip()
                #done = False

main()
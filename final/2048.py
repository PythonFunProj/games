import numpy as np
import random
import pygame
import pickle
import os 
abspath = os.path.abspath(__file__) #sets the location of the .py file as the working directory
dname = os.path.dirname(abspath)
os.chdir(dname)

def main():
    recommencer = 0
    done3 = True
    heightscreen = 700/900
    pygame.display.set_caption('Image')
    image = pygame.image.load(r'images/retour.jpg')
    image = pygame. transform. scale(image, (int(heightscreen*56), int(heightscreen*56)))
    pygame.display.set_caption('Image2')
    image2 = pygame.image.load(r'images/recommencer.jpg')
    image2 = pygame. transform. scale(image2, (int(heightscreen*56), int(heightscreen*56)))
    clock = pygame.time.Clock()

    while done3:

        class Game:
            def __init__(self, score, board, bestscore, lastmove):
                self.score = score
                self.board = board
                self.bestscore = bestscore
                self.lastmove = lastmove




        with open('game.save', 'rb') as f:
            jeu2 = pickle.load(f)
        bestscore = jeu2.bestscore
        pygame.init()
        pressed = 0
        score = 0
        board = np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0,  0, 0, 0]])
        lastmove = np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0,  0, 0, 0]])
        board[random.randrange(0, 4), random.randrange(0, 4)] = 2
        for i in range(0, 4):
            for j in range(0, 4):
                lastmove[i, j] = board[i, j]
        done = True
        pressed2 = 1
        display_surface = pygame.display.set_mode((int(heightscreen*650), int(heightscreen*900)))
        screen = pygame.display.set_mode((int(heightscreen*650), int(heightscreen*900)))
        screen.fill([0, 0, 0])
        ud = 0
        font = pygame.font.Font(None, int(heightscreen*50))
        font1 = pygame.font.Font(None, int(heightscreen*200))
        colors = [(254, 254, 226), (231, 168, 84), (230, 126, 48), (237, 127, 16), (253, 70, 38), (198, 8, 0), (247, 255, 60),
                  (223, 218, 0), (253, 238, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0),
                  (0, 0, 0)]

        def board1():
            screen.fill([193, 191, 177])
            for i in range(0, 4):
                for j in range(0, 4):
                    if board[j, i] != 0:
                        t = 0
                        n = board[j, i]
                        while n != 2:
                            t += 1
                            n /= 2
                        pygame.draw.rect(screen, colors[t], pygame.Rect(int(heightscreen*(i*150+25)),
                                                                        int(heightscreen*(j*150+275)),
                                                                        int(heightscreen*150), int(heightscreen*150)))
                        if board[j, i] == 2 or board[j, i] == 128 or board[j, i] == 256 or board[j, i] == 512:
                            screen.blit(font.render(str(board[j, i]), True, (0, 0, 0)),
                                        (int(heightscreen*(i*150+85)), int(heightscreen*(j*150+335))))
                        else:
                            screen.blit(font.render(str(board[j, i]), True, (230, 230, 230)),
                                        (int(heightscreen * (i * 150 + 85)), int(heightscreen * (j * 150 + 335))))
                        screen.blit(font1.render(str(2048), True, (50, 50, 50)), (int(heightscreen*25), int(heightscreen*25)))
                        screen.blit(font.render('score:', True, (150, 50, 50)), (int(heightscreen*435), int(heightscreen*25)))
                        screen.blit(font.render(str(score), True, (50, 50, 150)), (int(heightscreen*435), int(heightscreen*55)))
                        screen.blit(font.render('best score:', True, (150, 50, 50)),
                                    (int(heightscreen * 435), int(heightscreen * 95)))
                        screen.blit(font.render(str(bestscore), True, (50, 50, 150)),
                                    (int(heightscreen * 435), int(heightscreen * 125)))
                        pygame.draw.rect(screen, (125, 125, 125), pygame.Rect(int(heightscreen * 75),
                                                                        int(heightscreen * 175),
                                                                        int(heightscreen * 60), int(heightscreen * 60)))
                        pygame.draw.rect(screen, (125, 125, 125), pygame.Rect(int(heightscreen * 200),
                                                                              int(heightscreen * 175),
                                                                              int(heightscreen * 60), int(heightscreen * 60)))
            display_surface.blit(image, (int(heightscreen*78), int(heightscreen*177)))
            display_surface.blit(image2, (int(heightscreen*202), int(heightscreen*177)))

            for i in range(0, 5):
                pygame.draw.line(screen, (127, 127, 127), (int(heightscreen*(i*150+25)), int(heightscreen*275)),
                                 (int(heightscreen*(i*150+25)), int(heightscreen*(600+275))), 3)
                pygame.draw.line(screen, (127, 127, 127), (int(heightscreen*25), int(heightscreen*(275+i*150))),
                                 (int(heightscreen*(600+25)), int(heightscreen*(275+i*150))), 3)
                pygame.display.flip()


        board1()
        done1 = True
        while done1:
            font2 = pygame.font.Font(None, int(heightscreen * 100))
            pygame.draw.rect(screen, (118, 111, 100), pygame.Rect(int(heightscreen * 100),
                                                                  int(heightscreen * 150),
                                                                  int(heightscreen * 450), int(heightscreen * 550)))
            if recommencer == 0:
                screen.blit(font2.render('continue?:', True, (30, 40, 40)),
                            (int(heightscreen * 150), int(heightscreen * 240)))
            else:
                screen.blit(font2.render('sure?:', True, (30, 40, 40)),
                            (int(heightscreen * 150), int(heightscreen * 240)))
            pygame.draw.rect(screen, (0, 200, 0), pygame.Rect(int(heightscreen * 195),
                                            int(heightscreen * 400), int(heightscreen * 100), int(heightscreen * 100)))
            pygame.draw.rect(screen, (200, 0, 0), pygame.Rect(int(heightscreen * 350),
                                            int(heightscreen * 400), int(heightscreen * 100), int(heightscreen * 100)))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = False
                    done1 = False
                    done2 = False
            x, y = pygame.mouse.get_pos()
            if int(heightscreen * 195) < x < int(heightscreen * 295) and int(heightscreen * 400) < y < int(heightscreen * 500):
                pygame.draw.rect(screen, (0, 250, 0), pygame.Rect(int(heightscreen * 195),
                                                                  int(heightscreen * 400), int(heightscreen * 100),
                                                                  int(heightscreen * 100)))
                if pygame.mouse.get_pressed()[0]:
                    if recommencer == 0:
                        score = jeu2.score
                        board = jeu2.board
                        lastmove = jeu2.lastmove
                    done1 = False
                    board1()
            if int(heightscreen * 350) < x < int(heightscreen * 450) and int(heightscreen * 400) < y < int(heightscreen * 500):
                pygame.draw.rect(screen, (250, 0, 0), pygame.Rect(int(heightscreen * 350),
                                                                  int(heightscreen * 400), int(heightscreen * 100),
                                                                  int(heightscreen * 100)))
                if pygame.mouse.get_pressed()[0]:
                    if recommencer == 1:
                        score = jeu2.score
                        board = jeu2.board
                        lastmove = jeu2.lastmove
                    done1 = False
                    board1()
            pygame.display.flip()
        for i in range(0, 4):
            pygame.draw.line(screen, (200, 0, 0), (int(heightscreen*(i * 150+25)), int(heightscreen*275)),
                             (int(heightscreen*(i * 150+25)), int(heightscreen*(600+275))), 3)
            pygame.draw.line(screen, (200, 0, 0), ((int(heightscreen*25)), int(heightscreen*(i * 150+275))),
                             (int(heightscreen*(600+25)), int(heightscreen*(i * 150+275))), 3)
        cont = 1
        while done:
            cont -= 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = False
                    done3 = False
            key = pygame.key.get_pressed()

            if key[pygame.K_LEFT] and pressed == 0 :
                pressed = 1
                a = -1
                b = 0
                pressed2 = 0
                controler = False
            if key[pygame.K_UP] and pressed == 0:
                pressed = 1
                a = 0
                pressed2 = 0
                b = -1
                controler = False
            if key[pygame.K_DOWN] and pressed == 0:
                a = 0
                pressed = 1
                b = -1
                ud =1
                pressed2 = 0
                controler = False
            if key[pygame.K_RIGHT] and pressed == 0:
                a = -1
                pressed = 1
                b = 0
                ud = 1
                pressed2 = 0
                controler = False


            x, y = pygame.mouse.get_pos()
            if pygame.mouse.get_pressed()[0] and int(heightscreen * 75) < x < int(heightscreen * 135) and \
                    int(heightscreen * 175) < y < int(heightscreen * 235):
                for i in range(0, 4):
                    for j in range(0, 4):
                        board[i, j] = lastmove[i, j]
                board1()
            if pygame.mouse.get_pressed()[0] and int(heightscreen * 200) < x < int(heightscreen * 260) and \
                    int(heightscreen * 175) < y < int(heightscreen * 235):
                done = False
                recommencer = 1
            if score >= bestscore:
                bestscore = score
            if pressed == 1 and pressed2 == 0:
                pressed2 = 1
                for i in range(0, 4):
                    for j in range(0, 4):
                        lastmove[i, j] = board[i, j]
                done2 = True
                test = 0
                t = 0
                if ud == 1:
                    board = np.rot90(board, 2)
                while done2:
                    for i in range(0, 4):
                        for j in range(0, 4):
                            if 3 >= j + a >= 0 and 3 >= i + b >= 0:

                                if board[i, j] == board[i + b, j + a]:
                                    if board[i, j] != 0:
                                        t = 1
                                    score += board[i, j]*2
                                    board[i + b, j + a] = board[i, j]*-2
                                    board[i, j] = 0
                                else:
                                    test += 1
                                if board[i, j] != 0 and board[i + b, j + a] == 0:
                                    if board[i, j] != 0:
                                        t = 1
                                    board[i + b, j + a] = board[i, j]
                                    board[i, j] = 0

                                else:
                                    test += 1
                    if test >= 64:
                        done2 = False
                for i in range(0, 4):
                    for j in range(0, 4):
                        if board[i, j] < 0:
                            board[i, j] = board[i, j]*-1
                done2 = True
                if ud == 1:
                    board = np.rot90(board, 2)
                    ud = 0
                while done2 and t == 1:
                    x = random.randrange(0, 4)
                    y = random.randrange(0, 4)
                    if board[y, x] == 0:
                        nombre = random.random()
                        if nombre < 0.66666666:
                            nombre = 2
                        else:
                            nombre = 4
                        board[y, x] = nombre
                        done2 = False
                if score >= bestscore:
                    bestscore = score
                board1()
                pygame.display.flip()
            if cont < -2:
                if not key[pygame.K_LEFT] and not key[pygame.K_UP] and not key[pygame.K_DOWN] and not key[pygame.K_RIGHT]:
                    pressed = 0
                    print(1, cont)


        pygame.display.flip()


        class Game:
            def __init__(self, score, board, bestscore, lastmove):
                self.score = score
                self.board = board
                self.bestscore = bestscore
                self.lastmove = lastmove

        jeu = Game(score=score, board=board, bestscore=bestscore, lastmove=lastmove)
        with open("game.save", "wb") as f:
            pickle.dump(jeu, f)

if __name__ == '__main__':
    main()
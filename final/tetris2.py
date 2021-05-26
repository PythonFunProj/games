import random
import numpy as np
import pygame
from pygame.locals import *

taille = 700


# to do list:
# rotation problem
# rotation piece n°7
# time
# pause
# menu
# musique


def tetris():
    heightscreen = taille / 991
    tcarre = ((taille - 23) // 22)
    pygame.init()
    screen = pygame.display.set_mode((int(tcarre * 22 + 23), int(tcarre * 22 + 23)))
    font = pygame.font.Font(None, int(heightscreen*50))

    board = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])

    """def of the pieces"""
    piece1 = np.array([[0, 1, 0],
                       [1, 1, 1],
                       [0, 0, 0]])
    piece2 = np.array([[0, 0, 2],
                       [2, 2, 2],
                       [0, 0, 0]])
    piece3 = np.array([[3, 0, 0],
                       [3, 3, 3],
                       [0, 0, 0]])
    piece4 = np.array([[4, 4, 0],
                       [0, 4, 4],
                       [0, 0, 0]])
    piece5 = np.array([[0, 5, 5],
                       [5, 5, 0],
                       [0, 0, 0]])
    piece6 = np.array([[6, 6, 0],
                       [6, 6, 0],
                       [0, 0, 0]])
    piece7 = np.array([[7],
                       [7],
                       [7],
                       [7]])
    pieces = [piece1, piece2, piece3, piece4, piece5]

    nextpiece = random.randrange(1, 8)
    nextpiecehold = 0
    hold = 0
    hold2 = 0
    pressed = 0
    pressed2 = 0
    t = 0
    speed3 = 0
    speed = 100

    ligne = 0
    score = 0
    level = 1

    """def of the function that show the board"""
    def board1():
        # print(board)
        screen.fill([0, 0, 0])
        for a in range(0, 12):
            for j in range(0, 2):
                pygame.draw.rect(screen, (200, 200, 200), pygame.Rect((int(a * tcarre + a + 1)), int(j * 21 * tcarre + j * 21 + 1), int(tcarre), int(tcarre)))
        for a in range(0, 2):
            for j in range(1, 21):
                pygame.draw.rect(screen, (200, 200, 200), pygame.Rect((int(tcarre * a * 11 + a * 11 + 1)), int((j * tcarre + j + 1)), int(tcarre), int(tcarre)))
        for a in range(0, 10):
            for b in range(0, 20):
                pygame.draw.rect(screen, colors[abs(board[b, a])], pygame.Rect(int(a * tcarre + a + 2 + tcarre), int(b * tcarre + b + 2 + tcarre), int(tcarre), int(tcarre)))
        pygame.draw.rect(screen, (10, 10, 150), pygame.Rect(int(heightscreen*560), int(heightscreen*55), int(heightscreen*200), int(heightscreen*200)), int(heightscreen*6))

        """show the next piece"""
        screen.blit(font.render("Next:", True, (255, 0, 0)), (int(heightscreen*560), int(heightscreen*20)))
        if nextpiece != 7 and nextpiece != 6:
            for a in range(0, 2):
                for b in range(0, 3):
                    if pieces[nextpiece - 1][a, b] != 0:
                        pygame.draw.rect(screen, colors[nextpiece], pygame.Rect(int(heightscreen * 595 + (b * tcarre)+1), int(heightscreen * 105 + (a * tcarre)+1), int(tcarre), int(tcarre)))
        elif nextpiece == 6:
            for a in range(0, 2):
                for b in range(0, 2):
                    pygame.draw.rect(screen, colors[nextpiece], pygame.Rect(int(heightscreen * 617 + (b * tcarre)), int(heightscreen * 110 + (a * tcarre)), int(tcarre), int(tcarre)))
        else:
            for a in range(0, 4):
                pygame.draw.rect(screen, colors[nextpiece], pygame.Rect(int(heightscreen*640), int(heightscreen*(a * 40 + 78)), int(heightscreen*39), int(heightscreen*39)))
        pygame.draw.rect(screen, (10, 10, 150), pygame.Rect(int(heightscreen*560), int(heightscreen*310), int(heightscreen*200), int(heightscreen*200)), int(heightscreen*6))

        """show the piece hold"""
        screen.blit(font.render("hold:", True, (255, 0, 0)), (int(heightscreen*560), int(heightscreen*275)))
        if hold != 7 and hold != 6:
            for a in range(0, 2):
                for b in range(0, 3):
                    if pieces[hold - 1][a, b] != 0:
                        pygame.draw.rect(screen, colors[hold], pygame.Rect(int(heightscreen*(b * 45 + 595)), int(heightscreen*(a * 45 + 105+255)), int(heightscreen*44), int(heightscreen*44)))
        elif hold == 6:
            for a in range(0, 2):
                for b in range(0, 2):
                    pygame.draw.rect(screen, colors[hold], pygame.Rect(int(heightscreen*(b * 45 + 617)), int(heightscreen*(a *45+ 110+255)), int(heightscreen*44), int(heightscreen*44)))
        else:
            for a in range(0, 4):
                pygame.draw.rect(screen, colors[hold], pygame.Rect(int(heightscreen*640), int(heightscreen*(a * 40 + 78+255)), int(heightscreen*39), int(heightscreen*39)))

        """print scoreboard"""
        pygame.draw.rect(screen, (10, 10, 150), pygame.Rect(int(heightscreen*560), int(heightscreen*565), int(heightscreen*200), int(heightscreen*400)), int(heightscreen*6))
        screen.blit(font.render("score:", True, (255, 0, 0)), (int(heightscreen*590), int(heightscreen*595)))
        screen.blit(font.render(str(score), True, (255, 0, 255)), (int(heightscreen*590), int(heightscreen*645)))
        screen.blit(font.render("level:", True, (255, 0, 0)), (int(heightscreen*590), int(heightscreen*715)))
        screen.blit(font.render(str(level), True, (255, 0, 255)), (int(heightscreen*590), int(heightscreen*765)))
        screen.blit(font.render("lines:", True, (255, 0, 0)), (int(heightscreen*590), int(heightscreen*835)))
        screen.blit(font.render(str(ligne), True, (255, 0, 255)), (int(heightscreen*590), int(heightscreen*885)))
        pygame.draw.line(screen, (120, 0, 0), (int(1 + tcarre), int(3 + 3 * tcarre)), (int(11 * tcarre + 12), int(3 + 3 * tcarre)))

    def pause():
        if key[pygame.K_ESCAPE]:
            pressed = 1
            pause = 1
            while pause == 1:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return False
                if not key[pygame.K_ESCAPE]:
                    pressed = 0
                if key[pygame.K_ESCAPE] and pressed == 0:
                    pause = 0
            board1()
            pygame.display.flip()
        return True

    done = True
    while done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = False

        """set speed"""
        if level % 3 != 0:
            speed3 = 0
        if level % 3 == 0 and speed3 == 0:
            speed3 = 1
            speed = speed - speed/5

        key = pygame.key.get_pressed()

        if nextpiecehold == 0:
            piece = nextpiece
            nextpiece = random.randrange(1, 8)
        else:
            piece = nextpiecehold

        colors = [(20, 20, 20), (102, 0, 153), (237, 127, 16), (16, 52, 166), (220, 0, 0),
                                (0, 255, 0), (200, 200, 0), (0, 200, 200)]

        if piece == 1:
            piececelect = piece1
        elif piece == 2:
            piececelect = piece2
        elif piece == 3:
            piececelect = piece3
        elif piece == 4:
            piececelect = piece4
        elif piece == 5:
            piececelect = piece5
        elif piece == 6:
            piececelect = piece6
        else:
            piececelect = piece7

        if piece != 7:
            for a in range(0, 3):
                for b in range(0, 3):
                    if piececelect[a, b] > 0:
                        piececelect[a, b] -= piececelect[a, b]*2
        x = 5
        i = 0

        """movement of other piece"""
        done1 = True
        if piece == 7:
            done1 = False
        while done1:
            screen = pygame.display.set_mode((int(tcarre * 22 + 23), int(tcarre * 22 + 23)))
            for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
            key = pygame.key.get_pressed()

            """rotation"""
            if key[pygame.K_UP] and pressed == 0 and piece != 6:
                pressed = 1
                """if you're at the wall you don't have enough space so you have to move"""
                if x == 0:
                    done2 = 0
                    for a in range(0, 3):
                        for b in range(0, 3):
                            if piececelect[a, b] < 0:
                                if board[i + a - 1, x + b] > 0:
                                    done2 = 1
                    if x != 8 or piececelect[0, 2] + piececelect[1, 2] + piececelect[2, 2] == 0:
                        if x != 9 and done2 == 0:
                            pressed = 1
                            for a in range(0, 3):
                                for b in range(0, 3):
                                    if piececelect[a, b] != 0:
                                        board[a + i - 1, x + b - 1] = 0
                            x += 1
                            for a in range(0, 3):
                                for b in range(0, 3):
                                    if piececelect[a, b] != 0:
                                        board[a + i - 1, x + b - 1] = piececelect[a, b]
                if x == 9:
                    done2 = 0
                    for a in range(0, 3):
                        for b in range(0, 3):
                            if piececelect[a, b] < 0:
                                if board[i + a - 1, x + b - 2] > 0:
                                    done2 = 1
                    if x != 1 or piececelect[0, 0] + piececelect[1, 0] + piececelect[2, 0] == 0:
                        if x != 0 and done2 == 0:
                            pressed = 1
                            for a in range(0, 3):
                                for b in range(0, 3):
                                    if piececelect[a, b] != 0:
                                        board[a + i - 1, x + b - 1] = 0
                            x -= 1
                            for a in range(0, 3):
                                for b in range(0, 3):
                                    if piececelect[a, b] != 0:
                                        board[a + i - 1, x + b - 1] = piececelect[a, b]
                """rotation"""
                for a in range(0, 3):
                    for b in range(0, 3):
                        if piececelect[a, b] != 0:
                            board[a + i - 1, x + b - 1] = 0
                piececelect = np.rot90(piececelect, 3)
                for a in range(0, 3):
                    for b in range(0, 3):
                        if piececelect[a, b] != 0:
                            board[a + i - 1, x + b - 1] = piececelect[a, b]
            if key[pygame.K_DOWN]:
                if pressed2 == 0:
                    speed2 = speed
                    speed = speed / 8
                    pressed2 = 1
            if not key[pygame.K_DOWN] and pressed2 == 1:
                speed = speed2
                pressed2 = 0
                """move right/left"""
            if key[pygame.K_RIGHT] and pressed == 0:
                done2 = 0
                for a in range(0, 3):
                    for b in range(0, 3):
                        if piececelect[a, b] < 0:
                            if board[i + a - 1, x + b] > 0:
                                done2 = 1
                if x != 8 or piececelect[0, 2]+piececelect[1, 2]+piececelect[2, 2] == 0 :
                    if x != 9 and done2 == 0:
                        pressed = 1
                        for a in range(0, 3):
                            for b in range(0, 3):
                                if piececelect[a, b] != 0:
                                    board[a + i - 1, x + b - 1] = 0
                        x += 1
                        for a in range(0, 3):
                            for b in range(0, 3):
                                if piececelect[a, b] != 0:
                                    board[a + i - 1, x + b - 1] = piececelect[a, b]
            if key[pygame.K_LEFT] and pressed == 0:
                done2 = 0
                for a in range(0, 3):
                    for b in range(0, 3):
                        if piececelect[a, b] < 0:
                            if board[i + a - 1, x + b - 2] > 0:
                                done2 = 1
                if x != 1 or piececelect[0, 0]+piececelect[1, 0]+piececelect[2, 0] == 0:
                    if x != 0 and done2 == 0:
                        pressed = 1
                        for a in range(0, 3):
                            for b in range(0, 3):
                                if piececelect[a, b] != 0:
                                    board[a + i - 1, x + b - 1] = 0
                        x -= 1
                        for a in range(0, 3):
                            for b in range(0, 3):
                                if piececelect[a, b] != 0:
                                    board[a + i - 1, x + b - 1] = piececelect[a, b]
            """pressed?"""
            if not key[pygame.K_LEFT] and not key[pygame.K_RIGHT] and not key[pygame.K_UP]:
                pressed = 0
            """collision?"""
            for a in range(0, 3):
                for b in range(0, 3):
                    if piececelect[a, b] < 0:
                        if board[i + a, x+b-1] > 0:
                            done1 = False
            """hold"""
            nextpiecehold = 0
            if key[pygame.K_h] and hold2 > 0:
                if hold == 0:
                    print("test")
                    hold = piece  # wich piece to hold
                    done1 = False
                    nextpiecehold = nextpiece
                    hold2 = -1
                    for a in range(0, 3):
                        for b in range(0, 3):
                            if piececelect[a, b] != 0:
                                board[a + i - 1, x + b - 1] = 0
                if hold != 0:

                    nextpiecehold = hold
                    hold = piece
                    done1 = False
                    hold2 = -1

                    for a in range(0, 3):
                        for b in range(0, 3):
                            if piececelect[a, b] != 0:
                                board[a + i - 1, x + b - 1] = 0

            """chronometer"""
            t = t + 1

            if t > speed:
                t = 0
                c = piececelect[1, 1]
                if pressed2 == 1:
                    score += 1
                for a in range(0, 3):
                    for b in range(0, 3):
                        if piececelect[a, b] != 0:
                            board[a + i - 1, x + b - 1] = 0
                i += 1
                for a in range(0, 3):
                    for b in range(0, 3):
                        if piececelect[a, b] != 0:
                            board[a + i - 1, x + b - 1] = c

                board1()
                pygame.display.flip()
            # I don't know why or how but this make the code work
            board1()
            pygame.display.flip()

        for a in range(0, 3):
            for b in range(0, 3):
                if board[i+a-1, x+b-1] < 0:
                    board[i + a - 1, x + b - 1] = -c

        rotation = 0

        """movement piece 7"""
        done1 = True
        if piece == 7:
            screen = pygame.display.set_mode((int(tcarre * 22 + 23), int(tcarre * 22 + 23)))
            i -= 2
            while done1:
                screen = pygame.display.set_mode((int(tcarre * 22 + 23), int(tcarre * 22 + 23)))

                key = pygame.key.get_pressed()
                if key[pygame.K_UP] and pressed == 0:
                    pressed = 1
                    if rotation == 0:
                        for a in range(0, 4):
                            board[a + i - 2, x] = 0
                        rotation = 1
                        piececelect = np.rot90(piececelect, 1)
                        for a in range(0, 4):
                            board[i, x + a - 2] = 7
                    else:
                        for a in range(0, 4):
                            board[i, x + a - 2] = 0
                        rotation = 0
                        piececelect = np.rot90(piececelect, 3)
                        for a in range(0, 4):
                            board[i + a - 2, x] = 7
                if key[pygame.K_RIGHT] and pressed == 0 and i != -2 and i != -1 or rotation == 1:
                    if x != 8 and rotation == 1:
                        pressed = 1
                        board[i, x + 2] = 7
                        board[i, x - 2] = 0
                        x += 1
                    elif x != 9 and rotation == 0:
                        pressed = 1
                        for a in range(0, 4):
                            board[i + a - 2, x] = 0
                            board[i + a - 2, x + 1] = 7
                        x = x + 1
                if key[pygame.K_DOWN]:
                    if pressed2 == 0:
                        speed2 = speed
                        speed = speed / 8
                        pressed2 = 1
                if not key[pygame.K_DOWN] and pressed2 == 1:
                    speed = speed2
                    pressed2 = 0
                if key[pygame.K_LEFT] and pressed == 0 and i != -2 and i != -1 or rotation == 1:
                    if x != 2 and rotation == 1:
                        if x != 1:
                            pressed = 1
                            board[i, x - 3] = 7
                            board[i, x + 1] = 0
                            x -= 1
                    elif x != 0 and rotation == 0:
                        pressed = 1
                        for a in range(0, 4):
                            board[i + a - 2, x] = 0
                            board[i + a - 2, x - 1] = 7
                        x = x - 1

                nextpiecehold = 0
                if key[pygame.K_h] and hold2 > 0:
                    if hold == 0:
                        hold = piece  # wich piece to hold
                        done1 = False
                        hold2 = -1
                    if hold != 0:
                        nextpiecehold = hold
                        hold = piece
                        done1 = False
                        hold2 = -1
                    if rotation == 0:
                        for a in range(0, 4):
                            board[i + a - 2, x] = 0
                    else:
                        for a in range(0, 4):
                            board[i, x+a-2] = 0

                if i == 5:
                    for a in range(0, 2):
                        for b in range(0, 10):
                            board[a+20, b] = 1

                if not key[pygame.K_LEFT] and not key[pygame.K_RIGHT] and not key[pygame.K_UP]:
                    pressed = 0
                if rotation == 0:
                    if board[i + 2, x] != 0:
                        done1 = False
                if rotation == 1:
                    for b in range(0, 4):
                        if board[i + 1, x + b - 2] > 0:
                            done1 = False

                t = t + 1
                if t > speed:
                    t = 0
                    if pressed2 == 1:
                        score += 1

                    if rotation == 0:
                        if i > 0:
                            board[i - 2, x] = 0
                        i += 1
                        board[i + 1, x] = 7

                    if rotation == 1:
                        for a in range(0, 4):
                            board[i, x + a - 2] = 0
                            board[i + 1, x + a - 2] = 7
                        i += 1

                    board1()
                    pygame.display.flip()
                board1()
                pygame.display.flip()
            board1()
            pygame.display.flip()

        """finish line?"""
        lignes = []
        for a in range(0, 20):
            test = 1
            for b in range(0, 10):
                test = test * board[a, b]
            if test != 0:
                lignes.append(a)
                ligne += 1
        if lignes:
            for a in range(0, len(lignes)):
                if lignes[a] != 0:
                    for b in range(0, lignes[a]-1):
                        for c in range(0, 10):
                            board[lignes[a]-b, c] = board[lignes[a]-b-1, c]
                for b in range(0, 10):
                    board[0, b] = 0

        """lose?"""
        for a in range(0, 10):
            if board[1, a] > 0:
                done = False

        """score"""
        level = 1 + ligne//10
        if len(lignes) == 1:
            score += 100*(level+1)
        elif len(lignes) == 2:
            score += 300*(level+1)
        elif len(lignes) == 3:
            score += 500*(level+1)
        elif len(lignes) == 4:
            score += 800*(level+1)

        hold2 += 1
        board1()
        #done = pause()
        pygame.display.flip()

tetris()





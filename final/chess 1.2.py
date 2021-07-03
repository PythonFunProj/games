import pygame
import numpy as np

chess = np.array([["r0", "n", "b", "q", "k0", "b", "n", "r1"],
                 ["p", "p", "p", "p", "p", "p", "p", "p"],
                 ["0", "0", "0", "0", "0", "0", "0", "0"],
                 ["0", "0", "0", "0", "0", "0", "0", "0"],
                 ["0", "0", "0", "0", "0", "0", "0", "0"],
                 ["0", "0", "0", "0", "0", "0", "0", "0"],
                 ["P", "P", "P", "P", "P", "P", "P", "P"],
                 ["R2", "N", "B", "K2", "Q", "B", "N", "R3"]])

image1 = pygame.image.load(r'WPawn.png')
image1 = pygame.transform.scale(image1, (100, 100))
image2 = pygame.image.load(r'WQueen.png')
image2 = pygame.transform.scale(image2, (100, 100))
image3 = pygame.image.load(r'WKnight.png')
image3 = pygame.transform.scale(image3, (100, 100))
image4 = pygame.image.load(r'WKing.png')
image4 = pygame.transform.scale(image4, (100, 100))
image5 = pygame.image.load(r'WTower.png')
image5 = pygame.transform.scale(image5, (100, 100))
image6 = pygame.image.load(r'WBishop.png')
image6 = pygame.transform.scale(image6, (100, 100))
image7 = pygame.image.load(r'BPawn.png')
image7 = pygame.transform.scale(image7, (100, 100))
image8 = pygame.image.load(r'BQueen.png')
image8 = pygame.transform.scale(image8, (100, 100))
image9 = pygame.image.load(r'BKnight.png')
image9 = pygame.transform.scale(image9, (100, 100))
image10 = pygame.image.load(r'BKing.png')
image10 = pygame.transform.scale(image10, (100, 100))
image11 = pygame.image.load(r'BRook.png')
image11 = pygame.transform.scale(image11, (100, 100))
image12 = pygame.image.load(r'BBishop.png')
image12 = pygame.transform.scale(image12, (100, 100))


pygame.init()
screen = pygame.display.set_mode((800, 800))
font = pygame.font.SysFont("calibri", 72)
pygame.display.set_caption("chess")


pionn = ["R", "N", "B", "Q", "K", "P"]
pionb = ["r", "n", "b", "q", "k", "p"]
enemy = [pionn, None, pionb]

pion_blanc = [image5, image3, image6, image2, image4, image1]
pion_noir = [image11, image9, image12, image8, image10, image7]


def chess_board(tour, chess, movement, r, passant):
    for i in range(0, 5):
        for j in range(0, 5):
            pygame.draw.rect(screen, (225, 195, 154), pygame.Rect(200*i, 200*j, 100, 100))
            pygame.draw.rect(screen, (225, 195, 154), pygame.Rect(200*i+100, 200*j+100, 100, 100))
            pygame.draw.rect(screen, (133, 100, 77), pygame.Rect(100+200*i, 200*j, 100, 100))
            pygame.draw.rect(screen, (133, 100, 77), pygame.Rect(200*i, 200*j+100, 100, 100))
    for i in range(0, 7):
        pygame.draw.rect(screen, (255, 215, 0), pygame.Rect(100 + 100 * i, 0, 1.5, 800))
        pygame.draw.rect(screen, (255, 215, 0), pygame.Rect(0, 100 + 100 * i, 800, 1.5))

    if tour == -1:
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(1, 1, 798, 798), 3)
    else:
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(1, 1, 798, 798), 3)

    for j in range(0, 8):
        for i in range(0, 8):
            if chess[j, i][0] != "0":
                if chess[j, i][0] in pionn:
                    screen.blit(pion_noir[pionn.index(chess[j, i][0])], (i * 100, j * 100))
                else:
                    screen.blit(pion_blanc[pionb.index(chess[j, i][0])], (i * 100, j * 100))

    for square in movement:
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(square[1] * 100 + 2, square[0]*100+2, 96, 96), 3)

    for square in r:
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(square[1] * 100 + 2, square[0]*100+2, 96, 96), 3)

    if passant[0] > -1:
        print(passant)
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(passant[1] * 100 + 2, passant[0] * 100 + 2, 96, 96), 3)




    pygame.display.flip()


def pawn(x, y, chess, tour, p):
    movement = []
    passant = -1, -1

    if chess[y-1*tour, x] == "0" and 0 <= y-1*tour < 8:
        movement.append([y-1*tour, x])
        if -1 < y - 2 * tour < 8 and chess[y - 2 * tour, x] == "0" and y == 1+2.5*(tour+1):
            movement.append([y - 2 * tour, x])

    for i in range(-1, 3, 2):
        if -1 < x+i < 8 and chess[y-tour, x+i] in enemy[tour + 1]:
            movement.append([y-tour, x+i])

    # en passant:
    if p > -1 and y == 3+0.5*(-1*tour+1):
        if p == x + 1 and chess[y-tour, p] == '0':
            passant = y-tour, p
        if p == x - 1 and chess[y-tour, p] == '0':
            passant = y-tour, p

    print(passant)

    return movement, passant


def rook(x, y, chess, tour):
    movement = []
    for i in range(-1, 2, 2):
        a = i
        while 0 <= a + y < 8:
            if chess[y+a, x] == "0":
                movement.append([y+a, x])
            elif chess[y+a, x] in enemy[tour + 1]:
                movement.append([y+a, x])
                break
            else:
                break
            a += i

    for i in range(-1, 2, 2):
        a = i
        while 0 <= a + x < 8:
            if chess[y, x + a] == "0":
                movement.append([y, x + a])
            elif chess[y, x + a] in enemy[tour + 1]:
                movement.append([y, x + a])
                break
            else:
                break
            a += i

    return movement


def bishop(x, y, chess, tour):
    movement = []
    for i in range(-1, 2, 2):
        for j in range(-1, 2, 2):
            a = i
            b = j
            while 0 <= a + x < 8 and 0 <= b + y < 8:
                if chess[y + b, x + a] == "0":
                    movement.append([y + b, x + a])
                elif chess[y + b, x + a] in enemy[tour + 1]:
                    movement.append([y + b, x + a])
                    break
                else:
                    break
                a += i
                b += j
    return movement


def knight(x, y, chess, tour):
    movement = []
    for i in range(-1, 2, 2):
        for j in range(-1, 2, 2):
            if 0 <= y + 2*i < 8 and 0 <= x + j < 8 and chess[y + 2*i, x + j] == "0":
                movement.append([y + 2*i, x + j])
            elif 0 <= y + 2*i < 8 and 0 <= x + j < 8 and chess[y + 2*i, x + j] in enemy[tour + 1]:
                movement.append([y + 2*i, x + j])

    for i in range(-1, 2, 2):
        for j in range(-1, 2, 2):
            if 0 <= y + i < 8 and 0 <= x + 2 * j < 8 and chess[y + i, x + 2 * j] == "0":
                movement.append([y + i, x + 2*j])
            elif 0 <= y + i < 8 and 0 <= x + 2 * j < 8 and chess[y + i, x + 2*j] in enemy[tour + 1]:
                movement.append([y + i, x + 2*j])

    return movement


def king(x, y, chess, tour, roque):
    movement = []
    R = []
    for i in range(3):
        for j in range(3):
            if y + i - 1 < 8 and  x + j - 1 < 8:
                if chess[y + i - 1, x + j - 1] == "0":
                    movement.append([y + i - 1, x + j - 1])
                elif chess[y + i - 1, x + j - 1] in enemy[tour + 1]:
                    movement.append([y + i - 1, x + j - 1])

        # roque
        if roque[int(chess[y, x][1])] == 2:
            b = True
            for a in chess[int(int(chess[y, x][1]) * 3.5), 1: int(4 - 0.5*int(chess[y, x][1]))]:
                if a != '0':
                    b = False
            if b:
                R.append([y, x - 2])

        if roque[int(chess[y, x][1])+1] == 2:
            b = True
            for a in chess[int(int(chess[y, x][1])*3.5), int(5 - 0.5*int(chess[y, x][1])): 7]:
                if a != '0':
                    b = False
            if b:
                R.append([y, x + 2])
        print(roque)

    return movement, R


def queen(x, y, chess, tour):
    movement = bishop(x, y, chess, tour) + rook(x, y, chess, tour)
    return movement


def main(chess):
    roque = [2, 2, 2, 2]
    en_passant = -1
    passant = -1, 0

    # who play?
    tour = -1

    # possible movement
    movement = []
    r = []

    # mouse position
    x = y = 0
    select = None

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                print("''''''''''''''''''''''")
                x //= 100
                y //= 100
                print(x, y, passant)
                if chess[y, x][0] in enemy[tour * -1 + 1]:
                    select = y, x

                    if str(chess[y, x][0]).lower() == 'r':
                        movement = rook(x, y, chess, tour)

                    elif str(chess[y, x]).lower() == 'n':
                        movement = knight(x, y, chess, tour)

                    elif str(chess[y, x]).lower() == 'b':
                        movement = bishop(x, y, chess, tour)

                    elif str(chess[y, x]).lower() == 'q':
                        movement = queen(x, y, chess, tour)

                    elif str(chess[y, x][0]).lower() == 'k':
                        movement, r = king(x, y, chess, tour, roque)

                    elif str(chess[y, x]).lower() == 'p':
                        movement, passant = pawn(x, y, chess, tour, en_passant)

                    print(movement)

                elif [y, x] in movement or [y, x] in r or (y == passant[0] and x == passant[1]):
                    print("test")
                    # roque
                    if chess[select][0].lower == 'r':
                        roque[chess[select][1]] = '0'

                    if chess[select][0].lower == 'k':
                        if roque[chess[select][1]] == '0':
                            roque[0], roque[1] = 0, 0
                        else:
                            roque[2], roque[3] = 0, 0

                    # en passant
                    if str(chess[select]).lower() == 'p' and abs(select[0] - y) == 2:
                        en_passant = x
                    else:
                        en_passant = -1

                    # final movement
                    if str(chess[select]).lower() == 'p' and (y == 0 or y == 7):
                        if chess[select] == 'P':
                            chess[select] = 'Q'
                        else:
                            chess[select] = 'q'

                    chess[y, x] = chess[select]
                    chess[select] = '0'
                    tour *= -1
                    movement = []
                    if passant[0] > -1:
                        chess[passant[0]-tour, passant[1]] = '0'
                        passant = -1, 0


                    # roque
                    if r:
                        if x > 4:
                            chess[y, 5-y//7] = chess[y, 7]
                            chess[y, 7] = '0'
                        else:
                            chess[y, 3 - y // 7] = chess[y, 0]
                            chess[y, 0] = '0'
                        r = []

        # draw board
        chess_board(tour, chess, movement, r, passant)

        x, y = pygame.mouse.get_pos()


if __name__ == '__main__':
    main(chess)

import pygame
import numpy as np
import time
chessb = np.array([["r", "n", "b", "q", "k", "b", "n", "r"],
                   ["p", "p", "p", "p", "p", "p", "p", "p"],
                   ["0", "0", "0", "0", "0", "0", "0", "0"],
                   ["0", "0", "0", "0", "0", "0", "0", "0"],
                   ["0", "0", "0", "0", "0", "0", "0", "0"],
                   ["0", "0", "0", "0", "0", "0", "0", "0"],
                   ["P", "P", "P", "P", "P", "P", "P", "P"],
                   ["R", "N", "B", "Q", "K", "B", "N", "R"]])
print(chessb)
pygame.init()
screen = pygame.display.set_mode((800, 800))
screen.fill([0, 0, 0])
done = False
font = pygame.font.SysFont("calibri", 72)
pionn = ["R", "N", "B", "Q", "K", "B", "N", "R", "P"]
pionb = ["r", "n", "b", "q", "k", "b", "n", "r", "p"]
tour = 0
bool1 = 0
pselect = "0"
listx = []
listy = []
pmn = pmb = []
ya = xa = 0
def chessbord():
    for i in range(0, 5):
        for j in range(0, 5):
            pygame.draw.rect(screen, (225, 195, 154), pygame.Rect(200*i, 200*j, 100, 100))
    for i in range(0, 5):
        for j in range(0, 5):
            pygame.draw.rect(screen, (225, 195, 154), pygame.Rect(200*i+100, 200*j+100, 100, 100))
    for i in range(0, 5):
        for j in range(0, 5):
            pygame.draw.rect(screen, (133, 100, 77), pygame.Rect(100+200*i, 200*j, 100, 100))
    for i in range(0, 5):
        for j in range(0, 5):
            pygame.draw.rect(screen, (133, 100, 77), pygame.Rect(200*i, 200*j+100, 100, 100))
    for i in range(0, 7):
        pygame.draw.rect(screen, (255, 215, 0), pygame.Rect(0, 100 + 100 * i, 800, 1.5))
    for i in range(0, 7):
        pygame.draw.rect(screen, (255, 215, 0), pygame.Rect(100 + 100 * i, 0, 1.5, 800))
    if tour == 0:
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(1, 1, 798, 798), 3)
    else:
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(1, 1, 798, 798), 3)


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    chessbord()
    for j in range(0, 8):
        for i in range(0, 8):
            if chessb[j, i] == "0":
                pass
            else:
                if chessb[j, i] in pionn:
                    text = font.render(chessb[j, i], True, (0, 0, 0))
                    screen.blit(text, (30 + i * 100, 15 + j * 100))
                else:
                    text = font.render(chessb[j, i], True, (255, 255, 255))
                    screen.blit(text, (30 + i * 100, 15 + j * 100))
    x, y = pygame.mouse.get_pos()
    x2, y2 = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN and x > 800:
        if tour == 0:
            tour = 1
        else:
            tour = 0
        time.sleep(0.5)
    if pselect in pionb and tour == 0:
        if pselect != "0" and pselect not in pionn:
            if event.type == pygame.MOUSEBUTTONDOWN and x < 800:
                xb = x2 // 100
                yb = y2 // 100
                for i in range(0, len(listx)):
                    if len(listx) != 0:
                        if xb == listx[i] and yb == listy[i]:
                            if chessb[yb, xb] in pionn:
                                pmn.append(chessb[yb, xb])
                            chessb[yb, xb] = chessb[ya, xa]
                            chessb[ya, xa] = "0"
                            listx = listy = []
                            if pselect == "p" and ya == 6:
                                chessb[yb, xb] = "q"
                            tour = 1
                pselect = "0"
        if event.type == pygame.MOUSEBUTTONDOWN and x < 800:
            pselect = chessb[y // 100, x // 100]
            ya = y // 100
            xa = x // 100
    if event.type == pygame.MOUSEBUTTONDOWN and tour == 0 and x < 800:
        pselect = chessb[y//100, x//100]
        ya = y//100
        xa = x//100

        if pselect == "p":
            listx = []
            listy = []
            if ya + 1 != 8:
                if chessb[ya + 1, xa] == "0":
                    listx.append(xa)
                    listy.append(ya + 1)
                    if ya + 2 != 8 and ya == 1:
                        if chessb[ya+2, xa] == "0":
                            listx.append(xa)
                            listy.append(ya + 2)
            if xa + 1 != 8 and ya + 1 != 8:
                if chessb[ya+1, xa+1] in pionn:
                    listx.append(xa + 1)
                    listy.append(ya + 1)
            if ya + 1 != 8:
                if chessb[ya+1, xa-1] in pionn:
                    listx.append(xa - 1)
                    listy.append(ya + 1)
        elif pselect == "r":
            listx = []
            listy = []
            a = xa + 1
            while a < 8:
                if chessb[ya, a] == "0":
                    listx.append(a)
                    listy.append(ya)
                else:
                    if chessb[ya, a] in pionn:
                        listx.append(a)
                        listy.append(ya)
                    a = 9
                a += 1
            a = xa - 1
            while a > -1:
                if chessb[ya, a] == "0":
                    listx.append(a)
                    listy.append(ya)
                else:
                    if chessb[ya, a] in pionn:
                        listx.append(a)
                        listy.append(ya)
                        a = -2
                    a = -2
                a = a - 1
            a = ya - 1
            while a > -1:
                if chessb[a, xa] == "0":
                    listx.append(xa)
                    listy.append(a)
                else:
                    if chessb[a, xa] in pionn:
                        listx.append(xa)
                        listy.append(a)
                        a = -2
                    a = -2
                a = a - 1
            a = ya + 1
            while a < 8:
                if chessb[a, xa] == "0":
                    listx.append(xa)
                    listy.append(a)
                else:
                    if chessb[a, xa] in pionn:
                        listx.append(xa)
                        listy.append(a)
                        a = 8
                    a = 8
                a += 1
        elif pselect == "b":
            listx = []
            listy = []
            a = xa
            b = ya
            while a > 0 and b > 0:
                if chessb[b - 1, a - 1] == "0":
                    listx.append(a - 1)
                    listy.append(b - 1)
                elif chessb[b - 1, a - 1] in pionn:
                    listx.append(a - 1)
                    listy.append(b - 1)
                    a = b = -1
                else:
                    a = -1
                a = a - 1
                b = b - 1
            a = xa
            b = ya
            while a < 7 and b > 0:
                if chessb[b - 1, a + 1] == "0":
                    listx.append(a + 1)
                    listy.append(b - 1)
                elif chessb[b - 1, a + 1] in pionn:
                    listx.append(a + 1)
                    listy.append(b - 1)
                    a = 8
                    b = -1
                else:
                    a = 8
                a = a + 1
                b = b - 1
            a = xa
            b = ya
            while a < 7 and b < 7:
                if chessb[b + 1, a + 1] == "0":
                    listx.append(a + 1)
                    listy.append(b + 1)
                elif chessb[b + 1, a + 1] in pionn:
                    listx.append(a + 1)
                    listy.append(b + 1)
                    a = b = 10
                else:
                    a = b = 10
                a = a + 1
                b = b + 1
            a = xa
            b = ya
            while a > 0 and b < 7:
                if chessb[b + 1, a - 1] == "0":
                    listx.append(a - 1)
                    listy.append(b + 1)
                elif chessb[b + 1, a - 1] in pionn:
                    listx.append(a - 1)
                    listy.append(b + 1)
                    a = -10
                    b = 10
                else:
                    a = -10
                a = a - 1
                b = b + 1
        elif pselect == "n":
            listx = []
            listy = []
            if xa + 2 < 8 and ya < 7:
                if chessb[ya + 1, xa + 2] == "0" or chessb[ya + 1, xa + 2] in pionn:
                    listx.append(xa + 2)
                    listy.append(ya + 1)
            if xa + 2 < 8:
                if chessb[ya-1, xa + 2] == "0" or chessb[ya-1, xa + 2] in pionn:
                    listx.append(xa + 2)
                    listy.append(ya - 1)
            if ya + 1 < 8:
                if chessb[ya+1, xa-2] == "0" or chessb[ya+1, xa-2] in pionn:
                    listx.append(xa-2)
                    listy.append(ya+1)
            if chessb[ya-1, xa-2] == "0" or chessb[ya-1, xa-2] in pionn:
                listx.append(xa - 2)
                listy.append(ya - 1)
            if xa + 1 < 8 and ya + 2 < 8:
                if chessb[ya+2, xa+1] == "0" or chessb[ya+2, xa+1] in pionn:
                    listx.append(xa + 1)
                    listy.append(ya + 2)
            if xa + 1 < 8:
                if chessb[ya-2, xa+1] == "0" or chessb[ya-2, xa+1] in pionn:
                    listx.append(xa + 1)
                    listy.append(ya - 2)
            if ya + 2 < 8:
                if chessb[ya + 2, xa - 1] == "0" or chessb[ya + 2, xa - 1] in pionn:
                    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(xa * 100 - 98, ya * 100 + 202, 96, 96), 3)
                    listx.append(xa - 1)
                    listy.append(ya + 2)
            if chessb[ya-2, xa-1] == "0" or chessb[ya-2, xa-1] in pionn:
                listx.append(xa - 1)
                listy.append(ya - 2)
        elif pselect == "k":
            listx = []
            listy = []
            if xa < 7:
                if chessb[ya, xa + 1] == "0" or chessb[ya, xa + 1] in pionn:
                    listx.append(xa + 1)
                    listy.append(ya)
            if xa < 7 and ya < 7:
                if chessb[ya + 1, xa + 1] == "0" or chessb[ya + 1, xa + 1] in pionn:
                    listx.append(xa + 1)
                    listy.append(ya + 1)
            if xa < 7:
                if chessb[ya - 1, xa + 1] == "0" or chessb[ya - 1, xa + 1] in pionn:
                    listx.append(xa + 1)
                    listy.append(ya - 1)
            if chessb[ya - 1, xa] == "0" or chessb[ya - 1, xa] in pionn:
                listx.append(xa)
                listy.append(ya - 1)
            if ya < 7:
                if chessb[ya + 1, xa] == "0" or chessb[ya + 1, xa] in pionn:
                    listx.append(xa)
                    listy.append(ya+1)
            if chessb[ya - 1, xa - 1] == "0" or chessb[ya - 1, xa - 1] in pionn:
                listx.append(xa - 1)
                listy.append(ya - 1)
            if ya < 7:
                if chessb[ya + 1, xa - 1] == "0" or chessb[ya + 1, xa - 1] in pionn:
                    listx.append(xa - 1)
                    listy.append(ya + 1)
            if chessb[ya, xa - 1] == "0" or chessb[ya, xa - 1] in pionn:
                listx.append(xa - 1)
                listy.append(ya)
        elif pselect == "q":
            listx = []
            listy = []
            a = xa + 1
            while a < 8:
                if chessb[ya, a] == "0":
                    listx.append(a)
                    listy.append(ya)
                else:
                    if chessb[ya, a] in pionn:
                        listx.append(a)
                        listy.append(ya)
                    a = 9
                a += 1
            a = xa - 1
            while a > -1:
                if chessb[ya, a] == "0":
                    listx.append(a)
                    listy.append(ya)
                else:
                    if chessb[ya, a] in pionn:
                        listx.append(a)
                        listy.append(ya)
                        a = -2
                    a = -2
                a = a - 1
            a = ya - 1
            while a > -1:
                if chessb[a, xa] == "0":
                    listx.append(xa)
                    listy.append(a)
                else:
                    if chessb[a, xa] in pionn:
                        listx.append(xa)
                        listy.append(a)
                        a = -2
                    a = -2
                a = a - 1
            a = ya + 1
            while a < 8:
                if chessb[a, xa] == "0":
                    listx.append(xa)
                    listy.append(a)
                else:
                    if chessb[a, xa] in pionn:
                        listx.append(xa)
                        listy.append(a)
                        a = 8
                    a = 8
                a += 1
            a = xa
            b = ya
            while a > 0 and b > 0:
                if chessb[b - 1, a - 1] == "0":
                    listx.append(a - 1)
                    listy.append(b - 1)
                elif chessb[b - 1, a - 1] in pionn:
                    listx.append(a - 1)
                    listy.append(b - 1)
                    a = b = -1
                else:
                    a = -1
                a = a - 1
                b = b - 1
            a = xa
            b = ya
            while a < 7 and b > 0:
                if chessb[b - 1, a + 1] == "0":
                    listx.append(a + 1)
                    listy.append(b - 1)
                elif chessb[b - 1, a + 1] in pionn:
                    listx.append(a + 1)
                    listy.append(b - 1)
                    a = 8
                    b = -1
                else:
                    a = 8
                a = a + 1
                b = b - 1
            a = xa
            b = ya
            while a < 7 and b < 7:
                if chessb[b + 1, a + 1] == "0":
                    listx.append(a + 1)
                    listy.append(b + 1)
                elif chessb[b + 1, a + 1] in pionn:
                    listx.append(a + 1)
                    listy.append(b + 1)
                    a = b = 10
                else:
                    a = b = 10
                a = a + 1
                b = b + 1
            a = xa
            b = ya
            while a > 0 and b < 7:
                if chessb[b + 1, a - 1] == "0":
                    listx.append(a - 1)
                    listy.append(b + 1)
                elif chessb[b + 1, a - 1] in pionn:
                    listx.append(a - 1)
                    listy.append(b + 1)
                    a = -10
                    b = 10
                else:
                    a = -10
                a = a - 1
                b = b + 1
    if pselect in pionn and tour == 1:
        if pselect != "0" and pselect not in pionb:
            if event.type == pygame.MOUSEBUTTONDOWN:
                xb = x2 // 100
                yb = y2 // 100
                for i in range(0, len(listx)):
                    if len(listx) != 0:
                        if xb == listx[i] and yb == listy[i]:
                            if chessb[yb, xb] in pionb:
                                pmb.append(chessb[yb, xb])
                            chessb[yb, xb] = chessb[ya, xa]
                            chessb[ya, xa] = "0"
                            listx = listy = []
                            if pselect == "P" and ya == 1:
                                chessb[yb, xb] = "Q"
                            tour = 0
                pselect = "0"
        if event.type == pygame.MOUSEBUTTONDOWN and x < 800:
            pselect = chessb[y // 100, x // 100]
            ya = y // 100
            xa = x // 100
    if event.type == pygame.MOUSEBUTTONDOWN and tour == 1 and x < 800:
        pselect = chessb[y//100, x//100]
        ya = y//100
        xa = x//100

        if pselect == "P":
            listx = []
            listy = []
            if ya + 1 != 8:
                if chessb[ya - 1, xa] == "0":
                    listx.append(xa)
                    listy.append(ya - 1)
                    if ya - 2 != 8 and ya == 6:
                        if chessb[ya-2, xa] == "0":
                            listx.append(xa)
                            listy.append(ya - 2)
            if xa + 1 != 8 and ya + 1 != 8:
                if chessb[ya-1, xa+1] in pionb:
                    listx.append(xa + 1)
                    listy.append(ya - 1)
            if ya + 1 != 8:
                if chessb[ya-1, xa-1] in pionb:
                    listx.append(xa - 1)
                    listy.append(ya - 1)
        elif pselect == "R":
            listx = []
            listy = []
            a = xa + 1
            while a < 8:
                if chessb[ya, a] == "0":
                    listx.append(a)
                    listy.append(ya)
                else:
                    if chessb[ya, a] in pionb:
                        listx.append(a)
                        listy.append(ya)
                    a = 9
                a += 1
            a = xa - 1
            while a > -1:
                if chessb[ya, a] == "0":
                    listx.append(a)
                    listy.append(ya)
                else:
                    if chessb[ya, a] in pionb:
                        listx.append(a)
                        listy.append(ya)
                        a = -2
                    a = -2
                a = a - 1
            a = ya - 1
            while a > -1:
                if chessb[a, xa] == "0":
                    listx.append(xa)
                    listy.append(a)
                else:
                    if chessb[a, xa] in pionb:
                        listx.append(xa)
                        listy.append(a)
                        a = -2
                    a = -2
                a = a - 1
            a = ya + 1
            while a < 8:
                if chessb[a, xa] == "0":
                    listx.append(xa)
                    listy.append(a)
                else:
                    if chessb[a, xa] in pionb:
                        listx.append(xa)
                        listy.append(a)
                        a = 8
                    a = 8
                a += 1
        elif pselect == "B":
            listx = []
            listy = []
            a = xa
            b = ya
            while a > 0 and b > 0:
                if chessb[b - 1, a - 1] == "0":
                    listx.append(a - 1)
                    listy.append(b - 1)
                elif chessb[b - 1, a - 1] in pionb:
                    listx.append(a - 1)
                    listy.append(b - 1)
                    a = b = -1
                else:
                    a = -1
                a = a - 1
                b = b - 1
            a = xa
            b = ya
            while a < 7 and b > 0:
                if chessb[b - 1, a + 1] == "0":
                    listx.append(a + 1)
                    listy.append(b - 1)
                elif chessb[b - 1, a + 1] in pionb:
                    listx.append(a + 1)
                    listy.append(b - 1)
                    a = 8
                    b = -1
                else:
                    a = 8
                a = a + 1
                b = b - 1
            a = xa
            b = ya
            while a < 7 and b < 7:
                if chessb[b + 1, a + 1] == "0":
                    listx.append(a + 1)
                    listy.append(b + 1)
                elif chessb[b + 1, a + 1] in pionb:
                    listx.append(a + 1)
                    listy.append(b + 1)
                    a = b = 10
                else:
                    a = b = 10
                a = a + 1
                b = b + 1
            a = xa
            b = ya
            while a > 0 and b < 7:
                if chessb[b + 1, a - 1] == "0":
                    listx.append(a - 1)
                    listy.append(b + 1)
                elif chessb[b + 1, a - 1] in pionb:
                    listx.append(a - 1)
                    listy.append(b + 1)
                    a = -10
                    b = 10
                else:
                    a = -10
                a = a - 1
                b = b + 1
        elif pselect == "N":
            listx = []
            listy = []
            if xa + 2 < 8 and ya < 7:
                if chessb[ya + 1, xa + 2] == "0" or chessb[ya + 1, xa + 2] in pionb:
                    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(xa*100 + 202, ya*100 + 102, 96, 96), 3)
                    listx.append(xa + 2)
                    listy.append(ya + 1)
            if xa + 2 < 8 and ya - 1 < 8:
                if chessb[ya-1, xa + 2] == "0" or chessb[ya-1, xa + 2] in pionb:
                    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(xa*100 + 202, ya*100 - 98, 96, 96), 3)
                    listx.append(xa + 2)
                    listy.append(ya - 1)
            if xa - 2 < 8 and ya + 1 < 8:
                if chessb[ya+1, xa-2] == "0" or chessb[ya+1, xa-2] in pionb:
                    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(xa*100 - 198, ya*100 + 102, 96, 96), 3)
                    listx.append(xa-2)
                    listy.append(ya+1)
            if xa - 2 < 8 and ya - 1 < 8:
                if chessb[ya-1, xa-2] == "0" or chessb[ya-1, xa-2] in pionb:
                    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(xa * 100 - 198, ya * 100 - 98, 96, 96), 3)
                    listx.append(xa - 2)
                    listy.append(ya - 1)
            if xa + 1 < 8 and ya + 2 < 8:
                if chessb[ya+2, xa+1] == "0" or chessb[ya+2, xa+1] in pionb:
                    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(xa * 100 + 102, ya * 100 + 202, 96, 96), 3)
                    listx.append(xa + 1)
                    listy.append(ya + 2)
            if xa + 1 < 8 and ya - 2 < 8:
                if chessb[ya-2, xa+1] == "0" or chessb[ya-2, xa+1] in pionb:
                    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(xa * 100 + 102, ya * 100 - 198, 96, 96), 3)
                    listx.append(xa + 1)
                    listy.append(ya - 2)
            if ya + 2 < 8:
                if chessb[ya + 2, xa - 1] == "0" or chessb[ya + 2, xa - 1] in pionb:
                    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(xa * 100 - 98, ya * 100 + 202, 96, 96), 3)
                    listx.append(xa - 1)
                    listy.append(ya + 2)
            if xa - 1 < 8 and ya - 2 < 8:
                if chessb[ya-2, xa-1] == "0" or chessb[ya-2, xa-1] in pionb:
                    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(xa * 100 - 98, ya * 100 - 198, 96, 96), 3)
                    listx.append(xa - 1)
                    listy.append(ya - 2)
        elif pselect == "K":
            listx = []
            listy = []
            if xa < 7:
                if chessb[ya, xa + 1] == "0" or chessb[ya, xa + 1] in pionb:
                    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(xa * 100 + 102, ya * 100 + 2, 96, 96), 3)
                    listx.append(xa + 1)
                    listy.append(ya)
            if xa < 7 and ya < 7:
                if chessb[ya + 1, xa + 1] == "0" or chessb[ya + 1, xa + 1] in pionb:
                    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(xa * 100 + 102, ya * 100 + 102, 96, 96), 3)
                    listx.append(xa + 1)
                    listy.append(ya + 1)
            if xa < 7:
                if chessb[ya - 1, xa + 1] == "0" or chessb[ya - 1, xa + 1] in pionb:
                    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(xa * 100 + 102, ya * 100 - 98, 96, 96), 3)
                    listx.append(xa + 1)
                    listy.append(ya - 1)
            if chessb[ya - 1, xa] == "0" or chessb[ya - 1, xa] in pionb:
                pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(xa * 100 + 2, ya * 100 - 98, 96, 96), 3)
                listx.append(xa)
                listy.append(ya - 1)
            if ya < 7:
                if chessb[ya + 1, xa] == "0" or chessb[ya + 1, xa] in pionb:
                    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(xa * 100+2, ya * 100 + 102, 96, 96), 3)
                    listx.append(xa)
                    listy.append(ya+1)
            if chessb[ya - 1, xa - 1] == "0" or chessb[ya - 1, xa - 1] in pionb:
                pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(xa * 100 - 98, ya * 100 - 98, 96, 96), 3)
                listx.append(xa - 1)
                listy.append(ya - 1)
            if ya < 7:
                if chessb[ya + 1, xa - 1] == "0" or chessb[ya + 1, xa - 1] in pionb:
                    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(xa * 100 - 98, ya * 100 + 102, 96, 96), 3)
                    listx.append(xa - 1)
                    listy.append(ya + 1)
            if chessb[ya, xa - 1] == "0" or chessb[ya, xa - 1] in pionb:
                pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(xa * 100 - 98, ya * 100 + 2, 96, 96), 3)
                listx.append(xa - 1)
                listy.append(ya)
        elif pselect == "Q":
            listx = []
            listy = []
            a = xa + 1
            while a < 8:
                if chessb[ya, a] == "0":
                    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(2 + a * 100, 2 + ya * 100, 96, 96), 3)
                    listx.append(a)
                    listy.append(ya)
                else:
                    if chessb[ya, a] in pionb:
                        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(2 + a * 100, 2 + ya * 100, 96, 96), 3)
                        listx.append(a)
                        listy.append(ya)
                    a = 9
                a += 1
            a = xa - 1
            while a > -1:
                if chessb[ya, a] == "0":
                    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(2 + a * 100, 2 + ya * 100, 96, 96), 3)
                    listx.append(a)
                    listy.append(ya)
                else:
                    if chessb[ya, a] in pionb:
                        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(2 + a * 100, 2 + ya * 100, 96, 96), 3)
                        listx.append(a)
                        listy.append(ya)
                        a = -2
                    a = -2
                a = a - 1
            a = ya - 1
            while a > -1:
                if chessb[a, xa] == "0":
                    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(2 + xa * 100, 2 + a * 100, 96, 96), 3)
                    listx.append(xa)
                    listy.append(a)
                else:
                    if chessb[a, xa] in pionb:
                        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(2 + xa * 100, 2 + a * 100, 96, 96), 3)
                        listx.append(xa)
                        listy.append(a)
                        a = -2
                    a = -2
                a = a - 1
            a = ya + 1
            while a < 8:
                if chessb[a, xa] == "0":
                    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(2 + xa * 100, 2 + a * 100, 96, 96), 3)
                    listx.append(xa)
                    listy.append(a)
                else:
                    if chessb[a, xa] in pionb:
                        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(2 + xa * 100, 2 + a * 100, 96, 96), 3)
                        listx.append(xa)
                        listy.append(a)
                        a = 8
                    a = 8
                a += 1
            a = xa
            b = ya
            while a > 0 and b > 0:
                if chessb[b - 1, a - 1] == "0":
                    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(-98 + a * 100, -98 + b * 100, 96, 96), 3)
                    listx.append(a - 1)
                    listy.append(b - 1)
                elif chessb[b - 1, a - 1] in pionb:
                    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(-98 + a * 100, -98 + b * 100, 96, 96), 3)
                    listx.append(a - 1)
                    listy.append(b - 1)
                    a = b = -1
                else:
                    a = -1
                a = a - 1
                b = b - 1
            a = xa
            b = ya
            while a < 7 and b > 0:
                if chessb[b - 1, a + 1] == "0":
                    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(102 + a * 100, -98 + b * 100, 96, 96), 3)
                    listx.append(a + 1)
                    listy.append(b - 1)
                elif chessb[b - 1, a + 1] in pionb:
                    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(102 + a * 100, -98 + b * 100, 96, 96), 3)
                    listx.append(a + 1)
                    listy.append(b - 1)
                    a = 8
                    b = -1
                else:
                    a = 8
                a = a + 1
                b = b - 1
            a = xa
            b = ya
            while a < 7 and b < 7:
                if chessb[b + 1, a + 1] == "0":
                    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(102 + a * 100, 102 + b * 100, 96, 96), 3)
                    listx.append(a + 1)
                    listy.append(b + 1)
                elif chessb[b + 1, a + 1] in pionb:
                    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(102 + a * 100, 102 + b * 100, 96, 96), 3)
                    listx.append(a + 1)
                    listy.append(b + 1)
                    a = b = 10
                else:
                    a = b = 10
                a = a + 1
                b = b + 1
            a = xa
            b = ya
            while a > 0 and b < 7:
                if chessb[b + 1, a - 1] == "0":
                    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(-98 + a * 100, 102 + b * 100, 96, 96), 3)
                    listx.append(a - 1)
                    listy.append(b + 1)
                elif chessb[b + 1, a - 1] in pionb:
                    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(-98 + a * 100, 102 + b * 100, 96, 96), 3)
                    listx.append(a - 1)
                    listy.append(b + 1)
                    a = -10
                    b = 10
                else:
                    a = -10
                a = a - 1
                b = b + 1
    for i in range(0, len(listx)):
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(listx[i]*100+2, listy[i]*100+2, 96, 96), 3)
    if "K" in pmn:
        pygame.draw.rect(screen, (50, 50, 250), pygame.Rect(200, 320, 375, 130))
        text = font.render("white win", True, (255, 255, 255))
        screen.blit(text, (250, 350))
    if "k" in pmb:
        pygame.draw.rect(screen, (50, 50, 250), pygame.Rect(200, 320, 375, 130))
        text = font.render("black win", True, (0, 0, 0))
        screen.blit(text, (250, 350))
    pygame.display.flip()

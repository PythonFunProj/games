import pygame
import math
import time
#different planes:
#1speed
#2life
#3maneuverability
#4damage
#5overheat
#special talent:
#6   more damage but limited amos
#7   tourelles
#8   looping(demi-tour rapide)
#9   roquette

#to do:
#add sound
#more plane
#teta when we can't see the plane

#more plane:
#0) ??? 9(*4)
#1) +1 -2 +3 +8 (6?) -4
#2) --1  ++2 --3 +4 7 9unlimited
#3) -1 (2?) -3  +4 +5 (6?) 9(*6)
shoot1 = False
shoot2 = False
plane = [(5, 4, 100, 0.025, 1), (7, 3, 75, 0.05, 1), (3, 4, 200, 0.020, 1)]
pygame.init()
font = pygame.font.Font(None, 30)

"""screen and image"""
screen = pygame.display.set_mode()

image1 = pygame.image.load(r'plane1.png')
image1 = pygame.transform.scale(image1, (20, 20))
image1 = pygame.transform.rotate(image1, 180)

image2 = pygame.image.load(r'plane2.png')
image2 = pygame.transform.scale(image2, (20, 20))
image2 = pygame.transform.rotate(image2, -90)

image4 = pygame.image.load(r'explosion.png')
image4 = pygame.transform.scale(image4, (30, 30))

def menu():
    planeA, planeB = 0, 0
    done = False
    pressed = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        xm, ym = pygame.mouse.get_pos()
        if 1320<xm<1390 and 653<ym<723 and pygame.mouse.get_pressed()[0]:
            done = True
        if 290 < xm < 360 and 608 < ym < 678 and pygame.mouse.get_pressed()[0] and not planeA == 0 and not pressed:
            planeA -= 1
        if 408 < xm < 478 and 608 < ym < 678 and pygame.mouse.get_pressed()[0] and not planeA+1 == len(plane) and not pressed:
            planeA += 1
        if 875 < xm < 935 and 608 < ym < 678 and pygame.mouse.get_pressed()[0] and not planeB == 0 and not pressed:
            planeB -= 1
        if 993 < xm < 1063 and 608 < ym < 678 and pygame.mouse.get_pressed()[0] and not planeB+1 == len(plane) and not pressed:
            planeB += 1
        if pygame.mouse.get_pressed()[0]:
            pressed = True
        else:
            pressed = False
        screen.fill((65, 65, 90))
        pygame.draw.rect(screen, (200, 200, 200), pygame.Rect(100, 100, 1335, 663))

        pygame.draw.rect(screen, (110, 110, 255), pygame.Rect(290, 225, 190, 363))
        pygame.draw.rect(screen, (110, 110, 255), pygame.Rect(875, 300-75, 190, 363))
        pygame.draw.rect(screen, (180, 180, 255), pygame.Rect(500, 300-75, 180, 363))
        pygame.draw.rect(screen, (180, 180, 255), pygame.Rect(1085, 300-75, 180, 363))

        pygame.draw.rect(screen, (100, 100, 155), pygame.Rect(290, 608, 70, 70))
        pygame.draw.rect(screen, (100, 100, 155), pygame.Rect(408, 608, 70, 70))
        pygame.draw.rect(screen, (100, 100, 155), pygame.Rect(875, 608, 70, 70))
        pygame.draw.rect(screen, (100, 100, 155), pygame.Rect(993, 608, 70, 70))

        pygame.draw.polygon(screen, (60, 60, 60), ((305, 643), (335, 623), (335, 663)))
        pygame.draw.polygon(screen, (60, 60, 60), ((460, 643), (430, 623), (430, 663)))
        pygame.draw.polygon(screen, (60, 60, 60), ((305+585, 643), (335+585, 623), (335+585, 663)))
        pygame.draw.polygon(screen, (60, 60, 60), ((460+585, 643), (430+585, 623), (430+585, 663)))

        pygame.draw.rect(screen, (100, 100, 155), pygame.Rect(1320, 653, 70, 70))
        screen.blit(pygame.font.Font(None, 40).render("GO", True, (50, 50, 50)), (1333, 675))

        screen.blit(pygame.transform.scale(pygame.transform.rotate(image1, 90), (200, 200)), (290, 370-75))
        screen.blit(pygame.transform.scale(image2, (200, 200)), (875, 380-75))

        screen.blit(pygame.font.Font(None, 70).render("PLAYER 1", True, (10, 10, 10)), (290, 180))
        screen.blit(font.render("Name of plane", True, (20, 20, 20)), (520, 340-75))
        screen.blit(font.render("Speed: "+ str(plane[planeA][0]), True, (20, 20, 20)), (515, 400-75))
        screen.blit(font.render("Damage: "+ str(plane[planeA][1]), True, (20, 20, 20)), (515, 450-75))
        screen.blit(font.render("Armor: "+ str(plane[planeA][2]), True, (20, 20, 20)), (515, 500-75))
        screen.blit(font.render("Agility: "+ str(40*plane[planeA][3]), True, (20, 20, 20)), (515, 550-75))
        screen.blit(font.render("overheat: "+ str(40*plane[planeA][4]), True, (20, 20, 20)), (515, 525))

        screen.blit(pygame.font.Font(None, 70).render("PLAYER 2", True, (10, 10, 10)), (875, 180))
        screen.blit(font.render("Name of plane", True, (20, 20, 20)), (1105, 340-75))
        screen.blit(font.render("Speed: " + str(plane[planeB][0]), True, (20, 20, 20)), (1100, 325))
        screen.blit(font.render("Damage: " + str(plane[planeB][1]), True, (20, 20, 20)), (1100, 375))
        screen.blit(font.render("Armor: " + str(plane[planeB][2]), True, (20, 20, 20)), (1100, 425))
        screen.blit(font.render("Agility: " + str(40 * plane[planeB][3]), True, (20, 20, 20)), (1100, 475))
        screen.blit(font.render("overheat: " + str(40 * plane[planeB][4]), True, (20, 20, 20)), (1100, 525))
        pygame.display.flip()
    return planeA, planeB

font2 = pygame.font.Font(None, 100)
bullets = []
angle = []
done = False

class Planes(pygame.sprite.Sprite):
    def __init__(self, speed, damage, life, maneuverability, overheat2, shoot):
        super().__init__()
        self.y = 0
        self.x = 0
        self.teta = 0
        self.speed = speed
        self.changet = 0
        self.changes = 0
        self.life = life    
        self.overheat = 0
        self.overheat1 = 0
        self.shoot = shoot
        self.damage = damage
        self.maneuverability = maneuverability
        self.overheat2 = overheat2

    def update(self):
        if self.shoot:
            self.overheat1 = 0
        self.overheat1 += 1
        if self.overheat > 0  and not self.shoot and self.overheat1 == 3:
            self.overheat1 = 0
            self.overheat -=1
        self.teta += self.changet
        if self.teta > 2*math.pi:
            self.teta -= 2 * math.pi
        if self.teta < 2*math.pi:
            self.teta += 2 * math.pi
        if (self.changes < 0 and self.speed > 3) or (self.changes > 0 and self.speed < 8):
            self.speed += self.changes
        if (1635 > self.x or math.cos(self.teta) < 0) and (-100< self.x or math.cos(self.teta)>0):
            self.x += math.cos(self.teta)*self.speed
        if (863 > self.y or math.sin(self.teta) < 0) and (-100< self.y or math.sin(self.teta)>0):
            self.y += math.sin(self.teta)*self.speed

    def screen1(self):
        if self.x < 0:
            if self.y < 0:
                pygame.draw.polygon(screen, (220, 0, 0), ((0, 0), (10, 5), (5, 10)))
            elif self.y > 863:
                pygame.draw.polygon(screen, (220, 0, 0), ((0, 863), (10, 858), (5, 853)))
            else:
                pygame.draw.polygon(screen, (220, 0, 0), ((0, self.y), (10, self.y-5), (10, self.y+5)))
        if self.x > 1535:
            if self.y < 0:
                pygame.draw.polygon(screen, (220, 0, 0), ((1535, 0), (1525, 5), (1530, 10)))
            elif self.y > 863:
                pygame.draw.polygon(screen, (220, 0, 0), ((1535, 863), (1525, 858), (1530, 853)))
            else:
                pygame.draw.polygon(screen, (220, 0, 0), ((1535, self.y), (1525, self.y-5), (1525, self.y+5)))

        if self.y < 0:
            pygame.draw.polygon(screen, (220, 0, 0), ((self.x, 0), (self.x-5, 10), (self.x+5, 10)))
        if self.y > 863:
            pygame.draw.polygon(screen, (220, 0, 0), ((self.x, 863), (self.x-5, 853), (self.x+5, 853)))

planeA, planeB = menu()

player1 = Planes(plane[planeA][0],plane[planeA][1],plane[planeA][2],plane[planeA][3],plane[planeA][4], shoot1)
player2 = Planes(0, 4, 100, 0.025, 1, shoot2)

player1.x = 200; player1.y = 200; player1.teta = math.pi/2-2*math.pi/6
player2.x = 1335; player2.y = 663; player2.teta = math.pi+math.pi/6

allsprite = pygame.sprite.Group()
allsprite.add(player1)
allsprite.add(player2)

clock = pygame.time.Clock()

"""image = pygame.transform.rotate(image1, -180*player1.teta/(2*math.pi))
image2 = pygame.transform.rotate(image2, 90*player2.teta/(2*math.pi))"""

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player1.changet -= player1.maneuverability
            if event.key == pygame.K_RIGHT:
                player1.changet += player1.maneuverability
            elif event.key == pygame.K_UP:
                if player1.speed < 8:
                    player1.changes += 0.5
            elif event.key == pygame.K_DOWN:
                if player1.speed > 3:
                    player1.changes -= 0.5
            elif event.key == pygame.K_m:
                shoot1 = True
                player1.shoot = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player1.changet = 0
            if event.key == pygame.K_RIGHT:
                player1.changet = 0
            elif event.key == pygame.K_UP:
                player1.changes = 0
            elif event.key == pygame.K_DOWN:
                player1.changes = 0
            elif event.key == pygame.K_m or player1.overheat == 80:
                shoot1 = False
                player1.shoot = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                player2.changet -= player2.maneuverability
            if event.key == pygame.K_d:
                player2.changet += player2.maneuverability
            elif event.key == pygame.K_z:
                if player2.speed < 8:
                    player2.changes += 0.5
            elif event.key == pygame.K_s:
                if player2.speed > 3:
                    player2.changes -= 0.5
            elif event.key == pygame.K_e:
                shoot2 = True
                player2.shoot = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_q:
                player2.changet = 0
            if event.key == pygame.K_d:
                player2.changet = 0
            elif event.key == pygame.K_z:
                player2.changes = 0
            elif event.key == pygame.K_s:
                player2.changes = 0
            elif event.key == pygame.K_e or player2.overheat == 80:
                shoot2 = False
                player2.shoot = False
    """rotation of the planes"""
    image = pygame.transform.rotate(image1, -180 * player1.teta / math.pi)
    image3 = pygame.transform.rotate(image2, -180 * player2.teta / math.pi-90)
    """shoot"""
    if shoot1 and player1.overheat < 80:
        bullets.append((player1.x + 10, player1.y + 10))
        angle.append(player1.teta)
        player1.overheat += player1.overheat2

    if shoot2 and player2.overheat < 80:
        bullets.append((player2.x + 10, player2.y + 10))
        angle.append(player2.teta)
        player2.overheat += player2.overheat2
    """death"""
    if player2.life <= 0:
        image3 = image4
        player2.speed = 0
    if player1.life <= 0:
        image = image4
        player1.speed = 0

    screen.fill((65, 65, 90))
    """arrow when plane is out of screen"""
    Planes.screen1(player1)
    Planes.screen1(player2)

    allsprite.update()
    """show bullets"""
    for i in range(0, len(bullets), 2):
        xi, yi = bullets[i]
        xi += 40*math.cos(angle[i])
        yi += 40*math.sin(angle[i])
        if player1.x <= xi <= player1.x + 20 and player1.y <= yi <= player1.y+20 and player1.life != 0:
            player1.life -= player2.damage
        if player2.x <= xi <= player2.x + 20 and player2.y <= yi <= player2.y+20 and player2.life != 0:
            player2.life -= player1.damage
        bullets[i] = (xi, yi)
        xi += 10*math.cos(angle[i])
        yi += 10*math.sin(angle[i])
        pygame.draw.line(screen, (243, 214, 23), bullets[i], (xi, yi), 2)
    """life"""
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(20, 20, 150, 30))
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(20, 20, 150-player2.life*6/4, 30))
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(1350, 20, 150, 30))
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(1350, 20, 150 - player1.life*6/4, 30))
    pygame.draw.rect(screen, (0, 86, 27), pygame.Rect(18, 18, 152, 32), 2)
    pygame.draw.rect(screen, (231, 168, 84), pygame.Rect(1348, 18, 152, 32), 2)
    """overheat"""
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(22, 57, player2.overheat * 10 / 8, 5))
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(1398, 57, player1.overheat * 10 / 8, 5))
    pygame.draw.rect(screen, (120, 120, 120), pygame.Rect(20, 55, 102, 7), 2)
    pygame.draw.rect(screen, (120, 120, 120), pygame.Rect(1396, 55, 102, 7), 2)
    screen.blit(image, (player1.x, player1.y))
    screen.blit(image3, (player2.x, player2.y))
    pygame.display.flip()
    clock.tick(60)

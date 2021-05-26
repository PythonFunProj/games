import pygame
import random
from pygame.locals import *
import os 
abspath = os.path.abspath(__file__) #sets the location of the .py file as the working directory
dname = os.path.dirname(abspath)
os.chdir(dname)
pygame.init()
screen = pygame.display.set_mode((480, 639))
image = pygame.image.load(r'images/flappybird2.png')
image2 = pygame.image.load(r'images/flappy bird.png')
image3 = pygame.image.load(r'images/flappybird3.png')
image4 = pygame.transform.rotate(image3, 180)
mainClock = pygame.time.Clock()
def main():
    while True:
        score = 0
        y = 300
        speedY = 0
        done = True
        dead = False
        pressed = False
        pilierP = [500, 800]
        pilierH = [random.randrange(212, 550), random.randrange(212, 550)]
        while done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = False
            key = pygame.key.get_pressed()
            if key[pygame.K_ESCAPE]:
                    pygame.quit()
            if (key[pygame.K_SPACE] or pygame.mouse.get_pressed()[0]) and not pressed:
                pressed = True
                speedY = 4
            if (key[pygame.K_SPACE] or pygame.mouse.get_pressed()[0]) and dead:
                pressed = True
                done = False
            if not key[pygame.K_SPACE] and not pygame.mouse.get_pressed()[0]:
                pressed = False
            if pilierP[0] < -90:
                pilierP.remove(pilierP[0])
                pilierH.remove(pilierH[0])
                pilierP.append(500)
                pilierH.append(random.randrange(212, 550))
            if pilierP[0] == 80:
                score += 1
            if not dead:
                pilierP[0] -= 1
                pilierP[1] -= 1
                y -= speedY
                speedY -= 0.1
            screen.fill([255, 255, 255])
            screen.blit(image, (0, 0))
            screen.blit(image2, (150, y))
            screen.blit(image3, (pilierP[0]+5, pilierH[0]-597))
            screen.blit(image3, (pilierP[1]+5, pilierH[1]-597))
            screen.blit(image4, (pilierP[1], pilierH[1]))
            screen.blit(image4, (pilierP[0], pilierH[0]))
            screen.blit(pygame.font.Font(None, 50).render(str(score), True, (255, 0, 0)), (0, 0))
            if y > 540 or (80 < pilierP[1] < 200 and not pilierH[1]-41 > y > pilierH[1]-170) or (80 < pilierP[0] < 200 and not pilierH[0]-41 > y > pilierH[0]-170):
                speedY = 0
                dead = True
                print("you're dead")
            pygame.display.flip()
            mainClock.tick(120)  # nb of FPS

main()
import pygame
import random
pygame.init()
score = 0
y = 300
speedY = 0
screen = pygame.display.set_mode((480, 639))
image = pygame.image.load(r'flappybird2.png')
image2 = pygame.image.load(r'flappy bird.png')
image3 = pygame.image.load(r'flappybird3.png')
image4 = pygame.transform.rotate(image3, 180)
done = True
dead = False
pressed = False
pilierP = [500, 800]
pilierH = [random.randrange(212, 550), random.randrange(212, 550)]
while done:
    screen.fill([255, 255, 255])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
    screen.blit(image, (0, 0))
    screen.blit(image2, (150, y))
    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE] or pygame.mouse.get_pressed()[0] and not pressed:
        pressed = True
        speedY = 4
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
    screen.blit(image3, (pilierP[0]+3, pilierH[0]-597))
    screen.blit(image3, (pilierP[1]+3, pilierH[1]-597))
    screen.blit(image4, (pilierP[1], pilierH[1]))
    screen.blit(image4, (pilierP[0], pilierH[0]))
    screen.blit(pygame.font.Font(None, 50).render(str(score), True, (255, 0, 0)), (0, 0))
    if y > 540 or (80 < pilierP[1] < 200 and not pilierH[1]-41 > y > pilierH[1]-170) or (80 < pilierP[0] < 200 and not pilierH[0]-41 > y > pilierH[0]-170):
        speedY = 0
        dead = True
        print("you're dead")
    pygame.display.flip()

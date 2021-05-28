import pygame
from pygame.locals import *
from queue import Queue, Empty
import websocket
import _thread
import os
from levelsdata import wallsforlevel, killrectsforlevel, winrectsforlevel, spawnforlevel, backgroundforlevel, fakewallsforlevel
# sets the location of the .py file as the working directory
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
print(websocket.__version__)
q = Queue()
online = True
colors = [(255, 0, 0), (0, 255, 0), (255, 255, 0)]
pygame.mixer.init()
s = 'sound'
jumpsound = pygame.mixer.Sound('sounds/SFX_Jump_09.wav')
hurtsound = pygame.mixer.Sound('sounds/SFX_Jump_50.wav')
wintouch = pygame.mixer.Sound('sounds/coin10.wav')


def ws_message(ws, message):
    # print('Enqueued ' + message)
    q.put(message)


def ws_open(ws):
    ws.send('{"event":"subscribe", "subscription":{"name":"trade"}, "pair":["XBT/USD","XRP/USD"]}')


def ws_thread(*args):
    ws.run_forever()


ws = websocket.WebSocketApp("ws:///", on_open=ws_open, on_message=ws_message)

# Start a new thread for the WebSocket interface
_thread.start_new_thread(ws_thread, ())

# controller
pygame.joystick.init()


class Game:

    def __init__(self):
        print("init game")
        self.collision = False
        self.moveLeft, self.moveRight, self.moveUp, self.jump = False, False, False, False
        self.player = pygame.Rect(300, 600, 25, 25)
        self.MOVESPEED = 15
        self.MOVESPEEDy = 0
        # self.click = 0
        self.friend = [[-25, -25], [-25, -25], [-25, -25]]
        self.elevator = 0
        self.walls = []
        self.joy = False
        self.joysticks = False
        if pygame.joystick.get_count() > 0:
            # self.joystick = pygame.joystick.Joystick(0).init()
            self.joy = True
            pygame.joystick.init()
            self.joysticks = pygame.joystick.Joystick(0)

    def run_logic(self, winrects, killrects, level):
        self.collision = False

        """move/collision left"""

        if self.moveLeft and self.player.left > 0:
            self.player.left -= self.MOVESPEED
            for wall in self.walls[:]:
                if self.player.colliderect(wall) and wall.right <= self.player.left+self.MOVESPEED:
                    #print("oui")
                    self.player.left = wall.right
                    self.collision = True
            if self.player.left < 0:
                self.player.left = 0
            for player1 in self.friend:
                x = self.player
                x1 = int(player1[0])
                y1 = int(player1[1])
                if y1-25 < x.top < y1+25 and x1-25 < x.left < x1+25:
                    self.player.left = x1+25
                    self.collision = True

        """move/collision right"""

        if self.moveRight and self.player.right < 800:
            self.player.right += self.MOVESPEED
            for wall in self.walls[:]:
                if self.player.colliderect(wall) and wall.left >= self.player.right-self.MOVESPEED:
                    #print("oui")
                    self.player.right = wall.left
                    self.collision = True

            for player1 in self.friend:
                x = self.player
                x1 = int(player1[0])
                y1 = int(player1[1])
                if y1-25 < x.top < y1+25 and x.right > x1 and x.left < x1 + 25:
                    self.player.right = x1
                    self.collision = True

        """fall"""

        self.player.bottom -= self.MOVESPEEDy
        self.MOVESPEEDy -= 1
        for wall in self.walls[:]:
            if self.player.colliderect(wall) and not self.jump:
                self.player.bottom = wall.top
                #print(wall)
                self.MOVESPEEDy = 0
                self.collision = True

        for player1 in self.friend:
            x = self.player.left
            y = self.player.top
            x1 = int(player1[0])
            y1 = int(player1[1])
            if x-25 < x1 < x + 25 and y + abs(self.MOVESPEED) > y1 >= y:
                self.player.bottom = y1
                self.MOVESPEEDy = 0
                self.collision = True

        """jump"""

        if self.jump and self.MOVESPEEDy == 0:
            self.jump = False
        if self.moveUp and self.collision and not self.jump:
            self.jump = True
            pygame.mixer.Sound.play(jumpsound)
            self.MOVESPEEDy = 15

        """collision at the Top of the player"""

        for wall in self.walls[:]:
            if self.player.colliderect(wall) and self.jump:
                self.jump = False
                self.player.top = wall.bottom
                self.MOVESPEEDy = 0
       
        if self.friend:
            for player1 in self.friend:
                x = self.player.left
                y = self.player.top
                x1 = int(player1[0])
                y1 = int(player1[1])
                if x-25 < x1 < x + 25 and self.jump and y1+25 == y:
                    self.jump = False
                    self.player.top = y1+25
                    self.MOVESPEEDy = 0

        """collision with killrect"""

        for kr in killrects[:]:
            if self.player.colliderect(kr):
                print("ouch")
                pygame.mixer.Sound.play(hurtsound)###################################""
                self.player.left = int(spawnforlevel(level)[0])
                self.player.top = int(spawnforlevel(level)[1])

        """collision with winrect"""

        win = False
        for wr in winrects[:]:
            if self.player.colliderect(wr):
                pygame.mixer.Sound.play(wintouch)
                level += 1
                print('win')
                self.player.left = int(spawnforlevel(level)[0])
                self.player.top = int(spawnforlevel(level)[1])
                win = True
        return win, level

    def process_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                return True
            keys = pygame.key.get_pressed()

            self.moveLeft, self.moveRight, self.moveUp = False, False, False

            if keys[pygame.K_LEFT] \
                    or (self.joy and self.joysticks.get_axis(0) < -0.1):
                self.moveLeft = True
                self.moveRight = False

            if keys[pygame.K_RIGHT] \
                    or (self.joy and self.joysticks.get_axis(0) > 0.1):
                self.moveRight = True
                self.moveLeft = False

            if keys[pygame.K_UP] \
                    or (self.joy and self.joysticks.get_button(0)):
                self.moveUp = True
        return False

    
class Elevators:
    #    elevator = Elevators(660, 600, 30, 750, 500)
    def __init__(self, xbutton, ybutton, xelevator, yelevator, maxheight):
        self.xbutton = xbutton
        self.ybutton = ybutton
        self.xelevator = xelevator
        self.yelevator = yelevator
        self.maxheight = maxheight
        self.buttonOF = False
        self.height = 0

    def button(self, posx, posy, friend):
        self.buttonOF = False
        if posy == self.ybutton-25 and self.xbutton+15 < posx < self.xbutton + 115:
            self.buttonOF = True
        else:
            for i in range(3):
                if int(friend[i][1]) == self.ybutton-25 and self.xbutton+15 < int(friend[i][0]) < self.xbutton + 115:
                    self.buttonOF = True

    def elevator(self):
        if self.height < self.maxheight and self.buttonOF:
            self.height += 1
        if self.height > 0 and not self.buttonOF:
            self.height -= 1


def display_frame(friend, colors, screen, walls, xbutton, ybutton, height, player, xelevator, yelevator, killrects, winrects,fakewalls, background, image):

    screen.fill((35, 35, 60))
    screen.blit(background, [0, 0])

    # friend:
    for i in range(3):
        pygame.draw.rect(screen, colors[i], pygame.Rect(int(friend[i][0]), int(friend[i][1]), 25, 25))
        screen.blit(image, (int(friend[i][0]), int(friend[i][1])))

    # walls:
    for wall in walls:
        pygame.draw.rect(screen, (0, 0, 0), wall)
    for kr in killrects:
        pygame.draw.rect(screen, (200, 0, 0), kr)
    for wr in winrects:
        pygame.draw.rect(screen, (200, 200, 0), wr)
    for fw in fakewalls:
        pygame.draw.rect(screen,(0,0,0),fw)
        
    # button:
    pygame.draw.rect(screen, (50, 50, 50), pygame.Rect(xbutton, ybutton, 105, 8))
    pygame.draw.rect(screen, (150, 0, 0), pygame.Rect(xbutton+15, ybutton-3, 75, 7))

    # elevator
    pygame.draw.rect(screen, (20, 20, 20), pygame.Rect(xelevator, yelevator-height, 100, height))

    # player:
    pygame.draw.rect(screen, (0, 0, 255), player)
    screen.blit(image, (player.left, player.top))

    pygame.display.update()


def updatelevel(level, game):
    game.walls = wallsforlevel(level)
    killrects = killrectsforlevel(level)
    winrects = winrectsforlevel(level)
    spawn = spawnforlevel(level)
    fakewalls = fakewallsforlevel(level)
    background = backgroundforlevel(level)
    game.player.left = (int(spawn[0]))
    game.player.top = (int(spawn[1]))
    return killrects, winrects, background, fakewalls


def main():
    level = 1

    pygame.init()
    
    image1 = pygame.image.load(r'images/character.png')
    image1 = pygame.transform.scale(image1, (25, 25))

    # Create an instance of the Game class
    game = Game()
#    elevator = Elevators(660, 600, 30, 750, 500)
    elevator = Elevators(-100, -600, -30, -750, 500)

    updatelevel(level, game)

    clock = pygame.time.Clock()
    # pygame.key.set_repeat(10, 100)
    screen = pygame.display.set_mode((800, 800), 0, 32)
    pygame.display.set_caption("client")
    pygame.mouse.set_visible(False)

    killrects, winrects, background, fakewalls = updatelevel(level, game)

    done = False
    # Main game loop

    while not done:
        # Process events (keystrokes, mouse clicks, etc)
        done = game.process_events()

        # Update object positions, check for collisions
        win, level = game.run_logic(winrects, killrects, level)
        if win:
            killrects, winrects, background, fakewalls= updatelevel(level, game)
        elevator.button(game.player.left, game.player.top, game.friend)
        elevator.elevator()

        try:
            while True:
                data = q.get(False)
                # If `False`, the program is not blocked. `Queue.Empty` is thrown if
                # the queue is empty
                
                if data[0] == "p":
                    # data => p 'x' / 'y' 'player'
                    e = int(data[len(data)-1])
                    f = len(game.friend)
                    pos1 = data.find('/')
                    game.friend[e][0] = int(data[1:pos1])
                    game.friend[e][1] = data[pos1 + 1:len(data)-1]
                else:
                    #print(data[0])
                    pass
        except Empty:
            data = 0

        # send coordinates
        try:
            ws.send("p" + str(game.player.left) + "/" + str(game.player.top))
            online = True
        except:
            online = False
        # Draw the current frame
        display_frame(game.friend, colors, screen, game.walls, elevator.xbutton, elevator.ybutton, elevator.height,
                      game.player, elevator.xelevator, elevator.yelevator, killrects, winrects, fakewalls, background, image1)

        # Pause for the next frame
        clock.tick(60)

    # Close window and exit
    pygame.quit()


# Call the main function, start up the game
main()

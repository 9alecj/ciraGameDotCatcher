from cira.ciragame import *
from random import randint

class MyGame(CiraGame):
    # engine variables
    gameTitle = "My Game"

    # called once when the program first initializes
    def awake(self):
        print("Welcome to My Game!")


    # called at the beginning of each new play session
    def start(self):
        self.player = Player()
        self.playerColor = (0, 255, 0)
        self.EnemiesX = []
        self.EnemiesY = []
        self.EnemyColor = (255,0,0)
        self.FriendlyX = []
        self.FriendlyY = []
        self.FriendlyColor = (0,255,0)
        self.points = []
        pass

    # called each update frame
    def update(self):
         # player input
        if cira.keys.getKey("1-Left"):
            self.player.moveLeft()
        if cira.keys.getKey("1-Right"):
            self.player.moveRight()

        #Enemy stuff
        if len(self.EnemiesX) < 11 :
             self.EnemiesX.append(randint(1, cira.display.getWidth() - 1))
             self.EnemiesY.append(0)
             
        
        for y in range(len(self.EnemiesY)):
            if self.EnemiesY[y] < cira.display.getHeight()-1 :
                self.EnemiesY[y] = self.EnemiesY[y]+1
            else :
                self.EnemiesX[y] = randint(1, cira.display.getWidth() - 1)
                self.EnemiesY[y] = 0
            if self.EnemiesY[y] == 18 :
                for x in range (4):
                    if self.EnemiesX[y] == self.player.getSelfX()+x:
                        self.EnemiesX[y] = randint(1, cira.display.getWidth() - 1)
                        self.EnemiesY[y] = 0
                        if len(self.points) > 0:
                            self.points.pop()
                        if len(self.points) == cira.display.getWidth():
                            print("you win!")

        for y in range(len(self.FriendlyY)):
            if self.FriendlyY[y] < cira.display.getHeight()-1 :
                self.FriendlyY[y] = self.FriendlyY[y]+1
            else :
                self.FriendlyX[y] = randint(1, cira.display.getWidth() - 1)
                self.FriendlyY[y] = 0
            if self.FriendlyY[y] == 18 :
                for x in range (4):
                    if self.FriendlyX[y] == self.player.getSelfX()+x:
                        self.FriendlyX[y] = randint(1, cira.display.getWidth() - 1)
                        self.FriendlyY[y] = 0
                        self.points.append(1)
                        if len(self.points) == cira.display.getWidth():
                            print("you win!")

            
        #Friendly stuff
        if len(self.FriendlyX) < 11 :
             self.FriendlyX.append(randint(1, cira.display.getWidth() - 1))
             self.FriendlyY.append(0)
             
        for y in range(len(self.FriendlyY)-1):
            if self.FriendlyY[y] < cira.display.getHeight()-1 :
                self.FriendlyY[y] = self.FriendlyY[y]+1
            else :
                self.FriendlyX[y] = randint(1, cira.display.getWidth() - 1)
                self.FriendlyY[y] = 0
                
       
    # called when each new frame needs to be drawn
    def draw(self):
        cira.display.clearScreen(0, 0, 0)
        self.player.draw(self.playerColor)
        for x in range(len(self.EnemiesX)-1):
            cira.display.putPixel(self.EnemiesX[x], self.EnemiesY[x], self.EnemyColor[0],self.EnemyColor[1],self.EnemyColor[2])
        for x in range(len(self.FriendlyX)-1):
            cira.display.putPixel(self.FriendlyX[x], self.FriendlyY[x], self.FriendlyColor[0],self.FriendlyColor[1],self.FriendlyColor[2])
        for x in range(len(self.points)):
            cira.display.putPixel(x, 20, self.FriendlyColor[0],self.FriendlyColor[1],self.FriendlyColor[2])


       
class Player:

    # initialize the player
    def __init__(self):
        self.x = 0
        self.y = 18

    def getSelfX(self):
        return self.x

    def getSelfY(self):
        return self.y

    # move the player left
    def moveLeft(self):
        if self.x > 0:
            self.x -= 1

    # move the player right
    def moveRight(self):
        if self.x < cira.display.getWidth() - 4:
            self.x += 1

    # draw the player
    def draw(self, color):
        # draw player dot
        for x in range (4):
             cira.display.putPixel(self.x+x, self.y, color[0], color[1], color[2])


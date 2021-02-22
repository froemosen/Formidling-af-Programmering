import pygame as pg
import random as r
x = 1920
y = 1080
pg.mixer.init()



startButton = pg.image.load("Assets\mainMenu\startButton.png")
startButton1 = pg.image.load("Assets\mainMenu\startButton1.png")
quitButton = pg.image.load("Assets\mainMenu\quitButton.png")
quitButton1 = pg.image.load("Assets\mainMenu\quitButton1.png")

#Main Menu buttons
class buttons(object):
    def __init__(self, startX, startY, startheight, startwidth, quitX, quitY, quitheight, quitwidth):
        self.startX = startX
        self.startY = startY
        self.quitX = quitX
        self.quitY = quitY
        self.startheight = startheight
        self.startwidth = startwidth
        self.quitheight = quitheight
        self.quitwidth = quitwidth
    
    def drawStart(self, win):
        win.blit(startButton, (self.startX, self.startY))
    
    def drawQuit(self, win):
        win.blit(quitButton, (self.quitX, self.quitY))


class GameObject():
    def __init__(self, x, y):
        pass
    
    def draw(self, win):
        pass

class Snake(GameObject):
    def __init__(self):
        pass

class Food(GameObject):
    def __init__(self):
        pass

class Obstacle(GameObject):
    def __init__(self):
        pass
    

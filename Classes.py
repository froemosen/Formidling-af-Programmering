import pygame as pg
import random as r
x = 1920
y = 1080
pg.mixer.init()
win = pg.display.set_mode((x,y), pg.FULLSCREEN)

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
    
    def drawStart(self):
        win.blit(startButton, (self.startX, self.startY))
    
    def drawQuit(self):
        win.blit(quitButton, (self.quitX, self.quitY))


#Game Classes
class snake():

class obstacle():

class point():
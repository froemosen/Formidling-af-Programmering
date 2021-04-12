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
    def __init__(self, sprite, x, y):
        self.sprite = sprite
        self.x = x
        self.y = y

    def draw(self, win):
        win.blit(sprite, (x, y))

class Snake(GameObject):
    def __init__(self, x, y):
        self.length = 1
        self.snakeID = ((x, y, "R", "H"), (x-1, y, "R", "B"), (x-2, y, "R", "B")) #Id's go into master list, with snake bits inside ((x, y, orientation("U","R","D","L"), part("H", "B", "T")))
        """ Lav noget med snake-movement hvor en liste indeholder en masse instrukser: (L, U, D, L, U, R, U, L, L, L)"""

    def animate(self):
        pass

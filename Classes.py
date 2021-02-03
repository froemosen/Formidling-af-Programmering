import pygame as pg
import random as r
x = 1920
y = 1080
pg.mixer.init()
win = pg.display.set_mode((x,y), pg.FULLSCREEN)

startButton = pg.image.load("assets/menu/startButton.png")
startButton1 = pg.image.load("assets/menu/startButton1.png")
quitButton = pg.image.load("assets/menu/quitButton.png")
quitButton1 = pg.image.load("assets/menu/quitButton1.png")

#Main Menu buttons
class buttons(object):
    def __init__(self, startX, startY, settingX, settingY, quitX, quitY, height, width):
        self.startX = startX
        self.startY = startY
        self.settingX = settingX
        self.settingY = settingY
        self.quitX = quitX
        self.quitY = quitY
        self.height = height
        self.width = width
    
    def drawStart(self):
        win.blit(startButton, (self.startX, self.startY))
    
    def drawQuit(self):
        win.blit(quitButton, (self.quitX, self.quitY))



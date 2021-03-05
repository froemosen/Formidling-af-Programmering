#Imports
import pygame as pg
import os

#Variabler


pg.init()
pg.font.init()
win = pg.display.set_mode((1920, 1080), pg.FULLSCREEN)
bg = pg.image.load("Assets\gameSprites\Background.png")
i = 0
#level = pg.image.load()
"""for file in os.listdir("dirname") #Bruges til at finde de obstacles som man vil bruge"""

def start():
    run()


def run():
    while True:
        #Calculations and such
        drawWorld()
        pg.display.update()

def drawWorld():
    #Graphics and such
    win.blit(bg, (0, 0))

    

if __name__ == '__main__':
    start()
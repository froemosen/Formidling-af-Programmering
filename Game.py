#Imports
import pygame as pg
import os

#Variabler
#Window setup
pg.init()
pg.font.init()
win = pg.display.set_mode((1920, 1080), pg.FULLSCREEN)

#UI load
bg = pg.image.load("Assets\gameSprites\Background.png")
terminal = pg.image.load("Assets\gameSprites\Terminal.png")
level = pg.image.load("Assets\gameSprites\Baner\Bane.png")
grid = pg.image.load("Assets\gameSprites\Grid10x10.png")
dnd = pg.image.load("Assets\gameSprites\DnDOptions.png")

rock = pg.image.load("Assets\gameSprites\Obstacles\sten.png")

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

    #UI draw
    win.blit(bg, (0, 0))
    win.blit(terminal, (1260, 15))
    win.blit(level, (20, 20))
    win.blit(grid, (10, 10))
    win.blit(dnd, (15, 760))
    
    win.blit(rock, (1*100+20, 2*100+30))
    win.blit(rock, (7*100+20, 5*100+30))

    

if __name__ == '__main__':
    start()
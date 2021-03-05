#Imports
import pygame as pg
import os

#Variabler

def start():
    pg.init()
    pg.font.init()

    win = pg.display.set_mode((1920, 1080), pg.FULLSCREEN)

    #bg = pg.image.load()
    #level = pg.image.load()
    """for file in os.listdir("dirname")"""

    run()


def run():
    while True:
        pass

def drawWorld():
    pass

if __name__ == '__main__':
    start()
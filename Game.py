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
level = pg.image.load("Assets\gameSprites\Baner\Bane0.png")
gridSelected = pg.image.load("Assets\gameSprites\Grid100x100.png") #Default grid
grid100x100 = pg.image.load("Assets\gameSprites\Grid100x100.png") #100x100 grid size (12x7)
grid50x50 = pg.image.load("Assets\gameSprites\Grid50x50.png") #50x50 grid size (24x14)
dnd = pg.image.load("Assets\gameSprites\DnDOptions.png")

#Assets/Level load
lvlAssets = []
rock = pg.image.load("Assets\gameSprites\Obstacles\Sten.png")
lake = pg.image.load("Assets\gameSprites\Obstacles\Vandpyt.png")
plants = pg.image.load("Assets\gameSprites\Obstacles\Planter.png")

food = pg.image.load("Assets\gameSprites\Point.png")



#Backgrounds:
levels = []
for file in os.listdir("Assets\gameSprites\Baner"): #Bruges til at finde de obstacles som man vil bruge
    levels.append(file)


def start(levelID):
    levelDecode(levelID)
    run()

    #Level ID 

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
    win.blit(grid100x100, (10, 10))
    win.blit(dnd, (15, 760))
    
    #Assets/Level draw
    no = 0
    for i in range(int(len(lvlAssets)/2)):
        win.blit(lvlAssets[no], lvlAssets[no+1])
        no += 2

    #win.blit(rock, (1*100+20, 2*100+30))
    #win.blit(rock, (7*100+20, 5*100+30))

def levelDecode(levelID):
    global gridSelected
    global level
    global lvlAssets

    levelID = list(levelID)
    #Decode gridsize
    if levelID[0] == "S":
        gridSelected = grid100x100
        del(levelID[0])
    elif levelID[0] == "B":
        gridSelected = grid50x50
        del(levelID[0])
    #Decode level
    try: #Level valgt er nummereret fra 0 til 9
        level = pg.image.load("Assets\gameSprites\Baner/"+levels[int(levelID[0])])
        del(levelID[0])

    except ValueError: #Levelnummerering valgt er højere eller lig 10
        try:
            level = pg.image.load("Assets\gameSprites\Baner/"+levels[ord(levelID[0])-87]) #"ord" returnerer en nummerering for bogstavet. Når man subtakterer 87 vil a=10, b=11, c=12, osv. 
            del(levelID[0])

        except IndexError: #Default level er valgt (Valgt level eksisterer ikke)
            if levelID[0] != "B" or "F" or "L" or "P" or "R" or "Z": #Hvis at levelID[0] ikke skal bruges senere:
                del(levelID[0])
            else:
                pass
        
    #Decode items
    while len(levelID) > 0:
        #Item
        if levelID[0] == "F":
            lvlAssets.append(food) #Item append
            xoffset = 20+6
            yoffset = 20+17
        elif levelID[0] == "L":
            lvlAssets.append(lake)
            xoffset = 20
            yoffset = 20+31
        elif levelID[0] == "P":
            lvlAssets.append(plants)
            xoffset = 20
            yoffset = 20+25
        elif levelID[0] == "R":
            lvlAssets.append(rock)
            xoffset = 20
            yoffset = 20+12
        #elif levelID[0] == "Z": #Usynlig collision (Når forhindringer er indbygget i banen.)
            #lvlAssets.append()

        #Position
        if levelID[0] == "F" or "L" or "P" or "R":
            xy = []
            for i in range(2):
                if i == 0: offset = xoffset
                elif i == 1: offset = yoffset

                if levelID[i+1] == "0": #Position er 10
                    pos = 10
                    xy.append(pos*100+offset)
                else:
                    try: #Level valgt er nummereret fra 0 til 9
                        pos = int(levelID[i+1])
                        xy.append(pos*100+offset)
                    except ValueError: #Levelnummerering valgt er højere eller lig 10
                        pos = ord(levelID[i+1])-86 #"ord" returnerer en nummerering for bogstavet. Når man subtakterer 96 vil a=1, b=2, c=3, osv. 
                        xy.append(pos*100+offset)

            lvlAssets.append(xy)
            print(lvlAssets)
            del(levelID[2], levelID[1], levelID[0])
            print("len:", len(levelID))

if __name__ == '__main__':
    start("BcF11F56Fa4R22L95P74")
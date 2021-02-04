import pygame as pg
import time
import random as r
import Classes
import Game
x = 1920
y = 1080
pg.mixer.init(frequency=44100, size=-16, channels=6, buffer=4096)
clock = pg.time.Clock()
tick = pg.time.get_ticks()
bg1 = pg.image.load("Assets\mainMenu\Baggrund1.png") #Load Bg
bg2 = pg.image.load("Assets\mainMenu\Baggrund2.png") #Load Bg
bg3 = pg.image.load("Assets\mainMenu\Baggrund3.png") #Load Bg
bg4 = pg.image.load("Assets\mainMenu\Baggrund4.png") #Load Bg
bgAnimation = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 2, 3, 3, 2, 4, 3, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 2,]
bgChoice = 0
win = pg.display.set_mode((x,y), pg.FULLSCREEN)
pg.display.set_caption("Life of Mark episode 2 - Master The Snake")
icon = pg.image.load("Assets\others\icon.png")
pg.display.set_icon(icon)
select = pg.mixer.Sound("Assets\Sounds\selectMenu.wav")
soundCool = False
btnStartX, btnStartY, btnStartHeight, btnStartWidth, btnQuitX, btnQuitY, btnQuitHeight, btnQuitWidth = 841, 500, 60, 238, 872, 600, 58, 176
buttons = Classes.buttons(btnStartX, btnStartY, btnStartHeight, btnStartWidth, btnQuitX, btnQuitY, btnQuitHeight, btnQuitWidth)
startButton1 = Classes.startButton1
quitButton1 = Classes.quitButton1

def drawWorld():
        mx, my = pg.mouse.get_pos()
        global bgChoice
        global soundCool

        if bgChoice+1 > len(bgAnimation):
            bgChoice = 0
        
        if bgAnimation[bgChoice] == 1:
            bg = bg1
        elif bgAnimation[bgChoice] == 2:
            bg = bg2
        elif bgAnimation[bgChoice] == 3:
            bg = bg3
        elif bgAnimation[bgChoice] == 4:
            bg = bg4
        else: 
            bg = bg1

        win.blit(bg, (0,0))
        bgChoice += 1

        buttons.drawStart()
        buttons.drawQuit()

        if mx > btnStartX and mx < btnStartX+btnStartWidth and my > btnStartY and my < btnStartY+btnStartHeight:
            if not soundCool:
                pg.mixer.Channel(1).play(select)
                soundCool = True
            win.blit(icon, (btnStartX+109, btnStartY+260))
            win.blit(startButton1, (btnStartX, btnStartY))
            
                
        elif mx > btnQuitX and mx < btnQuitX+btnQuitWidth and my > btnQuitY and my < btnQuitY+btnQuitHeight:
            if not soundCool: 
                pg.mixer.Channel(2).play(select)
                soundCool = True
            win.blit(quitButton1, (btnQuitX, btnQuitY))
            
        
        else:
            buttons.drawStart()
            buttons.drawQuit()
            soundCool = False

def pygameMenuStart():
    pg.init()
    pg.mixer.music.load("Assets\Sounds\MainMenuMusic.mp3")
    pg.mixer.music.set_volume(0.35)
    pg.mixer.music.play(-1)
    run = True
    while run:
        mx, my = pg.mouse.get_pos()
        clock.tick(60)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.MOUSEBUTTONDOWN:
                if mx > btnStartX and mx < btnStartX+btnStartWidth and my > btnStartY and my < btnStartY+btnStartHeight:
                    pg.mixer.music.fadeout(1500)
                    Game.start()
                if mx > btnQuitX and mx < btnQuitX+btnQuitWidth and my > btnQuitY and my < btnQuitY+btnQuitHeight:
                    run = False
                    pg.quit()
        drawWorld()
        pg.display.update()

if __name__ == '__main__':
    pygameMenuStart()

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
bg = pg.image.load("Assets\mainMenu\Baggrund.png") #Load Bg
win = pg.display.set_mode((x,y), pg.FULLSCREEN)
pg.display.set_caption("Life of Mark episode 2 - Master The Snake")
icon = pg.image.load("Assets\others\icon.png")
pg.display.set_icon(icon)
select = pg.mixer.Sound("Assets\Sounds\selectMenu.wav")
btnStartX, btnStartY, btnStartHeight, btnStartWidth, btnQuitX, btnQuitY, btnQuitHeight, btnQuitWidth = 841, 500, 60, 238, 872, 600, 58, 176
buttons = Classes.buttons(btnStartX, btnStartY, btnStartHeight, btnStartWidth, btnQuitX, btnQuitY, btnQuitHeight, btnQuitWidth)
startButton1 = Classes.startButton1
quitButton1 = Classes.quitButton1

def drawWorld(baggrundValg):
        mx, my = pg.mouse.get_pos()
        win.blit(bg, (0,0))

        buttons.drawStart()
        buttons.drawQuit()

        if mx > btnStartX and mx < btnStartX+btnStartWidth and my > btnStartY and my < btnStartY+btnStartHeight:
            win.blit(icon, (btnStartX-30, btnStartY))
            win.blit(startButton1, (btnStartX, btnStartY))
            if pg.mixer.Channel(1).get_busy() == False:
                pg.mixer.Channel(1).play(select)
                
        elif mx > btnQuitX and mx < btnQuitX+btnQuitWidth and my > btnQuitY and my < btnQuitY+btnQuitHeight:
            win.blit(quitButton1, (btnQuitX, btnQuitY))
            if pg.mixer.Channel(2).get_busy() == False:
                pg.mixer.Channel(2).play(select)
        
        else:
            buttons.drawStart()
            buttons.drawQuit()

def pygameMenuStart():
    pg.init()
    pg.mixer.music.load("Assets\Sounds\MainMenuMusic.mp3")
    pg.mixer.music.set_volume(0.35)
    pg.mixer.music.play(-1)
    baggrundValg = 21
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
        drawWorld(baggrundValg)
        pg.display.update()

if __name__ == '__main__':
    pygameMenuStart()

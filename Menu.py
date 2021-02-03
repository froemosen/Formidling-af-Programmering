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
btnStartX, btnStartY, btnStartHeight, btnStartWidth, btnQuitX, btnQuitY, btnQuitHeight, btnQuitWidth = 720, 440, 60, 178, 700, 840, 70, 238
buttons = Classes.buttons(btnStartX, btnStartY, btnStartHeight, btnStartWidth, btnQuitX, btnQuitY, btnQuitHeight, btnQuitWidth)
startButton1 = Classes.startButton1
quitButton1 = Classes.quitButton1

def drawWorld(baggrundValg):
        mx, my = pg.mouse.get_pos()
        win.blit(bg, (0,0))

        buttons.drawStart()
        buttons.drawQuit()

        if mx > 850 and mx < 1070 and my > 520 and my < 560:
            win.blit(icon, (783, 480))
            win.blit(startButton1, (720, 440))
            if pg.mixer.Channel(1).get_busy() == False:
                pg.mixer.Channel(1).play(select)
                
        elif mx > 880 and mx < 1035 and my > 930 and my < 965:
            win.blit(quitButton1, (700, 840))
            if pg.mixer.Channel(2).get_busy() == False:
                pg.mixer.Channel(2).play(select)
        
        else:
            win.blit(bg, (0,0))
            buttons.drawStart()
            buttons.drawQuit()

def pygameMenuStart():
    pg.init()
    pg.mixer.music.load("Assets\Sounds\MainMenuMusic.mp3")
    pg.mixer.music.set_volume(0.3)
    pg.mixer.music.play(-1)
    baggrundValg = 21
    run = True
    while run:
        mx, my = pg.mouse.get_pos()
        clock.tick(60)
        baggrundValg = baggrundValg + 1

        if baggrundValg > 61:
            baggrundValg = r.randint(1, 40)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.MOUSEBUTTONDOWN:
                if mx > 850 and mx < 1070 and my > 520 and my < 560:
                    pg.mixer.music.fadeout(1500)
                    Game.start()
                if mx > 880 and mx < 1035 and my > 930 and my < 965:
                    run = False
                    pg.quit()
        drawWorld(baggrundValg)
        pg.display.update()

if __name__ == '__main__':
    pygameMenuStart()
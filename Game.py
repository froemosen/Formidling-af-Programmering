#Imports
import pygame as pg
import os
import Menu

#Window setup
pg.init()
pg.font.init()
pg.mixer.init(frequency=44100, size=-16, channels=6, buffer=4096)
win = pg.display.set_mode((1920, 1080), pg.FULLSCREEN)
keys = pg.key.get_pressed()

#UI load
bg = pg.image.load("Assets\gameSprites\Background.png") #Baggrund load
terminal = pg.image.load("Assets\gameSprites\Terminal.png") #Terminal load
level = pg.image.load("Assets\gameSprites\Baner\Bane0.png") #Default level load
gridSelected = pg.image.load("Assets\gameSprites\Grid100x100.png") #Default grid load
grid100x100 = pg.image.load("Assets\gameSprites\Grid100x100.png") #100x100 grid size (12x7)
grid50x50 = pg.image.load("Assets\gameSprites\Grid50x50.png") #50x50 grid size (24x14)
dnd = pg.image.load("Assets\gameSprites\DnDOptions.png") #DragnDrop window load

#Backgrounds/levels:
levels = [] #Tom liste, fyldes med navne på alle baner herunder
for file in os.listdir("Assets\gameSprites\Baner"): #Bruges til at finde de baner som man kan bruge
    levels.append(file)

#Level assets load
lvlAssets = [] #Tom list - Updaterer i levelSpawn og indeholder banens forhindringer og point. 
rock = pg.image.load("Assets\gameSprites\Obstacles\Sten.png") #Sten-sprite
lake = pg.image.load("Assets\gameSprites\Obstacles\Vandpyt.png") #Vand-sprite
plants = pg.image.load("Assets\gameSprites\Obstacles\Planter.png") #Plante-sprite
food = pg.image.load("Assets\Raspberry-pi\Raspberry.png") #Point-sprite


#Snake assets load
snakePos = []
snakePath = ""
snakeBodyLod = pg.image.load("Assets\gameSprites\Snake\BodyLod.png")
snakeBodyVand = pg.image.load("Assets\gameSprites\Snake\BodyVand.png")
snakeHeadD = pg.image.load("Assets\gameSprites\Snake\HeadD.png")
snakeHeadL = pg.image.load("Assets\gameSprites\Snake\HeadL.png")
snakeHeadR = pg.image.load("Assets\gameSprites\Snake\HeadR.png")
snakeHeadU = pg.image.load("Assets\gameSprites\Snake\HeadU.png")
snakeTailD = pg.image.load("Assets\gameSprites\Snake\TailD.png")
snakeTailL = pg.image.load("Assets\gameSprites\Snake\TailL.png")
snakeTailR = pg.image.load("Assets\gameSprites\Snake\TailR.png")
snakeTailU = pg.image.load("Assets\gameSprites\Snake\TailU.png")
snakeTurnDR = pg.image.load("Assets\gameSprites\Snake\TurnDR.png")
snakeTurnLD = pg.image.load("Assets\gameSprites\Snake\TurnLD.png")
snakeTurnLU = pg.image.load("Assets\gameSprites\Snake\TurnLU.png")
snakeTurnUR = pg.image.load("Assets\gameSprites\Snake\TurnUR.png")



def start(levelID, snakeID):
    pg.mixer.music.load("Assets\Sounds\MainMenuMusic.mp3")
    pg.mixer.music.set_volume(0.35)
    pg.mixer.music.play(-1)

    levelSpawn(levelID) #Create Level from levelID
    snakeSpawn(snakeID) #Create snake from snakeID
    run(snakeID) #Run game


def run(snakeID):
    snakeMove = False
    timeAllowed = True
    snakeCool = False
    snakePath = ("UUULLLLLLLLLLLLLLLLLDDDDDRRRRRRRRRRRUUUUUUULLLLLLLLLLLLLLLLLLLL") #Denne er forudbestemt i denne iteration. I fremtiden vil denne kode skabes af brugerens drag&drop input
    eatSound = pg.mixer.Sound("Assets\Sounds\eatSound.wav")

    while True:
        #Her bør brugerinput tjekkes:
        mx, my = pg.mouse.get_pos() 
        #Hvis startknappen er trykket på, bør følgende operation at begynde
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                snakeMove = True
            

        if snakeMove and len(snakePath)>0 and not snakeCool:
            snakeID = snakeMovement(snakeID, snakePath)
            snakeSpawn(snakeID)
            snakePath = snakePath[1:] #Fjerner første tegn i snakePath
            n = 0

            while n < int(len(lvlAssets)/2):
                if lvlAssets[n] == food: #Hvis asset er et point
                    if abs(lvlAssets[n+1][0] - snakeID[1][0]) < 50 and abs(lvlAssets[n+1][1] - snakeID[1][1]) < 50: #Hvis asset er tættere end 50 pixels på slangehoved
                        snakeID.insert(2, [snakeID[3][0], snakeID[3][1]])
                        snakeID.insert(2, snakeID[3])
                        print("Food was eaten.")
                        pg.mixer.Sound.play(eatSound)
                        del(lvlAssets[n+1], lvlAssets[n])
                
                n += 2
        
        if snakeCool == False: snakeCool = True
        else: snakeCool = False

        #Dette køres uafhængig af det andet
        drawWorld() #Draws world
        pg.display.update() #Updates display. 



def drawWorld():
    #UI draw
    win.blit(bg, (0, 0))
    win.blit(terminal, (1260, 15))
    win.blit(level, (20, 20))
    win.blit(grid100x100, (10, 10))
    win.blit(dnd, (15, 760))
    
    #Assets/Level draw
    no = 0
    for i in range(int(len(lvlAssets)/2)): #For hver anden ting i listen med assets (sprite og position er på to forskellige pladser):
        win.blit(lvlAssets[no], lvlAssets[no+1]) #Tegn sprite (pos0) på position (pos1)
        no += 2 #Tag to næste informationer
    #Snake Draw
    no = 0
    for i in range(int(len(snakePos)/2)):
        win.blit(snakePos[no], snakePos[no+1])
        no += 2


def levelSpawn(levelID):
    global gridSelected #Variablen ændres globalt (ikke kun inden i funktionen)
    global level #Variablen ændres globalt (ikke kun inden i funktionen)
    global lvlAssets #Variablen ændres globalt (ikke kun inden i funktionen)

    levelID = list(levelID) #LevelID laves om til liste, for at kunne tilgås

    #Decode gridsize
    if levelID[0] == "S": #"Small" grid (hvert felt er 100x100 pixels, hvilket giver 12x7 felter)
        gridSelected = grid100x100
        del(levelID[0])
    elif levelID[0] == "B": #"Big" grid (hvert felt er 50x50 pixels, hvilket giver 24x14 felter)
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
            if levelID[0] != "B" or "F" or "L" or "P" or "R" or "Z": #Hvis at levelID[0] ikke skal bruges senere (Hvis den næste item er en item som skal vises på banen):
                del(levelID[0])
            else: #Lvl-code er skrevet forkert ind
                pass
        
    #Decode items
    while len(levelID) > 0: #Længden skulle gerne gå fra ...4 -> 2 -> 0
        #Item
        if levelID[0] == "F":
            lvlAssets.append(food) #Item append
            xoffset = 20+12 #Offset på x-aksen
            yoffset = 20+11 #Offset på y-aksen
        elif levelID[0] == "L":
            lvlAssets.append(lake) #Item append
            xoffset = 20 #Offset på x-aksen 
            yoffset = 20+31 #Offset på y-aksen
        elif levelID[0] == "P":
            lvlAssets.append(plants) #Item append
            xoffset = 20 #Offset på x-aksen
            yoffset = 20+25 #Offset på y-aksen
        elif levelID[0] == "R": 
            lvlAssets.append(rock) #Item append
            xoffset = 20 #Offset på x-aksen
            yoffset = 20+12 #Offset på y-aksen
        #elif levelID[0] == "Z": #Usynlig collision (Når forhindringer er indbygget i banen.)
            #lvlAssets.append()

        #Position
        if levelID[0] == "F" or "L" or "P" or "R" or "Z": #Egentlig unødvendig, men dobbeltcheck
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
            del(levelID[2], levelID[1], levelID[0])


def snakeSpawn(snakeID):
    global snakePos
    snakePos = []
    #Store dele af koden fra levelSpawn benyttes
    #Decode items
    i = 0
    for run in range(int(len(snakeID)/2)):
        #Item
        if snakeID[i] == "BodyLod":
            snakePos.append(snakeBodyLod) #Item append
        elif snakeID[i] == "BodyVand":
            snakePos.append(snakeBodyVand) #Item append
        elif snakeID[i] == "HeadD":
            snakePos.append(snakeHeadD) #Item append
        elif snakeID[i] == "HeadL": 
            snakePos.append(snakeHeadL) #Item append
        elif snakeID[i] == "HeadR": 
            snakePos.append(snakeHeadR) #Item append
        elif snakeID[i] == "HeadU": 
            snakePos.append(snakeHeadU) #Item append
        elif snakeID[i] == "TailD": 
            snakePos.append(snakeTailD) #Item append
        elif snakeID[i] == "TailL": 
            snakePos.append(snakeTailL) #Item append
        elif snakeID[i] == "TailR": 
            snakePos.append(snakeTailR) #Item append
        elif snakeID[i] == "TailU": 
            snakePos.append(snakeTailU) #Item append      
        elif snakeID[i] == "TurnUR" or snakeID[i] == "TurnLD": 
            snakePos.append(snakeTurnDR) #Item append
        elif snakeID[i] == "TurnRD" or snakeID[i] == "TurnUL": 
            snakePos.append(snakeTurnLD) #Item append
        elif snakeID[i] == "TurnRU" or snakeID[i] == "TurnDL": 
            snakePos.append(snakeTurnLU) #Item append
        elif snakeID[i] == "TurnLU" or snakeID[i] == "TurnDR": 
            snakePos.append(snakeTurnUR) #Item append

        if snakeID[i+1][0] < 20 and snakeID[i+1][0] > 0: #Hvis ikke at positionen allerede er opdateret
            #Position
            snakeID[i+1][0] = snakeID[i+1][0]*100+20
            snakeID[i+1][1] = snakeID[i+1][1]*100+20
        
        #Map loop (slangen starter på den anden side af banen, hvis banen forlades)
        if snakeID[i+1][0] > 1120:
            snakeID[i+1][0] = 20
        elif snakeID[i+1][0] < 20:
            snakeID[i+1][0] = 1120

        elif snakeID[i+1][1] > 620:
            snakeID[i+1][1] = 20
        elif snakeID[i+1][1] < 20:
            snakeID[i+1][1] = 620

        snakePos.append(snakeID[i+1])
        
        i += 2
    #print(snakePos)


def snakeMovement(snakeID, snakePath):
    snakePath = list(snakePath)
    #Kroppen laves her - Hale og hoved og stykke efter hoved er i næste dele
    if len(snakeID) >= 6:
        n = -1
        for part in range(len(snakeID)-2):
            try:
                snakeID[n][0] = snakeID[n-2][0]
                snakeID[n][1] = snakeID[n-2][1]
            except:
                snakeID[n] = snakeID[n-2]
            n -= 1

    snakeID[3][0] = snakeID[1][0]
    snakeID[3][1] = snakeID[1][1]
    

    #Hoved og del efter hoved
    if not snakeID[0].replace("Head", "") == snakePath[0]: #Slangen drejer. 
        snakeID[2] = "Turn"+(snakeID[0].replace("Head", ""))+snakePath[0]
        snakeID[0] = "Head"+snakePath[0]

    else: #Slange fortsætter samme retning
        if snakePath[0] == "R" or snakePath[0] == "L":
            snakeID[2] = "BodyVand"
        elif snakePath[0] == "U" or snakePath[0] == "D":
            snakeID[2] = "BodyLod"

    if snakePath[0] == "D": 
        snakeID[1][1] += 100 
    elif snakePath[0] == "U": 
        snakeID[1][1] -= 100
    elif snakePath[0] == "R": 
        snakeID[1][0] += 100
    elif snakePath[0] == "L": 
        snakeID[1][0] -= 100

    #Hale
    if snakeID[-1][0] > snakeID[-3][0]: #Slange er gået til venstre
        snakeID[-2] = "TailL"
    elif snakeID[-1][0] < snakeID[-3][0]: #Slange er gået til højre
        snakeID[-2] = "TailR"
    elif snakeID[-1][1] > snakeID[-3][1]: #Slange er gået til op
        snakeID[-2] = "TailU"
    elif snakeID[-1][1] < snakeID[-3][1]: #Slange er gået til ned
        snakeID[-2] = "TailD"


    #print(snakeID)
    return snakeID
            



if __name__ == '__main__':
    start("S0F11F56Fa4R22L95P74", ["HeadR", [5,4], "BodyVand", [4,4], "BodyVand", [3,4], "BodyVand", [2,4],  "TailR", [1,4]])

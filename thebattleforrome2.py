from time import sleep
import sys
import random
import math
from datetime import date, time, datetime, timedelta
import pygame as pg
#Homebrew Classes
from Proclass import pro
from GunClass import Cgun
from BulletClass import Bullet
from VillainClass import villain
from RoomClass import rooms
from BossClass import boss
from ObjClass import article
pg.init()
pg.mixer.init()
fps=30
fpsclock=pg.time.Clock()
screen =pg.display.set_mode((1920,1080), pg.FULLSCREEN)
#screen =pg.display.set_mode((1920,1080))
screen.fill([100,100,100])
mouse = pg.image.load('mouse.png')
arrowforward = pg.image.load('arrow.png')
blink_i = 0
pg.font.init()

'''
def background(x, img):
    back = pg.image.load(img)
    screen.blit(back, (x + 30, -90))
'''

def dist(x1, y1, x2, y2):
    dist = math.sqrt(((x1-x2)**2) + ((y1-y2)**2))
    return(dist)


def sound(s):
    hear = pg.mixer.Sound(s)
    hear.play()

def write(txt, size, color, cords):
    myfont = pg.font.SysFont('arial', size)
    textsurface = myfont.render(txt, False, color)
    screen.blit(textsurface, cords)


    
English = ['France', 'Germany', 'Africa', 'Spain', 'Sicily', 'Britain', 'Italy', 'Rome']
Latin = ['Galia','Germania','Africa','Hispania','Sicilia','Britannia','Italia', 'Roma']
rimgs= ['r1.png','r2.png','r3.png','r4.png','r5.png','r6.png','r7.png','r8.png', 'final.png']

LatinRoute = ['Rome', 'Africa','Hispania' ,'Macedonia','Sicilia' ,'Germania','Brittania' ,'Aegyptus', None]
routeid = 1
#1,3,4,6,7
roomsin = []
roomid = 0

sphinxstage = datetime.now()
sstage1 = False
sstage2 = False
sstage3 = False
sstage4 = False

jstage = 1

cords = [50, 200, 400, 600, 800, 1000]
itcords = 0
walk = ['protagwalk.png', 'protagwalk2.png', 'protagwalk3.png', 'protagwalk4.png', 'protagwalk5.png']
axe_it = 0
axeani = ['axe1.png','axe2.png','axe3.png','axe4.png','axe5.png','axe6.png',]
walk_i = 0
pg.mouse.set_visible(False)
hero = pro(200)
gun = Cgun('Pistol.png', 'Pistol', 2, hero.getY(), hero.getX(),hero.getrectpro(), 'range')
jump = False
hero.setY(850)
blinktime = datetime.now() + timedelta(seconds = 3)
walktime = blinktime = datetime.now() + timedelta(seconds = 0)
Bul_list = []
vil_list = []
villains = []
platforms = []
bosses = []
spawnVillainTime = datetime.now()
spawnVillainTime2 = datetime.now()
spawnVillainTime3 = datetime.now()
bossstagetime = datetime.now()
bossstagetime2 = datetime.now()
spawnVillainTime4 = datetime.now()
bossSoundTimer = datetime.now()
spawnVillainTime5 = datetime.now()
damageFromSwordTimer = datetime.now()
spawnVillainTime6 = datetime.now()
spawnVillainTime7 = datetime.now()
spawnElephant = True
plat0 = True
plat1 = True
ceasarspearwield = True
chariotspawncleo = False
shieldout = datetime.now()
infantryShootingTime = datetime.now()
hannibalShootingTime = datetime.now()
relTime = datetime.now()
gun = Cgun('Pistol.png', 'Pistol', 2, hero.getY(), hero.getX(),hero.getrectpro(), 'range')
swordeffect = True
wincondition = True
while roomid < 8:
    print(roomid,Latin[roomid] ,English[roomid] ,rimgs[roomid])
    r = rooms(roomid,Latin[roomid] ,English[roomid] ,rimgs[roomid])
    roomid += 1
    roomsin.append(r)



currentroom = 0
shielddefense = False
Swordout = False
villainspawn = True
plat3 = True
health = 50
backscroll = -90
plat3lvl2 = False
Sphinxspawn = True
plat7 = True
readyforfinallvl = False
platlvlon = 1
plat33Xloc = 51
plat33Xloc2 = 1801
swordHitTimer = datetime.now()
changerooms = False
#INTRO LOOP (mit s wll)
Ycord = 50
pg.mixer.music.load("startscreen.wav")
pg.mixer.music.play(0)
startvar = "startscreen2.jpg"
while True:
    print(currentroom)
    scrn = pg.image.load(startvar)

    key_input = pg.key.get_pressed()

    for eve in pg.event.get():
        if eve.type==pg.QUIT:
            pg.quit()
            sys.exit()
            
    if (key_input[pg.K_r]):
        startvar = ("startscreen.jpg")
    if (key_input[pg.K_q]) and startvar == "startscreen.jpg":
        break

    screen.blit(scrn, [0,0])
    pg.display.update()


flipped = False
platmovment33 = 10
platmovment33_1 = 10
pg.mixer.music.load("maintrack.wav")
pg.mixer.music.play(0)
soundplayeddoor = False
JuliusSpawn = False
platFINAL = False
charge = False
over = False
JuliusMove = 10
currentroom = 0


print("Fin")
timetowrite = datetime.now()
mover = 800
text = 'The Battle for Rome 2'
textlist = ["The Battle for Rome 2", "Created by Justin Verlin", "Thank you to Mrs Mullay for giving me the neccesary time to complete this!"]
#MAIN LOOP+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
while True:
    if currentroom == 2 or currentroom == 4 or currentroom == 6:
        pg.quit()
        sys.exit()
    if over == True:
        fps = 0
        backscroll -=4
        back = pg.image.load('r4-1 - Copy.png')
        bosses.clear()
        platforms.clear()
        villains.clear()
        hero.setX(99999)
        if datetime.now() >= timetowrite:
            bossstagetime = datetime.now() + timedelta(seconds = 20)
            mover = 800
        mover -= 10
        write(text, 50, [255,255,255], (600, mover))
        



        
    if currentroom != 8:
        if jump != True and hero.getY() <= 850 and platlvlon != 2:
            hero.changeY(25)
        elif jump != True and hero.getY() <= 1200 and platlvlon == 2:
            hero.changeY(25)
            if hero.getY() >= 1050:
                hero.constantY(800)
                hero.setX(50)
    elif currentroom ==8:
        if jump != True and hero.getY() <= 800 and platlvlon != 2:
            hero.changeY(25)
        



    Swordout = False
    for obj in roomsin:
        if currentroom == obj.getid() and currentroom != roomid:
            back = pg.image.load(obj.getimg())
            roomid = obj.getid()
    if currentroom != 8:
        screen.blit(back, (0, -90))
    elif currentroom ==8: 
        screen.blit(back, (backscroll, -90))
        backscroll -=1
        
        screen.blit(aq, (0, 900))
        
    blink = True
    gun.setgunrect(hero.getX(),hero.getY() )
# CONTROLS ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    key_input = pg.key.get_pressed()
    for eve in pg.event.get():
        
        if eve.type==pg.QUIT:
            pg.quit()
            sys.exit()
    
        if pg.mouse.get_pressed()[0] and datetime.now() >= relTime and gun.getrorm() == 'range':
            sound("shot.wav")
            soundplayeddoor = True
            relTime = datetime.now() + timedelta(seconds = 2)
            #print('BAM')
            gun.rotate()
            B = Bullet(gun.getgunX(), gun.getgunY(), 'pistol', gun.getF(), gun.rotate(), False, (139,69,19), 0, 0,screen, 2)
            Bul_list.append(B)
            swordeffect = True

    if (key_input[pg.K_d]) or (key_input[pg.K_a]):
        blink = False
        if datetime.now()>walktime:
            try:
                walk_i +=1
                hero.setimgpro(walk[walk_i])
                walktime = blinktime = datetime.now() + timedelta(seconds = .1)
            except:
                walk_i = 0
        
    
    if (key_input[pg.K_d]):
        if (key_input[pg.K_LSHIFT]):
            hero.moveproright(12)
        else:
            hero.moveproright(8)
        blink = False
        gun.setgunrect(hero.getX(),hero.getY() )
    
    gun = Cgun('Pistol.png', 'Pistol', 2, hero.getY(), hero.getX(),hero.getrectpro(), 'range')
    if pg.mouse.get_pressed()[2]:
        
        if swordeffect == True:
            sound('sword.wav')
            swordeffect = False
            
        gun = Cgun('Sword.png', 'Pistol', 2, hero.getY(), hero.getX(),hero.getrectpro(), 'melee')
        Swordout = True
        
        #bullet = pg.draw.rect(screen, (255,255,255), ( gun.getgunX() + 100, gun.getgunY(), 10,5))
        

        #Swordbullet = Bullet(gun.getgunX(), gun.getgunY(), 'pistol', gun.getF(), gun.rotate(), False, (139,69,19), 0, 0,screen)
        #Swordbullet.swordCreate()

    if (key_input[pg.K_ESCAPE]):
        pg.quit()
        sys.exit()
        
    if (key_input[pg.K_a]):

        if (key_input[pg.K_LSHIFT]):
            hero.moveproleft(-12)
        else:
            hero.moveproleft(-8)
        hero.flipimg()
        gun.flipimg()
        gun.setgunrect(hero.getX(),hero.getY())
        blink = False
        
    if (key_input[pg.K_SPACE]):
        jump = True
        blink = False
    if jump == True:
        hero.setY(hero.jump())
        gun.setgunrect(hero.getX(),hero.getY() )
        blink = False
        if hero.getmoveY() >= 50:
            jump = False
            
#Controls End ______________________________________________________

        
#rooooooooooooooooooooooommmmmmmmmmmmmmsssssss
    if wincondition == True:
        exitdr = pg.image.load("exit.png")
        screen.blit(exitdr, [1823, 850])
        
    if hero.getX() >= 1823 and wincondition == True:
        changerooms = True

    if changerooms == True:

        for obj in platforms:
            platforms.remove(obj)
        if readyforfinallvl  == False:

            plat3lvl2 = False
            platlvlon = 1
            hero.hide()
            hero.resethealth()
            hero.setX(10828)
            villainspawn = False
            for obj in villains:
                villains.remove(obj)

            back = pg.image.load("doorback.png")
            
            doorA = pg.image.load("door.png")
            doorB = pg.image.load("door.png")
            

            x, y = (pg.mouse.get_pos())

            if x > 1300 and x < 1700 and y > 300 and y < 900 and wincondition == True:
                doorB = pg.image.load("selecteddoor.png")
                write(str(LatinRoute[routeid]),25 ,[0, 0, 0] ,[1500, 270])
                if soundplayeddoor == True:
                    sound("doorknob.wav")
                    soundplayeddoor = False

                if pg.mouse.get_pressed()[0] and wincondition == True:
                    currentroom = routeid
                    routeid += 2
                    hero.unhide()
                    hero.setX(0)
                    villainspawn = True
                    wincondition = False
                    changerooms = False
            elif x > 300 and x < 700 and y > 300 and y < 900 and wincondition == True:
                doorA = pg.image.load("selecteddoor.png")
                write(str(LatinRoute[(routeid + 1)]),25 ,[0, 0, 0] ,[500, 270])
                if soundplayeddoor == True:
                    sound("doorknob.wav")
                    soundplayeddoor = False
                if pg.mouse.get_pressed()[0] and wincondition == True:
                    currentroom = (routeid + 1)
                    routeid += 2
                    hero.unhide()
                    hero.setX(0)
                    wincondition = False
                    villainspawn = True
                    changerooms = False

                    
        elif readyforfinallvl == True:
            villains.clear()
            plat3lvl2 = False
            back = pg.image.load("doorback.png")
            wincondition = True
            platlvlon = 1
            hero.hide()
            hero.resethealth()
            hero.setX(10828)
            villainspawn = False
            doorA = pg.image.load("door.png")
            doorB = pg.image.load("nothing.png")
            x, y = (pg.mouse.get_pos())
            if x > 800 and x < 1200 and y > 300 and y < 900 and wincondition == True:
                doorA = pg.image.load("selecteddoor.png")
                write("Julius Ceasar",25 ,[0, 0, 0] ,[1000, 270])
                print("Doorselected")
                if pg.mouse.get_pressed()[0] and wincondition == True:
                    currentroom = 8
                    hero.unhide()
                    hero.setX(0)
                    wincondition = False
                    villainspawn = False
                    changerooms = False
                    readyforfinallvl = False
                    back = pg.image.load('Scroll Through.png')
                    aq = pg.image.load('Final(Front).png')
                    hero.constantY(800)
                    JuliusSpawn = True
                    platFINAL = True
                    pg.mixer.music.load("FInalboss.wav")
                    pg.mixer.music.play(0)

                    
                
        if currentroom != 7:     
            screen.blit(doorB, [1300, 300])
            screen.blit(doorA, [300, 300])
        else:
            screen.blit(doorA, [800, 300])
#Bullets/Animtion/Sword-----------------------------------------------------------------------------
    
    for obj in Bul_list:
        obj.create()
        obj.move()

        
    else:
        if blink == True:
            blink_an = ["protag.png","protag(b1).png", "protag(b2).png", "protag(b3).png", "protag(b2).png", "protag(b1).png", "protag.png" ]
            if datetime.now()>blinktime:
                blink_i +=1
                try:
                    hero.setimgpro(blink_an[blink_i])
                    blinktime = datetime.now() + timedelta(seconds = 0.1)
                except:
                    blink_i = 0
                    blinktime = datetime.now() + timedelta(seconds = random.randint(3,6))


    #Villians_______________________________________________________
    
    if villainspawn == True:
        #Spearmen:

        if currentroom == 0:
            if datetime.now() >= spawnVillainTime:
                spawnVillainTime = datetime.now() + timedelta(seconds = 3)
                SP = villain("SP", 10, "Spearman1.png", 1, screen, (2000, 850) )
                villains.append(SP)
            #Infantry
            if datetime.now() >= spawnVillainTime2:
                 spawnVillainTime2 = datetime.now() + timedelta(seconds = 8)
                 IF = villain("IF", 3, "Infantry.png", 1, screen, (2000, 850))
                 villains.append(IF)
            #Shieldman
            if datetime.now() >= spawnVillainTime3:
                spawnVillainTime3 = datetime.now() + timedelta(seconds = 5)
                SH = villain("SH", 5, "RomanLeggionare.png", 1, screen, (2000, 850))
                villains.append(SH)
        elif currentroom == 3 or sstage1 == True:
             if datetime.now() >= spawnVillainTime4 and platlvlon == 1:
                 spawnVillainTime4 = datetime.now() + timedelta(seconds = 5)
                 CA = villain("CA", 8, "Chariot.png", 2, screen, (2000, 780))
                 villains.append(CA)
        elif currentroom == 5:
             if datetime.now() >= spawnVillainTime5:
                 spawnVillainTime5 = datetime.now() + timedelta(seconds = 8)
                 AX = villain("AX", 4, "AxeThrower.png", 1, screen, (2000, 820))
                 villains.append(AX)
                 wincondition = True

             if datetime.now() >= spawnVillainTime6:
                 spawnVillainTime6 = datetime.now() + timedelta(seconds = random.randint(8, 11))
                 B = villain("B", 2, "Beserker.png", 3, screen, (2000, 750))
                 villains.append(B)
        print(currentroom)
        if sstage2 == True and datetime.now() >= spawnVillainTime7 and currentroom == 7:
            print("spawning")
            spawnVillainTime7 = datetime.now() + timedelta(seconds = random.randint(5,8))
            SNAKE = boss("SNAKE", 10, "snake.png", 1, screen, (1500, 920), 'elephantsound.wav')
            villains.append(SNAKE)

         
    for vil in villains:
        vil.create()
        vil.move()

        if hero.getrectpro().colliderect(vil.getvilrect()):
            hero.sethealth(20)
        
        if gun.getgunrect().colliderect(vil.getvilrect()) and gun.getrorm() == 'melee' and vil.gettype() != "SH" :
            spawnVillainTime3 = datetime.now() + timedelta(seconds = 2)
            vil.sethealth(1)
            
        elif gun.getgunrect().colliderect(vil.getvilrect()) and vil.gettype() == "SH" and shielddefense == False:
            vil.sethealth(1)
            spawnVillainTime3 = datetime.now() + timedelta(seconds = .5)
        elif gun.getgunrect().colliderect(vil.getvilrect()) and vil.gettype() == "SH" and shielddefense != False:
            pass

        for bul in Bul_list:
            if vil.getvilrect().colliderect(bul.getbulrect()) and vil.gettype() != "SH":
                vil.sethealth(1)
                Bul_list.remove(bul)
                
            elif  vil.getvilrect().colliderect(bul.getbulrect()) and vil.gettype() == "SH" and shielddefense == False:
                vil.sethealth(1)
                #print("KillShieldboy")
                Bul_list.remove(bul)

            elif  vil.getvilrect().colliderect(bul.getbulrect()) and vil.gettype() == "SH" and shielddefense == True:
                sound("shieldbloc.wav")
                Bul_list.remove(bul)

            

                
            '''
            elif shielddefense == True:
                sound("shieldbloc.wav")
                Bul_list.remove(bul)
            '''
            
        
        
        
        if vil.gethealth() <= 0:
            sound('swordhit.wav')
            villains.remove(vil)


        if vil.gettype() == "IF":
            x = (dist(hero.getX(), hero.getY(), vil.getX(), vil.getY()))
            if x <= 1000:
                vil.setspeed(0)
            if datetime.now() > infantryShootingTime and vil.getspeed() == 0:
                infantryShootingTime = datetime.now() + timedelta(seconds = 3)
                sound('shoot.wav')
                cords = (hero.getX(),  hero.getY() + 20)
                tarcordx, tarcordy = cords
                VB = Bullet((vil.getX() - 80), (vil.getY() + 40), 'pistol', None, gun.rotate(), True, (251,95,95), tarcordx, tarcordy, screen, 50)
                vil_list.append(VB)


        if vil.gettype() == "AX":
            x = (dist(hero.getX(), hero.getY(), vil.getX(), vil.getY()))
            if x <= 1000:
                vil.setspeed(0)
            if datetime.now() > infantryShootingTime and vil.getspeed() == 0:
                sound('shoot.wav')
                infantryShootingTime = datetime.now() + timedelta(seconds = 3)
                cords = (hero.getX(),  hero.getY() + 20)
                tarcordx, tarcordy = cords
                VB = Bullet((vil.getX() - 80), (vil.getY() + 40), 'axe', None, gun.rotate(), True, (231,75,75), tarcordx, tarcordy, screen, 25)
                vil_list.append(VB)


        elif vil.gettype() == "CA":
            if datetime.now() > infantryShootingTime:
                infantryShootingTime = datetime.now() + timedelta(seconds = 2)
                sound('shoot.wav')
                #cords = (hero.getX() + 30,  hero.getY() + random.randint(-10, 10))
                cords = (hero.getX(),  hero.getY() + 20)
                tarcordx, tarcordy = cords
                VB = Bullet((vil.getX() - 100), (vil.getY() + 60), 'pistol', None, gun.rotate(), True, (231,75,75), tarcordx, tarcordy, screen, 25)
                vil_list.append(VB)
            if vil.getX() <= 50:
                vil.flip()
                
        if vil.gettype() == "SH" and datetime.now() >= shieldout:
            shieldout = datetime.now() + timedelta(seconds = random.randint(3,8))
            if shielddefense == True:
                shielddefense = False
            else:
                shielddefense = True
        

        if shielddefense == True and vil.gettype() == 'SH':
            shieldimg = pg.image.load("shield.png")
            screen.blit(shieldimg, [vil.getX() + 40, vil.getY()])
            
               
    for obj in vil_list:
        obj.create()
        obj.move()
        #sound('shoot.wav')
        if obj.getX() <= -100:
            vil_list.remove(obj)
        if obj.getbulrect().colliderect(hero.getrectpro()):
            hero.sethealth(obj.getDamage())
            vil_list.remove(obj)
        if obj.getType() == "axe":

            try:           
                axeimg = pg.image.load(axeani[axe_it])
                obj.setimg(axeimg)
                screen.blit(axeimg, obj.getbulrect())
                axe_it += 1
            except:
                axe_it = 0
                
        if obj.getType() == 'rock':
            rockimg = pg.image.load('Brock.png')
            obj.setimg(rockimg)
            screen.blit(rockimg, obj.getbulrect())

    write(str(hero.gethealth()) + "/200", 30, [255,0,0], [25, 50])
    if hero.gethealth() <= 0:
        villains.clear()
        bosses.clear()        
        spawnElephant = True
        Sphinxspawn = True
        JuliusSpawn = True
        backscroll = -90
        jstage = 1
        if currentroom ==7:
            sstage1 = True
            sstage2 = False
            sstage3 = False
            sstage4 = False
        hero.setX(0)
        hero.resethealth()
       # print("You lost")

#Bosses+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    if spawnElephant == True and currentroom == 1:
        WE = boss("WE", 2, "Elephant.png", 3000, screen, (1599, 300), 'elephantsound.wav')
        bosses.append(WE)
        H = boss("H", 2, "hannibal.png", 30, screen, (2250, 350), 'elephantsound.wav')
        bosses.append(H)
        spawnElephant = False
    if Sphinxspawn == True and currentroom == 7:
        SP = boss("SP", 0, "Sphinx.png", 3000, screen, (1300, 500), 'elephantsound.wav')
        bosses.append(SP)
        C = boss("C", 0, "Cleo.png", 50, screen, (1500, 320), 'elephantsound.wav')
        bosses.append(C)
        Sphinxspawn = False
    if JuliusSpawn == True and currentroom == 8:
        print("Julius")
        J = boss("J", 0, "Julius.png", 120, screen, (1500, 550), 'elephantsound.wav')
        bosses.append(J)
        #jstage = 1
        JuliusSpawn = False
    if backscroll <= -12700:
        backscroll = -90
#GODMODE POWERS+++++++++++++++++++++++++++++++++
    #hero.resethealth()

#-------------------------------------------
    for obj in bosses:
        obj.create()
        obj.move()
        
        print(obj.gethealth())
        
        if obj.gethealth() <= 20 and obj.gettype() == 'J':
            over = True
            backscroll = -90
            print("OVER")
            
        if obj.gettype() == "J":

                
            if obj.getX() <= 50 or obj.getX() >= 1750:
                obj.flip()
            if gun.getgunrect().colliderect(obj.getvilrect()) and gun.getrorm() == 'melee' and datetime.now() >= swordHitTimer:
                    swordHitTimer = datetime.now() + timedelta(seconds = 0.5)
                    obj.sethealth(1)
                    
            for bul in Bul_list:
                if bul.getbulrect().colliderect(obj.getvilrect()):
                    obj.sethealth(2)
                    Bul_list.remove(bul)

            if obj.getvilrect().colliderect(hero.getrectpro()) and jstage == 5:
                hero.sethealth(5)
                
            if datetime.now() >= bossstagetime:
                bossstagetime = datetime.now() + timedelta(seconds = 30)
                jstage +=1
                if jstage >= 7:
                    jstage = 1
            if jstage == 1:
                obj.setloc(1500, 550)
                obj.setimg('Julius.png')
                hero.resethealth()
            elif jstage ==2:
                obj.setimg('CrossJulius.png')
                
                if datetime.now() >= hannibalShootingTime:
                    hannibalShootingTime = datetime.now() + timedelta(seconds = 0.2)
                    Ycord += 100
                    print(Ycord)
                    tarcordx = 50
                    sound("shoot.wav")
                    tarcordy = Ycord
                    JB = Bullet((obj.getX()), (obj.getY() + 130), 'pistol', None, gun.rotate(), True, (231,75,75), tarcordx, Ycord, screen, 10)
                    vil_list.append(JB)
                    if Ycord >= 1001:
                        Ycord = 50
            elif jstage ==3:
                obj.setimg('ChargeJulius.png')

                if datetime.now() >= spawnVillainTime4 and platlvlon == 1:
                     spawnVillainTime4 = datetime.now() + timedelta(seconds = 5)
                     CA = villain("CA", 8, "Chariot.png", 2, screen, (2000, 780))
                     villains.append(CA)
                     
                if datetime.now() >= spawnVillainTime3:
                    spawnVillainTime3 = datetime.now() + timedelta(seconds = 5)
                    SH = villain("SH", 5, "RomanLeggionare.png", 1, screen, (2000, 820))
                    villains.append(SH)

                if datetime.now() >= spawnVillainTime2:
                     spawnVillainTime2 = datetime.now() + timedelta(seconds = 8)
                     IF = villain("IF", 3, "Infantry.png", 1, screen, (2000, 800))
                     villains.append(IF)

            elif jstage == 4:
                villains.clear()
                obj.setimg("fireJulius.png")
                if datetime.now() >= hannibalShootingTime:
                    hannibalShootingTime = datetime.now() + timedelta(seconds = 0.8)
                    cords = (hero.getX(),  hero.getY() + 20)
                    tarcordx, tarcordy = cords
                    print(cords)
                    sound("shoot.wav")
                    JB = Bullet((obj.getX()), (obj.getY() + 130), 'pistol', None, gun.rotate(), True, (231,75,75), tarcordx, tarcordy, screen, 10)
                    vil_list.append(JB)
            elif jstage == 5:
                if ceasarspearwield == True:
                    obj.setimg("spearJulius.png")
                    ceasarspearwield = False
                print(obj.getX())
                obj.setspeed(JuliusMove)

                    
            elif jstage ==6:
                ceasarspearwield = True
                obj.setspeed(0)
                obj.setloc(1500, 400)
                obj.setimg('Juliusrock1.png')
                if datetime.now() >= hannibalShootingTime:
                    obj.setimg('Juliusrock2.png')
                    hannibalShootingTime = datetime.now() + timedelta(seconds = 3)
                    cords = (hero.getX(),  hero.getY() + 20)
                    tarcordx, tarcordy = cords
                    print(cords)
                    sound("shoot.wav")
                    JB = Bullet((obj.getX()), (obj.getY() + 130), 'rock', None, gun.rotate(), True, (231,75,75), tarcordx, tarcordy, screen, 50)
                    vil_list.append(JB)






        
        if currentroom == 7 and obj.gettype() != "SP":
            if gun.getgunrect().colliderect(obj.getvilrect()) and gun.getrorm() == 'melee' and datetime.now() >= swordHitTimer:
                swordHitTimer = datetime.now() + timedelta(seconds = 0.5)
                obj.sethealth(2)
                
            for bul in Bul_list:
                if bul.getbulrect().colliderect(obj.getvilrect()):
                    obj.sethealth(2)
                    Bul_list.remove(bul)

        if datetime.now() > hannibalShootingTime and obj.gettype() == 'C' and sstage3 != True:
            hannibalShootingTime = datetime.now() + timedelta(seconds = random.randint(3,5))
            cords = (hero.getX(),  hero.getY() + 20)
            tarcordx, tarcordy = cords
            sound("shoot.wav")
            VB = Bullet((obj.getX() + 80), (obj.getY() + 40), 'pistol', None, gun.rotate(), True, (255,69,0), tarcordx, tarcordy, screen, 10)
            vil_list.append(VB)
            
        elif datetime.now() > hannibalShootingTime and obj.gettype() == 'SP' and sstage3 == True:
                hannibalShootingTime = datetime.now() + timedelta(seconds = 0.5)
                Ycord += 100
                print(Ycord)
                tarcordx = 50
                tarcordy = Ycord
                sound("shoot.wav")
                VB = Bullet((obj.getX() + 300), (obj.getY() + 300), 'pistol', None, gun.rotate(), True, (231,75,75), tarcordx, Ycord, screen, 10)
                vil_list.append(VB)
                if Ycord >= 1001:
                    Ycord = 50
                
        if obj.gettype() == "C": 
            health = obj.gethealth()
            
            if sstage4 == True:
                obj.setloc(900, 850)
            elif sstage4 != True:
                obj.setloc(1500, 425)

            if obj.gethealth() <= 0:
                wincondition = True
                bosses.clear()
                platforms.clear()
                readyforfinallvl = True
        
                
        if obj.gettype() == 'SP' and currentroom == 7:
            if datetime.now() >= bossstagetime:
                bossstagetime = datetime.now() + timedelta(seconds = 20)
                if sstage4 == True:
                    sstage4 = False
                    sstage3 = False
                    sstage2 = False
                    sstage1 = True
                    
                elif sstage3 == True:
                    sstage3 = False
                    sstage4 = True

                elif sstage2 == True:
                    sstage2 = False
                    sstage3 = True
                    
                elif sstage1 == True:
                    sstage1 = False
                    sstage2 = True
                    
                elif sstage1 == False:
                    sstage1 = True
                
                    
                
                '''
            elif datetime.now() >= bossstagetime2:
                bossstagetime = datetime.now() + timedelta(seconds = 20)
                sstage1 = False
                '''

    



                
                
        if obj.gethealth() <= 0 and obj.gettype != 'J':
            wincondition = True
            for obj in bosses:
                bosses.remove(obj)
            for plats in platforms:
                platforms.remove(plats)
            
        if obj.getX() <= -300 or obj.getX() >= 1600 and obj.gettype() == "WE":
           obj.flip()
           flipped = True
           
        if flipped == True and obj.gettype() == "H":
            obj.flip()
            flipped = False
            
        if obj.gettype() == "H":
            #obj.create()
            #obj.move()

            if gun.getgunrect().colliderect(obj.getvilrect()) and gun.getrorm() == 'melee' and datetime.now() >= swordHitTimer:
                swordHitTimer = datetime.now() + timedelta(seconds = 0.5)
                obj.sethealth(1)

            for bul in  Bul_list:
                if bul.getbulrect().colliderect(obj.getvilrect()):
                    obj.sethealth(2)
                    Bul_list.remove(bul)


            if datetime.now() > hannibalShootingTime:
                hannibalShootingTime = datetime.now() + timedelta(seconds = random.randint(1, 2))
                sound('shoot.wav')
                cords = (hero.getX(),  hero.getY() + 20)
                tarcordx, tarcordy = cords
                VB = Bullet((obj.getX() - 80), (obj.getY() + 40), 'pistol', None, gun.rotate(), True, (231,75,75), tarcordx, tarcordy, screen, 10)
                vil_list.append(VB)
            
        if obj.gettype() == "WE":
            
            hitbox = pg.draw.rect(screen, [0,0,0, 0], (obj.getX() + 500, obj.getY() + 255, 600 ,obj.getY() + 75  ), 1)
            #obj.create()
            #obj.move()

            if datetime.now() >= bossSoundTimer:
                bossSoundTimer = datetime.now() + timedelta(seconds = random.randint(3, 8))               
                sound(obj.getsound())

            if hero.getrectpro().colliderect(hitbox):
                hero.sethealth(1)



#Platforms______________________________________________________________________________________________
    if currentroom == 0 and plat0 == True:
        plat0 = article(700, 750, 200, 25, screen, "First Level Plat")
        platforms.append(plat0)
        plat0 = False
        
    elif currentroom == 1 and plat1 == True:
        plat1 = article(WE.getX(), 720, 50, 25, screen, "WE trunk")
        platforms.append(plat1)

        plat1_1 = article(WE.getX() + 500, 680, 50, 25, screen, "WE tail")
        platforms.append(plat1_1)
        
        plat12 = article(WE.getX() + 500, 500, 450, 25, screen, "WE trunk 2")
        platforms.append(plat12)

        hanhealht = article(900, 1000, 440, 25, screen, "Hannibal Health")
        platforms.append(hanhealht)
        
        plat1 = False

    elif currentroom == 3 and plat3 == True:

        plat3 = article(1200, 500, 75, 25, screen, "Parcore1")
        platforms.append(plat3)

        plat32 = article(1450, 720, 150, 25, screen, "Parcore2")
        platforms.append(plat32)

        plat33 = article(1300, 300, 150, 25, screen, "Parcore3")
        platforms.append(plat33)

        plat34 = article(50, 100, 75, 25, screen, "Parcore4")
        platforms.append(plat34)

        plat3 = False


    elif currentroom == 7 and plat7 == True:
        plategypt = article(500, 750, 150, 25, screen, "egypthelp")
        platforms.append(plategypt)

        cleohealth = article(900, 1000, 440, 25, screen, "CleoHealth")
        platforms.append(cleohealth)
        plat7 = False
        
    elif plat3lvl2 == True:

        for obj in platforms:
            platforms.remove(obj)

        plat3_1 = article(50, 1000, 75, 25, screen, "Parcore1-2")
        platforms.append(plat3_1)

        plat3_1_1 = article(300, 800, 100, 25, screen, "Parcore1-2")
        platforms.append(plat3_1_1)

        plat3_1_2 = article(700, 800, 25, 25, screen, "Parcore1-2")
        platforms.append(plat3_1_2)

        
        plat3_1_3 = article(1000, 700, 100, 25, screen, "Parcore1-2")
        platforms.append(plat3_1_3)

        plat4_1 = article(55, 500, 100, 25, screen, "Parcore2-2")
        platforms.append(plat4_1)


        plat5_1 = article(1300, 300, 30, 25, screen, "Parcore3-2")
        platforms.append(plat5_1)


        platfin = article(50, 100, 75, 25, screen, "ParcoreFINAL")
        platforms.append(platfin)

        plat3lvl2 = False

    elif platFINAL == True:
        platfin1 = article(300, 500, 125, 25, screen, "FINAL1")
        platforms.append(platfin1)

        platfin2 = article(300, 700, 125, 25, screen, "FINAL2")
        platforms.append(platfin2)


        jh = article(550, 25, 125, 25, screen, "JULIUSHEALTH")
        platforms.append(jh)
        
        platFINAL = False
        
   
    if platlvlon == 2 or platlvlon == 3:
        for obj in villains:
            villains.remove(obj)
            
    for obj in platforms:
        obj.createplatform()
        if obj.getID() == "CleoHealth":
            obj.setwidth(health * 10)

        if obj.getID() == "ParcoreFINAL":
            screen.blit(exitdr, [45, 25])
            if hero.getrectpro().colliderect(obj.getplat()):
                for obj in platforms:
                    platforms.remove(obj)
                wincondition = True    
                changerooms = True

        if hero.getrectpro().colliderect(obj.getplat()):
            hero.constantY(int(obj.getY() - 100))

        if obj.getID() == "Parcore4":
            if hero.getrectpro().colliderect(obj.getplat()):
                back = pg.image.load('r4-1.png')
                platforms.remove(obj)
                hero.constantY(1000)
                hero.resethealth()
                plat3lvl2 = True
                platlvlon += 1
                for obj in platforms:
                    platforms.remove(obj)
                platmovment33 = platmovment33 * -1

                
        if obj.getID() == "Parcore3" or obj.getID() == "Parcore3-2":
            plat33Xloc += platmovment33
            obj.setX(plat33Xloc)
            if plat33Xloc >= 1802:
                platmovment33 = platmovment33 * -1
            elif plat33Xloc <= 50:
                platmovment33 = platmovment33 * -1
                
        if obj.getID() == "Parcore2-2":
            plat33Xloc2 += platmovment33_1 * -1
            obj.setX(plat33Xloc2)
            if plat33Xloc2 >= 1800:
                platmovment33_1 = platmovment33_1 * -1
            elif plat33Xloc2 <= 50:
                platmovment33_1 = platmovment33_1 * -1
        
        for bos in bosses:
            if bos.gettype() == "WE":
                if obj.getID() == "WE trunk":
                    obj.setX(bos.getX() + 300)

                if obj.getID() == "WE tail":
                    obj.setX(bos.getX() + 1200)

                if obj.getID() == "WE trunk 2":
                    obj.setX(bos.getX() + 630)

            if obj.getID() == "Hannibal Health" and bos.gettype() == "H":
                obj.setwidth(bos.gethealth() * 10)
            if obj.getID() == "JULIUSHEALTH" and bos.gettype() == "J":
                obj.setwidth((bos.gethealth() - 20) * 10)     
    
    #____________________
    #Loop Ending------------------------------------
                                 
    gun.rotate()
    gun.setgunrect(hero.getX() - 100 ,hero.getY() + random.randint(-30, 30))
    
    screen.blit(hero.getimgpro(), hero.getrectpro())
    
    try:
        screen.blit(gun.getimg(), gun.getrect())
    except:
        screen.blit(gun.gunimg(), gun.getrect())
    screen.blit(mouse, pg.mouse.get_pos())
    
    pg.display.flip()
    pg.display.update()
        
    fpsclock.tick(fps)

#CREDITS==============

#txt, size, color, cords


    































    


    


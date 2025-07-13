import pygame
from GunClass import Cgun
class Bullet(Cgun):

    def __init__(self, x, y, typ, f, angle, enem, color, tarX, tarY, screen, damage):
        self.x = x
        self.y = y
        self.typ = typ
        self.f = f
        self.angle = angle
        print(self.angle)
        print(self.f)
        self.enem = enem
        self.color = color
        self.screen = screen
        #if self._typ == 'pistol':
        self.damage = damage
        img = pygame.image.load('axe1.png')
        self.img = img
        if self.enem == False:
            self.destX, self.destY =  pygame.mouse.get_pos()
            dx, dy = (self.destX - self.x, self.destY - self.y)
            self.stepx, self.stepy = (dx / 25., dy / 25.)
        elif self.enem == True:
           self.destX, self.destY = tarX, tarY
           dx, dy = (self.destX - self.x, self.destY - self.y)
           self.stepx, self.stepy = (dx / 25., dy / 25.)

        

    def create(self):
        if self.enem == False or True and self.typ != "axe":
            #quad1
            if self.angle < 0 and self.angle > -100:
                self.bullet = pygame.draw.rect(self.screen, self.color, ( self.x + (self.angle * -1) , self.y + 8, 15,10)   )
            #quad2    
            elif  self.angle < -100:
                if self.angle > -140:
                    ystart = (self.y - 90) + (self.angle * -1)
                    self.bullet = pygame.draw.rect(self.screen, self.color, ( (self.x + 80), ystart , 15,10))
                else:
                    ystart = (self.y - 100) + (self.angle * -1)
                    self.bullet = pygame.draw.rect(self.screen, self.color, ( self.x + ((self.angle + 110 ) * -1), ystart , 15,10))
                
            #quad3
            elif self.angle > 100:
                ystart = (self.y - 70) - (self.angle * -1)
                self.bullet = pygame.draw.rect(self.screen, self.color, ( self.x, ystart , 15,10))
            #quad4
            else:
                self.bullet = pygame.draw.rect(self.screen, self.color, ( self.x, self.y, 15,10))
        else:
            self.bullet = pygame.draw.rect(self.screen, self.color, ( self.x+ 500, self.y, 15,10))
            print("Bulcreated")



        if self.enem == False or True and self.typ == "axe" or self.typ == 'rock':
                self.bullet = self.img.get_rect()
                self.bullet.y = self.y
                self.bullet.left = self.x


            
    def move(self):
        self.x += self.stepx
        self.y += self.stepy
            
        
        #else:
            #self.x -= self.stepx
            #self.y -= self.stepy
            
    def getbulrect(self):
        return self.bullet

    def swordCreate(self):
        self.bullet = pygame.draw.rect(self.screen, self.color, ( self.x , self.y, 15,10))

    def getDamage(self):
        return self.damage

    def getType(self):
        return self.typ
    
    def setimg(self, value):
        self.img = value
    def getX(self):
        return self.bullet.left




        

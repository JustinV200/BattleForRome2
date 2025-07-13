import pygame
class boss:
    def __init__(self, name, speed, img, health, screen, cord, sound):
        self.name = name
        self.speed = speed
        self.img = pygame.image.load(img)
        self.health = health
        self.rect = self.img.get_rect()
        self.x, self.y = cord
        self.screen = screen
        self.sound = sound
        self.facingnorm = True

    def flip(self):
        self.img = pygame.transform.flip(self.img, True, False)
        if self.facingnorm == True:
            self.facingnorm = False
        else:
            self.facingnorm = True


        
    def create(self):
        self.rect.x = self.x
        self.rect.y = self.y
        self.screen.blit(self.img, self.rect)
    def move(self):
        if self.facingnorm == True:
            self.x = self.x - self.speed
        else:
            self.x = self.x + self.speed
    def getvilrect(self):
        return self.rect
    def sethealth(self, value):
        self.health -= value
    def gethealth(self):
        return self.health
    def gettype(self):
        return self.name
    def setspeed(self, value):
        self.speed = value
    def getspeed(self):
        return self.speed
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def findtarg(self, value):
        self.playerpos = value
        print(self.playerpos)
        return
    def setimg(self, value):
        self.img = pygame.image.load(value)
    def setspeed(self, value):
        self.speed = value
    def hitbox(self):
        pass
    def getsound(self):
        return self.sound
    def setloc(self, x, y):
        self.x = x
        self.y = y
    def setimg(self, value):
        self.img = pygame.image.load(value)
        

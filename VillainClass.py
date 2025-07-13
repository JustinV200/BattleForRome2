import pygame
class villain:
    def __init__(self, name, speed, img, health, screen, cord ):
        self.name = name
        self.speed = speed
        self.img = pygame.image.load(img)
        self.health = health
        self.rect = self.img.get_rect()
        self.x, self.y = cord
        self.screen = screen
        self.normface = True

    def flip(self):
        self.img = pygame.transform.flip(self.img, True, False)
        if self.normface == True:
            self.normface = False
        else:
            self.normface = True

        
    def create(self):
        self.rect.x = self.x
        self.rect.y = self.y
        self.screen.blit(self.img, self.rect)
    def move(self):
        if self.normface == True:
            self.x = self.x - self.speed
        else:
            self.x = self.x + self.speed
    def getvilrect(self):
        return self.rect
    def sethealth(self, value):
        self.health -= 1
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

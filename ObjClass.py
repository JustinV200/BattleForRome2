import pygame

class article:

    def __init__(self, x, y, w, h, screen, iden):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.iden = iden
        self.screen = screen
    def createplatform(self):
        self.platform = pygame.draw.rect(self.screen, [255,0,0], (self.x, self.y, self.w, self.h ))

    def getplat(self):
        return self.platform

    def getY(self):
        return self.y

    def getID(self):
        return self.iden

    def setX(self, value):
        self.x = value

    def setwidth(self, value):
        self.w = value

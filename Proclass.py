import pygame

class pro:
    
    def __init__(self, health):
        self._self = self
        self._jumpcount = 10
        self._imgpro = pygame.image.load("protag.png")
        self._rectpro = self._imgpro.get_rect()
        self._moveY = 0
        self.health = health

    def jump(self):
        if self._jumpcount >= -10:
            self._moveY = 0
            self._moveY -= (self._jumpcount * abs(self._jumpcount)) * .5
            self._jumpcount -= 1
            #print(self._moveY)
            return(self._moveY)
        else:
            self._jumpcount = 10
            return(0)
            self._moveY = 0

    def getrectpro(self):
        return self._rectpro
    
    def getimgpro(self):
        return self._imgpro

    def setimgpro(self, value):
        self._imgpro = pygame.image.load(value)

    def flipimg(self):
        self._imgpro = pygame.transform.flip(self._imgpro, True, False)


    
    def getY(self):
        return int(self._rectpro.y)

    def getX(self):
        return int(self._rectpro.left)

    def getmoveY(self):
        return self._moveY
    
    def setY(self, value):
        self._rectpro = self._rectpro.move(0, value)

    def constantY(self, value):
        self._rectpro.y = value
        
    def setX(self, value):
        self._rectpro.left = value

    def changeY(self, value):
        self._rectpro.y += value
    
        
    def movepro(self, value):
        self._rectpro = self._rectpro.move(value, self._Y)

    def moveproright(self, value):
        self._rectpro = self._rectpro.move(value, 0)
        #print (self._rectpro.left)
        
    def moveproleft(self, value):
        self._rectpro = self._rectpro.move(value, 0)    
        #cords = self._gunimg.get_rect.left, self._gunimg.get_rect.y
        #print(self._gunrect)

    def gethealth(self):
        return self.health

    def sethealth(self, value):
        self.health -= value
    def resethealth(self):
        self.health = 200
        '''
    def blit(self):
        #self._gunrect.center = (self._rectpro.left + 30, self._rectpro.y + 30)
        screen.blit(self._imgpro,self._rectpro)
        '''
    def hide(self):
        self._imgpro = pygame.image.load("nothing.png")
    def unhide(self):
        self._imgpro = pygame.image.load("protag.png")

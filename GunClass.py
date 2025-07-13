import pygame as pg
import pygame
import math
class Cgun:
    def __init__(self, img, Btyp, rate, guyY, guyX, rectguy, rorm):

        self._guyY = (guyY)
        self._guyX = (guyX)
        self._gunimg = pygame.image.load(img)
        self._gunrect = self._gunimg.get_rect()
        self._gunrect.center = (self._guyX + 30, self._guyY)
        self._rectguy = rectguy
        self._typ = Btyp
        self._f = False
        self.rorm = rorm
    
    def getgunimg(self):
        
        return gunimg
    
    def getgunrect(self):
        
        return self._gunrect

    def flipimg(self):
        self._gunimg = pygame.transform.flip(self._gunimg, True, False)
        self._f = True

    def setgunrect(self, gx, gy):
        self._guyX = gx
        self._guyY = gy
        self._gunrect.center = (self._guyX + 300000, self._guyY)
        
    def getF(self):
        return self._f
    
    def rotate(self):
        #mouse_x, mouse_y = pygame.mouse.get_pos()
        #math.cos0 = mouse_x *
        
        mouse = pg.mouse.get_pos()
        if self._f == False:
            shoulder = self._guyX + (self._rectguy.width/2 + 8), self._guyY + (self._rectguy.height/4 + 10)
        elif self._f == True:
            shoulder = self._guyX + (self._rectguy.width/2), self._guyY + (self._rectguy.height/4 + 10)            
        '''
        #shoulder = (self._guyX-(mouse[0]), self._guyY-mouse[1])
        rads = math.degrees(math.atan2(*shoulder))
        #print(self.angle)
        hyp = math.sqrt(math.pow((mouse[0]-shoulder[0]),2)+math.pow((mouse[1]-shoulder[1]),2))
        opp = math.sqrt(math.pow((mouse[0]-shoulder[0]),2)+math.pow((shoulder[1]-shoulder[1]), 2))
        rads = math.asin(opp/hyp)
        self.angle = (rads * 180 / math.pi)
        self.angle = ((self.angle + 90))           
        '''

        #pygame.draw.rect(screen, (255,255,0), (shoulder[0], shoulder[1], 20, 20))        
        #print(angle)
        #old_center = self._gunrect.center
        #-18, -103
        self.angle = math.atan2(self._guyX-mouse[0], self._guyY-mouse[1])
        self.angle = (self.angle * 180/ math.pi)
        #print(self.angle)
        #old_center = self._guyX + (self._rectguy.width/2), self._guyY - (self._rectguy.height/2)
        if self._f == False:
            self.image = pg.transform.rotate(self._gunimg, (self.angle - 80))
        elif self._f == True:
            self.image = pg.transform.rotate(self._gunimg, ((self.angle + 80)))
            
        #print(self.angle)
        
        
        self.rect = self.image.get_rect(x=int(shoulder[0]), y=int(shoulder[1]))
        self.rect.center = shoulder

        return self.angle

        """
        if self.angle <= -18 and self.angle >= -103:
            self.image = pg.transform.rotate(self._gunimg, self.angle+70)
            self.rect = self.image.get_rect(center=old_center)
        elif self.angle <= -103:
            self.image = pg.transform.rotate(self._gunimg, -30)
            self.rect = self.image.get_rect(center=old_center)
        elif self.angle >= -18:
            self.image = pg.transform.rotate(self._gunimg, -18)
            self.rect = self.image.get_rect(center=old_center)
        """ 


    def getgunX(self):
        return int(self.rect.left)
    
    def getgunY(self):
        return int(self.rect.y)
    
    def getrect(self):
        return self.rect
    '''
    def blit(self):
        try:
            screen.blit(self.image, self.rect)
        except:
            screen.blit(self._gunimg, self.rect)
    '''
    def getrorm(self):
        return self.rorm
    def getimg(self):
        try:
            return self.image
        except:
            pass
    def hide(self):
        self.image = pygame.image.load("nothing.png")

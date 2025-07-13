import pygame

class rooms:

    def __init__(self, ident, ln, en, img):
        self.id = ident
        self.ln = ln
        self.en = en
        self.img = img
    def getid(self):
        return self.id
    def geten(self):
        return self.en
    def getln(self):
        return self.ln
    def getimg(self):
        return self.img
   

import pygame

class Button:
    def __init__(self, backImage, posE, heigthE, widthE, actionE):
        self.background = pygame.image.load(backImage).convert_alpha()
        self.pos = posE
        self.heigth = heigthE
        self.width = widthE
        self.background = pygame.transform.scale(self.background,(self.width , self.heigth))
        self.action = actionE

    def show(self, screen):
        screen.blit(self.background, self.pos)
        
    def getPos(self):
        return self.pos

    def getSize(self):
        return (self.width, self.heigth)

    def getAction(self):
        return self.action

    def setSize(self, size):
        self.background = pygame.transform.scale(self.background,size)

  
        
        
        

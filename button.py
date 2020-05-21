import pygame

class Button:
    def __init__(self, backImage, posE, heigthE, widthE, actionE, typeE = "button", ratioE = 1):
        self.backgroundBack = pygame.image.load(backImage).convert_alpha()
        self.posFixed = posE
        self.pos = (int(self.posFixed[0] * ratioE), int(self.posFixed[1] * ratioE))
        self.heigth = heigthE
        self.width = widthE
        self.background = pygame.transform.scale(self.backgroundBack,(int(self.width * ratioE), int(self.heigth * ratioE)))
        self.action = actionE
        self.type = typeE
        self.ratio = ratioE

    def show(self, screen):
        screen.blit(self.background, self.pos)        

    def getType(self):
        return self.type
    
    def getPos(self):
        return self.pos

    def getSize(self):
        return (self.width, self.heigth)

    def getAction(self):
        return self.action

    def changeResolution(self, newRatio):
        self.ratio = newRatio
        self.background = pygame.transform.scale(self.backgroundBack,(int(self.width * newRatio), int(self.heigth * newRatio)))
        self.pos = (int(self.posFixed[0] * newRatio), int(self.posFixed[1] * newRatio))
  
        
        
        

import pygame

class Slider:
    def __init__(self, posE, heigthE, widthE, minV, maxV, actionE, typeE = "slider"):
        #self.background = pygame.image.load(backImage).convert_alpha()
        self.pos = posE
        self.heigth = heigthE
        self.width = widthE
        #self.background = pygame.transform.scale(self.background,(self.width , self.heigth))
        self.action = actionE
        self.minValue = minV
        self.maxValue = maxV
        self.redColor = pygame.Color(255,0,0)
        self.blackColor = pygame.Color(0,0,0)
        self.type = typeE

        self.x = self.width
        self.y = 0

    def show(self, screen):
       
        pygame.draw.rect(screen,self.blackColor,pygame.Rect(self.pos[0],self.pos[1],self.width,self.heigth))
        pygame.draw.rect(screen,self.redColor,pygame.Rect(self.pos[0],self.pos[1],self.x,self.heigth))
        pygame.display.update(pygame.Rect(self.pos[0],self.pos[1],self.width,self.heigth))
        #screen.blit(self.background, self.pos)        

    def getType(self):
        return self.type
    
    def setVariable(self, posX):
        print("SAIDA::", posX)
        self.x = posX - self.pos[0]
    
    def getPos(self):
        return self.pos

    def getSize(self):
        return (self.width, self.heigth)

    def getAction(self):
        return self.action

    def setSize(self, size):
        self.background = pygame.transform.scale(self.background,size)

  
        
        
        

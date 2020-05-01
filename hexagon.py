import pygame

class hexagon:
    def __init__(self, border, background = 0, center = [], biome = 0, owner = 0, nTroop = 0, length = 0)
        self.background = background
        self.center = center
        self.biome = biome
        self.owner = owner
        self.nTroop = nTroop
        self.length = length  #30
        self.color = (0,255,0)

    def show(self, screen):
        pygame.draw.polygon(screen, self.color, [(self.center[0]-(1.1547*self.length/2),self.center[1]-self.length),(self.center[0]-(1.1547*self.length),
        self.center[1]),(self.center[0]-(1.1547*self.length/2),self.center[1]+self.length),(self.center[0]+(1.1547*self.length/2),self.center[1]+self.length),
        (self.center[0]+(1.1547*self.length),self.center[1]),(self.center[0]+(1.1547*self.length/2),self.center[1]-self.length)])

    def checkClick(self, posMouse):
        if(abs(posMouse[0] - center[0]) > 1.1547*self.length or abs(posMouse[1] - center[1]) > self.length):
            return
        if ((abs(posMouse[0] - center[0]) < 1.1547*self.length/2) and (abs(posMouse[1]-center[1]) < self.length)):
            print(center)
        elif (posMouse[0] < center[0]):
            if (((abs(posMouse[1]-(center[1])))/(abs(posMouse[0]-(center[0]-1.1547*self.length)))) < 1.732):
                print(center)
        else:
            if (((abs(posMouse[1]-(center[1])))/(abs(posMouse[0]-(center[1]+1.1547*self.length)))) < 1.732):
                print(center)
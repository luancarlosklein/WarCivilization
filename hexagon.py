import pygame

class hexagon:
    def __init__(self, background = 0, center = [0.0], biome = 0, owner = 0, nTroop = 0, length = 0, color = [0,255,0]):
        self.background = background
        self.center = center
        self.biome = biome
        self.owner = owner
        self.nTroop = nTroop
        self.length = length  #30
        self.color = color
        self.mod = 1.1547     # Escala do hexagono regular mod = 1.1547
        self.des = [0,0]          # Deslocamento do hexagono

    def setColor(self, color):
        self.color = color

    def setDes(self, des):
        self.des = des

    def getDes(self):
        return self.des

    def deslocate(self, des):
        self.des[0] += des[0]
        self.des[1] += des[1]

    def setLen(self, length):
        self.length = length

    def getLen(self):
        return self.length

    def setCenter(self, center):
        self.center = center
    
    def getCenter(self):
        return self.center

    def show(self, screen, length):
        pygame.draw.polygon(screen, self.color, [(self.center[0] + self.des[0] - (self.mod*length/2),self.center[1] + self.des[1] -length),(self.center[0] + self.des[0] -(self.mod*length),
        self.center[1] + self.des[1] ),(self.center[0] + self.des[0] -(self.mod*length/2),self.center[1] + self.des[1] +length),(self.center[0] + self.des[0] +(self.mod*length/2),self.center[1] + self.des[1] +length),
        (self.center[0] + self.des[0] +(self.mod*length),self.center[1] + self.des[1] ),(self.center[0] + self.des[0] +(self.mod*length/2),self.center[1] + self.des[1] -length)])

        pygame.draw.polygon(screen, [0,0,0], [(self.center[0] + self.des[0] -(self.mod*length/2),self.center[1] + self.des[1] -length),(self.center[0] + self.des[0] -(self.mod*length),
        self.center[1] + self.des[1] ),(self.center[0] + self.des[0] -(self.mod*length/2),self.center[1] + self.des[1] +length),(self.center[0] + self.des[0] +(self.mod*length/2),self.center[1] + self.des[1] +length),
        (self.center[0] + self.des[0] +(self.mod*length),self.center[1] + self.des[1] ),(self.center[0] + self.des[0] +(self.mod*length/2),self.center[1] + self.des[1] - length)], 1)    #Desenha a borda do hexagono

    def checkClick(self, posMouse):
        if(abs(posMouse[0] - center[0]) > self.mod*self.length or abs(posMouse[1] - center[1]) > self.length):
            return
        if ((abs(posMouse[0] - center[0]) < self.mod*self.length/2) and (abs(posMouse[1]-center[1]) < self.length)):
            print(center)
        elif (posMouse[0] < center[0]):
            if (((abs(posMouse[1]-(center[1])))/(abs(posMouse[0]-(center[0]-self.mod*self.length)))) < 1.732):
                print(center)
        else:
            if (((abs(posMouse[1]-(center[1])))/(abs(posMouse[0]-(center[1]+self.mod*self.length)))) < 1.732):
                print(center)
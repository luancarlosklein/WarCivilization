import pygame
import math

class hexagon:
    def __init__(self, center = [0.0], biome = "plain", owner = 0, nTroop = 0, length = 0, ratioE = 1):
        self.center = center
        self.ratioE = ratioE
        self.biome = biome
        self.owner = owner
        self.nTroop = nTroop
        self.length = length * self.ratioE  #30
        self.mod = 1.1547     # Escala do hexagono regular mod = 1.1547
        self.des = [0,0]          # Deslocamento do hexagono
        self.biomes_colors = {
			"plain" : (45,160,23),
			"forest": (0,51,0),
			"snow" : (220,255,255),
			"desert" : (219,191, 28)
		}
        self.hexagon_background = {
            "plain" : 0,
			"forest": 0,
			"snow" : 0,
			"desert" : 0
        }
        self.owner_color = {
            "France" : (0,0,255),
            "Brazil" : (0,51,0),
            "USA" : (255,0,0), 
        }

        self.color = self.biomes_colors[biome]
        self.configSurf()

    def setColor(self, color):
        self.color = color

    def setBioma(self, biome):
        self.biome = biome
        self.color = self.biomes_colors[biome]

    def setDes(self, des):
        self.des = des

    def getDes(self):
        return self.des

    def deslocate(self, des):
        self.des[0] += des[0]
        self.des[1] += des[1]

    def setLen(self, length):
        self.length = length * self.ratioE

    def set_ratioE(self, ratioE):
        self.lenght = (self.lenght / self.ratioE) * ratioE
        self.ratioE = ratioE

    def getLen(self):
        return self.length

    def setCenter(self, center):
        self.center = center
    
    def getCenter(self):
        return self.center

    def configSurf(self):
        self.center2 = (self.mod*self.length, self.length)

        self.surface = pygame.Surface((2*self.mod*self.length,2*self.length), pygame.SRCALPHA)

        rect = self.surface.get_rect()
        rect.topleft = (self.center[0] + self.des[0] - self.mod*self.length, self.center[1] + self.des[1] - self.length)

        pygame.draw.polygon(self.surface, self.owner_color[self.owner], [(self.center2[0] - (self.mod*self.length/2),self.center2[1] -self.length),(self.center2[0] -(self.mod*self.length),
        self.center2[1] ),(self.center2[0]  -(self.mod*self.length/2),self.center2[1]  +self.length),(self.center2[0] +(self.mod*self.length/2),self.center2[1] +self.length),
        (self.center2[0]  +(self.mod*self.length),self.center2[1] ),(self.center2[0]  +(self.mod*self.length/2),self.center2[1] -self.length)])

        self.alpha_surf = pygame.Surface((2*self.mod*self.length,2*self.length), pygame.SRCALPHA)
        self.alpha_surf.fill((255,255,255,0))

        self.surface.blit(self.alpha_surf, (0,0), special_flags=pygame.BLEND_RGBA_MULT)

        

    def show(self, screen):
        rect = self.surface.get_rect()
        rect.topleft = (self.center[0] + self.des[0] - self.mod*self.length, self.center[1] + self.des[1] - self.length)
        
        # Desenha o hexagono
        pygame.draw.polygon(screen, self.color, [(self.center[0] + self.des[0] - (self.mod*self.length/2),self.center[1] + self.des[1] -self.length),(self.center[0] + self.des[0] -(self.mod*self.length),
        self.center[1] + self.des[1] ),(self.center[0] + self.des[0] -(self.mod*self.length/2),self.center[1] + self.des[1] +self.length),(self.center[0] + self.des[0] +(self.mod*self.length/2),self.center[1] + self.des[1] +self.length),
        (self.center[0] + self.des[0] +(self.mod*self.length),self.center[1] + self.des[1] ),(self.center[0] + self.des[0] +(self.mod*self.length/2),self.center[1] + self.des[1] -self.length)])

        screen.blit(self.surface, rect)

        # Desenha a borda do hexagono
        pygame.draw.polygon(screen, [0,0,0], [(self.center[0] + self.des[0] -(self.mod*self.length/2),self.center[1] + self.des[1] -self.length),(self.center[0] + self.des[0] -(self.mod*self.length),
        self.center[1] + self.des[1] ),(self.center[0] + self.des[0] -(self.mod*self.length/2),self.center[1] + self.des[1] +self.length),(self.center[0] + self.des[0] +(self.mod*self.length/2),self.center[1] + self.des[1] +self.length),
        (self.center[0] + self.des[0] +(self.mod*self.length),self.center[1] + self.des[1] ),(self.center[0] + self.des[0] +(self.mod*self.length/2),self.center[1] + self.des[1] - self.length)], 1)

    def checkClick(self, posMouse):
        #self.surface.topleft = [self.center[0]-(self.mod*self.length), self.center[1] - self.length]
        if(abs(posMouse[0] - (self.center[0] + self.des[0])) > self.mod*self.length or abs(posMouse[1] - (self.center[1] + self.des[1])) > self.length):
            return False
        if ((abs(posMouse[0] - (self.center[0] + self.des[0])) < self.mod*self.length/2) and (abs(posMouse[1]-(self.center[1] + self.des[1])) < self.length)):
            return True
        elif (posMouse[0] < (self.center[0] + self.des[0])):
            if (((abs(posMouse[1]-((self.center[1] + self.des[1]))))/(abs(posMouse[0]-((self.center[0] + self.des[0])-self.mod*self.length)))) < 1.732):
                return True
        else:
            if (((abs(posMouse[1]-((self.center[1] + self.des[1]))))/(abs(posMouse[0]-((self.center[1] + self.des[1])+self.mod*self.length)))) < 1.732):
                return True
        return False

    def distanceTo(self, hexagon):
        dist = math.sqrt((self.center[0] - hexagon.center[0])**2 + (self.center[1] - hexagon.center[1])**2)
        h = 3*self.mod*self.length/2
        return (int(dist/h))

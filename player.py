import pygame
from playerInfoSelector import PlayerInfoSelector
from goal import Goal
from mapManager import mapManager
import os

INITIAL_MONEY = 10

class Player:
    def __init__(self, volEffect, volMain, ratioE):
                
        self.exists = 0
        self.victoryCount = 0
        self.money = INITIAL_MONEY
        self.owned_territories =[]
        self.mission = 0
        info = PlayerInfoSelector("None", "None", "None", volMain, volEffect, ratioE)
        self.name = info.defineFlag()
        self.emblem = pygame.image.load(os.path.join("images", self.findFlag()+".png")).convert_alpha()
        self.exists = 1
        self.morale = 50
        self.hexBiomes= [0,0,0,0]
        self.earnings = 0
        ######################################################
        self. moraleMultiplier = 1  #bonus de moral
        if (self.name == "France"):
            self.moraleMultiplier = 1.2
        elif(self.name == "Greece"):
            self.moraleMultiplier = 1.15
        elif(self.name == "India"):
            self.moraleMultiplier = 1.1
        elif(self.name == "India"):
            self.moraleMultiplier = 1.1
        ######################################################
        self. coinMultiplier = 1   #bonus de moedas
        if (self.name == "USA"):
            self.coinMultiplier = 1.15
        elif(self.name == "India"):
            self.CoinMultiplier = 0.9
    
    def findFlag(self):
        if (self.name=="Great Britain"):   #selecao das bandeiras... faltam algumas
            return "flag1"
        elif (self.name=="USA"):
            return "flag2"
        elif (self.name=="Egypt"):
            return "flag3"
        else:
            return "flag1"
        return False

    def increaseMorale(self, unexplored):    #funcao chamada apos uma vitoria para incrementar a moral
        self.victoryCount +=1
        self.morale += 5*self.moraleMultiplier
        if (self.name == "Portugal" and unexplored == true):
            self.morale +=1
        if (self.morale>100):
            self.morale = 100

    def decreaseMorale(self):                #funcao chamada apos uma derrota para diminuir a moral
        if (self.name == "Japan"):
            self.morale -= 5
        else:
            self.morale -= 10 *(2-self.moraleMultiplier)

    def gainHex (self, hex, dist ):
        if (self.name == "Spain" and not (isinstance(hex.owner, Player))and not dist):
            self.money +=1
        self. earnings += self.coinMultiplier
        if hex.biome == "plain":
            self.hexBiomes[0]+=1
        elif hex.biome == "forest":
            self.hexBiomes[1]+=1
        elif hex.biome == "snow":
            self.hexBiomes[2]+=1
        elif hex.biome == "desert":
            self.hexBiomes[3]+=1
        self.owned_territories.append(hex)



    def loseHex (self, hex):
        self. earnings -= self.coinMultiplier
        if hex.biome == "plain":
            self.hexBiomes[0]-=1
        elif hex.biome == "forest":
            self.hexBiomes[1]-=1
        elif hex.biome == "snow":
            self.hexBiomes[2]-=1
        elif hex.biome == "desert":
            self.hexBiomes[3]-=1
        self.owned_territories.remove(hex)


    def check_goal(self, player_list, mapa):
        print (self.mission.mission)
        if self.mission.mission == 1:
            for i in player_list:
                if i.money> self.money:
                    self.mission.count = 0
                elif i.money== self.money:
                    return False
                else:
                    count+=1
                    if (count ==10):
                        return True
                return False

        elif self.mission.mission ==2:
            if len(self.owned_territories) ==50:
                return True

        elif self.mission.mission == 3:
            if (mapa.check_corners() == self):
                self.mission.count+=1
                if (self.mission.count == 5):
                    return True
            else:
                return False

        elif self.mission.mission == 4:
            if (self.hexBiomes[self.mission.type] == mapa.biome_count[self.mission.type] ):
                return True

        elif self.mission.mission == 5:
            return False

        elif self.mission.mission == 6:
            if self.victoryCount >= 100:
                return True
            else: 
                return False
        else:
            if (len(player_list[self.mission.opponent].owned_territories) ==0):
                return True

        return False

        
        

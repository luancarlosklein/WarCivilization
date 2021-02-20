import pygame
from playerInfoSelector import PlayerInfoSelector
from goal import Goal
import os

INITIAL_MONEY = 10

class Player:
	def __init__(self, volEffect, volMain, ratioE):
                
		self.exists = 0
		self.money = INITIAL_MONEY
		self.owned_territories =[]
		self.mission = 0
		info = PlayerInfoSelector("None", "None", "None", volMain, volEffect, ratioE)
		self.name = info.defineFlag()
		self.emblem = pygame.image.load(os.path.join("images", self.findFlag()+".png")).convert_alpha()
		self.exists = 1
		self.morale = 75
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
		

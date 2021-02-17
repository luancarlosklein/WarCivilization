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
	
	def findFlag(self):
		if (self.name=="Great Britain"):
			return "flag1"
		elif (self.name=="USA"):
			return "flag2"
		elif (self.name=="Egypt"):
			return "flag3"
		return False
		
		

import pygame
from playerInfoSelector import PlayerInfoSelector
from goal import Goal
import os

INITIAL_MONEY = 10

class Player:
	def __init__(self):
		self.exists = 0
		self.money = INITIAL_MONEY
		self.owned_territories =[]
		self.mission = 0
		info = PlayerInfoSelector()
		#self.name = info.chooseName()
		self.name = info.chooseFlag()
		self.emblem = pygame.image.load(os.path.join("images", self.findFlag()+".png")).convert_alpha()
		#print (self.name)
		self.exists = 1
	
	def findFlag(self):
		if (self.name=="Great Britain"):
			return "flag1"
		if (self.name=="USA"):
			return "flag2"
		if (self.name=="Egypt"):
			return "flag3"
		
		

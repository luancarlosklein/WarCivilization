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
		#self.emblem = info.chooseFlag()
		self.name = "Egito"
		self.emblem = pygame.image.load(os.path.join("images", "flag2.png")).convert_alpha()
		#print (self.name)
		self.exists = 1
		
		

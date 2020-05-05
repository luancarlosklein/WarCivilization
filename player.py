import pygame
from playerInfoSelector import PlayerInfoSelector

INITIAL_MONEY = 10

class Player:
	def __init__(self):

		self.money = INITIAL_MONEY
		self.owned_territories =[]
		info = PlayerInfoSelector()
		self.name = info.chooseName()
		self.emblem = info.chooseFlag()
		print (self.name)
		
		

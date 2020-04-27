import pygame

INITIAL_MONEY = 10

class player:
	def __init__(self):

		self.money = INITIAL_MONEY
		self.owned_territories =[]
		self.name = "empty" 
		self.emblem = 0
		
		

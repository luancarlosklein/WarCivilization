import pygame
from mapManager import mapManager
from player import player
from inGameMenu import inGameMenu
from attackMenu import attackMenu
from draftMenu import draftMenu
from gameManager import gameManager

class gameManager:
	def __init__(self, np, screen):
		self.player_list =[]
		i=0
		while i<np:
			self.player_list.insert(player)
		self.commands = inGameMenu()
		self.attacks = attackMenu()
		self.draft = draftMenu()
		self.environment = mapManager()
		self.screen = screen
		self.active = True 

	def gameLoop():
		i=0
		while self.active:                                           ##enquanto o jogo estiver valendo
			while i < len(self.player_list)                      ##o turno de cada jogador
				operation = self.commands.execute(screen)    ##imprime o menu, verifica os clicks e retorna o indice do botao retornado
				if operation ==1                             ##opção 1: recrutar
					self.attack.execute(screen)          #menu que retorna as informações sobre o ataque
					self.attackProcedure()		     #realiza o ataque
				elif operation == 2			     #opção 2: recrutar
					self.draft.execute(screen)           #analogo a opção 1, porem relacionado ao recrutamento
					self.draftProcedure()
			status = self.checkGoals()			     #analiza se algum player cumpriu seu objetivo
			if status != 0					     #em caso positivo, retorna o vencedor
				self.active = False			     #em caso negativo, acaba o jogo

	def attackProcedure():
		return 1
	def draftProcedure():
		return 1
	def checkGOals():
		return 1			

		

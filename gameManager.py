import pygame
#from mapManager import mapManager
from player import player
from inGameMenu import InGameMenu
from attackMenu import AttackMenu
from draftMenu import DraftMenu

class GameManager ():
	def __init__(self, np, screen):
		self.player_list =[]
		i=0
		#while i<np:
			#self.player_list.insert(player)
		self.commands = InGameMenu()
		self.attacks = AttackMenu()
		self.draft = DraftMenu()
		#self.environment = mapManager()
		self.screen = screen
		self.active = True 

	def gameLoop(self):
		
		field =0
		selecting = 1
		attack = 2
		draft = 3
		
		i=0
		while self.active:                                        ##enquanto o jogo estiver valendo
			#while i < len(self.player_list):                      ##o turno de cada jogador
				events = pygame.event.get()		
				showing = field				     #variavel que controla o estado da intel. em "campo", ainda nao foi decidido se o player vai atacar ou recrutar
				self.showGameScreen()			     #mostra o campo com os exagonos
				operation = self.commands.execute(self.screen, events)    ##imprime o menu, verifica os clicks e retorna o indice do botao retornado
				if (showing ==field and operation ==0):
					showing = selecting
					self.commands.hidden = False
				elif (operation == 0):
					showing = field
					self.commands.showing = True
				elif (showing ==selecting):
					if (operation ==1):    
						#showing = ataque
						i=0
					if (operation ==2):
						i=0
						#showing = draft

				elif ( showing ==attack): 			     ##opção 1: atacar
						#self.attack.execute(screen)          #menu que retorna as informações sobre o ataque
						#self.attackProcedure()		     #realiza o ataque
						i=0
				elif ( showing ==draft): 			     ##opção 1: atacar
						#self.attack.execute(screen)          #menu que retorna as informações sobre o ataque
						#self.attackProcedure()		     #realiza o ataque
						i=0

				pygame.display.flip()
				pygame.display.update()
				status = self.checkGoals()			     #analiza se algum player cumpriu seu objetivo
				if status != 0:					     #em caso positivo, retorna o vencedor
					self.active = False			     #em caso negativo, acaba o jogo
				i+=1

	def attackProcedure(self):
		return 1

	def draftProcedure(self):
		return 1

	def checkGoals(self):
		return 0	

	def showGameScreen(self):
		return 0
		#environment.showScreen()
		
		

		

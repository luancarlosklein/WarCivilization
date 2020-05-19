import pygame
import time
from mapManager import mapManager
from player import Player
from inGameMenu import InGameMenu
from attackMenu import AttackMenu
from draftMenu import DraftMenu
from goal import Goal

class GameManager ():
   def __init__(self, np, screen):
      self.player_list =[]
      i = 0
      while i < np:
         i+=1
         new_player = Player()
         if new_player.exists:
            self.player_list.append(new_player)
         new_player.mission = Goal (np)
         if new_player.mission.opponent == i:
            new_player.mission.opponent = 1

      self.n_players = np
      self.current_player = 1
      self.commands = InGameMenu()
      self.attacks = AttackMenu()
      self.draft = DraftMenu()
      self.map = mapManager()
      self.screen = screen
      self.active = True 
      self.new_game =1

   def gameLoop(self):
      color_white = (255, 255, 255)
      field = 0
      selecting = 1
      attack = 2
      draft = 3
      showing = field
      ##Ativa a variavel para quando for chamado de mais uma vez, voltar a executar o loop
      self.active = True
      ##Variavel usada para retornar o valor de pause
      pause = "pause"	
      self.distribution()
      i=0
      while self.active:                                        ##enquanto o jogo estiver valendo
        while i < len(self.player_list):                      ##o turno de cada jogador
            end_turn = False
            while (end_turn==False):
               self.screen.fill(color_white)
               events = pygame.event.get()			     #variavel que controla o estado da intel. em "campo", ainda nao foi decidido se o player vai atacar ou recrutar
               self.showGameScreen()			     #mostra o campo com os exagonos
               operation = self.commands.execute(self.screen, events, self.player_list[i] )    ##imprime o menu, verifica os clicks e retorna o indice do botao retornado
               if (operation == 4):
                  end_turn = True
               if (showing ==field and operation ==0):
                  showing = selecting
                  self.commands.hidden = False

               ##Verifica se o retorno foi pause (cliclado na tecla esc), se sim, retorna o valor (para o loop)
               elif (operation == pause):
                  self.active = False
                  print(pause)
                  return pause
               elif (operation == 0):
                  showing = field
                  self.commands.hidden = True
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
            status = self.checkGoals(i)			     #analiza se algum player cumpriu seu objetivo
            if status != 0:					     #em caso positivo, retorna o vencedor
                  self.active = False			     #em caso negativo, acaba o jogo
                  i+=1

                        
            time.sleep (0.03)
            self.current_player = (self.current_player +1)%self.n_players

   def distribution (self):
      pause = "pause"	
      self.commands.hidden = False
      color_white = (255, 255, 255)
      choices = 0
      while (len(self.player_list[0].owned_territories)<5):
         for i in self.player_list:
            territory = 0
            selecting = True
            while selecting:
               territory = self.map.check_click()
               if (territory):
                  if (territory.owner != i):
                     selecting = False
               self.screen.fill(color_white)
               events = pygame.event.get()			     #variavel que controla o estado da intel. em "campo", ainda nao foi decidido se o player vai atacar ou recrutar
               self.showGameScreen()			     #mostra o campo com os exagonos
               operation = self.commands.execute(self.screen, events, i )    ##imprime o menu, verifica os clicks e retorna o indice do botao retornado
               if operation == pause:
                  return False

               pygame.display.flip()
               pygame.display.update()
            i.owned_territories.append(territory)
            territory.owner = i
            time.sleep (0.03)
            
      return True


   def createPlayers(self):
      while i<self.n_players:
         self.player_list.append(Player())
         i+=1

   def attackProcedure(self):
      return 1
        

   def draftProcedure(self):
      return 1

   def checkGoals(self, current_player):
      if self.player_list[current_player].mission == 3:
         if len(self.player_list[current_player.mission.opponent].owned_territories) ==0 :
            return 0
      return 0	

   def showGameScreen(self):
      self.map.show(self.screen)
		
		

		

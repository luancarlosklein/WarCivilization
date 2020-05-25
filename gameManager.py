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

      self.n_players = np
      self.current_player = 1
      self.commands = InGameMenu()
      self.attacks = AttackMenu()
      self.draft = DraftMenu()
      self.map = mapManager()
      self.screen = screen
      self.active = True 
      self.game_started =0
      self.chosenHex = False
      self.attackingHex = False
      self.showing = 0
   def gameLoop(self):
      color_white = (255, 255, 255)
      field = 0
      selecting = 1
      attack = 2
      draft = 3
      i = 0
      while i < self.n_players:
         i+=1
         new_player = Player()
         if new_player.exists:
            self.player_list.append(new_player)
         new_player.mission = Goal (self.n_players)
         if new_player.mission.opponent == i:
            new_player.mission.opponent = 1
      while(pygame.mouse.get_pressed()[0]):
         pygame.event.get()
         time.sleep(0.03)
      self.showing = selecting
      ##Ativa a variavel para quando for chamado de mais uma vez, voltar a executar o loop
      self.active = True
      ##Variavel usada para retornar o valor de pause
      pause = "pause"
      final = "final"
      self.distribution()
      self.commands.distribution = False
      self.game_started = 0
      i=0
      while self.active:                                        ##enquanto o jogo estiver valendo
        while i < len(self.player_list):                      ##o turno de cada jogador
            end_turn = False
            self.player_list[i].money+=len(self.player_list[i].owned_territories)
            while (end_turn == False):
               self.screen.fill(color_white)
               events = pygame.event.get()			     #variavel que controla o estado da intel. em "campo", ainda nao foi decidido se o player vai atacar ou recrutar
               self.showGameScreen(events)			     #mostra o campo com os exagonos
               operation = self.commands.execute(self.screen, events, self.player_list[i], self.chosenHex, self.showing )    ##imprime o menu, verifica os clicks e retorna o indice do botao retornado

               ##Verifica se o retorno foi pause (cliclado na tecla esc), se sim, retorna o valor (para o loop)
               if (operation == pause):
                  self.active = False
                  print(pause)
                  return pause
               

               if (operation == 3):
                  end_turn = True
               if (self.showing ==field and operation ==0):
                  self.showing = selecting
                  self.commands.hidden = False

               elif (operation == 0):
                  self.showing = field
                  self.commands.hidden = True
               elif (self.showing ==selecting):
                  territory = self.map.check_click()
                  if (territory):
                     self.chosenHex = territory
                  if (operation ==1):
                     self.showing = draft
                     self.chosenHex = 0
                  if (operation ==2):    
                     self.showing = attack
                     self.chosenHex = 0

               elif ( self.showing ==attack): 			     ##opção 1: atacar
                     self.attackProcedure(self.player_list[i], events)		     #realiza o ataque

               elif ( self.showing ==draft): 			     ##opção 1: atacar
                     self.draftProcedure(self.player_list[i], events)		     #realiza o recrutamento

               pygame.display.flip()
               pygame.display.update()
            status = self.checkGoals(i)			     #analiza se algum player cumpriu seu objetivo
            i= (i+1)%self.n_players

            if status != 0:					     #em caso positivo, retorna o vencedor
                  self.active = False			     #em caso negativo, acaba o jogo

                        
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
                  if ((isinstance(territory.owner, Player))==False):
                     selecting = False
               self.screen.fill(color_white)
               events = pygame.event.get()			     #variavel que controla o estado da intel. em "campo", ainda nao foi decidido se o player vai atacar ou recrutar
               self.showGameScreen(events)			     #mostra o campo com os exagonos
               operation = self.commands.execute(self.screen, events, i, 0 )    ##imprime o menu, verifica os clicks e retorna o indice do botao retornado
               if operation == pause:
                  return False

               pygame.display.flip()
               pygame.display.update()
            i.owned_territories.append(territory)
            territory.owner = i
            territory.nTroop = 1
            time.sleep (0.03)
            
      return True


   def createPlayers(self):
      while i<self.n_players:
         self.player_list.append(Player())
         i+=1

   def attackProcedure(self, player, events):
      if self.chosenHex==False:
         if self.attackingHex == False:
            operation = self.attacks.execute(self.screen, events, 0)
         else:
            operation = self.attacks.execute(self.screen, events, 1)
      else:
         operation = self.attacks.execute(self.screen, events, 2)
         if (operation ==0 and self.attackingHex.nTroop > self.attacks.troops+1):
            self.attacks.troops +=1
         if (operation ==1 and self.attacks.troops>0):
            self.attacks.troops -=1
         if (operation ==2):
            if (self.attacks.troops>self.chosenHex.nTroop):
               self.chosenHex.nTroop = self.attacks.troops - self.chosenHex.nTroop
               self.chosenHex.owner = player
               self.attackingHex.nTroop -=self.attacks.troops
            elif (self.attacks.troops<self.chosenHex.nTroop):
               self.chosenHex.nTroop = self.chosenHex.nTroop - self.attacks.troops
               self.attackingHex.nTroop -=self.attacks.troops
            else:
               self.chosenHex.nTroop = 0
               self.chosenHex.owner = False
               self.attackingHex.nTroop -=self.attacks.troops
            self.showing = 1
            self.attacks.troops = 0
            self.chosenHex = False
            self.attackingHex = False
      territory = self.map.check_click()
      if (territory):
         if (territory.owner == player):
            if self.attackingHex==False:
               self.attackingHex = territory
         elif(territory.distanceTo(self.attackingHex)<1.1):
               self.chosenHex = territory
      if (operation == 3):
         self.showing = 1
         self.attacks.troops = 0
         self.chosenHex = False
         self.attackingHex = False
      return 1
        

   def draftProcedure(self, player, events):
      if self.chosenHex==False:
         operation = self.draft.execute(self.screen, events, 0)
      else:
         operation = self.draft.execute(self.screen, events, 1)
         if (operation ==0 and player.money>self.draft.troops):
            self.draft.troops +=1
         if (operation ==1 and self.draft.troops>0):
            self.draft.troops -=1
         if (operation ==2):
            self.chosenHex.nTroop += self.draft.troops
            player.money -= self.draft.troops
            self.showing = 1
            self.draft.troops = 0
            self.chosenHex = False
      territory = self.map.check_click()
      if (territory):
         if (territory.owner == player):
            self.chosenHex = territory
      if (operation == 3):
         self.showing = 1

      
      return 1

   def checkGoals(self, current_player):
      if self.player_list[current_player].mission == 3:
         if len(self.player_list[current_player.mission.opponent].owned_territories) ==0 :
            return 0
      return 0	

   def showGameScreen(self, events):
      self.map.show(self.screen, events)

   def changeResolution(self, newRatio):
      return 1
		
		

		

import pygame
import time
import random
from mapManager import mapManager
from player import Player
from inGameMenu import InGameMenu
from attackMenu import AttackMenu
from draftMenu import DraftMenu
from goal import Goal

class GameManager ():
   def __init__(self, np, screen, volEffect, volMain, ratioE):
      self.player_list =[]

      self.n_players = np
      self.current_player = 1
      print (ratioE)
      self.commands = InGameMenu(ratioE)
      self.attacks = AttackMenu(ratioE)
      self.draft = DraftMenu(ratioE)
      self.map = mapManager()
      self.screen = screen
      self.active = True 
      self.game_started =0
      self.chosenHex = False
      self.attackingHex = False
      self.showing = 0

      self.volEffect = volEffect
      self.volMain = volMain
      self.ratioE = ratioE
#####################################################################################################################
   def gameLoop(self):
      color_white = (255, 255, 255)
      field = 0        # representa os estados possiveis
      selecting = 1
      attack = 2
      draft = 3
      i = 0
      while i < self.n_players:   #rotina para selecao de personagem dos players
         i+=1
         new_player = Player(self.volEffect, self.volMain, self.ratioE)
         if new_player.exists:
            self.player_list.append(new_player)
         new_player.mission = Goal (self.n_players)  #selecao de objetivos, provisorio
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
      self.distribution()  #etapa onde se escolhem os territorios
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
               

               if (operation == 3 and self.showing == selecting):  #verifica se foi pressionado o end turn
                  end_turn = True
               if (self.commands.hidden == True and operation ==0):  #verifica se o menu deve ser "desescondido"
                  self.showing = selecting
                  self.commands.hidden = False

               elif (operation == 0):    #verifica se o menu deve ser escondido
                  #self.showing = field
                  self.commands.hidden = True

               elif (operation == 4):    # x do papiro preto?
                  self.chosenHex = 0
                  
               elif (self.showing ==selecting):
                  if pygame.mouse.get_pressed()[0]:
                     territory = self.map.check_click() #verifica o hexagono clicado
                     if (territory):
                        self.chosenHex = territory
                     else:
                        self.chosenHex = 0
                  if (operation ==1):       #verifica se foi escolhida a opcao recrutar
                     self.showing = draft
                     self.chosenHex = 0
                  if (operation ==2):       # atacar
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
#####################################################################################################################
   
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

#####################################################################################################################

   def createPlayers(self):
      while i<self.n_players:
         self.player_list.append(Player())
         i+=1

#####################################################################################################################         

   def attackProcedure(self, player, events):
      if self.chosenHex==False:  #faltou selecionar ao menos um hexagono
         if self.attackingHex == False:
            operation = self.attacks.execute(self.screen, events, 0, player) #faltou escolher o de ataque
         else:
            operation = self.attacks.execute(self.screen, events, 1,player)  #faltou escolher o de defesa
      else:
         operation = self.attacks.execute(self.screen, events, 2, player)  #selecionar quantidade
         if (operation ==0 and self.attackingHex.nTroop > self.attacks.troops+1): #foi clicado em "+"
            self.attacks.troops +=1
         if (operation ==1 and self.attacks.troops>0):#foi clicado em "-"
            self.attacks.troops -=1
         if (operation ==2 and self.attacks.troops>0):#foi clicado em atacar
            atkMulti = self.calculateAtkMultiplier(self.attackingHex, self.chosenHex) #calculo dos bonus de batalha
            defMulti = self.calculateDefMultiplier(self.chosenHex)
            result = self.battleSimulation(atkMulti, defMulti, self.attacks.troops, self.chosenHex.nTroop)#simulacao da batalha
            #if (self.attacks.troops>self.chosenHex.nTroop):
            if (result > 0):         #o ataque ganhou... result diz o numero de tropas restantes
               #self.chosenHex.nTroop = self.attacks.troops - self.chosenHex.nTroop
               if (isinstance(self.chosenHex.owner, Player) >0):  #efeitos de moral
                  self.chosenHex.owner.decreaseMorale()
                  self.attackingHex.owner.increaseMorale(False)
               else:
                  self.attackingHex.owner.increaseMorale(True)                  
               self.chosenHex.nTroop = result       #troca o dono do hexagono
               self.chosenHex.owner = player
               self.attackingHex.nTroop -=self.attacks.troops
            #elif (self.attacks.troops<self.chosenHex.nTroop):
            elif(result<0):     #defesa ganhou
               #self.chosenHex.nTroop = self.chosenHex.nTroop - self.attacks.troops
               if (isinstance(self.chosenHex.owner, Player)):  #efeitos de moral
                  self.chosenHex.owner.increaseMorale(False)
               self.attackingHex.owner.decreaseMorale()
               self.chosenHex.nTroop = -result
               self.attackingHex.nTroop -=self.attacks.troops
            #else:
            #   self.chosenHex.nTroop = 0
            #   self.chosenHex.owner = False
            #   self.attackingHex.nTroop -=self.attacks.troops
            self.showing = 1
            self.attacks.troops = 0
            self.attackingHex = False
            return 1
      territory = self.map.check_click()         #se foi selecionado um hexagono, seta como de ataque ou defesa
      if (territory):
         if (territory.owner == player):
            if self.attackingHex==False:
               self.attackingHex = territory
         elif(self.attackingHex and territory.distanceTo(self.attackingHex)<1.1):
            self.chosenHex = territory
      if (operation == 3):                       #abortar
         self.showing = 1
         self.attacks.troops = 0
         self.chosenHex = False
         self.attackingHex = False
      return 1
        

   def draftProcedure(self, player, events):
      if self.chosenHex==False:         ##manda selecionar um hexagono
         operation = self.draft.execute(self.screen, events, 0, player)
      else:
         operation = self.draft.execute(self.screen, events, 1, player)  #manda escolher a quantidade
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
            return 1
      territory = self.map.check_click()
      if (territory):
         if (territory.owner == player):
            self.chosenHex = territory
      if (operation == 3):
         self.showing = 1

      
      return 1

   def checkGoals(self, current_player):
      # teste dos objetivos, provisorio
      if self.player_list[current_player].mission == 3:
         if len(self.player_list[current_player.mission.opponent].owned_territories) ==0 :
            return 0
      return 0	

   def showGameScreen(self, events):
      self.map.show(self.screen, events)

   def changeResolution(self, newRatio):
      return 1

######################################################################################################################

   def calculateAtkMultiplier(self, atk_hexagon, def_hexagon):   #calculo dos bonus de ataque
      multiplier = 50+atk_hexagon.owner.morale/2
      ##Egypt
      if (atk_hexagon.owner.name == "Egypt" and def_hexagon.biome == "desert"):
         multiplier *=1.05
      elif (atk_hexagon.owner.name == "Mongol" ):
         multiplier *=1.03
      elif (atk_hexagon.owner.name == "France" and def_hexagon.biome == "snow" ):
         multiplier *=0.7
      elif (atk_hexagon.owner.name == "Pirate" and (def_hexagon.des[0] == 0 or def_hexagon.des[1] == 0 or def_hexagon.des[0] == 18 or def_hexagon.des[1] == 8)):
         multiplier *=0.7
      elif (atk_hexagon.owner.name == "Italy" and def_hexagon.biome == "plain" ):
         multiplier *=1.01* atk_hexagon.owner.hexBiomes[0]
      if (atk_hexagon.owner.name == "Egypt" and def_hexagon.biome == "desert"):
         multiplier *=1.05
      return multiplier

#########################################################################################################################

   def calculateDefMultiplier(self, def_hexagon):   #calculo dos bonus de defesa
      multiplier = 50+def_hexagon.owner.morale/2
      ##Egypt
      if (isinstance(def_hexagon.owner, Player)):
         if (def_hexagon.owner.name == "Egypt" and def_hexagon.biome == "desert"):
            multiplier *=1.05
         elif (def_hexagon.owner.name == "China" ):
            multiplier *=1.03
         elif (def_hexagon.owner.name == "Soviet Union" and def_hexagon.biome == "snow" ):
            multiplier *=1.3
         elif (def_hexagon.owner.name == "Cuba" and def_hexagon.biome =="forest"):
            multiplier *=0.7
         elif (def_hexagon.owner.name == "Italy" and def_hexagon.biome == "plain" ):
            multiplier *=1.01* atk_hexagon.owner.hexBiomes[0]

      if (def_hexagon.biome == "snow"):
         multiplier += 0.1
      if (def_hexagon.biome == "plain"):
         multiplier -= 0.1
      if (def_hexagon.biome == "forest"):
         multiplier += 0.05

      return multiplier

		
   def battleSimulation(self, offensiveMultiplier, defensiveMultiplier, atkTroops, defTroops):
      while (defTroops>0 and atkTroops>0):  #termina quando um dos players nao tiver mais tropas
          #ve quem ganhou de acordo com a forca
         if (random.randint(-int(defensiveMultiplier* defTroops-1), int(offensiveMultiplier* atkTroops))>0):
            defTroops -=1
         else:
            atkTroops -=1
      return atkTroops - defTroops
		

		

import pygame
import menu
from button import Button
from player import Player
import os

class AttackMenu(menu.Menu):
   def __init__(self, ratio):
      super().__init__(os.path.join("images", "backgroundMainMenu.png"), soundBack = "none", soundEff = "none", volBack = 0, volEff = 0, ratioImage = ratio)
      ## o nome dos botoes ja diz o q eles sao...
      self.buttons.append(Button(os.path.join("images", "transp.png"), (int(1630*self.ratio), int(600*self.ratio)), int(100), int(100), "+"))
      self.buttons.append(Button(os.path.join("images", "transp.png"), (int(1430*self.ratio), int(600*self.ratio)), int(100), int(100), "-"))
      
      self.buttons.append(Button(os.path.join("images", "buttonSendAttack.png"), (int(1470*self.ratio), int(700*self.ratio)), int(70*self.ratio), int(280*self.ratio), "Select"))
      self.buttons.append(Button(os.path.join("images", "buttonCancel.png"), (int(1480*self.ratio), int(850*self.ratio)), int(100*self.ratio), int(300*self.ratio), "Return"))

      self.background = pygame.transform.scale(self.background,(int(600*self.ratio) , int(1080*self.ratio)))
      self.hidden = True
      self.distribution = True
      self.troops = 0
      
      self.coin = pygame.image.load(os.path.join("images", "coin.png")).convert_alpha()
      self.coin = pygame.transform.scale(self.coin,(int(50* self.ratio), int(50 * self.ratio)))
      
      self.chooseAttack = pygame.image.load(os.path.join("images", "chooseTerritoryAttacking.png")).convert_alpha()
      self.chooseAttack = pygame.transform.scale(self.chooseAttack,(int(500 * self.ratio), int(500 * self.ratio)))

      self.chooseDefense = pygame.image.load(os.path.join("images", "chooseTerritoryDefending.png")).convert_alpha()
      self.chooseDefense = pygame.transform.scale(self.chooseDefense,(int(500 * self.ratio), int(500 * self.ratio)))
      
   def show(self,screen, op, player = False):



      screen.blit(self.background, (int(1320*self.ratio),0))
      flag = player.emblem
      flag = pygame.transform.scale(flag,(int(self.ratio*171) , int(self.ratio*204)))
      screen.blit(flag,(int(1530*self.ratio),int(100*self.ratio)))

      pygame.font.init()                                ##### inicia font
      fonte=pygame.font.get_default_font()              ##### carrega com a fonte padrão
      fontesys=pygame.font.SysFont(fonte, int(self.ratio*80))           ##### usa a fonte padrão
      txt= (player.name)                          ##### armazena o texto
      txtscreen = fontesys.render(txt, 1, (255,255,255))  	  ##### renderiza o texto na cor desejada
      screen.blit(txtscreen,(int(1550*self.ratio),int(310* self.ratio)))                  ##### coloca na posição 50,900 (tela FHD)

      fontesys=pygame.font.SysFont(fonte, int(self.ratio*35))
      screen.blit(self.coin,(int(1720*self.ratio),int(255* self.ratio)))
      txt= (str(player.money))                          ##### armazena o texto
      txtscreen = fontesys.render(txt, 1, (0,0,0))  	  ##### renderiza o texto na cor desejada
      screen.blit(txtscreen,(int(1735*self.ratio),int(270* self.ratio)))                  ##### coloca na posição 50,900 (tela FHD)



      count = 0
      for i in self.buttons:
         count+=1
         if (op == 1 or count ==4 ):
            i.show(screen)
      
      pygame.font.init()                                ##### inicia font
      fonte=pygame.font.get_default_font()              ##### carrega com a fonte padrão
      fontesys=pygame.font.SysFont(fonte, int(self.ratio*60))           ##### usa a fonte padrão

      if (op == 0):
         screen.blit(self.chooseAttack, (1370* self.ratio, 420* self.ratio)) 
         ##txt= ('CHOOSE THE ATTACKING TERRITORY')                          ##### armazena o texto
         ##txtscreen = fontesys.render(txt, 1, (255,255,255))  	  ##### renderiza o texto na cor desejada
         ##screen.blit(txtscreen,(int(1250*self.ratio),int(650* self.ratio)))                  ##### coloca na posição 50,900 (tela FHD)

      if (op == 1):
         screen.blit(self.chooseDefense, (1370* self.ratio, 420* self.ratio)) 
         ##txt= ('CHOOSE THE DEFENDING TERRITORY')                          ##### armazena o texto
         ##txtscreen = fontesys.render(txt, 1, (255,255,255))  	  ##### renderiza o texto na cor desejada
         ##screen.blit(txtscreen,(int(1250*self.ratio),int(650* self.ratio)))                  ##### coloca na posição 50,900 (tela FHD)

      if (op == 2):
         
         txt= ('Troops: ')                          ##### armazena o texto
         txtscreen = fontesys.render(txt, 1, (255,255,255))  	  ##### renderiza o texto na cor desejada
         screen.blit(txtscreen,(int(1470*self.ratio),int(535* self.ratio)))                  ##### coloca na posição 50,900 (tela FHD)



         font2 = pygame.font.Font(os.path.join("fonts", "redondeta.ttf") , int(80*self.ratio))
         tPlus = font2.render("+", True, (255, 255, 255))
         tMinus = font2.render("-", True, (255, 255, 255))
         screen.blit(tPlus,(int(1680*self.ratio),int(600* self.ratio)))
         screen.blit(tMinus,(int(1470*self.ratio),int(600* self.ratio)))

         self.buttons[2].show(screen)
         ##txt= ('SEND ATTACK')                          ##### armazena o texto
         ##txtscreen = fontesys.render(txt, 1, (255,255,255))  	  ##### renderiza o texto na cor desejada
         ##screen.blit(txtscreen,(int(1380*self.ratio),int(750* self.ratio)))                  ##### coloca na posição 50,900 (tela FHD)

         txt= (str(self.troops))                          ##### armazena o texto
         txtscreen = fontesys.render(txt, 1, (255,255,255))  	  ##### renderiza o texto na cor desejada
         screen.blit(txtscreen,(int(1590*self.ratio),int(600* self.ratio)))                   ##### coloca na posição 50,900 (tela FHD)


      #txt= ('RETURN')                          ##### armazena o texto
      #txtscreen = fontesys.render(txt, 1, (255,255,255))  	  ##### renderiza o texto na cor desejada
      #screen.blit(txtscreen,(int(1380*self.ratio),int(850* self.ratio)))                  ##### coloca na posição 50,900 (tela FHD)



################################################################################################################################


################################################################################################################################


   def execute(self, screen, events, op, player):
      operation = -1
      stop = False
      self.show(screen, op, player)
      for event in events:
         if event.type == pygame.MOUSEBUTTONDOWN:##Verifica o clique do mouse
            operation = self.checkClick(pygame.mouse.get_pos())
            return operation
			
################################# MEXIDA LUAN ############################################################
##Verifica se a tecla clicada é o esc, e retorna um valor especifico (55)
         if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
               return "pause"
#########################################################################################################
         if event.type == pygame.QUIT: ## Verifica se o usuario clicou no X vermelho para fechar
            pygame.quit()
            stop = True
      if stop:
         return -1

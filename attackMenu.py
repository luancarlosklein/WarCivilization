import pygame
import menu
from button import Button
from player import Player
import os

class AttackMenu(menu.Menu):
   def __init__(self, ratio):
      super().__init__(os.path.join("images", "transp.png"), soundBack = "none", soundEff = "none", volBack = 0, volEff = 0, ratioImage = ratio)
      ## o nome dos botoes ja diz o q eles sao...
      self.buttons.append(Button(os.path.join("images", "transp.png"), (int(1650*self.ratio), int(600*self.ratio)), int(100), int(100), "+"))
      self.buttons.append(Button(os.path.join("images", "transp.png"), (int(1450*self.ratio), int(600*self.ratio)), int(100), int(100), "-"))
      self.buttons.append(Button(os.path.join("images", "transp.png"), (int(1370*self.ratio), int(750*self.ratio)), int(100), int(250), "Select"))
      self.buttons.append(Button(os.path.join("images", "transp.png"), (int(1370*self.ratio), int(850*self.ratio)), int(100), int(250), "Return"))
      self.background = pygame.transform.scale(self.background,(int(1640*self.ratio) , int(1080*self.ratio)))
      self.hidden = True
      self.distribution = True
      self.troops = 0
   def show(self,screen, op):
      count = 0
      for i in self.buttons:
         count+=1
         if (op == 1 or count ==4 ):
            i.show(screen)
      
      pygame.font.init()                                ##### inicia font
      fonte=pygame.font.get_default_font()              ##### carrega com a fonte padrão
      fontesys=pygame.font.SysFont(fonte, int(self.ratio*60))           ##### usa a fonte padrão

      if (op == 0):
         txt= ('CHOOSE THE ATTACKING TERRITORY')                          ##### armazena o texto
         txtscreen = fontesys.render(txt, 1, (255,255,255))  	  ##### renderiza o texto na cor desejada
         screen.blit(txtscreen,(int(1250*self.ratio),int(650* self.ratio)))                  ##### coloca na posição 50,900 (tela FHD)

      if (op == 1):
         txt= ('CHOOSE THE DEFENDING TERRITORY')                          ##### armazena o texto
         txtscreen = fontesys.render(txt, 1, (255,255,255))  	  ##### renderiza o texto na cor desejada
         screen.blit(txtscreen,(int(1250*self.ratio),int(650* self.ratio)))                  ##### coloca na posição 50,900 (tela FHD)

      if (op == 2):
         txt= ('TROOPS: ')                          ##### armazena o texto
         txtscreen = fontesys.render(txt, 1, (255,255,255))  	  ##### renderiza o texto na cor desejada
         screen.blit(txtscreen,(int(1250*self.ratio),int(600* self.ratio)))                  ##### coloca na posição 50,900 (tela FHD)

         txt= ('+')                          ##### armazena o texto
         txtscreen = fontesys.render(txt, 1, (255,255,255))  	  ##### renderiza o texto na cor desejada
         screen.blit(txtscreen,(int(1670*self.ratio),int(600* self.ratio)))                  ##### coloca na posição 50,900 (tela FHD)


         txt= ('-')                          ##### armazena o texto
         txtscreen = fontesys.render(txt, 1, (255,255,255))  	  ##### renderiza o texto na cor desejada
         screen.blit(txtscreen,(int(1470*self.ratio),int(600* self.ratio)))                  ##### coloca na posição 50,900 (tela FHD)


         txt= ('SEND ATTACK')                          ##### armazena o texto
         txtscreen = fontesys.render(txt, 1, (255,255,255))  	  ##### renderiza o texto na cor desejada
         screen.blit(txtscreen,(int(1380*self.ratio),int(750* self.ratio)))                  ##### coloca na posição 50,900 (tela FHD)

         txt= (str(self.troops))                          ##### armazena o texto
         txtscreen = fontesys.render(txt, 1, (255,255,255))  	  ##### renderiza o texto na cor desejada
         screen.blit(txtscreen,(int(1570*self.ratio),int(600* self.ratio)))                  ##### coloca na posição 50,900 (tela FHD)


      txt= ('RETURN')                          ##### armazena o texto
      txtscreen = fontesys.render(txt, 1, (255,255,255))  	  ##### renderiza o texto na cor desejada
      screen.blit(txtscreen,(int(1380*self.ratio),int(850* self.ratio)))                  ##### coloca na posição 50,900 (tela FHD)



################################################################################################################################


################################################################################################################################


   def execute(self, screen, events, op):
      operation = -1
      stop = False
      self.show(screen, op)
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

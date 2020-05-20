import pygame
import menu
from button import Button
from player import Player
import os

class InGameMenu(menu.Menu):
   def __init__(self):
      super().__init__(os.path.join("images", "transparente.png"))
      self.buttons.append(Button(os.path.join("images", "seta.jpeg"), (1720*self.ratio, 100*self.ratio), 100, 100, "MAIS"))
      self.buttons[0].background = pygame.transform.flip(self.buttons[0].background, True, False)
      self.buttons.append(Button(os.path.join("images", "transp.png"), (1370*self.ratio, 130*self.ratio), 100, 250, "MAIS NEGO"))
      self.buttons.append(Button(os.path.join("images", "transp.png"), (1370*self.ratio, 280*self.ratio), 100, 250, "PAR TOUTATIS"))
      self.buttons.append(Button(os.path.join("images", "transp.png"), (1370*self.ratio, 430*self.ratio), 100, 250, "PAR TOUTATIS"))
      self.background = pygame.transform.scale(self.background,(1640*self.ratio , 1080*self.ratio))
      self.hidden = True
      self.distribution = True
   def show(self, screen, pos, player):
      if (self.hidden ==False):
         screen.blit(self.background, (1200*self.ratio,0))
      count =0
      for i in self.buttons:
         if (count >0 and self.hidden ==False and self.distribution == False):
            i.show(screen)
         elif (count ==0 and self.hidden ==True):
            i.pos = (1810*self.ratio, 100*self.ratio)
            i.show(screen)
         elif (count ==0 ):
            i.pos = (1210*self.ratio, 100*self.ratio)
            self.buttons[0].background = pygame.transform.flip(self.buttons[0].background, True, False)
            i.show(screen)
            self.buttons[0].background = pygame.transform.flip(self.buttons[0].background, True, False)
         count +=1

      if (self.hidden ==False):

############################################ imprime o nome do jogador ########################################################			

         pygame.font.init()                                ##### inicia font
         fonte=pygame.font.get_default_font()              ##### carrega com a fonte padrão
         fontesys=pygame.font.SysFont(fonte, 60)           ##### usa a fonte padrão
         txt= (player.name+'\'s TURN')                          ##### armazena o texto
         txtscreen = fontesys.render(txt, 1, (255,255,255))  	  ##### renderiza o texto na cor desejada
         screen.blit(txtscreen,(1320*self.ratio,30* self.ratio))                  ##### coloca na posição 50,900 (tela FHD)

################################################################################################################################

############################################ imprime o dinheiro do jogador do jogador ########################################################			

         txt= (str(player.money)+' Coins')                          ##### armazena o texto
         txtscreen = fontesys.render(txt, 1, (255,255,255))  	  ##### renderiza o texto na cor desejada
         screen.blit(txtscreen,(1720*self.ratio,30* self.ratio))                  ##### coloca na posição 50,900 (tela FHD)

################################################################################################################################
         if (self.distribution == False):
############################################ imprime os botoes do jogador do jogador ########################################################			

            txt= ('RECRUIT')                          ##### armazena o texto
            txtscreen = fontesys.render(txt, 1, (255,255,255))  	  ##### renderiza o texto na cor desejada
            screen.blit(txtscreen,(1380*self.ratio,150* self.ratio))                  ##### coloca na posição 50,900 (tela FHD)

            txt= ('ATTACK')                          ##### armazena o texto
            txtscreen = fontesys.render(txt, 1, (255,255,255))  	  ##### renderiza o texto na cor desejada
            screen.blit(txtscreen,(1380*self.ratio,300* self.ratio))                  ##### coloca na posição 50,900 (tela FHD)

            txt= ('END TURN')                         ##### armazena o texto
            txtscreen = fontesys.render(txt, 1, (255,255,255))  	  ##### renderiza o texto na cor desejada
            screen.blit(txtscreen,(1380*self.ratio,450* self.ratio))                  ##### coloca na posição 50,900 (tela FHD)

################################################################################################################################
         else:
            txt= ('CHOOSE YOUR NEW TERRITORY')                          ##### armazena o texto
            txtscreen = fontesys.render(txt, 1, (255,255,255))  	  ##### renderiza o texto na cor desejada
            screen.blit(txtscreen,(1220*self.ratio,500* self.ratio))                  ##### coloca na posição 50,900 (tela FHD)




############################################ imprime o brasão do jogador ########################################################			

         flag = player.emblem
         flag = pygame.transform.scale(flag,(245 , 291))
         screen.blit(flag,(1635*self.ratio,100*self.ratio))            

################################################################################################################################


   def execute(self, screen, events, player):
      operation = -1
      stop = False
      self.show(screen, operation, player)
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


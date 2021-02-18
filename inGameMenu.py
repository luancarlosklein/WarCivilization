import pygame
import menu
from hexagon import hexagon
from button import Button
from player import Player
import os

class InGameMenu(menu.Menu):
   def __init__(self, ratio):
      super().__init__(os.path.join("images", "transparente.png"), soundBack = "none", soundEff = "none", volBack = 0, volEff = 0, ratioImage = ratio)
      ##botao da seta para esconder e chamar o menu de jogo
      self.buttons.append(Button(os.path.join("images", "seta.jpeg"), (int(1720*self.ratio), int(100*self.ratio)), int(100), int(100), "MAIS"))
      ##controla o sentido da flecha (apontando para abrir ou fechar)
      self.buttons[0].background = pygame.transform.flip(self.buttons[0].background, True, False)
      ##botoes para: recrutar, atacar e pular turno
      self.buttons.append(Button(os.path.join("images", "transp.png"), (int(1370*self.ratio), int(130*self.ratio)), int(100), int(250), "MAIS NEGO"))
      self.buttons.append(Button(os.path.join("images", "transp.png"), (int(1370*self.ratio), int(280*self.ratio)), int(100), int(250), "PAR TOUTATIS"))
      self.buttons.append(Button(os.path.join("images", "transp.png"), (int(1370*self.ratio), int(430*self.ratio)), int(100), int(250), "PAR TOUTATIS"))
      ##background
      self.background = pygame.transform.scale(self.background,(int(1640*self.ratio) , int(1080*self.ratio)))
      ##atributo que diz se o menu está escondido
      self.hidden = True
      ##diz se está da etapa de escolher os territorios iniciais
      self.distribution = True

    ##mostrar na tela
   def show(self, screen, pos, player, chosenHex, showing):
      if (self.hidden ==False):
         screen.blit(self.background, (int(1200*self.ratio),0))
      count =0
      for i in self.buttons:
      	##botoes de draftar, atacar e end turn só aparecem com o menu aparecendo e apos a fase inicial
         if (count >0 and self.hidden ==False and self.distribution == False):
            i.show(screen)
        ##se tiver escondido, a flecha aparce no canto
         elif (count ==0 and self.hidden ==True):
            i.pos = (int(1810*self.ratio), int(100*self.ratio))
            i.show(screen)
        ##se tiver aparecendo, antes do background
         elif (count ==0 ):
            i.pos = (int(1210*self.ratio), int(100*self.ratio))
            self.buttons[0].background = pygame.transform.flip(self.buttons[0].background, True, False)
            i.show(screen)
            self.buttons[0].background = pygame.transform.flip(self.buttons[0].background, True, False)
         count +=1

      if (self.hidden ==False):

############################################ imprime o nome do jogador ########################################################			

         pygame.font.init()                                ##### inicia font
         fonte=pygame.font.get_default_font()              ##### carrega com a fonte padrão
         fontesys=pygame.font.SysFont(fonte, int(self.ratio*60))           ##### usa a fonte padrão
         txt= (player.name+'\'s TURN')                          ##### armazena o texto
         txtscreen = fontesys.render(txt, 1, (255,255,255))  	  ##### renderiza o texto na cor desejada
         screen.blit(txtscreen,(int(1320*self.ratio),int(30* self.ratio)))                  ##### coloca na posição 50,900 (tela FHD)

################################################################################################################################

############################################ imprime o dinheiro do jogador do jogador ########################################################			

         txt= (str(player.money)+' Coins')                          ##### armazena o texto
         txtscreen = fontesys.render(txt, 1, (255,255,255))  	  ##### renderiza o texto na cor desejada
         screen.blit(txtscreen,(int(1720*self.ratio),int(30* self.ratio)))                  ##### coloca na posição 50,900 (tela FHD)

################################################################################################################################
         if (self.distribution == False):
############################################ imprime os botoes do jogador do jogador ########################################################			

            txt= ('RECRUIT')                          ##### armazena o texto
            txtscreen = fontesys.render(txt, 1, (255,255,255))  	  ##### renderiza o texto na cor desejada
            screen.blit(txtscreen,(int(1380*self.ratio),int(150* self.ratio)))                  ##### coloca na posição 50,900 (tela FHD)

            txt= ('ATTACK')                          ##### armazena o texto
            txtscreen = fontesys.render(txt, 1, (255,255,255))  	  ##### renderiza o texto na cor desejada
            screen.blit(txtscreen,(int(1380*self.ratio),int(300* self.ratio)))                  ##### coloca na posição 50,900 (tela FHD)

            txt= ('END TURN')                         ##### armazena o texto
            txtscreen = fontesys.render(txt, 1, (255,255,255))  	  ##### renderiza o texto na cor desejada
            screen.blit(txtscreen,(int(1380*self.ratio),int(450* self.ratio)))                  ##### coloca na posição 50,900 (tela FHD)

            if ((isinstance(chosenHex, hexagon))== True and showing == 1 ):
               if (isinstance(chosenHex.owner, Player))==True:
                  txt1= ('OWNER: '+ chosenHex.owner.name)  
                  txt2 = ("TROOP COUNT: "+str(chosenHex.nTroop) )
               else:
                  txt1= ('UNEXPLORED TERRITORY')   
                  txt2 = ("TROOP COUNT: 0" )
               txt3 = ('BIOME: '+chosenHex.biome)
               txtscreen = fontesys.render(txt1, 1, (255,255,255))  	  ##### renderiza o texto na cor desejada
               screen.blit(txtscreen,(int(1380*self.ratio),int(550* self.ratio)))                 ##### coloca na posição 50,900 (tela FHD)
               txtscreen = fontesys.render(txt2, 1, (255,255,255))  	  ##### renderiza o texto na cor desejada
               screen.blit(txtscreen,(int(1380*self.ratio),int(650* self.ratio)))                 ##### coloca na posição 50,900 (tela FHD)
               txtscreen = fontesys.render(txt3, 1, (255,255,255))  	  ##### renderiza o texto na cor desejada
               screen.blit(txtscreen,(int(1380*self.ratio),int(750* self.ratio)))                  ##### coloca na posição 50,900 (tela FHD)



################################################################################################################################
         else:
            txt= ('CHOOSE YOUR NEW TERRITORY')                          ##### armazena o texto
            txtscreen = fontesys.render(txt, 1, (255,255,255))  	  ##### renderiza o texto na cor desejada
            screen.blit(txtscreen,(int(1220*self.ratio),int(500* self.ratio)))                  ##### coloca na posição 50,900 (tela FHD)




############################################ imprime o brasão do jogador ########################################################			

         flag = player.emblem
         flag = pygame.transform.scale(flag,(int(self.ratio*245) , int(self.ratio*291)))
         screen.blit(flag,(int(1635*self.ratio),int(100*self.ratio)))            

################################################################################################################################


   def execute(self, screen, events, player, chosenHex, showing =0):
      operation = -1
      stop = False
      self.show(screen, operation, player, chosenHex, showing)
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


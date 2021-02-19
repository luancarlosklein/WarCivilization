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
      self.buttons.append(Button(os.path.join("images", "seta.png"), (int(1620*self.ratio), int(50*self.ratio)), int(50), int(50), "MAIS"))
      

      ##controla o sentido da flecha (apontando para abrir ou fechar)
      self.buttons[0].background = pygame.transform.flip(self.buttons[0].background, True, False)
      ##botoes para: recrutar, atacar e pular turno
      self.buttons.append(Button(os.path.join("images", "buttonRecruit.png"), (int(1480*self.ratio), int(610*self.ratio)), int(200*self.ratio), int(300*self.ratio), "MAIS NEGO"))
      self.buttons.append(Button(os.path.join("images", "buttonAttack.png"), (int(1480*self.ratio), int(380*self.ratio)), int(200*self.ratio), int(300*self.ratio), "PAR TOUTATIS"))
      self.buttons.append(Button(os.path.join("images", "buttonEndTurn.png"), (int(1480*self.ratio), int(850*self.ratio)), int(100*self.ratio), int(300*self.ratio), "PAR TOUTATIS"))

      self.buttons.append(Button(os.path.join("images", "transp.png"), (int(550*self.ratio), int(0*self.ratio)), int(15), int(15), "CLOSE_INFORMATION"))

      ##background
      self.background = pygame.transform.scale(self.background,(int(600*self.ratio) , int(1080*self.ratio)))
      ##atributo que diz se o menu está escondido
      self.hidden = True
      ##diz se está da etapa de escolher os territorios iniciais
      self.distribution = True

      self.choose = pygame.image.load(os.path.join("images", "chooseTerritory.png")).convert_alpha()
      self.choose = pygame.transform.scale(self.choose,(int(500 * self.ratio), int(500 * self.ratio)))

      self.backInfo = pygame.image.load(os.path.join("images", "backgroundInformations.png")).convert_alpha()
      self.backInfo = pygame.transform.scale(self.backInfo,(int(587* self.ratio), int(600 * self.ratio)))

    ##mostrar na tela
   def show(self, screen, pos, player, chosenHex, showing):
      if (self.hidden ==False):
         screen.blit(self.background, (int(1320*self.ratio),0))
      count =0
      for i in self.buttons:
      	##botoes de draftar, atacar e end turn só aparecem com o menu aparecendo e apos a fase inicial
         if (count >0 and self.hidden ==False and self.distribution == False):
            i.show(screen)
        ##se tiver escondido, a flecha aparce no canto
         elif (count ==0 and self.hidden ==True):
            i.pos = (int(1810*self.ratio), int(85*self.ratio))
            i.show(screen)
        ##se tiver aparecendo, antes do background
         elif (count ==0 ):
            i.pos = (int(1810*self.ratio), int(85*self.ratio))
            self.buttons[0].background = pygame.transform.flip(self.buttons[0].background, True, False)
            i.show(screen)
            self.buttons[0].background = pygame.transform.flip(self.buttons[0].background, True, False)
         count +=1

      if (self.hidden ==False):

############################################ imprime o nome do jogador ########################################################			

         pygame.font.init()                                ##### inicia font
         fonte=pygame.font.get_default_font()              ##### carrega com a fonte padrão
         fontesys=pygame.font.SysFont(fonte, int(self.ratio*80))           ##### usa a fonte padrão
         txt= (player.name)                          ##### armazena o texto
         txtscreen = fontesys.render(txt, 1, (255,255,255))  	  ##### renderiza o texto na cor desejada
         screen.blit(txtscreen,(int(1550*self.ratio),int(310* self.ratio)))                  ##### coloca na posição 50,900 (tela FHD)

################################################################################################################################

############################################ imprime o dinheiro do jogador do jogador ########################################################			

         ##txt= (str(player.money)+' Coins')                          ##### armazena o texto
         ##txtscreen = fontesys.render(txt, 1, (255,255,255))  	  ##### renderiza o texto na cor desejada
         ##screen.blit(txtscreen,(int(1720*self.ratio),int(30* self.ratio)))                  ##### coloca na posição 50,900 (tela FHD)

################################################################################################################################
         if (self.distribution == False):
############################################ imprime os botoes do jogador do jogador ########################################################			

            ##txt= ('RECRUIT')                          ##### armazena o texto
            ##txtscreen = fontesys.render(txt, 1, (255,255,255))  	  ##### renderiza o texto na cor desejada
            ##screen.blit(txtscreen,(int(1380*self.ratio),int(150* self.ratio)))                  ##### coloca na posição 50,900 (tela FHD)

            
            ##screen.blit(self.attack, (1480* self.ratio, 380* self.ratio))
            ##screen.blit(self.recruit, (1480* self.ratio, 610* self.ratio)) 
            ##screen.blit(self.endTurn, (1480* self.ratio, 850* self.ratio))
            ##txt= ('ATTACK')                          ##### armazena o texto
            ##txtscreen = fontesys.render(txt, 1, (255,255,255))  	  ##### renderiza o texto na cor desejada
            ##screen.blit(txtscreen,(int(1380*self.ratio),int(300* self.ratio)))                  ##### coloca na posição 50,900 (tela FHD)

            ##txt= ('END TURN')                         ##### armazena o texto
            ##txtscreen = fontesys.render(txt, 1, (255,255,255))  	  ##### renderiza o texto na cor desejada
            ##screen.blit(txtscreen,(int(1380*self.ratio),int(450* self.ratio)))                  ##### coloca na posição 50,900 (tela FHD)

            if ((isinstance(chosenHex, hexagon))== True):
               screen.blit(self.backInfo, (0* self.ratio, 0* self.ratio))
               font = pygame.font.Font(os.path.join("fonts", "seagram.ttf") , int(30*self.ratio))
               if (isinstance(chosenHex.owner, Player))==True:
                  
                  txt1= (chosenHex.owner.name)  
                  txt2 = ("Troops: "+str(chosenHex.nTroop))
                  flag = chosenHex.owner.emblem
                  flag = pygame.transform.scale(flag,(int(self.ratio*103) , int(self.ratio*122)))
                  screen.blit(flag, (self.ratio*250,self.ratio*130))

               else:
                  txt1= ('Unexplored')   
                  txt2 = ("Troops: 0" )
                  
               txt= ('X')                          ##### armazena o texto
               txtscreen = font.render(txt, 1, (255,0,0))  	  ##### renderiza o texto na cor desejada
               screen.blit(txtscreen,(int(550*self.ratio),int(0* self.ratio)))                  ##### coloca na posição 50,900 (tela FHD)

               txt3 = ('Biome: '+chosenHex.biome)
               txtscreen = font.render(txt1, 1, (255,255,255))  	  ##### renderiza o texto na cor desejada
               screen.blit(txtscreen,(int(110*self.ratio),int(270* self.ratio)))                 ##### coloca na posição 50,900 (tela FHD)
               txtscreen = font.render(txt2, 1, (255,255,255))  	  ##### renderiza o texto na cor desejada
               screen.blit(txtscreen,(int(110*self.ratio),int(330* self.ratio)))                 ##### coloca na posição 50,900 (tela FHD)
               txtscreen = font.render(txt3, 1, (255,255,255))  	  ##### renderiza o texto na cor desejada
               screen.blit(txtscreen,(int(110*self.ratio),int(390* self.ratio)))                  ##### coloca na posição 50,900 (tela FHD)
               

################################################################################################################################
         else:
           


            screen.blit(self.choose, (1370* self.ratio, 420* self.ratio)) 
            ##txt= ('CHOOSE YOUR NEW TERRITORY')                          ##### armazena o texto
            ##txtscreen = fontesys.render(txt, 1, (255,255,255))  	  ##### renderiza o texto na cor desejada
            ##screen.blit(txtscreen,(int(1220*self.ratio),int(500* self.ratio)))                  ##### coloca na posição 50,900 (tela FHD)




############################################ imprime o brasão do jogador ########################################################			

         flag = player.emblem
         flag = pygame.transform.scale(flag,(int(self.ratio*171) , int(self.ratio*204)))
         screen.blit(flag,(int(1530*self.ratio),int(100*self.ratio)))            

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


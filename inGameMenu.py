import pygame
import menu
from hexagon import hexagon
from button import Button
from player import Player
import os

class InGameMenu(menu.Menu):
   def __init__(self, ratio):
      super().__init__(os.path.join("images", "backgroundMainMenu.png"), soundBack = "none", soundEff = "none", volBack = 0, volEff = 0, ratioImage = ratio)
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

      ## Define a imagem que informa para escolher o territorio
      self.choose = pygame.image.load(os.path.join("images", "chooseTerritory.png")).convert_alpha()
      self.choose = pygame.transform.scale(self.choose,(int(500 * self.ratio), int(500 * self.ratio)))

      ## Define o background da parte que mostra as informações do hexagono
      self.backInfo = pygame.image.load(os.path.join("images", "backgroundInformations.png")).convert_alpha()
      self.backInfo = pygame.transform.scale(self.backInfo,(int(587* self.ratio), int(600 * self.ratio)))

      ## Define o background da moeda
      self.coin = pygame.image.load(os.path.join("images", "coin.png")).convert_alpha()
      self.coin = pygame.transform.scale(self.coin,(int(70* self.ratio), int(70 * self.ratio)))

      ## Define o background da honra
      self.honor = pygame.image.load(os.path.join("images", "honor.png")).convert_alpha()
      self.honor = pygame.transform.scale(self.honor,(int(75* self.ratio), int(75 * self.ratio)))

   ##Metodo que mostra na tela
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
         ##fontesys=pygame.font.SysFont(fonte, int(self.ratio*35))
         fontesys = pygame.font.Font(os.path.join("fonts", "ARMY_RUST.ttf") , int(50*self.ratio))
         screen.blit(self.coin,(int(1660*self.ratio),int(210* self.ratio)))
         txt= (str(player.money))                          ##### armazena o texto
         txtscreen = fontesys.render(txt, 1, (0,0,0))  	  ##### renderiza o texto na cor desejada
         screen.blit(txtscreen,(int(1730*self.ratio),int(225* self.ratio)))                  ##### coloca na posição 50,900 (tela FHD)


         txt = str(player.morale)
         txtscreen = fontesys.render(txt, 1, (0,0,0))
         screen.blit(self.honor,(int(1650*self.ratio),int(130* self.ratio)))
         screen.blit(txtscreen,(int(1730*self.ratio),int(145* self.ratio)))
      
################################################################################################################################

         if (self.distribution == True):           
            screen.blit(self.choose, (1370* self.ratio, 420* self.ratio)) 
            
############################################ imprime o brasão do jogador ########################################################			

         flag = player.emblem
         flag = pygame.transform.scale(flag,(int(self.ratio*171) , int(self.ratio*204)))
         screen.blit(flag,(int(1480*self.ratio),int(100*self.ratio)))            

########################################## imprime as informações do hexago clicado ######################################################
      
      if ((isinstance(chosenHex, hexagon))== True and self.distribution == False):
         screen.blit(self.backInfo, (0* self.ratio, 0* self.ratio))
         font = pygame.font.Font(os.path.join("fonts", "seagram.ttf") , int(30*self.ratio))
         if (isinstance(chosenHex.owner, Player))==True:
            
            txt1= (chosenHex.owner.name)  
            txt2 = ("Troops: "+ str(chosenHex.nTroop))
            txt3 = ("Moral: " + str(chosenHex.owner.morale))
            flag = chosenHex.owner.emblem
            flag = pygame.transform.scale(flag,(int(self.ratio*103) , int(self.ratio*122)))
            screen.blit(flag, (self.ratio*250,self.ratio*130))

         else:
            txt1= ('Unexplored')   
            txt2 = ("Troops: 0" )
            txt3 = ("Moral: 0")
            
         txt= ('X')                          ##### armazena o texto
         txtscreen = font.render(txt, 1, (255,0,0))     ##### renderiza o texto na cor desejada
         screen.blit(txtscreen,(int(550*self.ratio),int(0* self.ratio)))                  ##### coloca na posição 50,900 (tela FHD)

         txt4 = ('Biome: '+chosenHex.biome)
         
         txtscreen = font.render(txt1, 1, (255,255,255))      ##### renderiza o texto na cor desejada
         screen.blit(txtscreen,(int(110*self.ratio),int(270* self.ratio)))                 ##### coloca na posição 50,900 (tela FHD)
         txtscreen = font.render(txt2, 1, (255,255,255))      ##### renderiza o texto na cor desejada
         screen.blit(txtscreen,(int(110*self.ratio),int(315* self.ratio)))                 ##### coloca na posição 50,900 (tela FHD)
         txtscreen = font.render(txt3, 1, (255,255,255))      ##### renderiza o texto na cor desejada
         screen.blit(txtscreen,(int(110*self.ratio),int(360* self.ratio)))                  ##### coloca na posição 50,900 (tela FHD)
         txtscreen = font.render(txt4, 1, (255,255,255))      ##### renderiza o texto na cor desejada
         screen.blit(txtscreen,(int(110*self.ratio),int(405* self.ratio)))                  ##### coloca na posição 50,900 (tela FHD)
         
################################################################################################################################

   def execute(self, screen, events, player, chosenHex, showing =0):
      operation = -1
      stop = False
      self.show(screen, operation, player, chosenHex, showing)
      for event in events:
         if event.type == pygame.MOUSEBUTTONDOWN:##Verifica o clique do mouse
            operation = self.checkClick(pygame.mouse.get_pos())
            return operation
         			
         ##Verifica se a tecla clicada é o esc, e retorna um valor especifico (55)
         if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
               return "pause"
         if event.type == pygame.QUIT: ## Verifica se o usuario clicou no X vermelho para fechar
            pygame.quit()
            stop = True
      if stop:
         return -1


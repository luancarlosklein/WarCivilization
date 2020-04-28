import pygame
import menu
from button import Button
import os

class inGameMenu(menu.Menu):
	def __init__(self):
		super().__init__(os.path.join("images", "tavredonda.jpg"))
		self.buttons.append(Button(os.path.join("images", "draft.jpg"), (500, 300), 100, 201, "MAIS NEGO"))
		self.buttons.append(Button(os.path.join("images", "invasion.jpg"), (500, 450), 100, 201, "PAR TOUTATIS"))
		self.background = pygame.transform.scale(self.background,(518 , 388))
	def show(self, screen):
		screen.blit(self.background, (482,262))
		for i in self.buttons:
		    i.show(screen)

	############################################ imprime o nome do jogador ########################################################			

		pygame.font.init()                                ##### inicia font
		fonte=pygame.font.get_default_font()              ##### carrega com a fonte padrão
		fontesys=pygame.font.SysFont(fonte, 60)           ##### usa a fonte padrão
		txt= ('NAME'+'\'s TURN')                          ##### armazena o texto
		txtscreen = fontesys.render(txt, 1, (0,0,0))  	  ##### renderiza o texto na cor desejada
		screen.blit(txtscreen,(715,270))                  ##### coloca na posição 50,900 (tela FHD)

	################################################################################################################################


	############################################ imprime o brasão do jogador ########################################################			

		flag = pygame.image.load(os.path.join("images", "flag1.jfif")).convert_alpha()
		flag = pygame.transform.scale(flag,(245 , 291))
		screen.blit(flag,(715,350))            

	################################################################################################################################


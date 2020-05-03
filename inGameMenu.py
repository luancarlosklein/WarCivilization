import pygame
import menu
from button import Button
import os

class InGameMenu(menu.Menu):
	def __init__(self):
		super().__init__(os.path.join("images", "tavredonda.jpg"))
		self.buttons.append(Button(os.path.join("images", "seta.jpeg"), (800, 100), 100, 100, "MAIS"))
		self.buttons[0].background = pygame.transform.flip(self.buttons[0].background, True, False)
		self.buttons.append(Button(os.path.join("images", "draft.jpg"), (500, 130), 100, 201, "MAIS NEGO"))
		self.buttons.append(Button(os.path.join("images", "invasion.jpg"), (500, 280), 100, 201, "PAR TOUTATIS"))
		self.background = pygame.transform.scale(self.background,(518 , 388))
		self.hidden = True
	def show(self, screen, pos):
		count =0
		for i in self.buttons:
			if (count >0 and self.hidden ==False):
				screen.blit(self.background, (500,0))
				i.show(screen)
			elif (count ==0 and self.hidden ==True):
				i.pos = (890, 100)
				i.show(screen)
			elif (count ==0 ):
				i.pos = (390, 100)
				i.show(screen)
			count +=1

		if (self.hidden ==False):

	############################################ imprime o nome do jogador ########################################################			

			pygame.font.init()                                ##### inicia font
			fonte=pygame.font.get_default_font()              ##### carrega com a fonte padrão
			fontesys=pygame.font.SysFont(fonte, 60)           ##### usa a fonte padrão
			txt= ('NAME'+'\'s TURN')                          ##### armazena o texto
			txtscreen = fontesys.render(txt, 1, (0,0,0))  	  ##### renderiza o texto na cor desejada
			screen.blit(txtscreen,(600,30))                  ##### coloca na posição 50,900 (tela FHD)

	################################################################################################################################


	############################################ imprime o brasão do jogador ########################################################			

			flag = pygame.image.load(os.path.join("images", "flag1.png")).convert_alpha()
			flag = pygame.transform.scale(flag,(245 , 291))
			screen.blit(flag,(715,100))            

	################################################################################################################################


	def execute(self, screen, events):
		operation = -1
		stop = False
		self.show(screen, operation)
		for event in events:
			if event.type == pygame.MOUSEBUTTONDOWN:##Verifica o clique do mouse
				operation = self.checkClick(pygame.mouse.get_pos())
				return operation
	
			if event.type == pygame.QUIT: ## Verifica se o usuario clicou no X vermelho para fechar
				pygame.quit()
				stop = True
		if stop:
			return -1


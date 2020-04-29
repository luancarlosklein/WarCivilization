import pygame
import menu
from button import Button
import os

class playerInfoSelector(menu.Menu):
	def __init__(self):
		super().__init__(os.path.join("images", "tavredonda.jpg"))
		self.flags = ["flag1.png", "flag2.png", "flag3.png"]
		self.buttons.append(Button(os.path.join("images", "seta.jpeg"), (10, 200), 50, 50, "PAR TOUTATIS"))
		self.buttons.append(Button(os.path.join("images", "seta.jpeg"), (200, 200), 50, 50, "PAR TOUTATIS"))
		self.buttons.append(Button(os.path.join("images", "flag1.png"), (60, 10), 200, 200, "PAR TOUTATIS"))
		self.buttons[0].background = pygame.transform.flip(self.buttons[1].background, True, False)


	def show(self, screen):
		screen.blit(self.background, (482,262))
		for i in self.buttons:
		    i.show(screen)


	def checkClick(self, pos):
		count=0
		for i in self.buttons:
			posButton = i.getPos()
			sizeButton = i.getSize()
			if pos[0] <= (posButton[0] + sizeButton[0]) and pos[0] >= posButton[0]:
				if pos[1] <= (posButton[1] + sizeButton[1]) and pos[1] >= posButton[1]:
					print(i.getAction())
					return count
			count+=1
		return False

	def execute(self, screen):
		operation = -1
		stop = False
		self.show(screen)
		pygame.display.flip()
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:##Verifica o clique do mouse
				operation = self.checkClick(pygame.mouse.get_pos())
				return operation

			##Verifica se o usuario apertou a tecla Q 
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					pygame.quit()##Fecha a tela pygame
					stop = True 
			if event.type == pygame.QUIT: ## Verifica se o usuario clicou no X vermelho para fechar
				pygame.quit()
				stop = True
		if stop:
			return -1

	def chooseFlag (self, screen):
		i = 1
		while 1:
			operation = self.execute(screen)
			#print (operation)
			if operation ==0 and  i!=1:
				i-=1
			if operation ==1 and i!= 3:
				i+=1
			self.buttons[0].background = pygame.image.load(os.path.join("images", "flag"+str(i)+".png")).convert_alpha()
			
		






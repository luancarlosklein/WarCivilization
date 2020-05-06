import pygame
from hexagon import hexagon

class mapManager:
	def __init__(self, background = 0):
		self.hexagons = []
		self.background = background
		self.nCol = 9			# Numero de hexagonos por coluna
		self.nRow = 19			# Numero de hexagonos por linha
		self.hexaLen = 30
		self.lastPos = [0,0]
		self.rmClick = False	# Flag para o click do botao direito do mouse

		deslocate = 1
		pos = [85,50]
		start = [85,50]
		color = [0,255,0]

		for i in range (self.nRow):
			for j in range (self.nCol):
				self.hexagons.append(hexagon(0, pos, 0, 0, 0, self.hexaLen, color))
				pos = [pos[0] + 3*self.hexagons[0].mod*self.hexaLen, pos[1]]
			if not deslocate:
				self.hexagons.append(hexagon(0, pos, 0, 0, 0, self.hexaLen, color))
			pos = [start[0], pos[1]+self.hexagons[0].length]
			if (deslocate):
				pos[0] -= 1.5*self.hexagons[0].mod*self.hexaLen
				deslocate = 0
				color = [50,50,50]
			else:
				deslocate = 1
				color = [50,255,50]

	def set_nCol(self, num):
		self.nCol = num

	def set_nRow(self,num):
		self.nRow = num
	
	def show(self, screen):
		for hexagon in self.hexagons:
			hexagon.show(screen, self.hexaLen)
		self.check_translation()

	def resizeHexagons(self):
		i = 0

		pos = self.hexagons[0].center
		start = self.hexagons[0].center
		deslocate = 1
		lenght = self.hexaLen
		mod = self.hexagons[0].mod

		for row in range (self.nRow):
			for col in range (self.nCol):
				self.hexagons[i].setCenter(pos)
				pos = [pos[0] + 3*mod*lenght, pos[1]]
				i += 1
			if not deslocate:
				self.hexagons[i].setCenter(pos)
				i += 1
			pos = [start[0], pos[1]+lenght]
			if deslocate:
				pos[0] -= 1.5*mod*lenght
				deslocate = 0
			else:
				deslocate = 1

	def check_translation(self):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_LEFT]:
			for hexagon in self.hexagons:
				hexagon.setDes([hexagon.getDes()[0] + 5, hexagon.getDes()[1]])
		if keys[pygame.K_RIGHT]:
			for hexagon in self.hexagons:
				hexagon.setDes([hexagon.getDes()[0] - 5, hexagon.getDes()[1]])
		if keys[pygame.K_UP]:
			for hexagon in self.hexagons:
				hexagon.setDes([hexagon.getDes()[0], hexagon.getDes()[1] + 5])
		if keys[pygame.K_DOWN]:
			for hexagon in self.hexagons:
				hexagon.setDes([hexagon.getDes()[0], hexagon.getDes()[1] - 5])
		if keys[pygame.K_SPACE]:
			mousePos = pygame.mouse.get_pos()
			if self.rmClick:
				for hexagon in self.hexagons:
					hexagon.deslocate([mousePos[0] - self.lastPos[0], mousePos[1] - self.lastPos[1]])
			else:
				self.rmClick = True
			self.lastPos = mousePos
		else:
			if self.rmClick == True:
				self.rmClick = False

		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 4:
					#for hexagon in self.hexagons:
					#	hexagon.setLen(hexagon.getLen()+5)
					self.hexagons[0].setLen(self.hexagons[0].getLen()+5)
					self.hexaLen += 5
					self.resizeHexagons()

				if event.button == 5:
					# for hexagon in self.hexagons:
					# 	hexagon.setLen(hexagon.getLen()-5)
					self.hexagons[0].setLen(self.hexagons[0].getLen()-5)
					self.hexaLen -= 5
					self.resizeHexagons()
				
			# 	if event.button == 3:
			# 		print("DOWN")
			# 		if (self.rmClick):
			# 			for hexagon in self.hexagons:
			# 				hexagon.des(pygame.mouse.get_pos() - self.lastPos)
			# 		else:
			# 			self.rmClick = True
			# 		self.lastPos = pygame.mouse.get_pos()

			# if event.type == pygame.MOUSEBUTTONUP:
			# 	if event.button == 3:
			# 		print("UP")
			# 		self.rmClick = False



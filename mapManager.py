import pygame
import random
from hexagon import hexagon

class mapManager:
	def __init__(self, background = 0):
		self.hexagons = []
		self.background = background
		self.nCol = 9			# Numero de hexagonos por coluna
		self.nRow = 19			# Numero de hexagonos por linha
		self.hexaLen = 30
		self.lastPos = [0,0]
		self.step = 5
		self.rmClick = False	# Flag para o click do botao direito do mouse
		self.biomes = ["plain", "forest", "snow", "desert"]
		self.biomes = {
			"plain" : (153,255,51),
			"forest": (0,51,0),
			"snow" : (220,255,255),
			"desert" : (219,191, 28)
		}

		self.owners = ["France", "Brazil", "USA"]
		self.clicked = 0

		
		self.surface = pygame.Surface((260,160), pygame.SRCALPHA)

		pygame.draw.polygon(self.surface, (255,0,0), [(130 + 0 - (1.1547*30/2),80 + 0 -30),(130 + 0 -(1.1547*30),
		80 + 0 ),(130 + 0 -(1.1547*30/2),80 + 0 +30),(130 + 0 +(1.1547*30/2),80 + 0 +30),
		(130 + 0 +(1.1547*30),80 + 0 ),(130 + 0 +(1.1547*30/2),80 + 0 -30)])

		self.alpha_surf = pygame.Surface((260,160), pygame.SRCALPHA)
		self.alpha_surf.fill((255,255,255,120))

		self.surface.blit(self.alpha_surf, (0,0), special_flags=pygame.BLEND_RGBA_MULT)

		deslocate = 1
		pos = [85,50]
		start = [85,50]

		for i in range (self.nRow):
			for j in range (self.nCol):
				biome = random.choice(list(self.biomes))
				owner = random.choice(list(self.owners))
				self.hexagons.append(hexagon(pos, biome, owner, 0, self.hexaLen))
				pos = [pos[0] + 3*self.hexagons[0].mod*self.hexaLen, pos[1]]
			if not deslocate:
				biome = random.choice(list(self.biomes))
				owner = random.choice(list(self.owners))
				self.hexagons.append(hexagon(pos, biome, owner, 0, self.hexaLen))
			pos = [start[0], pos[1]+self.hexagons[0].length]
			if (deslocate):
				pos[0] -= 1.5*self.hexagons[0].mod*self.hexagons[0].getLen()
				deslocate = 0
			else:
				deslocate = 1

	def set_nCol(self, num):
		self.nCol = num

	def set_nRow(self,num):
		self.nRow = num
	
	def show(self, screen):
		#rect = self.surface.get_rect()

		self.check_click()

		pygame.draw.rect(screen, (9,46,255), (0, 0, 1920, 1080))
		for hexagon in self.hexagons:
			hexagon.show(screen)
		self.check_translation()
		#screen.blit(self.surface, rect)
	

	def resizeHexagons(self):
		i = 0

		pos = self.hexagons[0].center
		start = self.hexagons[0].center
		deslocate = 1
		lenght = self.hexagons[0].getLen()
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
				hexagon.setDes([hexagon.getDes()[0] + self.step, hexagon.getDes()[1]])
		if keys[pygame.K_RIGHT]:
			for hexagon in self.hexagons:
				hexagon.setDes([hexagon.getDes()[0] - self.step, hexagon.getDes()[1]])
		if keys[pygame.K_UP]:
			for hexagon in self.hexagons:
				hexagon.setDes([hexagon.getDes()[0], hexagon.getDes()[1] + self.step])
		if keys[pygame.K_DOWN]:
			for hexagon in self.hexagons:
				hexagon.setDes([hexagon.getDes()[0], hexagon.getDes()[1] - self.step])
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
		if keys[pygame.K_z] and self.hexagons[0].getLen() <= 70:
			for hexagon in self.hexagons:
				hexagon.setLen(hexagon.getLen()+self.step)
			self.resizeHexagons()
			self.step += 3
			for hexagon in self.hexagons:
				hexagon.configSurf()
		if keys[pygame.K_x] and self.hexagons[0].getLen() >= 20:
			for hexagon in self.hexagons:
				hexagon.setLen(hexagon.getLen()-self.step)
			self.resizeHexagons()
			self.step -= 3
			for hexagon in self.hexagons:
				hexagon.configSurf()

		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 4:
					for hexagon in self.hexagons:
						hexagon.setLen(hexagon.getLen()+self.step)
					self.resizeHexagons()
					self.step += 3
					for hexagon in self.hexagons:
						hexagon.configSurf()

				if event.button == 5:
					for hexagon in self.hexagons:
						hexagon.setLen(hexagon.getLen()+self.step)
					self.resizeHexagons()
					self.step -= 3
					for hexagon in self.hexagons:
						hexagon.configSurf()
				
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
	def check_click(self):
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				print("!!!!!!!!!!!")
				if event.button == 4:
					mouse = pygame.mouse.get_pos()
					for hexagon in self.hexagons:
						if (hexagon.checkClick(mouse)):
							hexagon.setColor((50,50,50))
							return hexagon

		keys = pygame.key.get_pressed()

		if keys[pygame.K_l]:
			mouse = pygame.mouse.get_pos()
			for hexagon in self.hexagons:
				if (hexagon.checkClick(mouse)):
					hexagon.setColor((50,50,50))
					return hexagon
		return False


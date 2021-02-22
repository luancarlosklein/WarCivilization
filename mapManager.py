import pygame
import random
from hexagon import hexagon

class mapManager:
	def __init__(self, background = 0, ratioE = 1):
		self.hexagons = []
		self.ratioE = ratioE
		self.background = background
		self.nCol = 9			# Numero de hexagonos por coluna
		self.nRow = 19			# Numero de hexagonos por linha
		self.hexaLen = 30
		self.lastPos = [0,0]
		self.step = 5
		self.rmClick = False	# Flag para o click do botao direito do mouse
		self.biomes = ["plain", "forest", "snow", "desert"]
		self.biomes_colors = {
			"plain" : (92,222,31),#(153,255,51),
			"forest": (0,51,0),
			"snow" : (220,255,255),
			"desert" : (219,191, 28)
		}
		self.biome_count = [0,0,0,0]
		self.biomes_pos = {
			"plain" : -1,
			"forest": random.randrange(self.nCol*3,self.nCol*(self.nRow-3)),
			"snow" : self.nCol,
			"desert" : (self.nCol * (self.nRow - 1)) + int(self.nRow / 2) - 1
		}

		self.biomes_len = {
			"plain" : -1,
			"forest": random.randrange(0,self.nCol/3 + 1),
			"snow" : random.randrange(0,self.nCol/3 + 1),
			"desert" : random.randrange(0,self.nCol/3 + 1)
		}

		self.owners=["France","Brazil","USA","Egypt","Mongolia","Soviet Union","Greece","Pirates","Great Britain","Italy","Cuba","Spain","Japan","China","India","Portugal"]
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
			biome = self.biomes[0]
			for j in range (self.nCol):

				owner = random.choice(list(self.owners))
				self.hexagons.append(hexagon(pos, biome, owner, 0, self.hexaLen, self.ratioE))
				pos = [pos[0] + 3 * self.hexagons[0].mod * self.hexaLen * self.ratioE, pos[1]]
			
			if not deslocate:
				owner = random.choice(list(self.owners))
				self.hexagons.append(hexagon(pos, biome, owner, 0, self.hexaLen, self.ratioE))
			pos = [start[0], pos[1]+self.hexagons[0].getLen()]
			if (deslocate):
				pos[0] -= 1.5*self.hexagons[0].mod*self.hexagons[0].getLen()
				deslocate = 0
			else:
				deslocate = 1

		it = 0
		deslocate = 1

		for i in range (self.nRow):
			for j in range (self.nCol):
				for bioma in self.biomes:
					p = self.biomes_pos[bioma]
					if (p == it):
						self.hexagons[it].setBioma(bioma)
						self.increase_bio_count(bioma)
					elif self.biomes_len[bioma] != -1:
						if self.hexagons[p].distanceTo(self.hexagons[it]) <= self.biomes_len[bioma]:
							self.hexagons[it].setBioma(bioma)
							self.increase_bio_count(bioma)
				it += 1

			if (deslocate):
				deslocate = 0
			else:
				for bioma in self.biomes:
					p = self.biomes_pos[bioma]
					if (p == it):
						self.hexagons[it].setBioma(bioma)
						self.increase_bio_count(bioma)
					elif self.biomes_len[bioma] != -1:
						if self.hexagons[p].distanceTo(self.hexagons[it]) <= self.biomes_len[bioma]:
							self.hexagons[it].setBioma(bioma)
							self.increase_bio_count(bioma)
				it += 1
				deslocate = 1
		self.biome_count[0] = len(self.hexagons) - (self.biome_count[1]+self.biome_count[2]+self.biome_count[3])


	def set_ratioE(self, ratioE):
		self.ratioE = ratioE
		for hexagon in self.hexagons:
			hexagon.set_ratioE(self.ratioE)

	def set_nCol(self, num):
		self.nCol = num

	def set_nRow(self,num):
		self.nRow = num
	
	def show(self, screen, events):
		#rect = self.surface.get_rect()

		#self.check_click()

		pygame.draw.rect(screen, (9,46,255), (0, 0, 1920, 1080))
		for hexagon in self.hexagons:
			hexagon.show(screen)
		self.check_translation(events)
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

	def check_translation(self, events):
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
		if pygame.mouse.get_pressed()[2]:
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
		if (keys[pygame.K_z] and self.hexagons[0].getLen() <= 70):
			for hexagon in self.hexagons:
				hexagon.setLen((hexagon.getLen()/self.ratioE)+self.step)
			self.resizeHexagons()
			self.step += 3
			for hexagon in self.hexagons:
				hexagon.configSurf()
		if (keys[pygame.K_x] and self.hexagons[0].getLen() >= 20):
			for hexagon in self.hexagons:
				hexagon.setLen((hexagon.getLen()/self.ratioE)-self.step)
			self.resizeHexagons()
			self.step -= 3
			for hexagon in self.hexagons:
				hexagon.configSurf()	



		for event in events:
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
						
	def check_click(self):
		answer = False
		if pygame.mouse.get_pressed()[0]:
			mouse = pygame.mouse.get_pos()
			for hexagon in self.hexagons:
				if (answer == False and hexagon.checkClick(mouse)):
					hexagon.setColor((50,50,50))
					answer = hexagon
				else:
					hexagon.setOwnerColor()
		return answer

	def check_corners(self):
		owner = self.hexagons[0].owner
		if (self.hexagons [self.nCol-1] == owner and self.hexagons[self.nRow*self.nCol-1].owner == owner and self.hexagons[self.nRow*self.nCol- self.nCol].owner == owner ):
			return owner
		return False

	def increase_bio_count(self, biome):
		if (biome == "plain"):
			self.biome_count[0] +=1
		elif (biome == "forest"):
			self.biome_count[1] +=1
		elif (biome == "snow"):
			self.biome_count[2] +=1
		elif (biome == "desert"):
			self.biome_count[3] +=1


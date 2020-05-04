import menu
from button import Button
import os

class DraftMenu(menu.Menu):
	def __init__(self):
		super().__init__(os.path.join("images", "tavredonda.jpg"), 1, 1)
		self.buttons.append(Button(os.path.join("images", "draft.jpg"), (10, 70), 50, 201, "MAIS NEGO"))
		self.buttons.append(Button(os.path.join("images", "invasion.jpg"), (10, 10), 50, 201, "PAR TOUTATIS"))
	def show(self, screen):
		screen.blit(self.background, (0,0))
		for i in self.buttons:
		    i.show(screen)

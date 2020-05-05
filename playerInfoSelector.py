import pygame
import time
import menu
from button import Button
import os
from textInput import TextInput

class PlayerInfoSelector(menu.Menu):
   def __init__(self):
      super().__init__(os.path.join("images", "tavredonda.jpg"))
      self.background = pygame.transform.scale(self.background,(1000 , 650))
      self.flags = ["flag1.png", "flag2.png", "flag3.png"]
      self.buttons.append(Button(os.path.join("images", "seta.jpeg"), (200, 300), 100, 100, "MENOS"))
      self.buttons.append(Button(os.path.join("images", "seta.jpeg"), (800, 300), 100, 100, "MAIS"))
      self.buttons.append(Button(os.path.join("images", "flag1.png"), (350, 100), 466,392, "BANDEIRA"))
      self.buttons[0].background = pygame.transform.flip(self.buttons[1].background, True, False)


   def show(self, screen):
      screen.blit(self.background, (0,0))
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

   def execute(self, screen, events):
      operation = -1
      stop = False
      self.show(screen)
      for event in events:
         if event.type == pygame.MOUSEBUTTONDOWN:##Verifica o clique do mouse
            operation = self.checkClick(pygame.mouse.get_pos())
            return operation
	
         if event.type == pygame.QUIT: ## Verifica se o usuario clicou no X vermelho para fechar
            pygame.quit()
            stop = True
      if stop:
         return -1

   def chooseFlag (self):		
      screen = pygame.display.get_surface()
      pygame.display.update()
      i = 1
      while 1:
         events= pygame.event.get()	
         operation = self.execute(screen, events)
         if operation ==0 and  i!=1:
            i-=1
         if operation ==1 and i!= 3:
            i+=1
         self.buttons[2].background = pygame.image.load(os.path.join("images", "flag"+str(i)+".png")).convert_alpha()
         if operation == 2:
            return self.buttons[2].background
         pygame.display.update()
         time.sleep (0.03)

   def chooseName (self ):
      txt_input = TextInput()
      screen = pygame.display.get_surface()
      name = "empty"
      while True:
         color_white = (255, 255, 255)
         screen.fill(color_white)
         events= pygame.event.get()	
         for event in events:
            if event.type == pygame.QUIT:
               exit()
            elif event.type == pygame.KEYDOWN:
               if event.key == pygame.K_RETURN:
                  name = txt_input.get_text()
                  txt_input.clear_text()
                  return name.lower()

		
      txt_input.update(events)
      name = txt_input.get_text()
      screen.blit(txt_input.get_surface(), (10, 10))
      pygame.display.update()
      time.sleep (0.03)
		






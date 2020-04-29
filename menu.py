import pygame
import button
class Menu:
    def __init__(self, backImage):
        self.background = pygame.image.load(backImage).convert_alpha()
        self.buttons = []
        self.background = pygame.transform.scale(self.background, (1000, 650))
        
    ##Método que verifica em qual botão foi clicado
    def checkClick(self, pos):
        for i in self.buttons:
            posButton = i.getPos()
            sizeButton = i.getSize()
            if pos[0] <= (posButton[0] + sizeButton[0]) and pos[0] >= posButton[0]:
                if pos[1] <= (posButton[1] + sizeButton[1]) and pos[1] >= posButton[1]:
                    print(i.getAction())
                    return i
        return False

    def checkMouseOn(self, pos):
        return self.checkClick(pos)
    
        
        
    def show(self):
        b = 1
        ##Método que mostra o menu na tela

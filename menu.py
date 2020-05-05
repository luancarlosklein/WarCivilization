import pygame
import button
class Menu:
    def __init__(self, backImage = "none", soundBack = "none", soundEff = "none", volBack = 0, volEff = 0):
        self.background = pygame.image.load(backImage).convert_alpha()
        self.buttons = []
        self.background = pygame.transform.scale(self.background, (1000, 650))
        self.soundBackground = soundBack
        self.soundEffect = soundEff
        self.volumeBackground = volBack
        self.volumeEffect = volEff
        
    ##Método que verifica em qual botão foi clicado
    def checkMouseOn(self, pos):
        cont = 0
        for i in self.buttons:
            posButton = i.getPos()
            sizeButton = i.getSize()
            if pos[0] <= (posButton[0] + sizeButton[0]) and pos[0] >= posButton[0]:
                if pos[1] <= (posButton[1] + sizeButton[1]) and pos[1] >= posButton[1]:
                    #print(i.getAction())
                    return cont
            cont += 1
        return -1

    def checkClick(self, pos):
        return self.checkMouseOn(pos)

    def actionButtonClicked(self, pos):
        i = self.checkMouseOn(pos)
        if i != -1:
            return self.buttons[i].getAction()
    
    def show(self):
        b = 1
        ##Método que mostra o menu na tela

    def setSoundBackground(self, sound):
        self.soundBackground = sound

    def setSoundEffect(self, sound):
        self.soundEffect = sound

    def setVolumeBackground(self, sound):
        self.volumeBackground = sound

    def setSoundEffect(self, sound):
        self.volumeEffect = sound
        
        

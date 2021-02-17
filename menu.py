import pygame
import button
## Classe Menu, que serve de base para todos os outros Menus do jogo
class Menu:
    def __init__(self, backImage = "none", soundBack = "none", soundEff = "none", volBack = 0, volEff = 0, ratioImage = 1):
        """
        @param backImage: Imagem de fundo
        @param soundBack: Som de fundo
        @param soundEfF: Som de efeito
        @param volBack: Volume do som de fundo
        @param volEff: Volume dos efeitos
        @param ratioImage: Parametro de ajuste das imagens
        """
        self.backgroundImage = pygame.image.load(backImage).convert_alpha()
        self.buttons = []
        self.background = pygame.transform.scale(self.backgroundImage, (int(1920*ratioImage), int(1080*ratioImage)))
        self.soundBackground = soundBack
        self.soundEffect = soundEff
        self.volumeBackground = volBack
        self.volumeEffect = volEff
        self.ratio = ratioImage

    def changeResolution(self, newRatio):
        self.ratio = newRatio
        self.background = pygame.transform.scale(self.backgroundImage, (int(1920*newRatio), int(1080*newRatio)))
        for i in self.buttons:
            i.changeResolution(newRatio)
        
    ##Método que verifica em qual botão foi clicado
    def checkMouseOn(self, pos):
        cont = 0
        for i in self.buttons:
            posButton = i.getPos()
            sizeButton = i.getSize()
            if pos[0] <= (posButton[0] + sizeButton[0]) and pos[0] >= posButton[0]:
                if pos[1] <= (posButton[1] + sizeButton[1]) and pos[1] >= posButton[1]:
                    return cont
            cont += 1
        return -1

    def checkClick(self, pos):
        saida = self.checkMouseOn(pos)
        return saida

    def actionButtonClicked(self, pos):
        i = self.checkClick(pos)
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

    
        
        

import menu
import button
import os
import pygame
import slider
from pygame.locals import *

class MenuConfiguration(menu.Menu):
    def __init__(self, soundBack = "none", soundEff = "none", volBack = 0, volEff = 0):
       super().__init__(os.path.join("images", "backgroundMenuConfiguration.png"), soundBack, soundEff, volBack, volEff) ##Chama a construtora da classe base

##Nesse menu, pra poupar memória, escrevemos com o pygame na tela, e carregamos apenas uma imagem trasnparente, para
##o sistema pegar o tamanho do botão etc
######################################################################################################

       font = pygame.font.Font(os.path.join("fonts", "1942.ttf") , 20)
       t1 = font.render("Main volume", True, (0, 0, 0))
       t2 = font.render("", True, (0, 0, 0))     
       t3 = font.render("Effect volume", True, (0, 0, 0))
       t4 = font.render("", True, (0, 0, 0))     
        
       
#######################################################################################################     
       self.buttons.append(button.Button(os.path.join("images", "transp.png"), (370, 160), 40, 100, "principalVolume"))
       self.buttons.append(slider.Slider((540, 165), 15, 150, 0, 100, "volumePrincipal"))

       self.buttons.append(button.Button(os.path.join("images", "transp.png"), (370, 190), 40, 100, "effectVolume"))
       self.buttons.append(slider.Slider((540, 195), 15, 150, 0, 100, "effectPrincipal"))

       
###########Utiliza essas duas listas, uma com a escrita normal, e outro com ela em vermelho
       self.texts = [t1, t2, t3, t4]

##Configuração de musica de fundo
       pygame.mixer.music.set_volume(self.volumeBackground)
       pygame.mixer.music.load(self.soundBackground)
       pygame.mixer.music.play(-1)
       print(self.soundEffect)
       self.soundOn = pygame.mixer.Sound(self.soundEffect)
       self.soundOnDone = False

    def show(self, screen, posMouse):
        ##Mostra o background
        screen.blit(self.background, (0,0))
        ##Ve onde que o mouse esta
        self.buttons[1].show(screen)
        self.buttons[3].show(screen)
        
        result = self.checkMouseOn(posMouse)
        ##Faz o efeito do mouse passando por cima
        if (result  >= 0):
            if (not self.soundOnDone):
                self.soundOn.play()
            self.soundOnDone = True
        else:
            self.soundOnDone = False

        ##Imprime os textos em preto, e salva aquele que pode ter o mouse em cima
        cont = 0
        toChangeColor = len(self.buttons)
        toPos = (0,0)
        for i in self.buttons:
            pos = i.getPos()
            screen.blit(self.texts[cont], pos)
            cont += 1
           

import menu
import button
import os
import pygame
import slider
from pygame.locals import *

class MenuConfiguration(menu.Menu):
    def __init__(self, soundBack = "none", soundEff = "none", volBack = 0, volEff = 0, ratioE = 1):
       super().__init__(os.path.join("images", "backgroundMenuConfiguration.png"), soundBack, soundEff, volBack, volEff, ratioE) ##Chama a construtora da classe base

##Nesse menu, pra poupar memória, escrevemos com o pygame na tela, e carregamos apenas uma imagem trasnparente, para
##o sistema pegar o tamanho do botão etc
######################################################################################################

       font = pygame.font.Font(os.path.join("fonts", "1942.ttf") , int(50*ratioE))
       t1 = font.render("Main volume", True, (0, 0, 0))
       t2 = font.render("", True, (0, 0, 0))     
       t3 = font.render("Effect volume", True, (0, 0, 0))
       t4 = font.render("", True, (0, 0, 0))     




       font2 = pygame.font.Font(os.path.join("fonts", "redondeta.ttf") , int(50*ratioE))
       t1Re = font2.render("Full Hd", True, (0, 0, 0))
       t2Re = font2.render("HD", True, (0, 0, 0))
       t3Re = font2.render("480p", True, (0, 0, 0))
       t4Re = font2.render("360p", True, (0, 0, 0))
       
       t1Rec = font2.render("Full Hd", True, (127, 0, 0))
       t2Rec = font2.render("HD", True, (127, 0, 0))
       t3Rec = font2.render("480p", True, (127, 0, 0))
       t4Rec = font2.render("360p", True, (127, 0, 0))

       res = font.render("Resolution", True, (0, 0, 0))
       
       ff = font2.render("Back", True, (0, 0, 0))
       ffc = font2.render("Back", True, (100, 0, 0))
#######################################################################################################     
       self.buttons.append(button.Button(os.path.join("images", "transp.png"), (370, 160), 40, 100, "principalVolume", ratioE))
       self.buttons.append(slider.Slider((540, 165), 15, 150, 0, 100, "volumePrincipal", ratioE))

       self.buttons.append(button.Button(os.path.join("images", "transp.png"), (370, 190), 40, 100, "effectVolume", ratioE))
       self.buttons.append(slider.Slider((540, 195), 15, 150, 0, 100, "effectPrincipal", ratioE))

       ##self.buttons.append(button.Button(os.path.join("images", "invasion.jpg"), (370, 500), 200, 100, "fullHd", "button", ratioE))
              
       self.buttons.append(button.Button(os.path.join("images", "transp.png"), (730, 800), 25, 250, "fullHD", "button", ratioE))
       self.buttons.append(button.Button(os.path.join("images", "transp.png"), (730, 840), 25, 250, "HD", "button", ratioE))
       self.buttons.append(button.Button(os.path.join("images", "transp.png"), (730, 880), 25, 250, "480p", "button", ratioE))
       self.buttons.append(button.Button(os.path.join("images", "transp.png"), (730, 920), 25, 250, "360p", "button", ratioE))
   
       self.buttons.append(button.Button(os.path.join("images", "transp.png"), (730, 700), 40, 100, "d", "button", ratioE))
       self.buttons.append(button.Button(os.path.join("images", "transp.png"), (900, 1020), 40, 250, "mainmenu", "button", ratioE))       
       
###########Utiliza essas duas listas, uma com a escrita normal, e outro com ela em vermelho
       self.texts = [t1, t2, t3, t4, t1Re, t2Re, t3Re, t4Re, res, ff]
       self.textsRed = [t1, t2, t3, t4, t1Rec, t2Rec, t3Rec, t4Rec, res, ffc]

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
        self.buttons[4].show(screen)
        
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
            if i == self.buttons[result] and result >= 0:
                toChangeColor = cont
                toPos = pos
            else:
                 screen.blit(self.texts[cont], pos)
            cont += 1
       ##Se o mouse estiver sobre algum botão, ele mostra a versão em vermelha
        if toChangeColor < len(self.buttons) and result >= 0:
            screen.blit(self.textsRed[toChangeColor], toPos)

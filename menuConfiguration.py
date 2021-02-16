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

       self.font = pygame.font.Font(os.path.join("fonts", "1942.ttf") , int(40*ratioE))
       t1 = self.font.render("Main volume", True, (0, 0, 0))
       t2 = self.font.render("Effect volume", True, (0, 0, 0))

       font2 = pygame.font.Font(os.path.join("fonts", "redondeta.ttf") , int(50*ratioE))

       tPlus = font2.render("+", True, (0, 0, 0))
       tMinus = font2.render("-", True, (0, 0, 0))

       tPlusRec = font2.render("+", True, (127, 0, 0))
       tMinusRec = font2.render("-", True, (127, 0, 0))

       self.volMain = self.font.render(str(100), True, (0, 0, 0))
       self.volEffect = self.font.render(str(100), True, (0, 0, 0))

       
       t1Re = font2.render("Full Hd", True, (0, 0, 0))
       t2Re = font2.render("HD", True, (0, 0, 0))
       t3Re = font2.render("480p", True, (0, 0, 0))
       t4Re = font2.render("360p", True, (0, 0, 0))
       
       t1Rec = font2.render("Full Hd", True, (127, 0, 0))
       t2Rec = font2.render("HD", True, (127, 0, 0))
       t3Rec = font2.render("480p", True, (127, 0, 0))
       t4Rec = font2.render("360p", True, (127, 0, 0))

       res = self.font.render("Resolution", True, (0, 0, 0))
       
       ff = font2.render("Back", True, (0, 0, 0))
       ffc = font2.render("Back", True, (100, 0, 0))


       
#######################################################################################################     

       self.buttons.append(button.Button(os.path.join("images", "transp.png"), (730, 200), 40, 100, "principalVolume", "button", ratioE))
       self.buttons.append(button.Button(os.path.join("images", "transp.png"), (1120, 200), 40, 40, "principalVolumeMinus", "button", ratioE))
       self.buttons.append(button.Button(os.path.join("images", "transp.png"), (1175, 200), 40, 40, "principalVolume", "button", ratioE))
       self.buttons.append(button.Button(os.path.join("images", "transp.png"), (1270, 200), 40, 40, "principalVolumePlus", "button", ratioE))
       

       self.buttons.append(button.Button(os.path.join("images", "transp.png"), (730, 250), 40, 100, "effectVolume", "button", ratioE))
       self.buttons.append(button.Button(os.path.join("images", "transp.png"), (1120, 250), 40, 40, "effectVolumeMinus", "button", ratioE))
       self.buttons.append(button.Button(os.path.join("images", "transp.png"), (1175, 250), 40, 40, "effectVolume", "button", ratioE))
       self.buttons.append(button.Button(os.path.join("images", "transp.png"), (1270, 250), 40, 40, "effectVolumePlus", "button", ratioE))

       
       self.buttons.append(button.Button(os.path.join("images", "transp.png"), (730, 800), 25, 250, "fullHD", "button", ratioE))
       self.buttons.append(button.Button(os.path.join("images", "transp.png"), (730, 840), 25, 250, "HD", "button", ratioE))
       self.buttons.append(button.Button(os.path.join("images", "transp.png"), (730, 880), 25, 250, "480p", "button", ratioE))
       self.buttons.append(button.Button(os.path.join("images", "transp.png"), (730, 920), 25, 250, "360p", "button", ratioE))
   
       self.buttons.append(button.Button(os.path.join("images", "transp.png"), (730, 700), 40, 100, "d", "button", ratioE))
       self.buttons.append(button.Button(os.path.join("images", "transp.png"), (900, 1020), 40, 250, "mainmenu", "button", ratioE))       
       
###########Utiliza essas duas listas, uma com a escrita normal, e outro com ela em vermelho
       self.texts = [t1, tMinus, self.volMain, tPlus, t2, tMinus, self.volEffect, tPlus, t1Re, t2Re, t3Re, t4Re, res, ff]
       self.textsRed = [t1, tMinusRec, self.volMain, tPlusRec,t2, tMinusRec, self.volEffect, tPlusRec, t1Rec, t2Rec, t3Rec, t4Rec, res, ffc]



##Configuração de musica de fundo
       pygame.mixer.music.set_volume(self.volumeBackground)
       pygame.mixer.music.load(self.soundBackground)
       pygame.mixer.music.play(-1)
       print(self.soundEffect)
       self.soundOn = pygame.mixer.Sound(self.soundEffect)
       self.soundOnDone = False


     
     

        
    def uptadteMainVol(self, newVol):        
        self.volMain = self.font.render(str(newVol), True, (0, 0, 0))
        self.texts[2] = self.volMain
        self.textsRed[2] = self.volMain
    
    def uptadteEffectVol(self, newVol):
        self.volEffect = self.font.render(str(newVol), True, (0, 0, 0))
        self.texts[6] = self.volEffect
        self.textsRed[6] = self.volEffect
        
    def show(self, screen, posMouse):
        
        ##Mostra o background
        screen.blit(self.background, (0,0))
        ##Ve onde que o mouse esta
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


        

import menu
import button
import os
import pygame

class MenuPause(menu.Menu):
    def __init__(self, background = "none", soundBack = "none", soundEff = "none", volBack = 0, volEff = 0, ratioE = 1):
       super().__init__(background, soundBack, soundEff, volBack, volEff, ratioE) ##Chama a construtora da classe base

       self.ratio = ratioE
##Nesse menu, pra poupar memória, escrevemos com o pygame na tela, e carregamos apenas uma imagem trasnparente, para
##o sistema pegar o tamanho do botão etc
######################################################################################################

       font = pygame.font.Font(os.path.join("fonts", "ARMY_RUST.ttf") , int(80*ratioE))
       t1 = font.render("Resume", True, (0, 0, 0))
       t2 = font.render("Configuration", True, (0, 0, 0))
       t3 = font.render("Main menu", True, (0, 0, 0))
       t4 = font.render("Exit", True, (0, 0, 0))

       t1r = font.render("Resume", True, (127, 0, 0))
       t2r = font.render("Configuration", True, (127, 0, 0))
       t3r = font.render("Main menu", True, (127, 0, 0))
       t4r = font.render("Exit", True, (127, 0, 0))
       
       
#######################################################################################################     
       self.buttons.append(button.Button(os.path.join("images", "transp.png"), (900, 290), 40, 250, "resume", "button", ratioE))
       self.buttons.append(button.Button(os.path.join("images", "transp.png"), (900, 380), 40, 250, "configuration", "button", ratioE))
       self.buttons.append(button.Button(os.path.join("images", "transp.png"), (900, 470), 40, 250, "mainmenu", "button", ratioE))
       self.buttons.append(button.Button(os.path.join("images", "transp.png"), (900, 560), 40, 250, "exit", "button", ratioE))
       
###########Utiliza essas duas listas, uma com a escrita normal, e outro com ela em vermelho
       self.texts = [t1, t2, t3, t4]
       self.textsRed = [t1r, t2r, t3r, t4r]

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
    
    def changeResolution2(self, newRatio):
       font = pygame.font.Font(os.path.join("fonts", "ARMY_RUST.ttf") , int(80*newRatio))

       t1 = font.render("Resume", True, (0, 0, 0))
       t2 = font.render("Configuration", True, (0, 0, 0))
       t3 = font.render("Main menu", True, (0, 0, 0))
       t4 = font.render("Exit", True, (0, 0, 0))

       t1r = font.render("Resume", True, (127, 0, 0))
       t2r = font.render("Configuration", True, (127, 0, 0))
       t3r = font.render("Main menu", True, (127, 0, 0))
       t4r = font.render("Exit", True, (127, 0, 0))
       self.ratio = newRatio
       ###########Utiliza essas duas listas, uma com a escrita normal, e outro com ela em vermelho
       self.texts = [t1, t2, t3, t4]
       self.textsRed = [t1r, t2r, t3r, t4r]
        

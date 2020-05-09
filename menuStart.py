import menu
import button
import os
import pygame

class MenuStart(menu.Menu):
    def __init__(self, backImage = "none", soundBack = "none", soundEff = "none", volBack = 0, volEff = 0, ratioE = 1):
        super().__init__(backImage, soundBack, soundEff, volBack, volEff, ratioE) ##Chama a construtora da classe base
        self.ratio = ratioE
        ##Salva os botões utilizados


        self.buttons.append(button.Button(os.path.join("images", "StartMenu", "globo.png"), (850, 550), 410, 380, "newgame", "button", ratioE))
        self.buttons.append(button.Button(os.path.join("images", "StartMenu", "janela.png"), (0, 180), 520, 140, "exit", "button", ratioE))
        self.buttons.append(button.Button(os.path.join("images", "StartMenu", "livros.png"), (244, 780), 156, 360, "results", "button", ratioE))
       

        ##self.buttons.append(button.Button(os.path.join("images", "StartMenu", "globo.png"), (410, 290), 210, 190, "newgame"))
        ##self.buttons.append(button.Button(os.path.join("images", "StartMenu", "janela.png"), (0, 90), 260, 70, "newgame"))
        ##self.buttons.append(button.Button(os.path.join("images", "StartMenu", "livros.png"), (122, 390), 78, 180, "newgame"))
       
        ##Configurações da musica de fundo
        pygame.mixer.music.set_volume(self.volumeBackground)
        pygame.mixer.music.load(os.path.join("sounds", "startMenuGame.mp3"))
        pygame.mixer.music.play(-1)
        self.soundOn = pygame.mixer.Sound(os.path.join("sounds", "mousePass.ogg"))
        self.soundOnDone = False

    def show(self, screen, posMouse):
        ##Pelo estilo do menu, ele não mostra os botões
        ##Porém, quando o mouse passa por cima de algum dele, ai sim eles aparecem
        screen.blit(self.background, (0,0))
        result = self.checkMouseOn(posMouse)
        ##Verifica se o mouse esta sobre algum botão, se estiver, ai mostra ele, e ativa o efeito do som passando
        if (result  >= 0):
            self.buttons[result].show(screen)
            if (not self.soundOnDone):
                self.soundOn.play()
            self.soundOnDone = True
        else:
            self.soundOnDone = False

   

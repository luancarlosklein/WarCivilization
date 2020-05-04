import menu
import button
import os
import pygame

class MenuStart(menu.Menu):
    def __init__(self, backImage = "none", soundBack = "none", soundEff = "none", volBack = 0, volEff = 0):
        super().__init__(os.path.join("images", "startMenuBack.jpg"), soundBack, soundEff, volBack, volEff) ##Chama a construtora da classe base
        ##Salva os botões utilizados
        self.buttons.append(button.Button(os.path.join("images", "btgMachone.png"), (450, 420), 130, 390, "Play"))
        self.buttons.append(button.Button(os.path.join("images", "buttonPicture.png"), (479, 100), 300, 300, "See best results"))
        self.buttons.append(button.Button(os.path.join("images", "buttonDoor.png"), (0, 100), 475, 100, "Exit"))
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

   

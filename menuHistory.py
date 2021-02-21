import menu
import button
import os
import pygame

class MenuHistory(menu.Menu):
    def __init__(self, backImage = "none", soundBack = "none", soundEff = "none", volBack = 0, volEff = 0, ratioE = 1):
        super().__init__(backImage, soundBack, soundEff, volBack, volEff, ratioE) ##Chama a construtora da classe base
        self.ratio = ratioE
        ##Salva os botões utilizados

        self.screen = pygame.display.get_surface()
        self.buttons.append(button.Button(os.path.join("images", "bookEgypt.png"), (1450, 112), 968, 170, "Egypt", "button", ratioE))
        
        self.egypt = pygame.image.load(os.path.join("images", "historyEgypt.png")).convert_alpha()
        self.egypt = pygame.transform.scale(self.egypt,(int(1920* self.ratio), int(1080 * self.ratio)))
      

        self.showing = -1
        ##Configurações da musica de fundo
        pygame.mixer.music.set_volume(self.volumeBackground)
        pygame.mixer.music.load(os.path.join("sounds", "startMenuGame.mp3"))
        pygame.mixer.music.play(-1)
        self.soundOn = pygame.mixer.Sound(os.path.join("sounds", "mousePass.ogg"))
        self.soundOnDone = False

    def show(self, screen, posMouse):
        
        if self.showing == -1:
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
            
        elif self.showing == "Egypt":
            
            screen.blit(self.egypt,(int(0*self.ratio),int(0* self.ratio)))
            pygame.display.flip()
            pygame.display.update()
          

    def checkClick(self, pos):
        saida = self.checkMouseOn(pos)
        if saida == "back":
            self.showing == -1
            return saida
        else:
            if self.showing == -1:
                self.showing = self.buttons[saida].getAction()
            return "history"

    def actionButtonClicked(self, pos):
        i = self.checkClick(pos)
        if i == "history":
            return "history"
        if i != -1:
            return self.buttons[i].getAction()

   

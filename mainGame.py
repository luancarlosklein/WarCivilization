import pygame, time, math, os
from random import *
from pygame.locals import *
import button
import menuStart
from menuStart import MenuStart

from menuPause import MenuPause

from inGameMenu import InGameMenu

from gameManager import GameManager


from menuFinal import MenuFinal


from menuConfiguration import MenuConfiguration

class MainGame:
    def __init__(self):

        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,30)

        self.initialRatio = 0.5
        self.currentRatio = self.initialRatio 
        self.height = int (1080 * self.initialRatio)
        self.width = int(1920 * self.initialRatio)
        pygame.init() ##Inicia os mï¿½dulos do PYGAME
        self.window = pygame.display.set_mode((self.width, self.height)) ##Cria uma tela.. X e Y
        #self.window = pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN)

        pygame.display.set_caption("War")##Nomeia a Janela
        #pygame.display.toggle_fullscreen()


        self.screen = pygame.display.get_surface()
        self.color_white = (255, 255, 255)

        self.window.get_rect().topleft = (0,0)

        self.window.fill(self.color_white)
        pygame.display.flip()
        pygame.display.update()

        self.startMenu = MenuStart(os.path.join("images", "StartMenu","game_room.jpg"), os.path.join("sounds", "startMenuGame.mp3"), os.path.join("sounds", "mousePass.ogg"), 1, 1, self.initialRatio)
        self.pauseMenu = MenuPause(os.path.join("images", "backgroundMenuPause.png"), os.path.join("sounds", "startMenuGame.mp3"), os.path.join("sounds", "mousePass.ogg"), 1, 1, self.initialRatio)

        self.finalMenu = MenuFinal(os.path.join("images", "inglesias.jpg"), os.path.join("sounds", "startMenuGame.mp3"), os.path.join("sounds", "mousePass.ogg"), 1, 1, self.initialRatio)
        
        self.game = GameManager (1, self.screen)
        
        self.configurationMenu = MenuConfiguration(os.path.join("sounds", "startMenuGame.mp3"), os.path.join("sounds", "mousePass.ogg"), 0, 0, self.initialRatio)
        self.game = GameManager (2, self.screen)

        self.pages = [self.startMenu, self.game, self.pauseMenu, self.configurationMenu, self.finalMenu]
        self.action = None
        self.activeNow = 0
        self.stop = False

    def execute(self):

        while not self.stop:
            pygame.display.flip()
            pygame.display.update()
            for event in pygame.event.get():  
                if self.activeNow != 1:
                
                    if event.type == pygame.MOUSEBUTTONDOWN or pygame.mouse.get_pressed()[0] != 0:##Verifica o clique do mouse
                        print(pygame.mouse.get_pos())
                        self.action = self.pages[self.activeNow].actionButtonClicked(pygame.mouse.get_pos())
                        print(self.action)
                    self.pages[self.activeNow].show(self.screen, pygame.mouse.get_pos())

            changeReso = False
            if self.action == "newgame":
                self.activeNow = 1
                self.window.fill(self.color_white)
                self.action = self.game.gameLoop()
             
            elif self.action == "resume":
                self.activeNow = 1
                self.window.fill(self.color_white)
                self.action = self.game.gameLoop()

            elif self.action == "exit":
                pygame.quit()
                self.stop = True

            elif self.action == "configuration":
                self.activeNow = 3

            elif self.action == "pause":
                self.activeNow = 2

            ######PRA MUDAR A IMAGEM DO FUNDO FINAL EH AQUI
            elif self.action == "final":
                self.activeNow = 4
                ##REINICIA A POSICAO 4, CRIANDO ELA DENOVO
                ##MenuFinal(os.path.join("images", "StartMenu","game_room.jpg"), os.path.join("sounds", "startMenuGame.mp3"), os.path.join("sounds", "mousePass.ogg"), 1, 1, self.initialRatio)
                
            elif self.action == "mainmenu":
                self.activeNow = 0

            elif self.action == "fullHD":
                self.currentRatio = 1
                changeReso = True
            elif self.action == "HD":
                self.currentRatio = 1290/1980
                changeReso = True
            elif self.action == "480p":
                self.currentRatio = 854/1980
                changeReso = True
            elif self.action == "360p":
                self.currentRatio = 640/1980
                changeReso = True
            elif self.action == "240p":
                self.currentRatio = 426/1980
                changeReso = True

            if changeReso == True:
                changeReso = False
                for i in self.pages:
                    i.changeResolution(self.currentRatio)
                self.height = int (int(1080 * self.currentRatio))
                self.width = int( int(1920 * self.currentRatio))
                self.window = pygame.display.set_mode((self.width, self.height)) 
                pygame.display.flip()
                pygame.display.update()
                self.pages[self.activeNow].show(self.screen, pygame.mouse.get_pos())
                self.action = "none"

            if event.type == pygame.QUIT: ## Verifica se o usuario clicou no X vermelho para fechar
                pygame.quit()
                self.stop = True


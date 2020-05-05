import pygame, time, math, os
from random import *
from pygame.locals import *
import button
import menuStart
from menuStart import MenuStart

from menuPause import MenuPause

from inGameMenu import InGameMenu

from gameManager import GameManager

class MainGame:
    def __init__(self):
        

        self.heigth = 650
        self.width = 1000

        pygame.init() ##Inicia os mï¿½dulos do PYGAME
        self.window = pygame.display.set_mode((self.width, self.heigth)) ##Cria uma tela.. X e Y
        pygame.display.set_caption("War")##Nomeia a Janela

        self.screen = pygame.display.get_surface()
        self.color_white = (255, 255, 255)

        self.window.fill(self.color_white)
        pygame.display.flip()
        pygame.display.update()
        
        self.startMenu = MenuStart(os.path.join("sounds", "startMenuGame.mp3"), os.path.join("sounds", "mousePass.ogg"), 1, 1)
        self.pauseMenu = MenuPause(os.path.join("sounds", "startMenuGame.mp3"), os.path.join("sounds", "mousePass.ogg"), 1, 1)
        self.game = GameManager (1, self.screen)
        self.pages = [self.startMenu, self.game, self.pauseMenu]
        self.action = None
        self.activeNow = 0
        self.stop = False

    def execute(self):

        while not self.stop:
            pygame.display.flip()
            pygame.display.update()
            for event in pygame.event.get():  
                if self.activeNow != 1:
                    self.pages[self.activeNow].show(self.screen, pygame.mouse.get_pos())
                    if event.type == pygame.MOUSEBUTTONDOWN:##Verifica o clique do mouse
                        self.action = self.pages[self.activeNow].actionButtonClicked(pygame.mouse.get_pos())
                        
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

            elif self.action == "pause":
                self.activeNow = 2

            elif self.action == "mainmenu":
                self.activeNow = 0

            if event.type == pygame.QUIT: ## Verifica se o usuario clicou no X vermelho para fechar
                pygame.quit()
                self.stop = True

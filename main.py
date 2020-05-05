# -*- coding: cp1252 -*-
import pygame, time, math, os
from random import *
from pygame.locals import *
import button
import menuStart
from menuStart import MenuStart

from menuPause import MenuPause

from inGameMenu import InGameMenu

from gameManager import GameManager

##Defini��es iniciais do pygame#############
heigth = 650
width = 1000

pygame.init() ##Inicia os m�dulos do PYGAME
window = pygame.display.set_mode((width, heigth)) ##Cria uma tela.. X e Y
pygame.display.set_caption("War")##Nomeia a Janela
screen = pygame.display.get_surface()
color_white = (255, 255, 255)
window.fill(color_white)
pygame.display.flip()
pygame.display.update()
######################################################

stop = False
startMenu = MenuStart(os.path.join("sounds", "startMenuGame.mp3"), os.path.join("sounds", "mousePass.ogg"), 0, 1)
pauseMenu = MenuPause(os.path.join("sounds", "startMenuGame.mp3"), os.path.join("sounds", "mousePass.ogg"), 0, 1)
game = GameManager (1, screen)

pages = [startMenu, game, pauseMenu]
activeNow = 0

###Loop principal do game ###################################
while True:
   
   pygame.display.flip()
   pygame.display.update()
   for event in pygame.event.get():
        click = -1
        
        ##Verifica se n�o ta no game, no caso de resumo etc. O game n�o tem um show!
        if activeNow != 1:
           gameReturn = -1
           pages[activeNow].show(screen, pygame.mouse.get_pos())
    
           if event.type == pygame.MOUSEBUTTONDOWN:##Verifica o clique do mouse
               click = pages[activeNow].checkClick(pygame.mouse.get_pos())
               #print("POSITION:", pygame.mouse.get_pos())
 
    
        ## Est� no menuStart e foi clicado o foi clicado na porta para sair
        if activeNow == 0 and click == 2:
            pygame.quit()
            stop = True

       ## Est� no menuStart e foi clicado o bot�o de play
        elif activeNow == 0 and click == 0:
           activeNow = 1
           window.fill(color_white)
           gameReturn = game.gameLoop()


        ##Est� no jogo e foi dado esc
        elif activeNow == 1 and gameReturn == 55:
           print("PAUSEEE")
           activeNow = 2

        ##Est� no menu pause e foi clicado no bot�o exit
        elif activeNow == 2 and click == 3:
           pygame.quit()
           stop = True

        ##Est� no menu pause e foi clicado no bot�o main game
        elif activeNow == 2 and click == 2:
           activeNow = 0

        ##Est� no menu pause e foi clicado no bot�o resume
        elif activeNow == 2 and click == 0:
           print("RESUMEEE")
           activeNow = 1
           window.fill(color_white)
           gameReturn = game.gameLoop()


        if event.type == pygame.QUIT: ## Verifica se o usuario clicou no X vermelho para fechar
            pygame.quit()
            stop = True

   time.sleep(0.03)
   if stop:
      break
####################################################################

# -*- coding: cp1252 -*-
import pygame, time, math, os
from random import *
from pygame.locals import *
import button
import menuStart
from menuStart import MenuStart

from menuPause import MenuPause

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
startMenu = MenuPause()


###Loop principal do game ###################################
while True:
   
   pygame.display.flip()
   pygame.display.update()
   for event in pygame.event.get():
        startMenu.show(screen, pygame.mouse.get_pos())
        if event.type == pygame.MOUSEBUTTONDOWN:##Verifica o clique do mouse
            startMenu.checkClick(pygame.mouse.get_pos())
            #print("POSITION:", pygame.mouse.get_pos())

        ##Verifica se o usuario apertou a tecla Q 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()##Fecha a tela pygame
                stop = True 
        if event.type == pygame.QUIT: ## Verifica se o usuario clicou no X vermelho para fechar
            pygame.quit()
            stop = True

   if stop:
      break
####################################################################

import pygame
import menu
import button
import os

## Classe Utilizada para definir a escolha do exercito do usuario
class PlayerInfoSelector(menu.Menu):
   def __init__(self, backImage = "none", soundBack = "none", soundEff = "none", volBack = 0, volEff = 0, ratioE = 1):
      ## Inicia a classe Pai, que e Menu
      super().__init__(os.path.join("images", "selectionMenu", "backgroundChosenOne.png"), soundBack, soundEff, volBack, volEff, ratioE)

      ## Adiciona todos os botoes na tela
      ## As posicoes foram colocadas com valores constantes visando a melhor adaptacao visual
      self.buttons.append(button.Button(os.path.join("images", "selectionMenu", "civilizations", "Greece.png"), (110, 525), 142, 94, "Greece", "button", ratioE))
      self.buttons.append(button.Button(os.path.join("images", "selectionMenu", "civilizations", "Egypt.png"), (885, 220), 190, 134, "Egypt", "button", ratioE))
      self.buttons.append(button.Button(os.path.join("images", "selectionMenu", "civilizations", "Brazil.png"), (100, 100), 87, 130, "Brazil", "button", ratioE))
      self.buttons.append(button.Button(os.path.join("images", "selectionMenu", "civilizations", "France.png"), (370,135), 360, 308, "France", "button", ratioE))
      self.buttons.append(button.Button(os.path.join("images", "selectionMenu", "civilizations", "Cuba.png"), (317, 530), 101, 86, "Cuba", "button", ratioE))
      self.buttons.append(button.Button(os.path.join("images", "selectionMenu", "civilizations", "China.png"), (1650, 650), 130, 195, "China", "button", ratioE))
      self.buttons.append(button.Button(os.path.join("images", "selectionMenu", "civilizations", "Portugal.png"), (1725, 510), 143, 66, "Portugal", "button", ratioE))
      self.buttons.append(button.Button(os.path.join("images", "selectionMenu", "civilizations", "Pirates.png"), (770, 520), 280, 342, "Pirates", "button", ratioE))
      self.buttons.append(button.Button(os.path.join("images", "selectionMenu", "civilizations", "Spain.png"), (1330, 560), 413, 344, "Spain", "button", ratioE))
      self.buttons.append(button.Button(os.path.join("images", "selectionMenu", "civilizations", "Mongolia.png"), (1550, 480), 149, 131, "Mongolia", "button", ratioE))
      self.buttons.append(button.Button(os.path.join("images", "selectionMenu", "civilizations", "SovietUnion.png"), (1560, 400), 121, 83, "Soviet Union", "button", ratioE))
      self.buttons.append(button.Button(os.path.join("images", "selectionMenu", "civilizations", "GreatBritain.png"), (240, 370), 134, 116, "Great Britain", "button", ratioE))
      self.buttons.append(button.Button(os.path.join("images", "selectionMenu", "civilizations", "India.png"), (260, 630), 117, 130, "India", "button", ratioE))
      self.buttons.append(button.Button(os.path.join("images", "selectionMenu", "civilizations", "USA.png"), (1550, 10), 248, 422, "USA", "button", ratioE))
      self.buttons.append(button.Button(os.path.join("images", "selectionMenu", "civilizations", "Japan.png"), (600, 145), 101, 740, "Japan", "button", ratioE))
      self.buttons.append(button.Button(os.path.join("images", "selectionMenu", "civilizations", "Italy.png"), (1070, 175), 754, 469, "Italy", "button", ratioE))

      ##Configurações da musica de fundo
      pygame.mixer.music.set_volume(self.volumeBackground)
      pygame.mixer.music.load(os.path.join("sounds", "startMenuGame.mp3"))
      pygame.mixer.music.play(-1)
      self.soundOn = pygame.mixer.Sound(os.path.join("sounds", "mousePass.ogg"))
      self.soundOnDone = False

   ## Metodo que define como e mostrado na tela
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

   ## Metodo que executa a escolha do exercito
   def defineFlag(self):
      ## Pega a instancia do pygame
      screen = pygame.display.get_surface()
      pygame.display.update()
      ## Variavel que controla se algum ja foi selecionado
      selected = False
      ## Enquanto nao estiver selecionado, continua executando
      while not selected:
         ## Mostra todos os objetos
         self.show(screen, pygame.mouse.get_pos())
         ## Verifica os eventos que acontecem
         for event in pygame.event.get():
            ## Verifica se ocorreu um evento de clique de mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
               ## Verifica se algum botao foi clicado
               objCliked = self.checkClick(pygame.mouse.get_pos())
               ## Se sim, encerra o loop
               if objCliked != -1:
                  selected = True
         
         pygame.display.update()
      ## Retorna o nome do objeto clicado
      return self.buttons[objCliked].getAction()




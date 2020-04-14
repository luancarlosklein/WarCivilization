import menu
import button
import os


class MenuFinal(menu.Menu):
    def __init__(self):
        super().__init__(os.path.join("images", "inglesias.jpg")) ##Chama a construtora da classe base
        self.buttons.append(button.Button(os.path.join("images", "inglesias.jpg"), (10, 10), 50, 201, "LUTARRR CARAI"))
        self.buttons.append(button.Button(os.path.join("images", "start.jpg"), (100, 240), 190, 508, "LEIRRAY GOLLLLL"))

    def show(self, screen):
        for i in self.buttons:
            i.show(screen)
    

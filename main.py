from PyQt6.QtWidgets import QApplication, QStackedWidget

from menu import Menu
from game import Game


class MainApp(QStackedWidget): # on utilise un QstackedWidget car permet de stocker des vues et ainsi pouvoir alterner d'écrans
    def __init__(self):
        super().__init__()

        # creation du menu
        self.menu = Menu(self.start_game)
        self.addWidget(self.menu)

        # de base aucune partie n'est créée tant qu'on a pas cliqué sur jouer
        self.game = None



    def start_game(self): # fonction appelée en callback lors du click sur le bouton jouer
        if self.game != None: # si une partie existe déjà on la supprime
            self.removeWidget(self.game) # on retire le widget
            self.game.deleteLater() # on le supprime

        # creation d'une nouvelle partie
        self.game = Game(self.back_to_menu)
        self.addWidget(self.game)
        self.setCurrentWidget(self.game) #affichage du jeu



    def back_to_menu(self): # fonction appelée en callback lors du click sur le bouton retour menu
        self.setCurrentWidget(self.menu) #affichage du menu



if __name__ == "__main__":
    app = QApplication([])
    window = MainApp()
    window.show()
    app.exec()
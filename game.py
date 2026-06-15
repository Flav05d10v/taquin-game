from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QGridLayout, QSizePolicy, QFrame
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QIcon
import random
from move import Move
from découpe import Decouper


class Game(QWidget):
    def __init__(self, back_callback):
        super().__init__()

        self.back_callback = back_callback

        #  choix aléatoire image
        self.image_choisie = random.choice(["bal_du_moulin","marat","vinci","tournesols","radeau_meduse","persistance_de_la_mémoire","ménines","mort_de_socrate","la_classe_de_danse","jeune_fille_a_la_perle","impression_soleil_levant","grande_vague","femmes_de_tahiti","epoux_arnolfini","enlevement_sabines","ecole_athenes","déjeuner_sur_l'herbe","déjeuner_des_canotiers","desespere"])

        self.decoupe = Decouper('./images/' + self.image_choisie + '.jpg',400)

        # layout principal
        self.main_layout = QVBoxLayout()

        # grille
        self.grille = QGridLayout()
        self.grille.setSpacing(0)
        self.grille.setContentsMargins(0, 0, 0, 0)

        self.taille_case = 120

        # on melange la grille
        self.etat = [1,2,3,4,5,6,7,8,None]
        while True: # tant qu'on a pas un mélange de taquin valide on continue de mélanger
            random.shuffle(self.etat)
            if self.est_resoluble(self.etat) and self.etat != [1,2,3,4,5,6,7,8,None]: # on verifie si le taquin est resoluble et si on a pas la solution directements
                break

        # création de la grille
        self.init_grille()

          # bouton retour
        self.bouton_retour = QPushButton("Retour menu")
        self.bouton_retour.setStyleSheet("""
            QPushButton {
                font-size: 20px;
                font-family: Times New Roman, sans-serif;
                background-color: #EDC9AF;
                color: black;
                border-radius: 5px;
                padding: 10px;
                border: none;
            }
            QPushButton:hover {
                background-color: #C19A6B;
                color: white;
            }""")
        self.bouton_retour.clicked.connect(self.back_callback)

        cadre = QFrame()
        cadre.setObjectName("cadre")

        cadre.setStyleSheet("""
            QFrame#cadre {
                border-image: url(images/cadre_dore.png);
            }
        """)
        # layout interne du cadre
        cadre_layout = QVBoxLayout()
        cadre_layout.setContentsMargins(40, 40, 40, 40)

        # container de grille
        container = QWidget()
        container.setLayout(self.grille)
        container.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        cadre_layout.addWidget(container, alignment=Qt.AlignmentFlag.AlignCenter)

        cadre.setLayout(cadre_layout)


        # ajout au layout
        self.main_layout.addWidget(cadre, alignment=Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addWidget(self.bouton_retour, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(self.main_layout)

        # background de la fenetre de la partie
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True) # on précise que le fond de ce widget sera créer avec une feuille de style
        self.setObjectName("main")
        self.setStyleSheet("""
            QWidget#main {
                border-image: url(./images/mur.jpg) 0 0 0 0 stretch stretch;
                background-position: center;
                background-repeat: no-repeat;
            }
        """)


    def init_grille(self):
        index = 0
        for ligne in range(3):
            for colonne in range(3):

                valeur = self.etat[index]

                bouton = Move(valeur, index, self)
                bouton.setFixedSize(self.taille_case, self.taille_case)

                if valeur is None:
                    bouton.setStyleSheet("background-color: #C19A6B; border-radius: 5px")
                else:
                    chemin = f"./images/{self.image_choisie}_{valeur}.png"
                    bouton.setIcon(QIcon(chemin))
                    bouton.setIconSize(QSize(self.taille_case, self.taille_case))
                    

                self.grille.addWidget(bouton, ligne, colonne)

                index += 1


    def mettre_a_jour(self):

        # supprimer anciens boutons
        for i in reversed(range(self.grille.count())): #on les supprime du dernier au premier pour éviter que l'index se décale

            widget = self.grille.itemAt(i).widget() #récupère le i-ième élément du layout

            if widget:
                widget.deleteLater() #permet de supprimer proprement le widget quand qt aura fini sa vie

        self.init_grille()
    

    def est_resoluble(self, etat): # un taquin 3x3 est resoluble si le nombre d'inversions est pair sinon impossible à résoudre
        valeurs = []
        # on retire la case vide
        for elt in etat:
            if elt != None:
                valeurs.append(elt)

        inversions = 0

        for i in range(len(valeurs)):
            for j in range(i + 1, len(valeurs)):
                if valeurs[i] > valeurs[j]:
                    inversions = inversions + 1
        if inversions % 2 == 0: # on regarde si le nombre d'inversions est pair
            return True
        return False
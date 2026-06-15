from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt6.QtCore import Qt, QSize

class Menu(QWidget): #fenêtre personalisée de menu qui hérite de Qwidget
    def __init__(self, start_callback): #fonction appelée quand on clique sur jouer
        super().__init__()

        self.start_callback = start_callback

        self.setWindowTitle("Taquin")
        self.setFixedSize(QSize(980, 620)) #taille fenetre pas modifiable

        # le fond de la fentre
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True) # on précise que le fond de ce widget sera créer avec une feuille de style
        self.setObjectName("main")
        self.setStyleSheet("""
            QWidget#main {
                border-image: url(./images/fond.jpg) 0 0 0 0 stretch stretch;
                background-position: center;
                background-repeat: no-repeat;
            }
            QPushButton {
                color: white;
            }
        """)

        # le layout du menu
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # creation du conteneur pour y mettre les widgets et pouvoir appliquer un CSS commun uniquement à ces widgets là
        container = QWidget()
        container_layout = QVBoxLayout()
        container_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        container.setLayout(container_layout)

        # feuille de style pour le conteneur
        container.setStyleSheet("""
            background-color: rgba(0, 0, 0, 150);
            border-radius: 20px;
            padding: 15px;
        """)

        # creation du texte
        self.label = QLabel("Jeu du Taquin")
        self.label.setStyleSheet("font-size: 35px; color: #C19A6B; font-family: Times New Roman, sans-serif;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # creation du bouton jouer
        self.button = QPushButton("Jouer")
        self.button.setFixedSize(200, 60)
        self.button.setStyleSheet("""
            QPushButton {
                font-size: 30px;
                font-family: Times New Roman, sans-serif;
                background-color: #EDC9AF;
                color: black;
                border-radius: 10px;
                border: none;
            }
            QPushButton:hover {
                background-color: #C19A6B;
                color: white;
            }
        """)

        self.button.clicked.connect(self.start_callback) # appel du callback pour changer de vue lorsque l'on clique sur le bouton


        # on ajoute au conteneur nos widgets
        container_layout.addWidget(self.label)
        container_layout.addWidget(self.button, alignment=Qt.AlignmentFlag.AlignCenter) # on aligne le bouton au centre du conteneur

        # on met le conteneur dans la fenetre
        layout.addWidget(container)

        # on ajoute le layout sur notre fenetre
        self.setLayout(layout)



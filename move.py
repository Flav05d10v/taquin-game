from PyQt6.QtWidgets import QPushButton

class Move(QPushButton):
    def __init__(self,valeur,index,grille):
        super().__init__()

        self.valeur = valeur
        self.index = index
        self.grille = grille

        self.clicked.connect(self.deplacer)

    def deplacer(self):

        vide = self.grille.etat.index(None) # position de la case vide

        voisin = False #on part du principe que la case n'est pas a côté de la case vide
        double = False #on part du principe que le deplacement n'est pas double au départ 

        # deplacements simples
        # gauche
        if self.index - 1 == vide and self.index % 3 != 0: #si la case à gauche est le vide et qu'on est pas sur le bord gauche
            voisin = True
        # droite
        elif self.index + 1 == vide and self.index % 3 != 2: #si la case de droite est le vide est qu'on est pas sur le bord droit
            voisin = True
        # haut
        elif self.index - 3 == vide:
            voisin = True
        # bas
        elif self.index + 3 == vide:
            voisin = True


        # deplacements doubles
        #verification
        if not((self.index//3) == (vide//3) or (self.index%3) == (vide%3)): #on regarde si on se deplace bien sur la meme ligne et meme colonne
            return
        #gauche
        if self.index - 2 == vide and self.index % 3 != 0:
            voisin = True
            double = True
        #droite
        elif self.index + 2 == vide and self.index % 3 != 2:
            voisin = True
            double = True
        #haut
        elif self.index - 6 == vide:
            voisin = True
            double = True
        #bas
        elif self.index + 6 == vide:
            voisin = True
            double = True

        # échange des cases
        if voisin:
            if double:
                # on defini la case entre le vide et la case sur laquelle on clique
                if self.index - 2 == vide:
                    mid = self.index - 1

                elif self.index + 2 == vide:
                    mid = self.index + 1

                elif self.index - 6 == vide:
                    mid = self.index - 3

                elif self.index + 6 == vide:
                    mid = self.index + 3

                # on decale une par une les cases
                self.grille.etat[vide] = self.grille.etat[mid]
                self.grille.etat[mid] = self.valeur
                self.grille.etat[self.index] = None

            else:
                self.grille.etat[vide] = self.valeur
                self.grille.etat[self.index] = None

            # on remet l'affichage à jour
            self.grille.mettre_a_jour()

            # victoire
            if self.grille.etat == [1, 2, 3, 4, 5, 6, 7, 8, None]:
                self.grille.etat[8] = 9 # on remplace la case None par sa valeur d'origine pour pouvoir afficher l'image correspondante lors de l'appel de la fonction init_grille

                self.grille.mettre_a_jour() # on met à jour le changement de grille

                self.grille.bouton_retour.setText("Bravo vous avez gagné !")

                return
            

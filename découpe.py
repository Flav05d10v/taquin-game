from PIL import Image

class Decouper():
    def __init__(self, nom_image,taille_carre):
        self.nom_image = nom_image
        self.taille_carre = taille_carre

        image=Image.open(self.nom_image) #on ouvre l'image
        new_name = self.nom_image.split('/')[2]
        largeur,hauteur = image.size #on va récupérer les dims de notre image

    #on veut calculer les coordonnées de notre carré que l'on va faire centré sur l'image
        gauche = (largeur - self.taille_carre) // 2
        haut = (hauteur - self.taille_carre) // 2
        droite = gauche + self.taille_carre
        bas = haut + self.taille_carre

        carre = image.crop((gauche, haut, droite, bas)) #crop elle sert a decouper une region rectangulaire a partir dune image

        taille_case = self.taille_carre // 3 #comme on fait un taquin en 3x3 la dimension des petits carrés et 3 fois plus petite que celle du grand

        compteur = 1 #le compteur va servir a nommer les cases

        # Double boucle pour parcourir les 3 lignes et 3 colonnes
        for ligne in range(3):  # 0, 1, 2
            for colonne in range(3):
                x1 = colonne * taille_case # Coordonnées de chaque petit carré
                y1 = ligne * taille_case
                x2 = x1 + taille_case
                y2 = y1 + taille_case

                morceau = carre.crop((x1, y1, x2, y2)) # On découpe le morceau correspondant

                nom_fichier = f"./images/{new_name.split('.')[0]}_{compteur}.png"# Créer le nom du fichier (ex: joconde1.png) si le fichier d'origine s'appelle joconde
                morceau.save(nom_fichier)  # Sauvegarder l’image

                compteur += 1  # On passe au numéro suivant image en haut à gauche sera la 1 puis celle de droite la 2 et ainsi de suite



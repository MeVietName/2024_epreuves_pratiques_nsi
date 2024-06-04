class Carte:
    def __init__(self, c, v):
        """Initialise les attributs couleur (entre 1 et 4), 
        et valeur (entre 1 et 13). """
        self.couleur = c
        self.valeur = v

    def recuperer_valeur(self):
        """ Renvoie la valeur de la carte : 
        As, 2, ..., 10, Valet, Dame, Roi """
        valeurs = ['As','2', '3', '4', '5', '6', '7', '8', 
                   '9', '10', 'Valet', 'Dame', 'Roi']
        return valeurs[self.valeur - 1]

    def recuperer_couleur(self):
        """ Renvoie la couleur de la carte 
        (parmi pique, coeur, carreau, trèfle). """
        couleurs = ['pique', 'coeur', 'carreau', 'trèfle']
        return couleurs[self.couleur - 1]

class Paquet_de_cartes:
    def __init__(self):
        """ Initialise l'attribut contenu avec une liste des 52
        objets Carte possibles rangés par valeurs croissantes en
        commençant par pique, puis cœur, carreau et trèfle. """
        self.contenu = []
        for i in range(1,5):
            for k in range(1,14):
                self.contenu.append(Carte(i, k))

    def recuperer_carte(self, pos):
        """ Renvoie la carte qui se trouve à la position pos 
        (entier compris entre 0 et 51). """
        assert pos > -1 and pos < 52, "pas bon"
        return self.contenu[pos]
        
jeu = Paquet_de_cartes()
# "8 de coeur"
carte1 = jeu.recuperer_carte(20)
carte1.recuperer_valeur() + " de " + carte1.recuperer_couleur()
carte2 = jeu.recuperer_carte(0)
    
# "As de pique"
carte2.recuperer_valeur() + " de " + carte2.recuperer_couleur()

# AssertionError : paramètre pos invalide
# carte3 = jeu.recuperer_carte(52)
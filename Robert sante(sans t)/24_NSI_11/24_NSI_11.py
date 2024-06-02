class Noeud:
    def __init__(self, etiquette):
        '''Méthode constructeur pour la classe Noeud.
        Crée une feuille d'étiquette donnée.'''
        self.etiquette = etiquette
        self.gauche = None
        self.droit = None

    def inserer(self, cle):
        '''Insère la clé dans l'arbre binaire de recherche
        en préservant sa structure.'''
        if cle < self.etiquette:
            if self.gauche != None:
                self.gauche.inserer(cle)
            else:
                self.gauche = Noeud(cle)
        else:
            if self.droit != None:
                self.droit.inserer(cle)
            else:
                self.droit = Noeud(cle) 

# bien se rappeler que le if et le else sont pareil juste le .gauche/droit change donc peut s'aider avec ca

arbre = Noeud(7)    
for cle in (3, 9, 1, 6):
    arbre.inserer(cle)
    
# 3
print(arbre.gauche.etiquette)

# 9
print(arbre.droit.etiquette)

# 1
print(arbre.gauche.gauche.etiquette)

# 6
print(arbre.gauche.droit.etiquette)
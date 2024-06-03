class Noeud:
    def __init__(self, etiquette, gauche, droit):
        self.v = etiquette
        self.gauche = gauche
        self.droit = droit

a = Noeud(1, Noeud(4, None, None), Noeud(0, None, Noeud(7, None, None)))

def taille(a):
    if a == None:
        return 0
    return 1 + taille(a.gauche) + taille(a.droit)

def hauteur(a):
    if a == None:
        return -1
    return 1 + max(hauteur(a.gauche), hauteur(a.droit))

    

# 4
print(taille(a))

# 0
print(taille(None))

# 1
print(taille(Noeud(1, None, None)))

# 0
print(hauteur(Noeud(1, None, None)))

# -1
print(hauteur(None))

# 2
print(hauteur(a))